---
layout: post
status: publish
published: true
title: How to comply with Google and Yahoo's requirements for bulk email senders
permalink: '/1338/how-to-comply-with-google-and-yahoos-requirements-for-bulk-email-senders/'
description: "Starting February 2024 Google and Yahoo will start enforcing additional requirements for emails to reach the inbox. Here's how to comply."
image:
  path: '/assets/images/dmarc-wax-seal.png'
wordpress_id: 1338
wordpress_url: https://seanthegeek.net/?p=1338
date: '2024-01-11 19:20:50 +0000'
date_gmt: '2024-01-11 19:20:50 +0000'
categories:
- Information Security
- How-to Guides
tags:
- DMARC
- email
comments: []
---
To help protect their customers from malicious and junk emails,
[Google](https://support.google.com/mail/answer/81126) and
[Yahoo](https://senders.yahooinc.com/best-practices/) have announced that they
will begin to enforce additional requirements for emails from bulk email
senders in February 2024. Failure to meet these requirements will result in
emails being placed in the spam folder instead of the inbox, or possibly not
being delivered at all. This includes both personal and business inboxes.
Other email providers are expected to follow suit, so any application that
sends email should work towards adhering to these requirements, regardless of
recipients or message volume.

**Update** : Google has begun to reject messages from bulk senders that do not
comply with authentication requirements.

## What are bulk email senders?

Updated on 2024-02-24 to reflect Clarified guidance from Google.

Google defines bulk senders based on the main domain of the from address. If
5,000 or more emails are ever sent Gmail customers from a domain or its
subdomains combined, that domain and its subdomains are permanently considered
bulk senders.

Even if a domain is not currently considered a bulk sender, properly
authenticating your emails is a deliverability best practice that will make it
more likely that your emails reach the inbox.

## What are the additional requirements?

* Message from domains must have a DMARC policy record published in DNS.

  * A `none` policy is ok to start with.

  * DMARC policy records should have a `rua` value set so that the domain owner can monitor DMARC compliance reports provided by receiving email services.

    * [parsedmarc](https://domainaware.github.io/parsedmarc/) is an open source tool that can parse and analyze DMARC reports.

    * Many commercial solutions exist to analyze DMARC reports, including [Dmarcian](https://dmarcian.com/). Proofpoint customers will need to use Proofpoint's Email Fraud Defense product or [use workarounds](https://seanthegeek.net/806/proofpoint-is-requiring-their-customers-to-pay-for-email-fraud-defense-to-get-aggregate-dmarc-data-from-their-own-gateways/) to get a full view of their DMARC data.

* Emails must pass a DMARC authentication check to verify that the from address is not spoofed.

  * This requires either SPF or DKIM to pass and be in alignment with the domain in the message from address.

* Once DMARC reporting data shows that all legitimate sending sources are passing DMARC, the domain owner should switch the domain's DMARC policy from "none" to "quarantine" or "reject".

* Non-transactional emails such as newsletters and promotions must support one-click unsubscribe standards.

## How do I know if my emails are passing DMARC?

Look for `dmarc=pass` in the `Authentication-Results` or
`Authentication-Results-Original` email headers after the email has been
delivered.

More information about SPF, DKIM, and DMARC authentication can be found in my
complete guide: [Demystifying DMARC: A guide to preventing email
spoofing](https://seanthegeek.net/459/demystifying-dmarc/).

## What do I do if my emails aren't passing DMARC?

DKIM is the most reliable way to pass DMARC. Ensure that your emails are DKIM
signed as the domain you are using in the message from header. With most
vendors this can be configured by the customer. Other vendors may require a
support case. Generally, the process works like this:

  1. Tell the vendor the domain you need to DKIM sign as

  2. The vendor will generate DNS records that need to be added to the domain you are sending as

  3. Add the required DNS records to the domain

  4. Inform the vendor that the DNS records have been added, and they will enable DKIM signing

If a vendor does not support DKIM signing as a customer's domain, check to see
if they support other options to pass DMARC, such as alignment via SPF or
using a custom email relay. Dmarcian maintains a helpful [public
list](https://dmarc.io/) of known DMARC support options for a variety of
services.

## How do I implement one-click unsubscribe for marketing emails?

Your vendor may already have this deployed. To check this, look for a `List-
Unsubscribe` email header. The user's email service will also show an
unsubscribe button above the email body. If not, ask your vendor for guidance
for implementing one-click unsubscribe as defined in
[RFC8058](https://datatracker.ietf.org/doc/html/rfc8058).
