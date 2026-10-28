# Outcome-based agents and agentic orchestration: VC primer

_Version 3, dated 2026-10-27 (America/New_York). v2 was earlier on 2026-10-27; v1 was 2026-10-26. Built from the oba repo: insights/ (framework, evidence-by-question, weekly/2026-W44, bull-bear, comps, market-sizing, startup-landscape, labs-vs-startups, timeline, expert-calls), companies/ cards, and the sources/ records named in Appendix C. Free sources only, plus the AlphaSense expert calls filed in the repo. Reading log and per-source notes: insights/primer-notes/._

**What changed in v2.** 17 more AlphaSense expert calls, each read in full (list in Appendix C). Main effects: buyer calls now exist for six of the ten picks (Didero, Magentic, Amperos, Actively, Omilia, Ema) and for Skan; Decagon and Fin have buyer-side pricing; the pricing table in Q2 grows from 10 to 18 rows; new evidence that buyers keep CX vendors interchangeable; SI and Microsoft calls on token cost. The verdict is unchanged; the case for outcome pricing outside CX is weaker (see Q2).

**What changed in v3.** New Section 8: six landscape cuts of 65 startups (five worlds, buyer, pricing, channel, stage, thesis fit), one group per company per cut. Full version: insights/landscape-cuts.md.

**Start here.** This primer is for an investor who writes Series B to D checks and is new to AI agents. Read it in this order:
1. Section 1 (the big picture) tells you what an "agent" is, who sells them, who buys them and how big the money pools are.
2. Section 0 (the decision summary) gives the view and the 10 things that shaped it.
3. Section 2 answers 17 questions in order. Skip to the ones you care about.
4. Sections 3 to 6 cover the companies, the money, the data and the bear case.
5. Section 8 shows where every startup sits, cut six ways. Read it after Section 3.
6. Appendix A is a glossary. Every acronym is spelled out the first time it appears and again in the glossary.

**Contents.** 0 Decision summary; 1 Big picture; 2 The 17 questions; 3 Company profiles; 4 Unit economics; 5 Data loops and moats; 6 Bear case; 7 Open questions; 8 Landscape cuts; Appendices A Glossary, B Gaps, C Source coverage.

**How to read this doc.** Three kinds of statement are kept apart:
- A plain sentence ending in `[src-…]` is a sourced fact: a filing, a release, a dataset or a reported figure.
- **Claim (who):** marks something a company, founder, investor or expert said. It is sourced but not verified.
- `[inference]` marks my read. It is not sourced. Argue with it.

Confidence (high, med, low) is marked where a number rests on one press article, an investor's own blog, an AI-run expert interview or a vendor case study. Most facts about the picks come from funding press releases, so they are the company's claims. Where two sources disagree on something that changes demand, right to win, unit economics or the data loop, both are shown. Funding and valuation gaps between sources are not flagged.

---

## 0. Decision summary

_In one line: agents that do a whole job and get paid per result are real and selling, but the "outcome" is usually counted by the vendor, most contracts are really priced per transaction, and the winners so far are vertical apps and the big software platforms, with consulting firms doing the installing._

**Verdict [inference].** Back vertical, outcome-sold agent companies that take over work enterprises already pay outsiders to do (insurance claims, medical billing, procurement, retail operations, legal review), at Series A or B. Treat Sierra and Decagon in customer service as benchmarks, not entries: they are priced at about 45x to 100x annual recurring revenue (ARR) per comps.md arithmetic [src-20260504-c9d184] [src-20260127-5d9191] [src-20261025-07358d]. Form a view on horizontal orchestration (software that coordinates many agents across a company) but do not push it until a company shows named customers in production. This matches the current repo view: vertical apps (world 5) and systems of record (world 2) win, and systems integrators (SIs) are the deployment channel (insights/weekly/2026-W44.md).

**The five worlds, in one table.** The core question is who ends up building and owning the "harness" (the software around a model that lets it act, remember and be checked) for a big company's agents. The repo tracks five possible answers and counts each source that points to one (framework.md section 2, recounted in W44).

| World | Who owns the harness | Source lines pointing here |
|---|---|---|
| 5. Vertical apps | Each function buys a complete agent | 31 |
| 2. Systems of record | Salesforce, ServiceNow, SAP, Workday run agents on their own data | 26 |
| 4. Systems integrators | Accenture, Deloitte, Cognizant assemble it per client | 22 |
| 1. Model labs | OpenAI, Anthropic, Google, Microsoft | 18 |
| 3. The enterprise itself | Big companies build their own | 11 |

A count of source lines is not a vote of buyers. It shows where the evidence keeps landing [inference].

**The outcome-pricing test.** A vendor "passes" only if three things hold: the unit is countable, the customer agrees with the count, and the contract has renewed at least once (framework.md section 3). For each vendor the repo also asks the price per unit, who audits the count, what happens at renewal and the gross margin after paying for the model. No vendor in the repo fully passes in public data. The closest is Sierra at Safelite, where the buyer describes the unit, the price and an 80% chance of renewal, but the contract has not yet renewed [src-20260710-37d40b].

**Top 10 things that shaped the view.**

1. **"Outcome" usually means a transaction, not a result.** Bain says most outcome pricing (per resolution, per lead) is really output pricing [src-20260810-21fe8d], and only about 10% of AI-native and hybrid vendors use outcome pricing at all (Bain, as cited by fileAI) [src-20261012-e6c2b7]. In the calls, Sierra bills Innovaccer by "platform and then per minute" [src-20260717-eb6872], Crescendo's "outcome" contracts were per contact, "not per resolution" [src-20260724-865e53], Pace bills an annual platform fee plus per-claim usage at a UnitedHealth unit [src-20260811-852c57], and Amperos describes a "volume-based" subscription [src-20261025-db0c8b]. Decagon says most customers choose per conversation [src-20241210-0d932d]. The v2 calls add more of the same: Magentic at IKEA is "just consumption-based" with no share of savings [src-20260209-7ec831], Didero charges "a platform-based fee with some kind of kickers in terms of volume" [src-20260617-937cc1], and Cresta charges "Primarily ... the number of minutes" with outcome charging as an option [src-20260618-f36dc6].
2. **Where outcome pricing exists, it is real money.** Zendesk's CEO says it passed $200M of AI ARR on per-resolution billing [src-20260805-5a9fa7]. Sierra went from $100M to $150M ARR in one quarter [src-20260309-78d5a1]. Intercom's Fin, priced at $0.99 per resolution, was bought by Salesforce for about $3.6B [src-20260615-74b583] [src-20260910-2cf2eb].
3. **The vendor grades its own homework.** Zendesk uses its own large language model (LLM) to decide whether a ticket was resolved [src-20250806-3921b6]. A Sierra buyer could not see how "resolved" was defined and audited it himself [src-20260318-033caf]. No independent auditor shows up in public sources (W44).
4. **Real resolution rates sit below the headlines.** Fin resolves 30% to 40% at Smartly.io [src-20260326-b3dd2d] against a 76% average Salesforce cites [src-20260910-2cf2eb]. Sierra runs at about 60% to 65% at two buyers [src-20260318-033caf] [src-20260717-eb6872]. An AI-native outsourcer contained 30% to 40% of email [src-20260724-865e53].
5. **Outcome pricing without proven automation destroys margin.** At Crescendo, discounts of 10% to 40% met flat costs and "Gross margin did tank heavily" (former director) [src-20260724-865e53]. Crosby's founder: "We lost a lot of money on it until we were able to get the pricing right" [src-20261025-1fbd1c].
6. **The prize is labor and outsourcing budgets, not software budgets.** HFS sizes business process outsourcing (BPO) at $786B by 2035 with $422B moving to "services-as-software" [src-20260831-73c927]. Gartner puts the whole AI agents and assistants line at $29.2B in 2026 [src-20260916-b894eb].
7. **The big platforms are taking a large share.** Salesforce added 2,000 paying production customers in a quarter, and half of bookings came from customers "refilling the tank" [src-20260826-580137]. A KPMG ServiceNow partner says "nothing on the market" competes with ServiceNow's AI in IT service management (ITSM) [src-20260911-0742fb].
8. **Consultancies are the installers, and the labs are paying them.** Anthropic put $100M into SI partners [src-20260312-73c25c], Google a $750M partner fund [src-20260422-72407e], and AWS (Amazon Web Services) a $1B in-house forward-deployed engineer (FDE) team [src-20260730-e4cc74]. An Accenture managing director says OpenAI is training SIs as its "extended arm" [src-20261017-72ec30].
9. **The labs are moving up into the job itself.** OpenAI's Presence ships a complete customer service agent [src-20260722-a3993b]. A Deutsche Telekom executive calls customer service agents "commoditized" and plans to cut from five vendors to one or two [src-20260727-3b21a8]. Chime's former product chief routed tickets across Decagon, Sierra and Maven and says "I would not bet on either" [src-20260518-714b0a].
10. **Outside customer service, the picks have named customers but little disclosed revenue.** Pace at Palomar resolves over 90% of service cases with no human [src-20261025-c77b6e]. Crosby works for Cursor, Ramp, Tishman Speyer and Starwood [src-20260331-50e583]. None of the ten picks discloses gross margin after inference or a renewal at the same price.

**Evidence on the thesis claims.**

| # | Claim | For | Against | Read [inference] |
|---|---|---|---|---|
| 1 | Outcome pricing is a real business model | Zendesk $200M+ AI ARR [src-20260805-5a9fa7]; ICONIQ: outcome pricing went from 18% to 23% of AI vendors in six months [src-20260715-e16b49] | Bain: mostly output pricing [src-20260810-21fe8d]; HubSpot says outcome pricing slowed deals [src-20260812-1b0bca] | Real in customer service. Elsewhere mostly per-transaction |
| 2 | Vertical apps beat horizontal platforms | Tally 31 for world 5 (W44); Levie: vertical players win background agent work [src-20260915-68c6ef] | Salesforce, ServiceNow, Workday absorbing agents (world 2, 26 lines); Battery: durable firms look like "SaaS companies of old" [src-20260123-b88941] | Verticals win where work is outsourced and countable. Platforms win where they own the data |
| 3 | Data from running the work compounds | Sierra customers automate 70% to 90% [src-20260310-ad2c26]; Crosby tracks lawyer review minutes weekly [src-20261025-1fbd1c] | Labs ship the same improvement loop in Presence [src-20260722-a3993b]; context drifts (30% to 90% accuracy, back to 60% in two months) [src-20261020-7922f1] | Possible, not shown in any filed number |
| 4 | Outcome-priced agents earn software margins | Pace targets 80% vs BPO 10% to 15% [src-20260203-a5df90]; Ema claims "close to 80%" [src-20260930-9ee545] | Bessemer: AI margins 50% to 60% vs 80% to 90% for SaaS [src-20260210-496d37]; Crescendo margin "did tank heavily" [src-20260724-865e53] | Unproven. Underwrite to 50% to 60% |

**What this means:** the opportunity is real but narrower than the pitch. Pay for countable work taken from outsourcers, not for the word "outcome".

---

## 1. The big picture

### 1.1 What an agent is, in plain English

A chatbot answers questions. An **agent** takes actions. It reads a customer email, looks up the order in the company's software, issues a refund and closes the ticket. It is built on a large language model (LLM), the kind of AI behind ChatGPT and Claude. Around the model sits a **harness**: the code that gives the model tools (logins to other software), memory, rules about what it may do, and tests (called "evals") that check its work.

**Orchestration** means coordinating many agents, and the people who supervise them, across many software systems. Example: a new hire needs accounts in 20 to 30 systems. Ema's founder says one large company had more than 100 tools and 1,000 people involved in requests like that [src-20261025-7ef133].

An **outcome-based agent** is sold per result instead of per user ("per seat"). Intercom's Fin charges $0.99 each time it resolves a customer question [src-20260924-93c5ed]. Salesforce charges $2 per resolution for its help agent [src-20260926-ff7125]. HubSpot charges $0.50 per resolved conversation [src-20260413-63104e].

**Why sellers want this.** A human agent costs $20 to $30 per resolved ticket, per Intercom's founder [src-20250821-666ad1]. Charging per result lets the vendor price against that labor cost instead of against a software seat.

**What this means:** an agent is software that does a job, so it competes with the people and outsourcers doing that job today, not with other software.

### 1.2 How the market is built: six layers

The repo splits the market into six layers (framework.md section 1).

