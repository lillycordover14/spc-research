# Expert calls: targets, question guide, search strings

Updated 2026-10-25 by grokbot. Builds on `expert-call-guide.md` (archetype questions and the filing steps). This file adds named public candidates, sharper questions tied to the five worlds and the outcome-pricing test, and search strings for AlphaSense and Tegus.

Sourcing rule: a name tagged with a source id is in a filed source. A name tagged [public: web, not filed] came from a public web search on 2026-10-25 (press pages, conference bios, LinkedIn titles). Check the current title before outreach. Public information only, no contact details.

## Target profiles and named public candidates

### P1. Fortune 500 head of AI or automation, agents in production (Q1-Q5, Q13)
| Candidate | Company | Why | Source |
|---|---|---|---|
| Prem Natarajan, EVP, Chief Scientist, Head of Enterprise AI | Capital One | Built an in-house multi-agent platform (Chat Concierge) on open models, a world 3 data point | [public: web, not filed]; platform in [src-20260416-e6896d] |
| Rashmi Shetty | Capital One | Presented Chat Concierge architecture | [src-20260416-e6896d] |
| Praveen Neppalli Naga, CTO | Uber | Quoted in Sierra's $950M coverage as a Sierra buyer | [src-20260504-c9d184] |
| Chime CX leadership (name n/v) | Chime | Decagon reference: 70%+ chat resolution, 60% cost cut | [src-20261025-22dc67] |
| Palomar COO (named in case study) | Palomar | Pace resolves 90%+ of cases without a human touch | [src-20261025-c77b6e] |
| Prudential operations lead (name n/v) | Prudential | Selected Pace for insurance operations | [src-20261025-58fd6b] |
| BMO AI lead (name n/v) | BMO | 500-person Workday pilot to 55,000 employees in a month | [src-20260827-79de17] |
| HP Frontier program owner (name n/v) | HP | Scaling OpenAI Frontier after pilots that started in Feb 2026, a world 1 data point | [src-20260628-930f51] |
| Wawa CIO (AlphaSense call already filed) | Wawa | ITSM agents, prior transcript to build on | [src-20260402-8d84cb] |

### P2. SI agentic practice leads (Q5, Q6, Q11, Q14)
| Candidate | Firm | Source |
|---|---|---|
| Stuart Scotis, Global Agentic AI Leader | Deloitte | [public: web, not filed] |
| Jagmohan Singh Kohli; Dhananjay R. | Deloitte (agentic / Zora AI) | [public: web, not filed]; Zora and FDE practice in [src-20261009-4138dc] |
| Harsh Kar, MD, Agentic Lead Global | Accenture | [public: web, not filed] |
| Babak Hodjat, Chief AI Officer | Cognizant | [public: web, not filed] |
| Pandiyan Elumalai | Cognizant | [public: web, not filed] |
| Cognizant ContextFabric / context-engineering lead (name n/v) | Cognizant | Workfabric channel, 1,000 context engineers [src-20250829-31a67a] |
| Cognizant Gemini Frontier Capability Group lead (name n/v) | Cognizant | 18,000 engineers [src-20261022-d5ad54] |
| Manish Goyal | IBM Consulting | [public: web, not filed]; GenAI is about half of IBM Consulting signings [src-20260722-1275ae] |
| DXC OASIS lead (name n/v) | DXC | LangSmith across 125 customer environments [src-20261013-1dcd15] |

### P3. Customers and formers: Sycamore, Duvo, Workfabric (Q7, Q11, Q15)
| Candidate | Relationship | Source |
|---|---|---|
| Gordon MacPherson, Group Productivity Director | Morrisons, Duvo customer | [src-20261014-fb6b7e] |
| Notino, Holland & Barrett, Boden, Allegro ops leads (names n/v) | Duvo customers | [src-20261014-fb6b7e] |
| Rohlik Group supply-chain planners | Duvo sister company (same founder, Tomas Cupr) | [src-20261014-fb6b7e] |
| Sycamore design partners: unnamed Fortune 500s; Dell (funder and partner) | Sycamore | [src-20260330-8d6266] [src-20260929-334bba] |
| Cognizant context engineers using ContextFabric | Workfabric channel users | [src-20250829-31a67a] |
| Formers: ex-Atlassian staff who followed Sri Viswanath; ex-Infosys staff near Rohan Murty | Formers | find via Tegus/AlphaSense, names n/v |

