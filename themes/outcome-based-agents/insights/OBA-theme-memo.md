<!-- OBA theme memo v25, 2026-10-29. Source of truth for exports/OBA-theme-memo-v25-2026-10-29.docx/.pdf. Inline cites show the short source name; bracketed ids map to sources/. Built with /workspace/oba-memo/build.py on the Sewon template. -->

# Enterprise Agents and the Frontier Labs

## What enterprises and the frontier labs are doing in AI agents that finish enterprise work, and which budget pays for that work

# 1. Key takeaways

The theme covers AI agents that finish a defined piece of enterprise work, such as working a denied medical claim or clearing a purchase order exception, and the software that runs them. Enterprises are adopting these agents quickly, while OpenAI, Anthropic, Microsoft and Google are moving from selling models toward selling the agents and the deployment work themselves.

1. **Agents that finish work get paid from labor and services budgets, which are many times bigger than software budgets and are increasingly controlled by business owners rather than IT**

- Companies spend far more paying people and outsourcers to do their work than buying the software those people use. Sequoia estimates that six dollars go to services for every dollar spent on software (Sequoia) [src-20260305-abed56], Felicis puts labor budgets at 35 times software budgets (Felicis) [src-20240927-2e10b2], and US government data counts 17,753,430 office and administrative support workers earning a mean wage of $51,560 (BLS) [src-20260401-ae18ba].
- Outsourcing contracts are the first part of that spending to be repriced, because agents can take over work that outsourcers bill by the hour or by the head. HFS expects agent-delivered services to become a $422 billion segment inside the outsourcing market by 2035 (HFS Research) [src-20260831-73c927], and the Vice President of Client Services at TTEC, a contact center outsourcing company, says agents are moving the industry's billing from a price per worker to a price per use (TTEC interview) [src-20260930-124dc3].
- Decisions about AI spending have moved out of the information technology (IT) department and into the business units that run the work, where an agent is weighed against an outsourcer's invoice. BCG finds that AI spending doubled in a year to 3.3% of revenue and that more than 80% of it now sits outside the enterprise IT budget (BCG) [src-20260930-591de0], and Sequoia argues that replacing an outsourcing contract with an AI provider is a simple change of vendor, while replacing headcount means reorganizing the company (Sequoia) [src-20260305-abed56].

2. **Almost every big enterprise now runs agents, but few can show a return yet, and buyers still pay for AI mostly by the seat or by usage**

- Agent use has spread across big companies quickly, both in surveys of enterprises and in the agent counts the main platforms report. In a July 2026 survey 95.3% of enterprises ran at least one agent workflow in production (IDC) [src-20260901-8a07a7], and Microsoft counts over 50M agents in its registry, up more than 30% in a quarter (Microsoft earnings call) [src-20261028-51d9ca].
- Returns lag well behind that usage, because most agents that enterprises have built still do simple, narrow and mostly supervised tasks. Only 13% of chief information officers (CIOs) report significant or transformational value from AI (Gartner) [src-20261019-a120c4], only 22% of organizations have scaled AI across multiple business units (Gartner) [src-20260901-59ebe1], and Matt Garman, chief executive of Amazon Web Services, describes most enterprise agents as relatively simple and mostly non-autonomous (AWS interview) [src-20261008-3ac60a].
- With returns still unproven, buyers distrust savings claims and keep paying the way they always have. For AI features billed separately, decision makers rank per-seat pricing first at 42.3%, ahead of consumption at 36.6% and outcome pricing at 21.1% (Futurum) [src-20260817-c3527b], and ServiceNow's finance chief says its customers are not asking for outcome pricing at all (ServiceNow earnings call) [src-20261028-88124d]. The Vice President of Operations at Health Prime, which runs billing and collections for healthcare providers, says the firm's own cost improvement from AI averages in the low double digits and he dismisses claims of savings above 20% (Health Prime interview) [src-20260608-5e7d7e].

3. **Since January the labs have moved from selling models to selling the agent runtime, ready-made department agents and their own deployment services, on the strength of fast-growing enterprise revenue**

