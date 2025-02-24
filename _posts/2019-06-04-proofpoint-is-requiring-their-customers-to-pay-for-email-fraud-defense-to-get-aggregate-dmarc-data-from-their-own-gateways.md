---
layout: post
permalink: /806/proofpoint-is-requiring-their-customers-to-pay-for-email-fraud-defense-to-get-aggregate-dmarc-data-from-their-own-gateways/
title: Proofpoint is requiring their customers to pay for Email Fraud Defense to get
  aggregate DMARC data from their gateways
description: In order to get aggregate DMARC data on mail flowing through their own
  gateways, Proofpoint customers must purchase Proofpoint Email Fraud Defense
date: 2019-06-04 04:31:21 -0000
last_modified_at: 2023-08-17 20:19:57 -0000
publish: true
pin: false
image:
  path: /assets/wp-content/uploads/2019/06/Proofpoint-DMARC-dashboard.webp
  alt: A redacted screenshot of the Proofpoint Email Fraud Defense dashboard
categories:
- Information Security
- Reviews
tags:
- DMARC
- email
- Proofpoint
---
I have written extensively about the DMARC email security standard, including publishing a [comprehensive guide][dmarc_guide] on how to implement it, with or without additional third-party vendors. I also do a little consulting on DMARC deployment best practices. One of those consulting clients uses Proofpoint for their email gateway. They also use Dmarcian, a reasonably priced DMARC report analytics service that also publishes a ton of [public content][dmarc.io] for the good of the community. We were considering moving the client's DMARC policy from monitor only (`p=none`) to an enforced state (`p=reject`) after many hours of steadily improving the SPF and DKIM alignment of their email sources. As I took another look at the aggregate (rua) DMARC data in Dmarcian, I noticed something odd: Dmarcian was getting aggregate reports from all of the expected third-party email recipients, like Google, Yahoo, Comcast, and the client's industry partners, but I didn't see any reporting from the client's own Proofpoint Secure Email Gateway (SEG).

This is a problem, because that meant Dmarcian wasn't seeing who was spoofing the client's domain in emails bound for the client's own gateways. We were blind to potential phishing activity, and critical items like payroll could break if we switched to an enforced DMARC policy without aggregate data from the Proofpoint gateway. Surely, I thought, there must be some configuration option in the Proofpoint console I was overlooking. I've never been a Proofpoint customer, so I reached out to some information security partners who are Proofpoint email gateway customers to find out what was going wrong. The answer was simple, infuriating, and confirmed by Proofpoint sales engineers: Proofpoint does not provide DMARC aggregate/rua reports to DMARC analytics inboxes, even though sharing those reports is a
cornerstone of the DMARC standard.

Proofpoint does provide aggregate DMARC data about the mail traffic flowing through a customer's gateway, but only via Proofpoint's own DMARC report
[analytics offering][efd], Proofpoint Email Fraud Defense (EFD). In essence, Proofpoint is ensuring that only their EFD offering provides their existing email gateway customers with the full picture needed to deploy DMARC, at an additional cost, of course.

## Workaround

As a less-than0ideal workaround for this problem, Proofpoint customers can create a Policy Route that matches on message `From` headers that end with their domains, and then create a DMARC policy in Proofpoint that applies to that route and configure the policy to copy any messages that fail DMARC to a separate quarantine folder for later review. That way, they can at least get samples of the emails that failed DMARC, even though they won't show up in third party DMARC analytics solutions.

### Create email authentication quarantine folders

Navigate to **System> Quarantine > Folders**, and add two new folders.

#### Email authentication failures

 Proofpoint will be configured to copy emails to this folder that fail DMARC with a message from header from domain that has a DMARC policy of quarantine or reject. That way, it is easy to see which  emails are being blocked from delivery by DMARC. This is useful for gathering threat intelligence, and for potential troubleshooting with domain owners who have prematurely set an enforced DMARC policy.

 Set the quarantine folder disposition to delete messages after **30 days**.

#### Email authentication failures from our domains

