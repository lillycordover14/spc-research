# Evidence by question

The fastest path from reading to a readout. Every time an agent summarizes a source, it adds one line per claim under the question it answers: `- <claim, with the number> [src-id]`. Newest first within each question. The weekly synthesis and the readout are written from this page, not from re-reading sources.

Questions are defined in `questions.md`.

## Q1. Production, not pilots
- 2026-10-08 | Adoption claims (nearly 90% of the Fortune 100 on Gemini Enterprise; SOMPO with 10,000+ custom agents) are vendor-reported breadth data [src-20261008-d5cbe2]
- 2026-07-22 | OpenAI says Presence resolves 75% of inbound issues on its own phone support line without humans; launch customers BBVA, SoftBank, IAG are exploring or testing, not in production [src-20260722-a3993b]
- 2026-06-28 | HP, a Frontier launch adopter, was still moving 'from pilots toward production' in Jun 2026 with use cases being refined [src-20260628-930f51]
- 2026-06-16 | Over half of the Fortune 500 using Cowork is a vendor-reported breadth signal for long-running agents in knowledge work [src-20260616-28211f]
- 2026-04-22 | Customer counts like 800 to 1,000+ agents at a single enterprise and 40% QoQ paid MAU growth are vendor-reported adoption data points for agent deployment breadth [src-20260422-d312c6]
- 2026-04-02 | Wawa CIO (AlphaSense, interview 2026-04-02): 30-50% of ITSM work agent-addressable today; still testing ServiceNow plus Moveworks, not in production [src-20260402-8d84cb]
- 2026-02-05 | Frontier first adopters HP, Intuit, Oracle, State Farm, Thermo Fisher and Uber; BBVA, Cisco and T-Mobile piloted; OpenAI says the blocker is how agents are built and run, not model intelligence [src-20260205-ea19f4]

## Q2. Outcome pricing, real or rhetoric
- 2026-10-22 | Agent payments via x402 and wallets suggests hyperscalers expect agents to transact per task, an enabling rail for per-outcome or per-task pricing [src-20261022-a0f852]
- 2026-10-21 | Bundling Duet into existing Pro and Max limits shows labs pricing agent labor inside subscriptions, making standalone per-task pricing harder for SMB-focused startups [src-20261021-7532a5]
- 2026-10-08 | SDR agent billed in Copilot credits is consumption pricing for digital labor, closer to per-task than per-seat, but still not per-outcome [src-20261008-5bb82b]
- 2026-10-07 | Gamma Communications markets AI Concierge (FAQ, intake, booking agents) as 'outcome-based agents' with no outcome pricing disclosed: the term is being used loosely [src-20261007-fc84b0]
- 2026-09-09 | Salesforce (GS Communacopia, 2026-09-09): premium agentic SKUs ~5% of installed base at 60-80% uplift; sales agents moving to paying for qualified leads or booked orders [src-20260909-c1900d]
- 2026-08-26 | Google is moving agent pricing from seats toward consumption (PAYG, pooled quotas, off-peak batch at half price), but not to outcomes; outcome-based pricing remains an app-layer opportunity on top of usage-priced labs [src-20260826-c6c4b5]
- 2026-06-16 | Microsoft layered consumption pricing (credits metered on model use, tool calls and runtime) on top of a seat, a hybrid that shows the shift from seats toward usage-based agent labor but not to per-outcome pricing [src-20260616-28211f]
- 2026-05-19 | A rubric-plus-grader 'outcomes' primitive makes it technically easy to define and verify a unit of completed work, the precondition for outcome-based pricing by apps built on the lab [src-20260519-55cca6]
- 2026-04-22 | OpenAI moved workspace agents to credit-based (usage) pricing on 2026-05-06, not seats or outcomes [src-20260422-75a0a8]
- 2026-04-08 | Session-hour pricing is a lab-level unit price for agent labor, a step toward time- or outcome-based units rather than seats [src-20260408-e5d37b]
- 2026-03-09 | Microsoft prices agent governance per human user ($15) and bundles it into a $99 seat, the opposite of per-agent or per-outcome pricing, which signals the largest incumbent is defending seat economics rather than moving to outcomes [src-20260309-f391cf]