- Businesses now account for most of the revenue at both Anthropic and OpenAI, and that revenue is growing fast. Anthropic reported revenue of $16.29 billion for the first half of 2026, up from $1.16 billion a year earlier, with most of it coming from businesses paying per use (Reuters) [src-20261026-f0b182], and OpenAI's finance chief said in August that enterprise now brings in more revenue than consumers (Unite.AI) [src-20260814-6efa2b], with annualized revenue of roughly $50 billion at the end of September (Bloomberg) [src-20261008-d13758].
- The software that runs agents, which agent platforms used to sell on its own, now comes from the labs at close to the cost of the tokens it uses. Anthropic launched Managed Agents at $0.08 per session-hour in April (Anthropic) [src-20260408-e5d37b], and OpenAI opened its Agents API in September with no fees beyond tokens and tools (OpenAI) [src-20260910-014b24].
- On top of that runtime both labs ship ready-made agents for whole departments that take a goal through to finished documents and analyses. Anthropic open-sourced 11 Cowork plugins for roles from sales and finance to legal and customer support in January (Anthropic) [src-20260130-79791d], and OpenAI launched ChatGPT Work in July as an agent that turns a goal into finished work (OpenAI) [src-20260709-eb8b16].
- To get those agents into production the labs are adding people and acquisitions as well as products. OpenAI formed a majority-owned deployment company with 19 partners that took over a firm of about 150 engineers who build systems on site at customers (OpenAI) [src-20260511-c3ff64], Anthropic formed a services firm with Blackstone, Hellman & Friedman and Goldman Sachs aimed at mid-sized companies (Anthropic) [src-20260504-8f8eff], and OpenAI's Frontier Alliances bring in BCG, McKinsey, Accenture and Capgemini to deploy its platform (OpenAI) [src-20260223-9272a6]. OpenAI made 10 acquisitions of AI companies through September 29 and Anthropic made 5 (Crunchbase via Forbes) [src-20261021-c49bee].
- Buyers are hedging against any single lab by spreading their bets across models and keeping control of their own agents. In a survey 81% of big-company CIOs use three or more model families (a16z CIO survey) [src-20260130-fb2a33], and 67% of agent platform users expect the control plane to sit at least partly outside a provider-managed service (VentureBeat survey) [src-20261005-66e092].

4. **The labs ship templates and tools but leave the work that needs private data, write access to core systems, a license or liability with the buyer and its service providers**

- Lab products stop at the template and leave the buyer responsible for the outcome, because running a regulated or messy operation is slow, local and risky work. Sapphire Ventures finds that the labs do not want to take on the operational mess of running work for customers (Sapphire Ventures) [src-20260416-926244].
- The data agents work on and the people who answer for a deployment also come from outside the labs. Anthropic's finance plugins pull market data from FactSet, MSCI, S&P Global and LSEG through connectors and plugins those data owners provide (Anthropic) [src-20260224-11d529], and Cognizant is training more than 18,000 engineers to build and deploy Google's Gemini agents and says they stay accountable through architecture, engineering and last-mile deployment (CIO Dive) [src-20261022-d5ad54].
# 2. Interesting categories

We split the theme into horizontal software that runs agents across a company, regulated verticals where a license or rulebook governs the work, and non-regulated verticals where the work is operational. In each category the lab moves are those OpenAI, Anthropic, Microsoft and Google made from January 2026 onward.

## A. Horizontal

### A1. Orchestration and Execution Platforms

**What is happening:**

- **Companies are handing agents real authority faster than they build the controls to govern them.** In a BCG survey of 1,330 executives, 42% expect agents to hold real decision authority by 2030, yet only 5% have the controls in place (BCG) [src-20260930-591de0].
- **Custom agent systems built by outside engineers are expensive to keep running, and Gartner expects most of them to be dropped.** Gartner expects 70% of enterprises to abandon agent systems built by vendor engineering teams by 2028 because of maintenance costs (Gartner) [src-20261012-11ce4a].
- **OpenAI, Google and Microsoft now each sell a general platform for running and governing agents across a company.** OpenAI launched Frontier in February with HP, Oracle, State Farm, Thermo Fisher and Uber as first adopters (OpenAI) [src-20260205-ea19f4], Google turned Vertex AI into the Gemini Enterprise Agent Platform in April (Google) [src-20260422-1f1ec3] and says nearly 90% of the Fortune 100 use Gemini Enterprise (Alphabet earnings call) [src-20260722-52c762], and Microsoft charges $15 per user per month for Agent 365 to govern agents (Microsoft) [src-20260501-fc687c].
- **How likely the labs are to absorb this: High.** The labs and the big clouds already sell this layer to many of the biggest companies, as the Fortune 100 uptake of Gemini Enterprise shows, and the main limit on them is that buyers want to keep at least part of their control plane outside any single provider.

**Example companies:** Duvo, Sycamore

### A2. Work Context

**What is happening:**

