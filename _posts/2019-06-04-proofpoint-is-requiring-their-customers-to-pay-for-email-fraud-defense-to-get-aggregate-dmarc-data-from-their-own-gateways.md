---
layout: post
status: publish
published: true
title: Proofpoint is requiring their customers to pay for Email Fraud Defense to get
  aggregate DMARC data from their gateways
description: In order to get aggregate DMARC data on mail flowing through their own gateways, Proofpoint customers must purchase Proofpoint Email Fraud Defense
permalink: /806/proofpoint-is-requiring-their-customers-to-pay-for-email-fraud-defense-to-get-aggregate-dmarc-data-from-their-own-gateways
image:
  path: /assets/images/Proofpoint-DMARC-dashboard.jpg
wordpress_id: 806
wordpress_url: https://seanthegeek.net/?p=806
date: '2019-06-04 04:31:21 +0000'
date_gmt: '2019-06-04 04:31:21 +0000'
categories:
- Information Security
- Reviews
tags:
- DMARC
- Proofpoint
- email
comments:
- id: 2262
  author: Steve Mitchell
  author_url: ''
  date: '2019-08-14 20:47:22 +0000'
  date_gmt: '2019-08-14 20:47:22 +0000'
  content: Testify, brother. Open those RFE's folks!
- id: 2433
  author: Jason Anthony
  author_url: ''
  date: '2019-09-18 19:48:48 +0000'
  date_gmt: '2019-09-18 19:48:48 +0000'
  content: "Steve Mitchell, Can you clarify your comment (\"Testify, brother. Open
    those RFE&rsquo;s folks!\")?\r\n\"Testify\" to what?\r\nWhat's \"RFE\" in this
    case? Is it any of the ones listed in \"https://en.wikipedia.org/wiki/RFE\"?\r\nThank
    you!"
- id: 2490
  author: Sean Whalen
  author_url: ''
  date: '2019-10-01 18:04:20 +0000'
  date_gmt: '2019-10-01 18:04:20 +0000'
  content: I believe he means Proofpoint customers should open a "Request For Enhancement"
    with Proofpoint.
- id: 3571
  author: Todd Shubert
  author_url: ''
  date: '2020-03-02 19:54:40 +0000'
  date_gmt: '2020-03-02 19:54:40 +0000'
  content: "In your \"ProofPoint Email Authentication Guide,\" would it work to set
    up a single Policy Route with:\r\n\r\nCondition: Message Header From (address
    Only)\r\nOperator: Is in domain set\r\nValue: default_inbound\r\n\r\nThis just
    seems more simple than setting up a route for every domain, but maybe I'm not
    seeing some very obvious pitfall."
- id: 7533
  author: Michael Schwartz
  author_url: ''
  date: '2022-06-28 20:05:51 +0000'
  date_gmt: '2022-06-28 20:05:51 +0000'
  content: "Sean,\r\nIm looking for a DMARC consultant.  Ive got my DMARC and doing
    pretty good, all pass/pass except every once in a while get a failure.  Are you
    able to help me figure out why?  Its only a couple of DMARC reports with fail
    and Ive been doing it a month, probably got 90 reports over my 2 domains.  Please
    email me and then I can give you my phone # and we can talk.  Or if you know someone
    who can help me.  Im looking for hourly consulting"
- id: 7800
  author: Barry Jones
  author_url: ''
  date: '2022-07-26 13:42:29 +0000'
  date_gmt: '2022-07-26 13:42:29 +0000'
  content: "I wanted to let you know I just finished writing a 3 part DMARC guide
    and cited you and this article in the Enterprise section, under Invisible Email
    Servers. Thanks for writing it!\r\n\r\nhttps://www.brightball.com/articles/enterprise-challenges-with-dmarc-deployment"
