<!-- OBA theme memo v19, 2026-10-29. Source of truth for exports/OBA-theme-memo-v19-2026-10-29.docx/.pdf. Inline cites show the short source name; bracketed ids map to sources/. Built with /workspace/oba-memo/build.py on the Sewon template. -->

# Enterprise Agents and the Frontier Labs

## Where to focus in AI agents that finish enterprise work, judged by the budget that pays for the work and by what OpenAI and Anthropic will take for themselves

# 1. Investment theses: key takeaways and macro

The theme covers AI agents that finish a defined piece of enterprise work, such as working a denied medical claim or clearing a purchase order exception, and the software that runs them. For every company we ask which budget pays for the work and whether OpenAI or Anthropic will take that work for themselves.

## Key takeaways

- **Focus on vertical companies that finish regulated or messy operational work and answer for the result.** Health plan administration, insurance below the biggest carriers, and procurement and freight are the places to start, because the labs have shipped tools there but left the accountable work.
- **Stay out of legal services and customer service, where the labs and the big software suites now sell the agents and the finished work directly.** In bank compliance, life sciences and finance operations we back only the narrow work the labs leave alone, such as outsourced compliance review, experiments run on a drug company's own data and filings a provider answers for.
- **The money is in the labor budget, which business owners control and which dwarfs what companies spend on software.** The labs still sell mostly tokens and seats to IT and are only now building services arms to reach this budget, so a company that sells the finished job already reaches a different and bigger buyer.
- **The labs give away the generic layers and cannot easily take work that needs private data, write access to core systems, a license or liability for mistakes.** Work that needs those things is where a vertical company can keep its price.
- **Back a horizontal platform only when it runs the actual work and stays neutral across models.** For any company, the test is named enterprise customers running it in production and paying out of an operations budget.

1. **Almost every big enterprise now runs agents in production, but few run them across functions and fewer can show a return**

- Agent usage on the biggest enterprise platforms keeps compounding from one quarter to the next. In a July 2026 survey 95.3% of enterprises ran at least one agent workflow in production (IDC) [src-20260901-8a07a7], and Microsoft counts over 50M agents in its registry, up more than 30% in a quarter (Microsoft earnings call) [src-20261028-51d9ca].
- The measured value shows up much more slowly than the usage does, and most agents stay simple. Only 13% of CIOs report significant or transformational value from AI (Gartner) [src-20261019-a120c4], only 22% of organizations have scaled AI across multiple business units (Gartner) [src-20260901-59ebe1], and the head of Amazon Web Services says most enterprise agents are relatively simple and mostly non-autonomous (AWS interview) [src-20261008-3ac60a].
- Buyers still pay by the seat or by usage, so a company selling finished work does not have to price per outcome. Decision makers rank per-seat pricing first at 42.3%, ahead of consumption at 36.6% and outcome pricing at 21.1% (Futurum) [src-20260817-c3527b], and ServiceNow's finance chief says customers are "not asking at all for outcome pricing" (ServiceNow earnings call) [src-20261028-88124d].

2. **Agents that finish work get paid from the labor budget, which is several times the software budget and is moving to business owners outside IT**

- Every published estimate puts spending on people and outsourcers well above spending on software. Sequoia estimates that "For every dollar spent on software, six are spent on services" (Sequoia) [src-20260305-abed56], Felicis finds labor budgets run 35 times software budgets (Felicis) [src-20240927-2e10b2], and US government data counts 17,753,430 office and administrative support workers at a mean wage of $51,560 (BLS) [src-20260401-ae18ba].
- Outsourcing contracts are already being repriced as agents take over the work people used to do. HFS sees agent-delivered services becoming "a segment worth $422 billion" inside the outsourcing market (HFS Research) [src-20260831-73c927], and a contact center outsourcing executive says the rate his firm can charge fell 20% to 40% in two years (expert call) [src-20260930-124dc3].
- The person who signs for this spend increasingly sits in the business and judges the agent against an outsourcer's invoice. BCG finds that "more than 80% of AI spending now sits outside enterprise IT" (BCG) [src-20260930-591de0], and Sequoia notes that replacing an outsourcing contract with an AI provider "is a vendor swap" while replacing headcount "is a reorg" (Sequoia) [src-20260305-abed56].

