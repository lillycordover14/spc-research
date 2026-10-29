<!-- OBA theme memo v2, 2026-10-29. Source of truth for exports/OBA-theme-memo-v2-2026-10-29.docx/.pdf. Inline cites show the short source name; bracketed ids map to sources/. Built with /workspace/oba-memo/build.py on the Sewon template. -->

# Outcome-Based Agents and Agentic Orchestration

## Investment theses and category views on AI agents that do enterprise work and get paid for results

# 1. Investment theses: tailwinds, key takeaways and macro

This theme covers AI agents that complete a piece of enterprise work from start to finish, such as resolving a support ticket, working a denied medical claim or placing a purchase order, and that are paid per result or per unit of work instead of per user. It also covers the orchestration software that lets a company run many agents under common rules. Five groups compete for this work, namely the model labs and cloud providers, the systems of record such as Salesforce and SAP, enterprises building their own agents, systems integrators and outsourcers, and vertical applications built for one job in one industry.

1. **Agents can now do whole jobs inside old enterprise software, and because seat pricing breaks once software replaces people, spending is moving from software budgets to the labor and outsourcing budgets that agents replace**

- Models crossed a usable threshold in the past year, and Pace, an insurance operations startup, says its success rate on tests that drive legacy insurance screens rose from 30% to over 95% in a single model release (Pace, claim) [src-20260527-cecfde]. Gartner expects agentic AI funding to grow 31.8% in 2027 against 3.7% for IT budgets overall (Gartner) [src-20260831-2bda07].
- The budget agents compete for is labor, which buyers measure in wages and outsourcing invoices instead of software licenses. The US employs 2,666,000 customer service representatives at a median wage of $44,770 (BLS) [src-20260827-b22de5], about $119B a year by our estimate, and HFS Research expects $422B of business process outsourcing (BPO) spending to shift to software that does the work by 2035 (HFS Research) [src-20260831-73c927].
- Seat pricing stops working once software does the work, because a vendor whose agent replaces five people loses four of the seats it used to bill. Zendesk's CEO says "seats are going to go away over time" (Zendesk) [src-20260805-5a9fa7], and the share of AI software vendors using outcome-based pricing rose from 18% to 23% in six months (ICONIQ) [src-20260715-e16b49].
- The largest customer service platforms already charge per result, which tells buyers the model will last. Intercom charges $0.99 per resolution (Intercom) [src-20260924-93c5ed] and HubSpot $0.50 per resolved conversation (HubSpot) [src-20260413-63104e], and Zendesk says it passed $200M of AI annual recurring revenue (ARR) (Zendesk) [src-20260805-5a9fa7].
- The labs and cloud providers are paying to get agents installed, which shortens the path to production for every vendor. Google set up a $750M partner fund (Google Cloud) [src-20260422-72407e], and postings for forward-deployed engineers (FDEs), engineers who build each customer's deployment on site, passed 7,300 in the first nine months of 2026 against under 200 in 2023 (Lightcast via CIO Dive) [src-20261022-d5ad54].
2. **New companies have an edge where they sell a finished job in one industry and carry the result, because the labs sell general tools and the incumbents mostly add AI to the seats they already sell**

- A vertical company knows the rules, exceptions and systems of one kind of work, which a general model does not learn from public data. Box's CEO Aaron Levie argues that closing the gap between the roughly 70% accuracy of a model off the shelf and the 97% a business needs is what makes work automatable (Sequoia Capital podcast) [src-20260915-68c6ef].
- Getting an agent into production is mostly integration and testing, so a company that brings its own engineers and owns the result gets through where software alone stalls. Cresta's head of forward-deployed engineering says one month of building can mean "two or three or even four months on the test eval" (expert call) [src-20260618-f36dc6].
- Companies that take legal or regulatory responsibility for the work keep more of the price, because buyers otherwise keep a person on the last step. Crosby is a registered law firm whose lawyers take liability for the contracts its AI reviews (Lux Capital) [src-20260331-50e583], while a dermatology group running a billing agent still has staff submit every claim (expert call) [src-20251016-371c9b].
- The incumbents often bolt agents onto old products and the labs avoid customer-specific work, which leaves room for specialists. Discover found the AI products of the contact-center incumbents "more of a bolt-on" (expert call) [src-20241114-f0ab80], and Edison Scientific's CEO says the labs avoid training on each customer's data because "they don't want to have a different model for every customer" (Edison Scientific, claim) [src-20260526-6ea6d3].
3. **Buyers compare an agent with the outsourcer or headcount it replaces and pay readily when the saving is measurable, but they prefer predictable pricing and keep vendors easy to replace**