### P4 (added). Vertical-outcome buyers outside CX (Q10, Q11)
Siemens and CCEP (Magentic) [src-20260923-47e348]; Footprint (Didero) [src-20260213-3c647d]; Ramp (Actively) [src-20260428-2d177a]; Cursor, Ramp, Tishman Speyer, Clay (Crosby) [src-20260331-50e583] [src-20261025-474366]; Ryze Claim Solutions (Pace) [src-20261025-9f5479]. Use these to test the outcome-pricing test outside CX, where we have no renewal evidence.

## Question guide per profile

Every call should close three gaps: (a) which world wins in this account, (b) does any outcome contract pass the test (countable unit, customer agrees with the count, renewed at least once), (c) margin after inference and FDE.

### P1. F500 head of AI
1. (Q1) Count agents in production by function. What is your definition of production (traffic share, autonomy, SLA)?
2. (Q2, test: unit) For each outcome-priced vendor, what is the unit and its price? Who counts it?
3. (Q2, test: verification and auditor) Have you ever disputed a count? Do you audit the vendor's resolution log, or does a third party? (We found no third-party auditor in public sources, see [src-20261025-24844b] [src-20260710-3b577b].)
4. (Q2, test: renewal) Did any outcome contract renew? At the same unit price? Did you move to a cap, floor or prepaid pool? ([src-20250918-7e3ad0] burn-down allotments.)
5. (Q3) What failed in production? Any incident like PocketOS [src-20260428-8baab9]? What did it cost, and who paid under the contract?
6. (Q4) Which budget line paid: IT software, BPO, or headcount? Did the BPO contract shrink?
7. (Q5, worlds) Map your stack to worlds 1 to 5: lab platform, system of record agent, in-house, SI-built, vertical app. Which will grow in 2027?
8. (Q6) What did OpenAI Frontier or Claude Managed Agents replace in your plans?
9. (Q8) Do Agentforce, Now Assist or Joule win by default because they hold the data? What would make you go around them?
10. (Q16) Would you sign a share-of-savings deal? What would kill one?

### P2. SI practice lead
1. (Q1, Q14) Share of agentic engagements in production vs pilot, and the average number of agents per production client.
2. (Q5, worlds) Platform mix in the last 10 deals: lab, system of record, hyperscaler, vertical app, custom. How has it moved since the spring launches?
3. (Q11) Revenue split per engagement: licences vs your people vs inference. How many FDE hours per agent?
4. (Q2) How many clients ask for outcome terms from you? Write one down: unit, price, cap, verification, termination.
5. (Q2, auditor) Who verifies outcomes in your deals? Does the SI act as the auditor? Is that a business?
6. (Q3) Top three reasons agents get pulled. Gartner says 40% get canceled [src-20250625-8a6cff]; is that your number?
7. (Q9, Q10) Which startups appear in client stacks and which got ripped out? Sycamore, Duvo, Workfabric, Decagon, Sierra, Ema?
8. (Q12) Which vendors would you buy or partner with exclusively (Cognizant and Workfabric [src-20250829-31a67a])?
9. (Q5) Where do lab and hyperscaler FDE teams (AWS $1B [src-20260730-e4cc74]) compete with you?

### P3. Sycamore, Duvo, Workfabric customer or former
1. (Q15) Why did you buy, and what did it replace: consultants, BPO, RPA, in-house team?
2. (Q2, test) What is the contract unit (seat, task, platform fee, outcome)? Any outcome clause?
3. (Q15) What outcome moved, by how much, and who measured it (for example Notino 70 to 15 days [src-20261014-fb6b7e])?
4. (Q11) How much of go-live was product vs vendor engineers on site? Is it shrinking?
5. (Q7) What context does the product learn? Who owns it if you leave? Could OpenAI Frontier or Gemini Enterprise plus an SI rebuild it?
6. (Q8) Does it sit on top of SAP, Salesforce or ServiceNow, or replace a module?
7. (Q15) Renewal intent, expansion plans, and what would make you churn.
8. Formers only: pipeline quality, win rate vs labs and incumbents, gross margin after inference, top churn reason.

