---
theme: "Enterprise Software & AI"
title: "Chief Data Scientist at Dell Technologies Inc. Believes Glean Is Effective for Non-Technical Users but Limited for Technical Teams"
doc_id: EC-1000000-232334
source_line: "Glean · Expert Call · Customer · 14 Oct 26"
date: 2026-10-14
company: "Glean"
pages: 2 of 2
saved: 2026-10-19T17:24:31.157Z
url: https://research.alpha-sense.com/search?search_id=tmp-0pnbg1kc8uodovl7vbczkp&sort=RELEVANCE&order=DESC&docid=EC-1000000-232334
---
# Chief Data Scientist at Dell Technologies Inc. Believes Glean Is Effective for Non-Technical Users but Limited for Technical Teams

Company Deep-Dive

DATE PUBLISHED

14 Oct 2026

INTERVIEW DATE

16 Jul 2026

EXPERT PERSPECTIVE

Customer

ANALYST PERSPECTIVE

Investor-Led (Buy-Side)

PRIMARY COMPANY

Glean

SMART SUMMARY

Summary

The interview discusses the deployment and use of AI agents and enterprise search tools across different departments, highlighting the division between technical and non-technical users and the selection criteria for various AI solutions.

EXPERT BACKGROUND

- Chief Data Scientist responsible for global AI and machine learning operations, strategy, and infrastructure selection at a large technology company, with direct experience evaluating and deploying enterprise AI tools and workflow automation solutions.

EXPERT SENTIMENT

- Views Glean as effective for non-technical business users but sees its limitations for technical teams focused on database operations.
- Believes that more technical teams are shifting towards tools like Databricks Genie and Anthropic Claude Cowork due to their advanced capabilities and better fit for technical workflows.
- Predicts that Glean usage will decrease within technical teams as more advanced or specialized tools become available, though non-technical teams will likely continue using Glean.

TAKEAWAYS

- Glean was selected after a competitive evaluation for enterprise search and workflow automation, primarily due to its performance and existing partnership.
- Glean is used by around 300 users across departments such as finance, marketing, sales, and the expert's technical team, mainly for unstructured data and enterprise search.
- Technical teams prefer Databricks Genie and Anthropic Claude Cowork for database and advanced AI operations, while Glean remains favored by business analysts for its user-friendliness.
- There is no unified data layer; different tools are used for different data types and user skill sets, with Glean handling unstructured data and Databricks/Teradata handling structured data.
- Token-based pricing is not a major concern for the company, as usage patterns and business priorities outweigh cost considerations.

AlphaSense Smart Summaries are AI Generated

Introduction and Initial Collaboration

Expansion into Agent Automation Tools

Integration and Data Source Management

Agent Context and Data Utilization

Comparative Analysis and Future Directions

EXPERT BIO

Chief Data Scientist at Dell Technologies Inc. The expert can speak to the implementation and utilisation of AI infrastructure and tools, providing insights into enterprise-level context management and decision-making processes.

Chief Data Scientist at Dell Technologies. Reporting to the Chief Marketing Officer, the expert is responsible for leading a 50-member decision sciences organisation that utilises patented, advanced statistical modelling to measure and optimise global go-to-market investments. In this role, the expert oversees an annual advertising budget of over $1.2 billion across consumer, small business, and large enterprise segments. The expert has full authority over developing marketing media mix models, managing onsite and offshore teams in the United States and India, and expanding analytics functions into supply chain, services, and corporate social responsibility. Notable achievements include increasing advertising Return on Investment by more than 15% through econometric modelling and receiving the Michael Dell Champion Award in 2019.

The expert can speak to procurement and capacity planning for Graphics Processing Unit and Artificial Intelligence data centre infrastructure, specifically regarding power and cooling requirements. The expert has implemented and utilised various infrastructure software solutions, including schedulers and cluster managers such as Slurm, Kubernetes, and Ray, as well as monitoring and observability tools. Additionally, the expert is an expert in the day-to-day operation of Artificial Intelligence clusters, workload scheduling, and maximising Graphics Processing Unit utilisation. They are also highly proficient in using "digital twin" simulation tools for data centre performance modelling and capacity planning scenarios.

View More

INTERVIEW TRANSCRIPT

