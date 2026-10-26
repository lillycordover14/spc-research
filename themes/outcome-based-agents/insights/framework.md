# Framework: how we present this theme and lead expert calls

The point of this page is to make the readout and every expert call answer the same few questions in the same structure, so evidence adds up instead of piling up. Agents: when a source speaks to a cell below, add a bullet with the source id to `evidence-by-question.md` under the matching question number.

## 1. The stack (one row per layer, from `taxonomy.yml`)

| Layer | What it is | Who is there today | Lab absorption risk | What a startup must prove |
|---|---|---|---|---|
| 1. Model labs | Labs' own agent platforms and solution sets | OpenAI, Anthropic, Google, Microsoft, AWS | n/a (they are the absorbers) | n/a, benchmark only |
| 2. Harness / infra | Runtime, tools, memory, evals, permissions | Lab SDKs, LangChain, observability vendors | High | Neutral across models and owns a hard problem (evals, identity, reliability at scale) |
| 3. Orchestration | Many agents across systems, governed | Agentforce, ServiceNow, UiPath, Copilot Studio; Sycamore, Duvo | Medium | Works across systems of record, sells completed workflows, enterprise trust |
| 4. Work context | How work actually happens | Celonis, process/task mining; Workfabric | Low to medium | Data compounds with use, and the vendor keeps the right to use it |
| 5. Vertical outcome | Owns a function, priced per outcome | Sierra, Decagon, function SaaS, BPOs | Medium | Countable outcome, margin after inference, renewals |
| 6. Services | SI practices, AI-native services | Accenture, Deloitte, Cognizant, Infosys | Low | Margin path from people to software |

Fill the "who is there" and "absorption risk" columns with sourced evidence as it lands; the version above is the starting hypothesis.

## 2. The harness question, framed as five possible worlds
Who ends up building and owning the harness for a large enterprise's agents?
1. **The labs.** Every enterprise runs on one or two lab platforms; the harness is a feature. Implication: avoid layers 2 and 3.
2. **Systems of record.** Salesforce, ServiceNow, SAP and Workday each run agents on their own data; orchestration fragments by system. Implication: cross-system orchestration is valuable but hard to sell.
3. **The enterprise itself.** Big companies build internal harnesses on open frameworks; vendors sell components. Implication: harness-infra components win, platforms struggle.
4. **SIs.** Accenture and Deloitte assemble harnesses per client. Implication: services margins, tools that make SIs faster win.
5. **Vertical apps.** Each function buys a complete agent with its own harness. Implication: layer 5 wins, horizontal orchestration loses.

For every source and call, note which world the evidence points to. The readout states which world we believe and why.

