---
layout: post
title: "Legal Rights of Voluntary Mental Health Patients in Ohio: A ChatGPT success story"
description: A case study in how AI assistants like ChatGPT can help assert rights, as long as you check their output
image:
 path: /assets/images/ai-hospital-outside.webp
 alt: An AI-generated image of the outside of a hospital
date: 2025-06-28 13:17 -0400
categories:
  - Healthcare
  - Law
tags:
  - AI
  - LLMs
  - ChatGPT
  - Mental Health
  - Healthcare
  - Law
---
Recently, a family friend called my mother with an urgent problem. Her adult daughter had spent a huge sum of money for an inpatient program for insomnia, but the therapy sessions were being cancelled, and the facility was refusing to let her leave without staying for a 72 hour hold and signing Against Medical Advice (AMA) paperwork. We all knew that this sounded illegal, but didn't have the resources to prove it.

I thought this kind of research would be perfect for AI, but I knew that I shouldn't depend on my [local Large Language Models (LLMs)][ollama] for something this urgent, especially when Gemma3 ia more likely to make things up than other models, so I turned to ChatGPT.

I explained the situation to ChatGPT, and told it to provide sources, then I checked the sources of the output. Impressively, when I told ChatGPT that one of its legal citations was incorrect it searched the web, found the correct citation, provided sources, and updated the draft letters.

![Screenshot of ChatGPT's response when I pointed out out the mistake](/assets/images/chatgpt-ohio-code-correction.webp)

Once the patient provided this information and asserted her rights, the facility relented and allowed her to leave. Afterwards, I asked a therapist about why a facility would try and keep her there. The answer: money. Every day they kept her there was another day they wouldn't need to prorate in a refund of her upfront payment when she left. Similarly, when patients use insurance for funding, the insurance company will tell the facility the maximum number of days that they will cover for a stay. The facility will then try to keep the patient for the full number of days no matter what to maximize the payout.

Here are all of the relevant details for anyone who finds themselves or someone they know in a similar situation. Most states have similar laws to Ohio. So if you are in another state try asking ChatGPT, just remember to always ask it to provide sources, then check those sources to see if they support what ChatGPT is saying.

## Voluntary Admission Means the Patient Can Request to Leave

Under Ohio Revised Code § [5122.03][5122.03], an individual admitted voluntarily to a psychiatric facility has the right to request discharge. The facility must release the individual unless, within three court days, the chief clinical officer files an affidavit for emergency detention under § [5122.11][5122.11].

This means unless the individual is mentally ill and represents a substantial risk of physical harm to self or others, or is gravely disabled, they cannot be legally held.

## Legal Grounds for Holding a Person Against Their Will

According to Ohio Revised Code § [5122.10] and § [5122.11][5122.11], a person may only be held against their will if they are mentally ill and present a substantial risk of physical harm to themselves or others, or cannot provide for their own basic needs.

Legal procedures including filing an affidavit and court involvement are required. The maximum emergency detention period is 72 hours (excluding weekends and holidays).

## AMA (Against Medical Advice) Forms Are Not Legally Binding

Facilities may ask patients to sign an AMA form when leaving against medical advice. However, this is not a legal requirement. Refusal to sign does not allow the facility to detain someone who wishes to leave voluntarily.

## Payment Status Is Irrelevant to Civil Rights

Whether a person uses insurance or pays privately does not affect their civil rights. A facility cannot detain someone based solely on payment or an unfinished program.

## Ohio Consumer Protection Law and Misrepresentation of Services

Ohio Revised Code § [1345.02][1345.02] prohibits unfair or deceptive acts in consumer transactions, including misrepresenting services.

A facility may be in violation if they:

- Advertise or promise services (like daily sessions or specific treatments) that are not provided.
- Omit or misrepresent refund policies or billing details.

Key Provision:
ORC § 1345.02(B)(1): It is deceptive to state that a service has characteristics or benefits that it does not.

## What Patients Can Do

If a person wants to leave or request a refund:

- Submit a written request for discharge.
- Request an itemized bill and refund for undelivered services.
- If denied, contact:
  - [Disability Rights Ohio][Disability Rights Ohio]
  - [Ohio Attorney General][Ohio Attorney General]
  - A legal aid or consumer protection attorney.

## Sample Discharge Request Letter

[Full Name]\
[Facility Name]\
[Date]

To Whom It May Concern,

I am writing to request my immediate discharge from [Facility Name], where I was voluntarily admitted. I am not suicidal, not a danger to others, and I am able to care for myself.

Under Ohio Revised Code § 5122.03, I retain the right to leave unless I meet the legal criteria for involuntary commitment, which I do not.

Please consider this my formal discharge request. I understand the risks of leaving early and take full responsibility. I am open to receiving any aftercare instructions.

I respectfully ask that no delay or additional documentation be required for my release. If not released promptly, I will explore legal remedies.

Sincerely,

[Full Name]\
[Signature]

## Sample Refund Request Letter

[Full Name]\
[Facility Name]\
[Date]

To Whom It May Concern,

I am requesting a refund for services not rendered during my recent voluntary stay at your facility. I was admitted on [Admission Date] and left on [Discharge Date]. Promised services were not provided.

I paid [Amount] in advance expecting full program access. This misrepresentation violates Ohio Revised Code § 1345.02(B)(1), which prohibits deceptive consumer practices.

Please issue a full refund. I expect a response within 10 business days before I escalate this to the Ohio Attorney General or seek legal advice.

Sincerely,

[Full Name]\
[Signature]

## Printable version

Here is a [printable PDF][PDF] of this information.

[ollama]: /posts/how-to-run-ollama-and-open-webui-as-a-systemd-service-using-docker-compose/
[5122.03]: https://codes.ohio.gov/ohio-revised-code/section-5122.03
[5122.10]: https://codes.ohio.gov/ohio-revised-code/section-5122.10
[5122.11]: https://codes.ohio.gov/ohio-revised-code/section-5122.11
[1345.02]: https://codes.ohio.gov/ohio-revised-code/section-1345.02
[Disability Rights Ohio]: https://www.disabilityrightsohio.org
[Ohio Attorney General]: https://www.ohioattorneygeneral.gov
[PDF]: /assets/documents/Ohio_Mental_Health_Rights_and_Refund_Guide.pdf
