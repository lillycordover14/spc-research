<!-- OBA theme memo v13, 2026-10-29. Source of truth for exports/OBA-theme-memo-v13-2026-10-29.docx/.pdf. Inline cites show the short source name; bracketed ids map to sources/. Built with /workspace/oba-memo/build.py on the Sewon template. -->

# Outcome-Based Agents and Agentic Orchestration

## What our research says about agents that finish enterprise work, which layers the model labs cannot absorb, and where we should push further

# 1. Investment theses: tailwinds, key takeaways and macro

This theme covers AI agents that complete a piece of enterprise work from start to finish, such as resolving a support ticket, working a denied medical claim or clearing a purchase order exception, and the orchestration software that lets a company run many agents under common rules. We read the 898 filed sources behind the theme, including 55 expert-call transcripts and 54 podcasts (our source count) [insights/memo-qa-checklist.md], together with our sourcing lists, a dedicated pass on what the model labs can absorb and the launches they shipped over the past nine months. The first three theses answer whether the market has tipped, which layer the labs cannot absorb and who we can back today, and the fourth gives our view on outcome pricing and whether to research it further.

1. **Partly, because almost every big enterprise now runs some agents in production but few run many of them at scale across functions, and buyers pay through seats and usage while outcome pricing stays a small minority**

- Almost every big enterprise now runs at least one agent in production, and agent counts are climbing fast. In a July 2026 survey 95.3% of enterprises ran at least one production agent workflow, about 11 on average (industry research) [src-20260901-8a07a7], the biggest productivity suite counts over 50M agents in its registry, up more than 30% in a quarter (company filings) [src-20261028-51d9ca], and the leading IT service platform reports agentic AI consumption in production up 13x this year (earnings call) [src-20261028-88124d].
- Few run many agents at scale across functions, and most of what runs is simple and supervised. About 1 in 3 enterprises has a cross-functional multi-agent solution and under 50% of proofs of concept reach production (industry research) [src-20260901-8a07a7], 40% of companies with revenue above $1B say they are scaling agents (industry research) [src-20260825-e5c5c1], the chief executive of the leading cloud says most agents built so far are simple and mostly non-autonomous (executive interview) [src-20261008-3ac60a], and the AI chief of a CRM integrator puts the clients seriously in production at about 20% (expert call) [src-20260804-3aa89c].
- Measured value is still thin, which keeps most of these programs short of scale across functions. Only 13% of 2,002 CIOs report significant or transformational value from AI (industry research) [src-20261019-a120c4], and the chief information officer of a $20B convenience retailer is still testing agents for IT service work he believes is 30% to 50% automatable (expert call) [src-20260402-8d84cb].
- Buyers pay through seats and usage, and outcome pricing remains a small minority. Only 19% of services buyers and 13% of seller-side service agreements use outcome-based arrangements (industry research) [src-20260831-c59649], and for separately billed AI, decision makers rank per-seat first at 42.3%, consumption at 36.6% and outcome at 21.1% (industry survey) [src-20260817-c3527b].
- The platforms that sell most agents see no demand for outcome pricing, and buyers push vendors the same way. The finance chief of the leading IT service platform says customers are "not asking at all for outcome pricing" (earnings call) [src-20261028-88124d], a model lab says its enterprise pricing stays usage-based (company announcement) [src-20261023-4ee362], and an insurance buyer negotiated its agent vendor from an annual license proposal to usage pricing with a floor (expert call) [src-20260811-a0aa1e].
2. **Vertical workflows are the layer the model labs cannot easily absorb, because the labs already absorb orchestration, harnesses and generic context, and the horizontal software that holds up either sells neutrality across models and clouds or sells executed work priced per run**