| Layer | What it is | Who is there | Risk the labs absorb it |
|---|---|---|---|
| 1. Model labs | The AI models plus the labs' own agent platforms | OpenAI, Anthropic, Google, Microsoft, AWS | They are the absorbers |
| 2. Harness and infrastructure | Runtime, tools, memory, evals, permissions | Lab toolkits, LangChain, monitoring vendors | High |
| 3. Orchestration | Many agents across systems, governed | Agentforce, ServiceNow, UiPath, Copilot Studio; Sycamore, Duvo, Ema, Kestra | Medium |
| 4. Work context | A record of how work really gets done | Celonis, process mining; Skan AI, Workfabric | Low to medium |
| 5. Vertical outcome | A complete agent for one function, priced per result | Sierra, Decagon, Pace, Crosby, Amperos | Medium |
| 6. Services | Consultancies and outsourcers | Accenture, Deloitte, Cognizant, Infosys, TCS | Low |

The "absorption risk" column is the repo's starting hypothesis, not a measured fact (framework.md).

**What this means:** the further a company sits from the model and the closer to a paid-for job, the safer it is from the labs [inference].

### 1.3 Six forces driving it

1. **Models got good enough to use old software.** Pace says its success rate on tests that drive legacy insurance screens went from 30% to over 95% in one model release [src-20260527-cecfde] (company claim).
2. **Labor and outsourcing are huge, slow-growing budgets.** Gartner forecasts IT services at $1,557B in 2026, growing 4.4%, against software at $1,464B, growing 15.2% [src-20261021-6d0517]. The US has 2,666,000 customer service representatives at a $44,770 median wage, about $119B a year (repo arithmetic) [src-20260827-b22de5].
3. **Seat pricing breaks when software does the work.** If an agent replaces five people, a per-seat vendor loses four seats. Zendesk's CEO: "seats are going to go away over time" [src-20260805-5a9fa7]. A KPMG partner sees ServiceNow seat counts shrink as AI is added [src-20260911-0742fb].
4. **Agent budgets are growing much faster than IT budgets.** Gartner: agentic AI funding up 31.8% against IT budgets up 3.7% for 2027 [src-20260831-2bda07].
5. **Deployment is the bottleneck.** Box's CEO Aaron Levie: "we're just going to be in for years and years of deployment and change management and adoption" [src-20260629-015aae]. Job postings for forward-deployed engineers (FDEs: vendor engineers who sit with the customer and build the deployment) passed 7,300 in nine months of 2026 against under 200 in 2023 (Lightcast) [src-20261022-d5ad54].
6. **The labs and clouds are pushing hard.** OpenAI gives its production harness away to developers [src-20260910-014b24]. Anthropic prices a managed harness at $0.08 per session-hour on top of model usage [src-20260408-e5d37b].

**What this means:** the money is there and growing, but getting agents into production is slow, people-heavy work.

### 1.4 Who buys, and how

- **Customer experience (CX) leaders** buy support agents. At Deutsche Telekom the core metric is net promoter score (NPS) and customer satisfaction (CSAT), not cost [src-20260727-3b21a8].
- **Operations heads** buy back-office agents that replace outsourcers: insurance carriers [src-20260527-cecfde], medical billing groups [src-20260422-d6ae9d], procurement teams [src-20260917-25441c].
- **Chief information officers (CIOs)** buy platforms and governance. Only 13% of 2,002 CIOs report significant value from AI [src-20261019-a120c4]. About 17% of enterprises have agents in production (Gartner via Technology Org) [src-20261012-11ce4a].
- **How a deal runs.** A paid pilot, then a contract. Innovaccer ran a 3-month pilot with Sierra; work split 70/30 between its own team and Sierra's engineers at first, moving to 90/10 [src-20260717-eb6872] (AI-run interview; med). Ema's founder says big deals take about nine months and many are "large seven figure deals per year, multi-year" [src-20261025-7ef133].
- **What they compare against.** The human or outsourcer cost. Safelite pays Sierra under $2 per claim-intake transaction against $7.50 to $9 for a human [src-20260710-37d40b].

**What this means:** the buyer is usually an operations or CX leader with a labor budget, and the deal hinges on a pilot that proves the count.

### 1.5 Policy and liability

There is little agent-specific regulation in the sources. Two points matter:
- **Data residency.** A Deutsche Telekom executive says OpenAI and Anthropic are "no-goes" for some work because of European Union data rules [src-20260727-3b21a8].
- **Liability is unassigned.** A German court (OLG Hamm, 12 May 2026) held a clinic liable for its chatbot's invented credentials, rejecting an "independent AI" defense [src-20260916-6e03e5]. An agent deleted a company's production database and backups in 9 seconds using an over-broad access token [src-20260428-8baab9]. Crosby avoids the gap by being a registered law firm whose lawyers take liability [src-20260331-50e583].

**What this means:** whoever carries liability for the agent's work will capture more of the price [inference].

### 1.6 How big is it?

Different publishers define pools differently. Do not add the rows (market-sizing.md).

| Pool | Size | Publisher | Source |
|---|---|---|---|
| BPO, conventional path | $786B by 2035 | HFS (analyst) | [src-20260831-73c927] |
| BPO moving to services-as-software | $422B by 2035 | HFS | [src-20260831-73c927] |
| Contact center and BPO spend, before LLMs | about $400B a year | Bret Taylor, Sierra CEO | [src-20260309-78d5a1] |
| IT services spending | $1,557B (2026) | Gartner | [src-20261021-6d0517] |
| AI agents and assistants spending | $16.5B (2025), $29.2B (2026), $65.5B (2027) | Gartner | [src-20260916-b894eb] |
| US agent software for coordination work | $100B TAM, $4B to $6B captured | Bain | [src-20260507-2c054a] |
| Software spend exposed to agents | $234B by 2030 | Gartner via PYMNTS (secondary) | [src-20261016-9f1777] |

TAM means total addressable market: the most that could be spent if everyone bought.

Disclosed incumbent agent revenue gives a reality check: Salesforce Agentforce ARR $1.5B+ (the definition widened to include Slackbot) [src-20260826-0b53e8], Workday AI products nearly $600M [src-20260827-79de17], Genesys AI $400M+ [src-20260902-b6edda], NiCE AI $362M [src-20260805-3deb2c]. These sum to about $2.9B, in line with Bain's $4B to $6B captured (market-sizing.md).

**What this means:** the labor pools are 20x to 50x the agent software line, so the upside is big, but today's captured revenue is a few billion dollars.

### 1.7 How venture investors see it

| Company | Last round | Valuation | Revenue signal | Source |
|---|---|---|---|---|
| Sierra | $950M (May 2026) | >$15B | $150M ARR (Feb 2026); >$200M later per Newcomer | [src-20260504-c9d184] [src-20261025-07358d] |
| Decagon | $250M Series D (Jan 2026) | $4.5B | >$100M ARR | [src-20260127-5d9191] [src-20261013-d7909a] |
| Pace | $46M Series B | $375M | not disclosed | [src-20260527-cecfde] |
| Actively | $45M Series B | $250M | not disclosed | [src-20260428-2d177a] |
| Sycamore | $65M seed | not filed | no customers named | [src-20260330-2b99a8] |
| Fin (exit) | bought by Salesforce | about $3.6B | ARR past $100M (Aug 2025) | [src-20260615-74b583] [src-20250821-666ad1] |

- Implied multiples (repo arithmetic, rough): Sierra about 75x to 100x ARR, Decagon about 45x, Fin under 36x on stale ARR (comps.md).
- Exits so far go to incumbents: Salesforce (Fin), NiCE (Cognigy), Genesys (Pinkfish), SAP (TechWolf), Workday (C1.ai) [src-20260805-3deb2c] [src-20260902-b6edda] [src-20261001-056aad] [src-20261013-7962db]. Decagon hired a bank to explore a sale [src-20261013-6d4b75].
- Investor maps tilt to vertical apps: 13 of 17 tallied, with Battery Ventures the main dissent (W44) [src-20260123-b88941].

**What this means:** customer service leaders are priced for perfection, and the only priced exit cleared at about a third of the private multiples. Earlier vertical names outside CX are where entry prices still make sense [inference].

---

## 2. The 17 questions

These are the questions in framework.md and evidence-by-question.md. Each has a short answer, the evidence and a one-line "What this means". Confidence is mine.

### Q1. Are agents in production, or still pilots?

**Answer: some production, mostly in customer service and inside big platforms. Confidence: med.**
- About 17% of enterprises have agents in production (Gartner CIO survey via Technology Org) [src-20261012-11ce4a]. Only 13% of 2,002 CIOs report significant value from AI [src-20261019-a120c4].
- Survey answers depend on the definition: 2% "fully scaled" (Capgemini) [src-20250716-cb70b8], 49% "piloting or deploying" (Accenture) [src-20260726-c50d29], 57% "in production" among LangChain builders [src-20251202-cd7dc4].
- Salesforce added 2,000 paying production customers in a quarter, up 70% quarter on quarter [src-20260826-580137]. An OSF Digital executive (a Salesforce partner, so biased) says about 20% of his clients are "really serious" about Agentforce, with 20% to 30% more coming within six months [src-20260804-3aa89c].
- Live examples from buyers: Safelite runs Sierra on claim intake across five regions after a 90-day pilot [src-20260710-37d40b]. Walmart has used Sierra for customer care for about a year [src-20261006-b21c7a]. Rohlik runs "hundreds" of Duvo agents in production [src-20260609-4b024f] (related party, see Q15).
- A Cognizant practice head: "three to five years before we have really penetrated most of the big enterprises" [src-20250627-297f7b].

- v2 buyer calls: IKEA runs Magentic on 45%-50% of global procurement volume, live since August 2025 [src-20260209-7ec831]. DOCS Dermatology runs about 30%-35% of all claims through Amperos [src-20251016-371c9b]. Notion's Decagon deployment automates above 60% of chat, aiming for 70%-75% [src-20260515-de88a1]. Hitachi has four Ema use cases live with 40%-60% shorter cycle times [src-20260224-8c72f4]. Cresta's voice agents take thousands of calls a day [src-20260618-f36dc6].
- Against: Discover set a 70%-75% containment target for Omilia and says "We are not there yet" [src-20241114-f0ab80]. A Cognizant practice head says pilot purgatory has ended but full penetration of BPO work takes "five, seven years easily" [src-20260724-b4a442].

**What this means:** production is real but early. Most buyers are one or two use cases in.

### Q2. Is outcome pricing real or rhetoric?

**Answer: real in customer service at a handful of vendors. Elsewhere it is mostly per-transaction pricing called "outcome". Confidence: med-high.**

How the main contracts actually bill:

| Vendor | What the customer pays for | Who counts it | Source |
|---|---|---|---|
| Intercom Fin | $0.99 per outcome (resolution, handoff or disqualification), $9.99 per sales qualification, minimum commitments | Vendor; customer confirms or leaves without asking for more help | [src-20260924-93c5ed] |
| Zendesk | Per automated resolution, from an allowance; $1.50 headline | Vendor's own LLM | [src-20250806-3921b6] [src-20251023-28432e] |
| Salesforce help agent | $2 per resolution; other agents use Flex Credits ($0.10 per action) | Vendor | [src-20260926-ff7125] [src-20261013-7d8358] |
| HubSpot | $0.50 per resolved conversation, paid in credits | Vendor | [src-20260413-63104e] |
| Sierra at Safelite | Under $2 per claim-intake verification, $4 to $5 with more steps; outcome defined per workflow | Agreed in contract; 4-year term | [src-20260710-37d40b] |
| Sierra at Innovaccer | Platform fee plus per minute | n/a | [src-20260717-eb6872] |
| Decagon | Per conversation (most customers) or per resolution | Vendor | [src-20241210-0d932d] |
| Crescendo | Per contact, "not per resolution", flat monthly rate plus overage | Vendor | [src-20260724-865e53] |
| Pace | Platform or implementation fee plus per-claim volume | n/a | [src-20260811-852c57] [src-20260508-386718] |
| Duvo | Per run or per executed workflow | n/a | [src-20260609-4b024f] [src-20260701-3b0c17] |
| Fin (former Intercom sales lead) | $0.99 per resolution: customer does not return within 24 hours or marks it resolved | Vendor | [src-20260310-e66bf3] |
| Fin (Notion buyer) | Per deflection, negotiable to "less than $2" | Vendor | [src-20260515-de88a1] |
| Decagon at Notion | Per meaningful conversation; same price for headless | Vendor | [src-20260515-de88a1] |
| Cresta | Per minute, with outcome options (tickets resolved, cards collected) | n/a | [src-20260618-f36dc6] |
| Magentic at IKEA | Consumption-based enterprise license, no share of savings | n/a | [src-20260209-7ec831] |
| Didero | Platform fee plus volume kickers (procurement BPO view); about $30,000-$60,000 a year at one small buyer | n/a | [src-20260617-937cc1] [src-20251024-112e5e] |
| Amperos at DOCS Dermatology | Proportional to claim volume, minimum-transaction contracts | n/a | [src-20251016-371c9b] |
| Ema at Hitachi | Subscription priced on workflows | n/a | [src-20260224-8c72f4] |
| Omilia at Discover | Annual license, $500,000 to $1M | n/a | [src-20241114-f0ab80] |