## Q3. What blocks production
- 2026-10-14 | Graduated access based on trace review is a lab-endorsed answer to the trust blocker for production agents [src-20261014-2e6208]
- 2026-10-08 | Google naming governance and affordability as the two gating factors is a lab-side read on production blockers [src-20261008-d5cbe2]
- 2026-10-02 | Treating FDE talent as the scaling constraint confirms deployment skill, not model capability, is the main blocker to production [src-20261002-8d9e4f]
- 2026-05-07 | Rackspace (TFiR, 2026-05-07) names data aggregation from legacy systems and standing up the AI ecosystem as the main production blockers; regulated healthcare customers refuse public cloud [src-20260507-288237]
- 2026-04-02 | Wawa CIO: only ~20% of IT issues are ever logged as tickets, so the ticket system itself limits what agents can see [src-20260402-8d84cb]
- 2026-03-12 | Services capacity, not model access, is treated as the bottleneck to production, consistent with pilot-to-production being the main blocker [src-20260312-73c25c]
- 2026-03-09 | OpenAI calls evaluation, security and compliance 'foundational requirements' for AI coworkers in real workflows [src-20260309-b2ac14]

## Q4. Whose budget
- 2026-10-22 | Letting Managed Agents and the full agent toolkit draw down Google Cloud commitments removes the procurement friction that favored hyperscaler-native harnesses, extending the lab's harness into cloud budgets [src-20261022-d0a3a2]
- 2026-10-21 | Budget for these agents likely comes from existing managed-services and BPO contracts rather than new IT software lines [src-20261021-776c89]
- 2026-09-09 | Salesforce says outcome deals are funded either from the savings themselves or from revenue-line metrics (qualified leads, booked orders) [src-20260909-c1900d]
- 2026-08-26 | Explicit 'never pay for empty seats' language signals seat compression pressure even at the platform layer, and per-project caps let agent spend be charged back to departments rather than central IT [src-20260826-c6c4b5]
- 2026-05-01 | Per-user licensing for agent governance keeps agent spend inside IT and security budgets [src-20260501-fc687c]
- 2026-04-02 | Wawa CIO sizes AI add-ons at ~20% of core ITSM platform cost, from IT budget, under pressure from rising SaaS costs [src-20260402-8d84cb]
- 2026-03-09 | Budget for agent governance lands in the IT and security line via the M365 agreement, not in BPO or headcount budgets [src-20260309-f391cf]