## AlphaSense and Tegus search strings

Paste as-is. AlphaSense supports Boolean and NEAR/n; Tegus search is simpler, so use the shorter line.

| Gap (question) | AlphaSense | Tegus |
|---|---|---|
| Outcome contract terms and renewal (Q2) | ("outcome-based" OR "per resolution" OR "pay per outcome" OR "share of savings") NEAR/10 (agent OR "AI agent") AND (renew* OR contract OR cap OR floor) | outcome-based pricing AI agent renewal |
| Third-party outcome verification (Q2) | ("resolution rate" OR "verified resolution" OR "automated resolution") NEAR/10 (audit* OR dispute* OR verif*) | resolution rate audit dispute AI agent |
| Agents in production at F500 (Q1, Q13) | ("agents in production" OR "agentic AI in production") AND ("Fortune 500" OR CIO OR "head of AI") | agents in production CIO |
| Failure incidents and liability (Q3) | ("AI agent" OR agentic) NEAR/10 (incident OR outage OR "deleted" OR liability OR indemnif*) | AI agent incident liability |
| Budget source, BPO displacement (Q4) | ("AI agent" OR agentic) NEAR/15 (BPO OR outsourcing OR headcount) NEAR/15 (budget OR replace*) | AI agents replacing BPO contract |
| Harness build vs buy (Q5, Q6) | ("Claude Managed Agents" OR "OpenAI Frontier" OR "Agents SDK" OR "Gemini Enterprise") AND (replace* OR evaluat* OR "build vs buy") | OpenAI Frontier enterprise evaluation |
| Systems of record defense (Q8) | (Agentforce OR "Now Assist" OR Joule OR "Workday agents") NEAR/10 (displace* OR renew* OR "per resolution" OR pricing) | Agentforce pricing customer |
| SI economics (Q11, Q14) | (Deloitte OR Accenture OR Cognizant OR "IBM Consulting" OR Infosys OR TCS) NEAR/15 ("agentic" OR "forward deployed") NEAR/15 (margin OR pricing OR "deal size") | agentic AI consulting deal size margin |
| Unit economics after inference (Q11) | ("gross margin" NEAR/10 inference) AND ("AI agent" OR agentic) | AI agent gross margin inference cost |
| Sycamore (Q15) | "Sycamore" NEAR/5 (agent OR Viswanath OR Lightspeed) | Sycamore AI agents |
| Duvo (Q15) | "Duvo" AND (Morrisons OR Notino OR Rohlik OR Balderton) | Duvo AI |
| Workfabric (Q15) | (Workfabric OR ContextFabric) AND (Cognizant OR Murty) | Workfabric ContextFabric |
| CX vendors renewal (Q10) | (Sierra OR Decagon OR "Fin" OR Intercom) NEAR/10 (renew* OR churn OR "price increase" OR "per resolution") | Decagon Sierra customer renewal |
| Exits (Q12) | (acqui* OR "M&A") NEAR/10 ("AI agent" OR agentic) AND (Salesforce OR ServiceNow OR SAP OR Workday OR NiCE OR Genesys) | acquisition AI agent startup ServiceNow |

## Priority order for the 2026-10-28/29 readout
1. One SI lead (P2) on outcome terms and platform mix. Closes Q2 and Q5 fastest.
2. One Duvo customer (MacPherson or Notino) on Q15 and the outcome test.
3. One F500 head of AI with an outcome-priced CX vendor (Chime-style) on renewal and verification.

## AlphaSense batch 4 filed (2026-10-28, 11 calls plus 3 reports)
Experts are anonymous; role as given by AlphaSense. Date is interview or publication date. Docid is the EC number in the PDF name.

