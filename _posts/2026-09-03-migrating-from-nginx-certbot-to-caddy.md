---
layout: post
title: Migrating from NGINX + Certbot to Caddy
description: "How I replaced NGINX and Certbot with a single Caddyfile: a Caddy reverse proxy with automatic Let's Encrypt TLS, Cloudflare DNS-01, and a hardened systemd service."
image:
  path: assets/images/caddy.webp
  alt: The Caddy logo
category: Guides
tags: Caddy, Caddyfile NGINX, certbot, Let's Encrypt
date: 2026-09-03 16:33 -0400
---
Caddy is a [web server written in Go](https://caddyserver.com/) that obtains and maintains Let's Encrypt TLS certificates automatically. It also has excellent reverse proxy configuration defaults, so much so that I was able to replace [NGINX and `certbot`](https://seanthegeek.net/posts/how-to-run-multiple-web-services-behind-one-public-ip-address/) and multiple large configuration files with a single, simple Caddyfile.

To give a sense of what I mean, here is an example of a Caddyfile for a Caddy server on the edge of a network that routes traffic to various applications behind one public IP address based on hostname **and** allows those backend servers to have their own publicly trusted TLS certificates with no additional configuration. It uses the [`caddy-dns/cloudflare`](https://github.com/caddy-dns/cloudflare) module to obtain Let's Encrypt TLS certificates for itself using the [ACME `DNS-01`](https://letsencrypt.org/docs/challenge-types/#dns-01-challenge) challenge, and proxies [ACME `HTTP-01`](https://letsencrypt.org/docs/challenge-types/#http-01-challenge) challenges to backend servers. This is great because it means that only the server running Caddy on the edge needs the sensitive API token that manages public DNS records, and you can continue to use hardware and software that only allows `HTTP-01` verification to obtain certificates, even on internal servers.

This configuration assumes an internal DNS server or a customized `/etc/hosts` file is in use on the Caddy host so that backend hostnames resolve to their internal addresses.

```caddyfile
# Catch-all
http:// {
        respond 404
}

# importable config snippet keeps the config nice and DRY

# Proxy ACME HTTP-01 challenges for internal and public-facing apps
(acme_relay) {
        handle /.well-known/acme-challenge/* {
                reverse_proxy {args[0]}:80
        }
        respond 404
}

http://gateway.example.net {
        import acme_relay gateway.example.net
}

http://pbx.example.net {
        import acme_relay pbx.example.net
}

http://unifi.example.net {
        import acme_relay unifi.example.net
}

http://graylog.example.net {
        import acme_relay graylog.example.net
}

http://sandbox.example.net {
        import acme_relay sandbox.example.net
}

http://nextcloud.example.net {
        import acme_relay nextcloud.example.net
}

# Proxy public-facing apps
(cloudflare_tls) {
        tls {
                dns cloudflare {env.CF_API_TOKEN}
                resolvers 1.1.1.1 # Use public DNS when checking for the challenge record
        }
}

sandbox.example.net {
        import cloudflare_tls
        reverse_proxy https://sandbox.example.net
}

nextcloud.example.net {
        import cloudflare_tls
        reverse_proxy https://nextcloud.example.net
}

```

For comparison, here is the same reverse proxy NGINX configuration with Certbot for just **one** of those sites.

```nginx
server {

server_name nextcloud.example.net;

# Proxy ACME HTTP-01 challenges to the backend
location /.well-known/acme-challenge/ {

proxy_pass http://nextcloud.example.net;

proxy_set_header Host $host;
proxy_set_header X-Forwarded-Proto $scheme;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
}


location / {
proxy_pass https://nextcloud.example.net;

proxy_set_header Host $host;
proxy_set_header X-Forwarded-Proto $scheme;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

# set max upload size and increase upload timeout:
client_max_body_size 512M;
client_body_timeout 300s;
fastcgi_buffers 64 4K;

# This setting allows you to optimize the HTTP2 bandwidth.
# See https://blog.cloudflare.com/delivering-http-2-upload-speed-improvements/

# for tuning hints
client_body_buffer_size 512k;
}


listen [::]:443 ssl; # managed by Certbot
listen 443 ssl; # managed by Certbot

ssl_certificate /etc/letsencrypt/live/nextcloud.example.net/fullchain.pem; # managed by Certbot
ssl_certificate_key /etc/letsencrypt/live/nextcloud.example.net/privkey.pem; # managed by Certbot
include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
}

server {
if ($host = nextcloud.example.net) {
return 301 https://$host$request_uri;
} # managed by Certbot

listen 80;
listen [::]:80;
server_name nextcloud.example.net;

return 404; # managed by Certbot
}
```

## Installing Caddy

Caddy is a self-contained Go binary. Extra features must be added at build time. This can be done from the [download page](https://caddyserver.com/download), but I prefer to build it myself using [`xcaddy`](https://github.com/caddyserver/xcaddy).

```bash
sudo apt install golang
go install github.com/caddyserver/xcaddy/cmd/xcaddy@latest
```

This will install `xcaddy` in `~/go/bin/xcaddy`.

For example, to build the latest version of `caddy` with the module `caddy-dns/cloudflare`:

```bash
~/go/bin/xcaddy build --with github.com/caddy-dns/cloudflare
```

Tip: You can add multiple modules by adding multiple `--with` arguments.

Then change file ownership of the generated `caddy` binary to `root`, and move it to `/usr/bin`.

```bash
sudo chown root:root caddy
sudo mv caddy /usr/bin
```

Then test that it worked.

```bash
caddy version
```

Next, create a directory for storing the config.

```bash
sudo mkdir /etc/caddy
```

Once you have created your Caddyfile, change ownership, and move it into place.

```bash
sudo chown root:root Caddyfile
sudo mv Caddyfile /etc/caddy
```

## Running Caddy as a systemd service

A common way to run Caddy is as a systemd service.

Create the `caddy` system group.

```bash
sudo groupadd --system caddy
```

Create the `caddy` system user.

```bash
sudo useradd --system \
--gid caddy \
--create-home \
--home-dir /var/lib/caddy \
--shell /usr/sbin/nologin \
--comment "Caddy web server" \
caddy
```

Create an environment file for storing secrets. It must be owned by and readable only by `root`, not the `caddy` user. The environment file configured by `EnvironmentFile=` is loaded by systemd before the service process is executed, so the service user never needs access to the file.

```bash
sudo touch /etc/caddy/caddy.env
sudo chmod 0600 /etc/caddy/caddy.env
```

Secrets like `CF_API_TOKEN` can be placed in this file in this format:

```dotenv
CF_API_TOKEN=value
SOME_OTHER_TOKEN=value
```

Create the service unit file at `/etc/systemd/system/caddy.service`.

```systemd
[Unit]
Description=Caddy
Documentation=https://caddyserver.com/docs/
After=network.target network-online.target
Requires=network-online.target

[Service]
Type=notify
User=caddy
Group=caddy
ExecStart=/usr/bin/caddy run --config /etc/caddy/Caddyfile
ExecReload=/usr/bin/caddy reload --config /etc/caddy/Caddyfile --force
TimeoutStopSec=5s
LimitNOFILE=1048576
PrivateTmp=true
ProtectSystem=full
AmbientCapabilities=CAP_NET_ADMIN CAP_NET_BIND_SERVICE
EnvironmentFile=/etc/caddy/caddy.env

[Install]
WantedBy=multi-user.target
```

This differs from the Caddy project's [example unit file](https://github.com/caddyserver/dist/blob/master/init/caddy.service) in two key ways:

- `--environ` is not included in the `ExecStart` value, because that switch logs the environment (including secrets) to the journal
- `EnvironmentFile=/etc/caddy/caddy.env` is added

Enable and start the new service.

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now caddy
```

Verify that it is running.

```bash
sudo systemctl status caddy
```

## Upgrading Caddy

Like any other software, Caddy and its modules must be kept up to date to stay secure. The one downside of manually installing Caddy is that upgrades won't happen via `apt` or `dnf`. You are responsible for building and installing upgraded versions.

1. Build a new `caddy` binary using `xcaddy`
2. Change `caddy` file ownership to `root` with `sudo chown root:root caddy`
3. Run `sudo mv caddy /usr/bin` to replace the existing binary
4. Run `sudo systemctl restart caddy` to restart the service

The Caddy CLI does list an `upgrade` command, but it is labeled `[EXPERIMENTAL]`, and there has been discussion of [removing it](https://github.com/caddyserver/caddy/issues/7010).

You can use GitHub watchers to receive notifications of new releases and security alerts. This requires a GitHub account, which is free. Go to the [Caddy project on GitHub](https://github.com/caddyserver/caddy), click on the dropdown next to Watch, click Custom, check Releases and Security Alerts, then click Apply. This allows you to keep an eye out for new releases and security alerts without the noise of issue, pull request, or discussion notifications. Do the same for each Caddy module that you use.