3. **Since January the labs have moved from selling models to selling the agent runtime, department agents and their own deployment services**

- The runtime that agent platforms used to sell now comes from the labs at about the cost of tokens. Anthropic launched Managed Agents at $0.08 per session-hour in April (Anthropic) [src-20260408-e5d37b], and OpenAI opened its Agents API in September with no fees beyond tokens and tools (OpenAI) [src-20260910-014b24].
- Both labs now ship agents for whole departments that take a goal through to finished documents and analyses. Anthropic open-sourced 11 Cowork plugins for roles from sales and finance to legal and customer support in January (Anthropic) [src-20260130-79791d], and OpenAI launched ChatGPT Work in July as an agent that can "turn a goal into finished work" (OpenAI) [src-20260709-eb8b16].
- Both labs also moved into services this year, which puts them up against anyone selling deployed work. OpenAI formed a majority-owned deployment company with more than $4B of initial investment (OpenAI) [src-20260511-c3ff64], and Anthropic formed a services firm with Blackstone, Hellman & Friedman and Goldman Sachs aimed at mid-sized companies (Anthropic) [src-20260504-8f8eff].

4. **Vertical companies hold the right to win where the work needs private data, write access, a license or liability, because the labs ship templates and leave the responsibility with the buyer**

- Investors who track the labs closely see the same gap in the operational work the labs avoid. Sapphire Ventures finds that "Labs don't want to handle the operational mess" (Sapphire Ventures) [src-20260416-926244], and Andrej Karpathy points builders to domains that are "valuable, verifiable, and undertrained by frontier labs" (conference summary) [src-20260430-1af2d4].
- A company that does the work keeps the data from doing it, and that data makes the next job better. Bessemer argues that every delivered unit of verifiable work becomes a training signal for the company that delivers it (Bessemer) [src-20260731-169caf], and Menlo Ventures finds that regulatory certification and human sign-off "slow down competitors" (Menlo Ventures) [src-20260407-5d9d8c].

5. **We should back vertical companies with real customers in production, back horizontal platforms only selectively, and treat the labs moving into vertical work as the main risk**

- At least one revenue cycle buyer discounts savings claims it cannot see in its own numbers, so traction has to show up in the customer's records. A revenue cycle executive whose own gains run to a "low-double digit" says of anything higher, "you can pretty much scrub it" (expert call) [src-20260608-5e7d7e].
- Buyers spread their bets across models and want to keep control of their agents themselves, which leaves room for a neutral platform. In a survey 81% of big-company CIOs use three or more model families (a16z CIO survey) [src-20260130-fb2a33], and 67% of agent platform users expect the control plane to sit at least partly outside a provider-managed service (VentureBeat survey) [src-20261005-66e092].
- The labs are adding consultancies and acquisitions to reach enterprise work, which puts their partners as well as the labs in front of vertical buyers. OpenAI's Frontier Alliances bring in BCG, McKinsey, Accenture and Capgemini to deploy its platform (OpenAI) [src-20260223-9272a6], and AI companies bought 195 other AI companies through September 29, with OpenAI making 10 of those deals and Anthropic 5 (Crunchbase via Forbes) [src-20261021-c49bee].
# 2. Interesting categories: where to focus

We split the theme into horizontal software that runs agents across a company, regulated verticals where a license or rulebook governs the work, and non-regulated verticals where the work is operational. Each area is judged on the budget it draws on and on what OpenAI, Anthropic, Microsoft and Google shipped there since January 2026. Where the labs now sell the finished work themselves, or put their own engineers inside the firms that already do the accountable work, we would not focus there. Where they ship tools but leave the accountable work to someone else, the category stays open.

## A. Horizontal

### A1. Orchestration and Execution Platforms

