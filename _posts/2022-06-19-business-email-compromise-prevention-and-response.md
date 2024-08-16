---
layout: post
permalink: /1234/business-email-compromise-prevention-and-response
title: Business Email Compromise prevention and response
description: A practical guide to preventing Business Email Compromise by using defense-in-depth
  techniques, multi-factor authentication, and training
date: 2022-06-19 22:27:21 -0000
last_modified_at: 2022-06-21 13:26:19 -0000
publish: true
pin: false
image:
  path: /assets/wp-content/uploads/2022/06/istock-phishing-laptop.png
  alt: An illustration of a phishing attack
categories:
- Information Security
tags:
- BEC
- email
- phishing
- social engineering
---
Business Email Compromise (BEC) attacks are easy, cheap, and often very
effective. This high Return on Investment makes BEC an extremely popular with
attackers of any skill level--from low-level scammers to state-sponsored
groups. BEC occurs when an attacker is able to access an email inbox within a
business. From there, an attacker examine sensitive emails, insert themselves
into email threads, and spread phishing emails from the trusted email account.
While BEC can be devastating to the finances, reputation, and operations of
any business, small businesses are particularly vulnerable. Fortunately. the
defenses against BEC such as multi-factor authentication and user training are
also simple, cheap and effective.

## BEC defense TL;DR

