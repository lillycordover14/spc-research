---
theme: "Energy & Grid"
title: "Senior Manager at RWE AG Praises Seeq's Analytics Platform for Operational Engineering in the Power Sector"
doc_id: EC-1000000-233924
source_line: "Seeq · Expert Call · Customer · 19 Oct 26"
date: 2026-10-19
company: "Seeq Corporation"
pages: 2 of 2
saved: 2026-10-21T16:32:10.475Z
url: https://research.alpha-sense.com/search?search_id=tmp-l5q00vjpbwvf9aw6o2hl&sort=DATE&order=DESC&docid=EC-1000000-233924
---
# Senior Manager at RWE AG Praises Seeq's Analytics Platform for Operational Engineering in the Power Sector

Company Deep-Dive

DATE PUBLISHED

19 Oct 2026

INTERVIEW DATE

21 Jul 2026

EXPERT PERSPECTIVE

Customer

ANALYST PERSPECTIVE

Investor-Led (Buy-Side)

PRIMARY COMPANY

Seeq Corporation

SMART SUMMARY

Summary

The conversation covered the expert's use of Seeq as an analytics platform for operational engineering in the power sector, including integration with existing data systems, deployment timelines, user adoption, pricing, and comparisons with third-party analytics solutions.

EXPERT BACKGROUND

- Senior manager with 15 years of experience in the power industry, overseeing utility-scale solar, BESS, and onshore wind assets, responsible for operational reliability and performance, and experienced in deploying and managing analytics platforms for asset monitoring.

EXPERT SENTIMENT

- Very satisfied with Seeq's current capabilities, especially its flexibility and user-friendly interface for engineering analytics.
- Sees room for improvement in Seeq, particularly in adding more built-in AI capabilities and ready-to-use templates for battery analytics, which would reduce reliance on third-party vendors.
- Unlikely to switch from Seeq in the near term due to deep workflow integration and high switching costs, unless a competitor offers significantly better capabilities or pricing.

TAKEAWAYS

- Seeq is used as the primary analytics platform for day-to-day engineering analysis, with most engineering work and model building done within the platform, while advanced analytics and machine learning are handled by a separate analytics team using Python.
- Integration with SCADA and PI System is crucial; Seeq acts as an analytics layer on top of existing data sources, enabling efficient data analysis and visualization without manual data extraction.
- Deployment of new use cases in Seeq typically takes 3-4 weeks, while initial platform implementation and integration can take 2-3 months, mainly due to data validation and user training.
- The expert's company has used third-party battery analytics vendors like ACCURE but found limited incremental value compared to internal analytics, and plans to reduce reliance on such vendors.
- Seeq is competitively priced on a subscription and user-license basis, and delivers strong ROI primarily through engineering time savings and improved asset reliability, though further AI automation could enhance value.

AlphaSense Smart Summaries are AI Generated

Introduction and Expert Background

Analytics Platforms and Model Development

Usage and Integration of Seeq

Third-Party Analytics and Support

Evaluation and ROI of Seeq

EXPERT BIO

Senior Manager, Operations Engineering, Bess/Solar Pv Rwe Americas at Rwe AG.

Senior Manager, Operations Engineering, BESS/Solar PV - RWE Americas at RWE. Reporting to the Director of Engineering, the expert is responsible for leading the North America Parts and Refurbishment Engineering business, supporting Onshore Wind and Battery Energy Storage Systems operations engineering. The expert's work involves failure analysis, component lifecycle optimization, and asset reliability improvement. For Battery Energy Storage Systems, the expert supports capacity testing, degradation tracking, State of Health analysis, and augmentation planning across utility-scale sites, while also collaborating with original equipment manufacturers and utilities to resolve performance issues.

Prior to this role at RWE, the expert was the Senior Wind Turbine Generator Engineer and Interim Category Manager for Wind Turbine Engineering in the Americas, leaving in March 2023. Reporting to the Head of Wind Turbine Engineering, the expert was responsible for leading the North America Parts and Refurbishment team. This included driving the performance and reliability of wind turbine components, overseeing refurbishment progress, supporting fleet operations, and managing the design of test benches for electrical and mechanical parts.