- **Adoption is rising from a low base.** ICONIQ: outcome pricing went from 18% to 23% of AI vendors in six months [src-20260715-e16b49]. Bain: most outcome pricing is output pricing [src-20260810-21fe8d].
- **Buyers often prefer predictability.** A buyer at a European fintech wanted "a more transactional pricing without outcome commitment" [src-20260708-a5fc76]. In an a16z survey, 27 of 50 buyers preferred work-based credits against 14 for tokens [src-20260827-fb556f]. HubSpot says outcome pricing and trials lengthened sales cycles [src-20260812-1b0bca].
- **Per-resolution pricing is hard to budget.** A former Intercom sales lead: "there's not a lot of cost control that can be deployed", so buyers put Fin on a subset of conversations [src-20260310-e66bf3]. A Cognizant practice head: consumption pricing "introduces a lot of variability, which CFOs and budget holders don't like" [src-20260724-b4a442].
- **Sellers' own doubts.** Sierra's CEO calls cost-savings pricing "a temporary drug" once agents are compared to other agents, not to labor [src-20250514-093b59].

**Conflict to note (unit economics).** Sierra is the outcome-pricing benchmark, yet one buyer pays per minute [src-20260717-eb6872] while another pays per verified transaction [src-20260710-37d40b]. Sierra's real pricing varies by account.

**Conflict to note (unit economics).** Magentic pitches 1% to 2% spend savings [src-20260923-47e348], but its IKEA contract has no value share [src-20260209-7ec831].

**What this means:** ask every company for the contract, not the slide. Count how much revenue is truly per result. In v2, none of the eight new contracts outside Fin is priced per result.

### Q3. What blocks production?

**Answer: data, integration, security reviews and trust, more than model quality. Confidence: med.**
- A Cognizant practice head lists proof-of-concept (POC) fatigue, no roadmap, legal review "a couple of months" and API (application programming interface) integration "two, three months" [src-20250627-297f7b].
- Infosys builds inside the client's firewall partly to skip security approvals that can take "up to six months" [src-20251006-b80311].
- Crescendo promised deployment in 6 months and took a year; clients would not hand over API keys [src-20260724-865e53].
- Smartly.io's Fin rollout was delayed "mainly from the vendor side, from the capability side", and accuracy depended on the knowledge base [src-20260326-b3dd2d].
- Incidents: an agent deleted a production database in 9 seconds [src-20260428-8baab9].
- Liability keeps the last step human. DOCS Dermatology will not let Amperos submit claims: "If any of the wrong claims go in, who takes a liability?" [src-20251016-371c9b]. A procurement BPO CEO: "I don't have any client that lets it go on its own" (Pactum negotiation) [src-20260617-937cc1]. Didero at Novilla: "It doesn't send any emails without me pressing send" [src-20251024-112e5e].
- Testing is the hidden cost. Cresta: "if we spent one month to build the AI agent, we might spend two or three or even four months on the test eval" [src-20260618-f36dc6]. Discover's Omilia setup took 6-12 months [src-20241114-f0ab80].

**What this means:** vendors that bring their own engineers and carry the integration work get through. That costs money (section 4).

### Q4. Whose budget pays?

**Answer: increasingly the labor or outsourcing budget, through the business unit. Confidence: med.**
- A Duvo co-founder sells from the department's "service budget line, because it is easier to procure, usually higher budgets than on softwares" [src-20260701-3b0c17].
- Safelite set the price by measuring a 35% to 40% cost cut and giving Sierra "10% of that" [src-20260710-37d40b].
- Salesforce says outcome deals are funded by savings or by qualified leads and booked orders [src-20260909-c1900d].
- Indian IT majors show the swap: Infosys AI revenue is 10.5% of total [src-20261023-db47fe] and TCS annualized AI revenue is $3.1B [src-20261008-ae3125], while their total growth is low single digit (market-sizing.md).

- v2 calls confirm the swap. Notion: the "offshore model cost us 4X to 7X more expensive than what Decagon costs us", and "Our external vendors have gone down maybe 75% over the last two years" while internal support stayed flat [src-20260515-de88a1]. Novilla replaced a consultant who "charged us about $7,000-$12,000 a month" with Didero at "about $30,000-$60,000 a year" [src-20251024-112e5e]. Cognizant: "Cognizant has 100,000 people doing BPO work. Just with us, it's potentially up to 70,000 people that can be automated away" [src-20260724-b4a442].
- Microsoft takes software budget first: Ascot moved to E7 at a 14.6% discount to E5 list, then spent the saving on Copilot Cowork, "Actually more" [src-20260904-8886b4].

**What this means:** the buyer compares against the outsourcer's invoice. That is a much bigger pool than software, but it is also a price ceiling.

### Q5. Who builds the harness?

**Answer: split. Vertical vendors build their own; SIs assemble the rest on lab and platform pieces. Confidence: med.**
- Sierra's FDE lead: "how do you actually guarantee the outcome? And that really is forward-deployed engineering" [src-20260728-aba703].
- The labs fund SIs: Anthropic $100M [src-20260312-73c25c], Google $750M [src-20260422-72407e]. An Accenture managing director says OpenAI trains SIs as FDEs, its "extended arm" [src-20261017-72ec30].
- Some enterprises build: Ramp built its Laminar harness in six weeks [src-20261022-ae18f2]; Capital One built a multi-agent platform on open-source models [src-20260416-e6896d]; Airbnb plans its own agent for 2027 [src-20261009-44e09b] (low-med).
- v2: Chime built its own router across Decagon, Sierra and Maven and keeps data, procedures and tools in its own systems so any vendor can plug in [src-20260518-714b0a]. Hitachi chose Ema over an estimated 12-14 month in-house build, then built later agents itself: "Today, for other use cases, we don't depend on Ema" [src-20260224-8c72f4]. Cresta built its own framework rather than LangChain [src-20260618-f36dc6]. Notion: "the build was a lot more expensive" than Decagon [src-20260515-de88a1].
- FDE economics: at Palantir, FDE time was "valued at low seven figures per year per forward-deployed engineer, prorated" inside usage contracts of "a few million dollars a year" [src-20260908-547a69]. The same former FDE says ex-Palantir firms resell FDE work as services [src-20260908-547a69].
- Counter-signal: Gartner predicts 70% of enterprises will abandon agent systems built by vendor FDE teams by 2028 [src-20261012-11ce4a].

**What this means:** the harness itself is not the moat. Whoever owns the deployment relationship and the result is.

### Q6. What did the labs ship, and what did it absorb?

**Answer: a lot, in 6 to 9 months. Generic harness and support agents are now lab features. Confidence: high on what shipped, med on impact.**
- OpenAI Presence: a complete CX agent harness with procedures, guardrails, simulations and graders [src-20260722-a3993b].
- OpenAI Agents API: production harness with no extra fee [src-20260910-014b24]. Anthropic Managed Agents at $0.08 per session-hour [src-20260408-e5d37b].
- Marketplaces: Sierra and Decagon are launch partners in the OpenAI Marketplace, so buyers can spend lab commitments on them [src-20260929-2fdd0f].
- AWS: $1B in-house FDE team [src-20260730-e4cc74].
- Buyers' view: Accenture says "models are such commodities" and model routing is "hardly ever" used in practice [src-20261017-72ec30]. Deutsche Telekom rules out US labs for some EU data [src-20260727-3b21a8].

- v2: a Skan.AI director: "Biggest competition is Anthropic and OpenAI" and "Once Claude figures out how to do this themselves, they don't need us" [src-20260616-48f4c6]. Ascot dropped Claude for Cowork and consolidated on Microsoft over data leakage; Agent 365 "still throws up errors all the time" [src-20260904-8886b4]. A former Palantir FDE: "DeployCo is the forward-deployed arm" of OpenAI [src-20260908-547a69].

**What this means:** a startup selling the agent loop alone is in the labs' path. Selling the finished job, with domain rules and liability, is safer [inference].

### Q7. Orchestration, context, vertical or services: where does value sit?

**Answer: vertical outcome first, then systems of record. Work context is promising but unproven. Horizontal orchestration is being squeezed. Confidence: med.**
- Orchestration is squeezed between clouds and systems of record that ship their own agents [src-20260422-1f1ec3]. Microsoft and ServiceNow both pitch the governance "control tower" over everyone's agents [src-20260501-fc687c] [src-20260507-e6c2cd].
- Context matters: one analytics agent rose from about 30% to about 90% accuracy with business context, then fell to 60% in two months as the context drifted [src-20261020-7922f1]. SAP is buying TechWolf's work-context graph [src-20261001-056aad].
- A Wawa CIO wants AI to first build "a map" of system interactions, then overlay business context [src-20260402-8d84cb].
- IKEA sees Magentic as "the system of execution and the system of intelligence that sits on top of the systems of record" [src-20260209-7ec831]. A procurement BPO CEO calls document ingestion "pretty commoditized" and puts workflow depth ahead of the AI layer: "AI is the fourth leg of that table" [src-20260617-937cc1]. Chime: integration is not a differentiator between CX vendors [src-20260518-714b0a].
- Battery Ventures dissents: "Durable companies will look more like SaaS companies of old with AI superpowers than collections of loosely orchestrated agents" [src-20260123-b88941].

**What this means:** buy the layer that owns a paid-for result or proprietary context, not the plumbing between agents.

### Q8. What about systems of record?

**Answer: they are strong where they own the data, weaker where they only add AI to a seat. Confidence: med.**
- Salesforce: Agentforce ARR $1.5B+ with a widened definition [src-20260826-0b53e8]; premium AI products are about 5% of the base at 60% to 80% price uplift [src-20260909-c1900d]; bought Fin [src-20260910-2cf2eb].
- ServiceNow: AI annual contract value over $1B in Q2 2026 [src-20260722-d4586c]. A KPMG partner says "nothing on the market" competes in ITSM and big clients are never lost because "The risks are just too great" [src-20260911-0742fb]. The same partner reports seat contraction, "debooks" and price-led growth [src-20260911-0742fb].
- A Wawa CIO says Now Assist does not "really do a job" and asks "Do I even need to have a ServiceNow platform?" [src-20260402-8d84cb].
- Zendesk and Intercom beat an AI-native outsourcer because they hold the data, and clients would not give the startup API keys [src-20260724-865e53].
- Zendesk's own AI is losing the frontline at the clients one BPO director sees: "this number is not a precise number, but I would say 70%" use custom or third-party AI instead (AI-run interview, low-med) [src-20260828-bb2734]. An Accenture VP says ServiceNow and Salesforce customization limits push work to UiPath [src-20260825-747be0].
- Exposure: personal agents could skip a retailer's support agent by calling its APIs directly, which Walmart calls "permissioning, not engineering work" [src-20261006-b21c7a].

**Conflict to note (right to win).** KPMG says ServiceNow is unbeatable in ITSM [src-20260911-0742fb]; Wawa's CIO is testing alternatives and questions the platform [src-20260402-8d84cb]. One is a partner, the other a buyer with no deployment yet.

**What this means:** systems of record are the default buyer choice and the main acquirer. A startup must win where the record holder is weak, or sell to it [inference].

### Q9. Which horizontal players are investable?

**Answer: few with proof. Confidence: med.**
- Ema: $77M Series B, 50+ active enterprise deals, bookings over $150M, prices by completed tasks and outcomes [src-20260930-9ee545] (company claims).
- Kestra: $25M Series A; enterprise revenue 25x since seed; 2B+ workflows in 2025 [src-20260331-83a5c4] (company claims). It is workflow orchestration more than an agent company [inference].
- Skan AI: $63M Series C; revenue up over 300% year on year; net dollar retention about 150% [src-20260812-4cb1fc] (company claims).
- Sycamore: $65M seed, no named customers [src-20260330-8d6266]. Workfabric: no customers or funding disclosed on its site [src-20261023-21a6d6].

- v2 buyer calls: Hitachi spends "a few hundred thousand" a year on Ema but expects growth of only 5%-10% because it now builds its own agents [src-20260224-8c72f4]. Justworks got about $1M of revenue from Actively on around $160,000 of spend, but switching "would be pretty easy" [src-20251126-6d86c8].

**What this means:** horizontal names with real customers exist (Ema, Kestra, Skan), but their numbers are press-release numbers, and the one Ema buyer call shows an expansion cap. Diligence first.

### Q10. Which vertical players are investable?

**Answer: the picks in section 3 outside customer service. Confidence: med.** Pace (insurance), Amperos (medical billing), Crosby (legal), Didero and Magentic (procurement), Actively (sales), Omilia (voice CX). Others in the repo: Lassie in dental back office, $10M+ annualized revenue and 700+ practices [src-20260603-ce0e80]; Basis in accounting, $100M Series B [src-20260224-b6a4eb].

