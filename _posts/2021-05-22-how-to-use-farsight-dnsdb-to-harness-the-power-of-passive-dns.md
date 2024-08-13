---
layout: post
status: publish
published: true
title: How to use Farsight Security's DNSDB to harness the power of passive DNS
permalink: /1122/how-to-use-farsight-dnsdb-to-harness-the-power-of-passive-dns/
description: "A guide to using the dsbdb-python Python module to perform forward and inverse queries on passive DNS data in Farsight Security's DNSDB"
wordpress_id: 1122
wordpress_url: https://seanthegeek.net/?p=1122
date: '2021-05-22 21:30:16 +0000'
date_gmt: '2021-05-22 21:30:16 +0000'
categories:
- Information Security
- How-to Guides
tags:
- DNS
- OSINT
- recon
- pentesting
comments: []
---
DNS describes the [structure](https://seanthegeek.net/1117/an-introduction-to-
dns/) of resources on the internet. It can provide lots of valuable
information about (attacker or target) infrastructure. However, in order to
query DNS records, you must already know the exact domains or subdomains to
query. When examining unknown infrastructure, this is not practical. On top of
that, DNS records can change often, so historical information is lost. Passive
DNS databases help solve both of these problems. Farsight Security DNSDB is
the largest passive DNS database in the world. With DNSDB, you can answer
questions like "How has this network infrastructure changed over time?", "What
other domains and subdomain point (or have pointed to) this IP address?",
"What are the subdomains and resource records for this domain?"

## How passive DNS works

Companies like Farsight Security use ICANN zone files, and partner with ISPs
and other large networks to deploy sensors that monitor and record DNS queries
and responses as they happen. The IP address and identities of those who are
making the queries are not recorded. The resulting database can then be used
by customers to query on both recent and historic DNS data. It is important to
note that no passive DNS database will have a truly complete set of all DNS
for all domains. The coverage of a passive DNS service is only as good as the
coverage of its sensors. With the largest and oldest network of DNS sensors,
Farsight Security DNSDB is the most complete commercial passive DNS database
available.

## Getting started

