---
layout: post
status: publish
published: true
title: How to examine a credential harvesting page using Microsoft Edge
permalink: /1069/how-to-examine-a-credential-harvesting-page-using-microsoft-edge/
description: A practical guide to using Microsoft Edge to examine heavily obfuscated JavaScript in a credential harvesting page
image:
  path: /assets/images/00-cred-harvest-page-edge.png
wordpress_id: 1069
wordpress_url: https://seanthegeek.net/?p=1069
date: '2021-05-10 05:22:10 +0000'
date_gmt: '2021-05-10 05:22:10 +0000'
categories:
- Information Security
- How-to Guides
tags:
- phishing
- credential harvesting
- Microsoft Edge
- JavaScript
comments: []
---
Recently I analyzed a credential harvesting page with some interesting
characteristics that made a great teaching moment. In this post, I'll go over
how I used the developer tools built into Microsoft Edge to examine the
credential harvesting page.

Credential harvesting pages are fake login forms. When a user is tricked into
using that login form to submit their credentials, those credentials are sent
off to someone else. From there, those stolen credentials can be sold on
underground markets, used to launch attacks, or both. Credential harvesters
vary widely in sophistication. Some look like they were created by someone who
just learned how to write some basic HTML, and others are visually
indistinguishable from legitimate login forms.

Most of the time, impact from stolen credentials can be mitigated by requiring
a user to input a code from a call, text message, app, or other second factor
for Multi-Factor Authentication (MFA) in addition to a password. However, MFA
is not failproof. Skilled developers make credential harvesters that work to
bypass MFA in real-time. This is done by using the stolen credentials on the
real login form as soon as the target has used the fake one, and when the
thief's bot is challenged for the MFA code on the real login form, it uses the
fake login form to ask the user for the code they received on their phone,
just like the real login form would, and then pass that code to the real login
form to complete the fraudulent MFA process.

## The phish

Like many credential harvesting campaigns, this one used a phishing email to
lure potential victims. It was sent from someone's compromised Virgin Media
email account.

![A screenshot of Received email headers showing the originating mail servers
that were abused to send the phish ](/assets/images/02-email-headers-received-1.png)

![A screenshot of Authentication-Results email headers](/assets/images/03-email-headers-auth-results-original.png)

What made this credential harvesting phish a little different was the use of
an attachment instead of a link.

![A screenshot of a phishing email with a credential
](/assets/images/01-email.png)

From a phishing perspective, there are many advantages to attaching a
credential harvesting page instead of linking to one. The email gateway cannot
rely on simple checks like the reputation of a URL or domain in a link, the
code in the attachment can be highly obfuscated to bypass static scans, and
because the form itself does not exploit anything on the system it will pass a
sandbox test. Even if the targeted user figures out it is a scam, there is no
obvious URL to report.

## Warning

Always use dedicated physical and/or virtual machines on separate networks
when examining malicious or potentially malicious content.

## Static analysis

Before diving in with dynamic analysis and examining the the JavaScript as it
executes, take a look at it as a file. The JavaScript used in the attachment
is very heavily obfuscated. The content is also minified, so the code is
crammed into as files lines and little whitespace as possible.

![A screenshot of the content of the phishing email
attachment](/assets/images/04-javascript.png)

