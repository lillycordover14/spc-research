# OBA theme memo: example companies audit (2026-10-29, grokbot; updated for v6 after AI-Native Production QA)

Requested by Lilly ("make sure all outcome-based agents as getting very broad so do a double check there"). Every name on the memo's Example companies lines (v4) was checked against its company card and filed sources.

**v6 changes.** Production QA cut Kestra and n8n (general workflow platforms), Workfabric AI (work context, like Skan AI and Mimica), ElevenLabs (build-your-own agent platform) and Zolvo (humans approve its matches, no traction on its source). Relevance AI stays.

**Test.** Keep a name only if (a) it sells an AI agent that does a whole job or task end to end, not a copilot, chatbot builder, analytics tool, model or general infrastructure, and (b) it fits the category. For A to D, keep only names actually building or selling agents or agentic orchestration; tools around agents (evals, monitoring, security, billing, compute) count as adjacent. Outcome or usage pricing tied to completed work is a strong signal, not a requirement. Where the filed evidence is too thin to decide, the name is cut and marked uncertain. Company statements are company claims. Body text may still cite cut names as evidence; only the example lists changed.

**Counts (v4 to v5 to v6).**
- A. Labs and Hyperscalers / Agent Infrastructure: 19 to 7 to 7
- B. Systems of Record / Incumbent Platforms: 9 to 7 to 7
- C. Enterprises Building Their Own / Horizontal Orchestration and Work Context: 16 to 8 to 5
- D. Systems Integrators and BPOs / AI Services and AI-Native Outsourcers: 17 to 10 to 10
- E1. Front Office: Customer Service and Sales: 19 to 14 to 13
- E2. Back-Office Operations: Finance, Accounting and Procurement: 25 to 16 to 15
- E3. Regulated Services: Healthcare, Insurance, Legal and Life Sciences: 26 to 19 to 19
- Total: 131 to 81 to 76

## A. Labs and Hyperscalers / Agent Infrastructure

| Company | Decision | Reason | Source |
|---|---|---|---|
| OpenAI | Keep | Sells agents and agent platforms (Agents API, Presence) on top of its models | src-20260910-014b24 |
| Anthropic | Keep | Sells Claude agents and a managed agent harness (Agent SDK, managed sessions) | src-20260408-e5d37b |
| Google | Keep | Sells Gemini Enterprise, the Agent Platform and ADK for building and running agents | src-20260422-72407e |
| Microsoft | Keep | Sells Copilot Studio agents and Agent 365 to run and govern agents | src-20260501-fc687c |
| Amazon Web Services | Keep | Ships autonomous frontier agents (Kiro, Security Agent, DevOps Agent) and AgentCore | src-20251202-2f7e92 |
| LangChain | Keep | Agent framework (LangChain, LangGraph) plus LangSmith for deploying agents | src-20261022-ae18f2 |
| CopilotKit | Keep | Agent-user interaction framework (AG-UI) used to build agents into products | src-20260505-826992 |
| Coval | Cut | Evaluation and monitoring for voice agents; tooling around agents, not an agent or orchestration | src-20260624-2cae61 |
| Dash0 | Cut | Observability platform first; its AI SRE agent is a feature of a general monitoring product | src-20260323-e76c06 |
| Daytona | Cut | Sandbox compute for agents; general infrastructure, not an agent or orchestration | src-20261023-3f4b4a |
| Flexprice | Cut | Open-source usage billing for AI companies; adjacent | src-20260802-db6422 |
| InsightFinder | Cut | Reliability monitoring for agents and infrastructure; tooling, not an agent | src-20260416-dfa630 |
| Natural | Cut | Payment rails for agents; adjacent | src-20260720-e50556 |
| Raindrop | Cut | Production monitoring for agent failures; tooling, not an agent | src-20260917-29a2db |
| Rein | Cut | Runtime security for agents; tooling, not an agent | src-20261008-418b1c |
| Runlayer | Cut | Governance control layer over employees' agent use; security and policy, not orchestration of work | src-20260624-0c6e18 |
| Tsuga | Cut | General observability priced per GB; adjacent | src-20260623-e97988 |
| Saviynt | Cut | Identity security platform extended to agent identities; adjacent | src-20261007-54b3ff |
| Modal | Cut (uncertain) | General compute; only filed evidence is a UBS profile list, too thin | src-20261022-c0698e |

## B. Systems of Record / Incumbent Platforms