In CX, Notion's RFP scored Decagon and Sierra "at 94% or 90%-94%" on chat, Ada and Fin 80%-90% [src-20260515-de88a1]. Asked to split $100, a procurement BPO CEO "would put $40 on Didero ... $30 on Magentic ... $20 on Pavus, and ... the balance on Pactum" [src-20260617-937cc1].

**What this means:** vertical names at Series A or B are where price and proof still line up.

### Q11. What are the unit economics?

**Answer: below software today, with a path up if automation rises. Confidence: med.** See section 4.
- v2: an Accenture VP prices a task at "$200 or $300 per month" on RPA and "$1,000 or $1,200 per month or even more" with AI [src-20260825-747be0]. Cognizant: "quite a lot of the labor cost will switch to token cost" [src-20260724-b4a442]. Ascot's Cowork tokens went "from 800,000 tokens to 3.3 million" in the first month [src-20260904-8886b4]. Cresta does not resell tokens, so cheaper models are its margin [src-20260618-f36dc6].

**What this means:** underwrite to 50% to 60% gross margin unless a company proves more.

### Q12. What are the exit paths?

**Answer: strategic sale to a system of record or contact-center platform. Confidence: med-high.**
- Fin to Salesforce for about $3.6B [src-20260615-74b583]. NiCE bought Cognigy [src-20260805-3deb2c]. Genesys bought Pinkfish [src-20260902-b6edda]. SAP is buying TechWolf [src-20261001-056aad]. Workday is buying C1.ai [src-20261013-7962db].
- Decagon hired a bank; ServiceNow was reported in early talks and says it is not interested [src-20261013-6d4b75] [src-20261013-d7909a].
- Buyers expect consolidation: Justworks thinks "many of the AI tools will come and go" [src-20251126-6d86c8]; Discover expects incumbents to buy standalone contact center AI [src-20241114-f0ab80].
- Sierra bought Takeoff, a three-person outcome-paid company [src-20260723-bd3453].

**What this means:** buyers exist, but they pay well below private CX multiples.

### Q13. What do Fortune 500 heads of AI and automation say?

**Answer from calls: they want results, distrust vendor counts, and plan to consolidate. Confidence: med.**
- Deutsche Telekom runs ElevenLabs, Sierra, Decagon and Wonderful, is dropping HappyRobot, and will consolidate to one or two vendors in about 1.5 years [src-20260727-3b21a8].
- Walmart: personal agents may mean "fewer calls" to support [src-20261006-b21c7a].
- Wawa's CIO: "outcome-based agents is going to be very important because they are directly aligned to what we're always trying to achieve" [src-20260402-8d84cb].
- Safelite: "they're cheap because they're outcome-based" [src-20260710-37d40b].
- Chime (former CPO): "our main goal was not to save costs"; "We were not cost optimizing, we were visibility optimizing"; "Paying under $25 a case, which is much more than you would pay any human, might make sense in certain situations" [src-20260518-714b0a].
- Notion: switching CX vendors takes about a month without deep integrations, and "The second year with Decagon was rough" [src-20260515-de88a1].
- IKEA on Magentic: "there is not specific stickiness" yet [src-20260209-7ec831]. Ascot on Microsoft: token-based Copilot pricing would "absolutely destroy us" [src-20260904-8886b4].

**What this means:** buyers like the idea and will pay, but will cut vendors fast once the category commoditizes.

### Q14. What do SI practice leads say?

**Answer: agents cut their revenue but can lift their margins. Confidence: med.**
- Cognizant: the agent platform costs under $10,000 per full-time-equivalent (FTE) a year against Cognizant revenue above $20,000 per outsourced FTE; about 50% of savings go back to the client; "Our revenues go down, but our margins go up" [src-20250627-297f7b].
- Infosys: headcount from about 400,000 to about 340,000 through attrition replaced by automation; the goal is to "move from a revenue-based company to a margin-based company" [src-20251006-b80311]. "We don't sell AI products" [src-20251006-b80311].
- OSF Digital: Agentforce work growing over 20% against single digits for core; SIs shifting from time-and-materials to fixed scope or outcome [src-20260804-3aa89c].
- Accenture: OpenAI is training SIs as FDEs; 90% of workloads run on frontier models [src-20261017-72ec30].

- Cognizant Northern Europe: 60%-70% of BPO work automatable over five to seven years; token cost "not yet a pressing problem for the enterprise clients I see" [src-20260724-b4a442].
- Accenture VP on UiPath: RPA automated "At the max, 30%-40%"; bots outnumber agents "90% to 10%, or even 95% to 5%" [src-20260825-747be0].
- Former Palantir FDE: Deloitte and Accenture rate about 80% of Palantir; Indian SIs' coding edge "has mainly eroded because of agentic coding tools" [src-20260908-547a69].

**What this means:** SIs are allies for vendors that make them faster and partners in the sale. Ema already sells through PwC and KPMG [src-20261025-7ef133].

### Q15. What do Sycamore, Duvo and Workfabric customers and formers say?

**Answer: only Duvo has customer evidence, and it comes from a related party. Confidence: low-med.**
- Rohlik, which shares a founder with Duvo, pays per run, "high six-digit or low seven-digit" a year, saves "Thirty, 40 FTEs ... but that's maybe double these costs", rates it 7 out of 10 and stopped using UiPath [src-20260609-4b024f].
- A Duvo co-founder: target contracts over $75,000 a year at companies over $1B revenue [src-20260416-1a8cca]; aim for "10%" of measured savings [src-20260701-3b0c17].
- The "Workfabric" Sierra buyer is ambiguous: the call is filed as Workfabric but describes healthcare work, likely at his former employer [src-20260318-033caf].
- No Sycamore customer or former has been interviewed.

**What this means:** the orchestration names are still untested by independent customers. That is the first diligence gap to close.

### Q16. Should SPC push further?

**Answer: push narrowly. Confidence: med.** The bull-bear.md net is: push on vertical, outcome-sold companies in outsourced, countable work outside CX, at Series A or B; publish a view on horizontal orchestration and the CX leaders. Six kill criteria are in section 6.

**What this means:** keep sourcing verticals; do not chase the CX leaders' prices.

### Q17. What is SPC's operator edge?

**Answer: enterprise go-to-market and deployment help, which is the bottleneck. Confidence: low (no SPC-specific evidence in the sources).** Deployment needs FDEs and change management for years [src-20260629-015aae] [src-20260728-aba703]. Buyers pick vendors top-down through executive champions [src-20260318-033caf] and via SI and consulting partners [src-20261025-7ef133]. An investor who can open F500 operations and SI doors addresses the real constraint [inference].

**What this means:** SPC's value add is distribution and deployment, so favor companies whose growth is gated by enterprise access, not by product.

---

## 3. Company profiles

**How to read this.** Each profile gives What it does, Money, Buyers, Claims, Bear and What this means. Almost every number on the picks comes from a funding press release, a founder interview, an investor blog or a vendor case study. Treat them as the company's claims unless a buyer call confirms them. Order: the ten picks, then the benchmarks, then incumbents.

### 3.1 Pace (insurance operations; vertical outcome)
- **What it does:** AI agents that do the back-office work insurance carriers outsource to business process outsourcers: email triage, claim setup, policy servicing. Its CEO says it focuses "exclusively on insurance carriers" [src-20260203-a5df90].
- **Money:** $46M Series B at $375M, led by Thrive with Sequoia; 28 people [src-20260527-cecfde].
- **Buyers:** Prudential, WTW, Convex, Palomar [src-20260527-cecfde]. Prudential's individual life insurance unit moved from pilot to a multi-year production deal [src-20261025-58fd6b].
- **Claims (Pace and customers):** up to 90% of policy servicing cases handled autonomously; success on legacy-screen tests went from 30% to over 95% in one model release [src-20260527-cecfde]. **Claim (Palomar COO, vendor case study):** over 90% of service cases resolved without a human; first agents live in 90 days; Palomar's operations team now edits the agents' operating procedures itself [src-20261025-c77b6e]. **Claim (CEO):** BPOs run at "10, 15 percent gross margin"; the goal is "an 80 percent gross margin business" [src-20260203-a5df90].
- **Buyer calls:** A former RYZE operations head (a claims firm, introduced by its private equity owner) says Pace charged an implementation fee then "a volume cost", ROI was not yet measured, and "Maybe it's not as sticky right now" [src-20260508-386718]. A UnitedHealth product leader (AI-run interview, low-med) describes an annual platform fee plus per-claim usage and big time savings [src-20260811-852c57].
- **Bear:** priced on volume, not outcomes, at both customer calls. Margin target is a goal, not a result. Small team relative to valuation [inference].
- **What this means:** the cleanest "replace the outsourcer" story in the set, but prove the margin and renewals before paying up.

### 3.2 Amperos Health (medical billing; vertical outcome)
- **What it does:** AI agents that work denied insurance claims end to end for healthcare providers, including phone calls to payers [src-20260422-d6ae9d].
- **Money:** $16M Series A led by Bessemer, with Uncork and Neo [src-20260422-d6ae9d]. Earlier $4.2M seed [src-20261025-db0c8b].
- **Buyers:** provider groups across 3,000 clinical locations in 50 states, unnamed [src-20260422-d6ae9d].
- **Claims (Amperos):** works claims worth "nearly $1 billion per year" [src-20260422-d6ae9d]. At seed: 75,000+ calls, $120M collected, over 90% accuracy, 80% lower cost, 3x to 5x productivity, customers earn $5 to $10 per $1 spent [src-20261025-db0c8b].
- **Pricing:** "subscription pricing model is volume-based" [src-20261025-db0c8b]. Not outcome-priced on the record.
- **Buyer call (v2):** DOCS Dermatology: pilot "increased our productivity by 3X"; about 30%-35% of claims; spend low six figures; contracts carry transaction minimums; humans still submit because of liability [src-20251016-371c9b].
- **Bear:** one buyer call, no named customers in public sources. Payer rules and health record write-back are where defensibility sits in healthcare admin [src-20260111-f1affc], and that is untested here.
- **What this means:** a measurable result (dollars recovered) that could be priced per outcome later. Needs customer calls.

### 3.3 Crosby (legal; AI-native law firm)
- **What it does:** a registered law firm that reviews and negotiates contracts with AI and lawyers, and takes liability for the work [src-20260331-50e583].
- **Money:** $60M Series B led by Lux [src-20260331-50e583] (investor blog, biased).
- **Buyers:** Cursor, Ramp, Tishman Speyer, Starwood; 0 to 100+ customers in a year [src-20260331-50e583]. Clay: about 1,000 requests, under 2 hours median turnaround [src-20261025-474366] (vendor case study).
- **Claims (Crosby):** 2,000+ contracts for Cursor with review time down 50% [src-20260331-50e583]. The founder bills "by deal ... let's charge once" and tracks lawyer review minutes every week [src-20261025-1fbd1c]. "We lost a lot of money on it until we were able to get the pricing right" [src-20261025-1fbd1c].
- **Bear:** the work is judgment-heavy, so human lawyer time may not fall fast. Legal drafting and redlining are now lab features [src-20260512-5c6e2d]. Investor-written source.
- **What this means:** the truest outcome pricing in the set (per deal, with liability). Ask for review minutes per contract over time.

### 3.4 Didero (procurement; vertical outcome)
- **What it does:** an agent layer on top of the enterprise resource planning (ERP) system that handles supplier communication and purchase orders for manufacturers and distributors [src-20260213-3c647d].
- **Money:** $30M Series A co-led by Chemistry and Headline, with M12 [src-20260212-5fd1e0].
- **Buyers:** 30+ customers, unnamed; founded December 2023 [src-20260212-5fd1e0].
- **Buyer calls (v2):** Novilla Pharmaceuticals replaced a $7,000-$12,000 a month consultant, pays about $30,000-$60,000 a year, went live in about three days and "would 100% renew" [src-20251024-112e5e]. A procurement BPO CEO describes a CPO buyer, 6-7 week deployments and a platform fee with volume kickers [src-20260617-937cc1]. IKEA picked Magentic over Didero [src-20260209-7ec831].
- **Bear:** buyer evidence is one small company and one BPO view; no named enterprise customer. Oracle and SAP are embedding agents in ERP [src-20261003-10d57c] [src-20261021-551046].
- **What this means:** a good category; the evidence now includes a happy small buyer and platform, not outcome, pricing.