**Client** [00:00:00]
Hello, thanks for taking the call today. I want to learn more about how enterprises are deploying agents specifically. If that sounds good for you, I think we should probably start off with a quick intro on your end, just briefing on your role and your decision of onboarding Glean.

**Expert** [00:00:18]
Yes, absolutely. Certainly can help because Dell is a big customer of Glean, and we also go to market together, enable Glean to install in the AI servers we produce. My responsibility, I cover basically all the AI and machine learning operations for Dell globally. I also cover some of the business intelligence as well. Not only for the operations, I also am responsible for the AI machine learning strategies formation and then also related compute infrastructure selection.

For all the AI tools, my team will be the first to use to test and see whether the tool is super powerful for other Dell's, the stakeholders from other departments as well. That's the reason why we use the Glean as the enterprise search and workflow automation tool in my team and also for sales, marketing, and finance as well.

---

**Client** [00:01:08]
Got it. Basically, because you mentioned that you are an early partner of Glean, when you were deciding to look for a solution in the field, what prompted this and when did you start working with Glean together?

**Expert** [00:01:21]
Sorry, can you repeat your question?

---

**Client** [00:01:24]
100%. My question was since when do you work together with Glean, and what was the original motivation to start working with them or look for a vendor like Glean?

**Expert** [00:01:35]
Okay. I remember it was last year, in Q2 last year, we would like to have an internal enterprise search tool. We also want to do some degree of low automation, especially across different enterprise tools we use, for example, salesforce.com and then Excel file, PDF file. At that time, we evaluated, I remember, three vendors. Glean is one of them and because the go-to-market relationship between Dell and Glean. At the end of the day, even during the request for proposal, Glean performed better than the other two tools. We selected Glean, and then that's how we started.

---

**Client** [00:02:15]
Got it. That sounds to me as if you started off with the enterprise search tool that they were having. Obviously, then they went into the agent tools afterwards, allowing you to build automations. Did you guys then also expand into the agent automation tools, into the context layer that they're offering now as well?

**Expert** [00:02:35]
Yes, we do.

---

**Client** [00:02:37]
Got it. For which use cases and for which teams are using Glean at the moment?

**Expert** [00:02:44]
Currently, we have around 300 users. Some more than heavy users, actually, eat a lot of tokens, but my department, finance, marketing, and sales.

---

**Client** [00:02:54]
Got it. How did you integrate Glean in the beginning? Initially, it was just a search tool, and you just have to give it access to all your other data tools, but now it became a context layer.

**Expert** [00:03:07]
That's correct.

---

**Client** [00:03:09]
Curious how did Glean plug into your existing data sources?

**Expert** [00:03:13]
Yeah. Glean is very good at actually managing the data governance and data security. It's probably one of their most important sales pitch, and then the next one their AI assistant. IT helped us to implement Glean in our on-prem space. Glean has the connectors to connect with our SharePoints. I don't think we allow Glean to connect with our Teradata yet, which is our enterprise database.

However, Glean connect with tools we use, salesforce.com, ERP, SAP. Glean also connect with the Confluence, is the enterprise collaboration tool, Jira, the IT ticket, and then not to mention the huge repository, so internal document, PDF file, Word, Excel. Those are the data sources Glean can connect to at this stage.

---

**Client** [00:04:03]
The one that you mentioned that you're not connecting it to, which one was that?

**Expert** [00:04:08]
Teradata, which is our central enterprise data warehouse.

---

**Client** [00:04:12]
Okay. It's basically a data warehouse, I assume, this one.

**Expert** [00:04:18]
Yeah.

---

**Client** [00:04:20]
Got it. How come you're not connecting it to that?

**Expert** [00:04:23]
First of all, Glean is very good at do the enterprise search, especially through those semantic search through the unstructured data, Excel file, PDF file, Word file. For the database, it's all column, row, and then a lot of them are just numbers. We just don't think Glean can do a very good job to grab the raw data from database and organize it and try to automate the process. Not to mention, it's not a SQL tool, even though it can write SQL, but it's not decent. We just use it to its advantages, connect those semantic search.

---

**Client** [00:04:58]
Makes sense. It's mainly focused on any unstructured data or trial knowledge in the company that lives more on the Salesforce, your ticketing systems, and your communication channels. Everything really structured data, financial data, and so on, that's separately handled by Teradata that you mentioned.