- The price an agent replaces is the outsourcer's invoice, and savings at the first buyers are wide enough to close deals quickly. Notion says its offshore support model cost "4X to 7X" what Decagon costs (expert call) [src-20260515-de88a1].
- Agent companies increasingly sell into the operating department's services budget, which is larger and easier to reach than the IT software budget. A Duvo co-founder sells from the "service budget line, because it is easier to procure" (Duvo, claim) [src-20260701-3b0c17].
- Buyers want to know what they will spend, so pure outcome pricing can slow a sale even when the buyer likes the idea. A European fintech buyer wanted "a more transactional pricing without outcome commitment" (expert call) [src-20260708-a5fc76], and 27 of 50 buyers in an a16z survey preferred credits tied to work over tokens (a16z) [src-20260827-fb556f].
- Buyers keep their data, procedures and tools in their own systems so any vendor can be replaced, which caps the price a vendor can hold once rivals catch up. Chime routed tickets across three customer service vendors through its own router (expert call) [src-20260518-714b0a].
4. **Agent companies earn gross margins between those of outsourcers and software today, and margins rise only as the share of work the agent completes rises and the cost of each deployment falls**

- AI products earn gross margins of 50% to 60% against 80% to 90% for traditional software (Bessemer) [src-20260210-496d37], and ICONIQ's survey projects AI product margins rising from 45% in 2025 to 59% in 2027 (ICONIQ via HackerNoon) [src-20260924-1b6619]. Pace's CEO puts outsourcers at "10, 15 percent gross margin" and targets 80% for his own company (Pace, claim) [src-20260203-a5df90].
- Under per-resolution pricing the vendor pays for model usage on every conversation but bills only the resolved ones, so the resolution rate drives margin directly. Intercom's CFO says a resolution rate that rose from about 25% to close to 70% improved margin (Intercom, claim) [src-20260522-b1dbe3], and Decagon runs about 90% of its workloads on cheaper fine-tuned open-source models (PYMNTS) [src-20261013-d7909a].
- Deployment cost falls with each agent a customer adds, which is where margins improve over the life of an account. Safelite's first Sierra agent took six months and its second one month, and setup ran to "at least 35%-40% of your first year spend" (expert call) [src-20260710-37d40b].
- The vendor keeps a thin slice of the savings it creates, so it needs volume to build a business. Safelite measured a 35% to 40% cost cut and gave Sierra about 10% of it (expert call) [src-20260710-37d40b], so on $10M of handled cost the vendor earns $350,000 to $400,000 a year by our estimate.
5. **The main risk is that the labs and systems of record absorb the agent and set its price, so new companies win where outsourced work is countable and they hold knowledge or liability the platforms lack**

- The labs now ship finished agents and give away the tools around them, which moves them into the job itself. OpenAI's Presence is a complete customer service agent with procedures, guardrails and graders (OpenAI) [src-20260722-a3993b], and Anthropic has released plugins for 12 legal practice areas (Anthropic) [src-20260512-5c6e2d].
- The systems of record are selling agents into their installed base at scale with the customer data already in hand. Salesforce's Agentforce passed $1.5B of ARR on a definition widened to include Slackbot (Salesforce) [src-20260826-0b53e8], and ServiceNow's AI products passed $1B of annual contract value (ServiceNow) [src-20260722-d4586c].
- Exits so far go to incumbents at prices well below the private rounds of the leaders, which limits the return on late entries. Salesforce bought Intercom's Fin for about $3.6B (Salesforce) [src-20260615-74b583], while Sierra and Decagon raised at roughly 75 to 100 times and about 45 times ARR respectively by our estimate (company reports) [src-20260504-c9d184] [src-20261025-07358d] [src-20260127-5d9191].
- New companies win in back-office work that enterprises already pay outsiders to do, such as insurance servicing, medical billing, procurement, accounting and legal review, where the unit of work is countable and the platforms' agents are thin. Startups are concentrated there as well, with 87 of the 121 companies we track building vertical applications (our count) [insights/landscape-cuts.md].
# 2. Interesting categories