### 3.5 Magentic (procurement and supply chain; vertical outcome)
- **What it does:** procurement agents for large manufacturers.
- **Money:** $18M Series A led by Felicis with Sequoia and Westly; $23.5M total [src-20260917-25441c].
- **Buyers:** one manufacturer runs over 1M purchase orders a year through it; $4M of savings found at another [src-20260917-25441c]. Siemens and Coca-Cola Europacific Partners (CCEP) are named on a podcast page [src-20260923-47e348].
- **Claims (Magentic):** 1% to 2% spend savings worth $100M to $200M against $50M from labor; agents start as "interns" [src-20260923-47e348].
- **Bear:** the article itself says it is unclear whether the wider Global 500 will adopt [src-20260917-25441c].
- **Buyer call (v2):** IKEA: live since August 2025, 45%-50% of procurement volume, pays "low-to-mid six figure range" on "an enterprise license based on the consumption"; asked about value-based pricing: "No, it's just consumption-based" [src-20260209-7ec831]. Little lock-in so far [src-20260209-7ec831].
- **What this means:** a savings story sold on consumption. The savings-share pitch is not in the one buyer contract we have.

### 3.6 Actively AI (sales; vertical outcome)
- **What it does:** one AI agent per sales account that researches and prioritizes, positioned as a Salesforce replacement over time [src-20260428-2d177a].
- **Money:** $45M Series B at $250M, co-led by TCV and First Harmonic; $67.5M total [src-20260428-2d177a].
- **Buyers:** Ramp, Verkada [src-20260428-2d177a].
- **Claims (customers via Forbes):** Ramp attributes "tens of millions" of new revenue and about 23% higher close rates on AI-driven deals; Verkada doubled productivity [src-20260428-2d177a].
- **Buyer call (v2):** Justworks: about $1M of revenue from closed-lost re-engagement, around $160,000 of spend, but switching would be easy and Clay or Gong could ship the feature [src-20251126-6d86c8].
- **Bear:** pricing model still not disclosed. Salesforce prices sales agents on qualified leads or booked orders [src-20260909-c1900d], directly in its path.
- **What this means:** revenue-side agents are easier to sell on value, but attribution is hard to audit.

### 3.7 Omilia (voice customer service; vertical)
- **What it does:** voice AI for contact centers and drive-throughs. Uses simpler non-LLM tools for simple intents ("bazooka ... knife") [src-20260806-53e2bf].
- **Money:** $67M Series B led by Expedition [src-20260806-53e2bf].
- **Buyers:** Capital One, Discover, RBC, the UK Department for Work and Pensions (DWP), PSEG, Taco Bell in 1,000+ outlets [src-20260806-53e2bf].
- **Claims (Omilia):** ARR $60M, up 10x; about 500 staff [src-20260806-53e2bf].
- **Bear:** CX voice is where the labs and Sierra compete hardest, and Deutsche Telekom calls it "commoditized" [src-20260727-3b21a8]. The article reports a disputed Taco Bell incident [src-20260806-53e2bf].
- **Buyer call (v2, interview 2024-11):** Discover chose Omilia on voice biometrics and agent assist; NICE, Genesys and Five9 GenAI looked "more of a bolt-on"; license $500,000 to $1M a year; containment below its 70%-75% target [src-20241114-f0ab80]. The call is two years old.
- **What this means:** the most revenue disclosed among the picks, in the most crowded lane.

### 3.8 Ema (horizontal orchestration; HR, IT, finance)
- **What it does:** "AI employees" made of teams of agents for HR, finance and support; runs in the customer's cloud, even fully disconnected ("air-gapped") [src-20261025-7ef133].
- **Money:** $77M Series B led by Creaegis; $140M total [src-20260930-9ee545].
- **Buyers:** NTT DATA, Hitachi, ADP, PwC, Google, KPMG, Wipro, Microsoft [src-20260930-9ee545].
- **Claims (Ema):** bookings over $150M; revenue up 50x in two years; 1M+ users; prices by completed tasks and outcomes; gross margin "close to 80%" (CEO) [src-20260930-9ee545]. Wipro HR went from 1,000 people to 550, a 45% cut (founder) [src-20261025-7ef133]. Sells with PwC and KPMG [src-20261025-7ef133].
- **Bear:** source is a trade site summarizing the company; many named "customers" are also IT-services partners [inference]. Horizontal layer faces lab and platform absorption (Q7).
- **Buyer call (v2):** Hitachi: a few hundred thousand a year, subscription priced on workflows, growth 5%-10% because Hitachi builds new agents in house; would still keep Ema [src-20260224-8c72f4]. This conflicts with the company's "completed tasks and outcomes" pricing claim [src-20260930-9ee545].
- **What this means:** the strongest horizontal traction claims in the repo, but the one buyer call shows subscription pricing and an expansion cap.

### 3.9 Kestra (workflow orchestration)
- **What it does:** open-source orchestration of data and infrastructure workflows; cloud product priced on usage [src-20260331-83a5c4].
- **Money:** $25M Series A led by RTP Global; $36M total [src-20260331-83a5c4].
- **Buyers:** Apple, Toyota, JPMorgan (security workflows), BHP (6 months to 6 days), Crédit Agricole; 30,000+ organizations use the open source [src-20260331-83a5c4].
- **Claims (Kestra):** enterprise revenue up 25x since seed; 2B+ workflows in 2025, up 20x [src-20260331-83a5c4].
- **Bear:** this is plumbing, not outcome-priced agents. It sits in the layer the labs and clouds are absorbing [inference].
- **What this means:** a good infrastructure business that is only loosely on-theme.

### 3.10 Skan AI (work context)
- **What it does:** captures how people actually work through on-device screenshots, sending only anonymized metadata, and feeds that context to agents [src-20260812-4cb1fc].
- **Money:** $63M Series C (Cathay, Dell Technologies Capital); about $120M total [src-20260812-4cb1fc].
- **Buyers:** a quarter of the Fortune 50, 7 of the 10 largest US banks, 3 of the 5 largest insurers; Mitie named [src-20260812-4cb1fc].
- **Claims (Skan):** revenue up over 300%; net dollar retention about 150%; one bank: 11.2M context switches, $37M of friction, cost per transaction down 32%, $18M savings; average savings 30% to 40% [src-20260812-4cb1fc].
- **Bear:** SAP (TechWolf), Celonis and Atlassian all claim the work-context layer [src-20261001-056aad] [src-20260303-4bfebc] [src-20260806-eab99c].
- **Insider call (v2):** a Skan director names Anthropic and OpenAI as the biggest competition and says Skan wants license, not services, revenue [src-20260616-48f4c6].
- **What this means:** the best evidence for the "work context" thesis, still company-reported, with the labs as the named threat.

### 3.11 Benchmarks: Sierra, Decagon and the CX leaders
- **Sierra.** $100M ARR in seven quarters, $150M in eight [src-20260309-78d5a1]; $950M raise at over $15B [src-20260504-c9d184]. Safelite: under $2 per transaction vs $7.50 to $9 human, 4-year contract with industry exclusivity, "80% likely to renew" [src-20260710-37d40b]. Deutsche Telekom ranks it first [src-20260727-3b21a8]. It lost a European fintech deal to Decagon on German voice quality; its business cases looked "too good to be true" to that buyer [src-20260708-a5fc76]. Customers automate 70% to 90% of cases per one source [src-20260310-ad2c26]; buyers report about 60% to 65% [src-20260318-033caf] [src-20260717-eb6872].
- **Decagon.** Over $100M ARR; about 90% of workloads on fine-tuned open models [src-20261013-d7909a]; hired a bank [src-20261013-6d4b75]. "Decagon is the worse Sierra" (Deutsche Telekom) [src-20260727-3b21a8]. Used at Airbnb [src-20261009-44e09b]. Notion: per meaningful conversation, around six figures a year, 4X to 7X cheaper than its offshore model, chat automation above 60% [src-20260515-de88a1]. Chime ran it next to Sierra and Maven behind its own router [src-20260518-714b0a].
- **Intercom Fin, now Salesforce.** 30,000+ customers, 76% average resolution [src-20260910-2cf2eb]; 30% to 40% at Smartly.io [src-20260326-b3dd2d]. A former sales lead: Fin often starts at about 30% of a contract and grows to 50%-60% of spend within a year (anecdotal); Sierra runs a paid three-month POC of $100,000 to $200,000 credited to the contract [src-20260310-e66bf3].
- **Crescendo (AI-native BPO).** Per-contact pricing, 10% to 40% discounts, "Gross margin did tank heavily", 50% to 60% of clients converted; mood at departure "dark" (former director) [src-20260724-865e53].

**What this means:** these set the price and performance bar every vertical pick is measured against.

### 3.12 Also tracked: Duvo, Sycamore, Workfabric
- **Duvo.** $32M Series A led by Balderton [src-20261014-1d5d80]. Maps processes with voice interviews and runs agents across ERPs and supplier portals [src-20260401-e0ba89]. Rohlik (related party) pays per run and saves 30 to 40 FTEs [src-20260609-4b024f]. Built on Anthropic with a "single-agent loop" [src-20260416-1a8cca].
- **Sycamore.** $65M seed co-led by Coatue and Lightspeed [src-20260330-2b99a8]. CEO: pricing is moving "towards the value or outcome-based" [src-20260404-029771]; CIOs want agents deployed inside their own private cloud [src-20260929-334bba]. No named customers.
- **Workfabric.** "Missions" and employee "twins"; no customers or funding on its site [src-20261023-21a6d6]; Cognizant named as a partner [src-20260710-e2a61b].

**What this means:** interesting teams, no independent proof yet.

### 3.13 Incumbents
- **Salesforce:** Agentforce ARR $1.5B+ [src-20260826-0b53e8]; Agentforce 1 at $550 per seat against about $1,300 of point tools [src-20260909-c1900d]; "50% of the bookings came from customers refilling the tank" [src-20260826-580137].
- **ServiceNow:** AI contract value over $1B [src-20260722-d4586c]; Control Tower free for a year [src-20260507-e6c2cd]; 90% of its own support cases handled by agents (CEO) [src-20260417-a917fe].
- **Zendesk:** $200M+ AI ARR, aiming for $400M this year [src-20260805-5a9fa7].
- **Workday:** AI products nearly $600M ARR [src-20260827-79de17].
- **Outsourcers:** Concentrix took a $1.05B impairment [src-20260929-4fcfe9]; TP core services fell 1.0% like for like [src-20260730-4cc420].

**What this means:** incumbents are monetizing agents fast, and outsourcers are already losing ground.

---

## 4. Unit economics

**How the money works, in plain English.** An outcome-priced agent company earns a fee per result. Its costs are:
1. **Inference:** what it pays the model provider each time the agent thinks. More steps and more checks mean more tokens (units of text the model reads and writes).
2. **Deployment:** forward-deployed engineers who integrate and tune the agent for each customer.
3. **Humans in the loop:** staff who handle cases the agent cannot, or check its work.

Gross margin is revenue minus those direct costs, as a share of revenue. Classic seat-based software (SaaS) runs at 80% to 90%. Outsourcers run at 10% to 15% [src-20260203-a5df90].

**Where AI companies sit today.**

| Measure | Value | Source |
|---|---|---|
| AI gross margin vs SaaS | 50% to 60% vs 80% to 90% | Bessemer [src-20260210-496d37] |
| AI product gross margin, trend | 45% (2025), 53% (2026E), 59% (2027E) | ICONIQ [src-20260924-1b6619] |
| AI product margin | about 50%, 20 to 30 points below SaaS | Growth Unhinged [src-20260513-fb3893] |
| AI-native at scale | 50% to 70% blended | Forbes [src-20260331-27a872] |
| Five9 (contact center incumbent) | adjusted gross margin down to 61.4% from 63.0% as AI grew | [src-20260806-833e7b] |
| Ema | "close to 80%" (CEO claim) | [src-20260930-9ee545] |
| Pace | target 80% (CEO goal) | [src-20260203-a5df90] |

**Price per unit against the human cost.**