- The model labs now ship the runtime, memory, evaluations, orchestration, connectors and department templates, plus a general coworker agent on top. A lab charges $0.08 per session-hour for managed agents and added multiagent orchestration, graders and memory six weeks later (company announcements) [src-20260408-e5d37b] [src-20260519-55cca6], the other lab charges nothing beyond tokens for its agents interface (company announcement) [src-20260910-014b24], and both now sell coworker agents that take a goal to finished work (company announcements) [src-20260709-eb8b16] [src-20261023-4ee362].
- The labs are moving into regulated templates and into services, so a vertical vendor has to own more than domain prompts. They ship templates for financial services, legal and healthcare work (company announcements) [src-20260505-1c452a] [src-20260512-5c6e2d] [src-20260111-f1affc], a lab formed a majority-owned deployment company with more than $4B of initial investment (company announcement) [src-20260511-c3ff64], the other formed a services firm with private equity backers aimed at mid-sized companies (company announcement) [src-20260504-8f8eff], and a former forward-deployed engineer calls the first of these the lab's forward-deployed arm (expert call) [src-20260908-547a69].
- The labs have not shown they can absorb proprietary data and verifiers, write access and accountability inside systems of record, regulated liability, neutrality across models or owned outcomes in fragmented markets. An agent framework founder says what persists is proprietary data, system access and domain verifiers (podcast) [src-20261017-d3bed0], vendors on lab platforms still park liability with a person in the loop (trade press) [src-20261021-c49bee], and a growth investor says gritty, regulated and fragmented markets repel the labs (investor research) [src-20260416-926244].
- Horizontal tools without one of those positions are already losing ground to the labs, and context on how work gets done holds value only when the vendor keeps it current by doing the work. A former product manager at a sales data company says a lab's assistant is now the biggest competitor to the leading go-to-market orchestration tool for small teams (expert call) [src-20260922-5e723f], a director at a work-context vendor expects customers to stop needing his company once the models learn to map work (expert call) [src-20260616-48f4c6], and business context lifted a data agent's accuracy from about 30% to about 90% before it fell back to 60% two months later (trade press) [src-20261020-7922f1].
- Every big enterprise will not run the same harness, because buyers route across models and want control outside any one provider, so harness value goes to the vertical vendor that owns the domain logic or to a neutral control plane. 81% of big-company CIOs use three or more model families (investor survey) [src-20260130-fb2a33], only 2% of agent platform users chose a platform mainly for its model and 67% expect the control plane to sit at least partly outside a provider-managed service (industry survey) [src-20261005-66e092], a global integrator assigns a model to each agent itself because routing fails in production (expert call) [src-20261017-72ec30], and a fintech built its own harness in six weeks (trade press) [src-20261022-ae18f2].
3. **We can back vertical agent companies with named enterprise customers in regulated or operationally messy markets full of mid-sized buyers at Series A and B today, while horizontal players with the same proof are few**

- Our lean follows the research toward regulated or operationally messy markets with many mid-sized buyers, which the labs and horizontal vendors find costly to serve. A venture firm says regulatory certification, human sign-off and compliance slow down competitors in regulated work (investor research) [src-20260407-5d9d8c].
- Vertical vendors already run production work for named enterprise customers at Series A and B prices. A procurement agent runs 45% to 50% of a global retailer's procurement volume after an $18M Series A (expert call, company announcement) [src-20260209-7ec831] [src-20260917-25441c], a loan servicing vendor has processed over $1 billion in transactions for named lenders (investor announcement) [src-20250728-f2a019], an insurance agent vendor runs servicing for a multi-line insurer inside the insurer's own cloud (company case study) [src-20261029-6049d3], and a health insurer's product leader says a claims agent let his teams bring outsourced work back in-house (expert call) [src-20260811-852c57].
- In non-regulated operations, new vendors report touchless rates and revenue growth that buyers can check in their own systems. A procurement exceptions vendor launched with $56M and says a contract manufacturer reached a 91% touchless rate in four weeks (company claim) [src-20261028-a36adc], a distribution agent vendor reports revenue up more than fivefold in a year after a $60M Series B (company claim) [src-20260714-2498c3], and a drug developer that replaced a procurement consultant with an agent vendor says it would "100% renew" (expert call) [src-20251024-112e5e].
- Horizontal players with the same proof are few, and at least one of the best funded has yet to name customers. An execution platform with a $32M Series A cut a named retailer's reconciliation from 70 days to 15 (company announcement) [src-20261014-1d5d80] and a work-context vendor raised a $30M Series A with three named enterprise customers (trade press) [src-20260318-d7f379], while an agent operating system raised a $65M seed without naming customers (trade press) [src-20260330-8d6266].
- The category leaders are priced beyond our stage, so our entry point is the Series A or B vertical vendor. The leading customer service agent company is valued at $15.8B (trade press) [src-20261020-28bcd0], the freight agent leader at $1.2B (trade press) [src-20260804-cd7dde], and the reference exit so far was an incumbent paying about $3.6B for a rival (company announcement) [src-20260615-74b583].

**Example companies:** Fragment, Magentic, Salient, Notch, Anterior, TJM Labs, Bretton AI, InstaLILY, Duvo