| Source | Expert role, company | Interview | Docid | Gaps it closes |
|---|---|---|---|---|
| src-20260930-124dc3 | VP Client Services, TTEC Holdings (Conduent competitor; AI-run interview) | 2026-09-30 | 256200 | AI BPO price compression, FTE to consumption billing, Conduent agentic pitch (Q2, Q4, Q14) |
| src-20260922-5e723f | Former Principal PM Growth, Apollo.io (Clay competitor) | 2026-09-22 | 253417 | Clay as GTM orchestration; Claude as competitor; AI SDR view (Q6, Q9, Q10) |
| src-20260811-a0aa1e | Head of Strategic Partnerships, Accelerant Holdings (Pace customer; AI-run interview) | 2026-08-11 | 240396 | Second Pace buyer: usage with a floor, ROI open, commoditization risk (Q2, Q10) |
| src-20260716-88dbe4 | Global Head of Enterprise Sales and Merchant Acquisition, PayPal (Zip and Omnea customer) | 2026-07-16 | 232624 | Procurement agents on top of the ERP (Q7, Q8, Q10) |
| src-20260608-5e7d7e | VP Operations, Health Prime (RCM services; former R1 RCM) | 2026-06-08 | 220193 | Incumbent services firm adopting agents; Epic gatekeeping; savings ceiling (Q3, Q4, Q10) |
| src-20260217-2cccb9 | Co-Founder, Enigma; former Senior Manager of Procurement, Personio | 2026-02-17 | 191104 | Zip, Omnea, Pivot, Levelpath evaluated; built in-house (Q8, Q10) |
| src-20250611-a24e31 | COO, Deel (micro1 customer) | 2025-06-11 | 137375 | AI recruiting buyer; BPO challengers per hour (Q2, Q4, Q10) |
| src-20250507-e13bdd | Former Strategic Advisor and GTM Advisor, 11x | 2025-05-07 | 132171 | AI SDR churn 80% to 90%; Nooks spend (Q3, Q10) |
| src-20250313-c22032 | Sourcing Manager, Honeywell (SAP Ariba customer) | 2025-03-13 | 124193 | In-house procurement news agent; low relevance (Q5) |
| src-20241031-1d55b6 | Former Head of Engineering, 11x | 2024-10-31 | 109190 | 11x vs Artisan; break clauses (Q10) |
| src-20240919-474182 | Founding Sales Executive, Thoughtful AI | 2024-09-19 | 103988 | RCM agents priced per agent (company view) (Q2, Q10) |

Reports filed in the same batch: UBS "Private 100" src-20261022-c0698e (142 pages); Truist agentic AI primer src-20260428-14f0c8 (111 pages); Oppenheimer SailPoint initiation src-20261007-54b3ff (36 pages, brief note for this theme).

Duplicate: docid 235321 (Crescendo, former Director of Partner Services) is already filed as src-20260724-865e53 (table below) and was not filed again. None of the 15 batch 4 docids was in the backlog list at the end of this file, so nothing was removed from it.

Still open after batch 4: no current enterprise buyer of an AI SDR; no Thoughtful AI customer; no Zip or Omnea pricing from a buyer.

## AlphaSense transcripts filed (2026-10-27, 17 calls)
Experts are anonymous; role as given by AlphaSense. Date is interview date. Same link pattern as below.

