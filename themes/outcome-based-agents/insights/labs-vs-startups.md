# Labs vs startups: what the model labs shipped and what it absorbed

Answers Q6 and feeds Q5 and Q7. One row per launch, newest first, each with a source id. Only launches aimed at enterprise agents: agent platforms, SDKs and harness features, domain solution sets (finance, legal, CX, healthcare, etc.), enterprise connectors, deployment and forward-deployed teams.

| Date | Lab | Launch | Layer it competes with | Startup categories hit | Source |
|---|---|---|---|---|---|
| 2026-10-22 | Anthropic | Full Claude Platform (incl. Managed Agents) on Google Cloud, Anthropic-managed | harness-infra | Agent runtimes, hosted agent infra sold via cloud marketplaces | [src-20261022-d0a3a2] |
| 2026-10-22 | AWS | Bedrock AgentCore 2026 build-out: Harness (managed loop), Policy GA, Registry, Payments, Gateway LLM routing, Evaluations, Memory | harness-infra, orchestration | Agent runtimes, AI gateways/routers, evals, agent identity, agent memory, agent payments | [src-20261022-a0f852] |
| 2026-10-21 | Anthropic | HCLTech Global Premier partner: FDE sandboxes, AI Force IT agents, HCLSoftware ISV | services | Agent deployment boutiques, AI-native IT-ops/managed services | [src-20261021-776c89] |
| 2026-10-21 | Anthropic | Claude Duet proactive always-on agent (research preview) | vertical-outcome (SMB), adjacent | SMB back-office agents, AI executive assistants, computer-use agents | [src-20261021-7532a5] |
| 2026-10-14 | Anthropic | Native OpenTelemetry agent tracing on Claude Platform | harness-infra | LLM observability (instrumentation layer), agent tracing | [src-20261014-2e6208] |
| 2026-10-08 | Google | Gemini agent (universal work agent), coworker agents with own identity, FS and Legal specializations | harness-infra, work-context, vertical-outcome | Horizontal work agents, digital coworker agents, finance and legal agents | [src-20261008-d5cbe2] |
| 2026-10-08 | Microsoft | Dynamics 365 Sales Development Agent, Service Agent, CRM in Teams, AI CRM migration | vertical-outcome, work-context | AI SDR/outbound, CX support agents, CRM migration services | [src-20261008-5bb82b] |
| 2026-10-02 | Anthropic | Claude Frontier Academy: $100M to train 10,000 Frontier Deployed Engineers | services | FDE-heavy agent startups, agent deployment consultancies | [src-20261002-8d9e4f] |
| 2026-09-29 | OpenAI | DevDay: dots and specialist dots (role agents with own identity, preview), Agents API computer use, Bedrock Managed Agents powered by OpenAI, Marketplace (32 partners) | vertical-outcome, harness-infra, orchestration | Back-office role agents (procurement, AP/invoice, contracting), computer-use agents, agent marketplaces | [src-20260929-2fdd0f] |
| 2026-09-10 | OpenAI | Agents API public beta: Codex harness as managed infra, no fee beyond tokens | harness-infra | Agent runtimes, agent frameworks and hosted harnesses | [src-20260910-014b24] |
| 2026-08-26 | Google | Flexible billing for agents: PAYG, savings plans, spend caps, deferred execution | harness-infra (pricing) | AI FinOps/cost control tools; pressure on seat-priced agent apps | [src-20260826-c6c4b5] |
| 2026-07-22 | OpenAI | Presence: deployed voice and chat CX agents (SOPs, guardrails, simulations, graders, Codex improvement loop), FDE and SI led | vertical-outcome | AI CX and voice support agents (Sierra, Decagon tier), outbound sales voice agents | [src-20260722-a3993b] |
| 2026-06-28 | OpenAI | HP scales Frontier as unified agent control plane after pilots (customer proof point) | orchestration | Enterprise agent OS and governance platforms | [src-20260628-930f51] |
| 2026-06-16 | Microsoft | Copilot Cowork GA (Anthropic models, credit-metered) | harness-infra, work-context | Horizontal long-running work agents, knowledge-work copilots | [src-20260616-28211f] |
| 2026-05-26 | Microsoft | Copilot Studio computer-using agents GA, workflows, A2A GA, voice agents GA | orchestration, harness-infra | RPA/agentic process automation, computer-use agents, voice CX agents | [src-20260526-3c3aa7] |
| 2026-05-19 | Anthropic | Managed Agents: outcomes (rubric grader), multiagent orchestration, dreaming memory, webhooks | harness-infra, orchestration | Multi-agent frameworks, agent evals/graders, agent memory | [src-20260519-55cca6] |
| 2026-05-12 | Anthropic | Claude for the legal industry: 12 practice plugins, 20+ legal connectors | vertical-outcome, work-context | Legal AI apps (contract review, litigation, legal research) | [src-20260512-5c6e2d] |
| 2026-05-05 | Anthropic | Agents for financial services: 10 templates (close, recon, audit, KYC, pitch, research) | vertical-outcome, work-context | Finance-ops agents (close, recon), KYC/AML, banking analyst copilots | [src-20260505-1c452a] |
| 2026-05-01 | Microsoft | Agent 365 GA: agent registry, cross-cloud sync, shadow-agent discovery, $15/user | orchestration (governance), adjacent | Agent governance, agent identity, AI security posture | [src-20260501-fc687c] |
| 2026-04-22 | Google | Next '26: agentic enterprise stack, CX and security domain agents, FDEs with SIs | harness-infra, vertical-outcome, services | AI CX agents, AI SOC agents, agent marketplaces, deployment services | [src-20260422-d312c6] |
| 2026-04-22 | Google | Gemini Enterprise Agent Platform (Vertex AI evolution) | harness-infra, orchestration | Agent builders, orchestration, agent memory, identity, simulation/evals, observability | [src-20260422-1f1ec3] |
| 2026-04-22 | OpenAI | Workspace agents in ChatGPT (Codex-powered shared agents, schedules, MCP, Slack; credit pricing from 2026-05-06) | harness-infra, vertical-outcome | No-code agent builders, departmental workflow agents | [src-20260422-75a0a8] |
| 2026-04-08 | Anthropic | Claude Managed Agents (managed harness, $0.08 per session-hour) | harness-infra, orchestration | Agent runtimes, sandboxes, agent memory, agent infra platforms | [src-20260408-e5d37b] |
| 2026-03-12 | Anthropic | Claude Partner Network ($100M, 5x partner team) | services | Agent deployment boutiques, AI consultancies | [src-20260312-73c25c] |
| 2026-03-09 | Microsoft | Microsoft 365 E7 Frontier Suite ($99/user) and Agent 365 pricing | orchestration (governance), adjacent | Agent governance and identity; seat-priced copilots | [src-20260309-f391cf] |
| 2026-03-09 | OpenAI | Acquires Promptfoo; red-teaming, evals and compliance folded into Frontier | harness-infra | Agent evals, AI red-teaming and security testing | [src-20260309-b2ac14] |
| 2026-02-24 | Anthropic | Enterprise agents: private plugin marketplaces, admin controls, HR/design/eng plugins, connectors | orchestration, work-context, vertical-outcome | Agent stores/marketplaces, AI governance, HR/sales/legal department agents | [src-20260224-a28ce9] |
| 2026-02-24 | Anthropic | Cowork finance plugins (IB, equity research, PE, wealth) | vertical-outcome, work-context | Front-office finance analyst copilots | [src-20260224-11d529] |
| 2026-02-23 | OpenAI | Frontier Alliances: BCG, McKinsey, Accenture, Capgemini certified practices with OpenAI FDEs | services | Agent deployment boutiques, FDE-heavy startups | [src-20260223-9272a6] |
| 2026-02-05 | OpenAI | Frontier enterprise agent platform: business context semantic layer, execution, memory, evals, agent identity, FDEs | harness-infra, orchestration, work-context | Agent platforms, enterprise agent OS, work-context/semantic layers, agent identity | [src-20260205-ea19f4] |
| 2026-01-30 | Anthropic | Cowork plugins (11 open-source department plugins) | harness-infra, vertical-outcome | Department copilots (sales, legal, support, finance, marketing) | [src-20260130-79791d] |
| 2026-01-11 | Anthropic | Claude for Healthcare (prior auth, claims, CMS/ICD-10/NPI connectors) | vertical-outcome, work-context | Healthcare RCM, prior authorization and claims-appeal agents | [src-20260111-f1affc] |


## Read-across
<!-- dated bullets: which layers look absorbed, which look safe, and why [src] -->
