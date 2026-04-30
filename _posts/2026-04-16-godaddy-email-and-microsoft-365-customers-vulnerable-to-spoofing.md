---
layout: post
title: GoDaddy's email and Microsoft 365
  customers are vulnerable to spoofing
date: 2026-04-16 14:42 -0400
description: Anyone with a GoDaddy server can create spoofed emails that pass SPF and DMARC, thanks to unauthenticated relays combined with lax documentation and an overly-broad SPF record
image:
  path: /assets/images/godaddy-logo.webp
  description: The GoDaddy logo
category: Information security
tags:
  - Email
  - GoDaddy
  - SPF
---

The [GoDaddy documentation](https://web.archive.org/web/20260408164836/https://www.godaddy.com/help/add-an-spf-record-to-my-domain-for-my-email-40499) for email and Microsoft 365 instructs customers to add `include:secureserver.net` to the SPF record of the customer domain. `secureserver.net` wastes an SPF lookup by only including `spf-0.secureserver.net`, instead of including the record data directly. `spf-0.secureserver.net` authorizes the IP addresses of GoDaddy's outbound webmail services and the unauthenticated gateways used by their web hosting customers. It ends with `include:spf.protection.outlook.com` for Microsoft 365 services — the only SPF `include` that Microsoft 365 customers actually need.

```bash
dig +short txt @1.1.1.1 secureserver.net | grep spf
"v=spf1 include:spf-0.secureserver.net -all"

dig +short txt @1.1.1.1 spf-0.secureserver.net
"v=spf1 ip4:64.202.168.0/24 ip4:97.74.135.0/24 ip4:72.167.238.0/24 ip4:72.167.234.0/24 ip4:72.167.218.0/24 ip4:68.178.252.0/24 ip4:68.178.213.0/24 ip4:216.69.139.0/24 ip4:208.109.80.0/24 ip4:92.204.81.0/24 ip4:198.71.224.0/19 ip4:184.168.224.0/24 ip4:184.1" "68.200.0/24 ip4:184.168.131.0/24 ip4:184.168.128.0/24 ip4:92.204.65.0/28 ip4:182.50.132.0/24 ip4:173.201.192.0/23 ip4:72.167.168.0/24 ip4:92.204.71.0/24 ip4:132.148.124.0/24 ip4:72.167.172.0/24 ip4:188.121.52.0/24 ip4:188.121.53.0/24 ip4:52.89.65.132 ip4:" "54.214.222.76 ip4:54.184.82.65 ip4:52.26.164.15 ip4:68.178.181.0/24 ip4:50.63.8.0/22 ip4:208.109.194.0/24 ip4:80.237.138.192/26 include:spf.protection.outlook.com -all"
```

So, anyone can fire up a cheap GoDaddy VPS, use the unauthenticated relay for that VPS region, and spoof any GoDaddy customer who has followed these instructions. In my testing, GoDaddy's relay retained the original SMTP `MAIL FROM`, so spoofed emails will pass SPF [with alignment](/459/demystifying-dmarc/), causing DMARC to pass — even if the spoofed domain has a `p=reject` DMARC policy. This can be seen in the email headers below.

```email
Return-Path: <attorney@examplelaw.com>
Received: from osnlsmtp01-07.prod.phx3.secureserver.net (osnlsmtp01-07.prod.phx3.secureserver.net. [50.63.10.84])
        by mx.google.com with ESMTPS id 5a478bee46e88-2e267b66dcasi1656168eec.1.2026.04.16.06.39.10
        for <infosecdemo42@gmail.com>
        (version=TLS1_3 cipher=TLS_AES_256_GCM_SHA384 bits=256/256);
        Thu, 16 Apr 2026 06:39:11 -0700 (PDT)
Received-SPF: pass (google.com: domain of attorney@examplelaw.com designates 50.63.10.84 as permitted sender) client-ip=50.63.10.84;
Authentication-Results: mx.google.com;
       spf=pass (google.com: domain of attorney@examplelaw.com designates 50.63.10.84 as permitted sender) smtp.mailfrom=attorney@examplelaw.com
Message-ID: <69e0e67f.050a0220.209457.53b7SMTPIN_ADDED_MISSING@mx.google.com>
Received: from mailer.badguysandco.com ([72.167.42.251])
	by : HOSTING RELAY : with ESMTPS
	id DMv2wDkJJaxAFDMv2wGhub; Thu, 16 Apr 2026 13:38:09 +0000
```

I used Cloudflare to purchase the domain `examplelaw.com` and host its DNS records. Then, I added the SPF record `v=spf1 include:secureserver.net -all` to simulate someone following GoDaddy's instructions. After that, I created a GoDaddy account using a different email domain. There was nothing tying that GoDaddy account to `examplelaw.com`, and yet GoDaddy let me send an email as that domain without any authentication.

There's no easy fix for GoDaddy because of the way their infrastructure was built.

If GoDaddy starts requiring credentials at the relay and tying accounts to verified domain ownership as they should, that instantly breaks email relaying for an untold number of customers accustomed to unauthenticated relaying. And those customers may not even be the people who originally built or configured their site — making fixes harder to coordinate.

GoDaddy could simply change their documentation, but that doesn't help the countless domains that already have the risky `include` in their SPF record.

Given this risk, `include:secureserver.net` does not belong in any SPF record. If you are using GoDaddy to relay email from a GoDaddy web server, consider using a different relay like Amazon SES instead. If you are using Microsoft 365, use `include:spf.protection.outlook.com` instead — even if you bought your Microsoft 365 subscription through GoDaddy or use a GoDaddy domain. If you use an email security gateway (e.g., IronPort or Proofpoint) and have your outgoing email routed through that, use their SPF `include`/`a` mechanism instead of either `include:secureserver.net` or `include:spf.protection.outlook.com`.
