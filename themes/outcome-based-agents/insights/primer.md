# Outcome-based agents and agentic orchestration: VC primer

_Version 1, dated 2026-10-26 (America/Chicago). Built from the oba repo: insights/ (framework, evidence-by-question, weekly/2026-W44, bull-bear, comps, market-sizing, startup-landscape, labs-vs-startups, timeline, expert-calls), companies/ cards, and the sources/ records named in Appendix C. Free sources only, plus the AlphaSense expert calls already filed in the repo. Reading log and per-source notes: insights/primer-notes/._

**Start here.** This primer is for an investor who writes Series B to D checks and is new to AI agents. Read it in this order:
1. Section 1 (the big picture) tells you what an "agent" is, who sells them, who buys them and how big the money pools are.
2. Section 0 (the decision summary) gives the view and the 10 things that shaped it.
3. Section 2 answers 17 questions in order. Skip to the ones you care about.
4. Sections 3 to 6 cover the companies, the money, the data and the bear case.
5. Appendix A is a glossary. Every acronym is spelled out the first time it appears and again in the glossary.

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

1. **"Outcome" usually means a transaction, not a result.** Bain says most outcome pricing (per resolution, per lead) is really output pricing [src-20260810-21fe8d], and only about 10% of AI-native and hybrid vendors use outcome pricing at all (Bain, as cited by fileAI) [src-20261012-e6c2b7]. In the calls, Sierra bills Innovaccer by "platform and then per minute" [src-20260717-eb6872], Crescendo's "outcome" contracts were per contact, "not per resolution" [src-20260724-865e53], Pace bills an annual platform fee plus per-claim usage at a UnitedHealth unit [src-20260811-852c57], and Amperos describes a "volume-based" subscription [src-20261025-db0c8b]. Decagon says most customers choose per conversation [src-20241210-0d932d].
2. **Where outcome pricing exists, it is real money.** Zendesk's CEO says it passed $200M of AI ARR on per-resolution billing [src-20260805-5a9fa7]. Sierra went from $100M to $150M ARR in one quarter [src-20260309-78d5a1]. Intercom's Fin, priced at $0.99 per resolution, was bought by Salesforce for about $3.6B [src-20260615-74b583] [src-20260910-2cf2eb].
3. **The vendor grades its own homework.** Zendesk uses its own large language model (LLM) to decide whether a ticket was resolved [src-20250806-3921b6]. A Sierra buyer could not see how "resolved" was defined and audited it himself [src-20260318-033caf]. No independent auditor shows up in public sources (W44).
4. **Real resolution rates sit below the headlines.** Fin resolves 30% to 40% at Smartly.io [src-20260326-b3dd2d] against a 76% average Salesforce cites [src-20260910-2cf2eb]. Sierra runs at about 60% to 65% at two buyers [src-20260318-033caf] [src-20260717-eb6872]. An AI-native outsourcer contained 30% to 40% of email [src-20260724-865e53].
5. **Outcome pricing without proven automation destroys margin.** At Crescendo, discounts of 10% to 40% met flat costs and "Gross margin did tank heavily" (former director) [src-20260724-865e53]. Crosby's founder: "We lost a lot of money on it until we were able to get the pricing right" [src-20261025-1fbd1c].
6. **The prize is labor and outsourcing budgets, not software budgets.** HFS sizes business process outsourcing (BPO) at $786B by 2035 with $422B moving to "services-as-software" [src-20260831-73c927]. Gartner puts the whole AI agents and assistants line at $29.2B in 2026 [src-20260916-b894eb].
7. **The big platforms are taking a large share.** Salesforce added 2,000 paying production customers in a quarter, and half of bookings came from customers "refilling the tank" [src-20260826-580137]. A KPMG ServiceNow partner says "nothing on the market" competes with ServiceNow's AI in IT service management (ITSM) [src-20260911-0742fb].
8. **Consultancies are the installers, and the labs are paying them.** Anthropic put $100M into SI partners [src-20260312-73c25c], Google a $750M partner fund [src-20260422-72407e], and AWS (Amazon Web Services) a $1B in-house forward-deployed engineer (FDE) team [src-20260730-e4cc74]. An Accenture managing director says OpenAI is training SIs as its "extended arm" [src-20261017-72ec30].
9. **The labs are moving up into the job itself.** OpenAI's Presence ships a complete customer service agent [src-20260722-a3993b]. A Deutsche Telekom executive calls customer service agents "commoditized" and plans to cut from five vendors to one or two [src-20260727-3b21a8].
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