The expert can speak to the Solid-State Transformer market, identifying key players as ABB, Siemens, Schneider Electric, Hitachi Energy, GE Vernova, and Mitsubishi Electric. The expert also works with low-voltage distribution transformers in renewable applications and believes Solid-State Transformers have clear potential in low-voltage use cases such as electric vehicle chargers and data centers, although cost and reliability remain limiting factors. Furthermore, the expert can discuss how Medium Voltage Solid-State Transformers may eventually replace low-voltage solutions by consolidating conversion stages, but sees a hybrid approach as more practical for current deployment.

View More

INTERVIEW TRANSCRIPT

**Client** [00:00:00]
Thank you for speaking with us abou Seeq, their main products and use cases. It would be great to start off with maybe your overall background and then some detail about your current role and responsibilities, and then we can go from there.

**Expert** [00:00:15]
Firstly, we have been using Seeq since close to three years now. I work as a senior manager in operations engineering division, and I have been in the power industry for close to 15 years. Right now, here at RWE, my main role is to oversee our utility scale solar BESS and then onshore wind assets. I am basically responsible for maintaining the reliability and performance of our operating assets.

Thinking about my day-to-day work, we monitor the plant performance, investigate different trips, any kind of abnormal events, performing root cause analysis. We have to work closely with our operations engineering OEMs and other software which we use, software vendors. A large part of my work involves using all of this operational data, which I see inside Seeq, and then we make engineering decisions based on that.

I would say I spend about two to three hours easily as a manager, but then I have a team of six people, six engineers. I think they work on Seeq almost maybe six to seven hours a day. We collect data from our SCADA systems, historians, other field devices.

We have our own analytics platforms also, so that we can have a better understanding about how our assets are performing. That is pretty much what I do. I have about 11 sites under me. Our company has about 16 GW of operating assets, and another eight GW are in the construction phase with the COD date of 2028. We are aggressively expanding right now.

---

**Client** [00:01:50]
Got it. That is super helpful. When you talk about, you mentioned, I think you have your own analytics platform also, in addition to Seeq. Can you talk more about that?

**Expert** [00:02:01]
We have a huge analytics team. We have over 25 people in our company. We develop our own models around degradation when it comes to BESS systems. We monitor temperatures. We monitor different types of voltages, currents. Then we have our own models which we have developed with the help of machine learning and all of the operational data which we have to create that trend. Then we use it.

Again, it really depends on site to site because with batteries, it is really important what chemistry we are dealing with. If it is a lithium-ion chemistry, then we have a different model for that. For NMC, we typically follow a different model. Yes, all of that is created in-house by our analytic engineers.

Then, these platforms which I am talking about, they sit on top of our historian and other data sources which we have. What happens is this allows our engineer to quickly search that historical data. They can build trends. They can compare events. They can create calculations. They can monitor KPIs without spending a lot of hours manually exporting that data from different systems. We have been doing this for quite some time now. It is not that we have just started working on these models, but it is good to have something internal.

---

**Client** [00:03:23]
Yes, that makes sense. Just to clarify my understanding, when you are developing your own models around your specific use cases, is that something you are doing within the Seeq platform? How often are you working within the Seeq platform versus doing something on your own, away from that platform? Is this all in Seeq?

**Expert** [00:03:43]
Most of the engineering work is done within Seeq. We typically use Seeq to build calculations, to identify patterns, compare events, create conditions, and then we also develop analytic models within Seeq for monitoring the equipment performance.

Now, for more advanced analytics or our machine learning, that's when our guys in the analytics team, they use things like Python, which is, I think, one of our data science team's core engine.

For day-to-day engineering analysis, Seeq is our primary platform. Building model is not something we do every day. We typically develop them or refine our analytics whenever we are investigating a recurring issue or whenever we are introducing a new KPI or monitoring any kind of known failure mode. Once that analysis is built, it is then reused and updated as needed. Like for instance, degradation modeling. One of my site, which is 100-MW-hour site, these lithium-ion batteries degrade every single year.