Proofpoint will be configured to copy emails to this folder if they fail DMARC with a message from header domain that matches one of your domains. This makes it easy to view the DMARC failures from only the domains that you control. Another key difference is, we will configure Proofpoint to copy messages here even if the DMARC policy is set to monitor only (`p=none`). That way, email sources that are failing DMARC can be identified and fixed before moving the the domain to an enforced DMARC policy (`p=quarantine` or `p=reject`).

 Set the quarantine folder disposition to delete messages after **30 days**.

### Create a new Policy Route

Navigate to **System> Policy Route**.

Set the Route ID to `from_our_domains`, and add a new Policy Route. Set the Description to "Emails with a message header from domain matching one of our domains"

Add a new condition to this Policy Route **for each of your domains**.

Condition: **Message Header From (Address Only)**
Operator: **Ends With**
Value: `@example.com`

Where `example.com` is your domain name.

**Warning**: It is important to use the **Ends With** operator, and start the value with `@`. Otherwise, the condition could match `badexample.com`.

### Configure the DMARC policies

#### Edit the default DMARC policy rules

1. Navigate to **Email Protection> Email Authentication> DMARC> Rules**
2. Select the `default` DMARC policy.

##### default quarantine rule

1. Edit the `quarantine` rule.
2. Set the **quarantine folder** to **Email authentication failures**.
3. Set the **Delivery Method** to **Discard**.
4. Click **Save Changes**.

##### default reject rule

1. Edit the `reject` rule.
2. Check **Quarantine message…** and select the **Email authentication failures** folder.
3. Set the **Delivery Method** to **Reject**
4. Click **Save Changes**.

##### default none rule

1. Edit the `none` rule.
2. Set the **quarantine folder** to **Email authentication failures**.
3. Set the **Delivery Method to** to **Continue**.
4. Click **Save Changes**.

#### Create a new from_our_domains DMARC policy

1. Navigate to **Email Protection> Email Authentication> DMARC> Policies**.
2. Create a new DMARC policy called `from_our_domains`
with a **Description** of "Emails with a  message header from domain matching one of our domains".

#### Edit the from_our_domains DMARC policy rules

1. Navigate to **Email Protection> Email Authentication> DMARC> Rules**.
2. Select the `from_our_domains` DMARC policy.
3. Move the `from_our_domains` Policy Route from the **Available** list to the **Require Any Of list**.

##### from_our_domains quarantine rule

1. Edit the `quarantine` rule.
2. Set the **quarantine folder** to **Email authentication failure from our domains**.
3. Set the **Delivery Method** to **Discard**.
4. Click **Save Changes**.

##### from_our_domains reject rule

1. Edit the `reject` rule.
2. Check **Quarantine message…** and select the **Email authentication failures from our domains** folder.
3. Set the **Delivery Method** to **Reject**
4. Click **Save Changes**.

##### from_our_domains none rule

1. Edit the `none` rule.
2. Set the **quarantine folder** to **Email authentication failures from our domains**.
3. Set the **Delivery Method to** to **Continue**.
4. Click **Save Changes**.

## Proofpoint Email Fraud Defense (EFD) features

Here is a detailed breakdown of all of the Proofpoint EFD [features][efd].

## Consultants

Proofpoint provides consultants to help customers to deploy DMARC. My health system client graciously kept me on as a consultant. We all worked well together, and I got a first-hand look at how EFD and other Proofpoint products work.

### Hosted authentication records

Proofpoint EFD offers the ability to host SPF, DKIM, and DMARC DNS records for a customer's domain and manage them through the EFD UI. This allows EFD administrators (e.g., SecOps/SecArch/email team/Proofpoint consultant, etc.) to make changes without needing full DNS write access, which simplifies changes while reducing risk, and reducing the number of people who would need to be involved in a DNS change. But, it also causes a some vendor lock-in by making it harder to move away from Proofpoint EFD if desired.

#### Hosted SPF

SPF records are made up of mechanisms. Most of those mechanisms require one or more DNS lookups. However, the SPF standard limits the number of DNS lookups to 10, which can be a problem if you send as many different services that each want to be added to your domain's SPF record.