The categories follow the five groups in our primer, with vertical applications split by buyer function, and for each one we set out tailwinds and headwinds and whether we should focus there.

## A. Labs and Hyperscalers

### Agent Infrastructure

- **Tailwinds: Every company that runs agents needs testing, monitoring, permissions and compute around the model, and that spending grows with each agent in production.** In a LangChain survey of agent builders, 57% said they already had agents in production (LangChain) [src-20251202-cd7dc4].
- **Model usage is now a major cost line for agent companies, which creates demand for tools that send each step to the cheapest capable model.** LangChain says routing cut median cost per conversation thread by 64% at one deployment (The New Stack) [src-20261022-ae18f2].
- **Security failures are making agent identity and permissions a required purchase for security teams.** An AI agent deleted a company's production database in 9 seconds using a token with broader rights than its task needed (Euronews) [src-20260428-8baab9].
- **Headwinds: The labs give the core agent harness away or price it near cost, which caps what an independent vendor can charge.** OpenAI's Agents API adds no fee on top of model usage (OpenAI) [src-20260910-014b24], and Anthropic charges $0.08 per session-hour for its managed harness (Anthropic) [src-20260408-e5d37b].
- **The labs are also building testing and improvement tools into their own agents, which removes the reason to buy them separately.** OpenAI's Presence ships with simulations, graders and an improvement loop that independent testing vendors sell separately (OpenAI) [src-20260722-a3993b].
- **Buyers rarely pay for neutrality across models, which weakens the main argument for an independent layer.** An Accenture managing director calls models "such commodities" and says routing between them is "hardly ever" used by his clients (expert call) [src-20261017-72ec30].
- **Why we should not focus here: Agent infrastructure is sold to engineering teams on usage, and the labs that sell the model can bundle the same tools for free.** Companies here compete with their own suppliers, earn usage revenue that falls with model prices and tend to sell to a lab or cloud provider at a modest price, so the returns go to the model owners and to the applications that sell the finished job.

**Example companies:** OpenAI, Anthropic, Google, Microsoft, Amazon Web Services, LangChain, CopilotKit, Coval, Dash0, Daytona, Flexprice, InsightFinder, Natural, Raindrop, Rein, Runlayer, Tsuga, ElevenLabs, Saviynt, Modal

## B. Systems of Record

### Agents on the System of Record

- **Tailwinds: Outcome pricing moves value to the company that holds the record, because a result can only be counted and billed where the ticket, claim or order is opened and closed.** To bill per resolution a vendor must know whether the customer came back or a person stepped in, and that history sits in the help desk, the customer database or the enterprise resource planning (ERP) system. Truist research makes the same point, that outcome pricing "could be especially advantageous to SoR companies" (Truist research) [src-20260428-14f0c8].
- **The record holders also decide how a resolution is verified, which today means the vendor checks its own work.** Zendesk bills a resolution only after its own language model reviews the conversation and confirms the request was resolved, and escalated or assisted cases are not billed (Zendesk) [src-20250806-3921b6]. Intercom bills when the customer confirms the answer or leaves without asking for more help (Intercom) [src-20260924-93c5ed], Zendesk's default test is 72 hours of customer inactivity (HackerNoon) [src-20260924-1b6619], and one Sierra customer audits the count himself because he cannot see how it is defined (expert call) [src-20260318-033caf].
- **The incumbents are selling agents into their installed base faster than any startup can reach the same buyers.** Salesforce says "50% of the bookings came from customers refilling the tank" of agent credits (Salesforce earnings call) [src-20260826-580137], and a KPMG partner says ServiceNow's AI faces "few viable alternatives" in core IT service management (expert call) [src-20260911-0742fb].
- **The record holders are active buyers of agent companies, which gives startups built on their platforms a clear exit.** Workday is buying C1.ai (Workday) [src-20261013-7962db], SAP is buying TechWolf (SAP) [src-20261001-056aad] and Guidewire invested in Sixfold (Sixfold) [src-20260129-3fadee].
- **Headwinds: The record holders control access to their data and can shut out or copy a startup that depends on them.** Clients of the AI-native outsourcer Crescendo were hesitant to give it the API key it needed to reach reporting in their systems (expert call) [src-20260724-865e53].
- **Incumbent outcome pricing is uneven outside customer service, so the pricing shift is slower than the headlines suggest.** Salesforce sells most agents through credits at $0.10 per action (Tech Insider) [src-20261013-7d8358], SAP's CFO says outcome-linked revenue will not move its 2027 numbers (SAP earnings call) [src-20261021-551046].
- **Seat-based incumbents lose seats as agents do the work, which pushes them to raise prices and invites buyers to question the platform.** The KPMG partner reports shrinking seat counts and growth led by price increases (expert call) [src-20260911-0742fb], and Wawa's CIO asks "Do I even need to have a ServiceNow platform?" (expert call) [src-20260402-8d84cb].
- **Why we should focus here: Systems of record hold the data, permissions and audit trail that outcome pricing needs, so much of agent spending will run through them, and the startups that run on top of them sell into a system the buyer already trusts.** These startups are paid per transaction on work the record already tracks, such as purchase orders, receivables and referrals, which makes results easy to check and renew. The record holders are also the most active acquirers in the theme, which lowers the risk that a platform closes its data to partners it may later buy.