What we have done is we have taken all the results of the capacity test, and then we have feed it into that analytics model, which we have created internally. Now we know what will be the degradation trend for the next year, considering if we are going to take into account the cycling the loads in the same manner as we have been doing in the past few years.

It really depends. All of these models are not AI models. I would say most of them are engineering analytics models, which involves a lot of calculation, trend analysis, conditions and things like that.

---

**Client** [00:05:18]
Got it. That makes sense. Thank you for clarifying there. When you are developing these algorithms within Seeq, I know that Seeq has a support team that they offer to help co-develop on their platform for specific use cases. Do you use their team or do you do this all in-house on the platform?

**Expert** [00:05:37]
We use them, again, from time to time, because at the end of the day, we are developers. I would say initially, yes. Whenever we are trying to implement, and I am talking about some of the more advanced use cases, we do work with their services team. We are still working with them on couple of our projects.

Seeq is relatively new for us as well, for some of the engineers. If you ask me how familiar I am with Seeq like a year ago, I would say not at all. I used to rely on my SCADA data. Then my PI System. All the data which we are seeing inside Seeq is actually coming from PI and from SCADA. Now since we have started to get ourselves used to Seeq, we are learning more and more.

On the professional services team side, we are in contact with them. We have taken some kind of service with them because those guys help us understand the best practices. We have this regular training, which happens right now, I would say, I have seen two or three invites in a month. That training is specifically built around analytics and how to optimize calculations on the entire workflow. I have been part of it from time to time.

---

**Client** [00:06:51]
Got it. You have been using Seeq for, I think you said three years. For you specifically, you still used your own process until about a year ago.

**Expert** [00:07:03]
I was relying more on the SCADA because we were still in the process of integrating Seeq with our internal workflow. We have different SCADA systems across all of my sites. That is also one of the reasons sometimes, if you have not integrated that site well enough with Seeq, there is a chance that you might get bad data, which I am seeing in one of my sites right now.

I am trying to figure this out, to get that corrected. It really depends on how well that integration has happened. That is also one of the reasons why I still have to open up SCADA and EMS from time to time to look at the data.

---

**Client** [00:07:39]
Got it. Would you say the primary users, I know you mentioned how often you as a manager and your team is working day to day in Seeq. Is your team really the primary users of this? Are there any other, either primary or regular users of Seeq, in the company?

**Expert** [00:07:56]
Primary users would be the engineers, the site operators, the people from the energy trading group. They use it sometimes too. I would say mostly it is the operation engineers, which is where I sit in, and then our reliability engineers, and they are the ones who use Seeq most frequently for troubleshooting, for doing RCA or performance analysis.

We also have SCADA and control engineers. They use it for their own investigation if there are any kind of communication issues. We have also asset management teams. I know a couple of folks there who have been using it to track their KPIs, identifying any kind of trend. Like I said at the beginning of the call, we have our analytics team who are right now working to build more advanced dashboards and calculations. To answer your question, majority of the day-to-day users, I would say they are engineers.

---

**Client** [00:08:51]
Got it. I might ask more about this a little bit later in the call, but when you are thinking about the solutions and the use case specifically that Seeq offers your company as a platform, is there anything missing there that you would either expect them to offer or that you wish that they offered that would make the solution better for you or make it easier to use or anything like that?

**Expert** [00:09:13]
A couple of things. Overall, right now I am very satisfied with Seeq because Seeq covers most of the analytics use cases which we need. I think would probably like them to build in more AI capabilities that can automatically detect faults, anomalies, and maybe suggest some possible root causes, recommend actions, instead of relying on our engineers to build that logic manually.

I think it would also be helpful if they can come up with some kind of advanced analytics which requires less configuration or if there is any more ready-to-use templates, for equipment like BESS, battery energy storage. I think those are the areas where they can improve. There is a reason being, because there are a lot of battery analytics companies like ACCURE, TWAICE, and they are good companies.