4. **Outcome pricing will stay a minority model that works where a vendor owns an attributable result, so we treat it as one pricing option, stop researching it as a theme and back the vendors that own the result**

- Outcome pricing works where the vendor can count and own the result, such as a resolved contact, a paid claim or a finished demand package. A customer service agent company says outcome pricing works only where the work is highly autonomous and attributable (company interview) [src-20260603-7bd160], and a venture firm advises pricing the highest layer a vendor can measure, attribute and defend (investor research) [src-20260827-fb556f].
- Buyers prefer spend they can predict, so most choose usage or per-conversation pricing even when outcome pricing is on offer. In a buyer survey 43% preferred consumption pricing and 27% outcome pricing (industry research) [src-20260512-1280a6], a fintech buyer wanted "a more transactional pricing without outcome commitment" (expert call) [src-20260708-a5fc76], and a customer service agent vendor says most customers choose per conversation (company claim) [src-20241210-0d932d].
- Vendors usually verify their own outcomes, and outcome contracts have hurt margins where vendors discounted ahead of automation. A software buyer audits its vendor's resolution count because it cannot see how a resolution is defined (expert call) [src-20260318-033caf], and a former director at an AI-native outsourcer says prices fell 10% to 40% on flat costs and gross margin fell hard (expert call) [src-20260724-865e53].
- The labs price agent work by seat, credit and session-hour and now give buyers their own way to grade results, which makes a generic per-task outcome price hard to defend. A lab bundled its always-on agent into existing subscription limits (company announcement) [src-20261021-7532a5], a cloud provider bills agents on pay-as-you-go and spend caps (company announcement) [src-20260826-c6c4b5], and a lab's rubric grader lets any buyer define and check a finished unit of work (company announcement) [src-20260519-55cca6].
- Our research on pricing is done, and we see no reason to push further on outcome pricing as its own theme. Vendors that hold a license or take liability keep more of the price, as a contract law firm whose lawyers take liability for the reviews its AI produces shows (company announcement) [src-20260331-50e583], so the expert calls test only whether outcome contracts renew at the vendors we would back.
# 2. Interesting categories

We split the theme into horizontal software that runs agents across a company, regulated verticals where a license or rulebook governs the work, and non-regulated verticals where the work is operational, and we judge each domain on whether a vendor finishing the work there holds up against the labs and the platforms buyers already own. Each company appears in one category only, and the names we would back first also appear under Thesis 3.

## A. Horizontal: Orchestration, Work Context and Harness

### A1. Orchestration and Harness Platforms

- **Tailwinds: Enterprises run hundreds of systems and a growing number of agents, and someone has to build those agents, coordinate them and record what each one did.** A founder in the category describes enterprises with "hundreds of applications" and thousands of people acting as glue between them (founder interview) [src-20261025-7ef133].
- **Buyers use several models and the labs also leave layers they enter, which keeps room open outside any single lab.** Customers building with multiple models on the biggest productivity suite's AI platform rose 5x (company filings) [src-20261028-51d9ca], and a lab is winding down the agent builder and evaluations products it launched a year earlier (company announcement) [src-20251006-d9ec32].
- **Platforms that sell executed work from the operations budget reach production in companies that lack engineering teams.** An execution platform bills per agent run and its customer says it saves 30 to 40 full-time roles while opening new processes (expert call) [src-20260609-4b024f], and an applied AI company reports work with 10 Global 2000 customers on permitting, energy and patient care (company claim) [src-20250911-dc1698].
- **Headwinds: Enterprises that buy a horizontal platform learn from it and build their next agents themselves, which caps how far each account grows.** An industrial buyer used a platform to skip a 12 to 14 month build and now expects its spending to grow only 5% to 10% (expert call) [src-20260224-8c72f4].
- **Generic harness features lose value with each model release, which erodes what a horizontal harness vendor sells.** A study of frontier models found harness choice did not significantly change coding scores (podcast) [src-20261019-54d838], and an agent framework founder says off-the-shelf harnesses win wherever a task sits inside what the model was trained on (podcast) [src-20260813-09fcee].
- **Custom agent systems built by outside engineers often fail to last, which weighs on platforms sold with heavy services.** An industry analyst expects 70% of enterprises to abandon agent systems built by vendor engineering teams by 2028 because of maintenance costs (industry research) [src-20261012-11ce4a].
- **Why we should focus here, on a longer time horizon: Orchestration and harness platforms are worth backing only when they sell executed work and grow with each agent the customer adds.** The generic runtime and control plane now come free from the labs, clouds and record holders. A platform that maps how a customer's work runs, builds agents against that map and charges per run can win in operations-heavy companies that lack engineers, while a control plane holds up only where buyers pay for its neutrality across models and clouds. We should back only platforms that bill per run and already show named customers in production, and use expert calls to test whether those customers keep the next agent with the vendor.