**Expert** [00:05:18]
Exactly. As you could imagine, majority of the users, they are MBA-type business analysts. They are not data scientists or data engineers, but Glean perform extremely well in that domain.

---

**Client** [00:05:32]
Got it. If we look a bit more on the agents that you're running right now, I would love to understand for the agents you're running, how you bring context to them. I would assume some of the agents that you mentioned are just hooked up to Glean. They get the context through Glean. I assume that you probably have also other systems running beyond the Glean system with actual agents. Curious, how do you bring the data that you have, be it the structured data in Teradata, but also the unstructured data that lives probably more in Glean then, to the agents for them to have the right context?

**Expert** [00:06:10]
Good question. I certainly can speak for my team and the stakeholders. I know their operations. We do actually deploy other AI agents as well, especially around database. I can give you one example. My team store a lot of data in Databricks, both unstructured and structured data. We do the API codes and connect with Cohere and Anthropic to train our own data and come up with the chatbot. For that type of operation, we use the agent AI assistant tool in the Databricks. It's Genie.

However, outside of database, especially if we need to connect with the tools most of the business analysts use, for example, Power BI and then Excel, Word file, PDF file, we use the Glean to help us to build up the agent AI function and to also do the workflow automation. We use different tools to do different types of things. It also depends on the skill set.

---

**Client** [00:07:11]
Got it. The takeaway from this is that you have, let's say, very different data sources ultimately. You have the one in Databricks, you have Teradata, you also have the unstructured data in Glean. There's not a one unified data layer in a way. It's more like for a specific use case, you have specific data warehouses, and those ones that are then connected to various different agents, for Glean, their own agents, For Databricks, you mentioned Cohere and Anthropic and so on, so on. The context layer is not really one, but there are various different contexts, warehouses in a way.

**Expert** [00:07:52]
Yes. Your understanding is 100% correct.

---

**Client** [00:07:56]
Got it. It sounds like the majority of the agents that you're using are based on third-party tooling, also Cohere here in this case, half of you guys are Glean. Do you also build agents yourself entirely in the way that you have engineers sit down and use open-source repositories to build a context layer, or you have engineers who try to plug into some of the toolings out there to build their own agent in-house, or is it mainly outsourced through third-party tooling?

**Expert** [00:08:27]
Good question. Look, if you look at those large language models, all the AI assistants, because if you look at Glean, if you look at the other graphical knowledge tool, like Stardog graphic-wise, even for Databricks, it's Genie, those AI assistant tools, those companies, they do not have their own foundation model. They always pull out the large language model from those Big Three.

If you look at those foundation model solution companies, Anthropic and OpenAI, they can only work in the CSP environment. I believe there's a way for them to deploy their models in the private cloud or on-prem space. They just choose not to do it. Currently, only Cohere can work in any environment, air-gapped, CSP, neocloud, on-prem.

We certainly need to test out those tools because the AI server we produce, we sell those servers to neocloud and Fortune top 50 or top 100 companies. We internally do test out the open-source large language model from Meta. However, our IT or my team has not built the agent AI tool around those open-source foundation models yet.

---

**Client** [00:09:39]
Got it. Maybe if we come back a bit to Glean here. I would love to get your view on why the use case you're using Glean for cannot be done by Databricks in this case. I think Databricks also has their Databricks Genie feature, which is one way to query the data. Since you mentioned that Databricks both includes structured, unstructured data, it sounds like they could also take over some of the things that Glean is doing.

**Expert** [00:10:07]
Yes. Be very honest with you, as I mentioned earlier, it's skill set. In my opinion, the whole Databricks infrastructure and the tool, the system set up, it's more for the developers or for data scientists or data engineers. It's not very user-friendly for MBA-type business analysts. My team, as long as the data is in the Databricks environment, right now, all the AI-related, agent AI workflow automation, for example, we automate the data pipeline is SQL.

Genie help us to come up with all the SQL queries, do the data prep, and then even come up with the BI dashboard. We do everything within Databricks. We actually do press Tableau, we do press Power BI, but that's for my team. We gradually began to move not all, but some of the Glean operation or orders to Genie. However, the other teams, they do not have this type of skill set. They seldom use SQL. They don't understand database functionality well enough.