- **Adoption is rising from a low base.** ICONIQ: outcome pricing went from 18% to 23% of AI vendors in six months [src-20260715-e16b49]. Bain: most outcome pricing is output pricing [src-20260810-21fe8d].
- **Buyers often prefer predictability.** A buyer at a European fintech wanted "a more transactional pricing without outcome commitment" [src-20260708-a5fc76]. In an a16z survey, 27 of 50 buyers preferred work-based credits against 14 for tokens [src-20260827-fb556f]. HubSpot says outcome pricing and trials lengthened sales cycles [src-20260812-1b0bca].
- **Sellers' own doubts.** Sierra's CEO calls cost-savings pricing "a temporary drug" once agents are compared to other agents, not to labor [src-20250514-093b59].

**Conflict to note (unit economics).** Sierra is the outcome-pricing benchmark, yet one buyer pays per minute [src-20260717-eb6872] while another pays per verified transaction [src-20260710-37d40b]. Sierra's real pricing varies by account.

**What this means:** ask every company for the contract, not the slide. Count how much revenue is truly per result.

### Q3. What blocks production?

**Answer: data, integration, security reviews and trust, more than model quality. Confidence: med.**
- A Cognizant practice head lists proof-of-concept (POC) fatigue, no roadmap, legal review "a couple of months" and API (application programming interface) integration "two, three months" [src-20250627-297f7b].
- Infosys builds inside the client's firewall partly to skip security approvals that can take "up to six months" [src-20251006-b80311].
- Crescendo promised deployment in 6 months and took a year; clients would not hand over API keys [src-20260724-865e53].
- Smartly.io's Fin rollout was delayed "mainly from the vendor side, from the capability side", and accuracy depended on the knowledge base [src-20260326-b3dd2d].
- Incidents: an agent deleted a production database in 9 seconds [src-20260428-8baab9].

**What this means:** vendors that bring their own engineers and carry the integration work get through. That costs money (section 4).

### Q4. Whose budget pays?

**Answer: increasingly the labor or outsourcing budget, through the business unit. Confidence: med.**
- A Duvo co-founder sells from the department's "service budget line, because it is easier to procure, usually higher budgets than on softwares" [src-20260701-3b0c17].
- Safelite set the price by measuring a 35% to 40% cost cut and giving Sierra "10% of that" [src-20260710-37d40b].
- Salesforce says outcome deals are funded by savings or by qualified leads and booked orders [src-20260909-c1900d].
- Indian IT majors show the swap: Infosys AI revenue is 10.5% of total [src-20261023-db47fe] and TCS annualized AI revenue is $3.1B [src-20261008-ae3125], while their total growth is low single digit (market-sizing.md).

**What this means:** the buyer compares against the outsourcer's invoice. That is a much bigger pool than software, but it is also a price ceiling.

### Q5. Who builds the harness?

**Answer: split. Vertical vendors build their own; SIs assemble the rest on lab and platform pieces. Confidence: med.**
- Sierra's FDE lead: "how do you actually guarantee the outcome? And that really is forward-deployed engineering" [src-20260728-aba703].
- The labs fund SIs: Anthropic $100M [src-20260312-73c25c], Google $750M [src-20260422-72407e]. An Accenture managing director says OpenAI trains SIs as FDEs, its "extended arm" [src-20261017-72ec30].
- Some enterprises build: Ramp built its Laminar harness in six weeks [src-20261022-ae18f2]; Capital One built a multi-agent platform on open-source models [src-20260416-e6896d]; Airbnb plans its own agent for 2027 [src-20261009-44e09b] (low-med).
- Counter-signal: Gartner predicts 70% of enterprises will abandon agent systems built by vendor FDE teams by 2028 [src-20261012-11ce4a].

**What this means:** the harness itself is not the moat. Whoever owns the deployment relationship and the result is.

### Q6. What did the labs ship, and what did it absorb?