Hosted SPF in Proofpoint EFS solves this problem by replacing the mechanisms in a domain's SPF record with a single `include` mechanism that looks like this:

```text
include:%{ir}.%{v}.%{d}.spf.has.pphosted.com
```

[SPF macros][spf_macros] are used in the `include` mechanism so that Proofpoint servers can dynamically decide if an email should pass SPF based on entries in EFD every time the SPF record is queried. Customers can load as many SPF entries as they want in EFD.

The only downside for customers using Hosted SPF is that it becomes more difficult to stop using Proofpoint EFD if desired. A customer would need to figure out which SPF mechanisms are necessary up to 10 DNS lookups and allow other email sources to be authenticated by DKIM alone, which does not have a limit on the number of sources.

#### Hosted DKIM

Hosted DKIM works by delegating a domain's `_dkim` subdomain to Proofpoint EFD using `NS` DNS records. Like hosted SPF, this allows DKIM keys to be added to a domain using the EFD UI, but makes moving away from EFD a little more complicated.

#### Hosted DMARC

Hosted DKIM works by delegating a domain's `_dmarc` subdomain to Proofpoint EFD using `NS` DNS records. This allows the domain's DMARC policy to be set using the EFD UI.

### Email visibility

What Proofpoint marketing calls "360-degree visibility" is just visualizations of DMARC data that you would get from any other DMARC analytics tool if Proofpoint properly followed the DMARC protocol. This includes which vendors have sent emails as your domain and their DMARC pass rate, and what unauthorized senders have sent emails as your domain.

### Identification of lookalike domains

Proofpoint EFD can identify lookalike domains as they are registered and when emails from those domains are delivered to your users. A nice feature that goes beyond DMARC.

### Supplier risk

Supplier risk identifies suppliers based on email data and checks their DMARC records. You could do the same thing semi-manually by looking up vendors in DMARC results and email logs and checking their DMARC records using tools like MX Toolbox or checkdmarc.

### Integration with Proofpoint email gateway

You can create DMARC policy overrides for the email gateway from EFD.

### DMARC visibility for Microsoft 365

Proofpoint EFD can work even if you use Microsoft as your email gateway and not Proofpoint. This really isn't an added feature, although Proofpoint markets it as one. Every DMARC analytics tool can do this, because unlike Proofpoint's gateway. Microsoft 365 follows the DMARC standard and provides DMARC aggregate reports.

## Impact

Proofpoint not sending aggregate DMARC reports has impacts beyond Proofpoint SEG and EFD. Even if a Proofpoint customer employs the above workaround, or pays for Email Fraud Defense, the lack of shared aggregate data harms non-Proofpoint users. Domain owners aren't getting the valuable DMARC feedback they need from Proofpoint mail recipients to identify email delivery problems and malicious campaigns. For example, consider a situation where a third-party supplier happens to mostly have customers that use Proofpoint SEG. If there was an issue with their email alignment or deliverability, they would have no idea. They would also be blind to any malicious spoofing of their domain targeting their customers who use Proofpoint.

## An open message to Proofpoint leadership

If Proofpoint started sending out RUA reports today, EFD still has useful features that are helpful for customers while also increasing lock-in to Proofpoint EFD – particularly hosted SPF and hosted DKIM.

DMARC can only be successful if everyone implementing it does the bare minimum effort of honoring DMARC policies by default, including sending out DMARC aggregate/rua reports to all services. By only sharing aggregate DMARC data in Email Fraud Defense service, Proofpoint is valuing vertical integration and market capture over the trustworthiness of email for all, including their own email gateway customers. Proofpoint EFD would not be possible if every other major email service and gateway wasn't doing their part by providing aggregate reports.

Please start honoring DMARC policies by default and sending proper DMARC aggregate/rua reports to everyone according to the RFC by default.

[dmarc_guide]: /459/demystifying-dmarc/
[dmarc.io]: https://dmarc.io/
[spf_macros]: https://www.jamieweb.net/blog/using-spf-macros-to-solve-the-operational-challenges-of-spf/
[efd]:https://www.proofpoint.com/us/products/email-fraud-defense