## Q5. Who builds the harness
- 2026-10-22 | The lab harness now ships inside a rival hyperscaler, so independent agent-runtime startups compete with a lab runtime that is available on every major cloud marketplace [src-20261022-d0a3a2]
- 2026-10-22 | Harness is model-agnostic (Bedrock, OpenAI, Gemini, LiteLLM), so AWS competes with the model labs' own managed harnesses on neutrality, making the harness a contested layer between labs and clouds rather than a startup-owned one [src-20261022-a0f852]
- 2026-10-21 | An IT-services/BPO giant embedding Claude agents into its managed IT support and code remediation platform (AI Force) is the services-as-software model run by an incumbent SI, competing with agent-native IT-ops startups [src-20261021-776c89]
- 2026-10-21 | FDE-staffed sandboxes on client systems show the SI is the harness builder for regulated enterprises, with the lab supplying models and agent runtime [src-20261021-776c89]
- 2026-10-02 | The lab is industrializing the forward-deployed engineer role and seeding it into SIs and large enterprises (Morgan Stanley, CBA, Novo Nordisk), so in-house teams and SIs, not startups, become the default harness builders [src-20261002-8d9e4f]
- 2026-09-29 | OpenAI is integrating specialist dots into Microsoft Agent 365 governance and shipping OpenAI agents inside Bedrock, splitting the harness between lab (agent) and platform owner (governance, cloud) [src-20260929-2fdd0f]
- 2026-09-09 | Salesforce partners with Anthropic (Claudeforce) and positions Agentforce as orchestrator of specialized agents (Fin, Piper), i.e. system of record as harness [src-20260909-c1900d]
- 2026-06-28 | HP picked OpenAI Frontier as its unified agent control plane (what runs, context, governance, evaluation) after a Feb to Jun 2026 evaluation [src-20260628-930f51]
- 2026-05-12 | Law firms co-developing workflows directly with Anthropic (Freshfields, Quinn Emanuel) show the enterprise and the lab building the harness together without a vertical vendor in between [src-20260512-5c6e2d]
- 2026-05-07 | Rackspace sells FDE pods plus private cloud with Palantir and Uniphore as 'AI outcome platforms', a services-led harness model [src-20260507-288237]
- 2026-05-05 | Shipping the same template as a Cowork plugin and as a Managed Agents cookbook shows the lab wants to own both the end-user surface and the programmatic harness for back-office agents [src-20260505-1c452a]
- 2026-04-22 | Google is positioning the cloud provider, not the enterprise or the SI, as the default orchestration and governance harness, with the employee app as the distribution surface [src-20260422-1f1ec3]
- 2026-04-22 | Google's answer to who builds the harness is lab FDE teams embedded inside the big SIs (Accenture, Deloitte, PwC, TCS and others), confirming the lab-plus-SI deployment model [src-20260422-d312c6]
- 2026-04-08 | With the harness priced at $0.08 per session-hour on top of tokens, the lab is the default harness builder for app companies like Notion, Asana and Atlassian; independent harness vendors must win on multi-model neutrality or on-prem control [src-20260408-e5d37b]
- 2026-04-02 | Wawa CIO prefers multiple vendors' agents over a single platform and keeps architects in-house, i.e. the enterprise assembles the harness [src-20260402-8d84cb]
- 2026-03-12 | Anthropic is subsidizing SIs ($100M, 5x partner engineers) to do the last-mile deployment rather than building a large in-house services arm, so the harness for most enterprises will be assembled by Accenture, Deloitte, Cognizant and Infosys on lab primitives [src-20260312-73c25c]
- 2026-02-24 | Department templates for HR, sales (Apollo, Clay, Outreach connectors) and legal (Harvey, LegalZoom, Docusign) mean the lab plus SaaS vendors' own plugins are building the departmental harness, leaving room mainly for vendors who own the data or the outcome [src-20260224-a28ce9]
- 2026-02-23 | OpenAI Frontier Alliances (BCG, McKinsey, Accenture, Capgemini) pair certified SI practice groups with OpenAI FDEs, so the large-enterprise harness is lab platform plus SI delivery [src-20260223-9272a6]
- 2026-02-05 | OpenAI pitches Frontier as the harness for agents built in-house, by OpenAI or by other vendors, i.e. the lab as the single enterprise harness [src-20260205-ea19f4]
- 2026-01-30 | Because plugins are portable files the enterprise owns, Anthropic is making the customer (or its SI) the author of the harness configuration, with the lab owning the runtime [src-20260130-79791d]
- 2026-01-11 | The lab ships a 'sample' prior auth skill and relies on Accenture, Deloitte, KPMG and PwC for deployment, so the production harness for regulated payer and provider workflows is still being built by SIs and vertical apps on top of the lab primitives [src-20260111-f1affc]