Seeq can easily do that internally as well if they can start working on these capabilities. Then you will not need these third-party analytics companies because that is expensive, too. That is the area where they should focus on, especially in this atmosphere where we are having so much craze about data centers and battery energy storage projects. I think that would be a win-win for them in terms of expanding their business, too.

---

**Client** [00:10:25]
That makes sense. Just to clarify your point on needing third-party analytics companies, how often are you bringing in third-party analytics resources to help build something out on the Seeq platform?

**Expert** [00:10:38]
We are actively working with them on five of my projects. There is a company called ACCURE. I have been working with them on five of my different projects, since last two years now. We are paying them. We are on a subscription-based model with them.

I have not been very satisfied with them because most of the things which they have been telling us, our sites already know it. Things like augmentation, degradation. They are telling us the things which we already know, maybe in a more refined way. The amount of money which we have been paying them, I do not think that is justified. Maybe we are going to use them for another five or six months. Once we are done with our contract, I think we would stop using them. That is my perspective on them.

---

**Client** [00:11:23]
Got it. When you think about the Seeq support team that sometimes will help you develop, as well versus the third party resources, what is the main difference? I know you mentioned more advanced analytics. In what situation would you have to bring in the third party versus something that maybe Seeq could help you with? Is it just more industry specific use cases or something like that?

**Expert** [00:11:46]
Yeah. I think the biggest difference is that if you look at the Seeq team, they know the platform extremely well. They have been helping us to build those analytics very efficiently, and they are recommending the best way so that we can use their software.

Now, a third party, they can bring much more deeper expertise on the battery side because they understand battery degradation, they understand cell behavior, they understand failure modes.

With the help of Seeq, you are basically getting most out of their platform. Your battery analytics would only tell you a specialized engineering knowledge. They would only tell you about predictive models for the assets themselves. Then, the other thing which I do not get it is these battery analytics company, they rely on data.

The reason why they say 100%, they claim that they can come up with degradation trend, they can come up with the exact date for augmentation, is because they have a lot of data from these different utility companies, different developers. Then, the question is, how accurate that data is? You can rely on them to some extent, but again, 100%, no.

It is better that you build up your own data library, which is what we are trying to do with Seeq. We are collecting all of their data. We are trying to create our own trend analysis, especially on different battery chemistries. Then, we are going to use it, for our own way. That way you do not need a third party who always has 100% access to your data, which is also not a good thing from a cybersecurity standpoint. That's the biggest reason which I can think of right now.

---

**Client** [00:13:26]
No, that makes perfect sense. It'd be helpful to hear a little bit about how these systems interact and maybe, when you were purchasing Seeq, if relevant, how you thought about it specifically around why, you mentioned obviously, you're building on top of your Historian and you have these other analytics platforms. Is there anything where you are choosing to use a different provider for something that Seeq offers? Does Seeq offer any capabilities that a Historian would offer, or anything like that?

Firstly, we think Seeq as an analytics layer. There's a reason because it connects our existing data sources, like Historians, SCADA systems, and that is where all of our operational data resides.

If we use a specialized battery analytics platform, it can either consume the same data directly from the Historian or using Seeq through data connectors or APIs. Seeq is not going to replace those domain-specific platforms, in my view.

It's just complementing them by giving our engineers that good and user-friendly interface to analyze and visualize that data. I think the biggest advantage with Seeq is flexibility, and that is why we went with them.

There's a reason any engineer, any starting engineer, graduate-level engineer, can open up Seeq and easily create their own analysis and compare historical events. I do not know if you have seen, if you have heard it on Seeq, but you can easily click on different projects. You can easily compare historical events. You can trend any signal, without waiting for an OEM to build that feature for you.

I think that flexibility is one of Seeq's biggest strengths, because right now, if I am running a battery energy storage project, and if you ask me, "Can you tell me what's going on in BESS container number 16?" Seeq shows all of that, so all you have to do is click on the project, MS5, click on it, BESS container 16, click on SOC. It will show you everything. It is very simple. It has a very user-friendly interface.