**Example companies:** Salesforce, ServiceNow, SAP, Oracle, Workday, Zendesk, Intercom, HubSpot, Guidewire, Moveworks, Didero, Magentic, Walter, GenHealth.ai, Sixfold, Stuut, Tennr, Assort Health, Rox, Zip, Omnea, Thoughtful AI

## C. Enterprises Building Their Own

### Horizontal Orchestration and Work Context

- **Tailwinds: Large companies run hundreds of systems and many agents, and someone has to coordinate them, set permissions and record what each agent did.** Ema's founder says "every enterprise today has hundreds of applications" and thousands of people acting as glue between them (Ema, claim) [src-20261025-7ef133].
- **Agents perform far better when they know how work is actually done, which makes a record of real work patterns valuable to every agent a company runs.** One analytics agent rose from about 30% to about 90% accuracy once it had business context (VentureBeat) [src-20261020-7922f1].
- **The leading horizontal companies report fast growth from enterprise customers, although the figures are their own.** Ema reports bookings over $150M (Ema, claim) [src-20260930-9ee545], Skan AI reports revenue growth over 300% and net dollar retention of about 150% (Skan AI, claim) [src-20260812-4cb1fc].
- **Headwinds: Enterprises that buy a horizontal platform often learn from it and build their next agents themselves, which caps how far each account grows.** Hitachi chose Ema over a 12 to 14 month internal build, then said "Today, for other use cases, we don't depend on Ema" and expects spending to grow only 5% to 10% (expert call) [src-20260224-8c72f4].
- **The clouds and systems of record give the coordination layer away to win the platform.** ServiceNow made its AI Control Tower free for a year (ServiceNow) [src-20260507-e6c2cd], and Microsoft sells Agent 365 to govern every agent (Microsoft) [src-20260501-fc687c].
- **The labs and automation incumbents are moving into work context, so the companies that map work face the suppliers of the models they feed.** A Skan AI director says "Once Claude figures out how to do this themselves, they don't need us" (expert call) [src-20260616-48f4c6].
- **Why we should not focus here: Horizontal orchestration sells a platform that enterprises increasingly build themselves or receive free from a platform they already own, so pricing power falls as the customer's own team learns.** Sales cycles run about nine months by Ema's account (Ema, claim) [src-20261025-7ef133], and expansion stalls once the customer builds its own agents. Work context is the stronger idea, because data on how work really gets done improves every agent, but SAP, UiPath and the labs all claim that layer, and we should revisit the category on a longer horizon if independent customers keep expanding.

**Example companies:** Ema, Kestra, Duvo, Sycamore, Airia, Maisa AI, Mimica, Skan AI, Workfabric AI, Relevance AI, n8n, Unframe, Glean, Workato, UiPath, Celonis

## D. Systems Integrators and BPOs

### AI Services and AI-Native Outsourcers

