# Working thesis: outcome-based agents and agentic orchestration

_Seeded 2026-10-23 from Lilly's brief. This is the living version: every claim should end with a source id once we have one. Nothing below is sourced yet; treat it as hypotheses to test._

## Definition
AI agents that complete enterprise work end to end and are bought on outcomes (per task, per resolution, share of savings) rather than per seat, plus the layers that let a large enterprise run many agents in production: the harness (runtime, tools, memory, evals, permissions), orchestration (coordinating many agents across systems with governance), and context on how work actually gets done.

The stack we use throughout (see `taxonomy.yml`): 1. model labs, 2. harness and infrastructure, 3. orchestration, 4. work context, 5. vertical outcome agents, 6. services and SIs.

## Why now (to source)
- The model labs have moved from selling models to selling enterprise agent platforms and domain solution sets over the last 6 to 9 months [src: TBD]
- Vendors are publicly experimenting with outcome pricing (per resolution, per task) [src: TBD]
- Surveys claim fast growth in agent deployment, while other studies say most pilots fail to reach production [src: TBD]

## Preliminary thesis (hypotheses)
1. Labs will absorb the generic harness. Building blocks like tool use, memory, computer use and basic orchestration become part of the lab platforms, so a horizontal harness company needs a reason to exist beyond "neutral".
2. What labs cannot see from outside is how a specific enterprise's work actually gets done: process data, exceptions, permissions, systems of record. That context, if it compounds and the vendor keeps rights to use it, may be the durable layer.
3. Outcome pricing is a go-to-market wedge into labor and BPO budgets, not proof of a moat. It works where the outcome is countable (a resolved ticket, a processed invoice) and fails where attribution is fuzzy.
4. Adoption at large enterprises today runs through services (SIs, forward-deployed engineers). The companies that win may look part-services for years; the question is whether margins converge.
5. Systems of record (Salesforce, ServiceNow, SAP, Workday) are the strongest incumbents because they hold the data and permissions; an independent orchestration layer has to be meaningfully better across systems to survive.

## What would make us wrong (test by 2026-10-29)
- Large enterprises are already running many agents in production with outcome contracts that renew, and they buy from startups, not labs or systems of record.
- Lab platforms are failing in the enterprise for reasons a startup can fix structurally (neutrality across models, liability, deployment), not just temporarily.
- A startup in orchestration or work context shows compounding customer value that a lab plus an SI cannot replicate within 12 months.

## Where SPC can play
- Enterprise GTM and sales-motion expertise is scarce for technical founders selling to Fortune 500 COOs and CIOs.
- Candidates for a first look: Sycamore (orchestration), Duvo (execution OS with outcome measurement), Workfabric (work context). See `companies/`.

## Running conclusions
<!-- dated bullets, newest first, source ids -->
