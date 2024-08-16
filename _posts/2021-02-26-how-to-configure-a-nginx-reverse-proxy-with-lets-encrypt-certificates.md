---
layout: post
permalink: /1035/how-to-configure-a-nginx-reverse-proxy-with-lets-encrypt-certificates
title: How to configure a nginx reverse proxy with Let's Encrypt certificates
description: Let's Encrypt allows nginx reverse proxy servers to have a real, trusted
  SSL certificate, even for internal sites.
date: 2021-02-26 20:07:37 -0000
publish: true
pin: false
image:
  path: /assets/wp-content/uploads/2021/02/lets-encrypt-logo.webp
  alt: The Let's Encrypt logo
categories:
- How-to Guides
tags:
- guide
- "let's encrypt"
- nginx
- reverse proxy
- tutorial
- Unifi
---
The `certbot` utility by the Electronic Fronter Foundation (EFF) can use DNS
authentication to obtain, install, and renew free trusted SSL certificates on
a variety of web server configurations, including a nginx reverse proxy.

This configuration can be used on internal and external websites. It is
particularly useful in situations where you want to have a trusted certificate
for an internal web application without the time, effort, and risks of
creating and maintaining your own internal Certificate Authority (CA).

As an example, this guide will explain how to configure nginx with a trusted
certificate to act as a reverse proxy in front of a Unifi Controller.

## Install certbot

Let's Encrypt certificates expire every 90 days, so they would be a pain to
maintain without certbot handling the renewals automatically. Of course,
appliance servers like the Unifi Controller can't run certbot themselves. A
system running nginx can use certbot to automatically renew certificates for
itself, and pass the traffic transparently to the appliance by acting a a
reverse proxy.

While certbot can be found in the package repositories of most Linux
distributions, the EFF recommends using the snap release, because the snap
release is published directly by the EFF, so it is always the latest release.

First, [install snapd](https://snapcraft.io/docs/installing-snapd). It is
already installed on Ubuntu.

Remove any `certbot` packages you may have already installed on your system.

Then use `snapd` to install `certbot`.

```bash
sudo snap install core; sudo snap refresh core
sudo snap set certbot trust-plugin-with-root=ok
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
```

## Configure nginx to be a reverse proxy

Install nginx. For example, on Debian or Ubuntu servers run

```bash
sudo apt install -y nginx
```

If your upstream site (the site that nginx is in front of) uses a self-signed
SSL certificate, download a copy of the certificate. The easiest way to do
this is to visit the website in Google Chrome or Microsoft Edge (such as the
Unifi controller's HTTPS URL https://host:8443), click on the padlock on the
address bar, and click certificate. On Windows, click on the Details tab, then
`click Copy to file...`. Click next, and select Base-64 format. Save the
certificate, then upload it to the web server using SCP, and move it into a
proper directory, for example:

```bash
sudo mkdir /etc/nginx/ssl
sudo mv unifi.cer /etc/nginx/ssl
sudo chown root:root /etc/nginx/ssl/unifi.cer
sudo chmod u=rw,go=r /etc/nginx/ssl/cert/unifi.cer
```

Create a new file within `/etc/nginx/sites-available`

```bash
sudo nano /etc/nginx/sites-available/unifi.example.net
```

Add configuration details for a basic HTTP reverse proxy. `certbot` will add
the HTTPS configuration for you later.

If the upstream site is using plain HTTP and not HTTPS, omit the
`proxy_ssl_trusted_certificate` line.

```nginx
server {
    listen 80;
    listen [::]:80;
    server_name unifi.example.net;

    location / {
        proxy_pass https://127.0.0.1:8443;
        proxy_ssl_trusted_certificate /etc/nginx/ssl/unifi.cer;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

Save the file.

Enable the new configuration

```bash
ln -s /etc/nginx/sites-available/unifi.example.net /etc/nginx/sites-enabled/unifi.example.net
sudo service nginx reload
```

Next install the `certbot` plugin for your DNS provider. A list of DNS plugins
can be found [here](https://certbot.eff.org/docs/using.html#dns-plugins).
There, you will find links to specific instructions for each plugin/DNS
provider.

DNS is a reliable authentication method that `certbot` can use even if your
web server is not exposed to the public internet.

In this example we'll use Google DNS.

```bash
sudo snap install certbot-dns-google
```

Request a certificate for your domain/subdomain using `sudo certbot certonly`,
and pass in the configuration options required by your DNS plugin, according
to that plugin's documentation. The example below uses Google DNS.

```bash
sudo certbot certonly --dns-google --dns-google-credential /etc/letsencrypt/creds/google-dns-creds.json -d unifi.example.net
```

Once the certificate is acquired, use `certbot` to add SSL configuration to
the nginx configuration earlier.

```bash
sudo certbot --nginx  -d unifi.example.net
```

You will see output like this

```text
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Plugins selected: Authenticator nginx, Installer nginx
Cert not yet due for renewal

You have an existing certificate that has exactly the same domains or certificate name you requested and isn't close to expiry.
(ref: /etc/letsencrypt/renewal/unifi.example.net.conf)

What would you like to do?
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1: Keep the existing certificate for now
2: Renew & replace the certificate (may be subject to CA rate limits)
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
```

Select option 1.

Reload the configuration for nginx

```bash
sudo service nginx reload
```

Edit the renewal configuration file for the certificate

```bash
 sudo nano /etc/letsencrypt/renewal/unifi.example.net.conf
```

Under the `[renewalparams]` section, add the line

```ini
renew_hook = systemctl reload nginx
```

and save the changes to the file

This configures `certbot` to reload the nginx configuration after the
certificate has been renewed.