### World tally
<!-- one line per source or call, newest first: `<date> <source> -> world N because ... [src-id]` -->
- undated Ema on PMF Show -> world 4 because Ema reaches enterprises through SI partners PwC and KPMG [src-20261025-7ef133]
- 2026-10-23  -> world 1 because Google deploys agents in public sector via its own RISE prototypers and FDEs [src-20261023-5b3495]
- 2026-10-22  -> world 3 because Ramp builds its own agent harness (Laminar) instead of buying [src-20261022-ae18f2]
- 2026-10-22  -> world 4 because Cognizant builds an 18,000-engineer Gemini agent deployment group [src-20261022-d5ad54]
- 2026-10-22  -> world 1 because Google channels agent deployment through Cognizant FDE bench [src-20261022-d5ad54]
- 2026-10-21  -> world 1 because Anthropic ships Claude Duet, a lab-owned always-on work agent [src-20261021-d5280b]
- 2026-10-21  -> world 2 because ServiceNow governs desktop agents through its Control Tower [src-20261021-bf34b8]
- 2026-10-21  -> world 1 because Microsoft ships a CX agent overlay on existing contact centers [src-20261021-e45563]
- 2026-10-21  -> world 1 because Meta pushes Muse business agents and enterprise platform [src-20261021-f65653]
- 2026-10-21 StockAnalysis -> world 2 because SAP keeps the ontology and treats 70+ models as interchangeable inputs [src-20261021-551046]
- 2026-10-20  -> world 4 because Sutherland (BPO) runs FlowX.AI agents on outcome pricing [src-20261020-a21f1d]
- 2026-10-19 AI Engineer Katz -> world 1 because A lab-owned coding agent team says models absorb harness intelligence and the lab-side harness opens the next task frontier [src-20261019-54d838]
- 2026-10-16  -> world 2 because SAP signals outcome-based reset pricing [src-20261016-9f1777]
- 2026-10-13  -> world 4 because DXC runs its own LangChain-based harness (OASIS) for customers' IT operations [src-20261013-1dcd15]
- 2026-10-13 Workday C1.ai -> world 2 because Workday absorbs agent identity and access into its platform [src-20261013-7962db]
- 2026-10-09  -> world 4 because Deloitte builds open-model harness practice with FDEs [src-20261009-4138dc]
- 2026-10-08 a16z Show Matt Garman -> world 3 because AWS FDEs aim to hand evals and agents to customer teams within 45 days [src-20261008-3ac60a]
- 2026-10-08 TCS -> world 4 because TCS takes over a client GCC to run it as an AI Capability Center [src-20261008-ae3125]
- 2026-10-05  -> world 3 because 67% of enterprises expect a hybrid, external or in-house agent control plane (VB Pulse) [src-20261005-66e092]
- 2026-10-05  -> world 4 because Mastek sells AI-built replacements for SaaS as services-as-software [src-20261005-ed6751]
- 2026-10-03  -> world 2 because Oracle embeds native agent orchestration (Fusion Claw) in ERP [src-20261003-10d57c]
- 2026-10-01 SAP TechWolf -> world 2 because SAP buys a work-context layer to own context for agents inside its suite [src-20261001-056aad]
- 2026-09-29 OpenAI DevDay 2026 -> world 1 because OpenAI offers always-on agents plus specialist role agents with identity, positioning itself as the enterprise agent provider, while delegating governance to Microsoft [src-20260929-2fdd0f]
- 2026-09-29  -> world 1 because OpenAI seeds an open-source agent control plane (OpenClaw Enterprise) [src-20260929-247cd8]
- 2026-09-24 Intercom -> world 5 because Intercom sells Fin as an outcome-priced CX agent across helpdesks [src-20260924-93c5ed]
- 2026-09-21 20VC Dines 2026 -> world 4 because UiPath repositions from RPA to orchestration plus process-context capture ('map and rails') [src-20260921-f28021]
- 2026-09-18 Dreamforce 2026 All-In -> world 2 because Salesforce exposes platform headless and pushes Slack as agent workspace [src-20260918-ddaf3a]
- 2026-09-16 Gartner -> world 2 because Gartner says enterprises mostly use embedded AI from incumbent software providers [src-20260916-b894eb]
- 2026-09-15 Sequoia Levie -> world 5 because Levie argues vertical applied players win async background agent work that horizontal products cannot render well [src-20260915-68c6ef]
- 2026-09-10 Oracle Q1 FY27 call -> world 2 because Oracle sells agents native to Fusion and argues suites beat one-off agents [src-20260910-fa41de]
- 2026-09-10 OpenAI Agents API -> world 1 because OpenAI gives away its production harness to developers, making the harness a lab feature [src-20260910-014b24]
- 2026-09-10 Salesforce completes Fin -> world 2 because the leading per-resolution CX agent was absorbed by the largest system of record [src-20260910-2cf2eb]
- 2026-09-09 Salesforce GS Communacopia (AlphaSense) -> world 2 because Salesforce runs agents on its own CRM data and Slack context, partnering with Anthropic for models and orchestrating Fin and Piper [src-20260909-c1900d]
- 2026-09-08 Six Five Benioff -> world 1 because Salesforce concedes the front end to lab surfaces like Claude Cowork and positions itself as headless data and workflow underneath [src-20260908-2d6352]
- 2026-09-03 StockAnalysis -> world 2 because UiPath sells Maestro orchestration with FDEs on its own platform [src-20260903-1f1484]
- 2026-09-02 Genesys -> world 5 because Genesys sells its own CX agents and partners Sierra on its platform [src-20260902-b6edda]
- 2026-08-27 StockAnalysis -> world 2 because Workday sells native agents and acquired agent startups inside its HR system of record [src-20260827-79de17]
- 2026-08-26 The Motley Fool -> world 2 because Salesforce runs agents on its own CRM and Data 360 and moves 2,000 customers into production in a quarter [src-20260826-580137]
- 2026-08-25  -> world 3 because 32% of enterprises now build software in-house with coding agents instead of buying (McKinsey) [src-20260825-e5c5c1]
- 2026-08-13 Sequoia Chase harness -> world 2 because LangChain argues harness, context and evals stay owned by the enterprise rather than the lab [src-20260813-09fcee]
- 2026-08-06 Atlassian -> world 2 because Atlassian runs Rovo agents on its Teamwork Graph [src-20260806-eab99c]
- 2026-08-06 Genpact -> world 4 because Genpact rebrands as Agentic Operations, delivering agents as a services firm [src-20260806-360bc1]
- 2026-08-05 Macro Talk Zendesk -> world 5 because Zendesk sells a complete CX agent with its own services motion, priced on outcomes [src-20260805-5a9fa7]
- 2026-08-05 NiCE -> world 5 because NiCE sells contact center agents (Cognigy) inside its CCaaS suite [src-20260805-3deb2c]
- 2026-08-05 StockAnalysis -> world 4 because TaskUs deploys agentic support for clients in production [src-20260805-c8c134]
- 2026-07-31 a16z Decagon -> world 5 because Decagon argues application-layer vertical agents keep business logic, testing and compliance tooling the labs will not build [src-20260731-a07321]
- 2026-07-30 Amazon Q2 2026 results -> world 1 because AWS funds a $1B in-house FDE team to deploy agents on its own stack [src-20260730-e4cc74]
- 2026-07-30 TP -> world 4 because TP delivers agents to clients through TP.ai with outcome-based contracts [src-20260730-4cc420]
- 2026-07-30 Capgemini -> world 4 because Capgemini sells agentified operations via WNS [src-20260730-c1194e]
- 2026-07-29 Microsoft FY26 Q4 call -> world 1 because Microsoft sells a model-agnostic harness in Foundry and runs its own FDE teams [src-20260729-8b3c16]
- 2026-07-28 AI Engineer Sierra FDE -> world 5 because Sierra's FDEs build and guarantee each customer's CX agent, so the vertical app owns the harness [src-20260728-aba703]
- 2026-07-22 IBM 2Q26 remarks -> world 4 because IBM pairs Orchestrate with consulting, where GenAI is about half of signings [src-20260722-1275ae]
- 2026-07-22 OpenAI Presence -> world 1 because the lab ships a complete vertical CX agent with its own harness, deployed by its FDEs and SIs [src-20260722-a3993b]
- 2026-07-10 Horse's Mouth Workfabric -> world 4 because Workfabric pitches SIs like Cognizant as context engineers for models, a services-led path [src-20260710-e2a61b]
- 2026-07-02 Automation Anywhere -> world 2 because Automation Anywhere sells outcome-based agents on its own automation platform [src-20260702-b5efa8]
- 2026-06-29 LangChain Levie Chase -> world 2 because Box and Salesforce expose systems of record headlessly via MCP, positioning incumbents as data layers for any agent [src-20260629-015aae]
- 2026-06-28 HP Frontier partnership -> world 1 because HP standardizes agent governance and evaluation on the lab platform [src-20260628-930f51]
- 2026-06-24 YC Coval -> world 3 because Coval sells eval components to enterprises building their own voice agents with 100+ internal people on the platform [src-20260624-eb13a6]
- 2026-06-15  -> world 2 because Salesforce acquires Fin to own the CX agent inside its harness [src-20260615-74b583]
- 2026-06-15 CXOTalk Levie -> world 4 because Levie says agent deployment needs FDEs from vendors, SIs or new consulting firms to re-engineer processes [src-20260615-6e3dba]
- 2026-05-27  -> world 2 because Agentforce $1.2B ARR sold mainly into Salesforce's installed base [src-20260527-478f91]
- 2026-05-27 Andreessen Horowitz -> world 5 because startups win by owning the system of work, not the lab-led path [src-20260527-b0d3f3]
- 2026-05-18 Felicis -> world 5 because pricing shifts from hours to outcomes in services-heavy verticals [src-20260518-e39d06]
- 2026-05-15 Presenc AI -> world 3 because enterprises assemble their own stack from infra vendors (Temporal, Braintrust, LiteLLM) [src-20260515-76034a]
- 2026-05-07 Rackspace TFiR (AlphaSense) -> world 4 because a managed-services provider embeds FDE pods and runs the agent stack for regulated customers [src-20260507-288237]
- 2026-05-07 Knowledge 2026 keynote -> world 2 because ServiceNow pitches itself as the governed control plane for every vendor's agents and gives Control Tower away to win it [src-20260507-e6c2cd]
- 2026-05-07 Bain & Company -> world 5 because Bain sizes coordination-work agents as a $100B software TAM sold by vendors [src-20260507-2c054a]
- 2026-04-29 Amazon Q1 2026 results -> world 1 because AWS ships a managed harness and OpenAI-powered managed agents on Bedrock [src-20260429-aec36c]
- 2026-04-29 Microsoft FY26 Q3 call -> world 3 because Bayer builds its own in-house agent platform on Foundry [src-20260429-8a8712]
- 2026-04-27 CXOTalk Akkiraju -> world 3 because Back-end, variable workflows are being built in-house on frameworks and model capabilities [src-20260427-1a7ad0]
- 2026-04-22 Google Cloud partner fund -> world 4 because Google pays SIs $750M to build and deploy agents for customers [src-20260422-72407e]
- 2026-04-17 No Priors McDermott -> world 4 because ServiceNow positions as AI control tower across models, hyperscalers and systems of record; integrated Moveworks, Veza, Armis [src-20260417-a917fe]
- 2026-04-16 TWIML Capital One -> world 3 because Capital One built its own multi-agent platform and harness on open-source models with banking model risk controls [src-20260416-e6896d]
- 2026-04-13 HubSpot -> world 5 because HubSpot sells a complete per-resolution CX agent inside its own app [src-20260413-63104e]
- 2026-04-07 Insight Partners -> world 4 because IBM Consulting experience across 200+ agentic engagements frames the rearchitecture [src-20260407-a1526f]
- 2026-04-04 Venture with Grace Sycamore -> world 2 because Sycamore is a horizontal agent OS sold to Fortune 500 CIOs, the platform model vertical players argue against [src-20260404-029771]
- 2026-04-02 Wawa CIO expert call (AlphaSense) -> world 3 because the CIO wants to combine multiple vendors' agents himself and questions whether the ITSM system of record is needed [src-20260402-8d84cb]
- 2026-04-01 Omni Talk Duvo -> world 5 because Duvo runs retail back-office processes itself on top of legacy systems, displacing consultant process work [src-20260401-e0ba89]
- 2026-03-30 Lightspeed Sycamore memo -> world 2 because Sycamore builds an agent OS that sits above multiple model labs and generates custom enterprise software [src-20260330-2b99a8]
- 2026-03-23 Emergence Capital -> world 5 because thesis is AI-native services selling a result per vertical [src-20260323-bf35e9]
- 2026-03-09 Kleiner Perkins Taylor -> world 5 because Sierra deploys its own FDE 'agent development' team and prices on outcomes, owning the CX harness end to end [src-20260309-78d5a1]
- 2026-02-26 CB Insights -> world 5 because top agent revenue is vertical CX (Sierra, Crescendo) with embedded engineers [src-20260226-87dd95]
- 2026-02-24  -> world 1 because Anthropic ships function plugins for enterprise agents [src-20260224-7eb23d]
- 2026-02-23 OpenAI Frontier Alliances -> world 4 because OpenAI relies on McKinsey, BCG, Accenture and Capgemini to assemble Frontier deployments per client, with the lab owning the platform (worlds 1 and 4 combined) [src-20260223-9272a6]
- 2026-02-05 OpenAI Frontier launch -> world 1 because OpenAI positions Frontier as the one platform that runs and governs every agent, including third-party ones [src-20260205-ea19f4]
- 2026-02-03 Pace on Training Data -> world 5 because Pace sells a complete insurance-ops agent with its own harness, replacing BPO [src-20260203-a5df90]
- 2026-01-23 Battery Ventures -> world 2 because orchestration moves into the model and product layer; durable winners look like SaaS [src-20260123-b88941]
- 2026-01-14 Pigment Traynor -> world 5 because Fin sells outcomes on top of rival systems of record (Zendesk, Service Cloud) [src-20260114-5bb0dc]
- 2026-01-01 AI People -> world 3 because 45 orchestration frameworks plus MCP gateways sold to builders, mostly Seed/A [src-20260101-798b0b]
- 2025-12-09 Menlo Ventures -> world 5 because 76% of enterprise AI is bought, application layer is 63% of spend [src-20251209-1f66cf]
- 2025-11-10 CB Insights -> world 5 because maps 400+ agent apps by function and vertical, healthcare category grew 7 to 47 [src-20251110-87a9f7]
- 2025-11-05 theCUBE Rinke -> world 1 because Celonis customers run Microsoft AI agents on top of Celonis process intelligence, with Celonis as context not harness [src-20251105-fde118]
- 2025-10-18 CamundaCon 2025 keynote -> world 4 because Camunda's agentic orchestration reaches enterprises through Cognizant and EY practices that assemble per-client solutions [src-20251018-229dda]
- 2025-10-02 Zapier Intercom Fin -> world 5 because Intercom Fin sells per-resolution outcomes on top of its own helpdesk, cannibalizing seats deliberately [src-20251002-0b85b2]
- 2025-10-01 theCUBE Dines Fusion 2025 -> world 4 because UiPath pivots company to agentic orchestration; partnerships with OpenAI, Gemini, Snowflake, NVIDIA [src-20251001-78dba6]
- 2025-09-25 Madrona -> world 5 because service-as-software apps own outcome delivery, not horizontal layers [src-20250925-ef08f4]
- 2025-08-21 Lenny McCabe -> world 5 because Intercom moved from seat SaaS to per-resolution Fin as its growth engine [src-20250821-666ad1]
- 2025-08-06 Zendesk -> world 5 because Zendesk bills per verified resolution in its own CX application [src-20250806-3921b6]
- 2025-05-14  -> world 5 because Sierra CEO argues applied vertical agents capture the value and business-model change favors startups over incumbents [src-20250514-093b59]
- 2025-02-18 NFX -> world 5 because vertical agent marketplaces and micro agents (Enso) capture the work [src-20250218-8373e2]
- 2024-12-18 20VC Dines 2024 -> world 2 because UiPath argues orchestration sits above systems of record because customers will not move data between them, contesting world 2 but confirming fragmentation by system [src-20241218-3282c7]
- 2024-12-17 Insight Partners -> world 5 because agents sold as Hire-an-Agent or outcome-priced per use case [src-20241217-06d5b1]
- 2024-12-05 Bessemer Venture Partners -> world 5 because vertical AI invents per-outcome business models [src-20241205-4ac3cf]
- 2024-10-02 Lightspeed Venture Partners -> world 5 because next automation wave is agentic apps with built-in auditability per workflow [src-20241002-fb86b9]
- 2024-09-27 Felicis -> world 5 because agents target labor budgets 35x software budgets via applications [src-20240927-2e10b2]
- 2023-12-07 Greylock -> world 5 because vertical AI apps with outcome pricing win per industry [src-20231207-3fbd49]

## 3. Outcome pricing test
For each vendor claiming outcome pricing, capture: the unit (resolution, task, document, % savings), price per unit, how the outcome is verified, who audits it, what happens at renewal, and the gross margin after inference. A vendor passes if the unit is countable, the customer agrees with the count, and the contract renewed at least once.

## 4. Readout structure (2026-10-28/29)
1. **Answer first:** push further, or "here is our perspective and why we're not pushing further". One paragraph.
2. **Tipping point** (Q1-Q4): three numbers and two quotes.
3. **Right to win** (Q5-Q8): which of the five worlds, the labs' 6-9 month launch list, and the layers it absorbed.
4. **Investable today** (Q9-Q12): a short list by layer with stage, customers and why each passes or fails the fit tests.
5. **What we'd need from calls** (Q13-Q15): the three call types below and the five questions we would ask.

## 5. Expert-call archetypes
Question lists are in `expert-call-guide.md`.
- **Fortune 500 head of AI / automation** with agents in production (buyer view, Q1-Q5, Q13)
- **SI agentic practice lead** at Deloitte, Accenture or others (cross-client view, Q3, Q5, Q14)
- **Customer or former employee** of Sycamore, Duvo or Workfabric (product truth, Q2, Q7, Q15)