## Q6. What the labs shipped (last 6-9 months) and what it absorbed
- 2026-10-22 | AWS added a managed agent loop (Harness), policy, registry, evaluations, memory, identity and an LLM gateway with routing and fallback in 2026, overlapping agent-runtime, AI gateway, eval and agent-identity startups in one hyperscaler service [src-20261022-a0f852]
- 2026-10-21 | An always-on agent with a cloud browser, 6,000+ connectors and payment rails, bundled free into consumer plans, pressures SMB back-office agent startups (bookkeeping, scheduling, admin assistants) and personal executive-assistant agents [src-20261021-7532a5]
- 2026-10-14 | By emitting standard OTel traces, the lab commoditizes trace capture, leaving LLM observability startups (Langfuse, Braintrust, Arize, LangSmith) to compete on analysis and evals rather than instrumentation [src-20261014-2e6208]
- 2026-10-08 | A first-party AI SDR agent and a service agent inside Dynamics and Teams hit AI SDR/outbound startups and CX support agent startups (Sierra, Decagon tier) within Microsoft accounts [src-20261008-5bb82b]
- 2026-10-08 | A single objective-driven universal agent with Financial Services and Legal specializations competes with both horizontal work-agent startups and vertical finance and legal agent apps [src-20261008-d5cbe2]
- 2026-09-29 | OpenAI specialist dots (preview 2026-09-29) target procurement, invoice processing, contracting and support roles with their own identity and system-of-record integrations, the same back-office workflows Duvo and Sycamore sell [src-20260929-2fdd0f]
- 2026-09-10 | OpenAI Agents API (public beta 2026-09-10) offers the Codex harness as managed infra with no fee beyond tokens, pressuring paid agent runtimes and frameworks [src-20260910-014b24]
- 2026-07-22 | OpenAI Presence (2026-07-22) is a first-party CX and voice resolution agent with policies, simulations, graders and a Codex improvement loop, directly overlapping Sierra and Decagon [src-20260722-a3993b]
- 2026-05-26 | GA computer-using agents inside a low-code workflow designer target the RPA and agentic process automation category (UiPath, Automation Anywhere) and computer-use agent startups head on [src-20260526-3c3aa7]
- 2026-05-26 | Real-time voice agents GA in Dynamics 365 Contact Center pressure voice CX agent startups in Microsoft-centric contact centers [src-20260526-3c3aa7]
- 2026-05-19 | Multi-agent orchestration, rubric-based graders and self-curating memory are now lab-native, absorbing much of what multi-agent framework, agent-eval and agent-memory startups sell [src-20260519-55cca6]
- 2026-05-12 | Twelve free practice-area plugins (contract review, employment, privacy, litigation) put the lab in direct overlap with legal AI apps; Harvey, Legora and Solve now appear as connectors inside Claude, a sign the lab is becoming the front door [src-20260512-5c6e2d]
- 2026-05-05 | Month-end close, GL reconciliation, statement audit and KYC screening templates go straight at finance-ops and compliance agent startups (close automation, recon, KYC/AML) with a free template on an existing seat [src-20260505-1c452a]
- 2026-05-01 | A cross-cloud agent registry, shadow-agent discovery and network controls priced per user absorb the agent inventory and agent security posture category that several startups target [src-20260501-fc687c]
- 2026-04-22 | Agent Simulation, Agent Observability, Agent Identity, Gateway and Memory Bank in one hyperscaler platform absorb large parts of the evals, observability, agent identity and agent memory tooling categories [src-20260422-1f1ec3]
- 2026-04-22 | Google shipped first-party domain agents for CX (Gemini Enterprise for Customer Experience with support agents, Agent Assist, voice) and security operations (triage, threat hunting, detection engineering), hitting AI CX startups and AI SOC startups directly [src-20260422-d312c6]
- 2026-04-22 | ChatGPT workspace agents (shared, scheduled, MCP-connected, Slack-native, credit-metered from 2026-05-06) put a lab-built department agent builder in every Enterprise workspace [src-20260422-75a0a8]
- 2026-04-08 | This is the clearest lab move to own the harness itself (agent loop, sandbox, memory, permissions, scheduling, tracing), directly absorbing agent-infrastructure startups selling hosted runtimes, sandboxes and agent memory [src-20260408-e5d37b]
- 2026-03-09 | An agent registry, agent identity and governance control plane bundled into E7 compresses the standalone agent-governance and agent-identity startup category [src-20260309-f391cf]
- 2026-03-09 | OpenAI is folding Promptfoo (red-teaming and evals, used by 25%+ of Fortune 500) into Frontier, absorbing the agent eval and AI security testing category [src-20260309-b2ac14]
- 2026-02-24 | Free investment banking, equity research, PE diligence and wealth plugins overlap the front-office analyst copilot category (pitch books, comps, earnings notes) that several finance AI startups target [src-20260224-11d529]
- 2026-02-24 | Private marketplaces, per-user provisioning, MCP controls and OTel cost tracking are the enterprise agent governance and distribution layer many 'agent store' and AI-governance startups pitched; the lab now bundles them into Cowork [src-20260224-a28ce9]
- 2026-02-05 | OpenAI Frontier bundles business context, agent execution, memory, evals and per-agent identity in one enterprise platform, absorbing agent platform, agent identity, eval and memory startup categories [src-20260205-ea19f4]
- 2026-01-30 | Free, open-source Sales, Legal, Customer support and Finance plugins put a lab-built 'department agent' in front of every paid Claude seat, pressuring thin horizontal copilots for those functions [src-20260130-79791d]
- 2026-01-11 | Anthropic shipped prior authorization and claims-appeal templates plus CMS, ICD-10 and NPI connectors as free add-ons to Claude subscriptions, which directly overlaps the first workflow many healthcare RCM and prior-auth agent startups sell [src-20260111-f1affc]