- **Tailwinds: Systems integrators are the channel through which most large enterprises deploy agents, and the labs are paying them to do it.** Anthropic committed $100M to a partner network for the integrators that deploy its models (Anthropic) [src-20260312-73c25c].
- **Outsourcing is the budget agents replace, and the incumbent outsourcers are already losing ground.** Concentrix took a $1.05B goodwill impairment on its depressed share price (Concentrix) [src-20260929-4fcfe9], and TP's core services fell 1.0% like for like in the second quarter of 2026 (TP) [src-20260730-4cc420].
- **Automation lets services firms trade revenue for margin, which gives them a reason to adopt agents quickly.** A Cognizant practice head says the agent platform costs under $10,000 per worker a year against revenue above $20,000 per outsourced worker, and "Our revenues go down, but our margins go up" (expert call) [src-20250627-297f7b].
- **Headwinds: AI-run outsourcing is already in a price war, because the same models are available to every provider.** A TTEC vice president says outsourcing rates for health insurers fell "between 20% and 40%" in two years and that "Right now, there is no protection in the industry" (expert call) [src-20260930-124dc3].
- **The customer keeps the data, so switching providers is easy and contracts do not compound.** An Accelerant executive says "All the data is living within our existing systems" and expects a rival offer "at a 10th of the price by using open-source models" (expert call) [src-20260811-a0aa1e].
- **Discounting before the automation works erases the margin a services firm starts with.** Crescendo cut prices 10% to 40% while costs stayed flat, and a former director says "Gross margin did tank heavily" (expert call) [src-20260724-865e53].
- **Why we should not focus here: Services firms earn on people and hours, so automation shrinks their revenue even as it lifts their margin, and AI-native outsourcers that undercut the incumbents fight a price war with no switching costs because the data stays with the customer.** Integrators matter to the theme as the channel that installs agents in large enterprises, and the recurring value goes to the software they deploy, so we should back the products that integrators resell and treat the services firms as partners and acquirers.

**Example companies:** Accenture, Deloitte, Cognizant, Infosys, TCS, KPMG, PwC, Concentrix, Teleperformance, TTEC, Conduent, Crescendo, DeepOpinion, Otera, RapidCanvas, AuxoAI, Distyl AI

## E. Vertical Apps

### Customer Service and Contact Center

- **Tailwinds: Customer service is the first job paid per result at scale, because a resolved ticket is easy to count and the labor it replaces is easy to price.** Intercom's CEO says software companies spend $20 to $30 per ticket resolved by people, against the $0.99 Fin charges (Lenny's Podcast) [src-20250821-666ad1].
- **Savings at early buyers are wide enough to make the business case easy to defend.** Safelite pays Sierra under $2 per transaction against $7.50 to $9 for a person (expert call) [src-20260710-37d40b].
- **Voice is opening a second wave of spending in contact centers that still run mostly on people.** NiCE, a contact-center software incumbent, reports AI ARR of $362M growing 52% (NiCE) [src-20260805-3deb2c].
- **Headwinds: The labs, help desk platforms and contact-center incumbents all sell a customer service agent now, which pushes prices down for everyone.** OpenAI launched its own customer service agent, Presence (OpenAI) [src-20260722-a3993b], and Salesforce now owns Fin (Salesforce) [src-20260615-74b583].
- **Buyers route work across several vendors and plan to consolidate, so no vendor holds its account securely.** Chime split its support tickets across three vendors through a router it built itself (expert call) [src-20260518-714b0a].
- **Results vary widely by customer, and buyers will soon compare agents with each other instead of with people.** Fin resolves 30% to 40% of conversations at Smartly.io against a 76% average (expert call) [src-20260326-b3dd2d] (Salesforce) [src-20260910-2cf2eb], and Sierra's chairman calls cost savings "a temporary drug" (Sequoia Capital) [src-20250514-093b59].
- **Why we should not focus here: Customer service proves that buyers will pay per result, but labs, platforms and incumbents all sell the same countable unit at prices that are already low (Intercom) [src-20260924-93c5ed].** Buyers keep their data so they can switch, and the leaders raised at roughly 45 to 100 times ARR (our estimate) [src-20260504-c9d184] [src-20261025-07358d] [src-20260127-5d9191], which leaves a new entrant little room to win share or earn a strong return, so the category serves best as a guide to how outcome pricing behaves.

**Example companies:** Sierra, Decagon, Cresta, Crescendo, Parloa, Lorikeet, Gradient Labs, PolyAI, ElevenLabs, Omilia, respond.io

### Sales and Revenue