- **Enterprises expect to tailor agents to how their own business works, which requires knowledge about the company that no model ships with.** In a Deloitte survey of 3,235 leaders, 85% expect to customize agents to fit the unique needs of their business (Deloitte) [src-20260121-231aaa].
- **SAP agreed in October to buy a company that maps how work gets done and plans to keep that knowledge inside its own human resources (HR) software.** SAP says the acquired company is expected to become an intelligent core of its SuccessFactors HR suite (SAP) [src-20261001-056aad].
- **The labs now bundle company knowledge into the agent platforms they sell to enterprises.** Frontier includes a business context layer that spans data warehouses, customer relationship management (CRM) systems, ticketing and internal apps (OpenAI) [src-20260205-ea19f4], and Anthropic lets administrators package skills and connectors into private plugins for each team (Anthropic) [src-20260224-a28ce9].
- **Microsoft grounds its own long-running agent in its Work IQ layer and reports wide uptake among the biggest companies.** Copilot Cowork, built with Anthropic, became generally available in June, runs on Work IQ and is used by over half of the Fortune 500 (Microsoft) [src-20260616-28211f].
- **How likely the labs are to absorb this: Medium.** The labs and Microsoft bundle company knowledge for their own agents and SAP keeps what it buys inside its own suite, but no lab yet sells a knowledge layer that spans every application and serves any model.

**Example companies:** Edra, Workfabric AI

## B. Regulated Verticals

### B1. Healthcare Administration

**What is happening:**

- **Prior authorization is the step where a health insurer must approve a treatment before a doctor provides it, and it consumes a big share of staff time on both sides.** Physicians report 39 prior authorization requests per physician per week and 13 hours a week of physician and staff time spent on them, and insurers running private Medicare Advantage plans received more than 50 million requests in 2023 (AMA and KFF) [src-20250424-8f73e8].
- **A federal rule now sets deadlines for those approvals, which makes slow manual review a visible cost for health plans.** Under a rule from the Centers for Medicare & Medicaid Services (CMS), the US agency that runs Medicare and Medicaid, affected health plans must decide urgent requests within 72 hours and standard ones within seven calendar days from January 1, 2026, give a specific reason for every denial and publish their approval statistics each year (CMS) [src-20240117-c0af42].
- **On the provider side, the dominant electronic health record vendor decides which AI tools run inside big health systems.** The Vice President of Operations at Health Prime, a firm that runs billing and collections for healthcare providers, says the vendor does not allow outside AI integrations beyond what it already works on (Health Prime interview) [src-20260608-5e7d7e].
- **Both labs launched healthcare products in January, and both include help with prior authorization.** OpenAI launched ChatGPT for Healthcare on January 8 with HCA Healthcare, Cedars-Sinai and UCSF and templates that include prior authorization support (OpenAI) [src-20260108-5c4f2d], and three days later Claude for Healthcare added a connector to CMS coverage data and a customizable prior authorization review template (Anthropic) [src-20260111-f1affc].
- **How likely the labs are to absorb this: Medium.** Both labs have named health system customers and a prior authorization template, but under the CMS rule the approval decision and its deadline stay with the health plan, and inside hospitals the record vendor limits which outside AI tools can run.

**Example companies:** Anterior

### B2. Insurance Operations

**What is happening:**

- **Insurers employ big claims and policy teams whose work follows forms, rules and deadlines that agents can follow too.** Government data counts 324,230 claims adjusters, examiners and investigators at a mean wage of $80,470 (BLS) [src-20260401-ae18ba], and HFS expects traditional outsourcing to "decline from 55% to 37% of delivery" within two years (HFS Research) [src-20260831-73c927].
- **Insurance buyers are flooded with agent vendors but keep their data in their own systems.** The Head of Strategic Partnerships at Accelerant Holdings, a risk exchange serving more than 250 managing general agents (MGAs, firms that write policies on behalf of insurers), says vendors pitch the team two or three times a day and that all of the team's data lives within the company's existing systems (Accelerant interview) [src-20260811-a0aa1e].
- **Anthropic is building claims agents with Allianz, and State Farm was among the first carriers to adopt OpenAI's agent platform.** Allianz is co-developing motor and health claims agents with Anthropic (Allianz) [src-20260109-a82ace], State Farm was among the first adopters of OpenAI Frontier (OpenAI) [src-20260205-ea19f4], and the listed insurance software company Roadzen is launching underwriting and claims agents on Anthropic's managed agent platform (Roadzen filing) [src-20260507-76bd32].
- **How likely the labs are to absorb this: Medium.** The labs build claims agents with the biggest carriers and supply the platform that others build on, but no lab sells a packaged insurance product yet, and buyers like Accelerant keep their data inside their own systems.