Got it. Just for a quick data point or two, helpful for us, how likely would you be to recommend Seeq for this specific process analytics platform on a scale of 1-10?

**Expert** [00:15:45]
I would recommend nine, to be honest with you. That's because it's a very capable platform, like I've been trying to explain.

---

**Client** [00:15:54]
Then the other data point here is an ROI. How would you rate the ROI of this product on a scale of 1-10? Either, if you can measure that in actual dollars or time saved, or just qualitatively, the efficiency you've gained for-

**Expert** [00:16:11]
I would rate them maybe 8.5. Again, because your biggest return comes from reducing that engineering time spent on troubleshooting and investigating events. Right now, with the help of Seeq, like I was trying to explain you, our engineers, they can analyze the historical data very much faster than they were doing before, identifying root causes.

The biggest part of it is manually pulling data from multiple systems. That's what I was trying to explain to you. Seeq gathers all of our data from SCADA and PI. For me, it takes me about 10 minutes to get into the SCADA system because I have my normal laptop. I have to connect it to a remote desktop, and it's really a pain. That's one thing.

The other thing is it also helps to improve your asset reliability because now you can support your operational decisions based on the data which you are seeing. The reason why I didn't give it a 10, because your overall value is still dependent on the user.

I think Seeq needs more built-in AI automation and some analytic capabilities, which I was talking about before. The day they have it, I think that's going to increase their overall ROI, in a significant value.

---

**Client** [00:17:29]
Got it. That's super helpful. Moving on slightly, it'd be helpful to hear about, given that I think you mentioned you were involved in the decision to purchase Seeq three years ago?

**Expert** [00:17:41]
Yep.

---

**Client** [00:17:43]
Can you talk a little bit about that process and how you chose Seeq and what other alternatives you looked at?

**Expert** [00:17:49]
One of the things with these platform is to ask them. What I do is I typically ask them how easy it's to integrate your platform with our existing SCADA and workflows.

Typically, the way it started three years ago, when I first moved on the BESS side, we need to identify a business need that we are trying to solve, then we would define the requirements. We saw I think a couple of vendors through product demonstrations. We had technical discussions.

During that RFP process, that evaluation process, we have to look at the integration part, that's one. Ease of use, what cybersecurity they have, what support they are going to provide us, then the overall cost. Obviously, it's a collective decision. I would say 80% of the say comes from engineering. Operations procurement, they are involved too, then we provide our technical recommendation based on the evaluation. That's how it all started.

When we first acquired Con Edison, we acquired Con Edison almost four years ago. Then we got a lot of solar and BESS assets as a part of that acquisition. Then we are actually looking for some kind of a platform which would help us to combine all of that data into one system. That is how we came across Seeq at that time.

I know we did speak to a couple of other people as well. We are using them. For instance, PI Vision. We also use PI Vision and PI System in our company, because we did evaluate them. I normally do not go into PI, if you have to ask me, honestly, because I am getting everything in Seeq. We have PI System too, by AVEVA. We are using them since last four years now.

Then we also talked to, there is this company called Cognite Data Fusion. I think their platform is more of an industrial data platform, but they have some good analytic capabilities. We did not go with them because we still think that we are learning about AI, and we did not want to start using AI capabilities 100% on day one.

We are taking it slow right now. Which is why one of my point, which I mentioned about Seeq is the day they have those AI capabilities within their platform, that would increase their ROI in the greatest way possible. That is how I look at it right now. We are using PI System too, just for your information, the PI Vision system, PI Vision, PI System.

---

**Client** [00:20:17]
Is it even your current main Historian platform? Is PI Vision also the Historian platform of either, or is that specifically the analytics on top of it?

**Expert** [00:20:27]
It is actually for analytics. Your PI Vision is basically the visualization layer for the PI System Historian. The Historian basically helps you collect the data from SCADA, from sensors, and then your PI Vision basically is giving that print to the user, different dashboards.