## Q7. Orchestration vs context vs vertical vs services
- 2026-10-14 | The lab chose to partner with, not replace, observability vendors, suggesting cross-model observability and evaluation remains a defensible neutral layer [src-20261014-2e6208]
- 2026-07-22 | Presence ships the full CX agent harness (SOPs, guardrails, simulations, graders, improvement loop), so vertical CX vendors must defend on outcomes, data and distribution rather than harness [src-20260722-a3993b]
- 2026-05-26 | Microsoft's hybrid of deterministic workflows plus agent nodes suggests the orchestration layer is being absorbed into the platform that already owns identity and the desktop [src-20260526-3c3aa7]
- 2026-05-19 | Vertical apps such as Harvey run their harness on the lab's managed orchestration, so their moat must sit in domain rubrics, data and distribution, not the agent loop [src-20260519-55cca6]
- 2026-05-12 | Defensibility in legal shifts to proprietary content and workflow systems (Thomson Reuters, iManage, Relativity) and to outcome accountability, since general drafting and redlining is now lab-provided [src-20260512-5c6e2d]
- 2026-05-01 | Microsoft positions itself as the governance plane over agents built anywhere (Bedrock, Google Agent Platform, n8n, Zendesk), making the control plane rather than the harness its defensible layer [src-20260501-fc687c]
- 2026-04-22 | Orchestration as a standalone layer gets squeezed between hyperscaler platforms and systems of record that ship their own agents into the same gallery [src-20260422-1f1ec3]
- 2026-03-12 | Boutique agent-deployment services startups now compete with lab-funded global SIs carrying lab certifications [src-20260312-73c25c]
- 2026-02-24 | The finance data incumbents (FactSet, S&P, LSEG, MSCI) are distributing through Claude as connectors, so the work-context moat sits with licensed data owners rather than with agent wrappers [src-20260224-11d529]
- 2026-02-05 | Frontier claims the enterprise semantic layer ('how information flows, where decisions happen'), the same work-context asset Workfabric and Celonis sell [src-20260205-ea19f4]
- 2026-01-30 | Value for startups moves to proprietary data, system-of-record write access and measured outcomes, since prompts plus skills plus connectors is now a free file format [src-20260130-79791d]
- 2026-01-11 | Defensibility for vertical healthcare-admin players shifts toward proprietary payer rules, EHR write-back and outcome guarantees, since public coding and coverage data is now a commodity connector [src-20260111-f1affc]

