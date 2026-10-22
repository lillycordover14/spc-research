---
theme: "Other"
title: "Software Engineering Manager at Coinbase Believes Hex Enhances Business Intelligence with Notable ROI and Collaboration Features"
doc_id: EC-1000000-232392
source_line: "Hex Technologies · Expert Call · Customer · 14 Oct 26"
date: 2026-10-14
company: "Hex Technologies"
pages: 2 of 2
saved: 2026-10-19T17:31:11.322Z
url: https://research.alpha-sense.com/search?search_id=tmp-0pnbg1kc8uodovl7vbczkp&sort=RELEVANCE&order=DESC&docid=EC-1000000-232392
---
# Software Engineering Manager at Coinbase Believes Hex Enhances Business Intelligence with Notable ROI and Collaboration Features

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

Hex Technologies

SMART SUMMARY

Summary

The interview covered the expert's experience evaluating, adopting, and implementing Hex as a business intelligence tool, including comparisons to previous solutions, key features, user adoption, AI capabilities, and areas for improvement.

EXPERT BACKGROUND

- Software engineering leader with 15-16 years of experience in software development, primary evaluator and decision-maker for onboarding business analytics (BA) and enterprise analytics (EA) tools, and led the migration and adoption of Hex as the main BI tool at a large technology company.

EXPERT SENTIMENT

- Very positive about Hex's impact, citing significant improvements in flexibility, collaboration, and speed compared to previous tools.
- Believes Hex delivers strong ROI and is critical for business decision-making, though notes some limitations in governance and AI capabilities.
- Optimistic that Hex's AI features will continue to improve, but currently sees room for enhancement, especially in handling complex schemas and granular access controls.

TAKEAWAYS

- Hex was chosen over Apache Superset and Google Looker due to its dynamic dashboards, integrated data transformation, and strong collaboration features.
- Hex's modular and reusable logic, fast data refresh, and AI-powered natural language query capabilities were key differentiators.
- Adoption is widespread within the organization, with 3,000-4,000 users, mostly read-only; about 20-25% use the AI natural language features, mainly for complex queries.
- Limitations include lack of deep context for complex internal schemas, need for human validation of AI-generated queries, lack of granular access controls, and absence of formal version control or data lineage features.
- The organization has fully migrated to Hex, and the tool is considered essential for business operations, with perceived ROI far exceeding the cost.

AlphaSense Smart Summaries are AI Generated

Introduction and Background

Adoption and Features of Hex

User Statistics and AI Features

Limitations and Migration to Hex

Value Proposition and Additional Feedback

EXPERT BIO

Software Engineering Manager at Coinbase

Seasoned Engineering Leader having around 15 years of software development experience with a demonstrated history of working in the technologies like Java, Go, Spring Boot, AWS, GCP, Redis, Kafka, docker, microservices and RESTful webservices. Skilled in Crypto, Ecommerce, Electric 2w industry, Payments Industry and Telecom.

Expert is a customer of Hex, Claude Code, Cursor, OpenCode, and CodEx.

View More

INTERVIEW TRANSCRIPT

**Client** [00:00:00]
Hi, I appreciate you taking the time today. Just to give you a little bit of background, I am doing some research into the business intelligence data analytics space, and just trying to do a bit of a market map and understand the various players out there and how they stack up against one another. Looking forward to your feedback today. To start, would love to just get your background.

**Expert** [00:00:23]
Sure. I was an engineering leader with over 15-16 years of experience into software development. I have worked on multiple development projects, and I was also the primary evaluator for onboarding the BA tools and EA tools and whatnot in my organization. I think you wanted to know more about Hex. Let me know if you want to talk about Hex or about other BA tools and how we migrated things from other tools to Hex.

---

**Client** [00:00:52]
No, I'm primarily interested in your experience with Hex. I think, to start, I'd love to spend a lot of time on just the story of you guys adopting Hex at Coinbase. When did the process start? What goals were you trying to achieve? Who else did you look at? How did the various options compare against one another, and ultimately, why you chose Hex?

**Expert** [00:01:17]
Got it. I will tell you the story behind why we went to Hex. In the past, we were using Apache Superset and also Google Looker. Both are good and it was working to some extent. The main problem is the Superset dashboards are static and it was hard to maintain, because you need to build the underlying pipelines, and the dashboards are always static, and whenever you need to change something, you have to change the underlying dataset somewhere else, and it will reflect in the dashboard.

