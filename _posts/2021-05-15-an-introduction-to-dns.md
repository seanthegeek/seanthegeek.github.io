---
layout: post
permalink: /1117/an-introduction-to-dns
title: An introduction to DNS
description: An overview of what DNS is, how it works, and the purposes of the various
  DNS resource record types
date: 2021-05-15 02:09:42 -0000
last_modified_at: 2021-05-17 12:30:42 -0000
publish: true
pin: false
categories:
- Information Security
tags:
- DNS
- networking
---
The Domain Name System (DNS) is best known as the way domain names are
converted into IP addresses that clients connect to, but there are many other
uses for DNS. Read on to learn more.

Information about resources in a domain are stored as **Resource Records**
inside a DNS **zone**. There are many different types of Resource Records.

Type | Description  
---|---  
A | IPv4 addresses  
AAAA | IPv6 addresses  
CNAME | Configures a domain or subdomain as an alias for another domain or subdomain  
MX | Specifies incoming mail servers for the domain or subdomain  
NS | Specifies the secondary nameservers to be used for the zone or subdomain  
PTR | Pointer record that specifies the reverse DNS hostname of an IP address  
SOA |  Statement of Authority - contains multiple values separated by commas

  1. MNAME: The zone's primary nameserver
  2. RNAME: The administrator's email address, with the @ replaced with a period
  3. SERIAL: The zone's Serial Number (this is used as a revision number)
  4. REFRESH: The length of time in seconds secondary servers should wait before asking primary servers for the SOA record to see if it has been updated
  5. RETRY: The length of time in seconds a server should wait for asking an unresponsive primary nameserver for an update again
  6. EXPIRE:  If a secondary server does not get a response from the primary server for this amount of time in seconds) it should stop responding to queries for the zone
  7. TTL: The default Time to Live (TTL) for Resource Records - i.e. the length of time in seconds an individual resource record should be cached; each resource record can also have its own separate TTL value that overrides this default value

SRV |  A service record that specifies a hostname and port for a particular service - frequently used for chat VoIP services,  
  
The format is:

    _service._proto.name. TTL class type of record priority weight port target.

A XMPP chat service on server.example.com would need a SRV record like

    _xmpp._tcp.example.com. 86400 IN SRV 10 5 5223 server.example.com.

For more information on SRV resource records, [see
this](https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/)
documentation at Cloudflare.  
TXT | Arbitrary text strings. Used by standards like [SPF, DKIM, and DMARC](https://seanthegeek.net/459/demystifying-dmarc/) to publish information about a domain for email authentication. Also used by various services to validate domain ownership.  
  
 DNS zones are hosted in nameservers specified by the domain owner. The
nameservers may be hosted by the domain registrar, owner, or a third-party
service. Administrators/owners of a domain can delegate a control of a
subdomain to another nameserver using NS records, allowing someone else to
manage records for that subdomain and anything below as a separate DNS zone.
For example, the root zone of example.com is com.

The resource records for a given domain can be found by using a DNS query tool
like dig to query for each of the various record types.

    dig SOA example.com
    dig NS example.com
    dig A example.com
    dig AAAA example.com
    dig MX example.com
    dig TXT example.com
    dig SRV example.com

You can also query subdomains, but you must know the name of the subdomain (or
use a passive DNS service to learn about historical queries for a domain). www
is a commonly-used subdomain, so that is a good one to try.

    dig SOA www.example.com
    dig NS www.example.com
    dig A www.example.com
    dig AAAA www.example.com
    dig MX www.example.com
    dig TXT www.example.com
    dig SRV www.example.com

Here are the resource records for example.com and www.example.com:

rrname | rrtype | rdata  
---|---|---  
example.com. | A | 93.184.216.34  
example.com. | NS | a.iana-servers.net.<br>b.iana-servers.net.  
example.com. | SOA | ns.icann.org. noc.dns.icann.org. 2021022340 7200 3600 1209600 3600  
example.com. | MX | 0 .  
example.com. | TXT | "v=spf1 -all"<br>"8j5nfqld20zpcyr8xjw0ydcfq9rk8hgm"  
example.com. | AAAA | 2606:2800:220:1:248:1893:25c8:1946  
www.example.com. | A | 93.184.216.34  
www.example.com. | TXT | "v=spf1 -all"  
www.example.com. | AAAA | 2606:2800:220:1:248:1893:25c8:1946  
  
Based on these results, we know the following about the DNS zone for
example.com:

* The zone's primary nameserver is ns.icann.org
* The zone administrator's email address is noc@dns.icann.org
* The zone's serial number is 2021022340
* The REFRESH threshold is 7200 seconds (120 minutes)
* The RETRY threshold is 3600 seconds (one hour)
* The EXPIRES threshold is 1209600 seconds (14 days)
* The default TTL is 3600 seconds (one hour)
* Connections to example.com will be routed to the IPv4 address 93.184.216.34 and the IPv6 address is 2606:2800:220:1:248:1893:25c8:1946
* www.example.com points to the same IPv4 and IPv6 addresses
* An empty MX record value is set, which explicitly indicates that the domain does not accept incoming email
* The "v=spf1 -all" TXT records are SPF records that inform mail servers that example.com and www.example.com are not used in outgoing emails
* The purpose of example.com TXT record "8j5nfqld20zpcyr8xjw0ydcfq9rk8hgm" is unknown

If the administrator of example.com wanted to allow a contractor to control
the records of contractor.example.com and below, the administrator would add a
NS resource record named contractor.example.com, and set the value/rdata to
the nameservers of the contractor.

![A diagram of the structure of DNS](/assets/wp-content/uploads/2021/05/domain_name_space.webp)