## Q8. Systems of record
- 2026-10-08 | An AI-driven migration tool aimed at legacy CRM (Comcast's quote references Salesforce) shows agents being used as a wedge to displace incumbent systems of record, not just sit on top of them [src-20261008-5bb82b]
- 2026-10-08 | Giving agents their own Workspace identity and mailbox makes the productivity suite owner the natural home for 'digital coworker' agents, a strong position for incumbents holding identity and documents [src-20261008-d5cbe2]
- 2026-09-29 | OpenAI Marketplace lets enterprises spend OpenAI commitments on 32 partners including Salesforce, ServiceNow, Sierra and Decagon, so labs distribute systems of record and vertical apps rather than displace them [src-20260929-2fdd0f]
- 2026-09-09 | Salesforce rejects the headless-CRM bear case: CRM metadata encodes company knowledge; work shifting to Slack and Claude still increases CRM work volume [src-20260909-c1900d]
- 2026-06-16 | A system-of-work incumbent wrapping Anthropic's models and Cowork pattern, then undercutting Claude Cowork on price by 30 to 40% with its own fine-tuned model, shows the harness owner with the data (Work IQ) can commoditize the model lab [src-20260616-28211f]
- 2026-05-05 | FIS embedding Claude so its clients need not build infrastructure suggests the system of record plus lab combination, not a standalone vertical agent, captures many bank deployments [src-20260505-1c452a]
- 2026-04-22 | Systems of record (Salesforce, ServiceNow, Workday, Oracle) are partners distributing agents into Gemini Enterprise rather than being displaced [src-20260422-d312c6]
- 2026-04-02 | Wawa CIO calls ServiceNow 'just a bunch of data' and asks whether agents could replace it; rates Now Assist as not doing the job [src-20260402-8d84cb]
- 2026-02-24 | Systems of record (Salesforce via Slack, FactSet, S&P, LSEG) chose to ship as plugins inside Claude rather than resist, suggesting the defensible asset is proprietary data access, not the agent shell [src-20260224-a28ce9]

## Q9. Horizontal players, investable

## Q10. Vertical players, investable

- 2026-10-07 | Telecom channels (Gamma) now bundle SMB booking and intake agents, commoditizing SMB front-desk agent startups [src-20261007-fc84b0]
## Q11. Unit economics
- 2026-10-02 | FDE-heavy agent startups face a lab-trained talent pool at their customers, which compresses the services premium and pushes them toward product-led, outcome-priced models [src-20261002-8d9e4f]
- 2026-09-10 | The lab prices its managed harness at zero (tokens and tools only), so standalone harness vendors cannot charge for the agent loop itself [src-20260910-014b24]
- 2026-09-09 | Agentforce 1 Edition $550 per seat consolidates ~$1,300 of US sales-rep point-solution spend [src-20260909-c1900d]
- 2026-08-26 | Off-peak deferred execution at up to half the inference cost lowers COGS for async back-office agents, improving gross margins for outcome-priced vertical players [src-20260826-c6c4b5]

## Q12. Exit paths

- 2026-09-29 | OpenAI Marketplace is a new distribution channel for vertical agent startups (Sierra, Decagon, Harvey, Legora) via enterprise OpenAI commitments [src-20260929-2fdd0f]
- 2026-03-09 | Promptfoo sold to OpenAI after raising $23M at an $86M valuation (Jul 2025, PitchBook via TechCrunch): lab tuck-in is the exit for harness-infra point tools [src-20260309-b2ac14]
## Q13. F500 heads of AI / automation (calls)

- 2026-04-02 | Wawa CIO call shows the F500 buyer questions to ask: unlogged-issue share, add-on AI budget as % of platform, satisfaction with incumbent agents [src-20260402-8d84cb]
## Q14. SI practice leads (calls)

- 2026-02-23 | Each of the four Frontier Alliance SIs is building a dedicated, OpenAI-certified practice group, the natural pool for SI practice-lead calls [src-20260223-9272a6]
## Q15. Sycamore / Duvo / Workfabric customers and formers (calls)

## Q16. Push further or not

## Q17. SPC's operator edge