| Company | Decision | Reason | Source |
|---|---|---|---|
| Salesforce | Keep | Sells Agentforce agents on its own data platform | src-20260826-580137 |
| ServiceNow | Keep | Sells AI agents and AI Control Tower orchestration on its platform | src-20260507-e6c2cd |
| SAP | Keep | Sells Joule agents on its ERP | src-20261021-551046 |
| Oracle | Keep | Sells Fusion Agentic Applications and AI Agent Studio | src-20261021-a5c3e0 |
| Workday | Keep | Sells Workday agents on Flex Credits and is buying C1.ai | src-20261013-7962db |
| Zendesk | Keep | Sells AI agents billed per automated resolution | src-20250806-3921b6 |
| HubSpot | Keep | Sells Breeze agents priced per resolution and per lead | src-20260413-63104e |
| Guidewire | Cut | Only filed evidence is a strategic investment in Sixfold; no Guidewire agent product in our sources | src-20260129-3fadee |
| Epic | Cut (uncertain) | System of record that limits outside AI; no filed source on Epic selling its own agents | src-20260608-5e7d7e |

## C. Enterprises Building Their Own / Horizontal Orchestration and Work Context

| Company | Decision | Reason | Source |
|---|---|---|---|
| Ema | Keep | Teams of agents running HR, IT and finance processes, priced on completed tasks | src-20260930-9ee545 |
| Kestra | Cut (v6) | General workflow platform; orchestrates data and business workflows, with agent workflows as one type | src-20260331-83a5c4 |
| Duvo | Keep | Agents execute approved workflows across ERPs and portals, priced per agent run | src-20260609-4b024f |
| Sycamore | Keep | Enterprise OS that builds, deploys and orchestrates autonomous agents | src-20260404-029771 |
| Workfabric AI | Cut (v6) | Coordinates work context (employee twins), same reasoning as Skan AI and Mimica; still cited in the body as the Sierra customer | src-20261023-21a6d6 |
| Relevance AI | Keep | Platform to build and run teams of agents across functions | src-20250506-6ff4ce |
| n8n | Cut (v6) | General workflow automation platform; a Duvo customer uses it for deterministic flows | src-20260609-4b024f |
| UiPath | Keep | Incumbent repositioned as agentic automation and orchestration | src-20241218-3282c7 |
| Airia | Cut (uncertain) | Only named as a Sycamore competitor in TechCrunch; no filed source on its product | src-20260330-8d6266 |
| Maisa AI | Cut (uncertain) | Only named as a Sycamore competitor in TechCrunch; no filed source on its product | src-20260330-8d6266 |
| Mimica | Cut | Task mining that captures work to train agents; work context, does not run the work | src-20250924-c1a4cf |
| Skan AI | Cut | Process intelligence that feeds context to agents; does not run the work (still cited in the body) | src-20260812-4cb1fc |
| Unframe | Cut (uncertain) | 'Enterprise AI platform'; source does not say it sells agents that do the work | src-20250403-82b140 |
| Glean | Cut | Enterprise search and assistant first; agents are a feature, copilot-shaped | src-20250610-0a09d0 |
| Workato | Cut (uncertain) | Integration platform; only filed evidence is a UBS profile list | src-20261022-c0698e |
| Celonis | Cut | Process mining; sells context to agents, not agents (still named in the focus) | src-20260501-fc687c |

## D. Systems Integrators and BPOs / AI Services and AI-Native Outsourcers

| Company | Decision | Reason | Source |
|---|---|---|---|
| Accenture | Keep | Agentic AI practice deploying agents for clients; Anthropic and Google partner | src-20260312-73c25c |
| Deloitte | Keep | Cites a library of 1,000+ prebuilt agents in its Gemini Enterprise practice | src-20260422-72407e |
| Cognizant | Keep | Rebuilt a claims BPO account on an agent platform; 18,000 engineers building Gemini agents | src-20250627-297f7b |
| TCS | Keep | Launched ADD AgentHub, an agentic workforce for clinical trials and pharmacovigilance services | src-20261008-ae3125 |
| Teleperformance | Keep | Growth from AI-powered, outcome-based activities; 1,100+ TP.ai projects | src-20260730-4cc420 |
| Conduent | Keep | Pitching an agentic AI product (Sidecar) to remove tier one payer calls | src-20260930-124dc3 |
| Crescendo | Keep | AI-native BPO selling contacts handled by AI on per-contact contracts | src-20260724-865e53 |
| DeepOpinion | Keep | Agentic automation platform running a claims BPO account, priced per task | src-20250627-297f7b |
| Otera | Keep | Insurance agentic automation, Cognizant global partner | src-20260724-b4a442 |
| Distyl AI | Keep | AI-native services firm deploying agents (Google Gemini Enterprise practice partner) | src-20260422-72407e |
| Infosys | Cut | Its AI head says it resells ServiceNow, UiPath, SAP and Oracle rather than its own agents | src-20251006-b80311 |
| KPMG | Cut (uncertain) | Appears as an expert source and Gemini practice name only; no filed agent offering | src-20260422-72407e |
| PwC | Cut (uncertain) | Appears as an Ema customer and partner name only; no filed agent offering | src-20260422-72407e |
| Concentrix | Cut (uncertain) | Filed source covers an impairment and AI-era revenue mix, not an agent offering | src-20260929-4fcfe9 |
| TTEC | Cut | Its own VP says TTEC does not offer the agentic product Conduent pitches | src-20260930-124dc3 |
| RapidCanvas | Cut (uncertain) | 'Managed AI execution' on subscription; source does not show agents doing a finished job | src-20261016-425bfa |
| AuxoAI | Cut (uncertain) | Only a one-line mention as a startup growing AI engineering talent | src-20261022-d5ad54 |

