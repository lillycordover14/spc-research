# Outcome-based agents: verified example companies (v12 lists, v11 test, 2026-10-29)

Built for memo v7 after Lilly's feedback on v6 (restore Workfabric, tighten the set, verify every name) and tightened for v8 after the AI-Native Production QA (Otera rename, 18 more cuts, each reason checked on the company's own site on 2026-10-29). Every row cites a filed source id. Company statements are company claims. Where no public price exists, pricing says unknown. Nothing here is estimated.

## The test (v11, 2026-10-29)

Lilly's direction on 2026-10-29: outcome-based agents are not defined by outcome pricing, and the memo lists only the best example companies. The test is now job completion, not the pricing model.

An outcome-based agent company sells an AI agent that:
1. completes a defined unit of work end to end (a resolved ticket, a processed claim, a closed book, a negotiated order, a delivered research run), so the buyer receives finished work rather than a tool its staff operate, and
2. owns the result, meaning the vendor answers for whether the unit was done correctly, the way an outsourcer, TPA, broker, law firm or employee does (stated accountability, a regulated role, a completion guarantee, or billing that excludes failed or escalated work all count as evidence).

Pricing is recorded in the tables as a fact about how the vendor captures value. It no longer decides the verdict. Pricing buckets: outcome (per resolution, per completed unit, savings share, contingency); per-task or usage (per minute, per conversation, per credit, platform fee plus volume); seat or subscription (per user, per agent, revenue band); unknown.