**Example companies:** Duvo, Sycamore, Ema, Convey, Brain Co

### A2. Work Context

- **Tailwinds: Agents need context that no system of record holds, such as how exceptions get handled and which email settles a dispute.** A work-context vendor builds a living knowledge base from emails, logs, tickets and chat histories (trade press) [src-20260318-d7f379].
- **A global integrator plans to train engineers to capture work context for clients, which would give context vendors a channel at scale.** A work-context vendor's integrator partner plans to train and deploy 1,000 context engineers (trade press) [src-20251229-050f87].
- **The process-mining incumbent argues that agents need a map of how processes connect, which validates the category with buyers.** Its co-chief executive says about 40% of work in big businesses happens on desktops outside systems (podcast) [src-20260504-0c7955].
- **Headwinds: The labs and record holders are building or buying the context layer themselves.** A lab's enterprise agent platform includes a shared semantic layer of company context (company announcement) [src-20260205-ea19f4], and an HR software incumbent agreed to buy a work context graph company (company announcement) [src-20261001-056aad].
- **Context vendors face the suppliers of the models they feed, and their own staff expect the models to learn to map work themselves.** A director at a work-context vendor names the labs as his biggest competition (expert call) [src-20260616-48f4c6].
- **Standalone context vendors show uneven proof of paying customers, which makes their value hard to test.** One work-context vendor counts three named enterprise customers after a $30M Series A (trade press) [src-20260318-d7f379], while another with a well-known founder names no customers on its site (company site) [src-20261023-21a6d6].
- **Why we should not focus here: Context on how work gets done is the input every agent needs, and it holds value when a vendor collects it while doing the work and uses it to finish the next job.** Standalone context vendors sell to the same buyers the labs, record holders and process-mining incumbents now court with bundled context layers, so we should back context inside the vertical vendors in categories B and C and use expert calls to test whether any buyer pays for context apart from finished work.

**Example companies:** Workfabric AI, Edra

## B. Regulated Verticals

### B1. Healthcare Administration

- **Tailwinds: Prior authorization, coding and billing are rule-bound work that providers and health plans already pay for by the claim or by the dollar recovered.** Fees to health plans for prior authorization can include a charge per automatically approved request (trade press) [src-20260213-d1e7fa], and at least one coding review vendor bills hospitals only for findings that are approved and billed (vendor pricing pages) [src-20261029-559e73].
- **Clinical review of care requests has reached production at health plans, starting with fast approvals of cancer care at a regional plan.** A prior authorization vendor that has raised $64M in total says a regional health plan approves cancer care in about 155 seconds (company claim) [src-20260213-d1e7fa].
- **Headwinds: The dominant electronic health record vendor controls the record at most big health systems and limits outside AI, which slows new vendors in those accounts.** A revenue cycle executive says the vendor does not "allow integrations of AI outside of what they're already working on" (expert call) [src-20260608-5e7d7e].
- **Providers still review claims before submission because errors carry liability, so the agent does not yet replace the whole job.** A dermatology group's chief information officer asks, "If any of the wrong claims go in, who takes a liability?" (expert call) [src-20251016-371c9b].
- **The labs are moving into healthcare administration with connectors, sample workflows and services capacity of their own.** A model lab released healthcare connectors and a sample skill for reviewing prior authorization requests (company announcement) [src-20260111-f1affc], and its services firm targets mid-sized companies in healthcare among other industries (company announcement) [src-20260504-8f8eff].
- **Why we should focus here: Healthcare administration is paid by the claim, the authorization or the dollar recovered, so an agent that completes the unit replaces work providers and plans already buy from outsourcers.** Payer rules, write-back into the record and liability for errors are what a lab template lacks, and the record vendor's limits matter least at health plans and independent and specialty practices, so we should back vendors that sell into those buyers and show results in the buyer's cash.

**Example companies:** Anterior, SmarterDx, Procode, TJM Labs, Adaptive Innovations, Alaffia Health

### B2. Insurance Operations