- **Tailwinds: Companies are handing agents real authority faster than they build the controls, which leaves room for a neutral layer that runs and records the work.** In a BCG survey of 1,330 executives, 42% expect agents to hold real decision authority by 2030 while only 5% have the controls in place (BCG) [src-20260930-591de0].
- **Headwinds: Every lab and cloud now ships the generic runtime and control plane for agents, so a company selling only that layer has nothing the labs do not already give away.** OpenAI launched Frontier in February with HP, Oracle, State Farm, Thermo Fisher and Uber as first adopters (OpenAI) [src-20260205-ea19f4], Google turned Vertex AI into the Gemini Enterprise Agent Platform in April (Google) [src-20260422-1f1ec3], and Microsoft sells Agent 365 to govern agents at $15 per user per month (Microsoft) [src-20260501-fc687c].
- **Custom agent systems built by outside engineers rarely last, which hurts any platform sold as a build project.** Gartner expects 70% of enterprises to abandon agent systems built by vendor engineering teams by 2028 because of maintenance costs (Gartner) [src-20261012-11ce4a].
- **Why we should focus here selectively: We should back a horizontal platform only when it runs the work itself across many processes, gets paid from the operations budget and works with any model or cloud.** A platform that resells the runtime or control plane has to beat the labs on price, and the labs give that layer away.

**Example companies:** Duvo, Sycamore, Brain Co

### A2. Work Context

- **Tailwinds: Enterprises expect to tailor agents to how their own business works, which needs context that no model ships with.** In a Deloitte survey of 3,235 leaders, 85% expect to customize agents to fit the unique needs of their business (Deloitte) [src-20260121-231aaa].
- **Headwinds: The labs now bundle company context into their own platforms at no extra charge.** Frontier includes a business context layer that spans warehouses, CRM, ticketing and internal apps (OpenAI) [src-20260205-ea19f4], and Anthropic lets admins package skills and connectors into private plugins for each team (Anthropic) [src-20260224-a28ce9].
- **SAP is buying context about how work gets done for its own HR suite, which squeezes anyone selling that context on its own.** SAP agreed to buy a work context graph company for its HR suite (SAP) [src-20261001-056aad].
- **Why we should focus here selectively: Context is worth backing when a company gathers it by doing the work in a specific process and sells it together with that work.** Context sold as a separate catalog runs into the layers that SAP and the labs now bundle.

**Example companies:** Edra, Workfabric AI

## B. Regulated Verticals

### B1. Healthcare Administration

- **Tailwinds: Federal rules now put deadlines and public reporting on prior authorization, so slow manual review becomes a visible cost for health plans.** A CMS rule requires most affected payers to decide within 72 hours for urgent requests and seven calendar days for standard ones from January 1, 2026 (CMS) [src-20240117-c0af42], and practices complete 39 prior authorization requests per physician per week (AMA) [src-20250424-8f73e8].
- **Headwinds: Both labs launched healthcare products in January, and Anthropic's includes a sample template for the prior authorization review that health plans run today.** OpenAI launched ChatGPT for Healthcare on January 8 with HCA Healthcare, Cedars-Sinai and UCSF and templates that include prior authorization support (OpenAI) [src-20260108-5c4f2d], and three days later Claude for Healthcare added a CMS coverage connector and a customizable prior authorization review template (Anthropic) [src-20260111-f1affc].
- **A revenue cycle executive says the dominant health record vendor blocks outside AI at big health systems, which closes the provider side to most new vendors.** The executive says the vendor does not "allow integrations of AI outside of what they're already working on" (expert call) [src-20260608-5e7d7e].
- **Why we should focus here: Health plans pay for each review or claim, carry the liability when one goes wrong and need write access to their own systems, none of which a lab template provides.** We should back companies that sell to health plans, where the record vendor matters least, and that show results in the plan's own numbers.

**Example companies:** Anterior

### B2. Insurance Operations

- **Tailwinds: Insurers employ big claims and policy teams whose work follows forms, rules and deadlines that agents can follow too.** Government data counts 324,230 claims adjusters, examiners and investigators at a mean wage of $80,470 (BLS) [src-20260401-ae18ba], and HFS expects traditional outsourcing to "decline from 55% to 37% of delivery" within two years (HFS Research) [src-20260831-73c927].
- **Headwinds: Anthropic is building claims agents with Allianz and State Farm adopted OpenAI's agent platform early, so the biggest carriers get custom agents straight from the labs.** Allianz is co-developing motor and health claims agents with Anthropic (Allianz) [src-20260109-a82ace], State Farm was among the first adopters of OpenAI Frontier (OpenAI) [src-20260205-ea19f4], and the listed insurtech Roadzen is launching underwriting and claims agents on Anthropic's managed agent platform (Roadzen filing) [src-20260507-76bd32].
- **Insurers are pitched constantly and keep their data in house, which makes it easy to switch vendors.** An insurance executive says he hears pitches "at least two or three a day" and that "All the data is living within our existing systems" (expert call) [src-20260811-a0aa1e].
- **Why we should focus here: Neither lab sells a finished insurance product, and below the top carriers the work sits inside licensed agencies, smaller carriers and claims administrators that answer to regulators.** We should back companies that hold the license or run the claim for the insurer, because they get paid like the outsourcer they replace and switching away from them means rebuilding the operation.