In order to use Farsight Security DNSDB, you must have an API key that
authenticates you to the service. Farsight Security offers a free [community
edition](https://www.farsightsecurity.com/dnsdb-community-edition/) and [free
trial](https://www.farsightsecurity.com/trial-api/) access to DNSDB. Of
course, you can also purchase a full subscription.

Once you have obtained an API key, it can be used with your
integration/platform of choice. This guide will cover using the Python library
and CLI [dnsdb-python.](https://pypi.org/project/dnsdb-python/)

Ensure Python 3 is installed on your system, then run this command to install
dnsdb-python.

    pip3 install dnsdb-python

Next, set the environment variable DNSDB_KEY to your DNSDB API key.

## Basic DNSDB queries

DNSDB has two query types: forward and inverse. Forward queries find all known
records associated with a domain or subdomain. Inverse lookups find all
hostnames that have pointed to a specific IP address or CNAME value.

in this guide, we will be running queries to examine the infrastructure behind
a [credential harvesting page](https://seanthegeek.net/1069/how-to-examine-a-
credential-harvesting-page-using-microsoft-edge/).

This particular credential harvesting page sends stolen credentials to a web
server at plotoperation1.3eehj3wdhdhjww3r3dkjd.com.

### Forward queries

A forward query with a wildcard will output the full history of all records in
DNSDB for the domain and its subdomains. Results can also be filtered by date
and record type, and output to various file formats, such as CSV and JSON, if
desired.

    dnsdb forward "*.3eehj3wdhdhjww3r3dkjd.com"
    
    
    ;; bailiwick:  com.
     ;; count:      2
     3eehj3wdhdhjww3r3dkjd.com. IN NS ns1.reg.ru.
     3eehj3wdhdhjww3r3dkjd.com. IN NS ns2.reg.ru.
    
     ;; bailiwick:  3eehj3wdhdhjww3r3dkjd.com.
     ;; count:      40
     ;; source:     sensor
     ;; first seen: 2021-04-07T20:56:39+00:00
     ;; last seen:  2021-05-20T22:22:35+00:00
     3eehj3wdhdhjww3r3dkjd.com. IN A 194.58.112.174
    
     ;; bailiwick:  com.
     ;; count:      81
     ;; source:     sensor
     ;; first seen: 2021-04-06T19:35:53+00:00
     ;; last seen:  2021-05-20T22:22:35+00:00
     3eehj3wdhdhjww3r3dkjd.com. IN NS ns1.reg.ru.
     3eehj3wdhdhjww3r3dkjd.com. IN NS ns2.reg.ru.
    
     ;; bailiwick:  3eehj3wdhdhjww3r3dkjd.com.
     ;; count:      1
     ;; source:     sensor
     ;; first seen: 2021-05-06T12:53:19+00:00
     ;; last seen:  2021-05-06T12:53:19+00:00
     3eehj3wdhdhjww3r3dkjd.com. IN NS ns1.reg.ru.
     3eehj3wdhdhjww3r3dkjd.com. IN NS ns2.reg.ru.
    
     ;; bailiwick:  3eehj3wdhdhjww3r3dkjd.com.
     ;; count:      98
     ;; source:     sensor
     ;; first seen: 2021-04-07T20:55:50+00:00
     ;; last seen:  2021-05-20T21:19:11+00:00
     3eehj3wdhdhjww3r3dkjd.com. IN SOA ns1.reg.ru. hostmaster.ns1.reg.ru. 1617737377 14400 3600 604800 10800
    
     ;; bailiwick:  3eehj3wdhdhjww3r3dkjd.com.
     ;; count:      2
     ;; source:     sensor
     ;; first seen: 2021-04-07T20:55:50+00:00
     ;; last seen:  2021-05-06T12:53:19+00:00
     3eehj3wdhdhjww3r3dkjd.com. IN MX 10 mail.plotoperation1.3eehj3wdhdhjww3r3dkjd.com.
    
     ;; bailiwick:  3eehj3wdhdhjww3r3dkjd.com.
     ;; count:      51
     ;; source:     sensor
     ;; first seen: 2021-04-06T19:35:53+00:00
     ;; last seen:  2021-05-20T21:19:11+00:00
     plotoperation1.3eehj3wdhdhjww3r3dkjd.com. IN A 37.18.30.131

From these results, we can see that plotoperation1.3eehj3wdhdhjww3r3dkjd.com
has pointed to the same IP address for over a month.

### Inverse queries

An inverse query can be used to find other domains and hostnames that have
pointed to an IP address.

    dnsdb inverse ip "37.18.30.131"
    
    ;; count:      1
     ;; source:     sensor
     ;; first seen: 2021-04-07T06:06:16+00:00
     ;; last seen:  2021-04-07T06:06:16+00:00
     l291067a.justinstalledpanel.com. IN A 37.18.30.131
    
     ;; count:      51
     ;; source:     sensor
     ;; first seen: 2021-04-06T19:35:53+00:00
     ;; last seen:  2021-05-20T21:19:11+00:00
     plotoperation1.3eehj3wdhdhjww3r3dkjd.com. IN A 37.18.30.131

### Pivoting

These results provided another domain to investigate, justinstalledpanel.com.
Running a forward query on that reveals more infrastructure. the -o option
will redirect output to a file in the format specified by the file extension.

    dnsdb forward "*.justinstalledpanel.com" -o justinstalledpanel.com.csv

At the time of this writing, this returned 10,000 records, including 5 A
records, 7 NS records, and 9,988 SOA records.

The high number of SOA records suggests that the domain is modified very
frequently, because the SOA record is updated every time a DNS zone changes.
So why are only a few other records returned? This is because DNSDB queries
return a maximum of 10,000 results. In this case most of that 10,000 result
limit is being used up by SOA records, which isn't very useful. Unfortunately,
there is no way to filter out just SOA records. Each record type will need to
be queried separately.

For example, to only view A records, the command is

    dnsdb forward -t A "*.justinstalledpanel.com" -o justinstalledpanel.com.csv

When running separate queries for each record type, queries for this domain
returned the following record counts:

Type | Count  
---|---  
A | 10,000+  
AAAA | 108  
CNAME | 0  
MX | 0  
NS | 7  
SOA | 10,000+  
SRV | 0  
TXT | 0  
  
The results can be refined further by adding time boundaries. Time range
arguments in dnsdb-python accept relative and absolute formats. For example,
as of this writing there were 4,507 A record changes over the last 7 days.

    dnsdb forward -f csv  -t A --last-seen-after 7d "*.justinstalledpanel.com" | wc
      -l
     
    4509

In fact, there are about 184 A record changes **every minute** , which in a
testament to the near real-time nature of the data provided by DNSDB.

    dnsdb forward -f csv  -t A --last-seen-after 1m "*.justinstalledpanel.com" | wc
      -l
    
     186

Based on a[ whois
lookup](https://www.virustotal.com/gui/domain/justinstalledpanel.com/details),
It turns out justinstalledpanel.com is used as part of the domain parking
infrastructure for publicdomainregistry.com, which explains why there are so
many record changes so frequently.
