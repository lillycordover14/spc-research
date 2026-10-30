# Labs, layers, vertical vs horizontal, and adoption: research pass (2026-10-29)

Scope: three questions Lilly asked on 2026-10-29. What OpenAI and Anthropic can and cannot easily absorb, layer by layer. Whether to back vertical or horizontal. Whether large enterprises run many agents in production, and whether they pay for outcomes or seats. Evidence window Apr 2025 to Oct 2026, weighted to the last 6 to 9 months. Every claim carries a [src] id from this theme or a URL. Sources filed this pass are flagged (new).

---

## Q1. What can the labs easily absorb?

### Bottom line

The labs are absorbing everything model-adjacent and horizontal: the harness and runtime, memory, evals, multi-agent orchestration, tracing, connectors, department templates and the general "coworker" surface. As of 2026 they are also buying their way into services through FDE armies and PE-backed delivery companies. They have not shown they can absorb five things: proprietary data and verifiers, write access and accountability inside systems of record, regulated liability, multi-model and multi-cloud neutrality, and owned outcome delivery in gritty, fragmented markets. Their incentive to move up is margin. Their limit is focus. Plenty of operators and VCs share that view, but it is not unanimous (see disagreements).

### Layer-by-layer read

| Layer | Absorb risk | Why | Evidence |
|---|---|---|---|
| Model | Owned by labs | Oligopoly, but enterprises route across models. 81% use 3+ model families. Customers building with multiple models on Foundry up 5x YoY | [src-20260130-fb2a33] (new), [src-20261028-51d9ca] (new) |
| Agent framework / harness / runtime | High | Anthropic Managed Agents at $0.08 per session-hour; OpenAI Agents API with no fee beyond tokens; AWS AgentCore Harness. Chase: LangChain keeps rebuilding as labs absorb earlier hacks. Katz: harness choice barely moves coding eval scores | [src-20260408-e5d37b], [src-20260910-014b24], [src-20261022-a0f852], [src-20261017-d3bed0], [src-20261019-54d838] |
| Evals, graders, tracing | High but unstable | Anthropic outcomes grader and OpenTelemetry tracing; OpenAI bought Promptfoo. But OpenAI is winding down Agent Builder and Evals, gone from 2026-11-30, so labs also exit layers they enter | [src-20260519-55cca6], [src-20261014-2e6208], [src-20260309-b2ac14], [src-20251006-d9ec32] (new) |
| Orchestration / control plane | Contested | OpenAI Frontier and Microsoft Agent 365 (50M+ agents in registry) want to be the control point. But VB Pulse: only 2% picked a platform for the model, and 67% expect the control plane at least partly outside the provider. Battery: orchestration moves into the model and product layer | [src-20260205-ea19f4], [src-20261028-51d9ca] (new), [src-20261005-66e092], [src-20260123-b88941] |
| Context, memory, connectors | High for generic, low for portable | Forbes/HumanX: basic connectors, cost dashboards and single-session memory are platform "features". Portable cross-model memory is a "position" no lab will credibly sell. A context layer drifted from 90% to 60% accuracy in two months, so upkeep is real work | [src-20261021-c49bee] (new), [src-20261020-7922f1] |
| Department templates / horizontal work agents | High | Cowork plugins, unified Claude chat and Cowork GA for Enterprise (usage-priced), ChatGPT workspace agents, OpenAI specialist dots for procurement and AP. Feb 2026 selloff: Goldman estimated about $2T wiped off stocks in a week | [src-20260130-79791d], [src-20261023-4ee362] (new), [src-20260422-75a0a8], [src-20260929-2fdd0f], [src-20260210-153efa] (new) |
| Vertical workflow and data | Medium, rising | Labs now ship regulated-vertical front ends: Claude for FS (2025-07-15, https://www.anthropic.com/news/claude-for-financial-services), FS agent templates, legal plugins, Claude for Healthcare, Claude for Life Sciences (2025-10-20, https://www.anthropic.com/news/claude-for-life-sciences), ChatGPT for FS, GPT-Rosalind. They lean on licensed data partners and SIs instead of owning the data or the liability | [src-20260505-1c452a], [src-20260512-5c6e2d], [src-20260111-f1affc], [src-20260910-8f172a] (new), [src-20260416-fc8cf7] (new) |
| Services / outcome delivery | Medium, new in 2026 | OpenAI DeployCo: majority owned, 19 partners led by TPG, more than $4B, ~150 FDEs via Tomoro. Anthropic, Blackstone, H&F and Goldman services firm ($1.5B per CNBC) targets PE-owned mid-market. Plus Claude Partner Network ($100M), Frontier Academy (10,000 FDEs), Frontier Alliances. Rao: "Enterprise demand for Claude is significantly outpacing any single delivery model." | [src-20260511-c3ff64] (new), [src-20260504-8f8eff] (new), [src-20260312-73c25c], [src-20261002-8d9e4f], [src-20260223-9272a6] |

### What the labs shipped (dated)

Full table, about 42 rows, in insights/labs-vs-startups.md. The highlights, newest first:

- 2026-10-23 Anthropic: unified Claude chat and Cowork GA for Enterprise; managed cloud sandboxes; "Claude Enterprise pricing stays usage-based." [src-20261023-4ee362] (new)
- 2026-10-22 Anthropic: full Claude Platform, including Managed Agents, on Google Cloud [src-20261022-d0a3a2]
- 2026-10-21 Anthropic: Claude Duet, a proactive always-on agent (preview) [src-20261021-7532a5]
- 2026-10-14 Anthropic: native OpenTelemetry agent tracing [src-20261014-2e6208]
- 2026-10-02 Anthropic: Frontier Academy, $100M to train 10,000 FDEs [src-20261002-8d9e4f]
- 2026-09-29 OpenAI DevDay: specialist dots (procurement, AP), Agents API computer use, Marketplace with 32 partners [src-20260929-2fdd0f]
- 2026-09-10 OpenAI: Agents API public beta, no fee beyond tokens [src-20260910-014b24]; ChatGPT for Financial Services (Morgan Stanley and Evercore design partners; data from Daloopa, PitchBook, LSEG, Crunchbase, Quartr) [src-20260910-8f172a] (new)
- 2026-07-22 OpenAI: Presence voice and chat CX agents, FDE and SI led [src-20260722-a3993b]
- 2026-06-03 OpenAI: notice winding down Agent Builder and Evals (off 2026-11-30) [src-20251006-d9ec32] (new)
- 2026-05-19 Anthropic: Managed Agents outcomes grader, multi-agent, memory [src-20260519-55cca6]
- 2026-05-12 Anthropic: legal plugins and connectors [src-20260512-5c6e2d]
- 2026-05-11 OpenAI: Deployment Company (DeployCo) [src-20260511-c3ff64] (new). Axios: $10B pre-money and a guaranteed minimum 17.5% return to investors (https://www.axios.com/2026/05/11/openai-deployco-private-equity)
- 2026-05-05 Anthropic: 10 FS agent templates (close, recon, audit, KYC) [src-20260505-1c452a]
- 2026-05-04 Anthropic: services company with Blackstone, H&F and Goldman [src-20260504-8f8eff] (new)
- 2026-04-22 OpenAI: workspace agents in ChatGPT [src-20260422-75a0a8]
- 2026-04-16 OpenAI: GPT-Rosalind life sciences model (Amgen, Moderna, Thermo Fisher) [src-20260416-fc8cf7] (new)
- 2026-04-08 Anthropic: Claude Managed Agents at $0.08 per session-hour [src-20260408-e5d37b]
- 2026-03-12 Anthropic: Claude Partner Network, $100M [src-20260312-73c25c]
- 2026-03-09 OpenAI: acquires Promptfoo [src-20260309-b2ac14]
- 2026-02-24 Anthropic: enterprise plugin marketplaces and finance plugins [src-20260224-a28ce9], [src-20260224-11d529]
- 2026-02-23 OpenAI: Frontier Alliances (BCG, McKinsey, Accenture, Capgemini) [src-20260223-9272a6]
- 2026-02-05 OpenAI: Frontier enterprise agent platform [src-20260205-ea19f4]
- 2026-01-30 Anthropic: Cowork plugins [src-20260130-79791d]
- 2026-01-11 Anthropic: Claude for Healthcare [src-20260111-f1affc]
- 2025-10-20 Anthropic: Claude for Life Sciences (https://www.anthropic.com/news/claude-for-life-sciences)
- 2025-10-16 Anthropic: Agent Skills (https://www.anthropic.com/news/skills), later donated to the Agentic AI Foundation (https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation)
- 2025-10-06 OpenAI: AgentKit (Agent Builder, Connector Registry, ChatKit, evals) [src-20251006-d9ec32] (new)
- 2025-09-29 Anthropic: Claude Agent SDK (https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)
- 2025-07-15 Anthropic: Claude for Financial Services (https://www.anthropic.com/news/claude-for-financial-services)

Hyperscalers are absorbing the same layers: AWS AgentCore and $1B in FDEs [src-20261022-a0f852], [src-20260730-e4cc74]; Google Gemini Enterprise Agent Platform and FS and legal specializations [src-20260422-1f1ec3], [src-20261008-d5cbe2]; Microsoft Agent 365 and Copilot Cowork [src-20260501-fc687c], [src-20260616-28211f].

### What credible voices say

- **a16z, Yellow Brick Road (2026-05-27):** the obvious stack of strong model, off-the-shelf connectors and an orchestration layer is the most dangerous place to build, because labs absorb it. Durable companies are vertical by default and own the system of work. [src-20260527-b0d3f3]
- **a16z CIO survey (2026-01-30):** "the reported death of third party apps is greatly exaggerated". Enterprises have moved away from fine-tuning toward routing across models. [src-20260130-fb2a33] (new)
- **Sequoia, Ascent 2026 keynote (third-party transcript):** labs come at the market "tech-out" and startups "customer-back". "The diffusion gap is the opportunity for companies building at the application layer." [src-20260507-37adcc] (new)
- **Karpathy at Ascent:** look for domains that are "valuable, verifiable, and undertrained by frontier labs". Coding and math are already targeted. [src-20260430-1af2d4] (new)
- **Foundation Capital:** labs see what works through API traffic and bake it in. They are "aggressively training agents inside simulated versions of the top 150 websites and every major system of record." [src-20261029-b22bb6] (new)
- **Sapphire (2026-04-16):** "Labs don't want to handle the operational mess". Narrow, clean jobs are ones "a frontier lab can ship ... directly". Labs face conflicting priorities, including maximizing token revenue. [src-20260416-926244] (new)
- **RunLLM founders (2026-01-08):** inference is "low-margin and high-volume", so labs move into apps. Generic enterprise search is the least defensible. Differentiation comes from workflow complexity. [src-20260108-90b476] (new)
- **Forbes / HumanX (2026-10-21), the feature vs position test:** connectors, cost dashboards and single-session memory are features. Portable memory, multi-cloud neutrality, domain workflow QA and decision logic are positions. Positions erode too: Workday made its own audit trail mandatory, and Opaque's team joined Anthropic. VC-backed AI firms bought 195 AI startups through Sept 29; OpenAI made 10 of those buys and Anthropic 5. [src-20261021-c49bee] (new)
- **Levie (Box):** would not bet on one or two labs capturing 95% of value. The gap between 70% and 97% accuracy decides whether a process can be automated. [src-20260915-68c6ef]
- **Edison Scientific:** pharma wants models trained on its own data and no single-provider lock-in. [src-20260526-6ea6d3]

### Disagreements

- **Will orchestration stay independent?** Battery says it moves into the model and product layer [src-20260123-b88941], and the labs plus Microsoft are building control planes [src-20260205-ea19f4], [src-20260501-fc687c]. Against that, buyers say they want the control plane outside the provider [src-20261005-66e092], and the Forbes neutrality argument holds [src-20261021-c49bee].
- **Will labs really go vertical?** Inside the Forbes piece, Chalkias (Mysten) says vertical is "a distraction" and labs will buy instead of build [src-20261021-c49bee]. The 2026 launch list shows labs shipping FS, legal, healthcare and life-sciences products anyway, though they lean on partners for data and delivery.
- **Is the harness a moat?** Chase sees value in the harness, which labs keep absorbing [src-20261017-d3bed0]. Katz finds harness choice barely matters for quality [src-20261019-54d838]. Writer's Habib, quoted in Forbes, says "The harness decides how the model works" [src-20261021-c49bee].
- **Lab services: threat or validation?** DeployCo and the Anthropic PE firm compete head on with services-as-software startups. They also show generic coworkers cannot do the job alone, which is a16z's reading [src-20260527-b0d3f3].

---

## Q2. Vertical or horizontal?

### Bottom line

Lean vertical and outcome-owning, weighted toward regulated or operationally gritty markets that are fragmented across many mid-sized buyers. Horizontal is investable only where neutrality is the product: cross-model, cross-cloud governance, memory or identity that no lab or hyperscaler can credibly sell about itself. Even there, expect squeeze and M&A rather than standalone scale. Generic horizontal agents, builders, connectors and enterprise search are the most exposed.

### Bull case: vertical

- Value goes to whoever controls the delivery layer. Verifiable output means each unit of work is a free RL environment. Professional services are about 13% of US GDP. Bessemer [src-20260731-169caf] (new)
- Sell the work, not the tool. For every software dollar, six go to services. Sequoia Bek [src-20260305-abed56]
- Vertical AI goes after labor budgets, which lifts the old vertical SaaS TAM ceiling (about 30 horizontal vs 7 vertical SaaS companies above $10B). Menlo [src-20260407-5d9d8c] (new)
- Labs avoid gritty, fragmented markets. Horizontal vendors "need concentrated, high-value customers to make deployment economics work." Sapphire [src-20260416-926244] (new)
- Durable companies are vertical by default and judged on the customer's P&L. a16z [src-20260527-b0d3f3]
- Applied AI sold as agents, priced on resolution, favors startups because incumbents struggle to change business models. Bret Taylor [src-20250514-093b59]
- Advantage comes from learning loops in high-exception work and owning the execution layer. Foundation Capital [src-20261029-b22bb6] (new)

### Bear case: vertical

- Labs now ship vertical front ends in the richest regulated verticals (FS, legal, healthcare, life sciences) with licensed data partners [src-20260505-1c452a], [src-20260910-8f172a] (new), [src-20260416-fc8cf7] (new), [src-20260111-f1affc].
- 65% of G2000 buyers prefer incumbent solutions when available [src-20260130-fb2a33] (new). Gartner says buyers default to embedded incumbent agents [src-20260916-b894eb]. Vertical SoR owners (Oracle, Workday) are shipping native agents and gating access [src-20260324-59ab43], [src-20261021-c49bee].
- Build vs buy: 32% of McKinsey respondents decided against buying at least one software product because they could build it [src-20260825-e5c5c1].
- Outcome-heavy delivery can compress margins. One AI-native BPO said margins "did tank heavily" [src-20260724-865e53].
- Vertical TAM can be too small for a venture outcome. Sapphire's counter is that markets which look small are exactly the ones labs ignore [src-20260416-926244] (new).

### Bull case: horizontal

- Multi-model is the norm: 81% of buyers use 3+ model families [src-20260130-fb2a33] (new), and multi-model customers on Foundry are up 5x [src-20261028-51d9ca] (new). That creates room for a neutral control plane. 67% expect it to sit at least partly outside the provider [src-20261005-66e092].
- Neutrality is a position labs cannot credibly sell ("Google cannot credibly promise neutrality about Google") [src-20261021-c49bee] (new).
- A huge agent sprawl needs governing. Microsoft has 50M+ agents in its registry, up 30%+ QoQ [src-20261028-51d9ca] (new). IDC counts 45 non-human identities per human [src-20260901-8a07a7] (new).
- Levie would not bet on one or two labs taking 95% of value [src-20260915-68c6ef].

### Bear case: horizontal

- The "obvious" horizontal stack gets absorbed [src-20260527-b0d3f3]. Thin wrappers have an "incredibly low" survival rate (Lessin) [src-20260513-e7a907] (new). Generic enterprise search is the least defensible [src-20260108-90b476] (new).
- Labs and hyperscalers bundle runtime, memory, evals and governance at token or seat prices: Managed Agents at $0.08 per session-hour, the Agents API with no extra fee, Agent 365 at $15 per user [src-20260408-e5d37b], [src-20260910-014b24], [src-20260501-fc687c].
- Neutral positions get bought or squeezed (Opaque to Anthropic; Workday's mandatory audit trail) [src-20261021-c49bee] (new).

### Regulated vs non-regulated split

- **Regulated (FS, insurance, healthcare, legal, collections):** defensive moats such as certification, human sign-off and compliance set a floor on displacement (Menlo) [src-20260407-5d9d8c] (new). Rule-dense work like FDCPA, TCPA and Reg F collections is a messy problem bundle labs avoid (Sapphire) [src-20260416-926244] (new). Liability stays parked with a human in the loop on lab platforms [src-20261021-c49bee] (new). Pharma wants its own data and no lock-in [src-20260526-6ea6d3].
  - Counterpoint: these are also where labs aim first, through partners and data licensing [src-20260505-1c452a], [src-20260910-8f172a] (new), [src-20260111-f1affc]. Their PE services firm targets healthcare, FS and manufacturing in the mid-market [src-20260504-8f8eff] (new). So regulation slows labs but does not stop them. The moat is owning the accountable outcome, not just the domain prompts.
- **Non-regulated horizontal functions (sales, marketing, support, IT, generic back office):** most exposed to Cowork and ChatGPT department plugins, specialist dots and incumbent embedded agents [src-20260130-79791d], [src-20260929-2fdd0f], [src-20261008-5bb82b]. CX is the exception with real outcome-priced scale, but it now faces OpenAI Presence [src-20260722-a3993b].

### Disagreements

- **Menlo, Sapphire, Bessemer, Sequoia and a16z** lean vertical and outcome. **Battery** (2026-01-23) says durable companies look like "SaaS with AI superpowers" more than loosely orchestrated agents [src-20260123-b88941], which is closer to incumbents than to services-as-software.
- **Writer's Habib** (horizontal platform) argues domain QA can live inside a horizontal product [src-20261021-c49bee] (new).
- The a16z CIO survey shows buyers moving from DIY to packaged apps [src-20260130-fb2a33] (new), while McKinsey shows build substituting for buy [src-20260825-e5c5c1].

---

## Q3a. Are large enterprises running many agents in production?

### Bottom line

Many agents, yes. Many autonomous, scaled, value-producing agents, not yet. Nearly every large enterprise has at least one agent workflow in production, and agent registries are in the tens of millions. But scaled, cross-functional or autonomous deployment sits at roughly a quarter to two-fifths of large firms. Under half of pilots convert, and only about 1 in 8 CIOs report significant value. The curve steepened in 2026: consumption is growing very fast off a small base.

### Evidence (newest first)

| Date | Source | Datapoint |
|---|---|---|
| 2026-10-28 | Microsoft FY27 Q1 | "Over 50 million agents are now in the registry, up over 30% quarter-over-quarter." Agents open more than 1/3 of GitHub PRs. Unilever order taking and coupon disputes run as a "fully agentic touchless system" [src-20261028-51d9ca] (new) |
| 2026-10-28 | ServiceNow Q3 2026 | "Year-to-date, agentic AI consumption in production is up 13x year-over-year." $1M+ AI deals up 4.5x. L1 service desk specialist "in full autonomous production". "Over 100 customers" on AI specialists. AI ACV target $1.7B against $3,988M quarterly subscription revenue [src-20261028-88124d] (new), [src-20261028-7a8f1c] (new) |
| 2026-10-19 | Gartner (n=2,002 CIOs) | 13% report significant or transformational value; about 1 in 5 use cases succeed [src-20261019-a120c4] |
| 2026-10-08 | KPMG Q3 Pulse ($1B+ firms, n=314) | 62% building, deploying or developing agents (53% prior quarter); 25% run multi-agent systems vs 6% [src-20261008-1ab8b8] |
| 2026-10-08 | AWS Garman | Most agents are simple and not autonomous [src-20261008-3ac60a] |
| 2026-09 (deck) | IDC FERS Wave 4, July 2026 | 95.3% run at least one production agent workflow, about 11 on average; about 1 in 3 have a cross-functional multi-agent solution; under 50% of PoCs convert [src-20260901-8a07a7] (new). 67% overran agent budgets by more than 10% [src-20261029-18aa48] (new) |
| 2026-09-10 | Oracle | 2,300 agents in production [src-20260910-fa41de] |
| 2026-09-08 | Benioff | The vast majority of customers are still at the beginning [src-20260908-2d6352] |
| 2026-08-31 | Gartner CIO 2027 planning | 37% deployed agentic AI, 34% more within 12 months (17% in April) [src-20260831-2bda07], [src-20260415-f936e3] |
| 2026-08-25 | McKinsey (n=1,719) | 40% of $1B+ firms scaling agents vs 27% a year earlier; EBIT impact flat at 37% [src-20260825-e5c5c1] |
| 2026-08-04 | OSF Digital (SI) | About 20% of clients are serious in Agentforce production [src-20260804-3aa89c] |
| 2026-04-29 | Microsoft FY26 Q3 | Nearly 90% of the F500 have active agents built with Microsoft low-code tools [src-20260429-8a8712] |
| 2026-02-24 | Anthropic's Jensen | 2025 agent hype "mostly premature" [src-20260224-7eb23d] |
| 2026-01-30 | a16z CIO (G2000) | 78% use OpenAI in production; Anthropic 44%, or 63%+ including testing [src-20260130-fb2a33] (new) |
| 2026-01-21 | Deloitte | 25% moved 40%+ of pilots to production [src-20260121-231aaa] |
| 2026-01-19 | Mayfield | 42% have agents in production [src-20260119-2b35fb] |
| 2025-12-09 | Menlo | Only 16% of enterprise deployments are true agents [src-20251209-1f66cf]. 2026 report pending; the 2026-10-15 preview flags about 5x spend growth (https://www.linkedin.com/posts/menlo-ventures_matt-murphy-joined-andrew-ross-sorkin-this-activity-7516506641861705728-nhTO) |
| 2025-07-16 | Capgemini | 2% fully scaled [src-20250716-cb70b8] |
| 2025-07-01 | MIT NANDA | 95% of organizations get zero return [src-20250701-e3ae84] |
| 2025-06-25 | Gartner | 40%+ of agentic projects canceled by 2027 [src-20250625-8a6cff] |

### Disagreements

- **Definitions drive the spread.** "At least one workflow" (IDC 95%) and registry counts (Microsoft 50M) measure breadth. "Scaling" (McKinsey 40%), "deployed" (Gartner 37%) and "true agents" (Menlo 16%) measure depth. Value surveys (Gartner 13%, MIT 95% zero return) measure payoff. Cisco's 5% in-production figure is vendor research cited secondhand [src-20261003-10d57c]. Weight it low.
- **Vendors vs buyers.** Incumbents report steep consumption growth [src-20261028-88124d] (new), [src-20261028-51d9ca] (new). Benioff and Garman concede most usage is early or simple [src-20260908-2d6352], [src-20261008-3ac60a].

---

## Q3b. Outcomes vs seats

### Bottom line

Enterprises mostly pay seat plus usage. Outcome pricing is real but a minority: about 10 to 23% of vendors and about 13 to 19% of services deals. It is concentrated in CX resolution pricing and AI-native vendors. Incumbents say buyers are not asking for it, and buyers want predictable AI budgets. Gartner expects outcome pricing to stay under a quarter of tech services contracts through 2031. The direction is toward measurable units (credits, cases, resolutions), not pure value share.

### Evidence

- **Vendor mix:**
  - ICONIQ: outcome-based pricing rose from 18% to 23% of AI product vendors in six months; consumption from 35% to 42% [src-20260715-e16b49].
  - Bain: about 10% of AI-native and hybrid vendors use outcome pricing [src-20261012-e6c2b7]. Much "outcome" pricing is really output pricing, and about 1 in 5 AI-natives are still mostly per-seat [src-20260810-21fe8d].
  - Poyar data via a buyer's guide: seat-based fell from 21% to 15%, hybrid rose from 27% to 41% [src-20261017-be23bc].
- **Deal mix:** Gartner (Coshow): "Only 19% of services buyers and 13% of service agreements on the seller side" use outcome arrangements. Under 25% of tech CEO services contracts through 2031. "More buzz than reality." [src-20260831-c59649] (new)
- **Buyer preference:**
  - Futurum 2H 2026: for separately billed AI, per-seat ranks first at 42.3%, consumption 36.6%, outcome 21.1%. For core software, per-seat ranks last at 12.6%. ETR data does not yet reward pure outcome-priced vendors [src-20260817-c3527b] (new).
  - a16z: 27 of 50 technical buyers prefer credits tied to recognizable work, vs 14 for tokens [src-20260827-fb556f].
  - KPMG: 74% run AI cost reviews [src-20261008-1ab8b8]. IDC: 67% overran agent budgets [src-20261029-18aa48] (new).
- **Incumbents:**
  - ServiceNow CFO: customers "quite happy with the hybrid model ... and are not asking at all for outcome pricing". McDermott: customers like "the predictability of the seat-based pricing model". [src-20261028-88124d] (new)
  - Microsoft: "expanding from per seat subscriptions to include consumption"; credit-consuming Copilot customers up 75%+ QoQ [src-20261028-51d9ca] (new).
  - Salesforce: AWUs are a usage meter, and outcome pricing is one option [src-20260826-0b53e8], [src-20260826-580137].
  - SAP outcome pricing is a 2028+ story [src-20261021-551046]. Workday and Oracle price on usage [src-20260827-79de17], [src-20261008-c5856f].
  - Anthropic: Claude Enterprise "stays usage-based" [src-20261023-4ee362] (new).
- **Where outcome pricing works:**
  - Fin at $0.99 per resolution [src-20260312-1f35f8].
  - Agentforce at $2 per resolution [src-20260926-ff7125].
  - Zendesk counts only fully AI-resolved interactions [src-20260831-c59649] (new).
  - Pega charges a fixed fee per completed case [src-20260831-c59649] (new).
  - Sierra outcome units and the Safelite contract [src-20260930-9b1413], [src-20260710-37d40b].

### Disagreements

- **Taylor and Sequoia vs buyers.** Taylor and Sequoia argue outcome pricing is the startup wedge [src-20250514-093b59], [src-20260305-abed56]. Buyer data says predictability beats value share [src-20260817-c3527b] (new), [src-20261028-88124d] (new).
- **Margin risk.** An incumbent said outcome pricing hurt a quarter [src-20260812-1b0bca]. An AI-native BPO saw margins "tank heavily" [src-20260724-865e53]. A buyer preferred transactional pricing [src-20260708-a5fc76].
- **Analyst direction vs observed share.** Gartner's analyst guidance says move away from seats toward activity or outcome contracts [src-20260831-c59649] (new). Its own observed share is low.

---

## Sources filed this pass (all under themes/outcome-based-agents/sources)

src-20261028-88124d, src-20261028-7a8f1c, src-20261028-51d9ca, src-20260130-fb2a33, src-20260731-169caf, src-20260504-8f8eff, src-20261023-4ee362, src-20260511-c3ff64, src-20260910-8f172a, src-20260416-fc8cf7, src-20251006-d9ec32, src-20260901-8a07a7, src-20261029-18aa48, src-20260817-c3527b, src-20260831-c59649, src-20261021-c49bee, src-20261029-b22bb6, src-20260108-90b476, src-20260407-5d9d8c, src-20260416-926244, src-20260513-e7a907, src-20260210-153efa, src-20260507-37adcc, src-20260430-1af2d4.

Data caveats:
- **No captured body:** the OpenAI DeployCo, ChatGPT for FS and GPT-Rosalind records have no body (the site blocks scripted fetch). Facts come from pages read on 2026-10-29.
- **Dates:** IDC deck date is set to the upload month. The Foundation Capital and IDC blog pages are undated, so their ids carry today's date.
- **Secondhand transcripts:** the Sequoia keynote is a third-party transcript, and the TWiST item is a third-party summary.