Verdicts (v11):
- **Core**: completes a defined unit of work end to end and owns the result, whatever the pricing.
- **Core (pricing not per result)**: replaces the v8 label "Whole job, not outcome-priced". Under the v11 test these companies pass on job completion; the label is kept so the pricing fact stays visible.
- **Category example (not scored)**: suppliers (A), incumbents (B), platforms (C) and incumbent SIs and BPOs (D), kept as the memo frames them.
- **Exclude**: fails the test (copilot that assists staff, platform for the customer's own team to build agents, or no defined unit of work). Pricing alone is no longer a reason to exclude.

Note on earlier cuts: several v7 and v8 cuts below rested only on pricing (per-minute, per-conversation, per-agent or subscription). Those reasons no longer apply under the v11 test, and the companies are flagged for re-review in the example-company pass (see /workspace/oba-memo/v11-example-notes.md). They are not re-added here.

## Workfabric AI: finding and decision

- **What it sells.** Workfabric sells "missions", long-running business goals such as finding hidden revenue, catching escalations early, recovering cash at risk and seeing what customers want next. On-device "twins" learn how each employee works and coordinate with other twins across teams to surface signals no single team sees (site snapshot, src-20261029-3f0bd1). Its core product, ContextFabric, captures decisions, exceptions, approvals and judgement calls from live workflows so agents have operational context (Moneycontrol, src-20251229-050f87; Cognizant partnership for 1,000 context engineers, src-20250829-31a67a).
- **Traction (company claims).** Live in the Fortune 500, no integrations, running in 48 hours, $380M of net-new pipeline "on track for $1B", 39 days of average warning before escalations (src-20261029-3f0bd1). Moneycontrol says it is live and generating revenue, backed by Bob McGrew and Chris Re (src-20251229-050f87). It is also a Sierra customer that audits Sierra's resolution counts (src-20260318-033caf). Founder podcasts: src-20260408-5408bb, src-20260710-e2a61b.
- **Pricing.** Not public in any source.
- **Verdict.** It does not pass the v11 test. It frames the product around outcomes, but the output is coordinated insight across people, not a defined unit of completed work it owns. It stays a category example in C.
- **Decision.** Restored to C (Horizontal Orchestration and Work Context) as that category's work-context example, listed third after Ema and Duvo, with a new C tailwind sentence citing Moneycontrol. Cutting it in v6 was a mistake for C, where it fits better than Sycamore or Relevance AI. In v8, C lists only Ema, Duvo and Workfabric AI, and the memo says why the horizontal build platforms were moved out.

## A. Agent platforms, frameworks and infrastructure (suppliers)

| Company | Job | Pricing (evidence) | Traction | Verdict | Sources |
|---|---|---|---|---|---|
| OpenAI | Models; Frontier agent platform | not scored (supplier) | Frontier with HP, Intuit, Uber | Category example | src-20260205-ea19f4 |
| Anthropic | Models; agent tooling | not scored (supplier) | n/v here | Category example | src-20260111-f1affc |
| Google | Models; Agents CLI | not scored (supplier) | n/v here | Category example | src-20261021-16f218 |
| Microsoft | Agent 365 governance | not scored (supplier) | nearly 40M agents (claim) | Category example | src-20260729-8b3c16 |
| Amazon Web Services | AgentCore managed agent loop | not scored (supplier) | n/v here | Category example | src-20261022-a0f852 |
| LangChain | Agent framework | unknown | 57% figure in memo | Category example | src-20251202-cd7dc4 |

## B. Systems of record and platform incumbents

Listed with the incumbents already billing per result first.

| Company | Job | Pricing (evidence) | Traction | Verdict | Sources |
|---|---|---|---|---|---|
| Salesforce | Owns Fin; Agentforce | outcome for Fin ($0.99 per resolution) | bought Fin for about $3.6B | Category example (incumbent with core product) | src-20260924-93c5ed, src-20260615-74b583 |
| Zendesk | Support agents | outcome (per automated resolution) | n/v | Category example (incumbent with core product) | src-20250806-3921b6 |
| HubSpot | Support and sales agents | outcome ($0.50 per resolved conversation) | n/v | Category example (incumbent with core product) | src-20260413-63104e |
| ServiceNow | AI Control Tower | subscription (free for a year) | n/v | Category example | src-20260507-e6c2cd |
| SAP | ERP agents | unknown | n/v | Category example | memo B section |
| Oracle | Fusion ERP agents | usage (paid AI units) | n/v | Category example | src-20261003-10d57c |
| Workday | HR and finance agents | unknown | n/v | Category example | memo B section |

## C. Horizontal orchestration and work context

| Company | Job | Pricing (evidence) | Traction | Verdict | Sources |
|---|---|---|---|---|---|
| Ema | Teams of agents running HR, IT and finance processes | outcome (completed tasks, company claim) | bookings $150M+ (claim); $77M Series B | Core | src-20260930-9ee545 |
| Duvo | Executes approved operational workflows across ERPs and portals | per completed run (one flat price per execution) | $32M round 2026-10-14 | Core | src-20260701-3b0c17, src-20260609-4b024f |
| Workfabric AI | Work-context twins coordinating teams on missions | unknown | generating revenue; Cognizant 1,000 engineers | Category example (not scored) | src-20261029-3f0bd1, src-20251229-050f87 |
| Convey | Digital teammates that run invoice processing, reconciliation and reporting; operators train them | unknown (not public) | 1.1M+ hours of work for NBCUniversal, Samsara, Unity, Faire, ChargePoint, TelevisaUnivision (company claim); $38M Series A led by a16z (Jun 2026) | Core (horizontal, close to a platform; Affinity LC) | convey.dev; businesswire.com/news/home/20260617486214 |

## D. Systems integrators and BPOs

AI-native service providers first, then incumbents.

| Company | Job | Pricing (evidence) | Traction | Verdict | Sources |
|---|---|---|---|---|---|
| Crescendo | AI-native CX BPO that sells the finished contact | outcome (per-contact outcome contracts) | n/v | Core | src-20260724-865e53 |
| Otera (previously DeepOpinion) | Autonomous operations for insurance, banking and other regulated back offices; earlier used by Cognizant for insurance claims BPO | outcome (company claim: "Priced on outcomes. Not licenses, not seats, not modules."); no public price; DeepOpinion-era Cognizant deal used per-task credits | Allianz, Erste, Siemens, SAAB named on site; Cognizant deployment | Core (pricing is a company claim) | src-20261029-d6fdcf, src-20260724-b4a442, src-20250627-297f7b |
| Mechanical Orchard | Rewrites mainframe applications end to end into verified production code (Imogen) | unknown (not public) | SulAmerica, a North American bank, a Fortune 100 retailer; $80M+ raised (GV, Emergence, Munich Re Ventures) | Core (Affinity LC Tier 3) | mechanical-orchard.com |
| Tessera Labs | Multi-agent ERP modernization, including SAP ECC to S/4HANA migration | unknown (not public) | $60M Series A led by a16z (May 2026); 9 anonymized case studies, no named customers | Core, early (Affinity LC) | businesswire.com/news/home/20260506853624; a16z.com/announcement/investing-in-tessera-labs |
| Accenture, Deloitte, Cognizant, Teleperformance | Incumbent SIs and BPOs | not scored | public | Category example (not scored) | memo D section |

## E1. Front office: customer service and sales

| Company | Job | Pricing (evidence) | Traction | Verdict | Sources |
|---|---|---|---|---|---|
| Sierra | Resolves customer service contacts for consumer brands | outcome: under $2 per transaction plus about 10% of savings at Safelite | see filed calls | Core | src-20260710-37d40b, src-20241201-958c00 |
| Gradient Labs | Resolves financial-services support and back-office cases | outcome: pay only for successful resolutions, no platform fee | Wise, Yonder, Pockit, SteadyPay listed on site | Core | src-20261029-170473, src-20250530-b93251 |
| Decagon | Resolves support contacts | per conversation by default; per resolution offered; most customers choose per conversation | n/v here | Core (pricing not per result) | src-20261029-58b696, src-20260515-de88a1 |

## E2. Back office: finance, compliance and supply chain

| Company | Job | Pricing (evidence) | Traction | Verdict | Sources |
|---|---|---|---|---|---|
| Basis | Completes tax, audit and close work for accounting firms | outcome: "We never had a seat-based model for our core product", no token pricing; rates not public | $100M Series B (Accel); $1.15B valuation; a third of the US Top 25 firms | Core | src-20260730-3a49fd, src-20260224-b6a4eb |
| Magentic (magentic.com) | Procurement and supply-chain savings agents | outcome: "no win, no fee", paid only on realized savings (summary of company remarks) | $18M Series A; Fortune 500 manufacturers | Core | src-20260723-5994c7, src-20260923-47e348 |
| Freehand | Decides whether to pay, dispute or negotiate each invoice | unknown; CEO says agents "take accountability for the outcome" | $75M seed; Meta, Unilever, J&J, Pfizer | Core (on responsibility claim) | src-20260729-f4bed6 |
| Didero | Runs procurement for manufacturers and distributors | usage: platform fee plus volume kickers | $30M Series A; Novilla renewal quote | Core (pricing not per result) | src-20260617-937cc1, src-20251024-112e5e |
| Salient | Voice and omnichannel agents run auto-loan servicing and collections end to end | unknown (not public) | Westlake, ACA, Exeter, CPS; Westlake CEO cites $12M a year saved; a16z-led Series A; site says $75M raised and $1B+ processed | Core (Affinity LC Tier 3) | trysalient.com; a16z.com/announcement/investing-in-salient; ir.consumerportfolio.com release |
| Bretton AI (formerly Greenlite) | Agents staff KYC/KYB, AML and sanctions investigations; a person approves the case | unknown (not public) | 1.2M+ L1/L2 investigations (claim); one client cut $5.35M of BPO spend (claim); $75M Series B led by Sapphire (Feb 2026); Robinhood, Mercury, Gusto, Lead Bank, Coastal Community Bank | Core (Affinity LC Tier 3) | businesswire.com/news/home/20260209387593 |
| BackOps | Relay agents resolve freight claims, billing and logistics exceptions end to end | unknown (not public) | 500K+ carrier claims at one deployment, 91% resolved without humans (claim); $42M Series B led by Insight (Sep 2026); $26M Series A led by Theory (Mar 2026) | Core (Affinity LC Tier 3) | backops.com/relay; prnewswire Series B release |
| Niural | AI-native global PEO; EMMA executes payroll, onboarding, compliance and payments, and the PEO carries the employer obligation | unknown (not public) | $31M Series A (Jun 2025) extended to $52M (Jun 2026) | Core (Affinity SP 2026 Tier 3) | niural.com/ai; prnewswire Series A and AI Labs releases |

## E3. Regulated services: healthcare, insurance, legal and life sciences

| Company | Job | Pricing (evidence) | Traction | Verdict | Sources |
|---|---|---|---|---|---|
| Procode | Surgical coding and billing, with acquired billing companies | outcome: contingency billing | $10M Series A; 350+ providers | Core | src-20260728-5c2f73 |
| EvenUp | Personal injury demand packages | per demand package | 10,000 cases a week (claim); $150M round | Core | src-20241205-4ac3cf, src-20251007-efb7da |
| Crosby | AI-native law firm reviewing commercial contracts | outcome: per contract, not hourly | $60M Series B; Cursor, Ramp | Core | src-20260331-50e583, src-20261025-1fbd1c |
| Anterior | Auto-approves prior authorizations for health plans | outcome: value-based, can include fees per auto-approved prior authorization | $40M raise, $64M total; Geisinger Health Plan | Core | src-20260213-d1e7fa |
| SmarterDx | Pre-bill review of every chart for missed diagnoses | outcome: pay only for approved and billed findings | $4.5M per 10,000 DRG discharges (claim); UAMS, Novant, McLaren | Core (humans approve findings) | src-20261029-559e73 |
| Reserv | AI-native claims TPA | sells claims handling as a service | $25M Series B; 80+ MGAs, 20 carriers (claim) | Core (on responsibility) | src-20250604-fd80b0 |
| Strala | AI-native claims TPA from first notice to payout and subrogation | unknown | $51.3M raised; Founders Fund, Emergence | Core (on responsibility) | src-20260401-133cee |
| Harper | AI-native commercial insurance brokerage | brokerage commission (terms not in source) | $46.8M; 5,000+ customers | Core (on responsibility) | src-20260225-3917a2 |
| Lawhive | AI-native consumer law firm (UK and Arizona) | unknown fee model; regulated firm of record | revenue above $35M, up 7x; $60M Series B | Core (on responsibility) | src-20260205-e13567 |
| Pace (withpace.com) | Replaces insurance BPO work (claims QA, servicing) | usage with a floor at one insurer | $46M Series B; Prudential, Palomar; Palomar COO says it resolves more than 90% of cases without a human touch (claim) | Core (pricing not per result) | src-20260811-a0aa1e, src-20261025-c77b6e, src-20261029-99058e |
| Edison Scientific | Kosmos research runs for biopharma | per-run credits at launch ($200), retired May 2026 | $70M seed; Incyte | Core (pricing not per result) | src-20251105-cdfbed, src-20260519-9cb3f1 |
| TJM Labs | Pharmacy agents do intake, data entry, refills and prior-auth support; a pharmacist verifies | unknown (not public) | 550+ pharmacies and 1M+ tasks a day (site, Oct 2026); $100M total incl. $75M Series B led by Elephant; acquired EncoreRx and Pharmesol | Core (Affinity LC Tier 3) | tjmlabs.com/ai-agents-for-pharmacy |
| Adaptive Innovations (adaptive.co) | AI-native home health provider that delivers the care and runs intake, scheduling, charting and billing | unknown (not public) (licensed provider billing for care) | $50M Series A led by Felicis and Bain Capital Ventures, $60M total (Jun 2026) | Core (on responsibility; Affinity LC Tier 3) | adaptive.co/blog/introducing-adaptive-innovations |
| Alaffia Health | Agents plus clinician review run health-plan payment integrity, utilization review and appeals | unknown (not public) | $55M Series B led by Transformation Capital (Feb 2026) | Core (Affinity SP 2026) | businesswire.com/news/home/20260203113559 |

## Cut from the memo lists in v12 (Affinity screen, 2026-10-29)

Lilly asked for only the best names after the v11 redefinition. Rows for these companies were removed from the section tables above; their filed sources stay in sources/. New names come from insights/affinity-oba-screen-2026-10-29.md, which holds the evidence URLs (not yet filed as source records).

| Company | Was in | Reason | Sources |
|---|---|---|---|
| Distyl AI | D | Builds agents for enterprises; ownership of a unit of work not shown | src-20250922-1bc8b4 |
| TCS, Conduent | D | Trimmed to keep the incumbent list tight | memo D section |
| Lorikeet | E1 | Passes, but traction not verified; weaker than Sierra, Decagon and Gradient Labs | src-20261029-0118e7 |
| Vida | E1 | Agent OS for leads and service; not best in class | src-20261008-fb6a3d |
| Sable | E1 (v11 only) | Runs demos and qualification, a step in the sale rather than an owned result (AI-Native Production QA, v11) | fortune.com 2026/07/16 Sable article |
| fileAI | E2 | Document extraction; traction not verified | src-20261012-e6c2b7 |
| Lio | E2 | Traction thin next to Didero and Magentic | src-20260305-fefcb3 |
| HappyRobot, Augment | E2 | Logistics brokerage agents fit the finance and procurement focus poorly; BackOps carries supply chain | src-20250903-f1a523; Augment row in v11 |
| Prosper AI | E3 | Part per-minute; not best in class | src-20261023-cc2e6e |
| Amperos Health | E3 | Weaker than SmarterDx and Procode | src-20260422-d6ae9d |
| GenHealth.ai | E3 | Not best in class | src-20261008-50f3eb |

## Cut from the memo lists in v8

Each reason was checked on the company's own site on 2026-10-29 or in the filed source named. Cresta, Sixfold and Pactum stay in the memo body as evidence.

| Company | Was in | Reason | Sources |
|---|---|---|---|
| CopilotKit | A | Developer SDKs and the AG-UI protocol for in-app copilots, not a supplier the memo needs to name | src-20261029-0e1811 |
| Sycamore | C | Now sells Forge and Guard, an agent operating system for enterprises to build and govern their own agents | src-20261029-4e4c26 |
| Relevance AI | C | Sells Invent, a tool for customer teams to build their own AI workforces | src-20261029-6a85cf |
| UiPath | C | RPA and business orchestration platform sold as a license | uipath.com homepage, company card |
| Parloa | E1 | Priced per minute for voice and per interaction for chat | src-20261029-95b348 |
| PolyAI | E1 | Priced per connected minute | src-20261029-dabc99 |
| Cresta | E1 | Mainly per-minute pricing, and much of the suite assists human reps in real time (still cited in the body) | src-20260618-f36dc6, src-20261029-ee1f31 |
| Omilia | E1 | No public pricing; the platform includes CSR CoPilot real-time assistance for reps alongside voice agents | src-20261029-cfa241, src-20260806-53e2bf |
| Definite | E2 | Now an ontology layer for finance data; its site says "Your team does the analysis" (usedefinite.com; definite.ai is a different company) | src-20261029-0b05f0 |
| Adaptive (adaptive.build; a different company from Adaptive Innovations in E3) | E2 | Sold as construction accounting software with agents; no outcome pricing stated | src-20261029-93fb4a |
| Pactum | E2 | Annual subscription by revenue band, no success fee (still cited in the body) | src-20261029-a2fafb |
| Elimentary | E2 | Early YC company; no public pricing; one unnamed customer | src-20261023-c1d343 |
| Zomma | E2 | Early YC company; no public pricing; two pilots | src-20261023-36cc4e |
| Walter | E2 | Spring 2026 YC company; no public pricing or named customers | src-20261023-aee4fa |
| Sixfold | E3 | Underwriting AI that supports underwriters, who keep the decision; no public pricing (still cited in the body) | src-20261029-dd9fd4, src-20260129-3fadee |
| FurtherAI | E3 | Sold as an underwriting and claims platform; no public pricing | src-20261029-23a59e |
| Tennr | E3 | Sold as a patient orchestration platform; no public pricing | src-20261029-91d43b |
| Candid Health | E3 | Sold as a revenue cycle automation platform; no public pricing | src-20261029-c03bec |

DeepOpinion was not cut: it is the old name of Otera (deepopinion.ai redirects to otera.ai, and the site header reads "previously DeepOpinion"), so the two rows were merged.

## Cut from the memo lists in v7

| Company | Was in | Reason | Sources |
|---|---|---|---|
| 11x | E1 | Exclude: AI SDRs avoid outcome pricing; 80% to 90% churn per a former advisor | src-20250703-8a38e7, src-20250507-e13bdd |
| Artisan | E1 | Exclude: same AI SDR evidence; pricing not disclosed | src-20250703-8a38e7, src-20241031-1d55b6 |
| Rox | E1 | Exclude: sales agent platform for reps, pricing not disclosed | src-20260312-b92bcd |
| Actively AI | E1 | Exclude: agent advances deals with the rep; no defined unit or price (still cited in the body as evidence) | src-20260428-2d177a |
| Xelix | E2 | Exclude: AP control software; pricing not disclosed in filed sources (still cited in the body) | src-20250721-54e512 |
| Tabs | E2 | Exclude: billing system, subscription by revenue band with agents included | src-20261029-795928 |
| Stuut | E2 | Exclude: collections software; pricing not disclosed in filed sources (still cited in the body) | src-20251120-b7dfc3 |
| Thoughtful AI | E3 | Exclude: priced per agent, not per transaction | src-20240919-474182 |
| Wordsmith | E3 | Exclude: platform and inbox for in-house legal teams | src-20260603-a6ea11 |
| Notch | E3 | Exclude: AI operating system for regulated ops; pricing not disclosed | src-20260325-5584af |
| Adonis | E3 | Exclude: RCM orchestration platform; pricing not disclosed | src-20260325-9a969a |
| Assort Health | E3 | Exclude: patient call and scheduling voice agent; pricing not disclosed | src-20251002-499204 |

## Reviewed but not added (not verified to our standard)

- Ada (E1): the agent does the whole contact, but Ada argues for per-conversation pricing (src-20250718-aac9a5). Filed as counter-evidence.
- Siena AI, Maven AGI, Yellow.ai, Forethought (E1): third-party pages report per-ticket or per-resolution prices. Not filed, not added.
- Infinitus, AKASA, EtherMed, ClarityCare (E3): pricing comes only from third-party snippets or is not public. Not added.
- SMB collections tools on contingency (Receivable, Syntharra, Recoup and others): small, unverified vendors. Not added.

## Counts (50 names across the v12 lists)

| Verdict | n |
|---|---|
| Core | 28 (C 3, D 4, E1 2, E2 7, E3 12) |
| Core (pricing not per result) | 4 (E1 1, E2 1, E3 2) |
| Category example, not scored | 18 (A 6, B 7, C 1, D 4) |

Pricing is unknown (not public) for all 10 names added from the Affinity screen; their verdicts rest on the work the agent completes and who answers for it.

## Counts (52 names across the v8 lists, kept for history)

| Verdict | n |
|---|---|
| Core | 23 (C 2, D 2, E1 4, E2 5, E3 10) |
| Core (pricing not per result) | 8 (E1 1, E2 3, E3 4) |
| Unclear under v11 | 1 (D 1, Distyl AI) |
| Category example, not scored | 20 (A 6, B 7, C 1, D 6) |
| Excluded and cut | 30 (12 in v7, 18 in v8) |

Under the v8 test, of the 23 core names, 18 passed on a disclosed per-outcome or per-unit price (Otera's is a company claim with no public price) and 5 pass on responsibility for the result (Freehand, Reserv, Strala, Harper, Lawhive). Pricing is unknown for 8 of the 32 scored companies (Distyl AI, Freehand, Lio, HappyRobot, Strala, Lawhive, Amperos Health, GenHealth.ai), so the verdicts on those rest on what the agent does, not on how it is paid.

Under the v11 test (job completion and ownership), the 8 "Core (pricing not per result)" names are scored on the work the agent completes, and pricing no longer affects the count. Distyl AI stays flagged, because the filed source shows it building agents for enterprises, not owning a unit of work.
