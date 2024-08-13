---
layout: post
status: publish
published: true
title: Demystifying DMARC - A guide to preventing email spoofing
permalink: /459/demystifying-dmarc/
image:
  path: /assets/images/DMARC-Summary-dashboard.png
wordpress_id: 459
wordpress_url: https://seanthegeek.net/?p=459
date: '2018-06-15 20:00:30 +0000'
date_gmt: '2018-06-15 20:00:30 +0000'
categories:
- Information Security
- How-to Guides
tags:
- SPF
- DMARC
- checkdmarc
- open source
- parsedmarc
- talks
- DKIM
- 614Con
comments:
- id: 737
  author: Mehran
  author_url: ''
  date: '2018-09-07 02:06:15 +0000'
  date_gmt: '2018-09-07 02:06:15 +0000'
  content: "Great article.\r\n\r\nUnder DKIM required tags I think you meant bh not
    hb."
- id: 750
  author: Sean Whalen
  author_url: ''
  date: '2018-09-11 17:33:56 +0000'
  date_gmt: '2018-09-11 17:33:56 +0000'
  content: Good catch. Fixed. Thanks!
- id: 849
  author: Sebastiano
  author_url: ''
  date: '2018-11-27 11:40:52 +0000'
  date_gmt: '2018-11-27 11:40:52 +0000'
  content: Hello Sean, first of all I'd like to thank you for your parsedmarc implementation,
    which is what brought me here. Is there a palce where I could ask for some help
    about it? I'm trying to test it at my working place, but I can't send properly
    the results to Elasticsearch/Kibana. I don't want to bother you with trivial questions,
    because I feel I'm a bit incompetent on this topic. Maybe a community help would
    be more appropriate.
- id: 852
  author: Sebastiano
  author_url: ''
  date: '2018-11-29 10:37:47 +0000'
  date_gmt: '2018-11-29 10:37:47 +0000'
  content: Ok, I've installed everything from scratch using pypy3 3.5 virtualenv (which
    is currently compatible with Python 3.5.3) on my Ubuntu 18.04.1 server... and
    everything works just fine. I thinks it's possible that Python 3.6.7 (which comes
    with Ubuntu 18.04.1) it's not fully compatible with parsedmarc package. Again,
    thank you very much for this useful tool.
- id: 958
  author: Rick Koch
  author_url: ''
  date: '2019-01-14 15:08:20 +0000'
  date_gmt: '2019-01-14 15:08:20 +0000'
  content: "As I browse material touting DMARC, it's often mentioned that DMARC allows
    vendors to send mail without getting flagged as spam. Based on what I've read
    there and what is hinted at above, is then a requirement for DMARC compliance
    that a vendor must have DKIM keys from my domain and/or be included in my SPF
    records, PLUS he must use my domain as his FROM addresses?\r\n\r\nTrying to figure
    out what distinguishes a DMARC-compliant vendor from a non-compliant one. I have
    a vendor who is on the dmarc.io list, but they say they do not support DMARC.
    Their mail process ultimately puts their own domain in the FROM header, and I'm
    not sure they can modify this. But as I read it, that will be a non-starter for
    DMARC regardless of SPF or DKIM."
- id: 1479
  author: elemzy
  author_url: ''
  date: '2019-04-10 16:04:15 +0000'
  date_gmt: '2019-04-10 16:04:15 +0000'
  content: "Whao....This is the most extensive explanation of email authentication
    in one single article. Good work. \r\nQuestion: Which is what lead me here. Can
    I set my Dmarc policy to reject/quarantine, if I only have SPF and no DKIM (I
    use GFI which doesn't support DKIM at this time). \r\nIf yes will this Dmarc record
    cause my mails to have issues?\r\n v=DMARC1; p=none; rua=mailto:DMARCReports@abc.com;
    ruf=mailto:DMARCReports@abc.com; fo=1:s; aspf=r"
- id: 1490
  author: Sean Whalen
  author_url: ''
  date: '2019-04-12 15:26:27 +0000'
  date_gmt: '2019-04-12 15:26:27 +0000'
  content: As long as the vendor can DKIM sign as your domain, their email will work
    fine with DMARC, even if the vendor does not know that. :)
- id: 1491
  author: Sean Whalen
  author_url: ''
  date: '2019-04-12 15:34:53 +0000'
  date_gmt: '2019-04-12 15:34:53 +0000'
  content: |-
    Without DKIM, messages that are forwarded will fail DMARC

    /assets/images/smtp_forward_spf_dmarc_process.png

    That said, the DMARC record you describe is monitor only (p=none), so it won't impact delivery at all.
- id: 1539
  author: elemzy
  author_url: ''
  date: '2019-04-18 16:15:06 +0000'
  date_gmt: '2019-04-18 16:15:06 +0000'
  content: Thanks Sean. Was planning to change to p=quarantine but not anymore. Will
    turn off DMARC totally for now and  just rely on SPF only, since i do not have
    DKIM.
