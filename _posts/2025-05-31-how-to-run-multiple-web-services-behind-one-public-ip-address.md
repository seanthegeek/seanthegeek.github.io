---
layout: post
title: How to run multiple web services behind one public IP address
description: With nginx, a domain name, and Let's Encrypt, all internal and external-facing web applications can use HTTPS — even on a home network
image:
  path: "/assets/images/nginx-logo.png"
  description: The nginx logo
categories:
- Guides
tags:
- nginx
- Let's Encrypt
- Home lab
- DNS
date: 2025-05-31 19:42 -0400
---
One of the most popular use cases for nginx (pronounced Engine X) is to to act as a reverse proxy that takes requests from web clients and proxies them to application webservers. You can configure your firewall/router to forward TCP ports 80 (for HTTP) and 443 (for HTTPS) to a server running nginx, and nginx be configured to proxy incoming web requests to the correct webserver based on the hostname in the web request. Each application will also use nginx as its webserver. Let's Encrypt TLS certificates can provide certificates that protect traffic to the edge webserver and between the edge webserver and the internal webservers, and between internal clients and the internal webservers.

## Let's Encrypt

Let's Encrypt is a Certificate Authority (CA) that issues free TLS certificates. It uses the [ACME protocol](https://datatracker.ietf.org/doc/html/rfc8555) to verify control of a domain before issuing a certificate. There are two methods of verification: the HTTP challenge and the DNS challenge. For the HTTP challenge, the ACME client temporally places a file at a path specified by the ACME server under `/.well-known/acme-challenge/`. The ACME server then checks if this file and issues the certificate if it exists.

In DNS challenge, the ACME client temporally adds a `TXT` DNS record to the domain at `_acme-challenge`, waits a few seconds for the DNS changes to propagate, then the ACME server checks if the record exists before issuing the certificate.

In this guide, we'll use [certbot](https://certbot.eff.org/) as the ACME client to verify domains on the edge webserver using DNS, and via HTTP on the application webservers. If a web application needs to be public facing, we'll configure the edge webserver to proxy all web traffic for that domain to the application server. But, if a web a web application is for internal use only, we'll configure the edge webserver to only forward traffic for the ACME HTTP verification path and return `HTTP 404 Not Found` for any other path. This architecture has a few advantages. Credentials for modifying DNS records are only located on one webserver, rather than every webserver, even if a web application is not public facing, and internal only applications can use the HTTP challenge without the application being publicly exposed.

## DNS configuration

To make this architecture work, you'll need:

- A registered domain name pointed to DNS nameservers [supported by certbot](https://eff-certbot.readthedocs.io/en/stable/using.html#dns-plugins)
- A [DNS server](https://en.wikipedia.org/wiki/Comparison_of_DNS_server_software) on your local network that hosts with non-authoritative DNS zones that point to internal IP addresses
  - Many firewalls have the ability to configure an internal DNS server
  - Alternatively, the hostnames could be added to the [hosts file](https://en.wikipedia.org/wiki/Hosts_(file)) of the edge webserver
  - A static public IP address or a [dynamic DNS](https://www.howtogeek.com/866573/what-is-dynamic-dns-ddns-and-how-do-you-set-it-up/) hostname pointing to a dynamic public IP address
    - Some firewalls/router manufacturers offer their own Dynamic DNS service for free

Configure your hostnames for all web applications in both internal and external DNS zones, even if they are internal-only applications.

In this guide we'll use `example.net` as our domain.

### External DNS

Configure a DNS record for `web.example.net` that points to the public address of your edge webserver

- Use an `A` record if you have an IPv4 public IP address
- Use an `AAAA` record if you have an IPv6 public IP address
- Use a `CNAME` record if you are using a dynamic DNS hostname

Next, configure a `CNAME` record for each web application hostname you'll use, and point it to `web.example.net`. This way, if you ever need to change the public IP address for the webserver, you only need to do it for `web.example.net`.

### Internal DNS

Configure your internal DNS server or hosts file on your webserver so that the same hostnames configured in external DNS point to each individual internal IP address of the server that is hosting the application. This way, the edge webserver will proxy requests to the correct internal systems, instead of to itself.

## Install certbot

Install certbot on all webservers. Instructions for installing certbot can be found on the [project's website](https://certbot.eff.org/).

This guide will show how to install certbot on a Debian or Ubuntu server using `snapd`.

```bash
sudo apt update
sudo apt install snapd
sudo snap install snapd
sudo snap install --classic certbot
```

## Configure the edge webserver to proxy traffic to internal webservers

Create a nginx configuration file for each hostname. On Debian or Ubuntu servers, for example run:

```bash
sudo nano /etc/nginx/sites-available/internal.example.net
```

Other Linux distributions may store nginx configuration files in `/etx/nginx/conf.d/`.

### Internal-only applications

```nginx
server {
    listen 80;
    listen [::]:80;
    server_name internal.example.net;

    location /.well-known/acme-challenge/ {
        proxy_pass http://internal.example.net;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location / {
        return 404;
    }
}
```

### External-facing applications

```nginx
server {
    listen 80;
    listen [::]:80;
    server_name external.example.net;

    location / {
        proxy_pass http://external.example.net;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

For external-facing applications, you add the same nginx configuration options that you do in the application's web server configuration (e,g, `client_max_body_size`).

### Enable the configuration

On Debian or Ubuntu systems, you must add a symlink for each configuration file for it to apply.

```bash
sudo ln -s /etc/nginx/sites-available/internal.example.net /etc/nginx/sites-enabled/internal.example.net
udo ln -s /etc/nginx/sites-available/external.example.net /etc/nginx/sites-enabled/external.example.net
```

Restart the server to apply the configuration changes.

```bash
sudo service nginx restart
```

## Obtain TLS certificates on the edge webserver

Use a certbot [DNS plugin](https://eff-certbot.readthedocs.io/en/stable/using.html#dns-plugins) to obtain certificates for the edge webserver using the DNS challenge.

## Configure nginx to use Let's Encrypt certificates

On the external webserver, run:

```bash
sudo certbot -d internal.example.com -d external.example.com --nginx
```

Use as many `-d` arguments as needed for each domain.

And confirm that you want to use the existing certificates that you obtained with the last command.

Run the same command on each application server. The HTTP challenge request should be successfully routed through the edge webserver and pass.

## Update the edge web server to proxy using HTTPS

Once an application server has successfully passed the HTTP challenge and obtained a TLS certificate, change the corresponding nginx configuration on the edge web server for that application to use `https` instead of `http` in the `proxy_pass` option and restart or reload nginx. Otherwise, a redirect loop will occur, resulting in a `Too many redirects` error.