**Example companies:** Notch, Pace, Harper, Strala

### B3. Lending and Financial Crime

**What is happening:**

- **Financial crime compliance is a big and rising cost whose biggest line is people.** It costs institutions in the US and Canada $61 billion a year, and labor is the biggest cost within that spending (LexisNexis and Forrester) [src-20240221-19ce25].
- **The biggest banks either build agents on their own or work directly with the labs on products.** Capital One built its own agent platform under model risk rules (podcast) [src-20260416-e6896d], and OpenAI built ChatGPT for Financial Services with Morgan Stanley and Evercore (OpenAI) [src-20260910-8f172a].
- **Anthropic and OpenAI now reach the rest of the banks through the companies that run their core banking systems.** FIS made its anti-money laundering (AML) agent, built with an embedded Anthropic team, available to any US bank in October (FIS) [src-20261015-9b6d2c], Fiserv launched agentOS with OpenAI as a collaborator and an AML triage agent among its four launch agents (Fiserv) [src-20260514-c198a1], and Anthropic's financial services templates include know your customer (KYC) screening, with Citadel, BNY and FIS among its named customers (Anthropic) [src-20260505-1c452a].
- **The FIS agent recommends a decision and leaves each case with the bank's own investigators.** The design partner for the FIS agent says "the investigator remains accountable for the final determination" (FIS) [src-20261015-9b6d2c].
- **How likely the labs are to absorb this: High.** Through FIS the labs can now reach any US bank with an investigation agent, and their own templates cover KYC screening, though the bank's investigators still own every final determination.

**Example companies:** Salient, Bretton AI, Gradient Labs

### B4. Legal Services

**What is happening:**

- **Legal work is a big services budget that buyers already pay per matter or per hour to outside firms.** Speakers at a Sequoia event put legal services alone at about $400B in the US (Sequoia event transcript) [src-20260507-37adcc].
- **Anthropic now sells a full legal product and says legal professionals became the most engaged users of its Cowork agent of any knowledge-work function.** Claude for Legal launched in May with 12 practice-area plugins and more than 20 connectors (Anthropic) [src-20260512-5c6e2d], and by October Anthropic had added more than 60 legal connectors and a gallery of legal tools built with law firms and PwC (Anthropic) [src-20261027-c877fb].
- **OpenAI followed in September with a legal version of its newest model, and its engineers now build custom tools inside several of the biggest law firms.** Astra for Law ships with a legal search index and 26 partner plugins, and OpenAI engineers working on site built tools for Sullivan & Cromwell, Ropes & Gray and Cooley (OpenAI) [src-20260917-10e700]. OpenAI's own usage research shows weekly active enterprise Codex users in legal grew 108-fold from February, faster than in any other function it reported (Unite.AI) [src-20260814-6efa2b].
- **Thomson Reuters, the main legal research company, works both with the labs and alongside them.** Anthropic describes its CoCounsel Legal as a legal agent built on the Claude Agent SDK, Anthropic's software development kit for agents (Anthropic) [src-20260224-a28ce9], and in August Thomson Reuters launched Thomson 1.0, a model trained on its own legal research content, while Google expanded Gemini Enterprise for legal professionals (Reuters) [src-20260917-5df2c2].
- **How likely the labs are to absorb this: High.** Both labs sell complete legal products, lab engineers build tools inside top law firms and the main research company built its legal agent on a lab toolkit, which makes legal one of the categories where the labs are most competitive.

**Example companies:** Crosby, Lawhive, EvenUp

### B5. Life Sciences Research

**What is happening:**

- **Drug research is one of the biggest professional budgets in any industry and keeps growing.** Research and development spending at the biggest pharma companies rose to $190Bn in 2024 from $163Bn in 2023 (IQVIA Institute) [src-20250301-62db38].
- **Anthropic sells research products straight to drug companies, and research software stocks fell on the day it launched its research workbench.** Anthropic named Novo Nordisk and Sanofi as customers in January (Anthropic) [src-20260111-f1affc], and Schrodinger shares fell as much as 8.3% the day Anthropic launched Claude Science in June, with Recursion and IQVIA also lower (trade press) [src-20260630-55a218].
- **OpenAI has its own life sciences model, which left research preview in September and is sold to drug companies through a vetted access program.** OpenAI launched GPT-Rosalind in April with Amgen and Moderna among its customers and made it generally available to eligible organizations on September 11, alongside a free Codex plugin that connects to more than 50 public databases, literature collections and biology tools (OpenAI) [src-20260416-fc8cf7].
- **How likely the labs are to absorb this: Medium.** Both labs sell research models and workbenches to named drug companies and research software shares have already fallen on their launches, but these products are tools for each drug company's own scientists rather than research the labs run themselves.

