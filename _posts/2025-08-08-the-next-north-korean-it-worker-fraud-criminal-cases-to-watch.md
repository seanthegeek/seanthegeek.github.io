---
layout: post
title: The next North Korean IT worker fraud criminal cases to watch
description: Multiple cases are still winding their way through the criminal justice system
image:
  path: /assets/images/christina-chapman-laptop-farm.webp
  alt: A photo of Christina Chapman's laptop farm from the DOJ's sentencing memorandum
categories:
  - Law
  - Crime
  - Geopolitics
  - Information Security
  - National Security
tags:
  - North Korea 
date: 2025-08-08 17:41 -0400
---
 The government of North Korea, formally known as the Democratic People's Republic of Korea (DPRK) wants to continue its nuclear weapons program despite US and UN sanctions. To do that it needs lots of money, which is difficult to come by if most of the world has you under sanction. To work around this, the DPRK has trained some of its people in IT skills, and then used fake, borrowed, or stolen identities to get them high-paying jobs around the world. The proceeds from these jobs are then laundered and funneled into North Korea's weapons program. To pull this off, they need help from a variety of others. They need someone who can pass an interview and people to help forge identification documents. Once one of their personas are hired, they need people in the US to run laptop farms. These facilitators receive the victim company's laptop, host it at their residence, and configure remote access software (e.g., Anydesk, TeamViewer, or Splashtop Streamer) or hardware such as a KVM over IP device, to allow the DPRK workers to appear to be working in the US.