- **Tailwinds: Insurance runs on outsourced servicing, underwriting support and claims work, much of it on old systems that agents can now operate directly.** Agents can now drive old insurance screens reliably enough for production (company claim) [src-20260527-cecfde], and an insurer reports its servicing agent resolves more than 90% of service cases without a person (company claim) [src-20261025-c77b6e].
- **Companies that hold a license or act as the service provider can sell the whole job and keep its economics.** An AI-native commercial brokerage and AI-native claims administrators now sell placement and claims handling, from first notice to payout, as a service (trade press) [src-20260225-3917a2] [src-20250604-fd80b0] [src-20260401-133cee], and an integrator that rebuilt an insurer's outsourced claims work on an agent platform reports straight-through processing above 95% on some flows (expert call) [src-20250627-297f7b].
- **Claims intake is now completed by agents at volume, and a vendor built by former insurance operators reports most intake conversations resolved without a person.** A vendor that ran as a licensed agency in 47 states reports 70% to 73% autonomous resolution across 20 million claims intake conversations (company claim) [src-20261029-6049d3].
- **Headwinds: Insurance buyers are pitched constantly and expect cheaper offers built on open models, which caps prices for vendors that sell tools.** An insurance executive says he is pitched "at least two or three a day" and expects a rival offer "at a 10th of the price by using open-source models" (expert call) [src-20260811-a0aa1e].
- **The insurer keeps the data, so switching vendors is easy and contracts do not compound.** The same executive says "All the data is living within our existing systems" (expert call) [src-20260811-a0aa1e].
- **At least one core insurance system vendor now invests in agent companies on its platform, which gives the record holder a say over which vendors win.** A core systems vendor invested in an underwriting agent company as a strategic investor (company announcement) [src-20260129-3fadee].
- **Why we should focus here: Insurance operations are bought by the claim, the submission and the policy, and most of the work sits with outsourcers on old systems the labs do not touch.** Vendors that hold a license or carry the operating liability keep more of the price than tool vendors and face the least pressure from cheaper open models, so we should back the ones with a named carrier in production across more than one line of work.

**Example companies:** Notch, Pace, Reserv, Harper, Strala

### B3. Lending and Financial Services Operations

- **Tailwinds: Loan servicing and collections run on scripted, regulated conversations that agents now complete across voice, text and email.** A servicing agent vendor says it cut lenders' handle times by 60% and monitors both AI and human agents for unfair or deceptive practices (investor announcement) [src-20250728-f2a019].
- **Compliance alerts arrive as countable cases, and backlogs draw fines when hiring lags volume.** A compliance agent vendor says alerts pile into backlogs that regulators fine (company site) [src-20261023-36cc4e], and an automation vendor now sells agents built for financial crime work (earnings call) [src-20260903-1f1484].
- **At least one outsourcer now packages anti-money laundering checks as agent solutions under committed pricing, which gives agent vendors a resale channel into banks.** An outsourcer with its agent partner packages anti-money laundering checks as agent solutions under committed pricing (trade press) [src-20261020-a21f1d].
- **Headwinds: The labs now ship financial services templates for regulated checks, which sets a free baseline for generic compliance work.** A lab released agent templates covering close, reconciliation and KYC screening for banks and insurers (company announcement) [src-20260505-1c452a].
- **The biggest card issuers and banks can build their own agent platforms under model risk rules, as one card issuer already has, which narrows the vendor opening at those institutions.** A card issuer built its own agent platform with evaluations and controls for regulated use (company interview) [src-20260416-e6896d].
- **Fintech buyers spread work across vendors and route between them, so no vendor holds the account securely.** A fintech routed tickets across three customer service vendors through a router it built itself (expert call) [src-20260518-714b0a], and a consumer bank's banking executive says its contact center agents have not yet reached their 70% to 75% containment target (expert call) [src-20241114-f0ab80].
- **Why we should focus here: Lending servicing and financial compliance are countable, regulated and costly when they go wrong, and the vendor that monitors its own conduct takes on a share of the compliance risk the bank or lender carries.** The biggest banks build their own, so we should back vendors serving consumer lenders, fintechs and regional banks with named customers and volumes.

**Example companies:** Salient, Bretton AI, Gradient Labs

### B4. Legal Services