Seeq sits on top of Historian, so that Seeq can access to that historical data. The way it starts is, if I could give you a good architecture, so from the field devices to SCADA, then it goes towards your PI Historian, which stores the data, then to PI Vision, and then you have Seeq at the bottom, because all of that data is flowing from SCADA to PI Historian, to PI Vision, and then through Seeq, which is why I only look at Seeq. I do not have to go inside PI Historian. I can still do it, but I do not do it.

---

**Client** [00:21:20]
Got it. You had it as an option, but it just was not enough for the specific analytics and use cases you want.

Got it. Then, I forgot to ask this earlier when you were talking about deployment and support and things like that, but my understanding of Seeq platform is, again, you mentioned you have a lot of different projects going on and where you're developing calculations for specific use cases.

About how long does it take on average? I know it could depend and you can push back on me, but is there an average time for how long it takes to deploy a specific use case or for a specific project to be initiated and then built on Seeq and then deployed?

It depends on the complexity of the use case. On an average, I would say three to four weeks. That would include understanding the problem, building the analytics, and validating the results with the engineers, finally rolling it out to the users.

The actual configuration in Seeq, I would say it's actually the easiest part. Most of the time, I would say, goes in making sure that the logic is correct and it's providing value. I would say anywhere between three to four weeks to be realistic, but it can be achievable in three weeks.

Got it. Then, what about the initial implementation of the Seeq platform? Once you decided on it, how long did it take to really be able to start using it for active projects and start solving problems?

**Expert** [00:22:49]
We started off with two or three different projects. It can take anywhere between two to three months, and that typically includes setting up the connections to the Historian. You have to configure user access, validating all the data quality, whether or not you are getting good data or bad data, training the users.

When that foundation is in place, you get new analytics I think that can be added very quickly. You do not have to spend a lot of time installing Seeq because it happens within minutes. I think the time it takes is to integrate those existing data sources. You have to validate tags, data quality. That is the most time-consuming process in my opinion.

I think after the first few weeks, when your initial use cases go live, you would see that value coming in. I can tell you from my case, it took me almost three or four days to get used to it because it is very simple to use.

---

**Client** [00:23:44]
Got it. That is really interesting to hear. That is quicker than I actually thought, so I appreciate that. I know I am jumping back a little bit, but, I was also a little bit curious on pricing. In terms of the cost in your initial evaluation, how did they compare to alternatives you looked at in terms of cost? How are they priced? Is it user license-based? Is there any usage-based pricing, besides the support?

**Expert** [00:24:15]
I believe we are on a subscription-based. We are a subscription-based service with them right now. They were very competitively priced, if I can tell you that, compared to some of the other platforms which we looked at. They were not the cheapest, that I can tell you.

Because they offer a good value and that ease of use of analytics and their capabilities, I think that is what really attracted to us. Your pricing, in my opinion, is based on the licensing and then also the number of users right now. It also depends on the deployment model. What kind of support services you want from them. That can differ a lot, to be honest.

---

**Client** [00:24:53]
Got it. That is helpful. Thank you. Then I know we are around time. I have one last question, which is just trying to get a sense of the evaluation cycle for these types of products.

How likely is it that you would seriously evaluate switching and/or using a different solution in the near term and moving away from Seeq?

**Expert** [00:25:14]
I think it is very unlikely right now because we are getting used to Seeq more and more. Probably, I would say there is a very low likelihood about that. The thing is, once you like any kind of analytic platform and that is integrated into your workflow, like deeply integrated into your workflow, your users are in, there is a significant switching cost which you have to take care of.

I think we would only consider switching if there is any other platform which can offer a meaningful improvement in terms of capabilities, AI functionality integration, maybe substantially cheaper than what we are paying for Seeq right now. Again, to answer your question, we do not formally reevaluate every year. Like I said, there is a competing product which can offer a lot more than what Seeq is offering.

---

**Client** [00:25:59]
That makes perfect sense. All right. I really appreciate you answering my questions, especially the rapid fire at the end. This was super helpful, and thank you for all the detail.