Google Looker also scaled well for simple dashboards, but when the data grew and whenever you want to add more dimensions to the dashboard, that's when it gets complex, because the definitions of the dashboard stay somewhere and the dashboard is always static. We want the flexibility of updating the dashboards then and there, like a collaboration tool. We are looking for something where you can have everything side by side. Say, for example, we should be able to have the SQL queries, we should be able to have a Python script, and we also need the dashboards in one place. I was the one who was going through the list of other tools available in the market. This is when I was talking about in the beginning of 2025.

I found out Hex, and I also interacted with couple of my friends who are working in different companies who are already started using Hex. I was also going to the developer forums and some of the technical blogs to understand what is the best BI layer built currently and being adopted by other companies. I started evaluating Hex by getting a trial license, and I found it very powerful enough so that it bridges the gap between the Apache Superset and Google Looker. I proposed a plan to my executive team and I showed them couple of dashboards which I built it on Hex by using the trial license. I got a buy-in and we got enterprise license for Hex and then we onboarded Hex. That's how we got into Hex.

---

**Client** [00:03:26]
Got it. To go further into how was it Hex compared well to the other names? What other features or aspects of Hex really stood out to you guys as a team?

**Expert** [00:03:37]
Yeah. The main things which distinguishes Hex from other things is it's a dynamic, I would call it as a dynamic dashboard. When it's a dynamic, you can directly go and edit the dashboard, you can update the SQL queries, you can write the transformation logic in Python, everything in the dashboard. For other things, you need to write a Python code which will transform the data in somewhere in a different pipeline. The transformed data has to be saved somewhere in the dataset, which will be powering these dashboards.

In Hex, you don't need to worry about having a transformation logic elsewhere. The transformation logic or the intermediate code which can power the dashboards all can exist in one place. That's why if you see in Hex dashboard, you'll be having multiple things. It's like what you call drag and build. You can simply drag a SQL snippet or you can drag a Python file or you can drag the visualization, which is the dashboards or the charts or whatever. All of this lies in one place, which gives us very strong collaboration. It is similar to Google Docs. Say for example, you can have a Google Doc. Inside the Google Doc, you can create a table, you can embed a pie chart or whatever. Similarly, I would tell Hex as the Google Docs for the BI layer. That's what I will tell you.

One more thing is modern data workflows. In other cases, you have to build the workflows outside of your dashboard. Here, you can build the workflows within the dashboard. As I also told, Hex allows you to define the modular and also reusable logic. When I say reusable logic, say for example, in a Hex dashboard, you can define a SQL query and a Python script, which can be reused for a different dashboard. In other cases, you have to copy-paste it in every other dashboard or every other widget you want. In Hex, you can reuse the same logic for two different dashboards. One more thing is the duplication has reduced drastically in the Looker dashboards and other tools that we are using. There are multiple widgets which are duplicated.

In case of Hex, we are able to unify all the widgets so that a single widget defined somewhere else can also be reused in a different dashboard. For example, you have dashboard one, two, and you need widget one in both the places. Instead of duplicating the same underlying logic and the UI or the visualization in both the dashboards, you can define it in one dashboard, and you can drag and drop, and you can build the dashboard by reusing the same widgets present elsewhere. One more thing is also it is pretty fast when compared to other things. Meaning, whenever the underlying data changes, the changes reflect very fast when compared to the other tools. More importantly, very recently, Hex is also providing a lot of AI features, including the natural language query.

For example, if I type a query say, "Hey, I want to know all the sales data for U.S. region." It will be able to translate the underlying context into a SQL query, which will be powering a dashboard. You also have debugging capabilities where you can debug and see whether your query is running fine or not. Most importantly, we found out because the Hex dashboard, it is not only being used by the developers. Now we have our product team and some of the marketing and sales team also using this dashboard.

In olden days, I am talking about two years before, every time when they need to make some changes, they have to reach out to the engineering team or the data analysts or data scientists and ask them, "Hey, can you make these changes in the query?" Now with Hex, since they are using this natural language query generation, all they want to do is, "Hey, looks like this report is giving the sales data across EU region or U.S. region. Can you add a dimension by adding the U.S. state? I want to know which state contributes to most of the sales or which U.S. state is contributing to most of our sales." This natural language will be understood by the underlying Hex AI agent, and it will be able to transform the existing natural language into a modified SQL query.