**Example companies:** Notch, Pace, Harper, Strala

### B3. Lending and Financial Crime

- **Tailwinds: Financial crime compliance is a big and rising cost whose biggest line is people.** It costs institutions in the US and Canada $61 billion a year, and "Labor costs rank highest in financial crime compliance spending" (LexisNexis and Forrester) [src-20240221-19ce25].
- **Headwinds: Anthropic and OpenAI now reach banks through the core banking providers, and FIS now sells an AML investigation agent built with Anthropic to every US bank.** FIS made its AML agent, built with an embedded Anthropic team, available to any US bank in October (FIS) [src-20261015-9b6d2c], Fiserv launched agentOS with OpenAI as a collaborator and an AML triage agent among its four launch agents (Fiserv) [src-20260514-c198a1], and Anthropic's templates include KYC screening (Anthropic) [src-20260505-1c452a].
- **Capital One built its own agent platform, and both labs now sell packages for financial services, so the biggest banks need an outside agent company least.** Capital One built its own agent platform under model risk rules (podcast) [src-20260416-e6896d], and OpenAI built ChatGPT for Financial Services with Morgan Stanley and Evercore (OpenAI) [src-20260910-8f172a].
- **Why we should focus here selectively: The FIS agent only recommends, so the bank still owns every case and the tool layer now comes from the core providers.** Its design partner says "the investigator remains accountable for the final determination" (FIS) [src-20261015-9b6d2c], so we should back only companies that take over the review work lenders, fintechs and regional banks now outsource and that answer to the examiner for it.

**Example companies:** Salient, Bretton AI, Gradient Labs

### B4. Legal Services

- **Tailwinds: Legal work is a big services budget that buyers already pay per matter or per hour to outside firms.** Speakers at a Sequoia event put legal services alone at about $400B in the US (Sequoia event transcript) [src-20260507-37adcc].
- **Headwinds: Anthropic now sells a full legal product and says legal professionals became the most engaged users of its Cowork agent of any knowledge-work function.** Claude for Legal launched in May with 12 practice-area plugins and more than 20 connectors (Anthropic) [src-20260512-5c6e2d], and by October Anthropic had added more than 60 legal connectors and a gallery of legal tools built with law firms and PwC (Anthropic) [src-20261027-c877fb].
- **OpenAI followed in September with a legal configuration of its newest model, and its engineers now build custom tools inside the biggest law firms.** Astra for Law ships with a legal search index and 26 partner plugins, and OpenAI's forward-deployed engineers built tools for Sullivan & Cromwell, Ropes & Gray and Cooley (OpenAI) [src-20260917-10e700].
- **Thomson Reuters rebuilt its CoCounsel product on Anthropic's agent toolkit and also launched a legal model of its own, so the research incumbent now competes on both the lab layer and the product.** It rebuilt CoCounsel on the Claude Agent SDK (Anthropic) [src-20260512-5c6e2d], and in August it launched Thomson 1.0, a model trained on its legal research content, while Google expanded Gemini Enterprise for legal professionals (Reuters) [src-20260917-5df2c2].
- **Why we should not focus here: Both labs, the research incumbents and the biggest law firms are building legal agents on the same models, which leaves little room for a new company to hold its price.** A company that sells legal work under its own license still carries liability the labs avoid, but it now competes with law firms that get custom tools from lab engineers, so we would not focus here.

**Example companies:** Crosby, Lawhive, EvenUp

### B5. Life Sciences Research

