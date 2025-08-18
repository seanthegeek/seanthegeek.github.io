---
layout: post
permalink: /15/doj-v-apple-precedent/
title: 'DoJ v. Apple: It''s all about the precedent'
description: Apple is fighting a court order forcing it to write software for breaking
  into iPhones. The privacy implications are huge. DoJ v. Apple is critical.
date: 2016-03-21 01:23:52 -0000
last_modified_at: 2016-08-06 20:28:13 -0000
publish: true
pin: false
image:
  path: /assets/wp-content/uploads/2016/03/secret-stamp.webp
  alt: A battle for encryption privacy and secrecy has been highlighted in a series of DoJ v. Apple court filings
categories:
- Information Security
- Politics
tags:
- Apple
- DOJ
- encryption
- law
- privacy
---
By now, you've probably heard something about the ongoing legal battle between
Apple and the Department of Justice. "DoJ v. Apple" coverage has been
abundant, on blogs and TV news shows alike, but in case you haven't here's a
quick recap. The FBI obtained the work iPhone of Syed Rizwan Farook, who,
along with his wife Tashfeen Malik, murdered 14 people in a
[shooting rampage](https://www.cnn.com/2015/12/03/us/syed-farook-tashfeen-malik-mass-shooting-profile/)
at a holiday party in San Bernardino, California. The
government suspects that iPhone may hold critical information about the
couple's contacts in the weeks leading up to the attacks - contacts that may
uncover future plots. They have a warrant, but they can't access the data on
the phone because it is using the strong encryption that
[comes with](https://www.apple.com/business/docs/iOS_Security_Guide.pdf)
iOS 9 and up. Not even Apple can bypass the encryption, at least directly.

### TL;DR? Watch John Oliver (NSFW)

<iframe width="560" height="315" src="https://www.youtube.com/embed/zsjZ2r9Ygzw?si=Fz5c6xRZl4zzFQ8S" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### DoJ v. Apple: The order

A federal judge granted the DoJ's
[motion](https://www.documentcloud.org/documents/2714000-SB-Shooter-MOTION-Seeking-Asst-iPhone.html)
for an order under the [All Writs Act](https://www.law.cornell.edu/uscode/text/28/1651),
compelling Apple to create a modified version of iOS for the shooter's iPhone
with the following changes:

* Disable the automatic wiping function that can be triggered if too many bad attempts and made when entering the PIN
* Disable the delay that occurs between bad PIN entries
* Have an automated method of brute-force guessing all possible PINs

Such modified software would provide access to the iPhone within minutes.

### One and done?

The DoJ contends that the software could be allowed to remain on Apple's
campus, and would only be used for this one phone in this case. However, there
are many, many more cases where an encrypted iPhone is suspected to contain
information relevant to a violent crime, including
[175 devices](https://abcnews.go.com/Technology/york-da-access-175-iphones-criminal-cases-due/story?id=37029693)
in NYC alone. If the order were allowed to stand, Apple would surely receive
similar orders from law enforcement agencies around the country and beyond,
including countries with
[dismal human rights records](https://www.amnesty.org/en/countries/asia-and-the-pacific/china/report-china/).
It would set a precedent that would allow courts to compel companies to do
anything. As a result, Apple and others would need to keep a weakened copy of
their software on hand at all times to be able to comply with such orders,
greatly increasing the risk of the software being stolen by an insider, or
outside attacker.

Apple [appealed](https://assets.documentcloud.org/documents/2722199/5-15-MJ-00451-SP-USA-v-Black-Lexus-IS300.pdf)
the order on grounds that the order:

* Would violate its First and Fifth Amendment rights by compelling speech
* Would cause an unreasonable burden
* Would set a dangerous precedent

Judge Orenstein
[granted](https://www.eff.org/files/2016/02/29/applebrooklyn-2.29.16order.pdf)
the appeal on the grounds that:

* The government's request fails to satisfy the requirements of the All Writs Act
* The government's request fails to satisfy the needs of judicial discretion
* Congress has already clearly defined what can be required of telecommunications companies
* Congress considered legislation that would have authorized such a request, but did not pass it, thus neither explicitly allowing or prohibiting such a request
* Accepting the [government's interpretation](https://cryptome.org/2016/02/usg-apple-001-009.pdf) of the All Writs Act would likely render it unconstitutional, based on the separation of powers in the branches of government

### Politicians and Encryption

High profile cases, such as the San Bernardino massacre have prompted
uninformed calls from politicians for the tech community to come up with a
solution that would allow law enforcement to access to encrypted devices and
communications.

> "I would hope that, given the extraordinary capacities that the tech
> community has and the legitimate needs and questions from law enforcement,
> that there could be a Manhattan-like project, something that would bring the
> government and the tech communities together…"  
>
> Hillary Clinton, [ABC News Democratic Debate](https://www.cbsnews.com/news/democratic-debate-transcript-clinton-sanders-omalley-in-new-hampshire/)
> December 19th, 2015

Does a former Secretary of State really not know
[how quickly](https://www.osti.gov/opennet/manhattan-project-history/Events/1942-1945/espionage.htm)
Manhattan Project secrets were leaked?

### Encryption is global and here to stay

> "In extremis, it has been possible to read someone's letter, to listen to
> someone's call, to mobile communications. The question remains: are we going
> to allow a means of communications where it simply is not possible to do
> that? My answer to that question is: no, we must not."  
>
> [David Cameron](https://www.theguardian.com/technology/2015/jan/15/david-cameron-encryption-anti-terror-laws)

Strong encryption cannot be outlawed, because math cannot be outlawed. The
algorithms have been known around the world
[for decades](https://en.wikipedia.org/wiki/History_of_cryptography#Public_key).

According to [A Worldwide Survey of Encryption Products, Feb 2016, v 1.0](https://www.schneier.com/cryptography/archives/2016/02/a_worldwide_survey_o.html)
by
[Schneider et al.](https://www.schneier.com/cryptography/archives/2016/02/a_worldwide_survey_o.html),
encryption projects can be found all over the world:

**Country** | **Open****Source** | **Proprietary** | **Unknown** | **Grand Total**  
---|---|---|---|---  
United States | 101 | 202 | 1 | 304  
Germany | 46 | 66 |  | 112  
United Kingdom | 18 | 36 |  | 54  
Canada | 15 | 32 |  | 47  
France | 25 | 16 |  | 41  
Sweden | 10 | 23 |  | 33  
Switzerland | 6 | 19 |  | 25  
Australia | 5 | 16 |  | 21  
Netherlands | 9 | 10 |  | 19  
Italy | 7 | 11 | 1 | 19  
Russia | 8 | 9 |  | 17  
Unknown | 8 | 7 |  | 15  
Finland | 4 | 5 |  | 9  
Israel | 1 | 8 |  | 9  
India | 1 | 8 |  | 9  
Japan | 3 | 5 | 1 | 9  
Czech Republic | 2 | 6 |  | 8  
Austria | 1 | 7 |  | 8  
Seychelles | 0 | 7 |  | 7  
Spain | 0 | 7 |  | 7  
**Grand Total** | **270** | **500** | **3** |  **773+**  
  
The following are high-quality, open source end-to-end encryption tools. Many
of these have global teams.

Use | Projects  
---|---  
Mobile messaging/voice | [Signal](https://whispersystems.org/)  
Files at rest | [GnuPG](https://www.gnupg.org/i)/[Gpg4win](https://www.gpg4win.org/)/[GPGTools](https://gpgtools.org/)  
Email frontend for GPG | [Thunderbird](https://www.mozilla.org/en-US/thunderbird/)/[Enigmail](https://www.enigmail.net/)  
Instant message (IM) | [OTR](https://otr.cypherpunks.ca/) on [Jitsi](https://jitsi.org/Main/Features)  
A/V conferencing |  [ZRTP](https://jitsi.org/Documentation/ZrtpFAQ) on [Jitsi](https://jitsi.org/Main/Features)  
  
### There's no magic solution

President Obama has a more detailed proposal that may seem reasonable at
first, but it has the same flaws.

> "I suspect the answer is going to come down to how do we create a system
> where the encryption is as strong as possible, the key is as secure as
> possible, it is accessible by the smallest number of people possible for a
> subset of issues that we agree are important."  
>
> President Obama at [SXSW 2016](https://www.businessinsider.com/obama-comments-on-encryption-at-sxsw-2016-3)

That's not going to work. Why?

* How valuable would such a key be? Priceless
* Who would want to steal such a key? Every hacker ever. Especially the same kinds of people who stole the HR and security records of every federal employee and job applicant, a breach that many consider to be [more damaging](https://www.washingtonpost.com/opinions/hitting-an-agency-where-it-hurts/2015/06/17/ffca6c6a-1512-11e5-9ddc-e3353542100c_story.html) than the Snoden leaks, especially when combined with other [stolen data](https://www.washingtonpost.com/world/national-security/in-a-series-of-hacks-china-appears-to-building-a-database-on-americans/2015/06/05/d2af51fa-0ba3-11e5-95fd-d580f1c5d44e_story.html).
* Would there be temptation for abuse? [Definitely.](https://arstechnica.com/tech-policy/2014/06/legal-experts-cops-lying-about-cell-tracking-is-a-stupid-thing-to-do/)

### Outlawing strong encryption only hurts the good guys

> "[Apple CEO] Tim Cook is living in a world of the make believe. I would come
> down so hard on him--you have no idea--his head would be spinning all of the
> way back to Silicon Valley."  
>
> [Donald Trump](https://www.bloomberg.com/politics/articles/2016-02-19/trump-calls-for-apple-boycott-until-company-unlocks-terrorist-s-iphone)

It can be tempting to try and simplify a complex issue to "You're either with
us or against us". Encryption is not that simple. It's true that recent
advancements in consumer technology have made it easy for anyone, including
criminals, to use unbreakable encryption. However, the underlying technology
has been around the world for decades. Trying to force everyone to use weak
encryption will make everyone who uses it extremely vulnerable, disrupting
trust in the internet and global commerce. It will criminalize anyone who
values their privacy and security, and make little difference in the ability
to read the communications of real criminals. If a criminal knows (like
everyone would, given the press) that the lawful encryption is weak, but that
unbreakable encryption can be had with a bit more effort and knowledge, the
choice is obvious.

Some are living in a world of make believe, but not Tim Cook. It would be nice
if more politicians
[actually learned about a topic](https://www.popsci.com/senator-graham-likes-encryption-now-that-he-understands-it)
before making broad statements about it.