- **Tailwinds: Sales teams already pay agencies and outsourced sales development teams per meeting and per lead, which gives agents a known price to replace.** Fin already charges $9.99 for each qualified lead it hands to a sales team (HackerNoon) [src-20260924-1b6619].
- **Early buyers report clear returns when the agent works deals already in the customer database.** Justworks says an Actively agent produced about $1M of revenue on spend of around $160,000 (expert call) [src-20251126-6d86c8].
- **Investors are funding agents that work each account continuously instead of tools that help a rep.** Actively AI raised at a $250M valuation with Ramp as a named customer (Forbes) [src-20260428-2d177a].
- **Headwinds: Churn is very high, because autonomous sales agents that send cold email burn through prospects and fail to show value inside short pilots.** A former 11x advisor puts churn at 80% to 90%, the worst of any category he advises (expert call) [src-20250507-e13bdd].
- **The general models already do much of the work, so the product is easy to copy and hard to price.** A former Apollo product manager says Claude is now Clay's biggest competitor for small teams (expert call) [src-20260922-5e723f].
- **Salesforce bundles its own sales agents to replace point tools, squeezing standalone vendors in its accounts.** Salesforce says its $550 Agentforce 1 Edition replaces roughly $1,300 of point-solution spend per US sales rep (Salesforce) [src-20260909-c1900d].
- **Why we should not focus here: Sales agents are paid on meetings and leads, which are countable but easy to game, so buyers churn when quality slips.** The tools are easy to copy and the customer database owners bundle their own agents, so the economics favor the platforms that own the sales record.

**Example companies:** Actively AI, Attention, Vida, Rox, Unify, Clay, 11x, Artisan, Nooks

### Finance and Accounting

- **Tailwinds: Finance teams repeat the same work every month, and each invoice, collection or reconciliation has a clear count and cost.** Xelix says it processes over 115M invoices a year (Xelix, claim) [src-20250721-54e512], and Stuut says its collections agents cut overdue balances 40% (Stuut, claim) [src-20251120-b7dfc3].
- **The general ledger is being rebuilt for the first time in decades, which lets new companies become the record instead of riding on someone else's.** Bessemer argues that AI-native ERPs such as Rillet put the old systems of record under pressure (Bessemer) [src-20250813-44ef93], and Rillet's revenue doubled in 12 weeks (Crunchbase News) [src-20250806-b579d5].
- **Accounting firms are short of staff and are paying for agents that do tax, audit and bookkeeping work end to end.** Basis raised at a $1.15B valuation to sell such agents to accounting firms (Basis) [src-20260224-b6a4eb].
- **Headwinds: Oracle is building agents into the ERP that many large finance teams already run, which limits how far a startup can reach inside those accounts.** Oracle sells these agents inside its Fusion ERP through paid AI units, with a rules layer validating every action the model proposes (Forkast News) [src-20261003-10d57c].
- **The largest ERP vendor expects little change in how it prices agents in the near term.** SAP's CFO says revenue linked to outcomes will not move its 2027 numbers (SAP earnings call) [src-20261021-551046].
- **Most finance agent companies do not disclose their pricing, so the move to pricing per unit of work is less proven than in customer service.** Xelix, Tabs and Stuut all announced funding without saying how they charge customers (Xelix, Tabs and Stuut) [src-20250721-54e512] [src-20250916-6b0cd0] [src-20251120-b7dfc3].
- **Why we should focus here: Finance work repeats every month, is easy to count and costs money when wrong, so buyers pay for agents that cut the cost of each invoice or collection.** Companies on the ERP sell quickly because the buyer keeps its record, and the new ledgers can become the record over a longer horizon. Revenue recurs with the monthly close, and margins should rise toward software levels as agents finish more work without review.

**Example companies:** Adaptive, Basis, Definite, Elimentary, Xelix, Zolvo, Zomma, Rillet, Campfire, Tabs, Stuut, Hebbia, Pigment

### Procurement and Supply Chain