- **Tailwinds: Legal agents are paid from the budget that pays outside counsel, often per matter.** Personal injury demand packages, the file of evidence and damages a lawyer sends an insurer to settle a claim, are now priced per package (investor research) [src-20241205-4ac3cf], and an AI-native consumer law firm reports revenue above $35M (trade press) [src-20260205-e13567].
- **Firms that hold a license and take liability for the result can price the finished work.** An AI-native contract firm says it has no billable hours and reinvests profits in the workflow to raise margin (podcast) [src-20260618-7d51b5].
- **A German appeals court has held a company liable for what its chatbot told customers, which favors legal providers that stand behind their work.** In that case the court held a cosmetic clinic responsible for specialist qualifications its website chatbot invented (law firm commentary) [src-20260916-6e03e5].
- **Headwinds: The labs now ship legal plugins and connectors to contract systems, which makes drafting tools cheap.** A lab released 12 legal practice-area plugins with connectors to contract and deal systems (company announcement) [src-20260512-5c6e2d].
- **Fixed and outcome pricing for legal work takes time to get right, and at least one AI-native firm lost money while learning it.** The co-founder of an AI-native contract firm says it lost a lot of money on pricing before getting it right (podcast) [src-20261025-1fbd1c].
- **Why we should focus here: As drafting tools get cheap, we should back firms that sell finished legal work under their own license, because they keep the price of the outside counsel they replace and the lab templates do not carry liability.** The plaintiff legal leader already raised at a valuation above $2B (company announcement) [src-20251007-efb7da], so we should back AI-native firms in commercial contracts and consumer law at Series A and B.

**Example companies:** Crosby, Lawhive, EvenUp

### B5. Life Sciences Research

- **Tailwinds: Drug companies are starting to buy research agents, beginning with target discovery, which gives vendors a paying customer for a clear unit of work.** A research agent vendor says one run equals about 6 months of a scientist's work (company claim) [src-20251105-cdfbed], and a listed drug developer is deploying a research agent across its research work (trade press) [src-20260519-f0a637].
- **At least one research agent vendor trains on each drug company's own data, which the labs avoid touching.** A research agent founder says his company trains on each customer's data (founder interview) [src-20260526-6ea6d3].
- **Headwinds: A lab launched a research workbench for scientists, and the market treated it as a threat to research software.** Shares of a drug discovery software maker fell as much as 8.3% on the launch day (trade press) [src-20260630-55a218].
- **Research outcomes take years to prove, so the agent's value is hard to price per result.** A research agent priced at $200 per run ended its founding subscriptions seven months after launch (company announcements) [src-20251105-cdfbed] [src-20260519-9cb3f1].
- **At least one listed drug developer keeps research decisions with its own teams while deploying a research agent, which slows the move from pilot to paid runs.** A listed drug developer's deployment covers research teams that still own the decisions (trade press) [src-20260519-f0a637].
- **Why we should focus here, on a longer time horizon: Life sciences research pays for discovery work in a regulated industry, and a research agent that trains on a drug company's own data does work a lab workbench does not.** Results take years to prove, so we should back companies only once they show repeat paid runs at the same customer, and use expert calls with pharma research leads to test how often a run changes a program decision.

**Example companies:** Edison Scientific

## C. Non-Regulated Verticals

### C1. Procurement, Logistics and Distribution

- **Tailwinds: Procurement savings are measured against total spend, which ties an agent's value to the money it saves on purchases as well as the labor it replaces.** For a manufacturer spending $10B a year, a 50% more efficient team saves $50M, while a 1% to 2% cut in purchase prices is worth $100M to $200M (founder interview) [src-20260923-47e348].
- **At a contract manufacturer, exception work in purchasing and payables defeated a long internal automation effort, which opens the door to vendors that finish it.** A contract manufacturer's internal machine learning effort ran for 18 months and capped out around 30% touchless (company claim) [src-20261028-a36adc].
- **Freight operators and distributors are buying agents for quoting, dispatch, collections and service, and the leaders show scale.** A freight agent vendor reports more than 150 enterprise customers and 5x growth since its Series B (trade press) [src-20260804-cd7dde], and a distribution agent vendor raised a $60M Series B with a home improvement retailer among its investors (trade press) [src-20260714-2498c3].
- **Headwinds: Procurement agents that run beside the buyer's record are easy to replace, which limits how long a vendor holds an account.** A global retailer that pays on a consumption license puts a replacement of its procurement agent vendor at seven to eight months (expert call) [src-20260209-7ec831].
- **A lab is testing its own specialist agents for procurement, invoice processing and contracting.** Its developer conference previewed specialist agents with their own identity for those roles (company announcement) [src-20260929-2fdd0f].
- **Buyers keep a person on the final step, so the full price of the job moves to the agent slowly.** The chief executive of a procurement outsourcer says "I don't have any client that lets it go on its own" (expert call) [src-20260617-937cc1].
- **Why we should focus here: Procurement, logistics and distribution work runs across suppliers, carriers, phone calls and email outside any single record, which makes it hard for an ERP vendor or a lab template to absorb.** The agents sit on the buyer's ERP, so results are counted in a record the buyer trusts, and value grows with the spend the agent handles. We should back vendors that clear exceptions end to end and show touchless rates at named manufacturers, freight operators and distributors, at Series A or B prices since the freight leader already trades as a Series C company.

