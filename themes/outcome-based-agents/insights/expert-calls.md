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

## AlphaSense transcripts filed (2026-10-25)
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
| src-20260811-852c57 | Product Management Leader, UnitedHealth Group (Pace customer) | 2026-08-11 | 240294 | Pace use, spend, pricing, BPO insourcing (Q10) |

Still open after these: no third-party outcome auditor named in any call; no per-resolution price for Decagon; Fin price point not stated by the customer; no Now Assist production share; no Duvo customer call; Sycamore has no AlphaSense coverage.

### Backlog: AlphaSense IDs not yet downloaded (from the 2026-10-25 search log)
247531 Ascot MS E7 agents; 223713 Cresta FDE; 235110 Cognizant automation head; 234187 PwC Maisa; 248195 ex-Palantir FDE economics; 240921 ex-Accenture IT services margins; 258221 Atlassian on Salesforce AI; 230791 Northeastern ServiceNow; 257399 Workday partner; 212668 ex-RYZE EVP (Pace); 206963 Accelerant FurtherAI; 260188 Airbnb AI agents; 258750 Walmart customer care; 220590 e-grocery on Duvo; 227928 Duvo cofounder Oct; 164829 Zendesk VP on Fin; 192831 Hitachi on Ema; 172553 SOPHiA on Kestra; 222882 Skan AI director; 218503 Skan AI exec; 223379 Avant on Didero/Magentic; 165187 Novilla on Didero; 189357 IKEA on Magentic; 173450 Justworks on Actively; 163248 DOCS Dermatology on Amperos; 110763 Discover on Omilia; 245344 Crescendo on Zendesk; 244213 Accenture VP on UiPath agentic; 233629 Liberty Mutual legal AI.
No-docid titles: Former Head of Sales Americas Intercom on outcome pricing (08 Jun 26); Decagon: Former CPO Chime (16 Aug 26), Notion Head of Business Technology (13 Aug 26), Hunter Douglas CX lead, Pocket FM Head of AI.
Sycamore: no AlphaSense coverage found.