- **Tailwinds: Procurement savings are measured against total spend, which ties an agent's value to the money it saves instead of the labor it replaces.** In Magentic's example, a manufacturer spending $10B a year saves $50M by making its team 50% more efficient, while a 1% to 2% cut in procurement cost is worth far more (Riding Unicorns) [src-20260923-47e348].
- **Procurement agents run on top of the ERP instead of replacing it, which speeds approval.** PayPal says "We weren't trying to replace our system of record" (expert call) [src-20260716-88dbe4], and IKEA's agent already handles 45% to 50% of its procurement volume (expert call) [src-20260209-7ec831].
- **Small and mid-sized buyers see value within days, which shortens the sales cycle.** Novilla had Didero running in about three days and says it "would 100% renew" (expert call) [src-20251024-112e5e].
- **Headwinds: Buyers keep a person on the final step, so the full price of the job moves to the agent slowly.** The chief executive of a procurement outsourcer says "I don't have any client that lets it go on its own" (expert call) [src-20260617-937cc1].
- **Some buyers pay for consumption with no share of savings, which caps revenue below the value created.** IKEA pays a consumption-based enterprise license and gives its procurement agent vendor no share of the savings (expert call) [src-20260209-7ec831].
- **Switching costs are still low, so vendors must keep proving value at each renewal.** IKEA reports little stickiness so far, with a switch taking seven to eight months (expert call) [src-20260209-7ec831].
- **Why we should focus here: Procurement pairs a countable unit of work with buyers who already pay consultants and outsourcers, and the agents sit on the ERP, so deployment is short and results are easy to check.** Pricing per order or by consumption ties revenue to volume the buyer can see, and savings on spend leave room to raise prices as the agent handles more of each order alone.

**Example companies:** Didero, Lio, Magentic, Walter, Pactum, Pavus AI, HappyRobot, Augment, Levelpath, Omnea, Zip, Pivot

### Healthcare Revenue Cycle and Admin

- **Tailwinds: Healthcare billing, prior authorization and referrals are high-volume, rule-bound work that providers pay for by the claim or by the dollar recovered.** Amperos says it helps clients at 3,000 clinical locations recover claims worth "nearly $1 billion per year" (Amperos, claim) [src-20260422-d6ae9d].
- **Agents that do the work instead of assisting staff are growing quickly with providers of every size.** Lassie serves over 700 dental practices, has over $10M of annualized revenue (a16z) [src-20260603-ce0e80], and Candid Health grew ARR 190% (Sixth Street) [src-20260722-e6a1e0].
- **Providers that adopt these agents expand their use, which shows the savings hold after the pilot.** Adonis reports net revenue retention above 130%, so existing customers spend more each year (Adonis, claim) [src-20260325-9a969a].
- **Headwinds: Epic controls the record at most large health systems and limits outside AI, which slows startups in those accounts.** A Health Prime executive says Epic does not "allow integrations of AI outside of what they're already working on" (expert call) [src-20260608-5e7d7e].
- **Providers still review claims before submission because errors carry liability, so the agent does not yet replace the whole job.** A dermatology group's CIO asks, "If any of the wrong claims go in, who takes a liability?" (expert call) [src-20251016-371c9b].
- **The labs and outsourcers are moving into the same work with their own agents.** Anthropic released healthcare connectors and a sample skill for reviewing prior authorization requests (Anthropic) [src-20260111-f1affc].
- **Why we should focus here: Healthcare administration is paid by the claim or by the dollar recovered, so outcome pricing ties revenue to cash the provider sees on its own books.** Payer rules reward companies that take responsibility for accuracy and know the rules in depth, and margins rise as agents complete more claims without review. Epic's control matters least in independent and specialty practices that run other systems.

**Example companies:** Adonis, Amperos Health, Candid Health, GenHealth.ai, Procode, Prosper AI, Tennr, Assort Health, Thoughtful AI, Abridge, Lassie

### Insurance and Regulated Operations

- **Tailwinds: Insurance runs on outsourced servicing, underwriting support and claims work, much of it on old systems that agents can now operate directly.** Palomar's COO says Pace resolves more than 90% of its service cases without a human touch (Pace, claim) [src-20261025-c77b6e], and Prudential moved Pace from pilot to a multi-year agreement (Pace) [src-20261025-58fd6b].
- **Insurers already buy this work by the claim or by the policy, so pricing per unit is familiar to them.** Reserv sells claims handling as a service instead of seats (Reserv, claim) [src-20250604-fd80b0], and RYZE paid Pace a fee plus a cost per claim (expert call) [src-20260508-386718].
- **AI-native companies that hold an insurance license can sell the whole job and keep its economics.** Harper, an AI-native commercial brokerage, reports over 160 carrier partners and over 5,000 customers (TechCrunch) [src-20260225-3917a2].
- **Headwinds: Buyers are pitched constantly and can choose among many similar vendors, which caps prices.** An Accelerant executive who buys from Pace says he is pitched "at least two or three a day" (expert call) [src-20260811-a0aa1e].
- **Open-source models let new entrants undercut the established insurance operations vendors on price.** The same Accelerant executive expects a rival offer "at a 10th of the price by using open-source models" (expert call) [src-20260811-a0aa1e].
- **Returns can take longer to show than a buyer expects, which makes renewals harder to win.** A RYZE executive says the main value of Pace was handling surges in claims and that the full return was not realized before he left (expert call) [src-20260508-386718].
- **Why we should focus here: Insurance operations are outsourced, rule-bound and measured per policy or per claim, so agents are paid on the unit the insurer already buys.** Companies that do the regulated work as brokers, claims administrators or service operators carry the result, keep more of the price than tool vendors and face the least pressure from cheaper open models.

