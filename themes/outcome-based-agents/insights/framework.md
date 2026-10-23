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
- 2026-10-23  -> world 1 because Google deploys agents in public sector via its own RISE prototypers and FDEs [src-20261023-5b3495]
- 2026-10-22  -> world 3 because Ramp builds its own agent harness (Laminar) instead of buying [src-20261022-ae18f2]
- 2026-10-22  -> world 4 because Cognizant builds an 18,000-engineer Gemini agent deployment group [src-20261022-d5ad54]
- 2026-10-22  -> world 1 because Google channels agent deployment through Cognizant FDE bench [src-20261022-d5ad54]
- 2026-10-21  -> world 1 because Anthropic ships Claude Duet, a lab-owned always-on work agent [src-20261021-d5280b]
- 2026-10-21  -> world 2 because ServiceNow governs desktop agents through its Control Tower [src-20261021-bf34b8]
- 2026-10-21  -> world 1 because Microsoft ships a CX agent overlay on existing contact centers [src-20261021-e45563]
- 2026-10-21  -> world 1 because Meta pushes Muse business agents and enterprise platform [src-20261021-f65653]
- 2026-10-20  -> world 4 because Sutherland (BPO) runs FlowX.AI agents on outcome pricing [src-20261020-a21f1d]
- 2026-10-16  -> world 2 because SAP signals outcome-based reset pricing [src-20261016-9f1777]
- 2026-10-13  -> world 4 because DXC runs its own LangChain-based harness (OASIS) for customers' IT operations [src-20261013-1dcd15]
- 2026-10-09  -> world 4 because Deloitte builds open-model harness practice with FDEs [src-20261009-4138dc]
- 2026-10-05  -> world 3 because 67% of enterprises expect a hybrid, external or in-house agent control plane (VB Pulse) [src-20261005-66e092]
- 2026-10-05  -> world 4 because Mastek sells AI-built replacements for SaaS as services-as-software [src-20261005-ed6751]
- 2026-10-03  -> world 2 because Oracle embeds native agent orchestration (Fusion Claw) in ERP [src-20261003-10d57c]
- 2026-09-29 OpenAI DevDay 2026 -> world 1 because OpenAI offers always-on agents plus specialist role agents with identity, positioning itself as the enterprise agent provider, while delegating governance to Microsoft [src-20260929-2fdd0f]
- 2026-09-29  -> world 1 because OpenAI seeds an open-source agent control plane (OpenClaw Enterprise) [src-20260929-247cd8]
- 2026-09-10 OpenAI Agents API -> world 1 because OpenAI gives away its production harness to developers, making the harness a lab feature [src-20260910-014b24]
- 2026-09-09 Salesforce GS Communacopia (AlphaSense) -> world 2 because Salesforce runs agents on its own CRM data and Slack context, partnering with Anthropic for models and orchestrating Fin and Piper [src-20260909-c1900d]
- 2026-08-25  -> world 3 because 32% of enterprises now build software in-house with coding agents instead of buying (McKinsey) [src-20260825-e5c5c1]
- 2026-08-13 Sequoia Chase harness -> world 2 because LangChain argues harness, context and evals stay owned by the enterprise rather than the lab [src-20260813-09fcee]
- 2026-07-31 a16z Decagon -> world 5 because Decagon argues application-layer vertical agents keep business logic, testing and compliance tooling the labs will not build [src-20260731-a07321]
- 2026-07-22 OpenAI Presence -> world 1 because the lab ships a complete vertical CX agent with its own harness, deployed by its FDEs and SIs [src-20260722-a3993b]
- 2026-07-10 Horse's Mouth Workfabric -> world 7 because Workfabric pitches SIs like Cognizant as context engineers for models, a services-led path [src-20260710-e2a61b]
- 2026-06-29 LangChain Levie Chase -> world 2 because Box and Salesforce expose systems of record headlessly via MCP, positioning incumbents as data layers for any agent [src-20260629-015aae]
- 2026-06-28 HP Frontier partnership -> world 1 because HP standardizes agent governance and evaluation on the lab platform [src-20260628-930f51]
- 2026-06-15  -> world 2 because Salesforce acquires Fin to own the CX agent inside its harness [src-20260615-74b583]
- 2026-05-27  -> world 2 because Agentforce $1.2B ARR sold mainly into Salesforce's installed base [src-20260527-478f91]
- 2026-05-07 Rackspace TFiR (AlphaSense) -> world 4 because a managed-services provider embeds FDE pods and runs the agent stack for regulated customers [src-20260507-288237]
- 2026-04-04 Venture with Grace Sycamore -> world 2 because Sycamore is a horizontal agent OS sold to Fortune 500 CIOs, the platform model vertical players argue against [src-20260404-029771]
- 2026-04-02 Wawa CIO expert call (AlphaSense) -> world 3 because the CIO wants to combine multiple vendors' agents himself and questions whether the ITSM system of record is needed [src-20260402-8d84cb]
- 2026-04-01 Omni Talk Duvo -> world 5 because Duvo runs retail back-office processes itself on top of legacy systems, displacing consultant process work [src-20260401-e0ba89]
- 2026-03-30 Lightspeed Sycamore memo -> world 2 because Sycamore builds an agent OS that sits above multiple model labs and generates custom enterprise software [src-20260330-2b99a8]
- 2026-02-24  -> world 1 because Anthropic ships function plugins for enterprise agents [src-20260224-7eb23d]
- 2026-02-23 OpenAI Frontier Alliances -> world 4 because OpenAI relies on McKinsey, BCG, Accenture and Capgemini to assemble Frontier deployments per client, with the lab owning the platform (worlds 1 and 4 combined) [src-20260223-9272a6]
- 2026-02-05 OpenAI Frontier launch -> world 1 because OpenAI positions Frontier as the one platform that runs and governs every agent, including third-party ones [src-20260205-ea19f4]
- 2025-05-14  -> world 5 because Sierra CEO argues applied vertical agents capture the value and business-model change favors startups over incumbents [src-20250514-093b59]

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