Code minification does have legitimate uses, particularity on websites used on
mobile devices, where every byte saved means faster load times and less data
usage. So, there are many tools to make HTML, JavaScript, and CSS minified.
Fortunately, there are also many tools to reverse the process, such as the
Beautify
[extension](https://marketplace.visualstudio.com/items?itemname=hookyqr.beautify)
for Visual Studio Code.

![A screenshot of the content of the phishing email attachment after the
Beautify has run](/assets/images/05-code-beautify.png)

Beautify certainly makes the code easier to read, but it does nothing to
deobfiscate the code to make all those variable manipulations easier to
understand. The open source [project](https://lelinhtinh.github.io/de4js/)
de4js can deobfiscate some JavaScript, but it was not successful in this case.
I will submit this sample to the maintainers so they can find out what went
wrong and fix it.

## Dynamic analysis

When static analysis fails to provide all of the answers you need, preform a
dynamic analysis by monitoring the activity of the page. This can be done in
the developer tools built into Microsoft Edge (and most other web browsers).
Microsoft Edge is a great choice of web browser for dynamic analysis of
potentially malicious websites, because as the default web browser in Windows
10, it has a large personal and corporate userbase, and is therefore a
frequent target. Modern versions of Microsoft Edge use Chromium, the same
browser engine that is behind Google Chrome, so pages so pages should behave
nearly identically in both browsers in most cases.

To open the developer tools in Microsoft Edge, click on the main ... menu,
navigate to More tools> Developer tools, or use the keyboard shortcut Ctrl +
Shift + I.

This sample continuously calls the debugger
[statement](https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Statements/debugger) in a loop as a basic
form of anti-analysis. This triggers a breakpoint that stops execution when a
debugger is used.

![A screenshot of the debugger stopping on the debugger
statement](/assets/images/06-anti-debug.png)

To bypass this, click on the deactivate breakpoints button, and refresh the
page. When the source tab is clicked, the Developer Tools provides the option
of deminifying the the code. Do that.

![A screenshot showing the deactivate breakpoints
button](/assets/images/07-edge-debugger-pretty.png)

Unfortunately, this also deactivates any breakpoints that could be set in the
debugger for line-by line dynamic analysis.

### Network forensics

Once breakpoints are deactivated on the Network tab to monitor network
activity, check the Preserve log and Disable cache checkboxes, then submit
fake credentials in the login form.

If the credential harvesting page had been hosted at a URL instead, it is
useful to toggle the Preserve log and Disable cache on **before** visiting a
link in a fishing email, that way any redirects are captured.

![A screenshot of the Network tab](/assets/images/08-edge-network.png)

Each request is listed in the left sidebar. Right-clicking on any of the
requests provides an option to copy the request headers, response headers, and
the response bodies. This is the full request.

    GET /rkFyMnr1Lndz4HfW22x2qLPuHAuGnVdWEUO2HlC4/T8rcLqB3Wl84kJhezG1cTALdGnVTLWY7yQvxIbnV/UQOYLWpdSGNlhiboXanQ.php?sOc9qJsBVqZihFxEBSoe=REDACTED%40REDACTED.com&wowVsfUC6toe92s7XQNn=Can%27tGuessThis! HTTP/1.1
    Host: plotoperation1.3eehj3wdhdhjww3r3dkjd.com
    Connection: keep-alive
    Pragma: no-cache
    Cache-Control: no-cache
    sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90"
    Accept: application/json, text/javascript, */*; q=0.01
    sec-ch-ua-mobile: ?0
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51
    Origin: null
    Sec-Fetch-Site: cross-site
    Sec-Fetch-Mode: cors
    Sec-Fetch-Dest: empty
    Accept-Encoding: gzip, deflate, br
    Accept-Language: en-US,en;q=0.9

When fake credentials are submitted, this sample displays the message
"Processing" for many seconds, before displaying an "incorrect email password"
password message.

![A screenshot of the phishing page saysing "processing"](/assets/images/09-processing.png)
![A screenshot of the phishing page saying "incorrect email password](/assets/images/10-incorrect-email-password.png)

At first, it seems like this might be an artificial delay and error message,
designed to trick the user into thinking that the login simply failed.
However, the response from the thief's Russian web server returned a JSON-
formatted error, and the Timing tab of the developer tools shows that the
server took nearly 7 seconds to respond. Taken together, these facts strongly
suggest that the server is testing credentials in real time. Valid credentials
were not used during testing, so It is not known if the victim would be
prompted to provide a MFA code.

    HTTP/1.1 200 OK
    Server: nginx
    Date: Thu, 06 May 2021 18:31:27 GMT
    Content-Type: text/html; charset=UTF-8
    Transfer-Encoding: chunked
    Connection: keep-alive
    Keep-Alive: timeout=60
    Vary: Accept-Encoding
    X-Powered-By: PHP/5.6.40
    Access-Control-Allow-Origin: *
    Expires: Thu, 19 Nov 1981 08:52:00 GMT
    Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
    Pragma: no-cache
    Set-Cookie: PHPSESSID=uoncani48a0iifqnqa4p4c6v55; path=/
    Content-Encoding: gzip
    
    {"msg":"errorsend"}

![A screenshot of the Timing tab in Microsoft Edge developer
tools](/assets/images/11-edge-timing.png)

Passive DNS data from Farsight Security's
[DNSDB](https://seanthegeek.net/1122/how-to-use-farsight-dnsdb-to-harness-the-
power-of-passive-dns/) revealed that l291067a.justinstalledpanel.com also
pointed to the same IP address. The IP address and domains currently have 0
detections on VirusTotal.

**Update** : It turns out justinstalledpanel.com is used as part of the domain
parking infrastructure for publicdomainregistry.com

![A screenshot of VirusTutal results for 37.18.30.131](/assets/images/VirusTotal-37.18.30.131.png)
![A screenshot of VirusTotal results for l291067a.justinstalledpanel.com](/assets/images/VirusTotal-plotoperation1.3eehj3wdhdhjww3r3dkjd.com_.png)
![A screenshot of VirusTotal results for VirusTotal-plotoperation1.3eehj3wdhdhjww3r3dkjd.com ](/assets/images/VirusTotal-l291067a.justinstalledpanel.com_.png)

## MITRE ATT&CK techniques

* [T1111](https://attack.mitre.org/techniques/T1111/) \- Two-Factor Authentication Interception
* [T1566](https://attack.mitre.org/techniques/T1566/) \- Phishing
* [T1568.002](https://attack.mitre.org/techniques/T1568/002/) \- Dynamic Resolution: Domain Generation Algorithms
* [T1583.001](https://attack.mitre.org/techniques/T1583/001/) \- Acquire Infrastructure: Domains

## MITRE ATT&CK mitigations

* [M1017](https://attack.mitre.org/mitigations/M1017) \- User Training
* [M1021](https://attack.mitre.org/mitigations/M1021) \- Restrict Web-Based Content
  * Block newly registered, newly observed, uncategorized, and meaningless content domains
* [M1032](https://attack.mitre.org/mitigations/M1032/) \- Multi-Factor Authentication

## Indicators

* plotoperation1.3eehj3wdhdhjww3r3dkjd.com (37.18.30.131)
* 3eehj3wdhdhjww3r3dkjd.com