---
I have written extensively about the DMARC email security standard, including
publishing a [comprehensive guide](https://seanthegeek.net/459/demystifying-
dmarc/) on how to implement it, with or without additional third-party
vendors.  I also do a little consulting on DMARC deployment best practices.
One of those consulting clients uses Proofpoint for their email gateway. They
also use Dmarcian, a reasonably priced DMARC report analytics service that
also publishes a ton of [public content](https://dmarc.io/) for the good of
the community. We were considering moving the client's DMARC policy from
monitor only (p=none) to an enforced state (p=reject) after many hours of
steadily improving the SPF and DKIM alignment of their email sources. As I
took another look at the aggregate (rua) DMARC data in Dmarcian, I noticed
something odd: Dmarcian was getting aggregate reports from all of the expected
third-party email recipients, like Google, Yahoo, Comcast, and the client's
industry partners, but I didn't see any reporting from the client's own
Proofpoint Secure Email Gateway (SEG).

This is a problem, because that meant Dmarcian wasn't seeing who was spoofing
the client's domain in emails bound for the client's own gateways. We were
blind to potential phishing activity, and critical items like payroll could
break if we switched to an enforced DMARC policy without aggregate data from
the Proofpoint gateway. Surly, I thought, there must be some configuration
option in the Proofpoint console I was overlooking. I've never been a
Proofpoint customer, so I reached out to some information security partners
who are Proofpoint email gateway customers to find out what was going wrong.
The answer was simple, infuriating, and confirmed by Proofpoint sales
engineers: Proofpoint does not provide DMARC aggregate/rua reports to DMARC
analytics inboxes, despite the fact that sharing those reports is a
cornerstone of the DMARC standard.

Proofpoint does provide aggregate DMARC data about the mail traffic flowing
through a customer's gateway, but only via Proofpoint's own DMARC report
[analytics offering](https://www.proofpoint.com/us/products/email-fraud-
defense), Proofpoint Email Fraud Defense (EFD). In essence, Proofpoint is
ensuring that only their EFD offering provides their existing email gateway
customers with the full picture needed to deploy DMARC, at an additional cost,
of course.

As a less than ideal workaround for this problem, Proofpoint customers can
create a Policy Route that matches on message From headers that end with their
domains, and then create a DMARC policy in Proofpoint that applies to that
route and configure the policy to copy any messages that fail DMARC to a
separate quarantine folder for later review. That way, they can at least get
samples of the emails that failed DMARC, even though they won't show up in
third party analytics.

**Update** : I have written a complete Proofpoint email authentication
[guide](/assets/docs/Proofpoint-Email-Authentication-Guide.pdf) that
describes how to implement this workaround in detail.

This has impacts beyond Proofpoint SEG and EFD. Even if a Proofpoint customer
employs the above workaround, or pays for Email Fraud Defense, the lack of
shared aggregate data harms non-Proofpoint users. Domain owners aren't getting
the valuable DMARC feedback they need from Proofpoint mail recipients to
identify email delivery problems and malicious campaigns. For example,
consider a situation where a third-party supplier happens to mostly have
customers that use Proofpoint SEG. If there was an issue with their email
alignment or deliverability, they would have no idea. They would also be blind
to any malicious spoofing of their domain targeting their customers who use
Proofpoint.

If Proofpoint started sending out RUA reports today, EFD still has useful
features that are helpful for administrators and increase lock-in to
Proofpoint EFD -- particularly hosted SPF and hosted DKIM. These features
allow customers to delegate SPF and DKIM records to Proofpoint EFD, so that
EFD administrators (e.g., SecOps/SecArch/email team, etc.) can add DKIM keys
or SPF records without needing full DNS write access, which simplifies changes
while reducing risk, and reducing the number of people who would need to be
involved in a DNS change.

DMARC can only be successful if everyone implementing it does the bare minimum
effort of honoring DMARC policies by default, including sending out DMARC
aggregate/rua reports to all services. By only sharing aggregate DMARC data in
their own Email Fraud Defense service, Proofpoint is valuing vertical
integration and market capture over the trustworthiness of email for all,
including their own email gateway customers. Proofpoint EFD would not be
possible if every other major email service and gateway wasn't doing their
part by providing aggregate reports.

To Proofpoint leadership: Please start honoring DMARC policies by default and
sending proper DMARC aggregate/rua reports to everyone according to the RFC by
default.

**Update** : Proofpoint Essentials now supports honoring a domain's DMARC
policy, but it must be [turned
on](https://help.proofpoint.com/Proofpoint_Essentials/Email_Security/Administrator_Topics/How_does_DMARC_work_with_Proofpoint_Essentials%3F)
by an account administrator and still does not send aggregate/rua email
reports.