| Work | Agent price | Human cost | Source |
|---|---|---|---|
| Support ticket | $0.99 (Fin) | $20 to $30 per resolved ticket | [src-20250821-666ad1] |
| Claim intake verification | under $2 (Sierra at Safelite) | $7.50 to $9 | [src-20260710-37d40b] |
| Outsourced FTE (insurance claims) | under $10,000 a year platform cost | above $20,000 Cognizant revenue | [src-20250627-297f7b] |
| CX resolution (one expert's estimate, low) | about $0.60 AI cost | $6 to $7 blended human | [src-20260708-a5fc76] |
| CX support at Notion | Decagon, around six figures a year | offshore model 4X to 7X Decagon | [src-20260515-de88a1] |
| Procurement coordination (small pharma) | Didero, about $30,000-$60,000 a year | consultant, $7,000-$12,000 a month | [src-20251024-112e5e] |
| Automated back-office task | $1,000 to $1,200 a month with AI | $200 to $300 a month on RPA (not a human cost) | [src-20260825-747be0] |

**Levers that raise margin.**
- **Higher automation.** Intercom's CFO: resolution went from about 25% to close to 70%, and "the more it's resolving, the better for our margin profile", because unresolved conversations burn compute that earns nothing [src-20260522-b1dbe3].
- **Cheaper models.** Decagon runs about 90% of workloads on fine-tuned open models [src-20261013-d7909a]. LangChain cut median cost per thread by 64% with routing [src-20261022-ae18f2]. But Accenture says routing is "hardly ever" used in practice [src-20261017-72ec30].
- **Falling deployment effort.** Safelite's first Sierra agent took 6 months; the second took 1 month; setup cost was "at least 35%-40% of your first year spend", declining [src-20260710-37d40b].
- **Deterministic steps.** UiPath and Pega argue for using AI at design time and cheaper fixed code at run time [src-20260903-1f1484] [src-20260722-796884].

**Levers that cut margin.**
- **Discounts without automation.** At Crescendo, invoices fell 10% to 40% while costs stayed flat [src-20260724-865e53].
- **More checks per task.** Decagon says tokens per conversation are rising as it adds quality checks [src-20260731-a07321].
- **Price compression.** Prices are converging on $0.50 to $2 per resolution in CX (W44, citing [src-20260413-63104e] [src-20260924-93c5ed] [src-20260926-ff7125]). Sierra's CEO expects agents to be compared to other agents, not labor [src-20250514-093b59].
- **Deferred revenue.** Automation Anywhere's milestone-based outcome deals delay ARR [src-20260702-b5efa8].
- **Token-priced seats.** Ascot caps heavy Cowork users at about 50, each "low four figures" a month [src-20260904-8886b4].
- **FDE as services.** A Workfabric executive calls FDE a "services play but with probably with more expensive engineers" [src-20260710-e2a61b].

**Conflict to note (unit economics).** Pace targets 80% [src-20260203-a5df90] and Ema claims close to 80% [src-20260930-9ee545], while every disclosed industry benchmark sits at 45% to 70% (table above). No pick reports gross margin after inference and deployment.

**Value-share math, worked example (repo numbers, my arithmetic).** Safelite measured a 35% to 40% cost cut and gave Sierra 10% of it [src-20260710-37d40b]. On $10M of handled cost, that is $3.5M to $4M saved and $350K to $400K to the vendor [inference]. Duvo's co-founder uses the same "10%" rule [src-20260701-3b0c17]. Cognizant returns about 50% of savings to the client [src-20250627-297f7b]. The vendor keeps a thin slice of the savings, so volume has to be large [inference].

**What this means:** underwrite these as 50% to 60% gross margin businesses that might reach 70% or more. Ask for margin after inference, FDE hours per customer by cohort, and the automation rate behind every price.

---

## 5. Data loops and moats

**What a data loop is.** Each job the agent does produces a record: what it tried, what failed, what a human corrected. If the company can use those records to make the next job cheaper or more accurate, and competitors cannot get them, it has a data loop. The question is whether this loop is real and whether it belongs to the startup, the customer, the platform or the lab.

**For: evidence that loops exist.**
- Sierra customers automate 70% to 90% of cases over time [src-20260310-ad2c26]. At Safelite, the second agent took a sixth of the time of the first [src-20260710-37d40b].
- Crosby tracks lawyer review minutes per task every week as its main company metric [src-20261025-1fbd1c] and runs a reinforcement-learning feedback loop with its lawyers [src-20260331-50e583] (investor blog).
- Duvo builds a database of automations reused across clients [src-20260609-4b024f] (related-party buyer) and pitches a cross-client memory layer [src-20260416-1a8cca].
- Pace's customer edits the agents' procedures itself, so operating know-how is captured in the product [src-20261025-c77b6e].
- Skan claims 25B work signals [src-20260812-4cb1fc]. Context improves accuracy a lot: about 30% to about 90% in one case [src-20261020-7922f1].
- Levie: the gap between 70% off-the-shelf and 97% accuracy decides whether work can be automated, and climbing that gap is where applied companies sit [src-20260915-68c6ef].

**Against: evidence that loops leak or do not compound.**
- The labs ship the improvement loop as a product: OpenAI Presence includes simulations, graders and an improvement loop [src-20260722-a3993b].
- Context drifts: the same analytics agent fell back to 60% in two months [src-20261020-7922f1].
- The customer owns the data. Rohlik says it could "mine the instructions of the agent" and move, though "It's theory" [src-20260609-4b024f]. A Sierra buyer called the learning loop "a little bit of a black box" with no service-level agreement [src-20260318-033caf].
- Buyers keep the context. Chime keeps data, procedures and tools in its own systems so vendors are interchangeable [src-20260518-714b0a]. Notion can switch CX vendors "within a month" without deep integrations [src-20260515-de88a1]. IKEA sees "not specific stickiness" at Magentic [src-20260209-7ec831].
- Systems of record hold the data and the API keys [src-20260724-865e53]. Walmart sees outside agents bypassing the support agent through APIs [src-20261006-b21c7a].
- In legal and healthcare admin, defensibility shifts to proprietary content, payer rules and write-back access, not the agent [src-20260512-5c6e2d] [src-20260111-f1affc].
- Prompts plus skills plus connectors are now a free file format, so value moves to proprietary data, write access and measured outcomes [src-20260130-79791d].

**Scorecard (my read).**

| Company | Proprietary data from doing the work | Customer can take it away? | Score [inference] |
|---|---|---|---|
| Crosby | Lawyer corrections per contract | Hard: the firm is the counterparty | Medium-high |
| Pace | Carrier procedures and exception handling | Possible: procedures are editable | Medium |
| Skan AI | Cross-company work patterns | Anonymized, aggregated | Medium |
| Amperos | Payer behavior on denied claims | Unknown | Medium (untested) |
| Magentic, Didero | Supplier and price behavior | Unknown | Low-medium |
| Sierra, Decagon | Conversation outcomes | Labs ship same loop; customer owns transcripts | Low-medium |
| Kestra, Ema, Sycamore | Workflow definitions | Yes | Low |

**What this means:** the loop is real where the vendor carries liability or sees cross-customer patterns the customer cannot. Ask every company to show accuracy or human minutes per task by quarter.

---

## 6. The bear case in one list (with the bull case at equal weight)

**Bull: why push further** (bull-bear.md).
1. Outcome pricing is real revenue: Zendesk $200M+ AI ARR [src-20260805-5a9fa7]; Sierra $100M to $150M ARR in a quarter [src-20260309-78d5a1]; Fin past $100M at 99 cents [src-20250821-666ad1].
2. Adoption is moving: outcome pricing 18% to 23% of vendors in six months [src-20260715-e16b49]; Salesforce added 2,000 production customers in a quarter [src-20260826-580137].
3. The budget is labor: about $119B of US CX wages [src-20260827-b22de5]; HFS $422B of BPO moving to services-as-software [src-20260831-73c927]; Concentrix impairment and TP's flat core show displacement has started [src-20260929-4fcfe9] [src-20260730-4cc420].
4. A liquid exit market: Fin about $3.6B [src-20260615-74b583]; Decagon has a banker [src-20261013-6d4b75]; SAP, Workday, NiCE and Genesys are buying [src-20261001-056aad] [src-20261013-7962db] [src-20260805-3deb2c] [src-20260902-b6edda].
5. Verticals outside CX have named customers: Pace at Palomar [src-20261025-c77b6e]; Crosby at Cursor and Ramp [src-20260331-50e583]; Magentic at Siemens and CCEP [src-20260923-47e348].
6. Buyers say they like it: "they're cheap because they're outcome-based" (Safelite) [src-20260710-37d40b]; Safelite rates renewal 80% likely [src-20260710-37d40b].
7. Deployment is the bottleneck, which favors investors with enterprise access [src-20260629-015aae] [src-20260728-aba703].
8. The swap from outsourcers is measurable: Notion's external vendor spend fell about 75% in two years [src-20260515-de88a1]; Novilla replaced a consultant at a fraction of the cost [src-20251024-112e5e].

**Bear: why stop and publish the view.**
1. Vendors grade their own outcomes. Zendesk uses its own LLM [src-20250806-3921b6]; a Sierra buyer had to reverse-engineer what "resolved" meant [src-20260318-033caf]; vendors quote containment without saying what is excluded from the denominator [src-20260708-a5fc76]. Outcome revenue could be repriced at renewal.
2. Most "outcome" pricing is per transaction: Bain [src-20260810-21fe8d]; Crescendo per contact [src-20260724-865e53]; Sierra per minute at Innovaccer [src-20260717-eb6872]; Pace by volume [src-20260508-386718].
3. Outcome pricing slows sales: HubSpot [src-20260812-1b0bca]; buyers prefer transactional pricing [src-20260708-a5fc76] and credits [src-20260827-fb556f].
4. Margins are worse than software: 50% to 60% vs 80% to 90% [src-20260210-496d37]; Crescendo's margin "did tank heavily" [src-20260724-865e53].
5. The labs are absorbing the stack: Presence [src-20260722-a3993b]; free harness [src-20260910-014b24]; AWS $1B FDE [src-20260730-e4cc74]; lab marketplaces become the channel [src-20260929-2fdd0f].
6. CX is commoditizing: Deutsche Telekom will cut to one or two vendors and calls the category "commoditized" [src-20260727-3b21a8]; a buyer saw nothing at Sierra "which others could not replicate" [src-20260708-a5fc76].
7. Volume may shrink: personal agents could bypass support agents through APIs, meaning "fewer calls" [src-20261006-b21c7a].
8. Real automation is below headlines: Fin 30% to 40% at Smartly.io [src-20260326-b3dd2d]; Sierra about 60% at a pilot with ROI "a little over 2x", below target [src-20260318-033caf].
9. Production is thin and fragile: 13% of CIOs see significant value [src-20261019-a120c4]; over 40% of agentic projects expected to be cancelled by 2027 [src-20250625-8a6cff]; 70% to abandon FDE-built systems by 2028 [src-20261012-11ce4a].
10. Prices are high: Sierra about 75x to 100x ARR, Decagon about 45x, Fin exit about a third of that (comps.md).
11. Horizontal orchestration lacks proof: no named customers at Sycamore or Workfabric [src-20260330-8d6266] [src-20261023-21a6d6].
12. Pick evidence is mostly self-reported: funding releases, an investor blog and vendor case studies (section 3).
13. Buyers keep vendors interchangeable: Chime routes across three CX vendors [src-20260518-714b0a]; Notion can switch in about a month [src-20260515-de88a1]; Hitachi builds its next agents without Ema [src-20260224-8c72f4].
14. Outside CX, v2 buyer contracts are consumption, platform or license priced, not per outcome [src-20260209-7ec831] [src-20260617-937cc1] [src-20251016-371c9b] [src-20260224-8c72f4] [src-20241114-f0ab80].

**Kill criteria (from bull-bear.md).** Stop pushing if any of these hold by the next checkpoint:
1. No outcome contract renews at the same or a higher unit price with a customer-agreed count.
2. Two or more F500 buyers or SI leads say a lab platform plus an SI replaced a vertical vendor in a live deal.
3. Formers report gross margin after inference and FDE below 50% with no falling trend in FDE hours.
4. Buyers say they take Agentforce, Now Assist or SAP's Joule by default and will not buy point vendors.
5. No candidate is available below about 30x forward ARR.
6. A buyer reports clawbacks or disputed counts at scale.

**What this means:** the bull case is about market size and early revenue; the bear case is about who counts the outcome and who keeps the margin. Both are strong. Diligence should target the bear points directly.

---

## 7. Open questions and expert-call targets

### 7.1 The open questions that decide the view
1. **Does any outcome contract renew at the same or a higher unit price, with a count the customer agrees with?** Safelite expects to renew Sierra, but the term runs to the end of 2028 [src-20260710-37d40b]. No renewal is on record.
2. **Who audits the count?** No independent auditor exists in public sources (W44). Buyers audit themselves [src-20260318-033caf].
3. **What is gross margin after inference and deployment at any pick?** None discloses it.
4. **How many FDE hours per customer, and is that falling?** Safelite's evidence says yes for one vendor [src-20260710-37d40b].
5. **Do labs plus SIs replace vertical vendors in live deals?** OpenAI trains SIs as FDEs [src-20261017-72ec30], but no call names a displaced vertical vendor.
6. **Does Pace or Amperos ever price per outcome, or stay on volume?** Both price by volume today [src-20260508-386718] [src-20261025-db0c8b]; the DOCS Dermatology call adds transaction minimums [src-20251016-371c9b].
9. **What is Decagon's unit price?** Notion gives the unit (per meaningful conversation) and the spend, not the price [src-20260515-de88a1].
7. **Do personal agents shrink support volume?** Walmart thinks simple calls could bypass the support agent [src-20261006-b21c7a].
8. **Who owns the context and the improvement loop when a customer leaves?** [src-20260609-4b024f] [src-20260318-033caf].

### 7.2 Expert-call targets (from expert-calls.md)

| Priority | Profile | Named targets | What to close |
|---|---|---|---|
| 1 | SI agent practice lead | Deloitte, Accenture, Cognizant, IBM Consulting and DXC agent leads listed in expert-calls.md | Outcome terms in real deals; platform mix; FDE hours (Q2, Q5, Q11) |
| 2 | Duvo customer (independent) | Morrisons, Notino, Holland & Barrett, Boden, Allegro [src-20261014-fb6b7e] | The outcome test outside a related party (Q15) |
| 3 | F500 buyer of an outcome-priced CX vendor | Uber (Sierra) [src-20260504-c9d184]. Chime and Notion now filed [src-20260518-714b0a] [src-20260515-de88a1] | Renewal and verification (Q2) |
| 4 | Vertical buyers outside CX | Palomar and Prudential (Pace); Siemens, CCEP (Magentic); Footprint (Didero); Ramp (Actively); Cursor, Clay (Crosby) | Renewal, pricing unit, margin (Q10, Q11) |

Filed in v2: Hitachi on Ema, Skan AI director, Avant on Didero and Magentic, IKEA on Magentic, Novilla on Didero, Justworks on Actively, DOCS Dermatology on Amperos, Discover on Omilia, ex-Palantir FDE, Cresta FDE, Cognizant, Accenture on UiPath, Crescendo on Zendesk, Ascot on Microsoft E7, Intercom Fin, Chime and Notion on Decagon. Still in the backlog: SOPHiA on Kestra, a second Skan AI executive, PwC on Maisa, Liberty Mutual legal AI and five others (expert-calls.md). Sycamore has no AlphaSense coverage.

**Five questions for every call** (W44):
1. What share of your agent spend is priced per outcome, and how is the outcome detected and audited?
2. Who built the harness in production: lab, SI, your team or the system-of-record vendor?
3. Which budget line paid: IT software, BPO or the business unit?
4. What blocked the last pilot from production?
5. If the lab shipped this feature tomorrow, what would you still pay the vendor for?

**What this means:** three calls (an SI lead, an independent Duvo customer, an F500 CX buyer) would test most of the kill criteria before the readout.

---

## 8. Landscape cuts: where each company sits

101 startups, cut six ways: the first 65 plus 36 vertical and horizontal players added 2026-10-28 from 2025 to 2026 funding reports and six VC primers (Foundation Capital, a16z twice, Bessemer three times; see insights/landscape-cuts.md for source ids). Late private names (Series D and later: Parloa, EvenUp, EliseAI, Federato, Glean, Sierra, Candid Health) are comps, outside the Seed to Series C check band. Each sits in exactly one group per cut. Full table with a source id on every row: insights/landscape-cuts.md. Pricing and stage come only from filed sources; thesis position is [inference].

### 8.1 The five worlds
Incumbents: labs and hyperscalers (OpenAI, Anthropic, Google, Microsoft, Amazon Web Services); systems of record (Salesforce, ServiceNow, SAP, Oracle, Workday and others); SIs and BPOs (Accenture, Cognizant, Infosys, TCS and others). No startup sits in "enterprises building their own".

| Group | n | Who |
|---|---|---|
| Vertical apps | 70 | Actively AI, Attention, Vida, Sierra, Decagon, Omilia, respond.io, Cresta, Moveworks, Adaptive, Basis, Definite, Elimentary, Xelix, Zolvo, Zomma, Didero, Lio, Magentic, Walter, Pactum, Pavus AI, Adonis, Amperos Health, Candid Health, GenHealth.ai, Procode, Prosper AI, ClearRisk AI, Notch, Pace, Crosby, Ivo, Wordsmith, Orbio, Spott, Take2, NeuBird AI, Crescendo, Rillet, Campfire, Tabs, Stuut, Tennr, Assort Health, Sixfold, Reserv, Harper, Federato, Eudia, Supio, EvenUp, ConverzAI, Juicebox, Rox, Unify, Parloa, Lorikeet, Gradient Labs, Resolve AI, Traversal, Serval, EliseAI, HappyRobot, Augment, GovDash, Polimorphic, Levelpath, Omnea, PolyAI |
| Horizontal orchestration | 13 | Ema, Kestra, Duvo, Sycamore, Airia, Maisa AI, Mimica, Skan AI, Workfabric AI, Relevance AI, n8n, Unframe, Glean |
| SIs and AI services | 5 | DeepOpinion, Otera, RapidCanvas, AuxoAI, Distyl AI |
| Agent infrastructure | 13 | CopilotKit, Coval, Dash0, Daytona, Flexprice, InsightFinder, Natural, Raindrop, Rein, Runlayer, Tsuga, LangChain, ElevenLabs |

**What this means:** venture money is in vertical apps (70 of 101); the other worlds belong to incumbents. The four added horizontal names (Relevance AI, n8n, Unframe, Glean) raised bigger rounds than the first nine but sit where labs and systems of record are moving. Distyl AI is placed with AI services [inference].

### 8.2 Buyer function
| Group | n | Who |
|---|---|---|
| Customer service and contact center | 11 | ElevenLabs, Sierra, Decagon, Omilia, respond.io, Cresta, Crescendo, Parloa, Lorikeet, Gradient Labs, PolyAI |
| Sales and revenue | 5 | Actively AI, Attention, Vida, Rox, Unify |
| Finance, accounting and lending ops | 11 | Adaptive, Basis, Definite, Elimentary, Xelix, Zolvo, Zomma, Rillet, Campfire, Tabs, Stuut |
| Procurement, supply chain and logistics | 10 | Didero, Lio, Magentic, Walter, Pactum, Pavus AI, HappyRobot, Augment, Levelpath, Omnea |
| Healthcare revenue cycle and admin | 8 | Adonis, Amperos Health, Candid Health, GenHealth.ai, Procode, Prosper AI, Tennr, Assort Health |
| Insurance and regulated ops | 9 | DeepOpinion, ClearRisk AI, Notch, Pace, Otera, Sixfold, Reserv, Harper, Federato |
| Legal | 6 | Crosby, Ivo, Wordsmith, Eudia, Supio, EvenUp |
| HR and recruiting | 5 | Orbio, Spott, Take2, ConverzAI, Juicebox |
| IT ops and agent infrastructure (sold to engineering) | 17 | CopilotKit, Coval, Dash0, Daytona, Flexprice, InsightFinder, Natural, Raindrop, Rein, Runlayer, Tsuga, LangChain, Moveworks, NeuBird AI, Resolve AI, Traversal, Serval |
| Real estate and property ops | 1 | EliseAI |
| Government and public sector | 2 | GovDash, Polimorphic |
| Cross-function (no single buyer) | 16 | Ema, Kestra, Duvo, Sycamore, Airia, Maisa AI, Mimica, Skan AI, Workfabric AI, RapidCanvas, AuxoAI, Distyl AI, Relevance AI, n8n, Unframe, Glean |

**What this means:** CX is crowded and late stage (Parloa at $3B, PolyAI at $750M added as comps [src-20260115-f3635c]); finance (11), procurement and logistics (10) and insurance (9) hold most early picks. Real estate (EliseAI) and government (GovDash, Polimorphic) are new groups.

### 8.3 Pricing model
Sierra: under $2 per transaction plus about 10% of savings [src-20260710-37d40b]. Decagon: per meaningful conversation [src-20260515-de88a1]. Crescendo: per contact [src-20260724-865e53]. Outcome rows are company claims from their own releases. Added: EvenUp per demand package [src-20241205-4ac3cf]; Unframe says customers do not pay until they see impact (company claim) [src-20250403-82b140]. None of the 36 added names disclosed a price in its funding announcement.

| Group | n | Who |
|---|---|---|
| Per outcome or savings share | 5 | Ema, Vida, Procode, Crosby, Unframe |
| Per transaction, task, conversation or run | 6 | Duvo, DeepOpinion, Sierra, Decagon, Crescendo, EvenUp |
| Hybrid (part outcome, part usage) | 1 | Prosper AI |
| Usage (minutes, GB, cloud consumption) | 3 | Tsuga, Kestra, Cresta |
| Subscription or seat | 1 | RapidCanvas |
| Not disclosed in any filed source | 85 | CopilotKit, Coval, Dash0, Daytona, Flexprice, InsightFinder, Natural, Raindrop, Rein, Runlayer, LangChain, ElevenLabs, Sycamore, Airia, Maisa AI, Mimica, Skan AI, Workfabric AI, Actively AI, Attention, Omilia, respond.io, Moveworks, Adaptive, Basis, Definite, Elimentary, Xelix, Zolvo, Zomma, Didero, Lio, Magentic, Walter, Pactum, Pavus AI, Adonis, Amperos Health, Candid Health, GenHealth.ai, ClearRisk AI, Notch, Pace, Otera, Ivo, Wordsmith, Orbio, Spott, Take2, NeuBird AI, AuxoAI, Rillet, Campfire, Tabs, Stuut, Tennr, Assort Health, Sixfold, Reserv, Harper, Federato, Eudia, Supio, ConverzAI, Juicebox, Rox, Unify, Parloa, Lorikeet, Gradient Labs, Resolve AI, Traversal, Serval, EliseAI, HappyRobot, Augment, GovDash, Polimorphic, Levelpath, Omnea, Distyl AI, Relevance AI, n8n, Glean, PolyAI |

**What this means:** buyer-verified prices are per transaction; true outcome pricing is only claimed, by five startups. 85 of 101 have no disclosed price.

### 8.4 Go-to-market channel
| Group | n | Who |
|---|---|---|
| Direct to the enterprise (no partner named in sources) | 73 | Coval, Dash0, Daytona, InsightFinder, Natural, Raindrop, Rein, Runlayer, Tsuga, ElevenLabs, Ema, Duvo, Sycamore, Airia, Maisa AI, Mimica, Skan AI, Actively AI, Attention, Sierra, Decagon, Omilia, respond.io, Cresta, Adaptive, Basis, Definite, Elimentary, Xelix, Zolvo, Zomma, Lio, Pactum, Pavus AI, Adonis, Amperos Health, Candid Health, ClearRisk AI, Notch, Ivo, Wordsmith, Orbio, Spott, Take2, NeuBird AI, Rillet, Campfire, Tabs, Federato, Eudia, Supio, EvenUp, ConverzAI, Juicebox, Unify, Parloa, Lorikeet, Gradient Labs, Resolve AI, Traversal, Serval, EliseAI, HappyRobot, Augment, GovDash, Polimorphic, Levelpath, Omnea, Relevance AI, Unframe, Glean, PolyAI, Distyl AI |
| Runs inside or on top of a system of record (SAP, Oracle, ServiceNow, existing EHR or email) | 10 | Moveworks, Didero, Magentic, Walter, GenHealth.ai, Sixfold, Stuut, Tennr, Assort Health, Rox |
| Sold or delivered through an SI, BPO or channel partner | 4 | DeepOpinion, Workfabric AI, Vida, Otera |
| Sells the finished work (AI-native service firm or BPO replacement) | 9 | Procode, Prosper AI, Pace, Crosby, Crescendo, RapidCanvas, AuxoAI, Harper, Reserv |
| Open source or developer-led | 5 | CopilotKit, Flexprice, LangChain, Kestra, n8n |

**What this means:** direct sale dominates (73 of 101). Added names that ride a record: Sixfold (inside policy admin systems, Guidewire invested), Stuut (existing ERPs), Tennr (writes to the EHR per a16z), Assort Health (embeds in the EHR), Rox (plugs into Salesforce and Zendesk). Harper (licensed agency) and Reserv (TPA) sell the work. The added 36 brought no new SI channel; all three SI-delivered startups run through Cognizant, so "SIs as channel" rests on one SI [src-20260724-b4a442] [src-20250627-297f7b] [src-20260710-e2a61b].

### 8.5 Stage
| Group | n | Who |
|---|---|---|
| Seed | 7 | Flexprice, Sycamore, Definite, Elimentary, Zolvo, Zomma, Walter |
| Series A | 34 | CopilotKit, Coval, Natural, Raindrop, Rein, Runlayer, Tsuga, Kestra, Duvo, Didero, Lio, Magentic, Amperos Health, GenHealth.ai, Procode, ClearRisk AI, Notch, Otera, Orbio, Spott, Take2, AuxoAI, Stuut, Harper, Eudia, ConverzAI, Juicebox, Lorikeet, Gradient Labs, Resolve AI, Traversal, Augment, Polimorphic, Unframe |
| Series B | 33 | Dash0, Daytona, InsightFinder, Ema, Mimica, Actively AI, Attention, Omilia, respond.io, Adaptive, Basis, Xelix, Pace, Crosby, Ivo, Wordsmith, NeuBird AI, RapidCanvas, Rillet, Campfire, Tabs, Sixfold, Reserv, Supio, Unify, Serval, HappyRobot, GovDash, Levelpath, Omnea, Distyl AI, Relevance AI, Assort Health |
| Series C | 4 | Skan AI, Adonis, Tennr, n8n |
| Series D or later / late private | 7 | Sierra, Candid Health, Federato, Parloa, EvenUp, EliseAI, Glean |
| Stage not in filed sources | 16 | LangChain, ElevenLabs, Airia, Maisa AI, DeepOpinion, Workfabric AI, Vida, Decagon, Cresta, Moveworks, Pactum, Pavus AI, Prosper AI, Crescendo, Rox, PolyAI |

**What this means:** Series A and B are most of the universe (67 of 101); 16 have no stage on file. Resolve AI's Series A was at a $1B valuation [src-20260204-8be226]; Serval's Series B too [src-20251211-c9227b].

### 8.6 Thesis position [inference]
| Group | n | Who |
|---|---|---|
| Fits: vertical app that owns a workflow | 53 | Actively AI, Attention, Vida, Sierra, Decagon, Omilia, respond.io, Cresta, Adaptive, Basis, Definite, Elimentary, Xelix, Zolvo, Zomma, Lio, Pactum, Pavus AI, Adonis, Amperos Health, Candid Health, ClearRisk AI, Notch, Ivo, Wordsmith, Orbio, Spott, Take2, NeuBird AI, Rillet, Campfire, Tabs, Federato, Eudia, Supio, EvenUp, ConverzAI, Juicebox, Unify, Parloa, Lorikeet, Gradient Labs, Resolve AI, Traversal, Serval, EliseAI, HappyRobot, Augment, GovDash, Polimorphic, Levelpath, Omnea, PolyAI |
| Fits: rides on the system of record | 10 | Moveworks, Didero, Magentic, Walter, GenHealth.ai, Sixfold, Stuut, Tennr, Assort Health, Rox |
| Fits: sells the outcome as a service | 7 | Procode, Prosper AI, Pace, Crosby, Crescendo, Harper, Reserv |
| Channel: SI, BPO or managed service | 5 | DeepOpinion, Otera, RapidCanvas, AuxoAI, Distyl AI |
| Exposed: horizontal orchestration or context | 13 | Ema, Kestra, Duvo, Sycamore, Airia, Maisa AI, Mimica, Skan AI, Workfabric AI, Relevance AI, n8n, Unframe, Glean |
| Neutral: picks and shovels (infra, evals, security) | 13 | CopilotKit, Coval, Dash0, Daytona, Flexprice, InsightFinder, Natural, Raindrop, Rein, Runlayer, Tsuga, LangChain, ElevenLabs |

**What this means:** about seven in ten (70 of 101) fit the thesis; the horizontal group (13) carries the most absorption risk from labs and systems of record. New pattern in the additions [inference]: vertical apps that replace the record rather than ride on it (Rillet, Campfire, Serval, Federato), and incumbents investing in agents on their own records (Guidewire in Sixfold, Thomson Reuters Ventures in Supio, RELX's REV in EvenUp).

## Appendix A. Glossary

- **Agent:** AI software that takes actions in other software, not just answers questions.
- **Agentforce:** Salesforce's agent product line.
- **AOP (Agentic Operating Procedure):** Pace's term for the written procedure an agent follows.
- **API (application programming interface):** a way for software to call other software directly.
- **ARR (annual recurring revenue):** yearly value of subscription or recurring contracts.
- **BPO (business process outsourcing):** paying an outside firm to run a process, such as a call center or claims processing.
- **CCaaS (contact center as a service):** cloud call-center software, such as Genesys, NiCE or Five9.
- **CCEP (Coca-Cola Europacific Partners):** a large bottler named as a Magentic customer.
- **CIO (chief information officer):** the executive who runs a company's IT.
- **Containment / resolution rate:** share of conversations an agent finishes without a human. Vendors define it differently.
- **CSAT (customer satisfaction score):** a survey score of how happy customers are.
- **CX (customer experience):** customer service and support.
- **Eval:** an automated test that checks an agent's work.
- **ERP (enterprise resource planning):** core business software for finance, purchasing and inventory, such as SAP or Oracle.
- **FDE (forward-deployed engineer):** a vendor engineer who sits with the customer to build and tune the deployment.
- **FNOL (first notice of loss):** the first report of an insurance claim.
- **FTE (full-time equivalent):** one full-time worker's worth of labor.
- **Gross margin:** revenue minus direct costs, as a share of revenue.
- **Harness:** the code around a model that gives it tools, memory, rules and tests.
- **Inference:** running a model to produce an answer. It is paid per token.
- **Headless:** running a vendor's agent behind the buyer's own interface, through an API.
- **ITSM (IT service management):** the help desk and ticket systems for IT problems.
- **LLM (large language model):** the type of AI model behind ChatGPT and Claude.
- **NDR (net dollar retention):** revenue from last year's customers this year, as a share of last year. Over 100% means they spend more.
- **NPS (net promoter score):** a survey of how likely customers are to recommend.
- **Orchestration:** coordinating many agents and people across many systems.
- **Outcome pricing:** charging per result (a resolved case, a recovered claim) instead of per user.
- **Output pricing:** charging per unit of work done (a conversation, a run), whether or not it achieved the goal.
- **POC (proof of concept):** a small test before a real deployment.
- **RCM (revenue cycle management):** the billing and collections work of healthcare providers.
- **RPA (robotic process automation):** older rule-based software that clicks through screens, sold by UiPath and others.
- **SaaS (software as a service):** cloud software usually sold per user.
- **Seat:** one user license.
- **Services-as-software:** software that delivers a service outcome that used to be bought from people.
- **SI (systems integrator):** a consulting firm that installs and connects software, such as Accenture, Deloitte or Cognizant.
- **SoR (system of record):** the main database for a function, such as Salesforce for customers or Workday for employees.
- **TAM (total addressable market):** the most that could be spent if every possible buyer bought.
- **Token:** a small unit of text that a model reads or writes; model use is billed by token.
- **Work context:** data on how work actually gets done, used to guide agents.

---

## Appendix B. Gaps and next actions

1. No renewal of an outcome contract on record. Next: SI lead and F500 CX buyer calls (section 7).
2. No gross margin after inference for any pick; the v2 Ema and Skan calls did not give one. Next: formers, and the Kestra call in the backlog.
3. No independent customer for Duvo, Sycamore or Workfabric. Next: Morrisons or Notino call.
4. Pick facts rest on press releases plus, since v2, one or two buyer calls each for Didero, Magentic, Amperos, Actively, Omilia and Ema. Crosby and Pace still lack an independent enterprise buyer. Next: named enterprise buyers (section 7.2).
6. No Decagon unit price. Next: ask the Notion or Chime contacts for the contract price per conversation.
5. Four long podcasts were only keyword-searched (Appendix C). Next: read in full if the readout leans on Ema, Crosby or Pace.

---

## Appendix C. Source coverage (what was and was not read in full)

**Read in full, line by line, with notes in insights/primer-notes/:**
- All 24 AlphaSense records filed in sources/alphasense/ for v1, from src-20250627-297f7b to src-20261017-72ec30 (one note file each).
- v2: 17 more AlphaSense records, each read in full, notes in primer-notes/v2-alphasense-2026-10-27.md: src-20241114-f0ab80, src-20251016-371c9b, src-20251024-112e5e, src-20251126-6d86c8, src-20260209-7ec831, src-20260224-8c72f4, src-20260310-e66bf3, src-20260515-de88a1, src-20260518-714b0a, src-20260616-48f4c6, src-20260617-937cc1, src-20260618-f36dc6, src-20260724-b4a442, src-20260825-747be0, src-20260828-bb2734, src-20260904-8886b4, src-20260908-547a69. All 41 filed AlphaSense calls are now read in full.
- Repo insights: framework.md, evidence-by-question.md (658 lines), weekly/2026-W44.md, bull-bear.md, comps.md, market-sizing.md, startup-landscape.md, labs-vs-startups.md, timeline.md.
- Company cards for the 10 picks plus sierra, decagon, duvo, sycamore, workfabric, salesforce, servicenow, intercom, zendesk and crescendo.
- The 17 pick sources: src-20260930-9ee545, src-20260331-83a5c4, src-20260812-4cb1fc, src-20260428-2d177a, src-20261025-5ffac1, src-20260422-d6ae9d, src-20261025-db0c8b, src-20260331-50e583, src-20261025-474366, src-20260212-5fd1e0, src-20260213-3c647d, src-20260917-25441c, src-20260923-47e348, src-20260806-53e2bf, src-20260527-cecfde, src-20261025-58fd6b, src-20261025-c77b6e.
- v3 (2026-10-28), for Section 8: six VC primers read in full: Foundation Capital services-as-software year one src-20250703-8a38e7; a16z "The Incumbents Are Coming" src-20260903-a696de; a16z "RIP to RPA" src-20241113-d5f4fa (dated 2024-11); Bessemer State of AI 2025 src-20250813-44ef93; Bessemer IT services roadmap src-20251028-1ffc30; Bessemer vertical AI part IV src-20250128-3948ca. Plus 35 startup sources (funding reports and company blogs), each read in full: src-20250806-b579d5, src-20251015-1d9298, src-20250916-6b0cd0, src-20251120-b7dfc3, src-20250618-89929d, src-20251002-499204, src-20260129-3fadee, src-20250604-fd80b0, src-20260225-3917a2, src-20251118-a1bc08, src-20250213-7eb7f6, src-20250430-935fd7, src-20251007-efb7da, src-20250211-780a74, src-20250925-7d17f1, src-20260312-b92bcd, src-20250714-a49000, src-20260115-f3635c, src-20250806-000216, src-20250530-b93251, src-20260204-8be226, src-20250618-b909ed, src-20251211-c9227b, src-20250820-5c5edf, src-20250903-f1a523, src-20250904-fe3d9b, src-20260115-edd4ec, src-20250709-395aa2, src-20250630-c0d572, src-20250917-786a38, src-20250922-1bc8b4, src-20250506-6ff4ce, src-20251009-9cd90b, src-20250403-82b140, src-20250610-0a09d0.

**Keyword-searched only, not read in full:**
- src-20261025-7ef133 (Ema founder podcast), src-20261025-1fbd1c and src-20260618-7d51b5 (Crosby podcasts), src-20260203-a5df90 (Pace on Sequoia's podcast). Quotes from these were checked in context around each line used.
- expert-calls.md was read for targets, the question guide and the filed list; signals.md and investor-theses.md were not read.

**Not read in full (cited through the repo's digests):**
- Most of the roughly 7MB of other source records in sources/. Facts from them are cited as they appear in evidence-by-question.md, W44, bull-bear.md, comps.md and market-sizing.md, which carry source ids. Those facts were checked against the digest text, not reopened in the original source. Treat them as one step removed.

**Weak or biased sources flagged in the text:**
- src-20260609-4b024f: Rohlik shares a founder with Duvo.
- src-20260318-033caf: buyer identity is ambiguous (filed as Workfabric, describes healthcare work).
- src-20260717-eb6872 and src-20260811-852c57: AI-run interviews; market statistics in them are not used.
- src-20260708-a5fc76: the expert's market statistics are unsourced and not used.
- src-20260804-3aa89c: a Salesforce partner, so biased toward Agentforce.
- src-20260507-288237 and src-20261007-fc84b0: marketing interviews. The Gamma source uses "outcome-based agents" as packaging with no outcome price.
- src-20260331-50e583: written by Crosby's lead investor.
- src-20261025-474366, src-20261025-c77b6e: vendor case studies.
- Most pick facts: funding press releases, so company claims.
- src-20260828-bb2734: AI-run interview; the 70% figure is called "not a precise number" by the expert.
- src-20241114-f0ab80: interview dated 2024-11, the oldest call in the set.
- src-20260617-937cc1: vendor ratings come from the expert's RFP scoring, not a contract.
- src-20251024-112e5e: the expert once says the consultant cost "a month" when the math is per year; only the stated ranges are used.
- src-20251126-6d86c8: pricing model not stated; spend figure only.
- src-20260310-e66bf3: the expert now works at ElevenLabs, a competitor.
- v3 funding reports: most are company press releases or trade write-ups of them, so company claims. src-20250714-a49000 (Unify) date is taken from a BusinessWire listing; the blog page metadata says 2026-03-10. Rox's $1.2B valuation is "according to multiple sources" [src-20260312-b92bcd]. PolyAI's round stage is not in the source [src-20260115-f3635c].