* Require Multi-Factor Authentication (MFA) for all user accounts
  * Hardware security keys are the most secure method, but they can be expensive to deploy to a large number of users
    * [Yubikey](https://www.yubico.com/products/)
  * Time-Based One Time Passwords (TOTP) are the second-best option
  * Push notifications are convenient but risky
  * Text/SMS and phone calls options have the weakest security
  * [Google Workspace](https://support.google.com/a/answer/175197) (formerly G Suite) MFA setup instructions
  * [Microsoft 365](https://docs.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/set-up-multi-factor-authentication?view=o365-worldwide) (formerly Office 365) MFA setup instructions
  * [Okta](https://support.okta.com/help/s/end-user-adoption-toolkit/setting-up-mfa-for-end-users?language=en_US) MFA setup instructions
* Set retention policies
  * [Google Workspace](https://support.google.com/vault/answer/2990828) (formerly G Suite) instructions
  * [Microsoft 365](https://docs.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/set-up-multi-factor-authentication?view=o365-worldwide) (formerly Office 365) instructions
* Extra credit
  * [Implement DMARC](https://seanthegeek.net/459/demystifying-dmarc/) to prevent unauthorized spoofing of your domains in email From headers. This can take a lot of time and effort.
* Train users
  * Hover over [press and hold on mobile] links to check them before clicking/tapping on them
  * Check the browser address bar before using a form
  * Watch out for lookalike domains
  * Be suspicious of any unexpected email, text/SMS message or phone call -- even if it appears to be from a trusted source
  * Validate any unexpected request or change in process (such as a change in payment instructions) by calling a known good phone number and speaking with a trusted contact
  * High risk users should use strong authentication methods and be especially cautious
    * Executives and their assistants
    * Bookkeepers
    * Procurement staff
    * Accounts payable staff
    * Anyone with access to confidential information

Read on to learn more about how to prevent Business Email Compromise at each
stage of the attack.

## External reconnaissance

Before launching a BEC attack, attackers will collect publicly available
information called Open Source Intelligence (OSINT) to select their targets
and better tailor their attacks to those targets. For example, website About
Us pages and LinkedIn profiles, and press releases. A simple Google search
will return websites marketing websites that store the email address format
for a wide variety of organizations.

Of course businesses must make this information public in order to do
business. It is critical for businesses to understand which users are at high
risk for being targeted based on their public profile or role, so those users
know to be extra vigilant. Frequent targets include executives and their
assistants, bookkeepers, procurement staff, accounts payable staff, IT staff,
and anyone with access to confidential information.

## Credential harvesting

The most common way for an attacker to gain unauthorized access to an email
account is through a technique called credential harvesting, where the victim
is tricked into entering their username and password into a fake form that
sends the credentials to an attacker. Targets can be lured to credential
harvesting websites by a phishing email, text message (smishing), or even a
phone call. (vishing). Credential harvesting sites are designed to look
identical to real login forms or password reset forms. Well-built credential
harvesting pages will even redirect the victim to the real login form after
the credentials have been stolen, so the user just thinks it's a glitch and
logs into the real service. From there, attackers can take actions as the
compromised user account, and/or sell the credentials to other scammers in
underground markets on the dark web. Targets and their security teams can
sometimes glean details about the attackers by [examining how the credential
harvesting page operates](https://seanthegeek.net/1069/how-to-examine-a-
credential-harvesting-page-using-microsoft-edge/).

![A screenshot of fake Microsoft login form used for credential harvesting, a
common first step of Business Email Compromise \(BEC\)](/assets/wp-content/uploads/2022/06/fake-login-page.webp)  
Screenshot by [Raymond Tec](https://raymondtec.com/2020/06/german-task-force-
for-covid-19-medical-equipment-targeted-in-ongoing-phishing-campaign/)

### Phishing awareness and user training

The first line of defense against any phishing is user awareness and training.
Conduct frequent phishing simulations, and train users on email security best
practices.

* Hover over [press and hold on mobile] links to check them before clicking/tapping on them
* Check the browser address bar before using a form
* Watch out for lookalike domains
* Be suspicious of any unexpected email, text/SMS message or phone call -- even if it appears to be from a trusted source
* Validate any unexpected request or change in process (such as a change in payment instructions) by calling a known good phone number and speaking with a trusted contact
* High risk users should be especially careful
  * Executives and their assistants
  * Bookkeepers
  * Procurement staff
  * Accounts payable staff
  * Anyone with access to confidential information

### Multi-factor authentication

To defend against credential harvesting, businesses must implement Multi-
Factor Authentication (MFA). MFA requires a user to provide two or more
factors when authenticating.

* Something you know, such as a password or passphrase
* Something you have, such as a mobile device or hardware key
* Something you are, such as a fingerprint or facial structure

With MFA enabled, even if an attacker knows a user's password from a
successful credential harvest, the attacker would not be able to login without
passing a second factor. That said, different types of second factors provide
different levels of security and convenience. It is important for businesses
and users to understand the strengths and weaknesses of each approach, and
perhaps only allow specific authentication methods depending on the
sensitivity of a role or the information the user have access to.

Here are the various MFA methods ranked by security

  1. Hardware keys
  2. Time-Based One Time Passwords (TOTP)
  3. Push notifications
  4. Text/SMS messages and phone calls

SMS/text messages and phone calls are common MFA methods used by banks and
others, but they are the weakest form of MFA, because a stolen phones will
still receive SMS/text messages and phone calls even after they are wiped.
Phone numbers can be stolen by tricking phone carriers into porting the phone
number to the attacker's account--an action known as [SIM
swapping](https://blog.mozilla.org/en/internet-culture/mozilla-
explains/mozilla-explains-sim-swapping/).

Push notifications are by far the most convenient option for users with a
smartphone or tablet. After the user enters the correct password, a
notification appears on their mobile devices to approve or deny the login.
Attackers can bypass this by repeatedly sending push notifications [until a
user selects approve out of frustration](https://arstechnica.com/information-
technology/2022/03/lapsus-and-solar-winds-hackers-both-use-the-same-old-trick-
to-bypass-mfa/).

![A screenshot of a push notification for multi-factor
authentication](/assets/wp-content/uploads/2022/06/push-notification-mfa.png)

Time-Based One Time Passwords (TOTP) are six digit numbers that change every
minute. To set up TOTP with a service, a user scans a QR code provided by the
service with a TOTP app, such as [Google
Authenticator](https://support.google.com/accounts/answer/1066447) (which can
generate TOTP codes for any service, not just Google). The QR code contains
the secret that the service and app use to generate a one-time code based on
the current time. When the user logs in, the service will prompt them to enter
a TOTP code generated by the authenticator app. Because the service and the
app know the same secret, the code will be the same on both ends at any given
time. If the numbers match, the service will authenticate the user. TOTP is
more secure than SMS/text messages, phone call, or push notifications, and has
no additional costs to anyone who has a smartphone. However, users should be
regularly reminded to never give out a TOTP code over a phone call, text/SMS
message, or email -- no matter who or what claims to be on the other end of
the conversation. Likewise, TOTP codes should never be entered in response to
an email, link, or attachment. Attackers have automated processes that pass a
stolen TOTP code into a login form in real-time as a TOTP replay attack.

Hardware keys such as [Yubikey](https://www.yubico.com/products/) offer the
strongest, most secure form of MFA. Unlike other forms of MFA, they cannot be
bypassed by tricking the user into tapping an allow button in an app, visiting
a lookalike website, or giving the attacker a one-time code.

![An image of the Yubikey 5 NFC hardware security key. Hardware security keys
are the most secure form of MFA.](/assets/wp-content/uploads/2022/06/yubikey-5-nfc.png)

To authenticate with a hardware key, the user plugs the key into a USB port
(or taps the key against the back of their phone), and presses the button on
the key when prompted. The authentication uses the
[FIDO2](https://www.ionos.com/digitalguide/server/security/what-is-fido2/)
standard, which ensures that even if the user is tricked into using the key on
a fake website, an attacker could not impersonate the user on the legitimate
site. Most services that accept hardware key authentication allow users to
register multiple security keys for redundancy. For example, a user could have
one key that they keep with them in a bag or on a keychain and a spare key in
a fireproof safe. The one disadvantage of using hardware keys is cost,
especially with a large number of employees.

For further reading on MFA, check out [Okta's MFA deployment
guide](https://www.okta.com/resources/whitepaper/multi-factor-authentication-
deployment-guide/). It great advice for rolling out MFA in general, not just
Okta's MFA product.

### Passwords and sessions

If an account is suspected of being compromised, it is critical to reset the
account password as soon as possible.

[Resetting a password in Google
Workspace](https://support.google.com/a/answer/33319?hl=en) will also log the
user out of all sessions.

After [resetting a Microsoft 365 password](https://docs.microsoft.com/en-
us/microsoft-365/admin/add-users/reset-passwords?view=o365-worldwide) (or
disabling an account), an administrator must also take the additional step of
[revoking tokens](https://docs.microsoft.com/en-us/azure/active-
directory/enterprise-users/users-revoke-access) to invalidate any currently
active sessions.

### Email address spoofing

It is trivial for anyone to spoof the From address of an email. Domain owners
can[implement DMARC](https://seanthegeek.net/459/demystifying-dmarc/) to
prevent unauthorized spoofing of their domains in email message From headers.
This is a time-consuming task that may to be practical for businesses without
dedicated IT staff. Consider is a nice-to-have defense.

## Internal reconnaissance

Once an attacker has access to an email inbox, they can gather contacts,
customer data, and vendor information from the emails in the inbox to refine
their attacks. Even if they do nothing else past that point, data
confidentiality has been violated, which has serious implications, especially
for victims who are entrusted with sensitive data, such as Personal
Identifying Information (PII), Protected Health Information (PHI), financial
data, or trade secrets. Exposure of such information can result in
reputational damage, costly lawsuits, and contractual and/or regulatory
violations that carry steep fines.

This impact may be slightly reduced by implementing email retention policies,
which automatically delete emails that are beyond a set age. Every email
server and service should offer data retention policies, including [Google
Workspace](https://support.google.com/vault/answer/2990828) and [Microsoft
365](https://docs.microsoft.com/en-us/microsoft-365/admin/security-and-
compliance/set-up-multi-factor-authentication?view=o365-worldwide).

Once attackers complete their initial internal reconnaissance, they can
proceed in many different directions--often all at once.

## Email thread hijacking

Once scammers have free reign of on inbox, they can identify existing
sensitive email threads, and insert themselves into the for the conversation.
For example. if a scammer finds a high-dollar invoice from an invoice, they
can steal the email and send an external email that looks like part of the
original email thread, including impersonating the vendor to the victim by
using a lookalike domain in the from address or reply-to address, and instruct
the victim to redirect payment to a bank account that the scammers.

Make sure that users are trained to validate any email, text/SMS message, or
unexpected phone call that requests a change in process by calling a known
good phone number.

When reviewing back transfer information [check the routing
number](https://bank-code.net/routing-numbers) to ensure that it corresponds
with the expected financial institution.

If a fraudulent bank transfer is initiated, contact the sending bank
immediately. There is generally a 24 to 48 hour window of time when a transfer
can be stopped before it clears.

## Internal phishing

With access to an internal inbox and business directory, attackers can exploit
the implicit trust people and tools have in internal emails to run highly
effective internal phishing campaigns, allowing them to acquire access
throughout the business. From there, they to perform actions such as deploying
ransomware.

When training users make sure they know that phishing email can spread
internally too.

## External phishing

Scammers can send phishing emails from victim email accounts to the victim's
vendors and customers to expand their pool of victims. In addition to
reputation damage,the victim business sending the phishing emails for the
attacker may be held liable for damages, depending on jurisdiction and
contractual obligations.

When sending emails from compromised email accounts, attackers will often add
a mailbox rule to send all incoming email to the trash. This is done so that
the actual owner of the mailbox won't see a bunch of bounce reports or other
replies that might raise the suspicions of the victim.

As soon as outgoing phishing emails have been observed, victims should start
taking corrective action, including resetting the account password, submitting
takedown requests of malicious domains and websites, and warning potential
targets.

## Extortion

Attackers can collect sensitive information and threaten to disclose it to the
public if the victim does not pay them. Victims should keep in mind that even
if victims pay the attackers, and the attackers don't make the data public,
the data is often sold in underground markets on the dark web.
