---
layout: post
title: Insights from the Peter Stokes "Scattered Spider" criminal complaint
description: Notes from a network defender watching the Peter Stokes case
date: 2026-07-10 18:51 -0400
categories: [Crime, Information Security]
tags: [Scattered Spider, Ransomware]
image:
  path: /assets/images/stokes-doj.webp
  description: Photo of stokes provided by the DOJ
---

I had been looking for the Peter Stokes case to be unsealed ever since the Chicago Tribune [broke the story](https://www.chicagotribune.com/2026/04/27/teen-charged-in-chicago-was-part-of-international-scattered-spider-hacker-group-feds-say/)  way back in April. The case, [United States v. Stokes, 1:25-cr-00812, (N.D. Ill.)](https://www.courtlistener.com/docket/73595564/united-states-v-stokes/)  was finally unsealed July 7th, nearly a week after the Department of Justice [press release](https://www.justice.gov/opa/pr/alleged-member-criminal-cyber-hacking-group-scattered-spider-arrested-finland-and-extradited).  In typical fashion, the [Criminal Complaint](https://storage.courtlistener.com/recap/gov.uscourts.ilnd.492131/gov.uscourts.ilnd.492131.1.0.pdf)  has 47 pages of definitions for legal purposes. The details of the activity itself begin in the Probable Cause section, on paragraph 48.

## Microsoft alleges that Stokes became involved with Scattered Spider when he was only 15

Paragraph 51 of the complaint includes part of Microsoft's criminal referral to the FBI. Octco Tempest is Microsoft's codename for Scattered Spider, which itself in a Crowdstrike codename given to the group. Spencer is Microsoft's codename for Stokes.

> Microsoft analysts have identified information about persona ‘spencer’, a likely operator for Octo Tempest, and their associated accounts. Persona  spencer’ handles malware associated with Octo Tempest and has handled files associated with persona \[Conspirator A’s moniker\]…. Persona ‘spencer’ is likely true name Peter Stokes, and probably lives in Tallinn, Estonia. Microsoft analysts have observed online services telemetry associated with persona 'spencer’ that indicates likely involvement in dozens of recent Octo Tempest intrusions including those targeting critical infrastructure organizations in the US and UK and has likely been involved with Octo Tempest since 2022.

Footnote 1 describes Conspirator A.

> More specifically, Coconspirator A was a Scattered Spider member who, at the time of certain Scattered Spider intrusions, was a juvenile, and who has been criminally charged for in connection with his Scattered Spider activities. According to Coconspirator A, STOKES committed the Subject Offenses against multiple victim-companies with Scattered Spider and went by the monikers “Bouquet” and “Jordan.” Coconspirator A attempted to cooperate in the government’s investigation but was untruthful in certain respects and continued to offend after law enforcement contact.

## Details of Tactics, Techniques, and Procedures (TTPs)

Starting on paragraph 52, the the Complaint  details the entire kill chain of a ransomware attack on Company F, "multibillion-dollar, luxury-item retailer".

### Vishing a helpdesk took over multiple IT admin accounts within hours

Access was gained by simply calling the helpdesk and getting them to reset the password and multi-factor authentication devices of multiple accounts, including two admin accounts.

> Regarding the intrusion, according to a Company F representative and a review of Company F network logs:
>
> a. The intrusion incident began on May 12, 2025, with several phishing calls4 to the Company F informational-technology help desk made by one or more threat actors from two Google Voice phone numbers, one ending in 8777 (the “8777 phone number”) and one ending in 2742 (the “2742 phone number”). The threat actors pretended to be Company F employee-users and requested a reset of their authentication credentials, including the password and mobile device for multi-factor authentication. Using this phishing technique, the threat actors compromised three Company F user accounts within approximately two to three hours.
>
> b. Two of these compromised user accounts belonged to Company F IT administrators. These users had high-privilege user accounts associated with their standard user accounts. To access their high-privilege accounts, those users would have to authenticate their standard user accounts and then be assigned a temporary password for their high-privilege account. The threat actors thus obtained access to high-privilege accounts for these two IT administrator accounts by using their compromised standard user accounts.

To mitigate this type of voice phishing (vishing) attack, organizations should establish policies that require users to provide non-public information, such as their employee ID, in order to reset their account.

### The ngrok cloud gateway was abused to bypass network controls

> As part of their malicious activity, the threat actors used a service called ngrok to circumvent Company F network defenses and enable persistent unauthorized access to the Company F data center...ngrok is a service used by web developers and others to securely connect local servers to the Internet, allowing broader access to information or applications hosted on local servers...ngrok is used to create secure tunnels between an Internet-accessible ngrok endpoint (e.g., `https://abc123.ngrok.io`) and a service on called "tunnels"...the Company F server established multiple tunnel connections with several ngrok servers. As described below, ngrok records for the account with the ngrok authentication token showed that the threat actors used these tunnel connections to transfer about 99.5 megabytes of data to the Company F data center and transfer about 1.27 gigabytes of data from the Company F data center.

To mitigate this, organizations should block `*.ngrock.com` if Ngrock is not used in the organization.

### Teleport abused to exfiltrate data to Amazon S3

> The threat actors then used the `Teleport.sh` utility and the Amazon S3 online storage utility to exfiltrate large amounts of sensitive Company F data, including OneDrive files belonging to Company F employee-users, Microsoft Active Directory data, and Microsoft Operations Management Suite data.
>
> Between May 12, 2025, and May 15, 2025, the threat actors were able to maintain persistent access to the Company F network and, primarily using the `Teleport.sh` utility and the Amazon S3 online storage utility, exfiltrated at least 77 gigabytes of data, despite ongoing attempts by Company F security personnel to block the attack.

As an early warning, organizations should create detections for large volumes of outbound data.

### Ransom note sent after failed attempt to deploy ransomware

> According to a Company F representative, the threat actors had likely attempted to deploy ransomware on Company F servers but had been thwarted by the security personnel. On May 15, 2025, the threat actors sent a ransom note to several Company F personnel from a Company F email account they had compromised. The ransom note had the subject “IMPORTANT: WE STOLE THE DATA, CONTACT UMMEDIATELY \[sic\].” In the email, the threat actors claimed they had stolen 100 gigabytes of data “including raw card information and payment details,” referring to credit card and related payment information, and threatened to publish the data unless Company F contacted them at a specified email address for negotiations.

## Chat on a victim's infrastructure

In their criminal referral, another victim, "Company H" provided logs between Conspirator A and Stokes on Company H's infrastructure, described on paragraph 65.

```text
STOKES         im in bed lmk if u need anything
Coconspirator A ok
Coconspirator A yo
Coconspirator A accept vcm
Coconspirator A vm [virtual machine]
Coconspirator A request
STOKES         yo
STOKES         accepted
STOKES         need anything?
Coconspirator A n
STOKES         kk
Coconspirator A yo
Coconspirator A can i anydesk [a remote desktop application]
Coconspirator A you
Coconspirator A send code
Coconspirator A i wanna search a [support] ticket
STOKES         yo
STOKES         send name
STOKES         ill search
….
Coconspirator A lmk when ur out of shower
Coconspirator A ill anydesk it
STOKES         when out
STOKES         Why
Coconspirator A cause I wanna look thru
STOKES         erm ok
...
Coconspirator A How
Coconspirator A do i search
Coconspirator A Again
STOKES         Just
STOKES         put whatever
STOKES         ui want
STOKES         in that
STOKES         Search
STOKES         Thing
…
STOKES         we can term
STOKES         any acount
STOKES         u got opps? [opposition]
... LOL
Coconspirator A BRO
STOKES         like not term
STOKES         disable
STOKES         haha
Coconspirator A BRO
Coconspirator A HOW
Coconspirator A SHOW ME
…
STOKES         the db [database] is full of google urls
STOKES         lmfao
STOKES         look
Coconspirator A oh
Coconspirator A wtf
Coconspirator A like
Coconspirator A fake rpeorts
…
Coconspirator A let me try to disable
STOKES         wait
Coconspirator A i got a user
Coconspirator A and discrim
STOKES         idk
STOKES         send
STOKES         think uy need
Coconspirator A ill put
STOKES         Email
Coconspirator A in search
STOKES         Ok
STOKES         How
STOKES         did u get
STOKES         Advancedsearcghh
STOKES         Lmfao
Coconspirator A advanced search
STOKES         U CAN SEARCH BY CREDIT CARD NUMBER
STOKES         LOL
Coconspirator A Nah
Coconspirator A Via
STOKES         Oh
STOKES         i thoguht it was VISA
STOKES         LMFAO
STOKES         Are
STOKES         u trying
STOKES         to term chris>
STOKES         ?
Coconspirator A No
Coconspirator A Haha
STOKES         Oh
STOKES         Haha
Coconspirator A Should
Coconspirator A i click
Coconspirator A Disable
Coconspirator A LOL
…
STOKES         u have 30 mins before i kcik u off btw
Coconspirator A Ok
STOKES         i gtg to school
Coconspirator A Ok
STOKES         and let this shit dump
STOKES         Disable
STOKES         LM FAOL
Coconspirator A Nah
STOKES         r u making
STOKES         disable API [application program interface]?
STOKES         LOL
…
STOKES         idk if u can like disable any account
STOKES         they have to have ticket
STOKES         i think
… go offline
STOKES
STOKES         stop disabling
STOKES         Btw
STOKES         we dont want
STOKES         to lose access
STOKES         Etc
Coconspirator A Nvm
Coconspirator A dont work
STOKES         Arghhh
STOKES         we should stop disableing
STOKES         ppl
Coconspirator A we should
Coconspirator A not be talking on [abbreviation for Company H]
STOKES         tg [Telegram]
```

## Other tools used

Paragraphs 67-68 describe other tools and services abused by the group, including MEGA file storage, File.io, and RustDesk.

Organizations should block file storage and remote support tools that they do not use.

## Identification of attacker infrastructure

Paragraphs 55-56 describe the attacker infrastructure.

> According to ngrok records, on or about May 12, 2025, at 19:21 UTC, an ngrok account with the ngrok authentication token was created and assigned Account ID `ac_2x0b16MSTJk4PvjLZMoqt4vOvZM` (the “ngrok account”). Also, according to ngrok records, the IP address of the user who created the ngrok account was `68.235.46.168`. According to public IP records, the `.168` IP address is assigned to a server hosted by Tzulo. According to Tzulo records, that server is in Mount Prospect, Illinois, and that IP address is assigned to a VPN proxy service. According to ngrok records, the ngrok account had five “connection events” and 12 “tunnel events” with the Company F server between May 12 and May 13, 2025—the dates of the intrusion.
>
>According to Google records, on May 12, 2025, the Google account with the 8777 phone number—which was used in the phishing calls to Company F—was logged into from the .168 address, the same IP address used to create the ngrok account on the same date. Also, according to Google records, subscriber information for the Google account with the 2742 phone number—the second phone number used in the phishing calls to Company F—included the email address `mykccncn109@gmail.com` (the Subject Google Account). According to ngrok records, subscriber information for the ngrok account included the Subject Google Account. And according to Teleport records, the Subject Google Account is also included in the subscriber information for the Teleport.sh accounts used in the  exfiltration of Company F data.

## Identification of Stokes via GDID

The use of Global Device ID (GDID)  tie the attacks to a specific installation of Windows is described in paragraphs 57-59.

> According to Microsoft records, the ngrok account was set up through Global Device Identifier `g:6755467234350028` (“the GDID”). According to a Microsoft representative, a Global Device Identifier in the Windows ecosystem is a persistent, device-level identifier designed to uniquely identify an installation of a Windows operating system on a device, either a physical device (e.g., a mobile phone or laptop) or virtual machine13, across certain Microsoft services and scenarios. A GDID is a globally unique identifier tied to the installation of Windows on a device. A GDID remains consistent across Windows operating system updates on a device, but a reinstall of Windows, either on the same device or on a different device, will be tied to a new unique GDID. Thus, one Microsoft user could have multiple GDIDs.
>
> According to Microsoft records, on May 12, 2025, at 19:21 UTC—when, according to ngrok records, the ngrok account was created—the device with the GDID accessed, among other ngrok pages, “`https://dashboard.ngrok.com/signup`,” the ngrok page to set up an ngrok account.
>
> Microsoft records also indicate: (1) the user of the device assigned the GDID accessed multiple sites from Tzulo servers in May 2025, including the `.168` server (the IP address used to create the ngrok account) on May 12, 2025; and (2) the user of the device assigned the GDID, on May 12, 2025 at 22:47 UTC, a little more than three hours after the ngrok account was created, the user visited “`[Company F].com`” from the `.168` proxy server.

Paragraphs 61-62 tie the GDID to the IP address activity of Stokes' social media accounts.

> As set forth below, there is probable cause that STOKES is the user of the device that set up the ngrok account used to commit the Subject Offenses. More specifically, the GDID assigned to the device that set up the ngrok account has common IP address activity with the Subject Accounts used by STOKES (discussed above).

Notably, the complaint **does not** mention how Microsoft obtained the internet traffic information for the specific GDID. It is possible that the Microsoft Edge browser was used by the attacker and that browsing  data was collected. However, the lack of specificity doesn't rule out more invasive collection, raising significant privacy concerns.

## What's next?

Nearly all of the docket entries are sealed, including a Superseding Criminal Complaint \[ECF entry 15\]. I'm tracking the case on my website [CaseCalendar.net](https://casecalendar.net), an automated website that tracks cases through CourtListener/RECAP data to build calendars of court hearings and deadlines. I'm checking public court records on PACER regularly, which feeds CourtListener/RECAP.
