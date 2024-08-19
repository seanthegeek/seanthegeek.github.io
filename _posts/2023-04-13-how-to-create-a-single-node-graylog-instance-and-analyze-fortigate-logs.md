---
layout: post
permalink: 1270/how-to-create-a-single-node-graylog-instance-and-analyze-fortigate-logs/
title: How to create a single-node Graylog instance and analyze FortiGate logs
description: A complete guide to creating a single-node Graylog instance, sending
  FortiGate firewall logs to it, and analyzing the data
date: 2023-04-13 19:51:33 -0000
last_modified_at: 2024-05-15 18:31:15 -0000
publish: true
pin: false
image:
  path: /assets/wp-content/uploads/2023/04/graylog-fortigate-dashboard-application-control.webp
  alt: The Application Control dashboard included in the FortiGate
    Syslog Content Pack for Graylog
categories:
- Information Security
- How-to Guides
tags:
- Forensics
- FortiGate
- Fortinet
- Graylog
- logging
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

Install the certbot [DNS plugin](https://eff-certbot.readthedocs.io/en/stable/using.html#dns-plugins) for your nameserver
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