**Answer: a lot, in 6 to 9 months. Generic harness and support agents are now lab features. Confidence: high on what shipped, med on impact.**
- OpenAI Presence: a complete CX agent harness with procedures, guardrails, simulations and graders [src-20260722-a3993b].
- OpenAI Agents API: production harness with no extra fee [src-20260910-014b24]. Anthropic Managed Agents at $0.08 per session-hour [src-20260408-e5d37b].
- Marketplaces: Sierra and Decagon are launch partners in the OpenAI Marketplace, so buyers can spend lab commitments on them [src-20260929-2fdd0f].
- AWS: $1B in-house FDE team [src-20260730-e4cc74].
- Buyers' view: Accenture says "models are such commodities" and model routing is "hardly ever" used in practice [src-20261017-72ec30]. Deutsche Telekom rules out US labs for some EU data [src-20260727-3b21a8].

**What this means:** a startup selling the agent loop alone is in the labs' path. Selling the finished job, with domain rules and liability, is safer [inference].

### Q7. Orchestration, context, vertical or services: where does value sit?

**Answer: vertical outcome first, then systems of record. Work context is promising but unproven. Horizontal orchestration is being squeezed. Confidence: med.**
- Orchestration is squeezed between clouds and systems of record that ship their own agents [src-20260422-1f1ec3]. Microsoft and ServiceNow both pitch the governance "control tower" over everyone's agents [src-20260501-fc687c] [src-20260507-e6c2cd].
- Context matters: one analytics agent rose from about 30% to about 90% accuracy with business context, then fell to 60% in two months as the context drifted [src-20261020-7922f1]. SAP is buying TechWolf's work-context graph [src-20261001-056aad].
- A Wawa CIO wants AI to first build "a map" of system interactions, then overlay business context [src-20260402-8d84cb].
- Battery Ventures dissents: "Durable companies will look more like SaaS companies of old with AI superpowers than collections of loosely orchestrated agents" [src-20260123-b88941].

**What this means:** buy the layer that owns a paid-for result or proprietary context, not the plumbing between agents.

### Q8. What about systems of record?

**Answer: they are strong where they own the data, weaker where they only add AI to a seat. Confidence: med.**
- Salesforce: Agentforce ARR $1.5B+ with a widened definition [src-20260826-0b53e8]; premium AI products are about 5% of the base at 60% to 80% price uplift [src-20260909-c1900d]; bought Fin [src-20260910-2cf2eb].
- ServiceNow: AI annual contract value over $1B in Q2 2026 [src-20260722-d4586c]. A KPMG partner says "nothing on the market" competes in ITSM and big clients are never lost because "The risks are just too great" [src-20260911-0742fb]. The same partner reports seat contraction, "debooks" and price-led growth [src-20260911-0742fb].
- A Wawa CIO says Now Assist does not "really do a job" and asks "Do I even need to have a ServiceNow platform?" [src-20260402-8d84cb].
- Zendesk and Intercom beat an AI-native outsourcer because they hold the data, and clients would not give the startup API keys [src-20260724-865e53].
- Exposure: personal agents could skip a retailer's support agent by calling its APIs directly, which Walmart calls "permissioning, not engineering work" [src-20261006-b21c7a].

**Conflict to note (right to win).** KPMG says ServiceNow is unbeatable in ITSM [src-20260911-0742fb]; Wawa's CIO is testing alternatives and questions the platform [src-20260402-8d84cb]. One is a partner, the other a buyer with no deployment yet.

**What this means:** systems of record are the default buyer choice and the main acquirer. A startup must win where the record holder is weak, or sell to it [inference].

### Q9. Which horizontal players are investable?

**Answer: few with proof. Confidence: med.**
- Ema: $77M Series B, 50+ active enterprise deals, bookings over $150M, prices by completed tasks and outcomes [src-20260930-9ee545] (company claims).
- Kestra: $25M Series A; enterprise revenue 25x since seed; 2B+ workflows in 2025 [src-20260331-83a5c4] (company claims). It is workflow orchestration more than an agent company [inference].
- Skan AI: $63M Series C; revenue up over 300% year on year; net dollar retention about 150% [src-20260812-4cb1fc] (company claims).
- Sycamore: $65M seed, no named customers [src-20260330-8d6266]. Workfabric: no customers or funding disclosed on its site [src-20261023-21a6d6].

**What this means:** horizontal names with real customers exist (Ema, Kestra, Skan), but their numbers are press-release numbers. Diligence first.