- id: 1540
  author: JAG
  author_url: ''
  date: '2019-04-18 18:32:13 +0000'
  date_gmt: '2019-04-18 18:32:13 +0000'
  content: "When reading about the mailing lists I wondered if the suggested \r\n\"do:
    Retain headers from the original message\"\r\nalso referred to the envelope from
    (\"Return-Path\"). Looking at the article you linked (https://begriffs.com/posts/2018-09-18-dmarc-mailing-list.html)
    it is not the case. The list is recommended to represent itself as the new return-path.\r\n\r\nReading
    the original article the recommendation was also to \"add a Sender header to indicate
    their relay role\". Did you leave this out for a reason or are the suggested setup
    actually doing so?  Even if RFC5322 seems to allow multiple Sender addresses it
    didn't seem to be valid usage. Adding Sender headers might be bad practice if
    there is one already (e.g. if an email is sent through multiple layers of lists)
    and I don't see it as a very useful thing for the recipient either. Would you
    agree?\r\n\r\nWhile commenting I would also mention that \"Sean Whalen April 12,
    2019 at 3:26 \" reply to \"Rick Koch\" seems a bit simplified.\r\n\"As long as
    the vendor can DKIM sign as your domain, their email will work fine with DMARC,\"
    relies on the fact that DMARC is ok with either SPF or DKIM passing. The alignment
    requirement for DKIM is however the header FROM field. \r\n\r\n\"Their mail process
    ultimately puts their own domain in the FROM header,\" says Rick and I would say
    that changes the answer quite a bit. They are in that case not sending emails
    from Rick's domain at all and they should not sign with his key. Right? It should
    require them to handle their spam reputation themselves."
- id: 1654
  author: Mario
  author_url: ''
  date: '2019-05-08 21:49:38 +0000'
  date_gmt: '2019-05-08 21:49:38 +0000'
  content: "Hi, this guide was really helpful!\r\nI was wondering, I have set this
    up accordingly on my office 365 instance. I have noticed though that mails send
    from shared mailbox (so basically using send-as) do not get dkim-signed. \r\nIs
    that a to be expected behavior?\r\nThanks"
- id: 1658
  author: Mario
  author_url: ''
  date: '2019-05-09 12:14:30 +0000'
  date_gmt: '2019-05-09 12:14:30 +0000'
  content: Turns out, that effective dkim activation on office365 might be delayed
    differently from one domain to another, even if activated at the same time. That's
    why, mails from a shared mailbox (with a different domain) were not signed.
- id: 1701
  author: Brad Bulger
  author_url: ''
  date: '2019-05-15 19:41:25 +0000'
  date_gmt: '2019-05-15 19:41:25 +0000'
  content: We're finding that with the Mailman 2 settings as recommended here, mail
    going to people with forwarded accounts (their uni address is in the list and
    forwards to their gmail address) is being rejected.
- id: 1833
  author: ShaneDT
  author_url: ''
  date: '2019-06-11 05:15:02 +0000'
  date_gmt: '2019-06-11 05:15:02 +0000'
  content: "Firstly thanks for a great guide very well explained.\r\n\r\nI have a
    question about SPF records and enabling DMARC with the p=none policy.\r\n\r\nIf
    I only have SPF enabled, the receiving server can lookup my SPF record and determine
    the list of authorised servers, and if receiving an email from a server not on
    my list, will reject or quarantine that email (I understand the limitation of
    Domain matching on the mailfrom field of course). \r\n\r\nIf I then enable DMARC
    (after enabling DKIM on my servers of course, or in this case Office 365) and
    set the policy to p=none initially, will the receiving server then record a fail
    on the SPF record if not sent from an authorised server, but deliver the email
    anyway as the DMARC policy is set to none?"
- id: 1848
  author: Sean Whalen
  author_url: ''
  date: '2019-06-12 15:26:08 +0000'
  date_gmt: '2019-06-12 15:26:08 +0000'
  content: That's correct. DMARC will record a failure, but will not impact delivery
    when p=none.
- id: 2356
  author: Anonymous
  author_url: ''
  date: '2019-09-02 16:28:46 +0000'
  date_gmt: '2019-09-02 16:28:46 +0000'
  content: "In the Authorization records example this line:\r\n\r\nexample.net._report._dmarc_example.com
    TXT \"v=DMARC1\"\r\n\r\nshould have the last underscore be a period.\r\n\r\nexample.net._report._dmarc.example.com
    TXT \"v=DMARC1\""
- id: 2452
  author: Mr shah
  author_url: https://www.nowebsite.com
  date: '2019-09-23 16:27:17 +0000'
  date_gmt: '2019-09-23 16:27:17 +0000'
  content: "Hi sean \r\n\r\nMy third party sender is trying to charge alot of money
    for this using sub domains. and sending my emails through their platform\r\n\r\nIs
    there an alternative way of doing this?\r\n\r\nthanks"
- id: 2491
  author: Sean Whalen
  author_url: ''
  date: '2019-10-01 18:14:52 +0000'
  date_gmt: '2019-10-01 18:14:52 +0000'
  content: Fixed. Thanks!
- id: 2492
  author: Sean Whalen
  author_url: ''
  date: '2019-10-01 18:16:33 +0000'
  date_gmt: '2019-10-01 18:16:33 +0000'
  content: Depends on if the vendor offers DKIM signing.
- id: 2714
  author: Scott D. Lockhart
  author_url: ''
  date: '2019-10-24 15:22:28 +0000'
  date_gmt: '2019-10-24 15:22:28 +0000'
  content: "This is the best article on email DMARC I have found so far.  Your article
    has answered almost all of my questions except for one.  I have a question about
    email delivery based on two scenarios:\r\n\r\nScenario 1:  A company does not
    have any SPF/DKIM/DMARC records published.\r\nScenario 2:  A company has an SPF
    record published and a DMARC record with p=none but does not have DKIM configured.\r\n\r\nIf
    a company moves from scenario 1 to scenario 2 there will be some legit emails
    that do not match the SPF record.  Are those legit emails at any addition risk
    of not being delivered than when there were no SPF/DKIM/DMARC records published?"
- id: 2951
  author: Sean Whalen
  author_url: ''
  date: '2019-12-04 14:29:29 +0000'
  date_gmt: '2019-12-04 14:29:29 +0000'
  content: A DMARC policy record of p=none does not add any additional risk to delivery
- id: 2968
  author: Sandeep
  author_url: https://postboxservices.com
  date: '2019-12-06 09:40:30 +0000'
  date_gmt: '2019-12-06 09:40:30 +0000'
  content: "I have deployed ParseDMARC but not receiving any emails. Its listed in
    the features :\r\n\r\n\"Optionally email the results\"\r\n\r\nIs there any configurations
    to switch on the reporting on emails. \r\n\r\nI have all required SMTP settings
    in the configuration file."
- id: 4764
  author: Sergio Costas
  author_url: https://www.rastersoft.com
  date: '2020-12-03 10:26:41 +0000'
  date_gmt: '2020-12-03 10:26:41 +0000'
  content: Thanks for this great article, and also for the PPTX presentation. I wonder
    if it is under a free license that allows it to be translated.
- id: 4765
  author: Sergio Costas
  author_url: https://www.rastersoft.com
  date: '2020-12-03 10:31:31 +0000'
  date_gmt: '2020-12-03 10:31:31 +0000'
  content: 'BTW: You recommend to disable DMARC when having only SPF. But what about
    setting it to "none" and adding an address for reports, for, at least, detect
    errors in SPF configuration?'
- id: 5221
  author: Asher Oto
  author_url: http://asheroto.com
  date: '2021-03-05 09:48:56 +0000'
  date_gmt: '2021-03-05 09:48:56 +0000'
  content: Wow, fantastic job. I love your stuff Sean. If you aren't posting on Medium,
    you should. I bet you'd get a lot of traffic that way! :-)
- id: 5224
  author: Sean Whalen
  author_url: ''
  date: '2021-03-05 13:26:41 +0000'
  date_gmt: '2021-03-05 13:26:41 +0000'
  content: Thanks! I'm honestly not very familiar with Medium, other than reading
    a few posts. What would be the advantage of posting there instead of here? At
    least here I get a tiny bit of ad revenue. ?
- id: 5226
  author: Sean Whalen
  author_url: ''
  date: '2021-03-05 13:30:45 +0000'
  date_gmt: '2021-03-05 13:30:45 +0000'
  content: I'll add a Creative Commons Attribution share-alike license.
- id: 5835
  author: Data
  author_url: ''
  date: '2021-06-29 15:37:49 +0000'
  date_gmt: '2021-06-29 15:37:49 +0000'
  content: "Hi Sean,\r\n\r\nThis is by far the most well-articulated, robust but concise
    documentation I can find ANYWHERE on the internet for SPF, DKIM, and DMARC. I
    have bookmarked this.\r\n\r\nHowever, I still can't fully figure out DKIM alignment
    with CNAME record implementation.\r\n\r\nWe have a vendor that uses mailgun and
    sends emails as our domain with noreply@ourdomain.com.  I tried having them put
    \"d=ourdomain.com\" in their TXT DKIM record, but it still signs emails as \"place.mg.theirdomain.com\"
    and not \"ourdomain.com\"\r\n\r\nTheir record has this name: \"smtp._domainkey.ourdomain.com\"
    and this value \" k=rsa; d=ourdomain.com; p=blahblahblah\"\r\n\r\nI tried putting
    this matching txt record in our DNS, but as \"smtp._domainkey\" instead. Still
    no dice. \r\n\r\nDo I instead need to create a CNAME record called \"smtp._domainkey\"
    and point it at \r\nthe current signer \"place.mg.theirdomain.com\"?\r\n\r\nThank
    you!"
- id: 6060
  author: dmarc
  author_url: https://blog.godmarc.com/how-to-select-the-best-dmarc-software-solution-to-protect-your-business-from-email-spoofing/
  date: '2021-08-21 13:20:39 +0000'
  date_gmt: '2021-08-21 13:20:39 +0000'
  content: Really Nice and well Explained
- id: 8196
  author: Alan Sill
  author_url: https://nsfcac.org
  date: '2023-01-07 18:03:33 +0000'
  date_gmt: '2023-01-07 18:03:33 +0000'
  content: "As many others have commented, this article remains a great service to
    the community. Thanks.\r\n\r\nFinding services to analyze the reports seems a
    minefield, though. Even wiht a few domains to monitor, getting a zipped xml file
    regularly for each domain is an incredible nuisance. What recommendations do you
    have to tame this automatic self-spamming behavior of getting DMARC reports?"
- id: 9974
  author: Bryan P Schappel
  author_url: https://www.crystalcomputer.com
  date: '2024-06-06 17:00:55 +0000'
  date_gmt: '2024-06-06 17:00:55 +0000'
  content: Search github for parsedmarc.
---
DMARC can stop spoofed spam and phishing from reaching you and your customers,
protecting your information security and your brand. However, complexity and
misconceptions deter many organizations from ever deploying it. Part
mythbusting, part implementation guide, this post explains the shortcomings
of SPF and DKIM, what DMARC is, how to deploy DMARC properly, and how to
respond to DMARC reports - **all without the need for an additional vendor** ,
thanks to open source software!

<iframe style="display: block; margin: 0 auto;" src="https://onedrive.live.com/embed?cid=5BEBF72EB17AB44F&amp;resid=5BEBF72EB17AB44F%2114733&amp;authkey=AOn2p6RPofuA2Gw&amp;em=2&amp;wdAr=1.7777777777777777" width="610px" height="367px" frameborder="0">This is an embedded <a target="_blank" href="https://office.com" rel="noopener noreferrer">Microsoft Office</a> presentation, powered by <a target="_blank" href="https://office.com/webapps" rel="noopener noreferrer">Office Online</a>.</iframe>

<div align="center">
<a href="https://1drv.ms/p/s!Ak-0erEu9-tb8w1gxxh1i0EHAV07">Direct link to presentation</a>
</div>

Modern email authentication relies on a combination of three standards: SPF,
DKIM, and DMARC. These standards help ensure that a message came from a server
related to the domain owner and was not spoofed.

## Sender Policy Framework (SPF)

SPF was the first widely adopted standard for combating email spoofing.
Despite its limitations in preventing spoofing, most email recipients expect
you to have it deployed on your domain. For example, Gmail/G-Site/Google will
throttle incoming emails from domains that do not have a valid SPF record.

### How SPF works

SPF is defined in [RFC 7208](https://tools.ietf.org/html/rfc7208). It works by
checking for a specially formatted DNS TXT record in the domain of the mail
from header in the SMTP transaction. This SPF record describes which servers
are authorized to send as that domain by using mechanisms to identify
authorized IP addresses and hostnames, or even include the SPF records of
other domains.

Every SPF record is a TXT record at the root of a domain or subdomain that
starts with v=spf1. From there, mechanisms are used to describe mail servers
are allowed (or not allowed) to send email as that domain or subdomain. A
domain or subdomain can only have one SPF record, but each subdomain can have
its own SPF record.

Some mechanisms like a, mx, include, and redirect use additional DNS lookups
to work. SPF has a maximum DNS lookup limit of 10, including any included
records. **Any SPF record that would require more than 10 DNS lookups to
resolve is invalid!** This is a common mistake to make when deploying SPF.

To work around this limit, send email from different subdomains. Each
subdomain needs its own SPF record and has its own set of limits for that
record. For example, you could send newsletters from news.example.com, and
invoices from billing.example.com.

You might not even need to include every vendor in your SPF records anyway. If
the vendor supports DKIM signing, you can rely on that to pass DMARC, even if
the sender is not in your SPF record. **Just make sure you are using ~all in
your SPF record**.

<table>
  <tbody>
    <tr>
      <th>Mechanism</th>
      <th>Description</th>
    </tr>
    <tr>
      <th>ip4</th>
      <td>Describes an ipv4 address or CIDR block of addresses.</td>
    </tr>
    <tr>
      <th>ip6</th>
      <td>Describes an ipv6 address or block of addresses.</td>
    </tr>
    <tr>
      <th>mx</th>
      <td>
        <p>Describes the servers listed in the mx record of the domain.</p>
        <p><strong>Counts towards the DNS lookup limit.</strong></p>
        <table>
          <tbody>
            <tr>
              <td>mx</td>
              <td>
                The servers listed in the mx records of its own domain
              </td>
            </tr>
            <tr>
              <td>mx:example.com</td>
              <td>
                The servers listed in the mx records of example.com
              </td>
            </tr>
          </tbody>
        </table>
      </td>
    </tr>
    <tr>
      <th>a</th>
      <td>
        <p>
          Describes the servers listed in the A and/or AAAA records of the
          domain.
        </p>
        <p><strong>Counts towards the DNS lookup limit.</strong></p>
        <table>
          <tbody>
            <tr>
              <td>a</td>
              <td>
                The IP addresses listed in the domains’ own A/AAAA records
              </td>
            </tr>
            <tr>
              <td>a:example.com</td>
              <td>
                The IP addresses listed in the A/AAA records of example.com
              </td>
            </tr>
          </tbody>
        </table>
      </td>
    </tr>
    <tr>
      <th>include</th>
      <td>
        <p>
          Includes the SPF record from the domain after the colon (it does not
          include the all modifier, if any)
        </p>
        <p><strong>Counts towards the DNS lookup limit.</strong></p>
      </td>
    </tr>
    <tr>
      <th>redirect</th>
      <td>
        <p>
          Stops processing the SPF record, and continues at the specified
          domain’s SPF record (including the all modifier!)
        </p>
        <p><strong>Counts towards the DNS lookup limit. </strong></p>
      </td>
    </tr>
    <tr>
      <th>exists</th>
      <td>
        <p>
          This mechanism is used to construct an arbitrary domain name that
          is<br />used for a DNS A record query. It allows for complicated
          schemes<br />involving arbitrary parts of the mail envelope to
          determine what is<br />permitted.
        </p>
        <p><strong>Counts towards the DNS lookup limit.</strong></p>
        <p>exists = “exists” “:” domain-spec</p>
        <p>
          The &lt;domain-spec&gt; is expanded as per
          <a href="https://tools.ietf.org/html/rfc7208#section-7">Section 7</a>.
          The resulting domain name is used for a DNS A RR lookup (even when the
          connection type is<br />IPv6). If any A record is returned, this
          mechanism matches.
        </p>
        <p>
          Domains can use this mechanism to specify arbitrarily complex<br />queries.
          For example, suppose example.com publishes the record:
        </p>
        <pre>v=spf1 exists:%{ir}.%{l1r+-}._spf.%{d} -all</pre>
        <p>
          The &lt;target-name&gt; might expand to
          “1.2.0.192.someuser._spf.example.com”. This makes fine-grained<br />decisions
          possible at the level of the user and client IP address.
        </p>
      </td>
    </tr>
  </tbody>
</table>

Mechanisms listed in the SPF record have an implicit pass (i.e. +) qualifier
in front of them. Possible qualifiers are:

Modifier | Name | Description
---------|------|------------
\+ | pass |  A "pass" result means the client is authorized to inject mail with the given identity. The domain can now, in the sense of reputation, be considered responsible for sending the message. Further policy checks can now proceed with confidence in the legitimate use of the identity.
? | neutral | A "neutral" result indicates that although a policy for the identity was discovered, there is no definite assertion (positive or negative) about the client. A "neutral" result MUST be treated exactly like the "none" result; the distinction exists only for informational purposes. Treating "neutral" more harshly than "none" would discourage domain managers from testing the use of SPF records. With a "none" result, the SPF verifier has no information at all about the authorization or lack thereof of the client to use the checked identity or identities. The check_host() function completed without errors but was not able to reach any conclusion.
\~ | softfail |  A "softfail" result ought to be treated as somewhere between "fail" and "neutral"/"none". The domain manager believes the host is not authorized but is not willing to make a strong policy statement.Receiving software SHOULD NOT reject the message based solely on this result, but MAY subject the message to closer scrutiny than normal.
\- | fail |  A "fail" result is an explicit statement that the client is not authorized to use the domain in the given identity. Disposition of SPF fail messages is a matter of local policy.

Most SPF records (except for those that are designed to be included in other
SPF records) end with an all modifier. The all modifier consists of the word
all with a qualifier in front of it. The all modifier states how emails should
be treated that do not match any of the listed mechanisms.

### SPF's weakness: Relying on SMTP headers

It is a common misconception that SPF stops email spoofing. At best, it makes
things a tiny bit more difficult on an attacker.

Remember, SPF checks for an SPF record at the domain in the mail from header
in the SMTP transaction (also known as the envelope from), not the message
from header that the receiving mail client sees, The SMTP transaction are not
visible to the end client, even when viewing the message headers.

This means that an attacker can use SMTP headers to direct the target's mail
server to check a domain that the attacker controls, which contains an
authorizing mechanism for the mail server the attacker is using, while
spoofing a completely different domain for the target to see in the message
from header!

In the example telnet screenshot below, the attacker is able to get the
receiving email server to check the SPF record of a domain that the attacker
controls (i.e. infosecspeakeasy.org), while spoofing the target's own domain
(i.e. cincykitchenandbath.com) in the message from header, which is the from
address that the target user will see.

[![A screenshot showing how SPF can be bypassed by spoofing the SMTP mail from
header](/assets/images/SPF-bypass.png)](/assets/images/SPF-bypass.png)
A screenshot showing how SPF can be bypassed by spoofing the SMTP mail from
header

This sort of domain mismatch occurs legitimately when a mailbox rule forwards
a message from another domain. The message from domain will stay the same, but
the SMTP mail from header will contain the domain of the forwarding mail
server.

[![A process graphic that shows how forwarded email fails SPF
alignment](/assets/images/smtp_forward_spf_dmarc_process.png)](/assets/images/smtp_forward_spf_dmarc_process.png)DKIM
signatures, on the other hand, are part of the message headers, and survive
message forwarding. **Therefore DKIM alignment is much more critical than SPF
alignment.**

### Example SPF records

**Once you know exactly which email services legitimately send as the domain
(DMARC reports will tell you), update the SPF record accordingly, and change
the ?all modifier to ~all.**

#### SPF record for domains that send emails from their incoming gateways and

are missing SPF records

    v=spf1 mx ?all

This record explicitly authorized any servers listed in the domain's MX
record, while treating all others as neutral. This is a good temporary SPF
record for new domains or newly acquired domains that do not already have a
SPF record.

Here are some good examples of SPF records for common cloud email providers:

#### Office 365

    v=spf1 include:spf.protection.outlook.com ?all

#### G-Suite

    v=spf1 include:_spf.google.com ?all

#### Proofpoint Essentials

    v=spf1 a:dispatch-us.ppe-hosted.com a:dispatch-eu.ppe-hosted.com ?all

#### SPF record for domains that do not send email (e.g. parked domains)

    v=spf1 -all

This record explicitly states that no mail servers are authorized to send
email as this domain.

This must be added to all domains that do not send email, inducing parked
domains.

## DomainKeys Identified Mail (DKIM)

DomainKeys Identified Mail (DKIM) is a email message authentication standard,
defined in [RFC 6376](https://tools.ietf.org/html/rfc6376). Because DKIM
authenticates the message headers , rather than the SMTP headers, DKIM
authentication survives intact when a message is directly forwarded (e.g. via
a mailbox rule).

### DKIM message headers

Here's an example DKIM header

    DKIM-Signature: v=1; a=rsa-sha256; d=example.com; s=s1; c=relaxed/simple; l=1234; t=1117574938; x=1118006938; h=from:to:subject:date; bh=MTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTI=;b=dzdVyOfAKCdLXdJOc9G2q8LoXSlEniSbav+yuU4zGeeruD00lszZVoG4ZHRNiYzR

#### Required DKIM header tags

Tag | Value Description
---|---
v | Signature version
a | Signature algorithm (rsa-sha256 should be used)
d | The domain where the public key can be found
s | The selector pointing to the public key at the domain (an arbitrary string)
h | A colon separated list of headers to concatenate when validating the header signature
b | The base64-enoded signature hash of the headers listed in the h tag
bh | The base64-enoded signature hash of the message body

#### Optional DKIM header tags

Tag | Value Description
---|---
t | Signature timestamp in UNIX timestamp format (i.e. the number of seconds from 00:00:00 on January 1, 1970 in the UTC time zone)
x | Signature expiration timestamp in UNIX timestamp format (i.e. the number of seconds from 00:00:00 on January 1, 1970 in the UTC time zone)
c | canonicalization algorithm: Defines if/how the receiving the receiving mail server should normalize the message to account for slight variations in whitespace and line breaks that could otherwise invalidate the signature. **Relaxed mode is strongly recommended for the header and body canonicalization** (i.e. c=relaxed/relaxed).
i | Identity/user-agent of the signer
l | Number of characters from the beginning of the body to use when calculating the body signature (**not recommended because someone could append malicious content**)
z | Not well defined

The receiving mail server uses the selector (`s=`) and domain (`d=`) tags to look
up the public key as a DNS TXT record at

    ._domainkey.

In the above signature example, the receiving server would look for the DKIM
key at:

    TXT s1._domainkey.example.com

### DKIM DNS records

DKIM DNS records are formatted as:

    v=DKIM1; k=rsa; p=;

**Lines in DNS TXT records are truncated at 256 characters. If the record is
longer, it must be split into separate lines in the same record in order to be
valid.**

DKIM public key records can be validated for syntax using the [DKIM record
lookup tool](https://mxtoolbox.com/dkim.aspx) at MX Toolbox.

#### Recommended DKIM DNS record tags

**Tag** | **Value Description**
---|---
**v** |  According to the RFC, this tag is recommended but not required, with an implicit default value of DKIM1. **However, in practice, some recipients don't follow the RFC exactly, and require this tag to be used anyway. This must be the first tag if used.****Your DKIM public key records should start with v=DKIM1;**
**n** | Notes: Human-readable notes for administrators reviewing DNS records **Useful for noting which service uses a selector and key.**

#### Required DKIM DNS record tags

**Tag** | **Value Description**
---|---
**p** |  Public key data encoded in base64. **Keys must be at least 1024 bytes long. 2048 bit length is strongly recommended.**

#### Optional DKIM record tags

<table>
  <tbody>
    <tr>
      <td><strong>Tag</strong></td>
      <td><strong>Value Description</strong></td>
    </tr>
    <tr>
      <td><strong>k</strong></td>
      <td>
        Key type: Defaults to rsa. Unrecognized key types
        <strong>must</strong> be ignored.
      </td>
    </tr>
    <tr>
      <td><strong>h</strong></td>
      <td>
        Acceptable hash algorithms: A colon-separated list of hash algorithms
        that might be used. Defaults to allowing all algorithms. Unrecognized
        algorithms <strong>must</strong> be ignored.
        <p>
          Refer to
          <a href="https://tools.ietf.org/html/rfc6376#section-3.3"
            >Section 3.3</a
          >
          for a discussion of the hash algorithms implemented by Signers and
          Verifiers. The set of algorithms listed in this tag in each record is
          an operational choice made by the Signer.
        </p>
      </td>
    </tr>
    <tr>
      <td><strong>s</strong></td>
      <td>
        Service Type: Defaults to *
        <p>
          A colon-separated list of service types to which this record applies.
          Verifiers for a given service type <strong>must</strong> ignore this
          record if the appropriate type is not listed. Unrecognized service
          types <strong>must</strong> be ignored.This tag is intended to
          constrain the use of keys for other purposes, should use of DKIM be
          defined by other services in the future.
        </p>
        <p>Currently defined service types are as follows:</p>
        <table>
          <tbody>
            <tr>
              <td><strong>Value</strong></td>
              <td><strong>Value Description</strong></td>
            </tr>
            <tr>
              <td><strong>*</strong></td>
              <td>Matches all service types</td>
            </tr>
            <tr>
              <td><strong>email</strong></td>
              <td>Electronic mail (not necessarily limited to SMTP)</td>
            </tr>
          </tbody>
        </table>
      </td>
    </tr>
    <tr>
      <td><strong>t</strong></td>
      <td>
        Flags: A colon-separated list of flags
        <p>Defaults to no flags</p>
        <table>
          <tbody>
            <tr>
              <td><strong>Flag</strong></td>
              <td><strong>Flag Description</strong></td>
            </tr>
            <tr>
              <td><strong>y</strong></td>
              <td>
                This domain is testing DKIM. Verifiers
                <strong>must not</strong> treat messages from Signers in testing
                mode differently from unsigned email, even if the signature
                fails to verify. Verifiers <strong>may</strong> wish to track
                testing mode results to assist the Signer.
              </td>
            </tr>
            <tr>
              <td><strong>s</strong></td>
              <td>
                <p>
                  Any DKIM-Signature header fields using the i= tag
                  <strong>must</strong> have the same domain value on the
                  right-hand side of the @ in the i= tag and the value of the d=
                  tag.
                </p>
                <p>
                  That is, the i= domain <strong>must not</strong> be a
                  subdomain of d=.
                </p>
                <p>
                  <strong
                    >Use of this flag is recommended unless subdomaining is
                    required.</strong
                  >
                </p>
              </td>
            </tr>
          </tbody>
        </table>
      </td>
    </tr>
  </tbody>
</table>

### Notes in DKIM DNS records

The DKIM selector (subdomain) is chosen by the vendor and is often non-
descriptive. You can use an arbitrary string in the n (i.e., notes) tag in the
DKIM record to make a note of the vendor's name, so you know which DKIM key is
used by which vendor as you audit your DNS records.

For example, if "matketingco" asked you to publish the following DKIM TXT
record:

    randomselector._domainkey.example.com TXT "p=base64Key"

You should create the record this way instead:

    randomselector._domainkey.example.com TXT "v=DKIM1; n=marketingco; k=rsa; p=base64Key"

### DKIM key rotation

It is generally recommended to rotate DKIM keys once per month, or at least
after you suspect that the DKIM private key has been compromised. Most
email/marketing services will handle key rotation for you when you configure
your domains for DKIM, but some almost never rotate their keys.

Unlike web and email certificates, the domain/email address is not part of the
PKI. DKIM does not use certificates.. The domain is listed in the d= header
tag. Therefore, **you do not need a separate public/private key pair for each
domain**.

You should create two key pairs, and store the public keys under two different
selectors, for example:

    s1._domainkey.example.com TXT "v=DKIM1; k=rsa; p=<public key>;"
    s2._domainkey.example.com TXT "v=DKIM1; k=rsa; p=<a different public key>;"

With CNAME records, your other domains can use the same selectors and keys:

    s1._domainkey.example.net CNAME s1._domainkey.example.com.
    s2._domainkey.example.net CNAME s2._domainkey.example.com.

Third party services will often have you authorize their DKIM keys on your
domains using CNAME records and will then validate that those records exist
before signing email, so they can handle key changes for you.

If you are using your own keys, it is up to you to manage them, preferably
using automation. Start by signing all of your emails using the first
selector. When it is time to rotate the keys, sign all outgoing email using
the s2 sector. After a week of not using the key at the s1 selector, replace
the key at the `s1` selector.

When it is time to rotate keys again, start using the s1 selector exclusively,
wait a week, then replace they key at the s2 selector with a new key, so it
will be ready for the next rotation.

Unless a key is known to have been compromised, it is important to wait a week
(i.e., 7 days) before replacing it, as some receiving mail servers will cache
the public key at a given selector for up to a week.

Using this ping-pong key rotation scheme, you ensure that email is always
signed with a valid, secure key.

  1. Start exclusively signing with the other selector.
  2. Wait 7 days.
  3. Replace the key at the old selector so it is ready for the next rotation.
  4. Go to step 1.

### DKIM's weakness: arbitrary d= values

Without DMARC, the d= value in a DKIM signature header is not required to
match the same domain that the user sees in the message From header. An
attacker can place a valid DKIM signature header in an email with a d= value
that points to a domain the attacker controls, allowing DKIM to pass while
still spoofing the from address to the user.

## Domain-based Message Authentication, Reporting, and Conformance (DMARC)

Domain-based Message Authentication, Reporting, and Conformance (DMARC) is
defined in [RFC 7489](http://Domain-
based%20Message%20Authentication,%20Reporting,%20and%20Conformance%20\(DMARC\)).
DMARC ensures that the SPF and DKIM authentication mechanisms actually
authenticate against the same base domain that the end user sees.

In order to be useful, a DMARC DNS record must be published by a domain owner,
and email recipients must honor this record, including its enforcement policy,
and at least send back aggregate reports if requested by the domain owner.

A message passes a DMARC check by passing DKIM **or** SPF, **as long as the
related indicators are also in alignment with the message's from address**.

  | DKIM | SPF
---|---|---
Passing | The signature in the DKIM header is validated using a public key that is published as a DNS record of the domain name specified in the signature | The mail server's IP address is listed in the SPF record of the domain in the SMTP envelope's mail from header.
Alignment | The signing domain aligns with the base domain in the message from header. | The domain in the SMTP envelope's mail from header aligns with the base domain in the message's from header.

DKIM alignment is more important than SPF, because only DKIM remains aligned
when a message is forwarded via a mailbox rule.

### DMARC reports

DMARC has two report types: aggregate and forensic. email recipients that
honor DMARC send these reports back to domain owners in emails sent to
addresses listed in the domain's DMARC record. There reports contain very
useful information for debugging message alignment and identifying malicious
spoofing campaigns.

Report type | Description
---|---
Aggregate (rua) | Compressed XML files sent at least once per day by recipient domains to the URIs listed in the rua DMARC tag. Records number of messages sent from an IP address, and the SPF and DKIM status. These reports are sent regardless of a success or failure, so that domain owners have a view of all mail authentication of messages appearing to be from their domain.
Failure/Forensic (ruf) | An email with an email that failed the DMARC check attached (RFC 822/.eml format) sent to the URIs listed in the ruf DMARC tag. These can be very useful for DMARC troubleshooting and phishing investigations. However, **most email recipients do not send forensic reports, or may only supply the message headers for privacy****reasons.**

### DMARC policies

DMARC requires domain owners to set a policy (p=) tag in their DMARC record.
This policy tells recipients how they should react to an email that appears to
come from that domain based on the message from header but does not pass DMARC
alignment.

Policy | Description
---|---
none | The Domain Owner requests no specific action be taken regarding delivery of messages. Use this first to ensure your messages are DMARC compliant before switching to quarantine or reject.
quarantine | The Domain Owner wishes to have email that fails the DMARC mechanism check be treated by Mail Receivers as suspicious. Depending on the capabilities of the Mail Receiver, this can mean "place into spam folder", "scrutinize with additional intensity", and/or "flag as suspicious".
reject | The Domain Owner wishes for Mail Receivers to reject email that fails the DMARC mechanism check. Rejection SHOULD occur during the SMTP transaction.

Even if a domain has a DMARC policy set to p=none, mail services may still
display warnings to their users in the event of a DMARC failure, as shown in
this screenshot of a valid email from a retail credit service, displayed in
[ProtonMail](https://protonmail.com/support/knowledge-base/email-has-failed-
its-domains-authentication-requirements-warning/) and Gmail.

[![A screenshot of ProtonMal showing a DMARC failure
warning](/assets/images/DMARC_failure_ProtonMail.png)](/assets/images/DMARC_failure_ProtonMail.png)

[![A creenshot of a DMARC failure warning in Gmail](/assets/images/Gmail-
DMARC-warning.png)](/assets/images/Gmail-DMARC-warning.png)

### Authentication-Results headers

As an email gateway evaluates SPF, DKIM, and DMARC, it adds the Message-
Authentication headers to the email. Users and administrators can use these
headers to determine which checks passed or failed, and why.

In the example above, the mail server mail17i.protonmail.ch added the
following headers to the email:

    Authentication-Results: mail17i.protonmail.ch; dmarc=fail (p=none dis=none) header.from=[redacted].com
    Authentication-Results: mail17i.protonmail.ch; spf=pass smtp.mailfrom=noreply_[redacted]_portal=[redacted].com__0-28eb251z589s1s@zihu5s1p6odwjt9p.s3cycftqbacrhjk9.hf76qay.3-1ffzneao.na45.bnc.salesforce.com
    Authentication-Results: mail17i.protonmail.ch; dkim=none

Email headers are added and read from the bottom to the top.

First, the server notes that the message has not been DKIM signed.

Then, SPF is checked, with a SMTP mail from header value of
noreply_[redacted]_portal=[redacted].com__0-28eb251z589s1s@zihu5s1p6odwjt9p.s3cycftqbacrhjk9.hf76qay.3-1ffzneao.na45.bnc.salesforce.com,
and SPF passed. A salesforce.com address was used so that Salesforce can keep
track of bouncebacks, and avoid sending to invalid email addresses in the
future. SPF passed.

Finally, DMARC is checked, which fails, because the message is not DKIM
signed, and the base of the SMTP mail from domain used by SPF (salesforce.com)
does not match the base domain in the message from header ([redacted].com).
dis=none (short for message disposition) indicates that the message was still
delivered, because the mail server noted that [redacted].com has a DMARC
policy of p=none.

The retail credit service should resolve the DMARC failures by configuring
Salesforce to DKIM sign the messages, and then publish the DKIM public key as
a DNS TXT record on [redacted].com.

**Note** : If you route your incoming email from one gateway service to
another, such as from an IronPort to Office 365, by the time an email reaches
a user's mailbox, the information from Office 365 in the Authentication-
Results header will always show that SPF and DMARC passed, since the IronPort
is authorized to send as your domains when messages are forwarded to Office
365. The results of the original IronPort check that occurs before the message
reaches Office 365 are stored in the Authentication-Results-Original header.

### DMARC policy DNS records

DMARC policy DNS records are placed at a TXT record at the _dmarc subdomain.
Subdomains of the TLD/base domain automatically inherit this DMARC policy
record, **or** they can have their own record at their own_dmarc subdomain.

Here is an example DMARC policy DNS record

    _dmarc.example.com TXT "v=DMARC1; p=none; rua=mailto:dmarc@example.com; ruf=mailto:dmarc@example.com"

#### Required DMARC policy DNS record tags

Tag | Description
----|------------
v   | DMARC version (e.g., `v=DMARC1`)
p   | DMARC policy

#### Recommended DMARC policy DNS record tags

These tags tell recipients where and how to send reports.

<table>
  <tbody>
    <tr>
      <td><strong>Tag</strong></td>
      <td>
        <strong>Value Description</strong>
      </td>
    </tr>
    <tr>
      <td><strong>v</strong></td>
      <td>
        <p>
          According to the RFC, this tag is recommended but not required, with
          an implicit default value of DKIM1.
        </p>
        <p>
          <strong
            >However, in practice, some recipients don’t follow the RFC exactly,
            and require this tag to be used anyway. This must be the first tag
            if used.</strong
          ><strong
            >Your DKIM public key records should start with v=DKIM1;</strong
          >
        </p>
      </td>
    </tr>
    <tr>
      <td><strong>n</strong></td>
      <td>
        Notes: Human-readable notes for administrators reviewing DNS records
        <p>
          <strong
            >Useful for noting which service uses a selector and key.</strong
          >
        </p>
      </td>
    </tr>
  </tbody>
</table>

#### Not recommended DMARC policy DNS record tags

Tag | Description
---|---
sp | **Default mirrors the p tag's value** Sets the policy for all subdomains. Setting this tag could allow the spoofing of any arbitrary subdomain. **Add a separate policy record for each subdomain as needed instead.**
pct |  **Default is 100** Sets the percentage of mail to apply the DMARC policy to. Set p=none when testing instead to ensure all mail is treated equally
adkim |  **Default is relaxed (r)** In relaxed mode, the Organizational Domains of both the DKIM-authenticated signing domain (taken from the value of the "d=" tag in the signature) and that of the RFC 5322 From domain must be equal if the identifiers are to be considered aligned.
aspf |  **Default is relaxed (r)** In relaxed mode, the SPF-authenticated domain and RFC5322 From domain must have the same Organizational Domain. In strict mode, only an exact DNS domain match is considered to produce Identifier Alignment.
rf |  A list separated by colons of one or more report formats as requested by the Domain Owner to be used when a message fails both SPF and DKIM tests to report details of the individual failure. Only "afrf" (the auth-failure report type) is currently supported in the DMARC standard.
ri |  **Default is 86400** Indicates a request to Receivers to generate aggregate reports separated by no more than the requested number of seconds. DMARC implementations MUST be able to provide daily reports and SHOULD be able to provide hourly reports when requested. However, anything other than a daily report is understood to be accommodated on a best-effort basis.

### DMARC authorization DNS records

If an email address in rua or ruf has a different base domain than the domain
of the policy record, an authorization record must be added to the base domain
of the email address to indicate that it accepts reports about that domain.
For example, if dmarc@example.com also needed to accept reports for
example.net, the poly record for example.net would look like this:

    _dmarc.example.net TXT "v=DMARC1; p=none; rua=mailto:dmarc@example.com; ruf=mailto:dmarc@example.com"

Because example.net is a different base domain than example.com, the following
record needs to be added to example.com to indicate that it accepts reports
about example.com:

    example.net._report._dmarc.example.com TXT "v=DMARC1"

## DMARC deployment steps

  1. Configure email gateways to honor DMARC records and send aggregate DMARC reports.
  2. Inventory domains.
  3. Deploy SPF.
  4. Deploy DKIM.
  5. Set up mailbox for receiving DMARC reports.
  6. Deploy DMARC DNS records.
  7. Monitor incoming DMARC reports.
  8. Adjust SPF, DKIM signing, and DMARC policies as needed.

## Calendar invites forwarded by Outlook violate DMARC

Calendar events from DMARC protected domains forwarded by outsiders using
Outlook will fail DMARC.  Unfortunately, unlike a normal forwarded email,
calendar events forwarded using Outlook are "sent on behalf of" the meeting
organizer. Instead of using the address of the person who forwarded the email
in the from header, Outlook uses the address of the meeting organizer.  The
address of the person who did the forwarding is placed in the Sender header,
which DMARC does not use.

[![A screenshot of a draft forward of a calendar event in Microsoft
Outlook](/assets/images/outlook-calendar-event-
forwarding.png)](/assets/images/outlook-calendar-event-forwarding.png)

If the domain of the meeting organizer has an enforced DMARC policy (i.e.,
p=quarantine, or p=reject), and the recipient mail server honors DMARC, the
message will not be delivered, because DMARC does not allow an unauthorized
mail server (i.e., the forwarding mail server) to send an email as the
organizer's domain.

This is a [known
problem](https://office365.uservoice.com/forums/264636-general/suggestions/34012756-forwarding-
of-calendar-appointments-from-a-dmarc-p) with Outlook that Microsoft has so
far not addressed. In the meantime, tell anyone who wants to forward calendar
events to do so by clicking on the three dots, and clicking Forward as
Attachment, instead of clicking on the usual Forward button.

[![A screenshot showing how to forward a calendar invite as an attachment in
Outlook](/assets/images/forward-calendar-invite-as-
attachment.png)](/assets/images/forward-calendar-invite-as-attachment.png)

On Outlook for macOS, calendar events must be forwarded by clicking on
Message> Forward as Attachment in the Menu Bar.

[![A screenshot of the Forward as attachment menu item in Outlook for
macOS](/assets/images/macos-outlook-forward-as-
attachment.png)](/assets/images/macos-outlook-forward-as-attachment.png)

### FAQs

#### How can I check a DKIM signature?

Send an email to a Gmail account. They have a nice UI that shows the DKIM
status of a message.

[![A screenshot showing how DKIM signature alignment can be verified using
Gmail's UI](/assets/images/DKIM-Gmail.png)](/assets/images/DKIM-Gmail.png)
A screenshot showing how DKIM signature alignment can be verified using
Gmail's UI

#### What if a third-party sender can't support DMARC?

  1. Some vendors don't know about DMARC yet; ask about SPF and DKIM/email authentication.
Check if they can send through your email relays instead of theirs.

  2. Do they really need to spoof your domain? Why not use the display name instead?
  3. Worst case, have that vendor send email as a specific subdomain of your domain (e.g. noreply@news.example.com), and then create separate SPF and DMARC records on news.example.com, and set p=none in that DMARC record.

**Do not** alter the p or sp values of the DMARC record on the Top-Level
Domain (TLD) - **that would leave you vulnerable to spoofing of your TLD
and/or any subdomain**.

[Further reading](https://dmarcian.com/what-to-do-about-non-dmarc-capable-
email-sources/) on this problem.

## How can I get more forensic reports?

Often, you will find a service that sends email that passes SPF alignment, but
not DKIM alignment, but you might not know which email workflow has the
problem, because you won't get many forensic reports, since at SPF is aligned.

Try setting fo=1 in your DMARC policy record.

By default, fo is implicitly set to 0. DMARC failure/forensic reports are only
sent if **all** authentication mechanisms (i.e., SPF and DKIM) fail to produce
an aligned "pass" result.

Setting fo=1 in the DMARC policy record will provide forensic/failure reports
if **any** authentication mechanisms fail.

This is noisy, but very useful for troubleshooting DKIM when SPF is passing,
Remove the fo tag, or set it to 0 once troubleshooting is complete.

## What about mailing lists?

When you deploy DMARC on your domain, you might find that messages relayed by
mailing lists are failing DMARC, most likely because the mailing list is
spoofing your from address, and modifying the subject, footer, or other part
of the message, thereby breaking the DKIM signature.

### Mailing list best practices

Ideally, a mailing list should forward messages without altering the headers
or body content at all. [Joe
Nelson](https://begriffs.com/posts/2018-09-18-dmarc-mailing-list.html) does a
fantastic job of explaining exactly what mailing lists should and shouldn't do
to be fully DMARC compliant. Rather than repeat his fine work, here's a
summary:

**Do**

+ Retain headers from the original message.
+ Add [RFC 2369](https://tools.ietf.org/html/rfc2369) List-Unsubscribe headers to outgoing messages, instead of adding unsubscribe links to the body.

        List-Unsubscribe: 

+ Add [RFC 2919](https://tools.ietf.org/html/rfc2919) List-Id headers instead of modifying the subject.

        List-Id: Example Mailing List 

Modern mail clients and webmail services generate unsubscribe buttons based on
these headers.

**Do not**

+ Remove or modify any existing headers from the original message, including From, Date, Subject, etc.
+ Add to or remove content from the message body, **including traditional disclaimers and unsubscribe****footers.**

In addition to complying with DMARC, this configuration ensures that Reply and
Reply All actions work like they would with any email message. Reply replies
to the message sender and Reply All replies to the sender and the list.

Even without a subject prefix or body footer, mailing list users can still
tell that a message came from the mailing list, because the message was sent
to the mailing list post address, and not their email address.

Configuration steps for common mailing list platforms are listed below.

#### Mailman 2 best practices

Navigate to General Settings, and configure the settings below

**Setting** | **Value**
------------|----------
**subject_prefix** |
**from_is_list** | No
**first_strip_reply_to** | No
**reply_goes_to_list** | Poster
**include_rfc2369_headers** | Yes
**include_list_post_header** | Yes
**include_sender_header** | No

Navigate to Non-digest options, and configure the settings below:

**Setting** | **Value**
---|---
**msg_header** |
**msg_footer** |
**scrub_nondigest** | No

Navigate to Privacy Options> Sending Filters, and configure the settings
below:

**Setting** | **Value**
---|---
**dmarc_moderation_action** | Accept
**dmarc_quarentine_moderation_action** | Yes
**dmarc_none_moderation_action** | Yes

#### Mailman 3 best practices

Navigate to Settings> List Identity

Make Subject prefix blank.

Navigate to Settings> Alter Messages

Configure the settings below:

**Setting** | **Value**
---|---
**Convert HTML to plaintext** | No
**Include RFC2369 headers** | Yes
**Include the list post header** | Yes
**Explicit reply-to address** |
**First strip reply-to** | No
**Reply goes to list** | No munging

Navigate to Settings> DMARC Mitigation

Configure the settings below

**Setting** | **Value**
---|---
**DMARC mitigation action** | No DMARC mitigations
**DMARC mitigate unconditionally** | No

Create a blank footer template for your mailing list to remove the message
footer. Unfortunately, the Postorius mailing list admin UI will not allow you
to create an empty template, so you'll have to create one using the system's
command line instead, for example:

    touch var/templates/lists/list.example.com/en/list:member:regular:footer

Where `list.example.com` the list ID, and `en` is the language.

Then restart mailman core.

### Mailing list workarounds

If a mailing list must go **against** best practices and modify the message
(e.g., to add a required legal footer), the mailing list administrator must
configure the list to replace the from address of the message (also known as
munging) with the address of the mailing list, so they no longer spoof email
addresses with domains protected by DMARC.

Configuration steps for common mailing list platforms are listed below.

#### Mailman 2 workaround

Navigate to Privacy Options> Sending Filters, and configure the settings below

**Setting** | **Value**
---|---
**dmarc_moderation_action** | Munge From
**dmarc_quarentine_moderation_action** | Yes
**dmarc_none_moderation_action** | Yes

**Note**

Message wrapping could be used as the DMARC mitigation action instead. In that
case, the original message is added as an attachment to the mailing list
message, but that could interfere with inbox searching, or mobile clients.

On the other hand, replacing the `from` address might cause users to
accidentally reply to the entire list, when they only intended to reply to the
original sender.

Choose the option that best fits your community.

#### Mailman 3 configuration

In the DMARC Mitigations tab of the Settings page, configure the settings
below:

**Setting** | **Value**
---|---
**DMARC mitigation action** | Replace From: with list address
**DMARC mitigate unconditionally** | No

**Note**

Message wrapping could be used as the DMARC mitigation action instead. In that
case, the original message is added as an attachment to the mailing list
message, but that could interfere with inbox searching, or mobile clients.

On the other hand, replacing the `From` address might cause users to
accidentally reply to the entire list, when they only intended to reply to the
original sender.

Choose the option that best fits your community.

#### LISTSERV

[LISTSERV 16.0-2017a](https://www.lsoft.com/news/dmarc-issue1-2018.asp) and
higher will rewrite the from header for domains with a DMARC quarantine or
reject policy.

Some additional steps are needed for Linux hosts.

## DMARC deployment guides

+ [NIST Special Publication 800-177 - Trustworthy Email](https://doi.org/10.6028/NIST.SP.800-177r1)
+ [DMARC Overview](https://dmarc.org/overview/)
+ [Proofpoint Email Authentication Guide](/assets/images/Proofpoint-Email-Authentication-Guide.pdf)
  + **[Proofpoint does not currently send any DMARC reports](https://seanthegeek.net/806/proofpoint-is-forcing-their-customers-to-pay-for-email-fraud-defense-to-get-aggregate-dmarc-data-from-their-own-gateways/)
**

+ [DMARC guide for G Suite](https://www.youtube.com/watch?v=WB-aUZMDnU8)
+ [DMARC guide for Office 365](https://technet.microsoft.com/en-us/library/mt734386\(v=exchg.150\).aspx)
  + Note: [**Office 365 does not currently send any DMARC reports**](https://office365.uservoice.com/forums/264636-general/suggestions/11094318-dmarc-aggregate-reports-from-o365-domains), but you can analyze DMARC data from Office 365 using the free[Valimail Monitor for Office 365](https://www.microsoft.com/security/blog/2019/06/03/secure-cloud-free-dmarc-monitoring-office-365/) service
+ [Complete DKIM and DMARC deployment guide for Cisco AsyncOS](/assets/images/AsyncOS-DKIM-DMARC-Guide.pdf)
+ [Generic DMARC Deployment guide - Dmarcian](https://space.dmarcian.com/deployment/)
+ [List of DMARC Support Status of SaaS Services - Dmarcian](http://dmarc.io/sources/)
+ [DMARC Guide for 3rd Party Senders - Dmarcian](https://space.dmarcian.com/how-to-send-dmarc-compliant-email-on-behalf-of-others/)
+ [Solutions to common problems - Dmarcian](https://dmarcian.com/category/deployment/)
+ [Reference library by OnDMARC](https://knowledge.ondmarc.com/)
+ [SPF Deployment Guide - MSDN](http://blogs.msdn.com/b/tzink/archive/2013/04/24/how-to-set-up-your-spf-records-if-you-are-outsourcing-some-or-all-of-your-email.aspx)
+ [RFC 7489](https://tools.ietf.org/html/rfc7489)

## SPF and DMARC record validators

+ [checkdmarc](https://domainaware.github.io/checkdmarc/) - A Python module and CLI tool I wrote to validate and parse SPF and DMARC records
+ [trustymail](https://github.com/dhs-ncats/trustymail) - By DHS; checks for compliance with BOD 18-01, including SPF, DMARC, and STARTTLS
+ [DNS Checker](https://dnschecker.org/) - Check DNS propagation worldwide

## DMARC report processing services

+ [Agari](https://www.agari.com/dmarc/) - Most popular provider to federal agencies, partners with ISACs and others - "Contact us" pricing
+ [Dmarcian](https://dmarcian.com/) - Public, [straightforward pricing](https://dmarcian.com/pricing/), free public [reference](https://space.dmarcian.com/deployment/)[guides](https://space.dmarcian.com/deployment/)
+ [OnDMARC](https://ondmarc.com/) - [Low cost](https://ondmarc.com/pricing) services, extensive free public [reference guides](https://knowledge.ondmarc.com/)
+ [Proofpoint Email Fraud Defense](https://www.proofpoint.com/us/products/email-fraud-defense) - "Contact us" pricing; most useful for current Proofpoint customers
+ [Valimail](https://www.valimail.com/) - Offers [automated SPF/DKIM/DMARC DNS record generation](https://www.valimail.com/why-valimail/#automate-dmarc-enforcement)
+ [parsedmarc](https://domainaware.github.io/parsedmarc/) - Open source self-hosted DMARC report processing and analytics

## DMARC adoption

+ [Email Authentication Policy and Deployment Strategy for Financial Services Firms](http://www.fsroundtable.org/wp-content/uploads/2015/05/BITSEmailAuthenticationFeb2013.pdf) (BITS/The Financial Services Roundtable - Feb. 2013)
+ [DHS Binding Operational Directive (BOD) 18-01](https://cyber.dhs.gov/bod/18-01/) (Oct. 2017)
+ [Fifty-Seven Percent of Email "From" Healthcare Industry is Fraudulent](https://nhisac.org/announcements/fifty-seven-percent-email-healthcare-industry-fraudulent/) (H-ISAC - Nov. 2017)

## DMARC compliant services

### Blackbaud

Payment and CRM solutions for non-profits

+ <https://www.blackbaud.com/solutions>
+ <https://docs.blackbaud.com/email-resource-center/faqs/best-practices-faq#what-is-an-spf-record-and-how-do-i-create-it>
+ <https://kb.blackbaud.com/articles/Article/65862>

### Constant Contact

+ <https://www.constantcontact.com/email-marketing>
+ <https://www.constantcontact.com/pricing>
+ <https://knowledgebase.constantcontact.com/guides/KnowledgeBase/5932-self-publishing-for-authentication>

### Cvent

Cvent planner supports alignment via SPF and DKIM.

Add the following to your SPF record:

include:cvent-planner.com

Contact [Cvent support](https://www.cvent.com/en/contact/customer-support) to
set up DKIM signing as your domain.

+ <https://www.cvent.com/>
+ <https://knowledge.ondmarc.com/articles/1977363-cvent-planner-spf-and-dkim-set-up>

### Emma

+ <https://myemma.com/pricing>
+ <https://support.e2ma.net/Resource_Center/Account_how-to/deliverability-best-practices#5._Authenticate_your_sending_domain>

### Elastic Email

Reasonably priced, fully DMARC compliant marketing and transactional email.

+ <https://elasticemail.com/pricing/>
+ <https://elasticemail.com/marketing-features/>
+ <https://elasticemail.com/transactional/>
+ <https://elasticemail.com/resources/settings/spf-dkim-tracking-faq/>

### GlobalCert SecureMail Gateway

+ <https://support.globalcerts.net/portal/kb/articles/dkim-signatures>

### HealthcareSource

Healthcare talent management SaaS. Contact support and let them know that you
need SPF and DKIM set up for DMARC alignment.

+ <https://www.healthcaresource.com/>
+ [support@healthcaresource.com](mailto:support@healthcaresource.com)

### HubSpot

Good option if a full Customer Relationship Management (CRM) platform is
needed.

+ <https://www.hubspot.com/pricing/marketing>
+ <https://www.hubspot.com/products/marketing>
+ <https://knowledge.hubspot.com/articles/kcs_article/email/can-i-use-a-dmarc-policy-with-hubspot>

### JangoMail

Full-featured email marketing

Add include:jangomail.com to your SPF record.

+ <https://jangomail.com/features/>
+ <https://jangomail.com/pricing/>
+ <https://jangomail.com/send-email-via-api/>
+ [https://jangomail.com/domainkeysdkim/](https://seanthegeek.net/392/stop-ada-education-reform-act/)

### JangoSMTP

Transactional email service used by IBM Phytel (see separate entry below) and
others.

Add include:jangomail.com to your SPF record.

+ <https://jangosmtp.com/features/>
+ <https://jangosmtp.com/pricing/>
+ <https://jangomail.zendesk.com/hc/en-us/articles/200660154-DomainKeys-DKIM>

### MailChimp

Extremely cheap bulk marketing email; extremely expensive transactional email.

+ [https://kb.mailchimp.com/accounts/email-authentication/verify-a-domain#Verify-Domain-in-Account-Settings](https://kb.mailchimp.com/accounts/email-authentication/verify-a-domain)
+ <https://kb.mailchimp.com/accounts/email-authentication/set-up-custom-domain-authentication-dkim-and-spf>

### Mandrill

A MailChimp add-on service for transitional email

+ <https://kb.mailchimp.com/mandrill/mailchimp-vs-mandrill>
+ <http://mandrill.com/pricing/>
+ <https://mandrill.zendesk.com/hc/en-us/articles/205582267-What-are-SPF-and-DKIM-and-do-I-need-to-set-them-up>
+ Set SMTP envelope sender for SPF alignment in the Mandrill dashboard
Settings -> Domains -> Tracking and Return Path Domain

### Mailgun

+ <https://www.mailgun.com/pricing>
+ <https://documentation.mailgun.com/en/latest/user_manual.html#verifying-your-domain>

### Mailjet

Email and SMS marketing**.**

+ [https](https://www.mailjet.com/pricing/)[://www.mailjet.com/pricing/](https://www.mailjet.com/pricing/)
+ <https://www.mailjet.com/docs/spf-dkim-guide>

### Net-Results

Marketing automation

+ <https://www.net-results.com/pricing/>
+ <http://support.net-results.com/index.php/Domain_Branding>

### OnSolve Mir3

Mass notification system for employees, contractors, students, etc.

Mir3 supports DKIM alignment via DKIM.

Contact your Mir3 account manager to have them set up DKIM signing/email
whitelabeling.

+ <https://www.onsolve.com/solutions/products/mir3/>
+ <https://www.onsolve.com/resources/support/>

### Phytel (sent via JangoSMTP)

IBM Phytel is used by healthcare providers to send appointment reminders and
other information to their patients. Emails are relayed through JangoSMTP.

Add include:jangomail.com to your SPF record.

Contact IBM Phytel support and ask them to configure DKIM signing.

+ [PhytelClientCare@us.ibm.com](mailto:PhytelClientCare@us.ibm.com)
+ <https://www-01.ibm.com/support/docview.wss?uid=ibm10716407>
+ <https://www.ibm.com/watson-health/phytel>

### Safe Pay Services

A payment processor that supports DMARC alignment via SPF and DKIM.

Add a:mail.safepayservices.com to your SPF record.

Contact support for details.

+ <https://safepayservices.com/services>
+ <https://safepayservices.com/contact>

### Salesforce Marketing Cloud

+ <https://www.salesforce.com/editions-pricing/marketing-cloud/>
+ <https://www.salesforce.com/products/marketing-cloud/email-marketing/>
+ [https://help.salesforce.com/articleView?id=emailadmin_create_secure_dkim.htm&type=5](https://help.salesforce.com/articleView?id=emailadmin_create_secure_dkim.htm&type=5)

### SendGrid

+ <https://sendgrid.com/solutions/email-marketing/>
+ <https://sendgrid.com/pricing/>
+ <https://sendgrid.com/docs/ui/account-and-settings/how-to-set-up-domain-authentication/>

### Sendinblue

Not as cheap as Elastic Email, but cheaper than SendGrid and Mandrill, with
options for SMS.

+ <https://www.sendinblue.com/pricing/>
+ <https://www.sendinblue.com/features/>
+ <https://help.sendinblue.com/hc/en-us/articles/209577385-Understand-SPF-DKIM-and-DMARC-protocols>

### Simplee

B2C medical billing

According to Simplee support as of 2019-05-23, in order to support DKIM
signing, they need to purchase a domain authentication package from
Salesforce, with the cost passed on to the customer, and have the Simplee
customer delegate a domain or subdomain to Salesforce via NS records:

+ ns1.exacttarget.com
+ ns2.exacttarget.com
+ ns3.exacttarget.com
+ ns4.exacttarget.com

Costs include:

+ One-time setup fee: $350 for Simplee to cover implementation and setup costs
+ Annual Fee: $1,500 per year per domain (pass-through expense via Salesforce) + $39 Salesforce Purchase Order Fee

For for information, contact Simplee support at
<https://support.simplee.com/hc/en-us/requests/new>

### Symantec MessageLabs

+ <https://support.symantec.com/en_US/article.HOWTO126432.html>

## Services that must use your SMTP relays to be fully DMARC compliant

+ [Qualtrics](https://www.qualtrics.com/support/survey-platform/distributions-module/email-distribution/using-a-custom-from-address/#SettingUpAnSMTPRelay)
+ [ServiceNow](https://docs.servicenow.com/bundle/jakarta-servicenow-platform/page/administer/reference-pages/task/t_ConfAltEmailUsgOwnSMTP.html)

## Incompatible services

Some services do not do any DKIM signing, or use their own domain came in the
DKIM d= tag, making the signature unaligned with the message from address
domain they are spoofing.

There are different two ways to work around this problem, each with its own
benefits and drawbacks:

  1. Have the vendor send emails from their domain instead of yours
  2. Configure the service to use a specific subdomain of your domain in the message from address. Then, create a separate DMARC record with p=none under that specific subdomain.

By having a service send as its own domain, you loose branding in the from
email address, but it will not cause additional complexity or risk.

Publishing a DMARC p=none policy on a specific subdomain allows spoofing of
that specific subdomain, without weakening DMARC enforcement for other
subdomains, or the top level domain. This allows you to keep your domain in
the from address, **but also opens up that specific subdomain to spoofing from
anyone**.

### UL PureSafety

DKIM signing as customer domains is not currently supported by UL PureSafety
OHM.
Most outbound email notifications in OHM are configured by the customer,
including the From address they will be sent with. The user(s) should go
through the screens where they have set them to various customer addresses and
change them to a generic puresafety.com address, such as
"DoNotReply@puresafety.com." They should also update the Body of each email
template to include appropriate contact information.

### Volgistics

Volgistics does not currently support DKIM signing, so the account
administrator will need to complete the following steps to configure
Volgistics to send email as Volgistics.com:

  1. Choose Setup from the menu in the account
  2. Expand Messages
  3. Click the "Ground Rules" link
  4. In the "From address" section, select the "Use VolunteerMail@volgistics.com as the from address (recommended)" option
  5. Click the Save button

## Bonus steps

These steps aren't required to deploy DMARC, but they can help to make your
email more secure.

### Verify TLS

TLS ensures that messages are encrypted on their way to your mail servers.
STARTTLS allows email clients to upgrade from a plan text connection to an
encrypted one.

To check `STARTTLS`, run:

`openssl s_client -connect mail.example.com:25 -starttls smtp`

To check the standard secure SMTP port, run:

`openssl s_client -connect mail.example.com:465`

You can also check SMTP TLS using [MX
Toolbox](https://mxtoolbox.com/diagnostic.aspx) or [Check
TLS](https://www.checktls.com/TestReceiver).

[checkdmarc](https://domainaware.github.io/checkdmarc/) also checks for TLS
and STARTTLS.

### Brand Indicators for Message Identification (BIMI)

[Brand Indicators for Message Identification
(BIMI)](https://authindicators.github.io/rfc-brand-indicators-for-message-
identification/) is an emerging standard that some mail applications/services
are starting to follow (currently only Yahoo, with more services throughout
2019) . When a mail client uses BIMI, it first checks to see if the message
passed DMARC alignment. If the DMARC policy is set to enforcement (i.e.
p=quarentine or p=reject) and DMARC alignment has passed, the mail/webmail
client then checks for a BIMI assertion record at the message from domain.
This record points the client to a SVG file publicly hosted on a web server,
which is then displayed in the client UI, next to the message from
information.

![Screenshots of an email with and without BIMI in Outlook
webmail](https://blog.returnpath.com/wp-content/uploads/2018/08/Screen-
Shot-2018-08-30-at-10.01.10-AM.png)

To set up BIMI, host a SVG graphic file at a publicly accessible HTTPS URL,
then add a BIMI assertion TXT DNS record like this one.

`default._bimi.example.com TXT "v=BIMI1; l=https://cdn.example.com/logo.svg"`

You can validate a BIMI record and logo format at the [Mailkit BIMI
inspector](https://www.mailkit.com/resources/bimi-inspector), which also gives
you nice previews of what your BIMI logo would look like in a mail client.

What is currently missing is a way to validate that an entity using a domain
actually owns the rights to use a logo, so BIMI isn't widely used yet. In May
2018, Valimail, Google, and Standcore published a [draft
standard](https://tools.ietf.org/html/draft-bkl-bimi-overview-00) for solving
this problem by authenticating BIMI logos using certificates, similar to how
Certificate Authorities (CAs) work for SSL certificates today, but there isn't
a public timeline for when this might be adopted for BIMI and/or Google.
Currently, Yahoo is the only major mail provider showing BIMI logos out of the
box.

Microsoft has their own non-BIMI beta process for validating and displaying
logos called [Business Profiles](https://business.microsoft.com/).

if you would like more information about BIMI, email
[info@authindicators.org](mailto:info@authindicators.org); or if you are a
customer of Aguri, Return Path, or Valimail (Who are members of the
AuthIndicators Working Group responsible for the BIMI standard), contact their
support for more information.