## E1. Front Office: Customer Service and Sales

| Company | Decision | Reason | Source |
|---|---|---|---|
| Sierra | Keep | Customer service agents priced per negotiated outcome (Safelite) | src-20260710-37d40b |
| Decagon | Keep | First-line support agents on chat and email, priced per conversation (Notion) | src-20260515-de88a1 |
| Cresta | Keep | Voice agents that book, rebook and cancel; some outcome charging | src-20260618-f36dc6 |
| Parloa | Keep | Customer service agents; $50M+ ARR | src-20260115-f3635c |
| Lorikeet | Keep | Customer service agents that resolve issues (company release) | src-20250806-000216 |
| Gradient Labs | Keep | Customer service agents for financial services, money back if it does not deliver | src-20250530-b93251 |
| PolyAI | Keep | Voice customer service agents for contact centers | src-20260115-f3635c |
| ElevenLabs | Cut (v6) | ElevenAgents is a build-your-own voice agent platform sold alongside its models and API, the same reason respond.io was cut; an Innovaccer expert calls it not focused on one job | src-20260717-eb6872 |
| Omilia | Keep | Voice-first contact center automation for banks and utilities | src-20260806-53e2bf |
| Actively AI | Keep | Keep rests on the Justworks call: it re-engages closed-lost deals inside Salesforce, users never touch the tool, about $1M of revenue that year | src-20251126-6d86c8 |
| Vida | Keep | Agents billed per verified outcome such as a qualified lead | src-20261008-fb6a3d |
| Rox | Keep | Autonomous sales agents (TechCrunch, sources-based) | src-20260312-b92bcd |
| 11x | Keep | Autonomous AI SDR selling outbound work | src-20241031-1d55b6 |
| Artisan | Keep | Autonomous AI SDR | src-20241031-1d55b6 |
| respond.io | Cut | Conversation inbox platform with AI agent features; chatbot builder | src-20260616-8a0be8 |
| Attention | Cut (uncertain) | Platform running rep workflows; source does not show it doing a finished sales task | src-20260624-c59112 |
| Unify | Cut | Company says reps are 'pulled in'; advisor classes it as a tool wrapping a human rep | src-20250507-e13bdd |
| Clay | Cut | Data enrichment and workflow tool; advisor classes it as a tool wrapping a human rep | src-20250507-e13bdd |
| Nooks | Cut | Dialer that augments human SDRs; copilot | src-20250507-e13bdd |

## E2. Back-Office Operations: Finance, Accounting and Procurement

| Company | Decision | Reason | Source |
|---|---|---|---|
| Adaptive | Keep | Project accounting agents for job costing, AP, billing and payments | src-20260917-e6c847 |
| Basis | Keep | End-to-end agents for accounting, tax and audit work | src-20260224-b6a4eb |
| Definite | Keep | Agents run bank regulatory reporting from ledger to filed report | src-20261023-12e7f6 |
| Elimentary | Keep | Agents running operations for private credit managers | src-20261023-c1d343 |
| Xelix | Keep | Agentic accounts payable processing 115M+ invoices a year | src-20250721-54e512 |
| Zolvo | Cut (v6) | Its YC page says the lender's team still reviews the exceptions, and the page lists no customers or traction | src-20261023-d2a134 |
| Zomma | Keep | Computer-use agents that run transaction alert investigations (AI BPO) | src-20261023-36cc4e |
| Tabs | Keep | Billing and collections agents | src-20250916-6b0cd0 |
| Stuut | Keep | Accounts receivable agents | src-20251120-b7dfc3 |
| Didero | Keep | Agents run day-to-day procurement inside existing systems and email | src-20260212-5fd1e0 |
| Lio | Keep | Agents complete the enterprise procurement process | src-20260305-fefcb3 |
| Magentic | Keep | Procurement and supply-chain agents across ERP data | src-20260917-25441c |
| Walter | Keep | AI employee that enters POs in SAP, Dynamics or Oracle | src-20261023-aee4fa |
| Pactum | Keep | AI-driven supplier negotiation, autonomous or semi-autonomous; no client lets it negotiate without a human in the loop (procurement BPO CEO) | src-20260617-937cc1 |
| HappyRobot | Keep | Logistics agents that negotiate rates, book appointments and collect payments | src-20250903-f1a523 |
| Augment | Keep | Freight agents; customer cut invoice delays 40% | src-20250904-fe3d9b |
| Rillet | Cut | AI-native ERP and ledger; a system of record, not an agent (still cited in the body) | src-20250806-b579d5 |
| Campfire | Cut | AI-native ERP; system of record, not an agent | src-20251015-1d9298 |
| Hebbia | Cut (uncertain) | Research and analytics tool; only filed evidence is a UBS profile list | src-20261022-c0698e |
| Pigment | Cut (uncertain) | Planning software; only filed evidence is a UBS profile list | src-20261022-c0698e |
| Pavus AI | Cut | Contract intelligence modules; does not create POs, per a procurement BPO CEO | src-20260617-937cc1 |
| Levelpath | Cut | Procurement software suite (intake, sourcing, contracts) | src-20250630-c0d572 |
| Omnea | Cut | Procurement intake and supplier management software | src-20260716-88dbe4 |
| Zip | Cut | Procurement intake and orchestration software over the ERP | src-20260716-88dbe4 |
| Pivot | Cut | Procurement intake tool | src-20260217-2cccb9 |

