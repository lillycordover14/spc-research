# Learning path: outcome-based agents and agentic orchestration

Reading path for getting up to speed fast, Day 1 basics through Day 4 expert. Every item is filed in this repo. Each line gives what you'll understand afterwards and how it ties to the questions. Items marked ★ carry the `must-read` tag. Back to [best-of](best-of.md).

## 1. State of play: are agents in production?

2-hour version: read items marked (2h) in order.

- (2h) Gartner 13% of CIOs see value [src-20261019-a120c4]: the value gap behind the hype (Q1)
- (2h) Gartner 17% in production and the FDE warning [src-20261012-11ce4a] (Q1, Q5)
- ★ McKinsey state of AI 2026 [src-20260825-e5c5c1] (Q1, Q4)
- ★ MIT NANDA GenAI Divide [src-20250701-e3ae84] (Q1, Q3)
- Levie and Chase on slow enterprise diffusion [src-20260629-015aae] (Q1, Q3)
- Gravitee security survey [src-20261012-fb5063] and Modern Data Survey [src-20261020-76881e]: what blocks production (Q3)

## 2. The stack and who builds the harness

- (2h) ★ Claude Managed Agents [src-20260408-e5d37b] and outcomes update [src-20260519-55cca6]: what a lab harness absorbs (Q6, Q7)
- (2h) Cognizant Gemini group and FDE postings [src-20261022-d5ad54]: the SI world (Q5)
- DXC OASIS on LangChain [src-20261013-1dcd15]: an SI-built harness in production (Q5)
- (2h) Chase on when to build your own harness [src-20260813-09fcee]: build vs buy and lock-in (Q6, Q7)
- Decagon on open-source models [src-20260731-a07321]: why an app keeps its own harness (Q6, Q11)
- Murty on FDEs as a services play [src-20260710-e2a61b] (Q5)
- McDermott on the AI control tower [src-20260417-a917fe] and Dines on the map of work [src-20260921-f28021] (Q8)
- Katz on what survives in the harness: runtime, security, cost [src-20261019-54d838] (Q6, Q7, Q11)
- Akkiraju on buy front end, build back end [src-20260427-1a7ad0] and Capital One's in-house platform [src-20260416-e6896d] (Q3, Q5)
- ServiceNow Arc on Nvidia OpenShell [src-20261021-4e9ddf]: system of record as governance plane (Q8)

## 3. Outcome pricing and unit economics

- (2h) ★ Cheeky Pint, Bret Taylor [src-20260310-ad2c26]: how per-resolution contracts work (Q2)
- (2h) HackerNoon pricing ladder with ICONIQ numbers [src-20260924-1b6619] (Q2, Q11)
- (2h) ★ a16z, price the highest layer you can attribute [src-20260827-fb556f] (Q2, Q11)
- ★ Bessemer pricing playbook [src-20260210-496d37]: margins and hybrids (Q2, Q11)
- Traynor on how Intercom picked $1 per resolution [src-20251002-0b85b2] and McCabe on 99 cents vs $20-30 human cost [src-20250821-666ad1] (Q2)
- Zendesk CEO on AI ARR and paid-if-solved [src-20260805-5a9fa7]; Intercom CFO on resolution rate and margin [src-20260522-b1dbe3] (Q2, Q11)
- Taylor on FDE tied to outcome pricing [src-20260309-78d5a1] and Medina on the outcome bonus [src-20250422-de3b52] (Q2, Q5)
- Agentforce $2 per resolution [src-20260926-ff7125] (Q2, Q8)
- Exotel on budgeting and ramp [src-20261019-d96d4c] (Q3, Q4)
- LangChain routing cut cost per thread 64% [src-20261022-ae18f2] (Q11)

## 4. Companies and the investable set

- (2h) ★ Sequoia, Services: The New Software [src-20260305-abed56] (Q9, Q10)
- (2h) [W44 readout](weekly/2026-W44.md): investable table and call questions (Q9, Q13-Q15)
- a16z Lassie memo [src-20260603-ce0e80]: labor as the unit of value (Q9)
- Decagon [src-20261013-d7909a], Duvo [src-20261014-1d5d80], Sycamore [src-20260330-8d6266] (Q9, Q10, Q12)

## Glossary

- Outcome pricing: charge per completed result (resolution, lead), not per seat or token.
- Harness: the runtime loop, tools, memory, evals and guardrails around a model.
- FDE: forward deployed engineer, vendor engineers embedded at the customer.
- System of record: the incumbent app holding the canonical data (CRM, ITSM, ERP).
