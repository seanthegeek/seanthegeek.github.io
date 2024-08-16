---
layout: post
permalink: /78/prevent-ransomware-strategic-defense
title: Prevent ransomware from succeeding with strategic defense-in-depth
description: Schools, hospitals, businesses and others can take simple, low cost steps
  to prevent ransomware and mitigate its potentially devastating effects.
date: 2016-08-22 03:56:33 -0000
last_modified_at: 2016-05-08 16:53:18 -0000
publish: true
pin: false
image:
  path: /assets/wp-content/uploads/2016/08/petya_ransomware.jpeg
  alt: Thoughtfully placed countermeasures can prevent ransomware like Petya, shown in this screenshot
categories:
- Information Security
tags:
- defense-in-depth
- EMET
- featured
- ransomware
comments: []
---
Ransomware has become the weapon of choice for financially motivated
cybercriminals. Individuals,
[hospitals](https://www.nbcnews.com/tech/security/big-paydays-force-hospitals-
prepare-ransomware-attacks-n557176), businesses,
[schools](https://wdtn.com/2016/03/08/sc-school-district-pays-nearly-10k-to-
ransomware-hackers/), [police departments](https://www.darkreading.com/), and
government agencies have all been victims of highly disruptive ransomware,
resulting in ransom payments totaling at least $24 million in 2015, [according
to the DoJ and DHS](https://www.businessinsider.com/doj-and-dhs-ransomware-
attacks-government-2016-4). It doesn't take much to start a ransomware
campaign, and the returns can be extremely high. Fortunately, the steps to
prevent ransomware from succeeding are equally simple and low cost.

## Don't be easy prey

The majority of cybercrime campaigns are opportunistic, including ransomware.
They cast wide nets with a high probability of catching at least one large
organization off-guard. They don't worry if a particular target fails to be
effected, they will inevitably find success elsewhere. Even when attacks are
slightly more targeted, like hunting for medical records to steal and sell,
attackers will focus their efforts on the weakest possible targets. Why spend
more time and resources than necessary? It's all about the ROI.

[![Comic drawing: I just realized I don't need to outrun the bear. I just need to outrun you!](/assets/wp-content/uploads/2016/08/outrun_bear.jpeg)](/assets/wp-content/uploads/2016/08/outrun_bear.jpeg)  
_Artist unknown_

## The best defense is deep defense

When designing and deploying defenses against ransomware or any other threat,
all aspects should be considered: the criminal motivations, target selection,
malware delivery vectors, and more. Each stage of a ransomware campaign
provides an opportunity for another roadblock.

Most ransomware campaigns are spread through phishing email or drive-by web
exploits. Let's focus on the phishing vector first.

### Be careful with that contact info

A phishing campaign needs a list of valid target email addresses. These are
frequently gathered by scraping public websites, documents, and social media.
CloudFlare provides a free service tier (which is used by this site) that can
[obscure email addresses](https://support.cloudflare.com/hc/en-
us/articles/200170016-What-is-Email-Address-Obfuscation-) from bots, and
prevent many bad bots from accessing your sites altogether.

Using social media services like Facebook and LinkedIn, attackers can get a
list of employees, and then build a list of probable email addresses based on
common conventions like firstname.lastname@example.com. Train your employees
to keep their social media profiles as private as possible, especially those
that list their employment details. Of course, sometimes public exposure of
email addresses are unavoidable. Many people in sales need their email address
to be public in order to attract new business or serve clients; but if they
don't, why make it easy for an attacker to build a bigger target list?

### Catching phish

Opportunistic phishing emails use generic themes to get potential victims to
open attachments, like this invoice reminder message:

[![A screenshot of a phishing email with a generic invoice
theme](/assets/wp-content/uploads/2016/08/phishing_email_sample.png)](/assets/wp-content/uploads/2016/08/phishing_email_sample.png)
_Proofpoint_

The best defense against phishing and other social engineering is education.
Vendors like [Wombat Security](https://www.wombatsecurity.com/) offer a
complete training, simulation, and testing suite.

#### Block high-risk attachment file extensions

Unsophisticated phishing campaigns will package malware in file types that
should _never_ attached to legitimate email, like .exe, .scr, .js, and .hta.
Microsoft maintains a [helpful list](https://support.microsoft.com/en-
us/kb/883260) of high-risk file extensions. You should configure your email
gateway to block delivery of any email that contains these attachment types,
including inside archive files like zips:

> * .ade
> * .adp
> * .app
> * .asp
> * .bas
> * .bat
> * .cer
> * .chm
> * .cmd
> * .com
> * .cpl
> * .crt
> * .csh
> * .exe
> * .fxp
> * .hlp
> * .hta
> * .inf
> * .ins
> * .isp
> * .its
> * .js
> * .jse
> * .ksh
> * .lnk
> * .mad
> * .maf
> * .mag
> * .mam
> * .maq
> * .mar
> * .mas
> * .mat
> * .mau
> * .mav
> * .maw
> * .mda
> * .mdb
> * .mde
> * .mdt
> * .mdw
> * .mdz
> * .msc
> * .msi
> * .msp
> * .mst
> * .ops
> * .pcd
> * .pif
> * .prf
> * .prg
> * .pst
> * .reg
> * .scf
> * .scr
> * .sct
> * .shb
> * .shs
> * .tmp
> * .url
> * .vb
> * .vbe
> * .vbs
> * .vsmacros
> * .vss
> * .vst
> * .vsw
> * .ws
> * .wsc
> * .wsf
> * .wsh

Also, check out cloud email gateway services like
[ProofPoint](https://www.proofpoint.com/us/products) to see if they can do a
better job than your current email security solution within your budget.

### Beware of macros

The old malware distribution method of malicious Office macros has made quite
a comeback in the last few years. These files instruct the recipient to click
on the enable macros button by claiming that they are needed decode, decrypt,
or view the document.

[![A screenshot of a simple macro lure that would drop ransomware if
enabled](/assets/wp-content/uploads/2016/08/simple_macro_lure.png)](/assets/wp-content/uploads/2016/08/simple_macro_lure.png)

Some of these documents are much more detailed, and can be very official
looking. The one in the screenshot below is designed to look like a QuickBooks
invoice.

[![This macro dropper for ransomware looks like an invoice generated by
QuickBooks](/assets/wp-content/uploads/2016/08/QuickBooks_macro.png)](/assets/wp-content/uploads/2016/08/QuickBooks_macro.png)
_Proofpoint_

Most users never use Office macros, with the notable exception of finance and
accounting, where Excel macros are extremely common. For everyone else,
administrators can make a registry change or apply a GPO to block all macros.
In Office 2016 a new option allows administrators to only block macros in
Office documents that were downloaded from the internet or email. This a great
option, because most legitimate documents with macros (like the aforementioned
Excel finance wizards) are stored on local storage or internal network shares.
Microsoft has a handy guide to macro security settings
[here](https://blogs.technet.microsoft.com/mmpc/2016/03/22/new-feature-in-
office-2016-can-block-macros-and-help-prevent-infection/).

[![A screenshot of the new Office 2016 GPO setting to disable macros from
office files that were downloaded from the internet.](/assets/wp-content/uploads/2016/08/Macro-GPO-Settings.png)](/assets/wp-content/uploads/2016/08/Macro-GPO-Settings.png)  
Microsoft

### Block OLE packages

Rather than using macros, some ransomware dropping documents are using OLE
Packages to store dropper code. This method evades sandboxing techniques by
requiring users to double-click on a specific object to launch the payload.

[![A screenshot of a malicious Word document that use an embedded OLE package
to download and execute
ransomware](/assets/wp-content/uploads/2016/08/OLE_Package_example.png)](/assets/wp-content/uploads/2016/08/OLE_Package_example.png)  
_Microsoft_

OLE packages are almost never used in legit files, even the ones for those
macro-crazy finance and accounting people, which is good because there is no
GPO setting to block them. [Registry
changes](https://blogs.technet.microsoft.com/mmpc/2016/06/14/wheres-the-macro-
malware-author-are-now-using-ole-embedding-to-deliver-malicious-files/) are
needed:

> Administrators can prevent activation of OLE packages by modifying the
> registry key `HKCU\Software\Microsoft\Office\Security\PackagerPrompt`.
>
> The Office version values should be:
>
> * 16.0 (Office 2016)
> * 15.0 (Office 2013)
> * 14.0 (Office 2010)
> * 12.0 (Office 2007)
>
>
>
> Setting the value to 2 will cause the  to disable packages, and they won't
> be activated if a user tries to interact with or double-click them.
>
> The value options for the key are:
>
> * 0 - No prompt from Office when user clicks, object executes
> * 1 - Prompt from Office when user clicks, object executes
> * 2 - No prompt, Object does not execute
>
>
>
> You can find details about this registry key the Microsoft Support article,
> <https://support.microsoft.com/en-us/kb/926530>

### Blocking exploits

Some ransomware spreads by exploiting vulnerabilities in software.
Malvertising is a common way of delivering exploits to a wide audience of
potential victims. The malware distributor crafts a malicious advertisement
that exploits a web browser or browser plugin when it is loaded, and submits
it to ad networks. If the ad networks do not detect the malicious payload, the
ad could be displayed on hundreds or thousands of otherwise trustworthy sites
that generate revenue by displaying ads. These types of attacks are often
fileless, and extremely difficult to detect.

#### Install software updates, seriously

In many organizations there can be an intense aversion to installing software
updates and patches, usually out of fear of breaking things and causing
headaches. Unpatched software is ripe for exploitation. It's easy to roll back
most patches if need be. It is much harder to recover from a data breach.

Focus your patching efforts on:

* Operating system updates (Also, consider upgrading to Windows 10 - it's the [most secure Windows ever](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/windows-10-security-guide))
* External services
* AV engine updates (Yep, those can have some [really nasty vulnerabilities](https://bugs.chromium.org/p/project-zero/issues/detail?id=820) too)
* Browsers
* Browser plugins (Java, Adobe Flash, Adobe Reader - or any other Adobe product for that matter)
* Office applications
* Industry-specific software (Development environments, CAD, etc)

#### Deploy Microsoft EMET on all windows endpoints: Workstations, servers

kiosks, etc.

[![A screenshot of the EMET GUI](/assets/wp-content/uploads/2016/08/EMET-GUI-Screenshot.png)](/assets/wp-content/uploads/2016/08/EMET-GUI-Screenshot.png)

The [Microsoft Enhanced Mitigation Experience Toolkit
(EMET)](https://technet.microsoft.com/en-us/security/jj653751) is a free and
extremely lightweight agent from Microsoft that employs multiple system and
application-layer techniques to make memory more secure, and successful
software exploits much, much harder.

You may have heard that EMET breaks applications, or that it can be coerced
into attacking itself, or that it has been bypassed in the wild. All of these
issues were fixed in the last few releases. The latest release at the time of
the writing is 5.51.

It is fantastic at preventing most zero-day exploits, and exploits against
software that you can't patch for whatever reason - like that ancient version
of Java that is required by that HR application everyone uses, and will never,
ever, be fixed to work with anything newer, because reasons. Its Microsoft
recommended settings focus on protecting popular software like Adobe Flash,
Adobe Reader, Java, and Microsoft Office in ways that are known to not break
the applications. It provides a _**much**_ stronger security posture without
additional risk of application breakage.

Don't take my word for for it. EMET is now a recommendation in the Center For
Internet Security (CIS) Windows benchmarks (e.g. [Windows 10 Enterprise
benchmark](https://benchmarks.cisecurity.org/tools2/windows/CIS_Microsoft_Windows_10_Enterprise_Release_1511_Benchmark_v1.1.0.pdf),
Recommendation 18.9.22). CIS' recommended EMET settings are stronger than and
generally preferred over Microsoft's recommended configuration. EMET is also
required by the [DISA STIGs for
Windows](https://iase.disa.mil/stigs/os/windows/Pages/index.aspx), which means
that is required on every Windows system in the US Department of Defense
(DoD), military, and National Security Agency (NSA). That makes up some of the
largest enterprise networks on the planet! They are also [rapidly
migrating](https://iasecontent.disa.mil/stigs/pdf/U_Windows_10_STIG_V1_Release_Memo.pdf)
to a standard Windows 10 image.

I've created [some
scripts](https://github.com/seanthegeek/powertools/tree/master/EMET) to make
silently deploying, configuring, and testing a little easier when you can't
work with GPOs in your organization.

For more information, check out the [EMET User
Guide](https://www.microsoft.com/en-us/download/details.aspx?id=53355).

#### Limit admin permissions

While most malware only uses user-level privileges, some ransomware like
[petya](https://blog.malwarebytes.com/threat-analysis/2016/05/petya-and-
mischa-ransomware-duet-p1/) uses elevated privileges to overwrite the Master
Boot Record (MBR).

Restrict local and domain admin privileges to only those who absolutely need
it. Products like [Avecto
DefendPoint](https://www.avecto.com/defendpoint/privilege-management) can
selectively elevate privileges on a per application basis, based on what that
user is permitted to do.

Microsoft's free [Local Administrator Password Solution
(LAPS)](https://technet.microsoft.com/en-us/library/security/3062591.aspx) can
help manage local administrator passwords.

### Defend your network

#### Routinely audit network share permissions

Avoid public shares at all costs. Restrict share permissions to only those
users who need them. If write access is not needed, ensure only read access is
granted. This limits the amount of damage a malicious user or malicious
software can do.

#### Patrol your perimeter

Ransomware campaigns have been known to use stolen credentials of employees
and contractors to login to RDP, VPNs, and VDI. Always use multi-factor
authentication for remote access. Services like [DUO](https://duo.com/) make
multi-factor authentication very easy. [Okta](https://www.okta.com/) identity-
as-a-service provides their own DUO-like multi-factor authentication. Both
services (and many others) can use a
[Yubikey](https://www.yubico.com/products/yubikey-hardware/yubikey4/) as a
robust USB hardware token that is more secure than phone-based authentication,
at a much lower cost and greater compatibility than RSA SecureID tokens,
thanks to support for PIV smartcard and [FIDO
U2F](https://fidoalliance.org/specifications/overview/) standards.

Some campaigns have exploited vulnerabilities in outdated software stacks like
jBoss. Scan external DMZ and cloud hosted applications for vulnerabilities
regularly.

#### Block high-risk sites and P2P protocols

Block all freeware, shareware, and piracy sites. These sites often contain
malware or crapware.

Block P2P protocols like BitTorrent that are frequently used for piracy.

#### Block all uncategorized sites

Most web filters are able to be configured to block uncategorized sites. This
would block new malicious Command and Control (C2) infrastructure before it
would even show up on blacklists. Most web filters categorize new legitimate
sites within a few days.

In the rare event that a user needs access to a site that has not been
categorized yet, you can submit a categorization request to the filter vendor,
and create an exception in your configuration for the meantime.

#### Automatically connect remote workers to your VPN

Protect your users and monitor their traffic when they are working remotely by
configuring their systems to automatically connect to your organization's VPN.
This enforces the same network and web filtering policies wherever they go.

### **Have robust backup and disaster recovery plans that are regularly and

thoroughly tested**

Create regular backups. Store them outside your regular network, and off site.
That way, when ransomware or some other disaster causes disruption, you can be
ready, and recover as quickly as possible.

## TL;DR to prevent ransomware

* Limit public exposure of contact information
* Block high-risk email attachment file types
* Train your users in security awareness
* Patch all the things
* Deploy Microsoft EMET
* Limit admin access
* Regularly check your network perimeter and publicly accessible applications for vulnerabilities
* Use multi-factor authentication for all remote access
* Block all uncatagorized sites
* Block high-risk sites and P2P protocols
* Automatic VPN for everyone working remotely
* Have solid backups and disaster recovery plans

## Further reading

* [Microsoft's ransomware guide](https://www.microsoft.com/security/portal/mmpc/shared/ransomware.aspx)