It will be able to dynamically update the SQL query and it will be deployed immediately, so that the salesperson or the marketing person or the product person who is a non-technical user can immediately see the results. Of course, I agree, there are cases out of, say, 10 instances, there are one or two instances where Hex is not able to generate the accurate query. 90% of the cases, it's able to generate the query. In 10% of the cases, it needs human in the loop. Because of all these reasons only, we moved away from other things to Hex, and these are our major features or use cases for which we use Hex.

---

**Client** [00:08:58]
Got you. How many users across Coinbase are on Hex? What's the ratio between viewers, and is it editors, the other user type?

**Expert** [00:09:07]
I cannot tell you exact number but I can tell you a range. It is close to 3,000-4,000 users. The write to read users will be easily 4:one. Meaning out of five users, four users were read-only users. One user will be having the write permission. That is because, as I told you, not everybody is interested in generating dashboards but lot of people are just consuming the dashboards. That is the reason we have more read users than users who have access to write.

---

**Client** [00:09:43]
Got it. For all users, what percentage of use cases or just usage of the product is the natural language AI features? Is it a side feature that some people use, or is it becoming more core to the user experience?

**Expert** [00:10:00]
I want to answer this from two perspectives. One is, yes, overall, the usage of these AI features, especially the natural language generation, is increasing day by day. The ratio of the users who are using that feature is quite less because of the fact, as I mentioned, the write users who have access to Hex dashboards are mostly data scientists, data analysts, and developers who already have the SQL knowledge. For them, they already know Hex is good at generating the queries. They don't want to beat the bush by giving the natural language and Hex giving them an initial version of the query, and then they're reiterating or rechecking it.

Most of the times, what these technical people will do is they start writing their own query instead of relying on the natural language. For complex cases, for example, there are multiple tables and multiple joins, which is quite complex for a human to write. In those cases, they rely on the natural language. To answer your question, the ratio of the users who use this feature, I would say, will be around 20%-25% overall.

---

**Client** [00:11:11]
Got it. How about things Hex could improve on? Dislikes of the product, your customer experience, in general, and also with respect to the natural language and AI features.

**Expert** [00:11:23]
Yeah. The main limitation is Hex doesn't have deep context about our internal schemas. Say for example, it is able to generate queries if you give a prompt about a single table, but when you ask it to do complex things like, "Hey, I want to know how many users were paid users in the last one month who has already completed the identification verification or who has completed the phone verification." Now, this needs to query the users table or the user schema or user database and then it also needs to query the payments table. It also needs to query the risk table. It also needs to query the portfolio table.

When there are multiple schemas involved and when there is a complex relationship between different tables where you need to apply more filtering. Say, for example, user might have made four or five payments. The four or five payments will have different payment IDs, though they are linked by user IDs. Sometimes there is no direct relationship. Say for example, you have user ID reference in almost all the tables, but in some of the tables, you'll not have user ID reference. Instead, you will have a UID or some other reference.

When the schema gets quite complex, Hex is not so good at developing a context about the internal schema, but if you tweak it a bit, say for example, if you ask a natural language query, if it gives you a data or query, by reviewing the data or query, if you tell it, "Hey, looks like you missed something." You forgot to consider the risk table or the onboarding table, then it will be able to double-check, and it is able to come up with the correct answer or the correct query in the second iteration or third iteration.

Most of the times, when there are complex internal schemas, it is not able to come up with the correct query in the very first iteration. That is the major limitation we are seeing. This limitation is because of the fact that Hex is an external tool. Though the integration is done in-house and whatever, still Hex is just an additional wrapper over the existing data or schema. It also needs strong context about these things. With LLM models nowadays and with the AI tools getting better day by day, I feel this is also getting better day by day. Still, I would say it is not there where I can say, "Hex has 100% context about your internal schemas." This is the major drawback.

Second one is, whenever there is a complex joins or business logic, there is a slight latency introduced when there is a complex business logic or whenever you are doing complex joins. For non-technical stakeholders, the main problem we are facing today is, though people know we can ask queries in human language and it can generate SQL queries, they always wanted a human in the loop to validate before they can even publish. Now, that is becoming a bottleneck. As I mentioned to you, out of five users, four users are read-only users, and only one user is a write user who has the context. Now, all these four users, though they are able to generate the dashboard, they are fearful to publish the dashboards because they want someone to validate this and say, "Hey, this is 100% right."