**Example companies:** Fragment, Magentic, Didero, HappyRobot, InstaLILY, BackOps

### C2. Finance and Accounting Operations

- **Tailwinds: Finance teams repeat the same work every month, and each invoice, collection or reconciliation has a clear count and cost.** Vendors in payables and collections report volumes above 100M invoices a year and overdue balances cut by 40% (company claims) [src-20250721-54e512] [src-20251120-b7dfc3].
- **Accounting and payables agents now sell the finished job and take responsibility for it.** An accounting agent vendor says it never had a seat or token price for its core product, and a payables vendor says its agents decide whether to pay each invoice and "take accountability for the outcome" (company interviews) [src-20260730-3a49fd] [src-20260729-f4bed6].
- **At least one accounting agent vendor built for a single trade has won customers at scale, which shows room for agents built around one industry's books.** That vendor raised a $30M Series B and counts more than 750 construction companies as customers (company announcement) [src-20260917-e6c847].
- **Headwinds: ERP vendors are building agents into the systems many finance teams already run, which limits how far a new vendor can reach inside those accounts.** A leading ERP vendor sells its agents through paid AI units, with a rules layer validating every action the model proposes (trade press) [src-20261003-10d57c].
- **A lab's financial services templates cover the generic monthly close directly, which narrows the opening for generic vendors.** Its templates cover close, reconciliation and audit work for finance teams alongside KYC screening (company announcement) [src-20260505-1c452a].
- **Agents cost more to run than the scripted bots many finance teams already use, so vendors must show savings beyond the old automation.** An integrator's automation lead says a task that costs $200 or $300 a month on bots costs $1,000 or $1,200 a month with AI (expert call) [src-20260825-747be0].
- **Why we should focus here: Finance and accounting work recurs with the monthly close and is checked in the buyer's own books, and the vendors that take accountability for each invoice or filing charge for the finished job.** ERP vendors and lab templates cover the generic close, so we should back vendors that serve accounting firms, global payroll or a specific industry's books, where rules and liability sit outside the ERP. The best-known accounting agent company already raised a $100M Series B at a $1.15B valuation (company interview) [src-20260730-3a49fd], so our entry point is the next vendor serving one industry's books or global payroll.

**Example companies:** Basis, Freehand, Niural

### C3. Customer Service and Sales

- **Tailwinds: Customer service is the first job agents complete end to end at scale, because a resolved ticket is easy to define and check and the labor it replaces is easy to price.** Software companies spend $20 to $30 per ticket resolved by people, which gives buyers a clear benchmark for an agent that resolves the ticket itself (founder interview) [src-20250821-666ad1].
- **Voice is opening a second wave of spending in contact centers that still run mostly on people.** The US still employs 2,666,000 customer service representatives whose work voice agents can now take on (government data) [src-20260827-b22de5].
- **Sales teams already pay agencies per meeting and per lead, which gives agents a known price to replace.** Agent vendors now bill sales work the same way, at published prices such as $9.99 per qualified lead (vendor pricing pages) [src-20260924-1b6619].
- **Headwinds: The labs, the help desk platforms and the contact-center incumbents all sell a customer service agent now, which pushes prices down for everyone.** A model lab launched its own customer service agent with written procedures, guardrails and automated scoring (company announcement) [src-20260722-a3993b].
- **Sales agents churn heavily, because agents that send cold email burn through prospects and fail to show value inside short pilots.** An advisor to sales agent companies puts churn at 80% to 90%, the worst of any category he advises (expert call) [src-20250507-e13bdd].
- **CRM incumbents bundle their own sales agents to replace point tools, which squeezes standalone vendors in their accounts.** A CRM bundle priced at $550 claims to replace roughly $1,300 of point-solution spend per US sales rep (company announcement) [src-20260909-c1900d].
- **Why we should not focus here: Customer service proves that agents can finish a whole job at scale, but every lab and help desk platform now sells that job.** Prices are falling, and the leaders already raised at prices that leave a new entrant little room. Sales agents are paid on meetings and leads that are easy to game, and the CRM owners bundle their own. We should use customer service resolution rates and prices as the benchmark for other functions and make no new bets in the category.