Christina Chapman, a 50-year-old woman from Arizona made headlines on July 30, 2025 for being sentenced to [102 months (8.5 years) in prison](https://www.justice.gov/usao-dc/pr/arizona-woman-sentenced-17m-it-worker-fraud-scheme-illegally-generated-revenue-north), with three years of supervised release afterwards. She was also ordered to forfeit $284,555.92 that was to be paid to the North Koreans, and to pay a judgement of $176,850 for her role as a facilitator of North Korean IT worker fraud. On February 11, 2025, she pled guilty to Conspiracy to Commit Wire Fraud ([18:1343], [1349][18:1349]), Aggravated Identity Theft ([18:1028A]), and Conspiracy to Launder Monetary Instruments ([18:1956]), in exchange for counts of Conspiracy to Defraud the United States ([18:371]), Conspiracy to Commit Bank Fraud ([18:1344][18:1344]\(1) & (2), [1349][18:1349]), Conspiracy to Commit Fraud and Related Activity in Connection with Identification Documents ([18:1028][18:1028](a)(7), (b)(1)(D), (c)(3)(A), & (f)), Prohibition of Unlicensed Money Transmitting Business ([18:1960]\(a), 2), and Causing Unlawful Employment of Aliens ([18:371], [8:1324a]\(a)(1)(A), [8:1324a]\(f)(1)) to be dismissed as part of a [plea agreement](https://storage.courtlistener.com/recap/gov.uscourts.dcd.268378/gov.uscourts.dcd.268378.22.0.pdf). The sentence is still less than the 111 months (9.25 years) that the Government recommended in their [sentencing memorandum](https://storage.courtlistener.com/recap/gov.uscourts.dcd.268378/gov.uscourts.dcd.268378.33.0.pdf).

By reviewing the court [docket](https://www.courtlistener.com/docket/68534169/united-states-v-chapman/) you can find the [Statement of Offense](https://storage.courtlistener.com/recap/gov.uscourts.dcd.268378/gov.uscourts.dcd.268378.23.0.pdf), which is an 18 page description of the criminal actions taken by Chapman that she has admitted to as part of the plea agreement. This includes chat logs and other evidence showing that Chapman was not only hosting the laptops, but was also actively participating in using identities that she knew were stolen and collecting paychecks at her residence.

> On or about August 2, 2023, Chapman acknowledged the severity of falsifying employment eligibility forms (i.e., the Form 1-9) in a group message that included several coconspirator overseas IT workers, stating, "[i]n the future, I hope you guys can find other people to do your physical 19s. These are federal documents. I will SEND them for you, but have someone else do the paperwork. I can go to FEDERAL PRISON for falsifying federal documents."

 The docket also includes victim impact statements from [Nike](https://storage.courtlistener.com/recap/gov.uscourts.dcd.268378/gov.uscourts.dcd.268378.42.1.pdf) and others, as well as [a letter from Chapman](https://storage.courtlistener.com/recap/gov.uscourts.dcd.268378/gov.uscourts.dcd.268378.41.1.pdf) to the judge prior to sentencing.

With the docket you can build a timeline of the case.

- In or around March 2020: An unknown coconspirator approached Chapman,
through her Linkedln page, and asked her to "be the U.S. face" of their company
and assist them in helping the overseas IT workers gain remote employment in
the United States.
- Between in or around August 2022, through in or around November 2023: North Koreans select targets
- Beginning at least in or around October 2020: The start of the conspiracy with Chapman
- On or about October 26, 2023: The end of the conspiracy with Chapman
- May 8,2024: Chapman is indited and the case is sealed
- May 16, 2024: Chapman is arrested, and the case is unsealed
- May 17, 2024: A Federal Public Defender appears for Chapman
- February 11, 2025: Chapman accepts plea agreement and pleads guilty
- July 30, 2025: Chapmen is sentenced

All of this detail made me wonder what other federal criminal cases related to DPRK worker fraud were still in progress. So, [I turned to RECAP](/posts/how-to-track-federal-court-cases/) to lookup the original criminal court records related to these crimes, I found that [this query](https://www.courtlistener.com/?q=(%22Democratic%20People%27s%20Republic%20of%20Korea%22%20OR%20DPRK%20OR%20%22North%20Korea%22)%20(%22Information%20Technology%22%20OR%20%22application%20developer%22%20OR%20%22application%20Development%22%20OR%20%22software%20developer%22%20OR%20%22software%20development%22)&type=r&order_by=dateFiled%20desc&case_name=%22United%20States%20v.%22) worked well for finding related criminal cases:

 ```text
Courts: All
Query: ("Democratic People's Republic of Korea" OR DPRK OR "North Korea") ("Information Technology" OR "application developer" OR "application Development" OR "software developer" OR "software development")
Case Name: "United States v."
```

> As a side-effect, this query also picked up cases against property rather than people, known as _in rem_ (pronounced race) jurisdiction cases; things like email accounts and cryptocurrency. These cases are usually related to North Korea's ransomware activities, which are not covered in this post. I decided not to filter out _in rem_ cases in the above search query out of curiosity.
{: .prompt-info }

While looking though the results, I found another case, [_United States v. Vong_](https://www.justice.gov/opa/pr/maryland-man-pleads-guilty-conspiracy-commit-wire-fraud), that while technically newer than _Chapman_ ended with a plea agreement before the _Chapman_ plea agreement, likely because only one charge was ever involved, Conspiracy to Commit Wire Fraud.

[Docket](https://www.courtlistener.com/docket/68814692/united-states-v-vong/)

Now, finally, on to the content that I promised in the title of this post, the cases currently in litigation.

## United States v. Jin et al

Two North Korean IT workers, Jin Sung-Il, and Pak Jin-Song, a Mexican citizen named Pedro Ernesto Alonso De Los Reyes, and US citizens Erick Ntekereze Prince and Emanuel Ashtor are [accused of a conspiracy](https://storage.courtlistener.com/recap/gov.uscourts.ncwd.118464/gov.uscourts.ncwd.118464.1.0.pdf) to allow the North Koreans to gain work under false identities. Once work was obtained by a false identity, the victim company would send a laptop to one of the US conspirators who would allow the North Korean IT workers to access the laptop by installing Anydesk, TeamViewer, or by shipping the laptop off to China.

> During the course of the conspiracy, the co-conspirators fraudulently obtained  remote IT work from at least 64 U.S. companies, with payments from ten U.S. companies,  including Company A, Company B, and Company D, totaling approximately $866,255, some of which was laundered through Online Payment Platform 1 accounts. During the course of the
> conspiracy, an Online Payment Platform 1 account belonging to one of the China-based financial facilitators deposited at least $677,440 into a Chinese bank account.

> During the course of the conspiracy, the co-conspirators caused damage and loss to victim companies, with the value of such harms exceeding a total of $1 million for Company B,  Company D, and U.S. IT Company 1. The loss resulting from the co-conspirators' conduct included the costs borne by the victim companies for legal fees and to remediate computer networks and devices.

 > During the course of the conspiracy and as a direct result of his participation in the conspiracy, ERICK NTEKEREZE PRINCE was paid more than $89,000, through Taggcar Inc., representing funds obtained or otherwise derived from specified unlawful activity.

 > During the course of the conspiracy and as a direct result of his participation in the conspiracy, EMANUEL ASHTOR was paid more than $40,000, through Vali Tech Inc. and other means, representing funds obtained or otherwise derived from specified unlawful activity.

To do this, they allegedly created fake identification documents and contracting companies tied to addresses related to Prince or Ashtor, who allegedly received laptops sent by victim companies to the fake personas.

Jin Sung-Il is alleged to have used Ernesto Alonso De Los Reyes' identity with his consent, using a fake non-immigrant United States-Mexico-Canada Agreement ("USMCA") Professional (TN) visa.

![A photo of the fake visa for Pedro Ernesto Alonso De Los Reyes](/assets/images/fake-visa-for-pedro-ernesto-alonso-de-los-reyes.webp)

Prince is alleged to have used his staffing company, Taggcar Inc, to invoice a US staffing company approximately eight times, totaling approximately $75,709.00, for IT work performed by Jin, who was posing as Alonso De Los Reyes.

Glaus Li was a fake persona allegedly created by Pak, Prince, and Jin to fraudulently gain employment. Li used the email address `glausli1990@outlook.com`. A fake US passport and Social Security card was even created for this persona.

![A photo of a fake US passport for Glaus Li](/assets/images/fake-us-passport-for-glsus-li.webp)

![A photo of a fake Social Security card for Glaus Li](/assets/images/fake-social-security-card-for-glsus-li.webp)

Once victim companies shipped laptops to Li at US addresses of Prince, remote access wad achieved either by installing Anydesk or by shipping the laptop to China.

Ashtor allegedly used a company that he fraudulently created, Vali Tech Inc., to complete I-9 verification of a fake US passport for Jin, which used the identity K. Bane. Once a laptop addressed to K. bane was received by Ashtor, he allegedly installed Anydesk or Team/Viewer on it.

![A photo of a fake US passport for K.Bane](/assets/images/fake-us-passport-for-k-bane.webp)

The trial for Erick Ntekereze Prince and Emanuel Ashtor is [currently scheduled](https://storage.courtlistener.com/recap/gov.uscourts.flsd.682422/gov.uscourts.flsd.682422.48.0_1.pdf) for October 6, 2025 at 400 North Miami Avenue, Courtroom 11-1, Miami, Florida.

They face counts:

1. Conspiracy to Damage a Protected Computer ([18:731])
2. Conspiracy to Commit Wire Fraud and Mail Fraud ([18:1349])
3. Conspiracy to Commit Money Laundering ([18:1956]h)
4. Conspiracy to Transfer False Identification Documents ([18:1028]\(a)(2) and (f))

[Department of Justice Press release](https://www.justice.gov/opa/pr/two-north-korean-nationals-and-three-facilitators-indicted-multi-year-fraudulent-remote)

Dockets:

- [United States v. Jin, 1:25-cr-00291, (N.D. Ga.)](https://www.courtlistener.com/docket/70673091/united-states-v-jin/)
- [United States v. Emanuel Ashtor, 1:25-cr-20021, (S.D. Fla.)](https://www.courtlistener.com/docket/69570297/united-states-v-emanuel-ashtor/)
- [United States v. Prince, 1:25-mj-00017, (E.D.N.Y)](https://www.courtlistener.com/docket/69571399/united-states-v-prince/)

## United States v. Hwa, 4:24-cr-00648, (E.D. Mo.)

In this case, 14 North Korean IT workers are [accused of](https://storage.courtlistener.com/recap/gov.uscourts.moed.216774/gov.uscourts.moed.216774.2.0.pdf) creating, managing, or working for alleged DPRK front companies, Yanbian Silverstar in China and Volasys Silverstar in Russia. Together, the two companies employed at least 110 DPRK IT workers.

> Throughout the approximately six-year conspiracy, the defendants and their  conspirators employed by Yanbian Silverstar and Volasys Silverstar fraudulently possessed and used the identities of hundreds of U.S. persons to generate at least $88 million in illicit revenue for the DPRK.

The incitement makes it clear how important US persons were as facilitators of the conspiracy.

> The conspirators pretended to be U.S. persons seeking remote IT work by using  stolen, borrowed, or purchased identities. In some instances, to better hide their identities and  obtain employment, the conspirators paid U.S. persons and others to appear in their place at  interviews and provided direction and guidance to the U.S. persons during the interviews. After  being hired, the conspirators paid U.S. persons and others to receive and maintain laptops that  were provided by U.S. businesses. By using U.S. persons to interview in their place and to host employer-provided laptops, the conspirators created the false appearance that employers had hired  U.S. persons who were performing work from within the United States.

They agreed to pay facilitators handsomely for their help, but end up paying them much less than they agreed to.

> On or about October 16, 2021 , KIM YE WON and SOK KWANG HYOK agreed to pay A.P. approximately $1 ,000 a week to impersonate M.A., thereby allowing KIM YE WON and SOK KWANG HYOK to regularly work for U.S. Business #1.
>
> Between on or about September 19, 2019, and on or about April 24, 2023, AP. received at least $69,900 from the conspirators. These funds were sent to A.P.'s account at a U.S. money transfer service ("U.S. MTS #1"), which AP. created on or about September 19, 2021. KIM YE WON was responsible for most of A.P.'s payments, and KIM YE WON made these payments using an account at U.S. MTS #1 , which was created with the name and identifying information of "J.C.," a U.S. person whose identity was borrowed.

They created websites for fake companies to make their resumes look real.

> To further the deception and make their resumes appear more appealing, the conspirators claimed that they previously worked in similar roles for other U.S.-based companies. However, those companies were fake. To make the companies appear legitimate, the conspirators purchased and designed websites for them.

Sometimes they would extort their victims by threatening to leak data if they were not paid.

> As part of their revenue-generation operations, in some instances, the conspirators extorted the U.S. businesses that hired them. They first gained access to sensitive or proprietary information and then threatened to publish, and in some cases did publish, that information if the businesses that hired them did not pay them a specified sum.

They often used different identities for the employee and the account for the employee's paycheck, which should set off red flags.

> Between on or about October 18, 2021, and on or about April 15, 2022, U.S. Business #4 paid CHOE JONG YONG, who posed as R.W., approximately $95,000...The J.H. U.S. MTS #2 account received payments from U.S. Business #4 associated with the R.W. identity's employment.

In addition to stolen identities, they also found people willing to allow the use of their identities in exchange for a shockingly small amount of money.

> On or about December 3, 2019, to conceal their identities and appear to be non DPRK citizens, CHOE JONG YONG and SON UN CHOL paid B.T., a Belgian person, approximately $130 in order to use B.T.'s identity to obtain freelance IT work in the United States.

They all face counts:

1. Conspiracy to Violate the International Emergency Economic Powers Act
2. Conspiracy to Commit Wire Fraud
3. Money Laundering Conspiracy
4. Conspiracy to Commit Identity Theft

8 of them face a fifth count of Aggravated Identity Theft.

[Justice Department press release](https://www.justice.gov/archives/opa/pr/justice-department-disrupts-north-korean-remote-it-worker-fraud-schemes-through-charges-and)<br>
[Wanted posters](https://www.fbi.gov/wanted/cyber/dprk-it-workers)<br>
[Docket](https://www.courtlistener.com/docket/69459808/united-states-v-hwa/)

## United States v. Knoot, 3:24-cr-00151, (M.D. Tenn.)

Matthew Isaac Knoot, 38, of Nashville, Tennessee, is accused being a facilitator of North Korean IT workers using the persona Yang Di, who used the stolen identity Andrew M. Knoot allegedly received laptops from victim companies, hosted them at this Tennessee residences, and installed remote access software (namely called Splashtop Streamer) on them, thus building a laptop farm to allow DPRK IT workers to appear to be working from a US location.

He was allegedly paid for this work, though apparently not nearly as much as he had expected.

> KNOOT was paid $15,100 for his services, which is substantially less than the $500 per month, per laptop, plus 20 percent of money earned from the remote IT work that he had agreed to.

He was charged with:

1. Conspiracy to Cause Damage to Protected Computers ([18:371])
2. Conspiracy to Commit Money Laundering ([18:1956]\(h))
3. Conspiracy to Commit Wire Fraud ([18:1349])
4. Intentional Damage to a Protected Computer ([18:1030]\(a)(5)(A), [18:1030]\(c)(4)(B), [18:1030]\(c)(4)(B), [18:1030]\(c)(4)(A)(i)(I), [18:2]\(4))
5. Aggravated Identity Theft ([18:1028A]\(a)(1) and [18:2])
6. Conspiracy to Cause the Unlawful Employment of Aliens ([18:371])

As you first start reading [the indictment](https://storage.courtlistener.com/recap/gov.uscourts.tnmd.100565/gov.uscourts.tnmd.100565.3.0_3.pdf), you might consider it to be a leap a guy just setting up laptops was involved in the overall conspiracy. Indeed, Knoot's attorney makes this argument [in his motion to dismiss](https://storage.courtlistener.com/recap/gov.uscourts.tnmd.100565/gov.uscourts.tnmd.100565.76.0.pdf) counts 1, 4, 5, and 6.

> The Government claims that Matthew Knoot committed, conspired to commit, or aid-and abetted the commission of no less than six crimes, including computer fraud, wire fraud, money laundering, aggravated identity theft, and unlawful employment of an unauthorized alien.
>
> The reason?  Because (according to the indictment) Knoot, acting at the direction of a person referred to as “Yang Di” (Yang), agreed in exchange for a small fee to install commercially available remote desktop applications onto a couple of laptops owned by companies that Yang  said he worked for so that Yang could log on to the laptops and do his job.  Unbeknownst to Knoot, however, Yang evidently used another person’s identity to obtain the jobs, meaning that neither he nor the person whose identity he used actually worked for the companies.

However, the source of payments made to Knoot as shown on page 13 of the indictment makes it very clear that the source countries China and Bangladesh and varying names from someone claiming to be the US citizen "Andrew M." should have at least raised alarm with Knoot, which is probably why they didn't move to dismiss counts 2 and 3.

Payment Date|Amount (USD)|Sender Country|Sender First Name|Sender Last Name
------------|------------|--------------|-----------------|----------------
1/30/2023   |1,100       |Bangladesh    |MST NASIMA       |KHATUN
11/30/2022  |1,600       |China         |tingting         |sun
11/2/2022   |1,600       |China         |tingting         |sun
9/29/2022   |1,600       |China         |chenglong        |jin
8/31/2022   |1,900       |China         |tingting         |sun

Instead, the Defense tried to argue that legally, no identity theft had occurred. The Government was having none of that [its response](https://storage.courtlistener.com/recap/gov.uscourts.tnmd.100565/gov.uscourts.tnmd.100565.80.0.pdf). The motion was partially granted: only count 6 was dismissed. Unfortunately, the Court's explanation was provided [during a teleconference](https://storage.courtlistener.com/recap/gov.uscourts.tnmd.100565/gov.uscourts.tnmd.100565.88.0.pdf), and no records or transcripts are currently on PACER. I have contacted to Court to ask for recordings and transcripts to be published on PACER, and I will update this post if they do so.

I noticed a couple of items on the Knoot docket that make this case unique from all other prosecutions of alleged facilitators so far. First, the Government has [given notice](https://storage.courtlistener.com/recap/gov.uscourts.tnmd.100565/gov.uscourts.tnmd.100565.57.0.pdf) that it plans to submit classified information in this case under [The Classified Information Procedures Act (CIPA)](https://www.congress.gov/crs_external_products/IF/PDF/IF12807/IF12807.1.pdf). It is widely known that North Korea engages in this sort of fraud, and uses US nationals to wittingly or unwittingly help them, so what classified information needs to be involved in this trial? The indictment in this case is very light on specifics, especially when compared with _Chapman_, so it seems that classified information must be needed to bolster the government's case. Second, both [the Government](https://storage.courtlistener.com/recap/gov.uscourts.tnmd.100565/gov.uscourts.tnmd.100565.61.0.pdf) and [the Defense](https://storage.courtlistener.com/recap/gov.uscourts.tnmd.100565/gov.uscourts.tnmd.100565.99.0.pdf) have given notice that they will call expert witnesses to testify. This will defiantly be a case to follow closely.

**Update 8/08/2025**: The United States has moved for the Court to [exclude the testimony of the defendant's expert witness](https://ecf.tnmd.uscourts.gov/doc1/16906160969?caseid=100565) on the basis of the defendant filing the notice of expert witness two weeks after the deadline to do so had passed.

The trial is [currently scheduled](https://storage.courtlistener.com/recap/gov.uscourts.tnmd.100565/gov.uscourts.tnmd.100565.100.0.pdf) for October 14, 2025, beginning at 9:00 a.m.

[Justice Department press release](https://www.justice.gov/usao-mdtn/pr/department-disrupts-north-korean-remote-it-worker-fraud-schemes-through-charges-and)<br>
[Docket](https://www.courtlistener.com/docket/69026861/united-states-v-knoot/)

## United States v. DIDENKO, 1:24-cr-00261, (D.D.C.)

Olesandr Didenko, also known as Alexander Didenko is a Ukrainian national last known to reside in Kyiv. Didenko is [accused](https://storage.courtlistener.com/recap/gov.uscourts.dcd.269128/gov.uscourts.dcd.269128.1.1.pdf) of operating a website called UpWorkSell, where users can rent accounts for freelance IT sites belonging to other ideates, as well as credit cards or SIM cards. Users can also buy or rent accounts at Money Service Transmitters (MSTs). In short, UpWorkSell provides all of the services needed to allow its users to conduct IT work fraud.

> As explained further herein, evidence collected during the investigation reveals that DIDENKO manages as many as approximately 871 proxy identities, provides proxy accounts for 3 freelance IT hiring platforms, and provides proxy accounts for 3 different MSTs. In coordination with co-conspirators, DIDENKO facilitates the operation of at least 3 US.-based “laptop farms” hosting approximately 79 computers. DIDENKO’s 3 MST accounts, which he uses to send and receive funds in furtherance of the scheme, have received approximately $920,000 in U.S.D. payments since July 2018.

The complaint against Didenko includes excerpts of chats, which include mentions of Christina Chapman and North Korea. The complaint mentions other laptop farms, so if Didenko decides to cooperate in a plea deal, (or not) we could see many more arrests.

Didenko was arrested on December 31, 2024. His plea hearing is currently scheduled for September 17, 2025, at 2:00 p.m. in Courtroom 8.

He faces counts:

1. Conspiracy to Commit Wire Fraud ([18:1343] & [1349][18:1349])
2. Conspiracy to Defraud the United States ([18:371])
3. Conspiracy to Falsely Represent to be a Citizen of the United States ([18:911], [371][18:371])
4. Aggravated Identity Theft ([18:2] and [1028][18:1028A](a)(1))
5. Conspiracy to Commit Fraud and Related Activity in Connection with Identification Documents ([18:1028]\(a)(7), (b)(1)(D), (c)(3)(A), & (f))
6. Conspiracy to Cause Unlawful Employment of Aliens ([18:371] and [8:1324a]\(a)(1)(A) and [1324a]1324a(f)(1))
7. Conspiracy to Launder Monetary Instruments ([18:1956][18:1956](a)(1)(B)(i) & (h))
8. Conspiracy to Launder Monetary Instruments ([18:1956][18:1956](a)(1)(B)(i) & (h))
9. Prohibition of Unlicensed Money Transmitting Business ([18:1960][18:1960](a))

[Justice Department press release](https://www.justice.gov/usao-dc/pr/charges-and-seizures-brought-fraud-scheme-aimed-denying-revenue-workers-associated-north)<br>
[Docket](https://www.courtlistener.com/docket/68810724/united-states-v-didenko/)

## What next?

Now we wait. I'm going to keep a close eye on these cases, so look for new blog posts here.

In the meantime, the IT-ISAC recently published a [great article](https://www.it-isac.org/post/do-you-know-who-you-are-hiring-spotting-fraudulent-job-seekers) about how to avoid and detect fraudulent job applicants and employees. It includes advice like requiring video interviews without virtual backgrounds, confirming that an applicant's previous employers are real, and once an employee is hired check that payment accounts match the employee's name and systems for unauthorized remote access software, as well as hardware like KVM over IP devices, and more.

[8:1324a]: https://www.law.cornell.edu/uscode/text/8/1324a
[18:2]: https://www.law.cornell.edu/uscode/text/18/2
[18:371]: https://www.law.cornell.edu/uscode/text/18/371
[18:911]: https://www.law.cornell.edu/uscode/text/18/911
[18:1028]: https://www.law.cornell.edu/uscode/text/18/1028
[18:1028A]: https://www.law.cornell.edu/uscode/text/18/1028A
[18:1030]: https://www.law.cornell.edu/uscode/text/18/1030
[18:1343]: https://www.law.cornell.edu/uscode/text/18/1343
[18:1344]: https://www.law.cornell.edu/uscode/text/18/1344
[18:1349]: https://www.law.cornell.edu/uscode/text/18/1349
[18:1956]: https://www.law.cornell.edu/uscode/text/18/1956
[18:1960]: https://www.law.cornell.edu/uscode/text/18/1956