All the data they have, most of them is Excel files, PDF files, Word files. They need to come into salesforce.com to actually pull some data out. They need to go to Confluence to pull some company documentation, whatever. On that part of the operation, they still use Glean. I really do not believe for finance, for marketing, for sales, they would like to learn how to use database and then just move their operation to Genie. No, it's completely different skill set, different requirement, different applications.

---

**Client** [00:11:47]
Got it. On the one side, Genie is the attempt of Databricks to become more open to non-technical users, but it's still not user-friendly enough yet to give this in front of your business grads to work with this.

**Expert** [00:12:00]
That's correct. I do want to point out, my team also subscribe to Anthropic Claude Cowork. When we use Cowork, we find out it will be a tool one day is going to replace Glean, especially Glean does not have its own foundation model. Anthropic has the foundation model, and Cowork exactly targets Glean.

---

**Client** [00:12:20]
Okay. Basically, on the one side, you have Claude Cowork eating up some part of Glean's pie. On the other side, you have Genie coming in. What happens for you guys is that ultimately, I would assume the Glean usage is going down, and you're shifting workloads away from Glean to either Claude Cowork or to Genie.

**Expert** [00:12:42]
Yeah, at least for my team. We are very familiar with Claude environment, Anthropic environment. We use the AI coding tool from the Claude Code. Cowork is very natural to us. Gradually, we almost move all the database related to Genie, and then for the enterprise search-related, we almost move into Cowork. We are not going to force our stakeholders to use any tool as long as they are happy.

---

**Client** [00:13:08]
Got it. Is there an issue with digesting context as well if you move to Claude Cowork? Obviously, Claude Cowork is good if you're going to give it the right file systems, but especially if you want to ingest a large amount of data, it needs some help with that aspect of it. Have you looked into any additional context tools based on that?

**Expert** [00:13:31]
Yes. You mentioned a good point. If I use Claude Cowork, I certainly need to upload a lot of data to Anthropic environment. It would eat a lot of tokens. At least for my team, probably we are more technical. The methodology we are looking for, the accuracy of the answer we are looking for, our standard is different from the other teams, even though our cost will increase.

By the way, when we use Glean, we also need to pay for the token. It's not a flat rate. It's a consumption-based pricing. If we use Glean to tap into more tools, ask more questions, semantic questions, our cost will increase anyway. Again, for my team, we are less care whether it's user-friendly because we are more technical. All my team members, they are either data scientists or data engineers. We are more care about whether we can get a better methodology to analyze our data. In that regard, we would prefer Databricks Genie or Claude Cowork.

---

**Client** [00:14:36]
Okay. If you make that more specific on the point of, let's say, what Glean is not doing well, what are some of the main shortcomings for Glean? Why does that motivate this shift over to Databricks and to Cowork?

**Expert** [00:14:50]
You are correct. I'm literally not saying Glean cannot deliver. I'm just saying that because my team, the entire team's operation is around data, database, data warehouse, and then we are very used to write a code. We are very familiar with how Anthropic works. We just move the operation over there. We still have the Glean operation, don't get me wrong. If we just need to tap into salesforce.com, do the model documentation, the PDF file, the Word file, Excel, we still use Glean.

---

**Client** [00:15:24]
Got it. Maybe one final question from my side, how much does cost of, let's say agents matter for you guys? How important is token costs whenever you're running agentic workflows?

**Expert** [00:15:38]
Good question. That's really, really good one. Can I be very honest with you? As long as the sales stock price perform well, we probably less care about it.

---

**Client** [00:15:51]
Okay.

**Expert** [00:15:51]
No, that's the honest answer. I'm serious. Look, we are not Uber or Meta. Uber, Meta, majority of their employees are software engineers. They are writing a code, their daily job, day in and day out. We are not. Look at the other users of the Glean. Most of them, I would say 80% business analyst, 10% director and just try to find information. If they could be sales, they use Glean. They just do the post-bank directors.

Another 10% is my team, the technical users, but we are not burning tokens like crazy, no. We basically have a central depository for those Excel files, PDF file. Different department would have their own depository. That would be their knowledge base or knowledge database and tap into that. Usually, the token spend is not crazy high, to be very honest with you.

---

**Client** [00:16:51]
Got it. This was super helpful. Thanks so much.