**Example companies:** Edison Scientific

## C. Non-Regulated Verticals

### C1. Procurement, Logistics and Distribution

**What is happening:**

- **Purchasing and freight coordination employ big teams whose work runs on email, portals and phone calls.** Government data counts 491,430 buyers and purchasing agents, 202,810 dispatchers outside emergency services and 97,670 cargo and freight agents (BLS) [src-20260401-ae18ba].
- **Oracle now ships 22 agentic applications of its own that act inside the business processes its enterprise resource planning (ERP) suite already runs.** Oracle launched its Fusion Agentic Applications in March as teams of specialized agents that run on Fusion data (Oracle) [src-20260324-59ab43].
- **OpenAI's procurement agents are still being built and tested inside its own finance team.** OpenAI is building a procurement agent with PwC for its own finance team (OpenAI) [src-20260504-c8e2ab] and in September previewed specialist agents that it had tested internally on procurement and invoice processing (OpenAI) [src-20260929-2fdd0f].
- **How likely the labs are to absorb this: Low.** OpenAI's procurement work so far is an internal agent and a preview, and Oracle's agents act inside its own ERP, so no lab product yet covers supplier and carrier work that runs across companies.

**Example companies:** Fragment, Magentic, Didero, InstaLILY, BackOps, HappyRobot, Freehand

### C2. Finance and Accounting Operations

**What is happening:**

- **Finance teams repeat the same work every month with big clerical staffs, and every invoice or reconciliation has a clear count and cost.** Government data counts 1,373,680 bookkeeping, accounting and auditing clerks at a mean wage of $53,560 (BLS) [src-20260401-ae18ba].
- **Agents still cost several times more to run than the scripted bots finance teams already use.** The Vice President of Digital Transformation at Accenture puts a task at $200 or $300 a month on scripted bots and $1,000 or $1,200 a month with AI (Accenture interview) [src-20260825-747be0].
- **Both labs now go after the in-house monthly close directly, with templates and a big accounting firm as partner.** Anthropic's spring financial services release includes a month-end closer (Anthropic) [src-20260505-1c452a], and OpenAI and PwC are building agents for planning, payments, tax and the accounting close (OpenAI) [src-20260504-c8e2ab].
- **How likely the labs are to absorb this: Medium.** Both labs target the monthly close with templates and PwC, but neither has named a finance team running a lab close agent in production, and agents still cost several times more to run than existing bots.

**Example companies:** Basis, Niural

### C3. Customer Service and Sales

**What is happening:**

- **Customer service is the first job agents finish end to end at scale, because a resolved ticket is easy to check and to price.** OpenAI says its Presence agent, launched in July, resolves 75% of inbound issues on its own phone line without human assistance (OpenAI) [src-20260722-a3993b], and Salesforce says its agents have handled 4.3 million inquiries on its own help site (CX Today) [src-20260926-ff7125].
- **Salesforce now sells finished service work at a published price, and Microsoft launched an AI layer for contact centers that sits on the systems buyers already run.** Salesforce charges $2 per resolution for its help agent (CX Today) [src-20260926-ff7125], and Microsoft launched Contact Center Intelligence in October on top of existing systems from Cisco and Avaya (Constellation) [src-20261021-e45563].
- **Some big buyers in Europe still rule the labs out because they cannot see where the labs store data or what they do with it.** A Senior Vice President at Deutsche Telekom who oversees marketing, procurement, training, ESG (environmental, social and governance) and compliance and evaluates its customer support AI says OpenAI and Anthropic are largely ruled out there over EU data concerns, and that the company runs several specialist vendors and plans to cut to one or two in about 18 months (Deutsche Telekom interview) [src-20260727-3b21a8].
- **How likely the labs are to absorb this: High.** OpenAI, Microsoft and Salesforce already sell finished service work, which makes this the category where the labs and the big software suites are most competitive, and the main limit is European buyers like Deutsche Telekom that rule the labs out over EU data concerns.

**Example companies:** Sierra, Decagon