Now, that validation can also be done by the subject-matter expert. Now, what is happening is naturally they are still blocked on the people. Earlier, they are blocked on people to develop the dashboards itself. Now, they are able to develop the dashboards themselves, but they want someone to validate it, and that bottleneck is increasing day by day. I think honestly speaking, since I was also closely observing the AI space and LLM models are getting better day by day. If I look back how Hex AI agent works six months before versus now, I would say there are drastic changes in the performance. It is doing better. You have to watch out for this space. I believe, in future, it will get better and better.

---

**Client** [00:15:44]
Got it. Maybe I missed it before, remind me. Have you moved entirely over to Hex, or are there still some instances for which you use Google Looker?

**Expert** [00:15:56]
We moved completely to Hex. In the initial phase, after migrating for three, four months, we are using the Superset, Google Looker, and also Hex together. After three, four months into the migration, we validated every Hex dashboard, and we made sure everything is right, and then we moved everything completely to Hex.

---

**Client** [00:16:20]
Got it. How do you feel about the value that you're getting for the cost of the product? It sounds like it's been a very valuable product and is important to your organization, but how do you feel about that value proposition relative to the price that you're paying?

**Expert** [00:16:37]
Are you talking about what is the return on investment?

---

**Client** [00:16:42]
Yeah.

**Expert** [00:16:43]
I think this is sometime back, our leadership team is also asking about some metrics around this, but still, this is a tricky one. I will tell you why, because if you see most of the dashboards, which we use through Hex or without Hex, these dashboards are used as an input for the marketing or the sales team. Say for example, we have dashboards across all the geos to see how many users are onboarded into the crypto platform. We have a dashboard saying, "Hey, what is the monthly active trade done by the active users across geos?" Now, this data is being used by product team or the business team to prioritize the upcoming projects. Say for example, if the crypto adoption is more in U.S. or if it's more in Canada, then the company will invest more in those regions.

Now, we don't have any single data point to tell what is the ROI, but it's a combined metric across all the things. I would say it's very critical Hex. I would say, this is the number one priority for the company to give the high-level overview about what exactly is happening inside the company, the revenue, the sales, the funnel, and the onboarding funnel, and how many users are onboarded, how many users are doing the first trade, how many users are onboarded successfully but not doing any trade.

All these key metrics that are responsible for the marketing or the sales team or the product team to come up with the next yearly planning or whatever. Definitely the ROI is more than what we are spending on Hex. It will be definitely 5X or 10X, but honestly, there is no direct metric and I cannot give you exact number on this.

---

**Client** [00:18:30]
Directionally, that's still very helpful. These are all the questions that I had, but anything else? Any other things about your experience using Hex that we didn't talk about that we should have?

**Expert** [00:18:44]
Yeah. One more thing I want to tell you is, Hex doesn't have much of the governance side of things and you don't have a lineage or version control. When I say version control, say for example, in Google Sheets. This is something I have given feedback to the Hex team directly in one of my interactions. Whenever you are deploying Hex dashboards in a larger organization, we need to worry more about the governance and the permissions, like RBAC and whatnot. The access controls is also not granularly defined in Hex. Say for example, if there is a dataset and if the dataset is containing some of the PI information, I should be having access, "Hey, I want all the users in a particular LDAP group only to see the PI information, and others should not be able to access that."

Now Hex is not providing that granular access controls today. We are working around it by saying, "Hey, if a person is not intended to see the PI data, then let him not see the Hex dashboard at all." It's zero or one. Either a user will be able to see the dashboard and access the underlying data or not. What I want to do is, if there are 10 columns or 10 different rows in a table, if one of them is containing the PI data, I want more granular controls where I want the user to see other data, other non-PI data, but not the PI data. That functionality is not there.

One more thing is, as I mentioned, version control. In Google Sheets, if you make some changes, it will become a new version and you can always revert to the older version at any point of time. Similarly, Hex is not providing any formal versioning. It would be excellent if they can provide these two features.

---

**Client** [00:20:39]
Got it. This has been very helpful. Thank you. Have a great day.