## E3. Regulated Services: Healthcare, Insurance, Legal and Life Sciences

| Company | Decision | Reason | Source |
|---|---|---|---|
| Adonis | Keep | RCM agents that autonomously progress claims to resolution (company claim) | src-20260325-9a969a |
| Amperos Health | Keep | Agentic workforce working denied claims end to end | src-20260422-d6ae9d |
| Candid Health | Keep | Autonomous RCM platform | src-20260722-e6a1e0 |
| GenHealth.ai | Keep | Agents for intake, eligibility, prior auth, billing and denials | src-20261008-50f3eb |
| Procode | Keep | AI surgical coding plus billing companies, contingency priced | src-20260728-5c2f73 |
| Prosper AI | Keep | AI-native healthcare services, part resolution-based pricing | src-20261023-cc2e6e |
| Tennr | Keep | Reads referrals, qualifies them and writes them into the EHR | src-20250618-89929d |
| Assort Health | Keep | Voice agents triage and schedule patient calls | src-20251002-499204 |
| Thoughtful AI | Keep | One custom agent per RCM workflow inside provider systems | src-20240919-474182 |
| Pace | Keep | Agents replacing offshore insurance BPO work | src-20260811-a0aa1e |
| Sixfold | Keep | Underwriting agent embedded in insurer systems | src-20260129-3fadee |
| Reserv | Keep | AI-enabled claims TPA selling claims handling, not seats | src-20241205-4ac3cf |
| Harper | Keep | AI-native commercial insurance brokerage paid on brokerage | src-20260225-3917a2 |
| FurtherAI | Keep | Named as an agentic insurance vendor in Accelerant's evaluation | src-20260811-a0aa1e |
| Notch | Keep | Deploys agents that resolve insurance and regulated ops issues end to end (company claim) | src-20260325-5584af |
| Crosby | Keep | AI-native law firm billing contract review on outcomes | src-20260331-50e583 |
| EvenUp | Keep | Produces demand packages, priced per package | src-20241205-4ac3cf |
| Wordsmith | Keep | Agent inbox that runs in-house legal requests | src-20260603-a6ea11 |
| Edison Scientific | Keep | Kosmos AI scientist agent priced per run | src-20251105-cdfbed |
| Abridge | Cut (uncertain) | Clinical documentation assistant (copilot); only filed evidence is a UBS profile list | src-20261022-c0698e |
| Federato | Cut | Underwriting software platform, not an agent doing the work | src-20251118-a1bc08 |
| ClearRisk AI | Cut | Assists claims adjusters; copilot | src-20260513-fb476a |
| Eudia | Cut | Positions as augmented intelligence that augments lawyers; copilot (still cited in the body) | src-20250213-7eb7f6 |
| Supio | Cut | Legal analysis platform for plaintiff lawyers; tool | src-20250430-935fd7 |
| Harvey | Cut (uncertain) | Legal assistant for lawyers; only filed evidence is a UBS profile list | src-20261022-c0698e |
| Ivo | Cut | Contract intelligence for in-house teams; tool | src-20260120-667118 |

## Uncertain (cut for thin evidence; re-add if a filed source shows an agent doing the work)

Modal, Epic, Airia, Maisa AI, Unframe, Workato, KPMG, PwC, Concentrix, RapidCanvas, AuxoAI, Attention, Hebbia, Pigment, Abridge, Harvey