- **Tailwinds: Drug research is one of the biggest professional budgets in any industry and keeps growing.** R&D spending at the biggest pharma companies rose to $190Bn in 2024 from $163Bn in 2023 (IQVIA Institute) [src-20250301-62db38].
- **Headwinds: Both labs now sell research products straight to drug companies, and research software stocks fell on the day Anthropic launched its research workbench.** Anthropic named Novo Nordisk and Sanofi as customers in January (Anthropic) [src-20260111-f1affc], OpenAI launched a life sciences model with Amgen and Moderna in April (OpenAI) [src-20260416-fc8cf7], and Schrodinger shares fell as much as 8.3% the day Anthropic launched Claude Science in June, with Recursion and IQVIA also lower (trade press) [src-20260630-55a218].
- **Why we should focus here selectively: Lab workbenches help a drug company's own scientists, while an agent that runs experiments on that company's data for its programs does work the labs leave alone.** Results take years to prove, so we should back only companies that already show repeat paid work at the same drug company.

**Example companies:** Edison Scientific

## C. Non-Regulated Verticals

### C1. Procurement, Logistics and Distribution

- **Tailwinds: Purchasing and freight coordination employ big teams whose work runs on email, portals and phone calls.** Government data counts 491,430 buyers and purchasing agents, 202,810 dispatchers outside emergency services and 97,670 cargo and freight agents (BLS) [src-20260401-ae18ba].
- **Headwinds: OpenAI is building and testing procurement agents that handle purchasing requests inside a single company, starting with its own finance team.** OpenAI is building a procurement agent with PwC inside its own finance team (OpenAI) [src-20260504-c8e2ab] and previewed specialist agents tested on procurement and invoice processing in September (OpenAI) [src-20260929-2fdd0f].
- **ERP suites now ship agents of their own that act inside the purchasing processes they already run.** Oracle launched 22 Fusion Agentic Applications that act inside its business processes (Oracle) [src-20260324-59ab43].
- **Why we should focus here: Those agents handle requests inside one company, while the work we want runs across suppliers, carriers and phone calls outside any single system, where an ERP vendor or a lab agent has no reach.** We should back companies that clear exceptions end to end and can show touchless rates at named manufacturers, freight operators and distributors.

**Example companies:** Fragment, Magentic, Didero, InstaLILY, BackOps, HappyRobot, Freehand

### C2. Finance and Accounting Operations

- **Tailwinds: Finance teams repeat the same work every month with big clerical staffs, and every invoice or reconciliation has a clear count and cost.** Government data counts 1,373,680 bookkeeping, accounting and auditing clerks at a mean wage of $53,560 (BLS) [src-20260401-ae18ba].
- **Headwinds: Both labs now go after the in-house monthly close directly, with templates and consulting partners.** Anthropic's spring financial services release includes a month-end closer (Anthropic) [src-20260505-1c452a], and OpenAI and PwC are building agents for planning, payments, tax and the accounting close (OpenAI) [src-20260504-c8e2ab].
- **Agents cost more to run than the scripted bots finance teams already use, which slows the switch.** An integrator's automation lead says a task costing $200 or $300 a month on bots costs $1,000 or $1,200 a month with AI (expert call) [src-20260825-747be0].
- **Why we should focus here selectively: The generic close is going to the ERP vendors and the labs, so the opening is in work with its own rules and liability.** We should back companies that serve accounting firms or run global payroll, where the company answers for each filing.

**Example companies:** Basis, Niural

### C3. Customer Service and Sales

- **Tailwinds: Customer service is the first job agents finish end to end at scale, because a resolved ticket is easy to check and to price.** OpenAI says its Presence agent resolves 75% of inbound issues on its own phone line without human assistance (OpenAI) [src-20260722-a3993b], and Salesforce says its agents have handled 4.3 million inquiries on its own help site (CX Today) [src-20260926-ff7125].
- **Headwinds: OpenAI, Microsoft and Salesforce now sell finished customer service work themselves, and Salesforce publishes the price.** OpenAI launched Presence in July as a deployed product for production support agents (OpenAI) [src-20260722-a3993b], Microsoft launched Contact Center Intelligence in October on top of existing systems from Cisco and Avaya (Constellation) [src-20261021-e45563], and Salesforce charges $2 per resolution for its help agent (CX Today) [src-20260926-ff7125].
- **Why we should not focus here: Customer service is where agents first finished a whole job, so the labs and the software suites moved in first and now set the price.** We should use its resolution rates and prices as the benchmark for other functions and make no new bets here.

**Example companies:** Sierra, Decagon