### Q10. Which vertical players are investable?

**Answer: the picks in section 3 outside customer service. Confidence: med.** Pace (insurance), Amperos (medical billing), Crosby (legal), Didero and Magentic (procurement), Actively (sales), Omilia (voice CX). Others in the repo: Lassie in dental back office, $10M+ annualized revenue and 700+ practices [src-20260603-ce0e80]; Basis in accounting, $100M Series B [src-20260224-b6a4eb].

**What this means:** vertical names at Series A or B are where price and proof still line up.

### Q11. What are the unit economics?

**Answer: below software today, with a path up if automation rises. Confidence: med.** See section 4.

**What this means:** underwrite to 50% to 60% gross margin unless a company proves more.

### Q12. What are the exit paths?

**Answer: strategic sale to a system of record or contact-center platform. Confidence: med-high.**
- Fin to Salesforce for about $3.6B [src-20260615-74b583]. NiCE bought Cognigy [src-20260805-3deb2c]. Genesys bought Pinkfish [src-20260902-b6edda]. SAP is buying TechWolf [src-20261001-056aad]. Workday is buying C1.ai [src-20261013-7962db].
- Decagon hired a bank; ServiceNow was reported in early talks and says it is not interested [src-20261013-6d4b75] [src-20261013-d7909a].
- Sierra bought Takeoff, a three-person outcome-paid company [src-20260723-bd3453].

**What this means:** buyers exist, but they pay well below private CX multiples.

### Q13. What do Fortune 500 heads of AI and automation say?

**Answer from calls: they want results, distrust vendor counts, and plan to consolidate. Confidence: med.**
- Deutsche Telekom runs ElevenLabs, Sierra, Decagon and Wonderful, is dropping HappyRobot, and will consolidate to one or two vendors in about 1.5 years [src-20260727-3b21a8].
- Walmart: personal agents may mean "fewer calls" to support [src-20261006-b21c7a].
- Wawa's CIO: "outcome-based agents is going to be very important because they are directly aligned to what we're always trying to achieve" [src-20260402-8d84cb].
- Safelite: "they're cheap because they're outcome-based" [src-20260710-37d40b].

**What this means:** buyers like the idea and will pay, but will cut vendors fast once the category commoditizes.

### Q14. What do SI practice leads say?

**Answer: agents cut their revenue but can lift their margins. Confidence: med.**
- Cognizant: the agent platform costs under $10,000 per full-time-equivalent (FTE) a year against Cognizant revenue above $20,000 per outsourced FTE; about 50% of savings go back to the client; "Our revenues go down, but our margins go up" [src-20250627-297f7b].
- Infosys: headcount from about 400,000 to about 340,000 through attrition replaced by automation; the goal is to "move from a revenue-based company to a margin-based company" [src-20251006-b80311]. "We don't sell AI products" [src-20251006-b80311].
- OSF Digital: Agentforce work growing over 20% against single digits for core; SIs shifting from time-and-materials to fixed scope or outcome [src-20260804-3aa89c].
- Accenture: OpenAI is training SIs as FDEs; 90% of workloads run on frontier models [src-20261017-72ec30].

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
- **Bear:** no named customers, no buyer call. Payer rules and health record write-back are where defensibility sits in healthcare admin [src-20260111-f1affc], and that is untested here.
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
- **Bear:** no named customers, no pricing, no buyer call. Oracle and SAP are embedding agents in ERP [src-20261003-10d57c] [src-20261016-9f1777].
- **What this means:** a good category, thin evidence.

### 3.5 Magentic (procurement and supply chain; vertical outcome)
- **What it does:** procurement agents for large manufacturers.
- **Money:** $18M Series A led by Felicis with Sequoia and Westly; $23.5M total [src-20260917-25441c].
- **Buyers:** one manufacturer runs over 1M purchase orders a year through it; $4M of savings found at another [src-20260917-25441c]. Siemens and Coca-Cola Europacific Partners (CCEP) are named on a podcast page [src-20260923-47e348].
- **Claims (Magentic):** 1% to 2% spend savings worth $100M to $200M against $50M from labor; agents start as "interns" [src-20260923-47e348].
- **Bear:** the article itself says it is unclear whether the wider Global 500 will adopt [src-20260917-25441c].
- **What this means:** a savings-share story that could support outcome pricing. Ask for a signed savings-share contract.