**Example companies:** Sierra, Decagon

# 3. Expert call framework

We will present the theme to experts as a set of positions to challenge, starting from what we have read and asking each expert to tell us where it breaks in their own deployments. Each call opens with our four theses in one sentence each, then spends most of its time on the questions for that expert's seat, and ends by asking for the one thing that would change the expert's view.

## Hypotheses we are testing

- On the tipping point, we expect that almost every big enterprise runs some agents in production, few run many at scale across functions, and buyers pay through seats and usage far more often than per outcome.
- On the right to win, we expect that vertical workflows hold up against the model labs, generic orchestration and harnesses get absorbed, the horizontal positions that last are neutrality across models and executed work priced per run, and every enterprise ends up with its own harness configuration on a few shared runtimes.
- On who we can back, we expect that vertical vendors with named enterprise customers in regulated or operationally messy markets full of mid-sized buyers are the companies we can back at Series A and B.
- On outcome pricing, we expect that outcome pricing stays a minority model that works only where the vendor owns an attributable result, and outcome contracts renew at lower rates than usage contracts.
## Call type 1. Heads of AI and automation at big enterprises running agents in production

**Call targets:** heads of AI, automation or shared services at Fortune 500 companies with agents in production in service, finance, procurement or claims

- How many agents run in production today, in which functions, and what share of them act without a person approving the last step?
- Which budget pays for those agents, software, the operations team's services line or outsourcing, and has any outsourcing contract been cut because of them?
- Who built the harness each agent runs on, your own engineers, a lab or cloud platform, an integrator or a vertical vendor, and who will build the next one?
- Which agent work would you never hand to a lab's own agent product, and what does a vertical vendor give you there that the lab does not?
- How are the agents priced, by seat, credit, run or outcome, and which pricing model would you choose again at renewal and why?
## Call type 2. Agentic AI practice leads at systems integrators

**Call targets:** agentic AI practice leads and lab alliance leads at Deloitte, Accenture and peer integrators

- Across your client deployments, which harness and orchestration stack do you standardize on, and how much of each client's harness is reused from one client to the next?
- When a lab funds your engineers to deploy its agents, which client work goes to the lab's product and which goes to a vertical vendor you resell?
- Which agent deployments at your clients reached production and stayed there for a year, and what separated them from the pilots that were abandoned?
- How often do clients ask for outcome-linked pricing, and how many of those outcome contracts have renewed on the same terms?
- Which vertical vendors do your clients ask for by name in regulated work such as claims, prior authorization or lending, and why those vendors?
## Call type 3. Customers and former employees of horizontal agent platforms

**Call targets:** customers and former employees of Sycamore, Duvo and Workfabric AI

- What work did the platform take over in its first year, and did the second and third agents come from the vendor or from your own team?
- What did the vendor learn about how your work gets done that your own systems and the labs' tools did not already capture?
- How is the platform priced, per run, per process or per outcome, and how did the price change at renewal or on expansion?
- Which lab or platform launch in the past nine months came closest to replacing the vendor, and why did you keep it?
- If the vendor disappeared tomorrow, how many weeks would it take to rebuild its agents on a lab or cloud runtime with your own team?
## Call type 4. Customers and former employees of the vertical vendors we would back first

**Call targets:** customers and former employees of Fragment, Magentic, Salient, Notch, Anterior, TJM Labs, Bretton AI and InstaLILY, and pharma research leads who have bought research agent runs

- What unit of work does the vendor finish for you, and what share of those units closes without a person on the last step?
- Which second and third use cases did you give the vendor after the first, and on what renewal terms?
- Which outsourcing contract or headcount did the vendor replace, and how much of that budget now goes to the vendor?
- What would a lab's own templates or services firm need before doing this work as well, and how long would that take?
- For research runs, how often has a run changed a program decision, and would you buy the next run at the same price?
## Open questions the calls must resolve

- For Thesis 1, the calls must give us the share of agents running without a person on the last step, and whether any big enterprise has cut an outsourcing contract because of agents.
- For Thesis 2, the calls must give us evidence on who builds the next harness at each enterprise and whether vendor-held context survives a lab platform reaching the same systems.
- For Thesis 3, the calls must give us second and third use cases at the same customer, with renewal terms, for the vertical and horizontal companies we would back.
- For Thesis 4, the calls must give us renewal rates on outcome contracts against usage contracts, and who verifies the outcome when the buyer disputes the count.