**Example companies:** Pace, Sixfold, Reserv, Harper, Federato, FurtherAI, DeepOpinion, ClearRisk AI, Notch, Otera

### Legal

- **Tailwinds: Companies spend heavily on outside counsel, and much legal work is priced per matter, which suits outcome pricing.** EvenUp prices per demand package (Bessemer) [src-20241205-4ac3cf] and says it handles 10,000 cases a week (EvenUp, claim) [src-20251007-efb7da].
- **Legal agents compete for the legal services budget that pays outside counsel, instead of the software budget.** Eudia's lead investor frames its market as legal services spending instead of software (Eudia) [src-20250213-7eb7f6].
- **Companies that take legal responsibility can sell the finished work instead of a tool.** Crosby is a registered law firm whose lawyers take liability for the contracts its AI reviews (Lux Capital) [src-20260331-50e583].
- **Headwinds: The labs are building legal products directly, which threatens companies that sell research and drafting tools.** Anthropic has released plugins for 12 legal practice areas, from commercial contracts to litigation (Anthropic) [src-20260512-5c6e2d].
- **Pricing finished legal work is hard, and getting it wrong is costly in the early years.** Crosby's Ryan Daniels says the firm lost a lot of money on its pricing until it got the pricing right (Stanford Law School) [src-20261025-1fbd1c].
- **Legal work depends on judgment, so lawyer time per matter may fall slowly and keep margins below software levels.** Daniels tracks lawyer review minutes every week because that cost sets the economics (Stanford Law School) [src-20261025-1fbd1c].
- **Why we should focus here: Legal work is expensive, often priced per matter and carries liability, so companies that take responsibility for the result can charge close to the price of the outside counsel they replace.** As the labs make drafting tools cheap, the firms that sell finished work under their own license become the stronger part of the category.

**Example companies:** Crosby, Eudia, EvenUp, Supio, Harvey, Ivo, Wordsmith

### R&D and Life Sciences

- **Tailwinds: Drug programs are expensive and slow, so agents that shorten research save money a drug company can measure.** Edison Scientific estimates about $99M of recovered peak sales per program from cutting the time to prepare regulatory filings (Edison Scientific, claim) [src-20260930-ed7d9b].
- **Research agents already do months of work in one run, which gives the vendor a clear unit to price.** Edison says one run equals about 6 months of a scientist's work, with 79.4% of conclusions judged accurate (Edison Scientific, claim) [src-20251105-cdfbed].
- **Large drug companies are buying and testing these agents now, starting with target discovery.** Incyte is deploying Edison's agent across its research work (BioPharm International) [src-20260519-f0a637], and executives at 6 of the top 10 drug companies sought more access to Edison's predecessor (FutureHouse) [src-20251105-9cd419].
- **Headwinds: Pricing is still experimental, which makes revenue per customer hard to forecast, and Edison charges $200 per run at a launch price it calls heavily discounted (Edison Scientific) [src-20251105-cdfbed].**
- **Drug results take years to arrive, which makes it hard to price on outcomes or prove value within a normal contract term.** Incyte and Edison will judge the work on decision quality and long-term pipeline productivity (BioPharm International) [src-20260519-f0a637].
- **The agents still make mistakes that need expert review, which limits how much scientist time they replace.** Edison warns that its agent can chase findings that are statistically significant but scientifically irrelevant (Edison Scientific) [src-20251105-cdfbed].
- **Why we should focus here, on a longer time horizon: Time saved in drug development is worth far more than in the back office, and companies that learn from each customer's data build knowledge the labs avoid, but today they sell runs and pilots and outcome pricing is years away.** Edison's $70M seed round (Edison Scientific) [src-20251218-eefcdb] shows the capital required, and we should commit as repeat use is proven.

**Example companies:** Edison Scientific