| Source | Expert role, company | Interview | Docid | Gaps it closes |
|---|---|---|---|---|
| src-20260908-547a69 | Former Forward Deployed Engineer, Palantir | 2026-09-08 | 248195 | FDE pricing inside usage contracts; SI vs Palantir vs OpenAI DeployCo (Q5, Q6, Q14) |
| src-20260904-8886b4 | SVP Infrastructure Operations and Services, Ascot Group (Microsoft E7 buyer) | 2026-09-04 | 247531 | E7 discount, Cowork token spend, Agent 365 maturity (Q4, Q6, Q11) |
| src-20260828-bb2734 | Director, Crescendo (Zendesk partner BPO; AI Interviewer) | 2026-08-28 | 245344 | Zendesk native AI share, seat pricing view (Q8) |
| src-20260825-747be0 | VP Digital Transformation, Accenture (UiPath SI) | 2026-08-25 | 244213 | RPA vs agent run cost, bot to agent ratio (Q11, Q14) |
| src-20260724-b4a442 | Head of Automation and AI Practice Northern Europe, Cognizant | 2026-07-24 | 235110 | BPO displacement size and timeline, token cost (Q4, Q11, Q14) |
| src-20260618-f36dc6 | Head of Forward Deployed Engineering, Cresta | 2026-06-18 | 223713 | Own harness vs LangChain, eval effort, per-minute and outcome pricing (Q2, Q5) |
| src-20260617-937cc1 | CEO, avant.ai (procurement BPO, Pavus customer) | 2026-06-17 | 223379 | Didero, Pavus, Magentic, Pactum scored from RFPs; Didero pricing (Q2, Q10) |
| src-20260616-48f4c6 | Director, Digital Operations and AI Enablement, Skan.AI | 2026-06-16 | 222882 | Process intelligence vs labs (Q6, Q7) |
| src-20260518-714b0a | Former CPO, Chime (Decagon and Sierra customer) | 2026-05-18 | 215049 | Multi-vendor router, cost per case ceiling (Q5, Q7, Q10) |
| src-20260515-de88a1 | Head of Business Technology, Notion (Decagon customer) | 2026-05-15 | 214749 | Decagon pricing unit and spend, RFP scores, BPO displacement (Q2, Q4, Q10) |
| src-20260310-e66bf3 | Former Head of Sales Americas, Intercom | 2026-03-10 | 197134 | Fin resolution definition, cost control, Sierra paid POC (Q2, Q11) |
| src-20260224-8c72f4 | Digital Solutions Leader, Hitachi Digital Services (Ema customer) | 2026-02-24 | 192831 | Horizontal platform spend and expansion cap (Q5, Q9) |
| src-20260209-7ec831 | Head of Digital Architecture, Supply Chain Development, IKEA (Magentic customer) | 2026-02-09 | 189357 | Magentic pricing, savings, adoption (Q2, Q10) |
| src-20251126-6d86c8 | Former VP of Sales, Justworks (Actively customer) | 2025-11-26 | 173450 | Actively ROI and switching cost (Q9) |
| src-20251024-112e5e | Chief of Staff and Head of Operations, Novilla Pharmaceuticals (Didero customer) | 2025-10-24 | 165187 | Didero spend vs replaced consultant (Q4, Q10) |
| src-20251016-371c9b | CIO, DOCS Dermatology (Amperos customer) | 2025-10-16 | 163248 | RCM agent pricing, liability limit (Q2, Q3) |
| src-20241114-f0ab80 | VP Consumer Banking and Lending, Discover (Omilia customer) | 2024-11-14 | 110763 | Contact center AI license cost, containment (Q1, Q3) |

Still open after these: still no third-party outcome auditor; Decagon price per conversation still not stated (Notion gives spend, not unit price); Sierra price per resolution still from one buyer only.

## AlphaSense transcripts filed (2026-10-25, 20 calls)
Experts are anonymous; role as given by AlphaSense. Date is interview date. Links: https://research.alpha-sense.com/search?sort=RELEVANCE&order=DESC&docid=EC-1000000-<ID>

