---
layout: post
permalink: /126/hhs-ransomware-encryption-ephi-hipaa-breach
title: 'HHS: Ransomware encryption of ePHI is a HIPAA breach'
description: The US Department of Health and Human Services (HHS) ransomware fact
  sheet states that any unauthorized affect on ePHI is presumed to be a breach.
date: 2016-08-23 13:34:42 -0000
publish: true
pin: false
image:
  path: /assets/wp-content/uploads/2016/08/Medical-Records.jpg
  alt: 'Colorful shelves of paper medical records at a dental clinic - Credit: Tom Magliery License:
    CC BY-NC-SA 2.0'
categories:
- Healthcare
- Information Security
tags:
- breach-notification
- ePHI
- HHS
- HIPAA
- PHI
- privacy
- ransomware
- regulation
---
As a growing number of medical facilities are struck by ransomware, the US
Department of Health and Human Services (HHS) has published a [fact
sheet](https://www.hhs.gov/sites/default/files/RansomwareFactSheet.pdf)
describing how businesses that process electronic Protected Health Information
(ePHI) should defend against and respond to ransomware. Most of the
recommendations are known IT security best practices.

> The presence of ransomware (or any malware) on a covered entity's or
> business associate's computer systems is a security incident under the HIPAA
> Security Rule. A security incident is defined as the attempted or successful
> unauthorized access, use, disclosure, modification, or destruction of
> information or interference with system operations in an information system.
> See the definition of security incident at 45 C.F.R. 164.304. Once the
> ransomware is detected, the covered entity or business associate must
> initiate its security incident and response and reporting procedures. See 45
> C.F.R. 164.308(a)(6).

However, it also mentions that **any unauthorized affect on ePHI must be
reported as a HIPAA breach**.

> Whether or not the presence of ransomware would be a breach under the HIPAA
> Rules is a fact-specific determination. A breach under the HIPAA Rules is
> defined as, "…the acquisition, access, use, or disclosure of PHI in a manner
> not permitted under the [HIPAA Privacy Rule] which compromises the security
> or privacy of the PHI." See 45 C.F.R. 164.402.6
>
> **When electronic protected health information (ePHI) is encrypted as the
> result of a ransomware attack, a breach has occurred**[emphasis added]
> because the ePHI encrypted by the ransomware was acquired (i.e.,
> unauthorized individuals have taken possession or control of the
> information), and thus is a "disclosure" not permitted under the HIPAA
> Privacy Rule.
>
> Unless the covered entity or business associate can demonstrate that there
> is a "…low probability that the PHI has been compromised," based on the
> factors set forth in the Breach Notification Rule, **a breach of PHI is
> presumed to have occurred**[emphasis added]. The entity must then comply
> with the applicable breach notification provisions, including notification
> to affected individuals without unreasonable delay, to the Secretary of HHS,
> and to the media (for breaches affecting over 500 individuals) in accordance
> with HIPAA breach notification requirements. See 45 C.F.R. 164.400-414.

...

> To demonstrate that there is a low probability that the protected health
> information (PHI) has been compromised because of a breach, a risk
> assessment considering at least the following four factors (see 45 C.F.R.
> 164.402(2)) must be conducted:
>
> 1\. the nature and extent of the PHI involved, including the types of
> identifiers and the likelihood of re-identification;
>
> 2\. the unauthorized person who used the PHI or to whom the disclosure was
> made;
>
> 3\. whether the PHI was actually acquired or viewed; and
>
> 4\. the extent to which the risk to the PHI has been mitigated.

...

> Although entities are required to consider the four factors listed above in
> conducting their risk assessments to determine whether there is a low
> probability of compromise of the ePHI, entities are encouraged to consider
> additional factors, as needed, to appropriately evaluate the risk that the
> PHI has been compromised. If, for example, there is high risk of
> unavailability of the data, or high risk to the integrity of the data, such
> additional factors may indicate compromise. In those cases, entities must
> provide notification to individuals without unreasonable delay, particularly
> given that any delay may impact healthcare service and patient safety.

The information security field tends to think of a breach as a loss of
confidentiality. However, this document makes it clear that HHS considers a
loss of integrity and/or availability to be a breach as well. Check out [my
guide](https://seanthegeek.net/2016/08/22/prevent-ransomware-strategic-
defense/) for strategic defenses against ransomware.

Image credit: [Tom
Magliery](https://www.flickr.com/photos/mag3737/5841741742). [Some rights
reserved](https://creativecommons.org/licenses/by-nc-sa/2.0/).
