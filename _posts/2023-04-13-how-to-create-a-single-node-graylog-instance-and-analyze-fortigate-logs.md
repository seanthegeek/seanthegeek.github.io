---
layout: post
status: publish
published: true
title: How to create a single-node Graylog instance and analyze FortiGate logs
permalink: /how-to-create-a-single-node-graylog-instance-and-analyze-fortigate-logs/
description: 'A guide to creating a production-ready single node Graylog instance, and how it can be used to analyze logs FortiGate firewall logs.'
image:
  path: assets/images/graylog-fortigate-dashboard-application-control.png
wordpress_id: 1270
wordpress_url: https://seanthegeek.net/?p=1270
date: '2023-04-13 19:51:33 +0000'
date_gmt: '2023-04-13 19:51:33 +0000'
categories:
- Information Security
- How-to Guides
tags:
- FortiNet
- FortiGate
- DFIR
- SIEM
- Graylog
- logging
comments:
- id: 8377
  author: Abe
  author_url: https://academy.graylog.org
  date: '2023-04-17 03:17:38 +0000'
  date_gmt: '2023-04-17 03:17:38 +0000'
  content: "Great write-up man. \r\n\r\nCouple of notes:\r\n* You included a part
    where you used letsencrypt/acmebot but never updated your Nginx to use it \r\n\r\n*
    You also generated a self signed cert for TLS inputs but you can use the one you
    generated with acmebot!\r\n\r\n* I love the dashboards, did you make them all?
    \ Lastly, you used a Stream Rule for directing the traffic, I strongly recommend
    a pipeline rule.  Fire an email if you want a quick primer on how to do it. \r\n\r\nGreat
    work, I love it. \r\n\r\nAbe\r\nDirector PS &amp; Training\r\nGraylog"
- id: 8379
  author: Sean Whalen
  author_url: ''
  date: '2023-04-17 13:08:08 +0000'
  date_gmt: '2023-04-17 13:08:08 +0000'
  content: "Wow! word got around quickly.\r\n\r\n> * You included a part where you
    used letsencrypt/acmebot but never updated your Nginx to use it\r\nThe certbot
    --nginx command takes care of all of that for you\r\n\r\n> * You also generated
    a self signed cert for TLS inputs but you can use the one you generated with acmebot!\r\n\r\nLet's
    Encrypt Certificates expire every few months and need to be renewed often. certbot
    takes care of the renewal process automatically, including reloading the web server
    configuration at the end. It does support adding renewal hooks for adding more
    services, but for Graylog I was concerned about the impact of reloading/restarting
    a listener while logs are streaming in. You don't need to worry about any of that
    with a self-signed certificate.\r\n\r\n> * I love the dashboards, did you make
    them all? Lastly, you used a Stream Rule for directing the traffic, I strongly
    recommend a pipeline rule. Fire an email if you want a quick primer on how to
    do it. \r\n\r\nI just sent you an email."