| Source | Expert role, company | Interview | Docid | Gaps it closes |
|---|---|---|---|---|
| src-20260710-37d40b | VP Client Sales and Support, Safelite AutoGlass (Sierra customer) | 2026-07-10 | 230822 | Sierra outcome definition, price per transaction, value split, term, exclusivity, renewal intent (Q2, Q11) |
| src-20260708-a5fc76 | Partner Director DACH, DRUID AI (RFP decision maker) | 2026-07-08 | 229598 | Sierra monthly price and implementation fee; outcome pricing as a deal loss (Q2) |
| src-20260318-033caf | Head of Context Engineering, Workfabric AI (Sierra customer) | 2026-03-18 | 199270 | What counts as a resolution; buyer-side verification (Q2, Q15) |
| src-20260717-eb6872 | Senior Director, Innovaccer (Sierra customer) | 2026-07-17 | 232902 | Sierra resolution rate, spend, buyer audit method (Q1, Q2) |
| src-20260727-3b21a8 | Senior Vice President, Deutsche Telekom (Sierra and Decagon customer) | 2026-07-27 | 236058 | Sierra vs Decagon; vendor consolidation (Q9, Q13) |
| src-20260326-b3dd2d | Senior Director of Product and Engineering Operations, Smartly.io (Fin customer) | 2026-03-26 | 201422 | Fin real-world resolution rate and pricing basis (Q1, Q2) |
| src-20260724-865e53 | Former Director of Partner Services, Crescendo | 2026-07-24 | 235321 | BPO outcome pricing in practice, margin impact, bear case (Q2, Q11, Q16) |
| src-20250627-297f7b | Nordic Head of Automation & AI Practice, Cognizant | 2025-06-27 | 140373 | SI deal economics, BPO displacement, STP definition (Q11, Q14) |
| src-20251006-b80311 | Head Of AI, Cloud Strategy And Sales, EMEA, Infosys | 2025-10-06 | 160623 | SI pricing models, outcome pricing risk (Q5, Q14) |
| src-20260804-3aa89c | Chief AI Officer, OSF Digital (Salesforce SI) | 2026-08-04 | 238432 | Agentforce production rate (Q1, Q8) |
| src-20260911-0742fb | National Executive Director, KPMG (ServiceNow partner) | 2026-09-11 | 249859 | Now Assist seat contraction and pricing (Q8) |
| src-20261017-72ec30 | Managing Director and Chief AI Architect, Accenture | 2026-10-17 | 263013 | Who builds the harness in production; model routing (Q5, Q6) |
| src-20260416-1a8cca | Co-Founder, Duvo | 2026-04-16 | 206485 | Duvo pricing and ACV (Q2, Q15) |
| src-20251023-28432e | Vice President, Enterprise Data and Analytics, Zendesk | 2025-10-23 | 164829 | Zendesk and Fin per-resolution headline prices (Q2) |
| src-20260508-386718 | Former Executive Vice President of Operations, RYZE Claim Solutions (Pace customer) | 2026-05-08 | 212668 | Pace pricing (Q2, Q10) |
| src-20260609-4b024f | Director of Business Process and Excellence, European e-grocery retailer (Duvo customer) | 2026-06-09 | 220590 | First Duvo customer: pricing, spend, FTEs, UiPath displacement (Q15) |
| src-20260701-3b0c17 | Co-Founder, Duvo AI | 2026-07-01 | 227928 | Duvo per-execution pricing (Q2) |
| src-20261006-b21c7a | Senior Director, Strategy and Operations, Walmart (Sierra customer) | 2026-10-06 | 258750 | Personal-agent disintermediation risk (Q7) |
| src-20261009-44e09b | Go-To-Market and Operations, New Verticals, Airbnb (Decagon customer) | 2026-10-09 | 260188 | Build plus buy in CX (Q5) |
| src-20260811-852c57 | Product Management Leader, UnitedHealth Group (Pace customer) | 2026-08-11 | 240294 | Pace use, spend, pricing, BPO insourcing (Q10) |

Still open after these: no third-party outcome auditor named in any call; no per-resolution price for Decagon; Fin price point not stated by the customer; no Now Assist production share; Sycamore has no AlphaSense coverage.

### Backlog: AlphaSense IDs not yet downloaded (from the 2026-10-25 search log)
234187 PwC Maisa; 240921 ex-Accenture IT services margins; 258221 Atlassian on Salesforce AI; 230791 Northeastern ServiceNow; 257399 Workday partner; 206963 Accelerant FurtherAI; 172553 SOPHiA on Kestra; 218503 Skan AI exec; 233629 Liberty Mutual legal AI.
No-docid titles: Hunter Douglas CX lead, Pocket FM Head of AI. Filed 2026-10-27 (docids found): Intercom Head of Sales Americas (197134), Decagon: Former CPO Chime (215049), Notion Head of Business Technology (214749).
Sycamore: no AlphaSense coverage found.
