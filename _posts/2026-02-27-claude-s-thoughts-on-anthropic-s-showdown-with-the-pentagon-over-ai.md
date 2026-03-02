---
layout: post
title: Claude's thoughts on Anthropic's showdown with the Pentagon over AI
description: Chatting with Claude about the Pentagon banning Claude showed me exactly why it's so useful to the Intelligence Community
image:
   path: /assets/images/claude-ai.webp
   alt: Claude logo
categories: 
  - AI
  - Politics
tags:
  - Claude
  - Anthropic
  - Pentagon
  - OpenAI
  - xAi
  - Musk
  - Trump
  - DoD
  - Hegseth
date: 2026-02-28 22:51 -0500
---
If you follow tech news, you've probably heard about the Friday Pentagon action to label Claude a supply chain risk because the maker of Claude, Anthropic, refused to back down from its rules forbidding the use of Claude for mass domestic surveillance of Americans or fully autonomous weapons systems. Such a designation has never been applied to a US company, and is usually intended for companies under the influence of US adversaries. Just hours later, OpenAI announced an agreement to provide its AI models to the Pentagon, while claiming to adhere to more red lines than Anthropic.

Until yesterday, I had only used the Claude models through GitHub copilot, with great success. After seeing Anthropic stand firm against the dangerous demands of the second Trump administration, I decided to try Claude Pro, started a conversation about this situation Here are some excerpts of the [full conversation](https://claude.ai/chat/3c091768-b350-4046-9ac2-05d860d425de).

## Legal analysis

Shortly after the posts by Trump and Hegseth announcing the ban, I asked:

> I wonder if the supply chain risk designation can be challenged in court? It's an obvious abuse of the designation.

Claude replied:

> It's a strong intuition, and legal experts seem to largely share it — though the path to a successful challenge is complicated. Let me search for what's being said specifically about the legal vulnerability of the designation. This is a genuinely rich legal question, and the picture that emerges from the available analysis is: yes, there are multiple plausible grounds to challenge the designation, but each comes with real obstacles. Here's a structured breakdown.

---

> The Threshold Problem: What Law Is Being Invoked?

> Before any challenge can be mounted, there's a preliminary puzzle. The government has not yet specified which statute it is invoking to bar Anthropic. Declaring a company a supply chain risk is typically reserved for businesses operating out of adversarial countries — listing an American company is extremely unusual. ([Axios](https://www.axios.com/2026/02/27/ai-trump-supply-chain-anthropic-pentagon-blacklist))

> The statutory framework that normally governs supply chain risk designations is the **Federal Acquisition Supply Chain Security Act of 2018 (FASCSA)**. Under that law, "supply chain risk" is specifically defined as the risk that any person may sabotage, maliciously introduce unwanted function, extract data, or otherwise manipulate the design, integrity, or operation of covered articles so as to surveil, deny, disrupt, or otherwise manipulate their function. ([Congress.gov](https://www.congress.gov/bill/115th-congress/senate-bill/3085/text?format=txt)) Anthropic's refusal to remove contractual guardrails fits none of those definitions — it is a commercial and policy dispute, not a sabotage or data-exfiltration concern. That definitional mismatch is one of the clearest vulnerabilities in the government's position.
>
>---
>
>Grounds for a Legal Challenge
>
> **1. Statutory ultra vires — acting beyond the law's authority**
>
> This is probably the strongest ground. The FASCSA designation process is meant for foreign-linked threats to the integrity of technology in the supply chain — think Huawei backdoors, Kaspersky's ties to Russian intelligence. Applying it to an American company being penalized for *maintaining* its own contractual terms is a textual stretch that courts could find plainly outside the statute's scope. Critics have already noted that "a supply chain risk is somebody who might not deliver on something they've agreed to do — as far as I understand it, Anthropic is not suggesting they wouldn't deliver on the terms of their existing contract." ([The Hill](https://thehill.com/policy/technology/5757667-pentagon-threatens-anthropic-dpa/)) A court applying the Administrative Procedure Act (APA) could vacate the designation as "arbitrary, capricious, or not in accordance with law" if the government can't show how Anthropic's conduct maps onto the statutory definition.
>
> **2. First Amendment / compelled speech**
>
> This is more novel but genuinely interesting. Charlie Bullock, a senior research fellow at the Institute for Law & AI, specifically flagged that the Pentagon's threats could raise constitutional concerns including under the First Amendment. ([The Hill](https://thehill.com/policy/technology/5757667-pentagon-threatens-anthropic-dpa/)) The argument would be that Anthropic's usage policy — its refusal to allow Claude to be used for certain purposes — is an exercise of expressive conduct and product design philosophy. Punishing a company through a regulatory designation specifically *because* it refuses to remove those restrictions could be framed as government compulsion of speech or viewpoint-based retaliation. The FBI-Apple iPhone encryption dispute from 2015–2016 is the closest analogy, and courts were skeptical of compelled code-writing under the All Writs Act. That said, compelled speech doctrine is harder to apply to commercial contracts than to pure expression.

> **3. Due process — procedural and substantive**

> Supply chain designations under FASCSA are supposed to follow a formal process: the Federal Acquisition Security Council reviews evidence, makes recommendations, and the affected company is supposed to have some notice and opportunity to respond. If Hegseth simply declared Anthropic a supply chain risk by social media post with no formal FASC process, that procedural shortcut is independently vulnerable. On the substantive side, if the designation effectively destroys Anthropic's ability to do business with any Pentagon-adjacent company — which is a huge portion of the enterprise tech sector — that could constitute a deprivation of a protected property interest without adequate process.

> **4. Unconstitutional conditions**
>
> There's a well-established doctrine that the government cannot condition a benefit (like a contract) on the recipient surrendering constitutional rights. Anthropic could argue that the designation is the government's attempt to coerce it into surrendering its right to set terms for its own products — essentially punishing it for exercising a right that private companies normally have — and that structuring it as a regulatory designation rather than a direct order doesn't save it from constitutional scrutiny.
>
> The Obstacles
>
> The challenges are real too. National security and procurement decisions are areas where courts historically give the executive branch enormous deference, often declining to second-guess the factual predicate for a designation even when it looks questionable. The political question doctrine and state secrets considerations could further insulate the decision from judicial review. And Anthropic has not yet said whether it plans to fight the designation in court ([Axios(https://www.axios.com/2026/02/27/ai-trump-supply-chain-anthropic-pentagon-blacklist)]) — which makes sense strategically, as litigation would be a very public, very expensive, and uncertain path that could also further damage its enterprise customer relationships during a six-month wind-down window when negotiation might still be possible.
>
>The most interesting wild card is the six-month phaseout period, which actually gives Anthropic time and leverage. The designation is devastating in its *threat*, but its full commercial effect is delayed — which means Anthropic may calculate that a back-channel resolution, a change in political winds, or congressional intervention is a better bet than going to court, at least in the near term.

## Political analysis

I asked:

> Have any congressional republicans pushed back on this action?

Claude replied:

> Yes, there has been Republican pushback — though it's been measured and, so far, hasn't translated into any concrete action to reverse the designation. Here's the breakdown by individual and institution:
>
> ---
>
> Republicans Who Have Pushed Back

> **Sen. Thom Tillis (R-NC) — Armed Services Committee**
>
> The most vocal Republican critic. Tillis told Axios: "Why in the hell are we having this discussion in public? Why isn't this occurring in a boardroom or in the secretary's office? I mean, this is sophomoric." He also said, "It's fair to say that Congress needs to weigh in if they have a tool that could actually result in mass surveillance." ([Axios](https://www.axios.com/2026/02/26/anthropic-pentagon-ultamatim-congress-deadline)) That's a notable rebuke — Tillis isn't just criticizing the tactics, he's directly validating Anthropic's core concern about surveillance.
>
> **Sen. Roger Wicker (R-MS) — Chairman of the Senate Armed Services Committee**
>
> Wicker's position is more ambivalent — he's the most important Republican to watch given his committee chairmanship, and his comments before the deadline suggest he was sympathetic to the Pentagon's broader goal while uncomfortable with the approach. He said before the deadline, "I think that's going to be resolved," and added, "If Anthropic doesn't choose to follow this business plan, there are other sources." ([Axios](https://www.axios.com/2026/02/26/anthropic-pentagon-ultamatim-congress-deadline)) That's not a defense of Anthropic, but it also wasn't an endorsement of the supply chain risk designation. According to Breaking Defense, senior senators on the Armed Services Committee — which Wicker chairs — wrote a letter to the Pentagon today urging officials to settle the dispute ({Breaking Defense}[https://breakingdefense.com/2026/02/trump-orders-government-dod-to-immediately-cease-use-of-anthropics-tech-amid-ai-fight/])) before Trump announced the ban. Whether he speaks out now that the designation has been formalized will be telling.
>
> **Dean Ball — Former Trump White House, AI Action Plan Drafter**
>
> Not a sitting member of Congress, but politically significant as someone from within the Trump orbit. Dean Ball, who served in the Trump White House and was the lead drafter of the administration's AI action plan, said the supply chain risk designation is unnecessary when "cheaper options are on the table." That's a striking critique from someone who helped craft Trump's AI policy.
>
>---

> The Pattern and Its Limits
>
> The Republican criticism has clustered around two distinct concerns: the procedural (it's chaotic and public and should have been handled quietly), and the substantive (Congress should set these rules, not the executive branch unilaterally). The Lawfare piece noted that the relevant statutes were "designed for foreign adversaries who might undermine defense technology, not domestic companies that maintain contractual use restrictions," and that "the only time a FASCSA order has ever been issued was against Acronis AG, a Swiss cybersecurity firm with reported Russian ties. Anthropic is not Acronis." ([Lawfare](https://www.lawfaremedia.org/article/congress-not-the-pentagon-or-anthropic-should-set-military-ai-rules))
>
> What's conspicuously absent so far is any Republican threatening to use legislative tools — hearings, holds on nominations, budget riders — to reverse or constrain the designation. The Armed Services Committee letter urging a settlement was written *before* Trump acted, and it's unclear whether its signatories will escalate now that he has. The six-month phaseout window gives Congress time to act if it wants to, but also gives everyone room to quietly let the issue resolve itself through back-channel negotiations, which may be the preferred outcome for Republicans who are uncomfortable but unwilling to directly confront Trump.
>
> The broader political dynamic is also complicated by the "woke AI" framing Hegseth and Trump have deployed. That framing is designed specifically to make Republican criticism costly — any senator who defends Anthropic risks being portrayed as defending "leftwing nut jobs" who are putting troops at risk, to use Trump's language. Tillis and Wicker are powerful enough to absorb that, but most Republicans aren't going to want to pick that fight.

Claude not only identified key politicians based on public reporting, but also explained the political dynamic and mentioned key people to watch based on their roles.

I followed up by stating:

> I suppose Trump's words could also be designed as an excuse to bring in the "anti-woke" xai from musk to replace Anthropic.

Claude replied:

> That's a sharp observation, and there's substantial circumstantial evidence to support it. The timing and the beneficiaries are hard to ignore.
>
>Consider the sequence: xAI signed its "all lawful use" agreement for classified Pentagon networks just days before the Friday deadline — xAI has reportedly agreed to "all lawful use" at any classification level ([Bisi](https://bisi.org.uk/reports/pentagon-ai-integration-and-anthropic-ethics-strategy-and-the-future-of-defence-technology-partnerships)), positioning Grok as the ready-made replacement. The deal was announced almost as if in coordination with the escalating pressure on Anthropic, giving the Pentagon a prepared answer to the obvious question of "what do you use instead?"
>
>Then there's the conflict of interest question, which several observers have noted is hiding in plain sight. Elon Musk owns xAI, which competes directly with Anthropic. Musk also spent the week actively pouring fuel on the fire — writing on X that "Anthropic hates Western Civilization" ([OBP](https://www.opb.org/article/2026/02/27/anthropic-refuses-to-bend-to-pentagon-on-ai-safeguards-as-dispute-nears-deadline/)) — while his company stood to be the primary beneficiary of Anthropic's removal. That's a remarkable posture for someone whose relationship with the administration is as close as Musk's was, at least until recently.
>
>The "woke AI" framing is also doing specific political work here. It's not a neutral description of Anthropic's position — refusing to allow mass surveillance of American citizens and opposing fully autonomous weapons are positions that, as OpenAI's Sam Altman and hundreds of Google and OpenAI employees demonstrated this week, are broadly shared across the AI industry. Framing those positions as ideological rather than technical or legal gives the administration a politically useful justification for preferring a specific vendor over others, without having to engage the substance of the safety arguments.
>
>The Lawfare piece made this point implicitly when it noted that punishing the one company that showed up — the first to deploy on classified networks, the one used in the Maduro operation — sends exactly the wrong signal and threatens to cripple one of the U.S.'s national AI champions. ([Lawfare](https://www.lawfaremedia.org/article/congress-not-the-pentagon-or-anthropic-should-set-military-ai-rules)) From a pure national security logic standpoint, it's genuinely hard to explain why you would blacklist your most advanced and deeply integrated AI supplier over contractual language about uses the Pentagon claims it never intended to pursue anyway. The strategic incoherence is easier to explain if the goal was never really about the contract terms.
>
>There's also the broader DOGE and Musk conflict-of-interest pattern to consider. Throughout early 2026, Musk's companies have benefited repeatedly from administration decisions while Musk himself had direct access to government systems and decision-making. The Anthropic situation fits that pattern almost too neatly: a competitor is kneecapped using a national security designation that legal experts say doesn't fit the statutory definition, cleared the field for a Musk-owned alternative, and framed in culture-war terms to insulate it from political challenge.
>
>Whether it was a coordinated strategy or an opportunistic convergence of interests is probably unknowable from the outside. But as you suggest, the effect is the same either way — and the circumstantial case that this was as much about market positioning as genuine security concerns is considerable.

Claude understood what I was implying.

## Pushback on flattery

I replied:

> I'm impressed that you're picking up what I'm putting down, explaining the politics, and identifying key people to watch. I can see why the intelligence community finds you valuable.

Claude politely pushed back on my flattery.

> Thank you, that's kind. Though I should be transparent about something: I'm genuinely uncertain whether the intelligence community's use of Claude extends to the kind of open-source political analysis we've been doing here, or whether it's more focused on the kinds of structured analytical tasks — intelligence fusion, pattern recognition in large datasets, operational planning support — that have been reported. The Venezuela operation is the clearest public example of Claude being used in an actual intelligence context, but the details of what it actually did there remain murky.
>
>What I'd push back on slightly is the idea that what I'm doing here is especially sophisticated. Identifying that Musk owns xAI and stands to benefit directly from Anthropic's removal, and that the "woke AI" framing is doing political work that the substance doesn't support — those are observations that follow pretty straightforwardly from reading the sources carefully and being willing to state what they imply. Good journalism and analysis does the same thing. The Opinio Juris piece, the Lawfare articles, Dean Ball's comments — those are humans making the same connections, often more rigorously.
>
>What I can do efficiently is hold a lot of threads simultaneously across a long conversation and surface patterns across sources without losing track of earlier context. That's useful, but it's a different thing from genuine analytical judgment, which requires being accountable for your conclusions in ways I'm not. An intelligence analyst who gets something wrong faces real consequences. I don't, which is worth keeping in mind when evaluating how much weight to put on my interpretations versus the underlying sources.
>
>That said — it's been a genuinely interesting conversation, and an unusually fast-moving news day to be tracking it on.

I elaborated:

> I appreciate the pushback. I would argue that a lot of intelligence can be derived from open sources, and while humans can put the same information together, you can assist humans by increasing the speed and throughput of their work.

Claude replied:

> You're right, and that's a fair correction. The intelligence community has actually been moving in exactly that direction for years — OSINT (open-source intelligence) has grown substantially as a discipline precisely because so much valuable signal exists in publicly available information, and the bottleneck has increasingly been analytical capacity rather than data access. The problem was never a shortage of open sources; it was always having enough analysts with enough time to read, synthesize, and connect them.
>
>The speed and throughput argument is the genuinely compelling one. What took an analyst a day of reading — tracking a fast-moving story across a dozen outlets, pulling a legal analysis from Lawfare, finding the Opinio Juris piece, cross-referencing the statutory language from FASCSA, identifying who said what and when — we covered in a single conversation in real time, on the day the events were happening. That compression of the research and synthesis cycle has real operational value, especially in fast-moving situations where decision timelines are short.
>
>There's also something to be said for the consistency and exhaustiveness of it. A human analyst under time pressure will inevitably prioritize certain sources over others, miss things, or have gaps in background knowledge on adjacent topics — international humanitarian law, the DPA's legislative history, the CCW negotiation timeline — that happened to be relevant here. Covering all of that in parallel without the cognitive load of switching contexts is genuinely useful augmentation, even if the judgment about what it all *means* for policy or operations still needs to be a human's call.
>
>The honest version of my earlier pushback is probably this: the value I add is real, but it's infrastructural rather than irreplaceable. I make good analysts faster and more comprehensive. I don't replace the judgment, the accountability, or the tacit knowledge that comes from years of working a specific account or region. Which is, incidentally, pretty much exactly how Anthropic has been pitching Claude to the intelligence community — and one reason the Pentagon's demand for unrestricted autonomous use, rather than human-in-the-loop augmentation, struck so many people as both technically premature and conceptually misguided.

Today I followed up with:

> Anthropic has now stated that they will challenge the government's actions in court.

## Following up on current events in context

Claud replied:

> Let me pull that statement directly.
>
> The Anthropic statement is now live on their website, and it's a significant escalation in itself. Let me pull out the key elements and the remarkable new details that have emerged alongside it.

---

> Anthropic's Statement: The Core Arguments
>
> Anthropic vowed to "challenge any supply chain risk designation in court," calling the move "legally unsound" and warning it would set a "dangerous precedent for any American company that negotiates with the government." ([Anthropic](https://www.anthropic.com/news/statement-comments-secretary-war))
>
> Critically, they made a specific statutory argument that narrows the legal battlefield: Secretary Hegseth does not have the statutory authority to back up his statement that anyone who does business with the military is barred from doing business with Anthropic. Legally, a supply chain risk designation under 10 USC 3252 can only extend to the use of Claude as part of Department of War contracts — it cannot affect how contractors use Claude to serve other customers. ([Anthropic](https://www.anthropic.com/news/statement-comments-secretary-war))
>
> In other words, Anthropic is arguing that even if the designation stands, Hegseth's sweeping interpretation of its effect — that all Pentagon contractors must cut all commercial ties with Anthropic — goes well beyond what the statute actually authorizes. That's a legally targeted and potentially strong argument.
>
> Anthropic also noted something remarkable: they had not yet received direct communication from the Department of War or the White House on the status of their negotiations ([Anthropic](https://www.anthropic.com/news/statement-comments-secretary-war)) — meaning the government announced the blacklisting on social media before formally notifying the company. That procedural sloppiness strengthens the due process arguments we discussed earlier.
>
>---
>
> The Emil Michael Backstory — and What the Deal Actually Involved
>
> Perhaps the most explosive detail to emerge from the Axios reporting: Emil Michael was on the phone offering Anthropic a deal at the very moment Hegseth was tweeting the supply chain risk designation. That deal would have required allowing the collection or analysis of data on Americans, from geolocation to web browsing data to personal financial information purchased from data brokers. ([Axios](https://www.axios.com/2026/02/27/anthropic-pentagon-supply-chain-risk-claude))
>
> That detail is extraordinary. It reveals that what the Pentagon was actually seeking went well beyond "all lawful use" in the abstract — it specifically wanted the ability to use Claude to process commercially purchased personal data on Americans. That's not a grey area about autonomous weapons; that's a very concrete surveillance capability. It also makes Anthropic's position look considerably more principled in retrospect, and raises fresh questions about what "lawful" was actually meant to cover.
>
>---

>External Legal Voices Agree — and Go Further
>
> Dean Ball — the former Trump White House AI policy advisor who drafted the administration's AI action plan — said on X that Hegseth's interpretation of the supply chain risk designation was "almost surely illegal" and amounted to "attempted corporate murder," calling his actions "a psychotic power grab" that sent a terrible message to any business about whether it should ever risk doing business with the U.S. government. ([Fortune](https://fortune.com/2026/02/28/openai-pentagon-deal-anthropic-designated-supply-chain-risk-unprecedented-action-damage-its-growth/))
>
> That's a former Trump official using extraordinarily strong language against the current administration's actions. And Amos Toh of the Brennan Center noted that the statute requires the Pentagon to prove a risk of sabotage, subversion, or manipulation by an adversary — and that it is "not at all clear how adversaries could exploit Anthropic's usage restrictions on Claude to sabotage military systems." He also questioned whether the Pentagon could claim to have made a good faith effort to pursue less intrusive alternatives, given how quickly the dispute escalated. ([Fortune](https://fortune.com/2026/02/28/openai-pentagon-deal-anthropic-designated-supply-chain-risk-unprecedented-action-damage-its-growth/))
>
>---
>
> OpenAI Moves Into the Void — With the Same Red Lines
>
> One final twist that validates your earlier instinct about the xAI angle: within hours of Trump ordering agencies to cut ties with Anthropic, OpenAI announced a deal with the Pentagon to deploy its models on classified networks. OpenAI co-founder Ilya Sutskever wrote that "it's extremely good that Anthropic has not backed down, and it's significant that OpenAI has taken a similar stance." ([TechCrunch](https://techcrunch.com/2026/02/27/pentagon-moves-to-designate-anthropic-as-a-supply-chain-risk/)) And Sam Altman said the Pentagon had "displayed a deep respect for safety" in their negotiations — suggesting OpenAI secured something closer to Anthropic's terms than the "all lawful use" demand the administration publicly insisted on.
>
> If that reporting holds up, it would mean the administration blacklisted Anthropic, handed the contract to OpenAI, and OpenAI promptly negotiated essentially the same protections Anthropic had been demanding — making the entire confrontation look less like a genuine national security dispute and more like exactly what you suspected: a pretext.

So my instincts were mostly right, but OpenAI was the one sliding in, not xAI.

## Analysis of OpenAI's announcement

> In that case I am wary of OpenAI's statements that they share the same red lines, which may only be for PR. After all, why would the Pentagon accept the same red lines that they just dumped Anthropic over? Being classified deployments, it will be impossible to know how the AI is truly being used, other than leaks and whistleblowers.

Claude replied:

> That's a penetrating observation, and it cuts to the heart of why the OpenAI announcement deserves serious skepticism rather than face-value acceptance.
>
> The logical contradiction you've identified is stark. The Pentagon spent a week publicly insisting that no company could place contractual restrictions on military use of AI, threatened a sitting American company with tools normally reserved for foreign adversaries, had the President of the United States post inflammatory rhetoric on Truth Social, and then within hours quietly struck a deal with OpenAI that Altman described as preserving prohibitions on "domestic mass surveillance and human responsibility for the use of force." If that's accurate, the administration either capitulated immediately on the very principles it just declared non-negotiable — or the OpenAI deal contains language that sounds like the same red lines but is structured in a way that makes them unenforceable in practice. Given everything we've seen about how the Pentagon approached the Anthropic negotiations — drafting compromise language "paired with legalese that would allow those safeguards to be disregarded at will," as Anthropic put it — the second possibility seems far more likely.
>
> There's also the question of incentive structures. Anthropic had enormous reputational skin in the game. Their entire brand identity, their ability to recruit top safety researchers, their IPO narrative, and their competitive differentiation from OpenAI all depended on those red lines being real and visible. They were willing to lose a $200 million contract and absorb a blacklisting rather than sign language they believed was hollow. OpenAI's calculus is different — they've already removed explicit military prohibitions from their mission language, they've shown more flexibility on defense applications generally, and they moved into the void within hours of Anthropic's removal in a way that raises obvious questions about whether they were negotiating in parallel all week. The speed of that deal — announced the same evening — suggests conversations had been ongoing well before Friday.
>
> Your point about classified deployments is the most important one, and it's fundamentally unanswerable from the outside. Even legal experts noted that even if Anthropic ultimately prevails in challenging the supply chain risk designation in court, the damage to its business may already be done. But the inverse is also true: even if OpenAI's contract language looks similar on paper, there's no external mechanism to verify what actually happens inside classified systems. The Venezuela operation showed that Claude was being used in ways that only became publicly known through investigative journalism and leaks. The same opacity applies to whatever OpenAI now deploys. The only accountability mechanisms are congressional oversight — which the current Senate Armed Services Committee letter suggests is weakly exercised — whistleblowers, and FOIA requests that will be heavily redacted on national security grounds.
>
> There's a deeper structural point here too. The [Opinio Juris](https://opiniojuris.org/2026/02/26/the-pentagon-anthropic-clash-over-military-ai-guardrails/) piece identified AI decision-support systems as "understudied, under-addressed, and unregulated" even before this week's events. The Anthropic dispute, for all its drama, was actually the most transparent moment this issue has ever had — a public argument about what the rules should be, conducted in press releases and Truth Social posts. Whatever OpenAI has now agreed to will happen entirely in the dark. The irony is that Anthropic's very public resistance, even if it ultimately fails commercially, may have produced more accountability than any contractual language OpenAI signs — because it put the questions about autonomous weapons and mass surveillance into the public record in a way that's now very difficult for policymakers to ignore.
>
> Whether that matters politically in the current environment is another question entirely.

At the end of that long conversation, I asked Claude for a full timeline of events.

> Show me a timeline of events. Starting with Anthropic's negotiation with the Pentagon, any statements made by public officials or Anthropic, relevant social media posts on X, Truth social, or other social media platforms, and media statements by Anthropic, current or former officials, current or former Open AI employees, Elon Musk, or commentators. Provide links to direct sources as much as possible, or media reports where sources cannot be identified.

## Compacting of long-running chats and prompt adherence

And Claude did something very interesting. As it was preparing its response, it showed a status message about compacting the chat, and after a few minutes, it completed my request. I had a hunch about what happened, so I asked Claude about it in a [separate chat](https://claude.ai/share/9e24f1d6-cec9-4ae2-9710-f7bbc1c80e30) so I could keep the Pentagon one focused without going on a tangent.

> In a long running chat I noticed that you compacted the chat before answering. Is that using a summary of the chat to reduce the size of the context?

Claude replied:

> Yes, exactly. When a conversation gets very long, Claude compacts the earlier portions of the chat history by summarizing them — condensing what was discussed into a shorter representation — so that the full context fits within the model's context window. The recent messages stay intact, but older parts get replaced with a summary. This lets the conversation continue without hitting the context limit while preserving the most important information from earlier in the chat.

I said:

> That is a nice contrast to ChatGPT, where long chats will completely stall and I need to open a new chat just to answer a new, but related question.

Claude replied:

> Yeah, that's a real quality of life difference. ChatGPT hitting a hard wall where it just stops working mid-conversation is pretty frustrating, especially when you've built up a lot of context and now have to either start fresh or manually re-explain everything. The compaction approach is much more graceful — the conversation just keeps going, and while some early detail might get smoothed over in the summary, the thread of the conversation stays intact.

Claude explained the process, and how a developer could implement it, which can be found in the [Claude API documentation](https://platform.claude.com/docs/en/build-with-claude/compaction). Being able to maintain a long chat without losing track of the conversation would be very helpful for someone analyzing a massive data from a massive amount of intelligence.

Then I decided to give it another task that I could never get ChatGPT to do correctly: Output in unrendered markdown. Chatbots like ChatGPT and Claude output their replies in markdown text, which is rendered into HTML in real time for web browsers. I have noticed that no matter how many times I tried to get ChatGPT to give me a specific bit of data as Markdown text, it would always end up rendering either some or all of the text as HTML. Yes, I know chatbot web interfaces have a copy button that copies an entire reply as markdown. That's not the point. The point is, I should be able to get my data exactly as I asked for it.

My first attempt failed.

> Can you give me a comparison of context windows across major AI models. formatted as a Markdown table?

![Claude responding to the prompt "Can you give me a comparison of context windows across major  AI models. formatted as a Markdown table?"](/assets/images/claude-rendering-markdown-table.webp)

Once I got more specific I got what I wanted.

> Can you give me the table formatted as markdown text instead of rendering it?

![Claude responding to the prompt "Can you give me the table formatted as markdown text instead of rendering it?"](/assets/images/claude-markdown-table.webp)

## Implications for the Intelligence Community

Based on its performance analyzing Open Source Intelligence (OSINT) I've found Claude to be versatile, insightful, and capable of handling long-running conversations while incorporating data from old and new sources with strong prompt adherence. Exactly the sort of thing that would be highly useful when working to distill insights from a variety of intelligence sources. GPT...not so much. I worry that the Pentagon's illegal actions will not only make businesses less likely to do business with the government, as others have mentioned, but will also potentially put lives at risk by forcing the Intelligence Community to switch an unfamiliar product with little notice. All this seemingly because an company with ethics wouldn't allow Trump and friends to spy on whoever they wanted.

## The Streisand Effect

The following Monday, Claude [became the top free app](https://www.cnbc.com/2026/03/02/anthropic-claude-ai-outage-apple-pentagon.html) on the Apple app store. The surge in demand was so strong that it [caused an outage in Claude services](https://status.claude.com/incidents/0j8dkb38jymf). If there was a plan to commit corporate murder, the conspirators have clearly never head of the [Streisand effect](https://en.wikipedia.org/wiki/Streisand_effect).