- id: 8384
  author: Ervin
  author_url: ''
  date: '2023-04-20 09:11:54 +0000'
  date_gmt: '2023-04-20 09:11:54 +0000'
  content: "hey man ,\r\n\r\nfirst i wanted to say , thank you for the great work
    you've done.\r\n\r\nim trying to follow step by step the guide here :\r\nbut im
    ending with unreadable messages in Graylog :\r\nsimilar to this: �98��������Q=�5��+�/�����������\\�`�V�R�#�'g@�r�v���\t�32ED������P<�/A��\r\n\r\nmy
    first though was the encoding was wrong , but im not sure.\r\n\r\nthe only step
    im not doing is the TLS certificate , the communication happens in IP (so no FQDN
    is involved ), but i dont think this is problem , is it?\r\n\r\nlooking forward
    to hear from you\r\n\r\nbest regards\r\nErvin"
- id: 8386
  author: Peter
  author_url: ''
  date: '2023-04-20 21:06:13 +0000'
  date_gmt: '2023-04-20 21:06:13 +0000'
  content: "Great work here!\r\n\r\nOne thing to be aware of:  In Streams, I had to
    shorten the Fortigate Syslog stream rule from ^FGT to ^FG before it would catch
    logs from my FortiGate 101F hosts.  For some reason those devid fields start with
    FGT101FT.  A more inclusive regex expression might be ^FG([0-9]{2,3})[A-Z]T|^FGT"
- id: 8390
  author: Sean Whalen
  author_url: ''
  date: '2023-04-21 01:25:59 +0000'
  date_gmt: '2023-04-21 01:25:59 +0000'
  content: Definitely looks like an encoding issue, not a TLS issue. I'm not sure
    what the cause could be. Try reaching out to Fortinet support and the Graylog
    community forums.
- id: 8391
  author: Sean Whalen
  author_url: ''
  date: '2023-04-21 01:27:12 +0000'
  date_gmt: '2023-04-21 01:27:12 +0000'
  content: Thanks for the tip. I just pushed a new release with that regex pattern.
- id: 8394
  author: David
  author_url: ''
  date: '2023-04-21 15:41:49 +0000'
  date_gmt: '2023-04-21 15:41:49 +0000'
  content: "Hi Sean,\r\n\r\nThank you for sharing this!\r\n\r\nWe have some FortiGate's
    that are virtual, and the serial number starts with FGVM, do we just edit the
    file where it says FGT to FGVM? because we are not seeing the logs come in on
    the server.\r\n\r\nAlso, we are seeing on the graylog server, you have any idea
    what that means?\r\n\r\nERROR [AbstractTcpTransport] Error in Input [Syslog TCP/64403e99d67b386d1ca8a2fc]
    (channel [id: 0x75d1d980, L:/graylogserverIP:6514 ! R:/FTGVMFirewallIP:9540])
    (cause io.netty.handler.codec.DecoderException: javax.net.ssl.SSLHandshakeException:
    error:10000070:SSL routines:OPENSSL_internal:BAD_PACKET_LENGTH)"
- id: 8418
  author: Luis
  author_url: ''
  date: '2023-05-03 15:52:50 +0000'
  date_gmt: '2023-05-03 15:52:50 +0000'
  content: The fields of the logs I'm getting don't match the dashboard filters. FGT100F.
- id: 8434
  author: Mathieu
  author_url: ''
  date: '2023-05-10 21:19:00 +0000'
  date_gmt: '2023-05-10 21:19:00 +0000'
  content: "Hi Sean, got an issue pretty early on with the procedure.\r\n\r\nAfter
    doing this part : \r\nsudo curl -sL -o /etc/apt/trusted.gpg.d/opensearch.gpg https://artifacts.opensearch.org/publickeys/opensearch.pgp\r\necho
    \"deb https://artifacts.opensearch.org/releases/bundle/opensearch/2.x/apt stable
    main\" | sudo tee /etc/apt/sources.list.d/opensearch-2.x.list\r\n\r\nWhen I try
    to do the apt update, I get an error that the repository is unsigned along another
    error :\r\nGPG error: https://artifacts.opensearch.org/releases/bundle/opensearch/2.x/apt/dists/stable/inRelease:
    The keys in the keyring /etc/apt/trusted.gpg.d/opensearch.gpg are ignored as the
    file has an unsupported filetype.\r\n\r\nFresh install and followed without errors
    the guide up to that point.\r\n\r\nAny idea ?"
- id: 8451
  author: Edzilla
  author_url: ''
  date: '2023-05-17 07:10:26 +0000'
  date_gmt: '2023-05-17 07:10:26 +0000'
  content: "Hi, \r\nI had the same issue as David, so I tried disabling TLS (on both
    sides), now I have the same issue Ervin: \r\n�\r\nDid anyone find a solution?"
- id: 8491
  author: Ervin
  author_url: ''
  date: '2023-06-06 15:06:26 +0000'
  date_gmt: '2023-06-06 15:06:26 +0000'
  content: "it was an encryption problem. after fixing that it went straight forward.\r\none
    thing im not getting on the dashboard is the IPS from the fortigate. any idea?"
- id: 8529
  author: sebastian
  author_url: ''
  date: '2023-06-27 19:47:54 +0000'
  date_gmt: '2023-06-27 19:47:54 +0000'
  content: no traffic arrives to graylog, if I configure the tcp port with cef format
    it does arrive, but follow the steps in the guide and I can't get the traffic
    to arrive via tcp tls
- id: 8535
  author: Mark
  author_url: ''
  date: '2023-06-29 13:24:55 +0000'
  date_gmt: '2023-06-29 13:24:55 +0000'
  content: "Any idea how we get the DNS queries from our DNS filter into Graylog?
    We are seeing events on our fortigates but nothing is coming towards the Graylog.\r\n\r\nThanks!"
- id: 9175
  author: Massimo
  author_url: ''
  date: '2023-12-06 08:13:51 +0000'
  date_gmt: '2023-12-06 08:13:51 +0000'
  content: Hi, I've used your content pack for a while, but I noticed that all fields
    are string, so I can't make any Sum in dashboard (for example a table with sentbyte,
    rcvdbyte for every policy). Have I make something wrong?
- id: 9211
  author: cmmh
  author_url: ''
  date: '2023-12-13 18:25:23 +0000'
  date_gmt: '2023-12-13 18:25:23 +0000'
  content: After importing the content pack, I don't see an option in Editing the
    Stream forthe FortiGate Syslog index set; I only see the default index set.  Is
    there a way to debug why the index set is missing?
- id: 9326
  author: Jarett LeBlang
  author_url: ''
  date: '2024-01-17 16:58:36 +0000'
  date_gmt: '2024-01-17 16:58:36 +0000'
  content: 'TLS private key file: /etc/graylog/server/graylog-selfsigned.crt <---
    this is wrong. should be graylog-selfsigned.key'
- id: 9438
  author: Ryan
  author_url: ''
  date: '2024-02-13 17:30:16 +0000'
  date_gmt: '2024-02-13 17:30:16 +0000'
  content: Where you link to the json file should be https://raw.githubusercontent.com/seanthegeek/graylog-fortigate-syslog/1.3.3-rev12/content_pack.json
- id: 9491
  author: Sean Whalen
  author_url: ''
  date: '2024-02-25 00:29:54 +0000'
  date_gmt: '2024-02-25 00:29:54 +0000'
  content: I have it linked the way I do so it always points to the latest version.
- id: 9492
  author: Sean Whalen
  author_url: ''
  date: '2024-02-25 00:30:39 +0000'
  date_gmt: '2024-02-25 00:30:39 +0000'
  content: Fixed. Thanks!
- id: 9534
  author: JM
  author_url: ''
  date: '2024-03-11 20:16:27 +0000'
  date_gmt: '2024-03-11 20:16:27 +0000'
  content: Amazing! I will try next weekend. Regards from Brazil.
- id: 9596
  author: simon
  author_url: ''
  date: '2024-03-27 08:43:33 +0000'
  date_gmt: '2024-03-27 08:43:33 +0000'
  content: "Dear All,\r\nI recently had a graylog server on Linux and first input
    was my perimeter fortygate firewall . I was having issues installing the Fortigate
    content pack\r\nThanks to sean for the new revision FG content pack\r\nSo i create
    a Fresh Install of the below\r\nRocky Linux 8\r\ngraylog-enterprise-5.2.5-1.x86_64\r\nfortigate
    syslog content pack 1.6.5 rev 26\r\ngraylog-fortigate-syslog-pipeline 1.0.5 rev
    7\r\nI had no issues in the above install\r\n\r\nI have 2 fortigates 1500D HA
    active /active mode\r\n\r\nserial no of primary firewall is XXXX1477\r\nserial
    no of secondary firewall is XXXX1393\r\n\r\nNow what I see under streams tab is
    that no messages from the default stream get routed to the fortigate syslog Index
    set as shown in the attached picture .\r\nI also have only one input that is my
    fortygate syslog configured in my graylog server\r\nAttached is a sanpshot of
    my streams tab\r\nIf any more information is required please do ask i really appreciate
    it\r\n\r\nThanks and regards\r\n\r\nSimon"
- id: 9611
  author: tyo
  author_url: ''
  date: '2024-04-04 01:47:30 +0000'
  date_gmt: '2024-04-04 01:47:30 +0000'
  content: "Hi thank you this is very useful\r\nhow can i get count in size, on the
    dashboard ?"
- id: 9758
  author: Snis
  author_url: ''
  date: '2024-04-28 12:53:29 +0000'
  date_gmt: '2024-04-28 12:53:29 +0000'
  content: "Thank you for this!\r\n\r\nI tested this on Graylog 6.0.0-rc4 and it works!
    Only the indicies and retention settings that where different (ended up using
    \"legacy, deprecated\")."
- id: 9845
  author: Theo
  author_url: ''
  date: '2024-05-15 16:47:51 +0000'
  date_gmt: '2024-05-15 16:47:51 +0000'
  content: Hi, I am new to graylog and Fortigate and am currently building a SIEM
    based  on Wazuh. My 3 x nodes backend wazuh manager, 3x nodes graylog/mongodb
    cluster, 3x nodes wazuh manager cluster with nginx as a load balancer in fron
    are up and running. I can send logs from endpoints to graylog from wazuh managers
    with fluent-bit. I need to send Fortigate logs npw to graylog cluster via nginx
    loab balancer qhile still following this gaide in terms of enabling tls. Is it
    eveb something possible to do in the first place+
- id: 9880
  author: DPS
  author_url: ''
  date: '2024-05-20 07:51:37 +0000'
  date_gmt: '2024-05-20 07:51:37 +0000'
  content: "Hello sir, i got some error in graylog when trying to install new version
    content packs, can you take a look.\r\nInstalling content pack failed with status:
    FetchError: There was an error fetching a resource: Internal Server Error. Additional
    information: Failed constraints: [GraylogVersionConstraint{type=server-version,
    version=>=6.0.1+7218cba}]. Could not install content pack with ID: 85f976d9-4d2d-45f9-922d-25d2d9c11f87"
- id: 10448
  author: Muhammad Huzaifi
  author_url: ''
  date: '2024-07-15 08:47:05 +0000'
  date_gmt: '2024-07-15 08:47:05 +0000'
  content: "hello sir\r\nI tried following the steps. For application control, DNS
    Filter, Forward Traffic IPS, Local Traffic, Multicast Traffic, SSL/TLS/SSH Inspection,
    VPN and Web Filter the graph does not appear and does not work. I wonder why?"
- id: 10477
  author: Daniel
  author_url: ''
  date: '2024-07-17 08:18:30 +0000'
  date_gmt: '2024-07-17 08:18:30 +0000'
  content: "Hi Sean,\r\n\r\nthanks for this guide! \r\n\r\nMany URL and httpmethod
    fields are separated into their own fields due to = or ' in the address. How do
    you handle these logs? I haven't found a method to drop random fields.\r\nI'm
    currently redirecting these to a separate index so that other searches don't become
    slow.\r\n\r\nBest regards,\r\nDaniel"
- id: 10479
  author: Sean Whalen
  author_url: ''
  date: '2024-07-17 12:58:19 +0000'
  date_gmt: '2024-07-17 12:58:19 +0000'
  content: Make sure each of your firewall policies are configured to log all events.
- id: 10480
  author: Sean Whalen
  author_url: ''
  date: '2024-07-17 13:01:03 +0000'
  date_gmt: '2024-07-17 13:01:03 +0000'
  content: I ran into the same problem and fixed it by creating a pipeline to set
    the data types correctly for new incoming traffic. https://github.com/seanthegeek/graylog-fortigate-syslog-pipeline
- id: 10481
  author: Sean Whalen
  author_url: ''
  date: '2024-07-17 13:03:54 +0000'
  date_gmt: '2024-07-17 13:03:54 +0000'
  content: That error says you need to use Graylog version 6.0.1 or later.
- id: 10482
  author: Sean Whalen
  author_url: ''
  date: '2024-07-17 13:07:02 +0000'
  date_gmt: '2024-07-17 13:07:02 +0000'
  content: Hmmm. I'm not sure. I've never run into that problem because I don't decrypt
    HTTPS traffic (so no URIs/URLs get logged), It would be worth asking on the Graylog
    forums. Let me know if you find a solution. I might be able to include it in a
    content pack.
---
Firewall logs provide a wealth of information about a network. They can be
used to identify devices, troubleshoot policies, and even help determine the
impact of a cyber attack. Graylog is a powerful open source log collection and
analysis platform that is well-suited for managing firewall logs. This guide
explains how to create a production-ready single node Graylog instance with
bidirectional authentication to the firewalls, and how it can be used to
analyze FortiGate firewall logs with premade dashboards.

Check out the presentation I made on this topic
[here](https://1drv.ms/p/s!Ak-0erEu9-tbgrYCRtQXqN-rFyXuyA?e=kn9lpo).

Download the Debian [ISO](https://www.debian.org/download) and create a
bootable flash drive using [Rufus](https://rufus.ie/en/). At the time of this
writing. the latest stable release is Debian 12, codename bookworm. Install
Debian on a dedicated workstation or server by booting from the flash drive
and selecting the non-graphical install option. Follow the prompts to set the
system keyboard, hostname, root password (make sure you remember what you set
that to!), standard user account, time zone, and system partitions. When you
reach the "select and install software" step, use the arrow keys and spacebar
to deselect Debian Desktop Environment and GNOME, and select SSH server for
remote shell access.

Sign in with your standard account, then switch to the root user using the su
command.

```bash
su -
```

Add your standard user account to the sudo group, so you can use the sudo
command to run commands as root without having to switch accounts (replace
username with your actual standard account username).

```bash
usermod -aG sudo username
```

Run the exit command twice to log out, then log back in for the change to take
effect.

A Graylog node requires two dependencies: MongoDB and OpenSearch.

## Install Graylog dependencies

Run the following commands to install MongoDB Community Edition.

Note: MongoDB does not support Debian 12 "Bookworm" because it requires
libssl1.1, which is only available in Debian 11 "Buster". A workaround is to
use the MongoDB package repository for Ubuntu 22.04 Jammy Jellyfish.

```bash
sudo apt-get install -y gnupg curl
curl -fsSL https://pgp.mongodb.com/server-7.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg    --dearmor
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
sudo apt-get update
sudo apt-get install -y mongodb-org
sudo systemctl daemon-reload
sudo systemctl enable mongod.service
sudo systemctl restart mongod.service
```

Run the following commands to install OpenSearch.

```bash
curl -o- https://artifacts.opensearch.org/publickeys/opensearch.pgp | sudo gpg --dearmor --batch --yes -o /usr/share/keyrings/opensearch.pgp
echo "deb [signed-by=/usr/share/keyrings/opensearch.pgp] https://artifacts.opensearch.org/releases/bundle/opensearch/2.x/apt stable main" | sudo tee /etc/apt/sources.list.d/opensearch-2.x.list
sudo apt update
sudo OPENSEARCH_INITIAL_ADMIN_PASSWORD=$(tr -dc A-Z-a-z-0-9_@#%^-_=+ < /dev/urandom  | head -c${1:-32}) apt-get -y install opensearch
```

## Configure OpenSearch

Before starting OpenSearch, it must be properly configured. The nano command
is a CLI text editor that is friendly for new users. Use nano to edit the
OpenSearch configuration file.

```bash
sudo nano /etc/opensearch/opensearch.yml
```

Most of the options can be kept at their default values.

Set the cluster name to graylog.

```yaml
cluster.name: graylog
```

In the network section, configure OpenSearch to listen on the loopback
interface.

```yaml
network.host: 127.0.0.1
```

Add the discovery type in the discovery section.

```yaml
discovery.type: single-node
```

Add these options in the various section.

```yaml
action.auto_create_index: false
plugins.security.disabled: true
```

Add this setting at the bottom of the file.

```yaml
# Custom settings
search.max_buckets: 200000
```

Save the changes to the file by pressing ctrl-o, and then enter. Press ctrl-x
to exit nano.

The JVM heap limits for OpenSearch must be set to half the size of the system
memory.

```bash
sudo nano /etc/opensearch/jvm.options
```

For example, if your system has 16 GB of RAM, use the following settings.

```text
-Xms8g
-Xmx8g
```

The `-Xms` and `-Xmx` values must be identical.

Save the changes to the file by pressing ctrl-o, and then enter. Press ctrl-x
to exit nano.

Configure kernel parameters by running the following commands.

```bash
sudo sysctl -w vm.max_map_count=262144
echo 'vm.max_map_count=262144' | sudo tee -a /etc/sysctl.conf
```

Start OpenSearch by running the following commands.

```bash
sudo systemctl daemon-reload
sudo systemctl enable opensearch
sudo systemctl start opensearch
```

## Install Graylog

Run the following commands to install Graylog.

```bash
wget https://packages.graylog2.org/repo/packages/graylog-6.0-repository_latest.deb  
sudo dpkg -i graylog-5.2-repository_latest.deb  
sudo apt-get update && sudo apt-get install graylog-server
```

## Configure Graylog

Edit the Graylog configuration file.

```bash
sudo nano /etc/graylog/server/server.conf
```

The password_secret value must be random. To generate a random secret, open a
new terminal session in a separate window, and run the following commands.

```bash
sudo apt install -y pwgen
pwgen -N 1 -s 96
```

The password for the Graylog root user is stored in the configuration file as
a SHA256 hash. To generate the hash, use the second open terminal and run the
following command.

**Warning** : The password will be displayed in plain text as you type it.
Make sure no one is watching your screen.

```bash
echo -n "Enter Password: " && head -1 </dev/stdin | tr -d '
' | sha256sum | cut -d" " -f1
```

Leave the `http_bind_address` option commented out to keep it at its default
value.

Set `http_publish_url` to the HTTPS URL that will be used to access Graylog. For
example, https://graylog.example.com/

Set `elasticsearch_hosts` to `https://127.0.0.1:9200`. The configuration file
says this is the default value, but I have found that it must be explicitly
set or Graylog will not find any data nodes.

Use the `ctrl-w` command in nano to locate the allow_leading_wildcard_searches
option. Set `allow_leading_wildcard_searches` and `allow_highlighting` to
`true`.

Save the changes to the file by pressing `ctrl-o`, and then enter. Press
`ctrl-x` to exit nano.

Start Graylog by running the following commands.

```bash
sudo systemctl daemon-reload
sudo systemctl enable graylog-server
sudo systemctl start graylog-server
```

This will start a setup web interface, which is different than the normal web
interface and uses different credentials. Even the root credentials you
configured in server.conf will not work.

## Configure NGINX as a reverse proxy

Graylog's HTTP interfaces are configured by default to only bind to `127.0.0.1`.
That's a good thing for security. NGINX can be used as a reverse proxy to
accept HTTPS connections and route them to Graylog over the loopback
interface.

Install NGINX using the following command.

```bash
sudo apt install -y nginx
```

Disable the default NGINX configuration.

```bash
sudo rm /etc/nginx/sites-enabled/default
```

Create a new NGINX configuration for Graylog. Replace graylog.example.com with
the actual hostname that you will use to access Graylog in a web

```bash
sudo nano /etc/nginx/sites-available/graylog
```

```nginx
server
{
    listen 80 default_server;
    listen [::]:80 default_server ipv6only=on;
    server_name graylog.example.org;

    location / {
      proxy_set_header Host $http_host;
      proxy_set_header X-Forwarded-Host $host;
      proxy_set_header X-Forwarded-Server $host;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header X-Graylog-Server-URL https://$server_name/;
      proxy_pass https://127.0.0.1:9000;
    }
}
```

Enable the new NGINX configuration and restart NGINX.

```bash
sudo ln -s /etc/nginx/sites-available/graylog /etc/nginx/sites-enabled/graylog  
sudo service nginx restart
```

## Deploy HTTPS on NGINX with Let's Encrypt DNS verification

Let's Encrypt is a non-profit [Certificate
Authority](https://letsencrypt.org/) that uses automation to verify domain
ownership and issue free certificates that are honored by browsers and
devices. The Electronic Frontier Foundation (EFF) created a tool called
[certbot](https://eff-certbot.readthedocs.io/) that automatically obtains
Let's Encrypt certificates, configures popular server software to use them,
and manages the certificate renewal process.

To obtain a certificate without exposing a web server to the internet, certbot
has a variety of DNS plugins for many DNS nameserver hosting providers. These
plugins use API credentials to add a TXT record to a DNS zone, which is then
checked by Let's Encrypt to verify domain ownership before issuing a
certificate. You do not need to add a hostname to the public DNS zone.
Instead, create an A record in a shadow DNS zone for your domain on a DNS
server on the local network. That way, local systems can find the local IP
address of the Graylog server.

Run the following commands to install certbot.

```bash
sudo apt install -y snapd  
sudo snap install core  
sudo snap install certbot  
sudo snap set certbot trust-plugin-with-root=ok  
```

Install the certbot [DNS plugin](https://eff-
certbot.readthedocs.io/en/stable/using.html#dns-plugins) for your nameserver
hosting provider. For example, for GCP DNS run the following command.

```bash
sudo snap install certbot-dns-google
```

Follow the documentation of the plugin and run the `certbot certonly` command to
obtain a certificate. The exact process and command arguments will vary
depending on the plugin being used. Follow the documentation for that plugin.
For example, to obtain a certificate for a domain with DNS nameservers hosted
in GCP, the following command could be used.

```bash
sudo certbot certonly --dns-google -d graylog.example.com --dns-google-credentials gcp-dns-credentials.json
```

Once the certificate has been obtained, have certbot configure HTTPS on NGINX
by running the following command. Replace graylog.example.com with the actual
HTTPS hostname of the Graylog server.

```bash
sudo certbot --nginx -d graylog.example.com
```

certbot will state that a certificate already exists. Select the `Attempt to
reinstall this existing certificate` option.

Congratulations! You now have a working single-node Graylog server with HTTPS
configured. Log into Graylog using the Graylog root account that was
configured earlier.

## Create a FortiGate Syslog index set

In the Graylog web interface, navigate to System> Indices. Create an index set
called FortiGate Syslog. Set a time-based index rotation of one day (P1D) and
base the retention on the number on the number of days (i.e., indices) that
you what to retain.

## Install the FortiGate Syslog content packs

I have created two Graylog content packs for FortiGate syslog data. The first
content pack, ([FortiGate syslog](https://github.com/seanthegeek/graylog-
fortigate-syslog)) contains a stream and dashboard. A stream tells Graylog
what data to direct to a particular index set or pipeline. Searches can also
be filtered by stream. After you install the first content pack install the
[Graylog syslog pipeline](https://github.com/seanthegeek/graylog-fortigate-
syslog-pipeline) content pack. This installs a pipeline that sets fields used
by the dashboard to their proper datatype and removes redundant fields. The
full original message is still available in the message field.

## Configure the FortiGate Syslog stream to use the FortiGate Syslog index set

Once you have created the index set and installed the content packs, navigate
to Streams, edit the FortiGate Syslog stream, select the FortiGate Syslog
index set you created, and click Update Stream.

## Prepare Graylog to accept logs from FortiGate firewalls

Create a self-signed certificate for accepting logs over TLS.

```bash
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/graylog/server/graylog-selfsigned.key -out /etc/graylog/server/graylog-selfsigned.crt
sudo chown graylog /etc/graylog/server/graylog-selfsigned.key
sudo chown graylog /etc/graylog/server/graylog-selfsigned.crt
```

Use a file transfer tool like [Cyberduck](https://cyberduck.io/) to transfer a
copy of the certificate at /etc/graylog/server/graylog-selfsigned.crt to your
local system over SFTP. Log into your FortiGate web interface. Import the
certificate to the FortiGate as a Remote CA certificate by navigating to
System> Certificates> Create/Import> CA Certificate> File.

While still at the Certificates page, download a copy of the root CA
certificate used by the firewall, which is named Fortinet_CA_SSL by default.
This will be used by the Graylog server to authenticate the connection from
the firewall, so unauthorized devices cannot send logs to the Graylog server.
Use a file transfer tool to upload the certificate to the server, then run the
following commands to move the certificate into place.

```bash
sudo mkdir -p /etc/graylog/server/trustedcerts.d  
sudo mv Fortinet_CA_SSL.cer /etc/graylog/server/trustedcerts.d  
sudo chown graylog -R /etc/graylog/server/trustedcerts.d  
sudo chmod ugo=rX -R /etc/graylog/server/trustedcerts.d
```

**Note** : A previous version of this guide attempted to use the CEF log
format. That turned out to be very buggy, so this content has been updated to
use the default Syslog format, which works very well.

In Graylog, navigate to System> Indices. Create a new index for FortiGate logs
with the title FortiGate Syslog, and the index prefix fortigate_syslog.
Configure the index rotation and retention settings to match your needs. For
example, to retain a year of logs set the rotation period to P1D and set the
max number of indices to 365.

Download the FortiGate Syslog Graylog content pack JSON file by right-clicking
on [this link](https://github.com/seanthegeek/graylog-fortigate-
syslog/raw/1.0.0-rev1/content_pack.json) and clicking "Save link as." Be sure
to add yourself as a watcher to the [GitHub
project](https://github.com/seanthegeek/graylog-fortigate-syslog) to be
notified of new Content Pack releases that fix bugs or add more features.

In Graylog, navigate to System> Content Packs. Click Upload, choose the
content_pack.json file, and click Upload. Click Install across from the
FortiGate Syslog content pack in the list of content packs.

Navigate to Streams. Edit the FortiGate Syslog stream by clicking on More
Actions> Edit Stream. Select the FortiGate Syslog index set, make sure "Remove
matches from 'Default Stream'" is checked, and Click Update Stream.

Navigate to System> Inputs. Launch a new Syslog TCP input.

```text
Title: Syslog TCP
Bind address: 0.0.0.0
Port: 6514
Time zone: GMT
TLS cert file: /etc/graylog/server/graylog-selfsigned.crt
TLS private key file: /etc/graylog/server/graylog-selfsigned.key
Enable TLS: True
TLS client authentication: Required
TLS Client Auth Trusted Certs: /etc/graylog/server/trustedcerts.d
```

## Configure FortiGate to send logs to Graylog

Use the CLI to configure the FortiGate.

To simplify and unify log management, it is important that every firewall be
configured to use the GMT time zone, which for logging purposes is equivalent
UTC. This ensures that times are consistent regardless of a firewall's
geographic location, or local factors such as daylight savings.

```text
config system global
    set timezone "Etc/GMT"
end
```

By default, logs sent to the syslog server are not filtered. To ensure that
the Graylog Input gets all logs, reset all log filter options to their default
settings.

```text
config log syslogd filter
    unset severity
    unset forward-traffic
    unset local-traffic
    unset multicast-traffic
    unset sniffer-traffic
    unset anomaly
    unset voip
end
```

Finally, configure the syslog output over TLS in Syslog format.

```text
config log syslogd setting
    set status enable
    set server "graylog.example.com"
    set mode reliable
    set port 6514
    set format default
    set enc-algorithm high
    set certificate "Fortinet_CA_SSL"
end
```

Logs will begin to appear in your Graylog server.

## Patching the server

To update all software on the server run the following command.

```bash
sudo apt update && sudo apt-dist upgrade -y && sudo apt autoremove -y
```

Server application updates do not take effect until the service is restarted.
Linux kernel or firmware updates do not take effect until the system is
rebooted. Stop the graylog-server service before restarting the mongodb or
opensearch services, then start the graylog service again.

```bash
sudo service stop graylog-server  
sudo service restart mongodb  
sudo service restart opensearch  
sudo service start graylog-server  
sudo service nginx restart
```

**Note** : NGINX will return an HTTP 504 Bad Gateway error until Graylog fully
starts.

## Adding users

To add users to Graylog navigate to System> Users. User authentication via
Active Directory or LDAP can be configured by navigating to System>
Authentication. Check out the [authentication
documentation](https://go2docs.graylog.org/5-0/setting_up_graylog/permission_management.html)
for more details.

## Querying data

Log entries are called messages. Clicking on a result in a message table will
show you all of the fields and values of that message. Clicking on any value
in a dashboard or message will offer to temporarily include or exclude that
value in the search filter. The time picker can be used to narrow the
timeframe of search results and temporarily override the time window of
dashboard widgets.

Graylog provides a powerful [query
syntax](https://docs.graylog.org/docs/query-language) to provide more specific
results.

One important difference between Graylog and other search engines is that
Graylog does not search for substrings unless wildcards are explicitly used.
For example, searching for google.com will only return results for connections
to google.com, and not any google.com subdomains. To search for google.com and
google .com subdomains, use *google.com. Likewise, to search for a substring,
surround it with wildcards, such as *example*.

## Commercial features

Graylog offers a commercial SIEM
[product](https://www.graylog.org/products/security/) called Graylog Security
that includes features such as anomaly detection.
