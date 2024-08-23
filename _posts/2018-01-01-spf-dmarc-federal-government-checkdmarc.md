---
layout: post
permalink: /310/spf-dmarc-federal-government-checkdmarc/
title: Lessons Learned from the US Federal Government's Ongoing Deployment of SPF
  and DMARC
seo_title: Lessons Learned as Feds Deploy SPF and DMARC - seanthegeek.net
description: An explanation of SPF and DMARC best practices, using results from checkdmarc
  scans of US Government domains as a case study, as federal agencies work towards
  fully implementing the cyber hygiene actions prescribed in DHS BOD 18-01
date: 2018-01-01 18:07:42 -0000
last_modified_at: 2019-02-11 23:54:37 -0000
publish: true
pin: false
image:
  path: /assets/wp-content/uploads/2018/01/army-mail.webp
  alt: Two soldiers process mail in a US Army Forward Operating Base Mailroom
categories:
- Information Security
tags:
- BOD 18-01
- checkdmarc
- DHS
- DMARC
- SPF
---
SPF and DMARC are standards that describe how the origins of email messages
should be verified, to prevent email spoofing. I spent some free time over the
past few weeks creating
[`checkdmarc`](https://domainaware.github.io/checkdmarc/) , a Python 3 module
and command-line interface that can validate and troubleshoot SPF and DMARC
records across multiple domains, with the intent of building it into a web
application that will process DMARC reports. The Department of Homeland
Security recently launched an initiative to deploy SPF, DMARC, and other best
practices on most federal agency domains by issuing BOD 18-01. This created
the perfect case study of common challenges and mistakes when deploying SPF
and DMARC across very large organizations, and even a few small ones.

**2018-01-30 update** : I have made many improvements to my script, corrected
a few of my own misconceptions about DMARC I had in this post, and switched to
updated results from 2018-01-28.

## DHS Binding Operational Directive 18-01 (BOD 18-01)

On October 17, 2017 the US Department of Homeland Security (DHS) issued
[Binding Operational Directive 18-01](https://cyber.dhs.gov/) (BOD 18-01).
This directive requires most federal agencies to deploy cyber hygiene best
practices to secure their websites and email services, including SPF, DMARC,
STARTTLS, and HTTPS with HTS:

> * "Within **30 days** of BOD issuance _(November 16th, 2017)_ , submit an
> "Agency Plan of Action" to [FNR.BOD@hq.dhs.gov](mailto:FNR.BOD@hq.dhs.gov)
> and begin implementing the plan.
> * Within **90 days** _(January 15, 2018)_ of BOD issuance:
>   * Configure all internet-facing mail servers to offer STARTTLS.
>   * Configure all second-level domains to have valid SPF/DMARC records,
> with at minimum a DMARC policy of "p=none" and at least one address defined
> as a recipient of aggregate and/or failure reports.
> * By **120 days** _(February 13, 2018)_ after BOD issuance:
>   * Ensure all publicly accessible Federal websites and web services
> provide service through a secure connection (HTTPS-only, with HSTS).
>   * Identify agency second-level domains that can be HSTS preloaded, and
> provide a list to DHS at [FNR.BOD@hq.dhs.gov](mailto:FNR.BOD@hq.dhs.gov).
>   * Disable SSLv2 and SSLv3 on web and mail servers.
>   * Disable 3DES and RC4 ciphers on web and mail servers.
>   * Within **15 days of the establishment of a centralized NCCIC reporting
> location** , add DHS as a recipient of DMARC aggregate reports.
> * Within **one year** _(October 16, 2018)_ of BOD issuance, set a DMARC
> policy of "reject" for all second-level domains and mail-sending hosts."
>

Unfortunately, Intelligence Community and/or National Security systems are not
required to comply with BODs, although they would still benefit from applying
them.

Enabling STARTTLS on mail servers allows senders to establish an encrypted
connection before sending email. Enabling HTS on a web server tells clients to
only use an encrypted (HTTPS) connection whenever they are accessing the site
in the future. Disabling obsolete, weak cipher suites prevents easy exploits
such as [POODLE](https://www.us-cert.gov/ncas/alerts/TA14-290A) from working.
SPF and DMARC are standards that work in tandem to prevent email spoofing.
This blog post will focus on these standards. However, all of the best
practices are key parts of [defense in depth](/78/prevent-ransomware-strategic-defense/).

## What is email spoofing?

Emails are spoofed when the from field of the message appears to be from
someone other than the actual sender. For example, an attacker sending a
phishing email can set the `from` address to match the target's CEO. In many
organizations, the target's mail client will even helpfully display a known
email address as a name and picture from their internal profile, which makes
the phishing email look more legitimate.

Spoofing is a powerful, simple tool for attackers, but there are legitimate
reasons for spoofing email from addresses. If an organization is using an
outside email marketing service, helpdesk, or any other outside service that
sends email, there is a need to make the items appear they are coming from
their trusted domain, and not the third party, so recipients know who is
responsible for the messages.

So how can a recipient mail server differentiate from legitimate and
illegitimate spoofing? SPF, DKIM, and DMARC, of course!

## What is SPF?

The Sender Policy Framework (SPF) is a standard for listing mail servers that
are authorized to send email from your domain. It is defined in [RFC
7208](https://tools.ietf.org/html/rfc7208). The domain owner publishes a
specially formatted `TXT` record in the DNS zone containing a list of
authorized servers.

Details about the exact record format [can be found
here](https://www.openspf.org/SPF_Record_Syntax).

When a receiver mail server receives an email, it checks to see if the domain
in the `MAIL FROM` part of the SMTP envelope has published a SPF record. If a
record is found, the IP address of the sending mail server is compared to the
list. Note that SPF does not check the from header that the user sees, and the
SMTP envelope is not part of the message headers. so it is easy to bypass SPF
and still spoof email to the user. The best illustration I have found of this
comes from the great guide at [o365info.com](https://o365info.com/how-to-simulate-spoof-e-mail-attack-and-bypass-spf-sender-verification-part2-of-2/)
that explains exactly how to bypass SPF:

[![An illustration of email spoofing that bypasses SPFchecks](/assets/wp-content/uploads/2018/01/Simulating-Spoof-E-mail-attack-and-bypassing-the-SPF-verification-check-03-B.webp)](/assets/wp-content/uploads/2018/01/Simulating-Spoof-E-mail-attack-and-bypassing-the-SPF-verification-check-03-B.webp)
An illustration of email spoofing that bypasses SPF checks
_Credit: o365info.com - Used under fair use for educational purposes_

Also, It is up the receiving mail server to decide what to do with an email if
the SPF check fails. SPF does not specify an action for the recipient mail
server to take in the event of a validation failure. DMARC fills these gaps,
and more.

## Common mistakes when deploying SPF and how to avoid them

### Not deploying SPF (and DMARC) on domains that do not send email

An attacker can still spoof email to make it look as if it is coming from a
domain even if it doesn't have MX records and/or you don't use it for email at
all; these domains are the easiest to deploy SPF on: just add a `TXT` record
containing `"v=spf1 -all"`

### Including the same servers more than once

There are multiple mechanisms to allow a server, but a server only needs to be
allowed by one of them. For example, if you use the ipv4 mechanism to state
that a whole netblock is allowed allowed to send email, you **don't** need to
use an a mechanism to include a sever by hostname.

### Using the wrong mechanism

The most common mechanisms in use are `ipv4`, `ipv6`, `mx`, `a`, and `include`

* `ipv4`: used to specify a single IPv4 address or CIDR  netblock
* `ipv6`:  used to specify a single IPv6 address or CIDR  netblock
* `mx`: used to specify the servers listed in a domain's `MX` resource records, **not** for allowing individual mail servers by hostname. If a `mx` mechanism includes a value (e.g. `mx:mail.example.com`), the MX records located at that value are queried; if a value is not included with the mechanism (e.g. `mx`), the domain's own records are queried
* `a`: used to specify a server by hostname, or a domain's own `A`/`AAAA` records if no hostname is included with it; this is frequently used to allow web servers to send mail, since they are not included in MX records
* `include`: used to include SPF mechanisms from another domain. This is frequently used to include lists of `ipv4`/`ipv6` mechanisms from third party services that send email as the domain including cloud email and marketing services, such as Office 365, Google, or Salesforce; multiple include statements can bu used (e.g. `include:spf.protection.outlook.com include:_spf.elasticemail.com`) `include` mechanisms do not include the `all` value; to include mechanisms and the `all` value (e.g. to have a standard configuration for all of your domains), use the `redirect=` modifier at the end of the record - this modifier can only be used once per record

### Using too many mechanisms that trigger DNS lookups

[RFC 7208, section 4.6.4](https://tools.ietf.org/html/rfc7208#section-4.6.4)
limits the combined number of `a`, `mx`, `include`, `exists`,  and `redirect`
mechanisms and modifiers used in a SPF record to 10, including any mechanisms
from included records -  the total number of `MX` records returned per `mx`
mechanism is also cannot exceed a separate limit of 10; this is done to
prevent DNS-based denial-of-service (DoS) attacks

To reduce the number of DNS lookup mechanisms in a record:

* If you have sending server IP addresses that won't change often, consider using `ipv4` or `ipv6` mechanisms, which don't trigger DNS lookups, instead of `mx` or `a`.
* Have third party services send emails from dedicated subdomains; for example, if a billing services vendor currently sends emails as `noreply@yourdomain.com`, have them send from `noreply@billing.yourdomain.com`, and make that email address an alias if you want to receive replies at `noreply@yourdomain.com`; this way `billing.yourdomain.com` gets its own SPF record and limits. Having MX records for these subdomains improves en emails trustworthiness to many gateways, even if you don't actually have mailboxes for that subdomain.

### Using the `ptr` mechanism

According to [RFC 7208, section
5.5](https://tools.ietf.org/html/rfc7208#section-5.5), the `ptr` mechanism
should not be used

## What is DKIM?

DKIM is a stronger method of validating that an email was sent from an
authorized server than SPF.  The sending server signs outgoing mail with a
private key, and places the signature in a message header and the receiving
server validates the signature using a public key published in DNS, as defined
in [RFC 6376](https://tools.ietf.org/html/rfc6376) - DomainKeys Identified
Mail (DKIM) Signatures. Messages may have multiple DKIM signature headers if
they have been forwarded through multiple gateways.

Take a look at this example, lightly modified from Wikipedia:

    DKIM-Signature: v=1; a=rsa-sha256; d=example.net; s=brisbane;
  
         c=relaxed/simple; q=dns/txt; l=1234; t=1117574938; x=1118006938;
  
         h=from:to:subject:date:keywords:keywords;
  
         bh=MTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTI=;
  
         b=dzdVyOfAKCdLXdJOc9G2q8LoXSlEniSbav+yuU4zGeeruD00lszZ
  
                  VoG4ZHRNiYzR

A verifier queries the `TXT` resource record type of
`brisbane._domainkey.example.net.`

Here, example.net is the author domain to be verified against (in the `d`
tag), `brisbane` is a selector given in the `s` tag, and `_domainkey` is a
fixed part of the protocol.

There are no CAs or revocation lists involved in DKIM key management. The
selector is a straightforward method to allow signers to add and remove keys
whenever they wish. Long lasting signatures for archival purposes are outside
DKIM's scope. Other tags are visible in the example are:

* v - version
* a - signing algorithm
* d - domain
* s - selector
* c - canonicalization algorithm(s) for header and body
* q - default query method
* l - length of the canonicalized part of the body that has been signed
* t - signature timestamp
* x - expire time
* h - list of signed header fields, repeated for fields that occur multiple times

## What is DMARC?

DMARC is the Domain-based Message Authentication, Reporting, and Conformance
standard, as described in [RFC 7489](https://tools.ietf.org/html/rfc7489). It
consists of a specially-formatted DNS `TXT` resource record published by a
Domain Owner, that tells mail servers what to do when they encounter a message
that appears to be from that domain, but fails SPF and/or DKIM. It also
provides methods for mail receivers to notify Domain Owners when mail fails
the DMARC check.

DMARC records are `TXT` resource records of a subdomain of a second-level
domain called `_dmarc`, i.e. `_dmarc.example.com`. Unlike SPF, DMARC options
apply to all subdomains, under the base domain (i.e. `example.com`). DMARC
records are composed of tags and values that are joined by `=`, and delimited
by `;`. All DMARC records start with `v=DMARC1`.

The most important and commonly used DMARC tags are `p`, `sp`, `pct`, `rua`,
and `ruf`.

The `p` tag sets the DMARC policy, which specifies the policy to be enacted by
the Receiver at the request of the Domain Owner on mail that is supposedly
from the Domain Owner's domain fails the DMARC check. The policy applies to
the domain and to its subdomains, unless subdomain policy is explicitly
described using the `sp` tag. Possible policy values include:

**Policy** | **Description**
---|---
`none` | The Domain Owner requests no specific action be taken regarding delivery of messages. **This is the implicit default policy.**
`quarantine` | The Domain Owner wishes to have email that fails the  DMARC mechanism check be treated by Mail Receivers as suspicious. Depending on the capabilities of the Mail Receiver, this can mean "place into spam folder", "scrutinize with additional intensity", and/or "flag as suspicious".
`reject` |  The Domain Owner wishes for Mail Receivers to reject email that fails the DMARC mechanism check. Rejection _should_ occur during the SMTP transaction.

The `pct` tag value is an integer percentage of messages from the Domain
Owner's mail stream to which the DMARC policy is to be applied. However, this
**must not** be applied to the DMARC-generated reports, all of which must be
sent and received unhindered. The purpose of the `pct` tag is to allow Domain
Owners to enact a slow rollout of enforcement of the DMARC mechanism. **The
implicit default value is 100**.

I **strongly recommend** leaving `pct` set at 100 (ideally by not setting it
at all), and using the policies to slow the rollout of DMARC instead. That
way, the same policy is applied to all mail, not an arbitrary percentage.

The `rua` tag specifies comma-separated delivery locations for aggregate
reports, which are typically daily emailed reports of [compressed XML
files](https://dmarc.org/wiki/FAQ#I_need_to_implement_aggregate_reports.2C_what_do_they_look_like.3F)
that describe how many emails a Receiver observed from a given mail server IP
address that failed the DMARC check.

The `ruf` tag specifies comma-separated delivery locations for forensic
reports, which are emails with copies of the original emails that failed the
DMARC check attached. These are particularly useful for allowing Domain Owners
to examine phishing emails sent third parties as well as their own
organization, that were made took look like they came from their domain.
However,  many Receivers only send aggregate reports, if they send DMARC
reports at all; others may only provide the email headers, and not the full
content.

Both `rua` and `ruf` tags are expected to have a value of a list of comma-
separated DMARC URIs, the only URI type currently supported in the DMARC
specification is `mailto`. Each email address in the list must be prefixed
with `mailto:` in order to be a valid DMARC URI.

Additionally, if an email address in the `rua` and `ruf` tag values has a
domain with a base domain that is different than the base domain that _dmarc
record is a subdomain of, an authorization record must be added on the base
domain of the email address. For example, if `example.com` had a DMARC record
like this:

    _dmarc.example.net TXT "v=DMARC1; p=none; rua=mailto:dmarc@mail.example.com"

because `example.net` does not match the base domain of `mail.example.com`.
receivers will check for the existence of the following record, before sending
a report to `dmarc@example.com`:

    example.net._report._dmarc_example.com TXT "v=DMARC1"

Likewise, if `example.com` was using a third party service like Agari to
receive, store, and process DMARC reports:

    _dmarc.example.com TXT "v=DMARC1; p=none; rua=mailto:example@rua.agauri.com ruf=mailto:example@ref.agari.com"

Then the following DNS records need to be added to the `agari.com` DNS zone
(which they do when a domain is added to an account):

    example.com._report._dmarc_rua.agari.com TXT "v=DMARC1"
    example.com._report._dmarc_ruf.agari.com TXT "v=DMARC1"

These records are defined in [RFC 7489, section
7.1](ttps://tools.ietf.org/html/rfc7489#section-7.1). and are required when
reports are directed external domains, so that someone can't flood your DMARC
inbox with reports for a domain that you do not operate by setting up a domain
like `totallylegit.com`,  adding the record:

    _dmarc.totallylegit.com TXT "v=DMARC1; p=none; rua=mailto:dmarc@mail.example.com; ruf=mailto:dmarc@mail.example.com"

And sending a ton of emails as `totallylegit.com` that purposefully fail the
DMARC check to many different organizations.

Return Path has an [great series of blog posts](https://blog.returnpath.com/how-to-read-your-first-dmarc-reports-part-1/)
on how to read DMARC reports. Check it out once you start getting reports.

## What is DMARC alignment?

Passing a DMARC check requires passing SPF or DKIM checks, but DMARC goes
beyond by also requiring that the identifiers for at least one of these checks
are aligned, so spoofing is prevented.

| **DKIM** | **SPF**
---|---|---
**Passing** | The signature in the DKIM header is validated using a public key that is  published as a DNS record of the domain name specified in the signature | The mail server's IP address is listed in the SPF record of the domain in the SMTP _mail from_ envelope header
**Alignment** | The signing domain aligns with the domain in the message's from header | The domain in the SMTP _mail from_ envelope header aligns with the domain in the message's from header

## DMARC without DKIM will break (some of) your email delivery

**You must sign outgoing email at your gateway with a unique DKIM key before
publishing a DMARC policy oa DMARC quarantine or reject policy**. Simply
allowing a sending server via SPF in not enough.

Why? Forwarded emails. Not the kinds of forwards that users send from their
mail clients or webmail, but the forwards from mailbox rules. These forwards
take place during SMTP delivery, and are common when someone changes
addresses, or when a company gets acquired.

When forwards happen at the SMTP level, the envelope mail from will not match
the header from, so the SPF indicators are not aligned, and the DMARC check
will fail, unless the original sending mail server signed the message with
DKIM, and the forwarding server(s) did not tamper with it. DKIM signatures are
included in forwarded messages, because they are in the message headers.

## The state of .gov in early 2018

I made some improvements to my scripts, and reran the tests on 2018-01-28 to
see how the federal government had improved, now that the deadline to at least
have a `p=none` DMARC policy had passed.

Unfortunately, due to the bug fixes I've made in between tests, the results
are not comparable, but these results are more accurate.

The generated files can be [downloaded here](/assets/wp-content/uploads/2018/01/USG-DMARC-2018-01-28.zip).

[![A pie chart of SPF deployment on .gov domains as of
2018-01-28](/assets/wp-content/uploads/2018/01/dotgov-spf-2018-01-28.webp)](/assets/wp-content/uploads/2018/01/dotgov-spf-2018-01-28.webp)
A pie chart of SPF deployment on .gov domains as of 2018-01-28

[![A pie chart of DMARC deployment on .gov domains as of
2018-01-28](/assets/wp-content/uploads/2018/01/dotgov-dmarc-2018-01-28.webp)](/assets/wp-content/uploads/2018/01/dotgov-dmarc-2018-01-28.webp)
A pie chart of DMARC deployment on .gov domains as of 2018-01-28

[![A column chart of DMARC deployment by policy on .gov domains as of
2018-01-28; Note: “none” is a valid DMARC policy – the “\(empty\)” chart value
represents domains that have missing or invalid DMARC
records](/assets/wp-content/uploads/2018/01/dotgov-dmarc-policy-2018-01-28.webp)](/assets/wp-content/uploads/2018/01/dotgov-dmarc-policy-2018-01-28.webp)
A column chart of DMARC deployment by policy on .gov domains as of 2018-01-28;
Note: "none" is a valid DMARC policy - the "(empty)" chart value represents
domains that have missing or invalid DMARC record

**Value** | **SPF** | **DMARC**
---|---|---
Invalid/Missing | 429 | 645
Valid | 881 | 665

**DMARC Policy (p value)** | **Count of Domains**
---|---
none | 463
quarantine | 10
reject | 192
Missing/Invalid DMARC record | 645

### High profile .gov domains

Rather than trying to examine all 1,310 .gov domains in a single blog post,
let's focus on a much smaller subset of 44 domains from agencies of political,
social, and/or bureaucratic significance:

**Domain** | **Agency** | **SPF** | **DMARC**
---|---|---|---
archives.gov | National Archives and Records Administration | Valid | p=reject
cbo.gov | Congressional Budget Office | Uses 13/10 DNS lookups | Missing record
cdc.gov | Centers for Disease Control | Valid | p=none
census.gov | US Census Bureau | Valid | doc.gov does not indicate that it accepts DMARC reports about census.gov
cms.gov | Centers for Medicare and Medicaid Services | Valid | p=none
commerce.gov | Department of Commerce | Valid | doc.gov does not indicate that it accepts DMARC reports about commerce.gov
consumerfinance.gov | Consumer Financial Protection Bureau | Missing record | cfpb.gov does not indicate that it accepts DMARC reports about consumerfinance.gov
doc.gov | Department of Commerce | Valid | p=none
doi.gov | Department of the Interior | Valid | p=none
dot.gov | Department of Transportation | Valid | p=none
ed.gov | Department of Education | Valid | p=none
epa.gov | Environmental Protection Agency | Valid | p=none
faa.gov | Federal Aviation Administration | Valid | p=none
fcc.gov | Federal Communication Commission | Valid | p=none
fda.gov | Food and Drug Administration | Valid | p=none
fdic.gov | Federal Deposit Insurance Corporation | Valid | p=reject
federalreserve.gov | Federal Reserve | Valid | p=reject
fema.dhs.gov | Federal Emergency Management Agency | Valid | p=none
fema.gov | Federal Emergency Management Agency | Valid | fema.dhs.gov does not indicate that it accepts DMARC reports about fema.gov
gsa.gov | General Services Agency | Uses 13/10 DNS lookups | pct value is less than 100. This leads to inconsistent and unpredictable policy enforcement.
healthcare.gov | Federal Healthcare Exchange | Valid | p=reject
hhs.gov | Department of Health and Human Services | The ptr mechanism should not be used - https://tools.ietf.org/html/rfc7208#section-5.5 | p=none
hud.gov | Department of Housing and Urban Development | Valid | p=none
ice.gov | Immigration and Customs Enforcement | Missing record | Missing record
interior.gov | Department of the Interior | Valid | p=none
irs.gov | Internal Revenue Service | DNS servers fail to respond to query for include:qai.irs.gov | p=none
loc.gov | Library of Congress | Valid | Missing Record
mail.nasa.gov | National Aeronautics and Space Administration | Valid | p=none
medicaid.gov | Medicaid | Valid | p=reject
medicare.gov | Medicare | Valid | p=none
nara.gov | National Archives and Records Administration | Valid | p=none
nasa.gov | National Aeronautics and Space Administration | Valid | p=none
ncua.gov | National Credit Union Administration | Valid | p=none
nhtsa.gov | National Highway Traffic Safety Administration | Valid | dot.gov does not indicate that it accepts DMARC reports about nhtsa.gov
nps.gov | National Park Service | Valid | p=none
ofdp.irs.gov | Internal Revenue Service | Valid | p=none
omb.gov | Office of Management and Budget | Valid | Invalid fo tag: Values 0 and 1 are mutually exclusive
sec.gov | Securities and Exchange Commission | Valid | p=none
ssa.gov | Social Security Administration | Valid | p=quarentine
uscis.gov | US Citizenship and Immigration Services | Missing record | Missing record
usda.gov | US Department Department of Agriculture | Valid | Missing record
usmint.gov | US Mint | Valid | p=none
uspto.gov | US Patent and Trademark Office | Valid | p=none
va.gov | Department of Veteran's Affairs | Valid | p=none

### The US Intelligence Community

Some very significant agencies are missing from the list above, because they
are members of the Intelligence Community (IC). DHS Binding Operational
Directives do not apply to IC and/or National Security systems. However, SPF
and DMARC would still be great security controls for them to deploy, as they
are much more likely to be targets of spoofed phishing email than other
agencies. At the very least, it could provide counterintelligence on phishing
attempts sent to Unclassified email systems, because [nothing like that has ever happened before](https://www.nytimes.com/2015/04/26/us/russian-hackers-read-obamas-unclassified-emails-officials-say.html).
So, let's check on the
deployment of SPF and DMARC in the IC too.

**Domain** | **Agency** | **SPF** | **DMARC**
---|---|---|---
af.mil | US Air Force | Missing record | Missing record
army.mil | US Army | Missing record | Missing record
cia.gov | Central Intelligence Agency | Unnecessary SPF mechanisms: mx:cia.gov mx:ucia.gov | Missing record
dea.gov | Drug Enforcement Agency | Valid | p=none
dhs.gov | Department of Homeland Security | Valid | p=none
dia.mil | Defense Intelligence Agency | Valid | Missing record
dni.gov | Director of National Intelligence | Missing record | Missing record
dod.gov | Department of Defense | Missing record | Missing record
energy.gov | Department of Energy | Valid | p=none
fbi.gov | Federal Bureau of Investigation | Valid | p=reject
hq.dhs.gov | Department of Homeland Security | Valid | p=none
justice.gov | Department of Justice | Valid | p=none
mail.mil | Shared Department of Defense email system hosted by DISA | Valid | Unrelated TXT records were discovered. These should be removed, as some receivers may not expect to find unrelated TXT records at _dmarc.mail.mil v=spf2.0/pra include:_spf.eemsg.mail.mil ~all
marines.mil | US Marine Corps | Missing record | Missing record
navy.mil | US Navy | Valid | Missing record
nga.mil | National Geospacial-Intelligence Agency | Missing record | Missing record
nro.gov | National Reconnaissance Office | Missing record | Missing record
nro.mil | National Reconnaissance Office | Missing record | Missing record
state.gov | Department of State | Valid | p=none
treasury.gov | Department of the Treasury | Valid | p=none
uscg.mil | US Coast Guard | Valid | Missing record
usdoj.gov | Department of Justice | Valid | p=none
usmc.mil | US Marine Corps | Valid | Missing record
whitehouse.gov | The White House | Valid | Missing record

**Shout out to the FBI for _still_ being the only IC member with a DMARC
policy currently set to** `reject`!

### IC Support Agencies

These agencies provide services to IC agencies:

**Domain** | **Agency** | **SPF** | **DMARC**
---|---|---|---
disa.mil | Defense Information Systems Agency | Missing record | Missing record
dla.mil | Defense Logistics Agency | Valid | Missing record
opm.gov | Office of Personnel Management | usalearning.net has multiple spf1 TXT records | p=none

## Defense contractors

Let's check the major defense contractors for comparison. I also threw in
Leidos, a spin-off of Lockheed Martian that provides information security
consulting services to a variety of industries, and SpaceX, to see how newer,
companies compare to the established giants.

Several of these companies have separate domains for their email and web
services. The email domains are protected by SPF and DMARC, but the web
domains are not. Although those web domains do not host email services, those
domains could still be useful to spoof for phishing.

**Domain** | **Company** | **SPF** | **DMARC**
---|---|---|---
baesystems.com | BAE Systems | Missing record | Missing record
bah.com | Booz Allen Hamilton (Email domain) | Valid | p=none
boeing.com | Boeing | Valid | Missing record
boozallen.com | Booz Allen Hamilton | Missing record | Missing record
gd.com | General Dynamics | Valid | Missing record
l3-com.com | L3 Communications | Valid | Missing record
l3t.com | L3 Technologies | Valid | Missing record
leidos.com | Leidos | Valid | Missing record
lmco.com | Lockheed Martin (Email domain) | Valid | Missing record
lockheedmartin.com | Lockheed Martin | Missing record | Missing record
ngc.com | Northrop Grumman (Email domain) | Valid | Missing record
northropgrumman.com | Northrop Grumman | Missing record | Missing record
palantir.com | Palantir | Valid | Missing record
raytheon.com | Raytheon | Valid | p=none
spacex.com | SpaceX | Valid | p=none
utc.com | United Technologies | Valid | p=none