### 3.6 Actively AI (sales; vertical outcome)
- **What it does:** one AI agent per sales account that researches and prioritizes, positioned as a Salesforce replacement over time [src-20260428-2d177a].
- **Money:** $45M Series B at $250M, co-led by TCV and First Harmonic; $67.5M total [src-20260428-2d177a].
- **Buyers:** Ramp, Verkada [src-20260428-2d177a].
- **Claims (customers via Forbes):** Ramp attributes "tens of millions" of new revenue and about 23% higher close rates on AI-driven deals; Verkada doubled productivity [src-20260428-2d177a].
- **Bear:** pricing not disclosed. Salesforce prices sales agents on qualified leads or booked orders [src-20260909-c1900d], directly in its path.
- **What this means:** revenue-side agents are easier to sell on value, but attribution is hard to audit.

### 3.7 Omilia (voice customer service; vertical)
- **What it does:** voice AI for contact centers and drive-throughs. Uses simpler non-LLM tools for simple intents ("bazooka ... knife") [src-20260806-53e2bf].
- **Money:** $67M Series B led by Expedition [src-20260806-53e2bf].
- **Buyers:** Capital One, Discover, RBC, the UK Department for Work and Pensions (DWP), PSEG, Taco Bell in 1,000+ outlets [src-20260806-53e2bf].
- **Claims (Omilia):** ARR $60M, up 10x; about 500 staff [src-20260806-53e2bf].
- **Bear:** CX voice is where the labs and Sierra compete hardest, and Deutsche Telekom calls it "commoditized" [src-20260727-3b21a8]. The article reports a disputed Taco Bell incident [src-20260806-53e2bf].
- **What this means:** the most revenue disclosed among the picks, in the most crowded lane.

### 3.8 Ema (horizontal orchestration; HR, IT, finance)
- **What it does:** "AI employees" made of teams of agents for HR, finance and support; runs in the customer's cloud, even fully disconnected ("air-gapped") [src-20261025-7ef133].
- **Money:** $77M Series B led by Creaegis; $140M total [src-20260930-9ee545].
- **Buyers:** NTT DATA, Hitachi, ADP, PwC, Google, KPMG, Wipro, Microsoft [src-20260930-9ee545].
- **Claims (Ema):** bookings over $150M; revenue up 50x in two years; 1M+ users; prices by completed tasks and outcomes; gross margin "close to 80%" (CEO) [src-20260930-9ee545]. Wipro HR went from 1,000 people to 550, a 45% cut (founder) [src-20261025-7ef133]. Sells with PwC and KPMG [src-20261025-7ef133].
- **Bear:** source is a trade site summarizing the company; many named "customers" are also IT-services partners [inference]. Horizontal layer faces lab and platform absorption (Q7).
- **What this means:** the strongest horizontal traction claims in the repo. Test bookings against revenue and renewal.

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
- **What this means:** the best evidence for the "work context" thesis, still company-reported.

### 3.11 Benchmarks: Sierra, Decagon and the CX leaders
- **Sierra.** $100M ARR in seven quarters, $150M in eight [src-20260309-78d5a1]; $950M raise at over $15B [src-20260504-c9d184]. Safelite: under $2 per transaction vs $7.50 to $9 human, 4-year contract with industry exclusivity, "80% likely to renew" [src-20260710-37d40b]. Deutsche Telekom ranks it first [src-20260727-3b21a8]. It lost a European fintech deal to Decagon on German voice quality; its business cases looked "too good to be true" to that buyer [src-20260708-a5fc76]. Customers automate 70% to 90% of cases per one source [src-20260310-ad2c26]; buyers report about 60% to 65% [src-20260318-033caf] [src-20260717-eb6872].
- **Decagon.** Over $100M ARR; about 90% of workloads on fine-tuned open models [src-20261013-d7909a]; hired a bank [src-20261013-6d4b75]. "Decagon is the worse Sierra" (Deutsche Telekom) [src-20260727-3b21a8]. Used at Airbnb [src-20261009-44e09b].
- **Intercom Fin, now Salesforce.** 30,000+ customers, 76% average resolution [src-20260910-2cf2eb]; 30% to 40% at Smartly.io [src-20260326-b3dd2d].
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
