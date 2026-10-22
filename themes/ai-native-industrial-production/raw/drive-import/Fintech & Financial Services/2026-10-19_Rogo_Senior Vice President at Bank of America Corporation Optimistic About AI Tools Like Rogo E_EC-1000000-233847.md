---
theme: "Fintech & Financial Services"
title: "Senior Vice President at Bank of America Corporation Optimistic About AI Tools Like Rogo Enhancing Investment Banking Operations"
doc_id: EC-1000000-233847
source_line: "Rogo · Expert Call · Customer · 19 Oct 26"
date: 2026-10-19
company: "Rogo"
pages: 2 of 2
saved: 2026-10-21T16:32:56.476Z
url: https://research.alpha-sense.com/search?search_id=tmp-l5q00vjpbwvf9aw6o2hl&sort=DATE&order=DESC&docid=EC-1000000-233847
---
# Senior Vice President at Bank of America Corporation Optimistic About AI Tools Like Rogo Enhancing Investment Banking Operations

Company Deep-Dive

DATE PUBLISHED

19 Oct 2026

INTERVIEW DATE

21 Jul 2026

EXPERT PERSPECTIVE

Customer

ANALYST PERSPECTIVE

Business-Led

PRIMARY COMPANY

Rogo

SMART SUMMARY

Summary

The interview covers the integration and use of LLMs and AI tools, particularly Rogo, within a large financial institution's B2B operations. Discussion centers on tool selection, data integration, compliance, and the practical impact of AI on investment banking workflows.

EXPERT BACKGROUND

- Senior executive with extensive experience in digital strategy and transformation, supporting B2B lines of business across small business to large corporate clients, with a focus on sales tools, internal-facing applications, and AI integration for financial services.

EXPERT SENTIMENT

- Optimistic about the value and adoption of specialized AI tools like Rogo for investment banking, especially for senior bankers.
- Cautious regarding data integration and compliance, emphasizing the need for strong controls and risk management before fully leveraging AI capabilities.
- Pragmatic about the future, noting that while Rogo is currently valuable, the landscape could shift quickly with new competitors or pricing models.

TAKEAWAYS

- The organization has integrated multiple LLMs (ChatGPT, Llama, Copilot, Claude Opus) into sales and internal tools, with flexibility for users to choose based on familiarity and use case.
- Rogo was selected over Hebbia and Model ML for its superior ability to 'speak investment banking' and support senior bankers with research and document automation; it is now in production with nearly 5,000 users.
- Data integration with Rogo is ongoing, with current use limited to external data and plans to securely integrate internal proprietary data, subject to compliance and security requirements.
- Security and compliance are paramount, with a focus on zero-copy environments, encryption, and careful contract review with data providers to ensure proper use of proprietary and third-party data.
- The biggest adoption driver for Rogo has been its ability to automate document population and daily briefings, reducing manual work for bankers, while the main frustration is the slow pace of internal data integration due to compliance hurdles.

AlphaSense Smart Summaries are AI Generated

Introduction and Expert Background

LLM Integration and Usage

Rogo Implementation and Features

Data Security and Integration Challenges

Future Developments and Recommendations

EXPERT BIO

Senior Vice President, Senior Digital Director at Bank of America. Reporting to executive leadership, the expert is responsible for leading large-scale digital transformation programs, driving AI adoption, managing enterprise-wide CRM and AI platform deployments, integrating Salesforce Financial Services Cloud, Microsoft Co-Pilot Chat, and other AI tools across multiple lines of business, overseeing global teams including process owners, developers, testers, and training/adoption leads, directing chatbot and digital assistant initiatives such as BankerAssist utilizing Erica technology, leading system integrations with nCino, PrecisionLender, LinkPoint, RelPro, Salesforce Marketing Cloud, CRMA, and bespoke internal applications, designing and executing strategic roadmaps for digital and AI initiatives, and aligning technology with business objectives.

The expert can speak to AI adoption and integration challenges, enterprise-scale platform usage, strategic roadmaps for digital transformation, operationalizing AI within large banking environments, vendor and stakeholder management, and competitive implications of generative AI and platform convergence. The expert has over 20 years of experience at the company, including multiple leadership roles in digital strategy, CRM transformation, and AI implementation. The expert is also a customer of Rogo.

View More

INTERVIEW TRANSCRIPT

**Client** [00:00:00]
Hi. Thanks for taking the time to talk with me. I am interested in learning more about your experience around Claude and integrating to data providers through MCP.

**Expert** [00:00:11]
Sure. Some of my background, I work within digital strategy and transformation, so I support the B2B lines of business. This is everything from small business-sized clients up through corporate and large clients like that and everything in between. I also help support the different product partners that engage with those lines of business, so credit, treasury, leasing, merchant, investment banking.

I primarily support the sales tools and the internal-facing tools for those B2B lines of business, so whatever tools they would happen to use to help with their prospecting or deepening client relationships, things like that. That includes traditional applications like a Salesforce, for example, but then also different ways that AI has been incorporated into the day-to-day work streams, whether augmenting those traditional applications or apart from those applications too. That's a very quick high level what it is that I do.

---

**Client** [00:01:08]
Great. I said Claude. I actually meant to say and other LLMs. Can you help me understand a little bit about which LLMs you've integrated with these sales tools and other outside products?

**Expert** [00:01:24]
Sure. Primarily, ChatGPT and Llama are the ones that have been more or less directly integrated. Obviously, we're not putting ChatGPT within a Salesforce instance, for example. Things like Salesforce, they have their own internal AI tool, Agentforce which runs off of ChatGPT. We have internally built LLMs and AI agents that use either ChatGPT or Llama, depending on the use case, and then having those talk to each other as well. We do Copilot. We have different Copilot integrations and Copilot, whether it's Chat or 365 or even Copilot Studio, having some of those one-off agents. We're starting to bridge the gap in between some of those different agents as well.

---

**Client** [00:02:14]
That's great. When we think about the LLM side of things, are these tools being derived just as a corporate standard, meaning you have your choice between ChatGPT, Llama, Copilot, or are you picking the tool based upon the project or the business outcome that you're after?

**Expert** [00:02:32]
It's a bit of both. I think that a lot of times, we try to pick which ones that we want. A lot of times, we leave it up to the users, or some different working groups are more familiar with others. We have Microsoft Copilot built out for our just day-to-day lives. It's in Teams. It's within Microsoft 365.

From there, you can either use the default LLM, but then you can also select Claude Opus or GPT or whatever you want to use. Sometimes, people, it's like what are they more familiar with? What have they been using more consistently? When we build out some of these tools, we're looking to see what makes sense for the application and what would give us the best leg up to start from there.

---

**Client** [00:03:19]
Okay. I was going to ask you two questions probably at the same time. Let me ask them one at a time. When you look at integrations between these LLMs, and I'm just going to call them external tools, external data providers, however you want to reference it, is MCP the way that you've always integrated these, or have there been other ways that you've integrated to these other outside tools?

**Expert** [00:03:45]
I wouldn't say always. I think MCP has become much more, I would even say required at this point because there's so many different LLMs and agents out there. We've had different ones using Llama going back to the beginning of last year. When things were onesie-twosies, we didn't really have the need for things like MCP and managing all the different agents.

Now, as different work streams are building their own agents, I wouldn't say in a vacuum, but initially from a proof of concept perspective, they are. As we go from a proof of concept to a pilot to an actual production implementation, whatever they're building it on, we end up having to use MCP to layer on top of all the agents to be the air traffic controller between all the different agents.

---

**Client** [00:04:33]
Okay. One of the questions that came up in the original screening was around your engagement with these tools. You had mentioned that Rogo was one of the products that you're integrating with. Tell me a little bit about what you're doing there.

**Expert** [00:04:49]
Sure. Rogo is a vendor. To back up to about Q3 of last year, as generative AI started to get more commonplace in our day-to-day lives, a lot of financial institutions are heavily invested in the Microsoft suite of applications, and Microsoft Copilot is pretty good at doing generic generative AI actions. "Make this sound better. Do this, that." We're all familiar with that, like how we use ChatGPT and other things outside of work. When it came to really engaging with Copilot and trying to do advanced financial analysis or dig in, speak to it in a way that makes it more financial institution-leaning, especially investment banking, it was lacking.

There were different tools out there, like Hebbia, Model ML, and Rogo, which were the three that we looked at independently from each other to say, what's a tool that we could use? After a couple proofs of concept in a pilot program using all three, we went with Rogo because the primary use case was a ChatGPT-esque experience that spoke investment banking language.

The investment bankers like to dig into numbers and get into the nitty-gritty, and that did that the best. They weren't necessarily looking for things that ran the analysis. The juniors, junior bankers were mostly doing this. This was more for the senior bankers, the directors, and MDs to ideate and bounce ideas and get more information from Rogo initially. We started and we rolled that out to the investment banking line of business.

Another way that it's been helpful is we have our different templates, whether it's earning statements, whether it's pitch decks, whatever it may be that we want the information to be put into. Previously, the juniors would research the information and copy and paste it into different things and put those decks together. Rogo has been able to do a lot of that for us, so an easy use case. This isn't where the research stops. What are some sell-side comps or NII or looking at things for different investments across the portfolio? It will understand that better and give more detailed analysis than a Microsoft Copilot.

---

**Client** [00:07:04]
I see. Do you do this analysis? I think you even referenced it like a ChatGPT experience? Is it done within the Rogo product itself, or are you integrating an LLM into Rogo for this?

**Expert** [00:07:21]
Primary use case right now is using the Rogo interface, so going out to the Rogo interface and interacting with it that way, and then also putting different amounts of our documentation on a Rogo in there. We are in the process of integrating some of our information into the Rogo externally. Rogo can give you that high-level analysis and earnings and whatever it may be, but it doesn't have any of our proprietary information, like who covers the client, previous deals, conversations, that kind of stuff.

We're working to get that information over to Rogo, so it can be part of the analysis. That's like the in-out. We're also doing some of the out-in as well, how do we get some of the more specific, detailed analysis, the narratives, charts, those types of things into whether it's Agentforce because you're doing some sort of sale-type work or something else, maybe even native Copilot. We're doing both now, and they're both starting to be kicked off in that way.

---

**Client** [00:08:21]
I see. How do you bring your data into Rogo? Is that an integration through an MCP? Do you upload physical files, or does Rogo point at your, it sounds like a Microsoft shop like OneDrive or SharePoint or something like that or all of the above?

**Expert** [00:08:40]
I would say all of the above in different places. I think initially, it is probably just sending a file. We send them a few files, so they can see how our data's structured, what it means, and how they can match it up with their data and don't match it up with their data. That way, they can know what to expect.

Eventually, to your point, a more of a batch and automated process, whether it's a OneDrive, whether it is literal SFTP type of file transfer protocol. Eventually using MCP so that you have a real-time call into our system from their system, so that there's an automatic pull of that information. We're not there quite yet, but that is the ultimate end state that we're angling for. Not that it can't be done necessarily yet, but there's a lot of different legal risk, compliance, information security type of aspects that we need to make sure we tick and tie before we just start sending our information all over the place.

---

**Client** [00:09:40]
Actually, that's a really good point. I was actually going to ask about compliance and things like that. In this type of scenario, is your data living or existing still in your environment, or does your data get copied into Rogo's environment? How does that work?

**Expert** [00:10:00]
It lives and stays in our environment. Whenever we do any sort of work with regards to these external vendors, we make sure that there's zero copy and they're not training their models on the data. Whether that's a private version of a public cloud and however they are housing the data, not that they would necessarily sell the data to any competitor, but just the fact that training their models on our information would inadvertently benefit other financial institutions.

We're making sure that as they use our data, they're using it only within the confines of helping us and not necessarily helping themselves. Now, I'm sure they're helping themselves as they learn how to execute at scale and how do they operate with other financial institutions doing the same thing necessarily, but not because of the data. The data is just the fuel to the engine, and we're helping them build their engine.

---

**Client** [00:10:56]
Your data is your data. From a secure perspective, do they have private keys that allow access into things, or have you gotten that far?

**Expert** [00:11:06]
It's like bring your own key. We go through encryption at rest and encryption in transit and all that type of fun stuff. That's how they tend to do it. That way, we hold the keys. It's really the best way to do it, to say it is. That way, we control our data, whether it's here or there. If it's a proof of concept, it's a one-time data send with maybe an update. As the actual implementation is rolled out, how do we make sure that we have a zero-copy environment?

---

**Client** [00:11:40]
I see. Outside of the key piece of it, how is the data isolated? Do you have an isolated tenant, or is it something that is shared with other tenants and the key is the key to encryption? How does that work?

**Expert** [00:11:56]
I'm not sure with Rogo, to be quite honest with you. Sometimes it is single-tenant, but sometimes it is multi-tenant environments because, to your point, the key is the key. Sometimes, it depends on the data itself. While theoretically any vendor could do either single or multi, they're probably going to want multi, so they can save money. I think part of it depends on what data we are sending them and how comfortable we are with saying, "Oh, it's a multi-tenant environment," to our compliance partners or any outside regulators that may come in. It could be that the security and the confidentiality of the information is we have to have a single-tenant environment just to have the comfort level with our internal regulators.

---

**Client** [00:12:42]
Was there any difference? You mentioned Hebbia, Model ML. Was there any differences in terms of the security components of Rogo compared to those, or were they all fairly comparable when it came to ingesting data?

**Expert** [00:12:55]
They were all fairly comparable. I think it was just really the primary focus and use of each one. A lot of what Hebbia is mainly used for is more of a deep diving into the information, really digging into the information. We have FactSet, and FactSet has their own AI plugin too. Rogo was more of a senior banker research tool, where Hebbia is more of a junior banker. Not that senior bankers don't do research and dive in. They could but more likely to be used by junior bankers. If we were going to equip somebody with a tool first, it'd be the senior bankers with Rogo.

The Model ML, just the name too, Model ML, it's more of a model of a workflow. Since this was primarily investment banking that was taking lead on this, it bled into corporate banking and commercial banking, and maybe they'll have more of a use for Model ML. Model ML is better at workflow automation, process flow-type things. The fact is in the investment banking, it's all sector-based. You could have global industrials run things a totally separate way than consumer and retail. You could go sector by sector, and they all have their own process and ways they do things. They're on this site, and they're going there for this thing. It's not disorganized, but it's just overly complex.

If you're going to roll out simpler process automation, it's a lot easier to look at the bottom, to look at consumer or small business and implementing at scale when it comes to things like AI. I think that's primarily. Security was mainly the same between all of them. We didn't really need to get too deep into it. It was more the specific use case that was driving force behind going with Rogo.

---

**Client** [00:14:48]
Got you. You mentioned FactSet just now. Does Rogo leverage your FactSet subscription or licensing that you already have? Does it come with its own content? How does that part of it work?

**Expert** [00:15:03]
That's a good question. It doesn't look like it includes the FactSet in it. Now, because we have an enterprise license for a particular vendor, we can effectively turn that on within a Rogo. A lot of what we're finding when it comes to, not necessarily or specifically FactSet and Rogo but every third party that has data, we're having to reassess the contracts to see how they're written, to see whether or not they include the use of taking that data and putting it in AI, not necessarily training AI on their data which is obviously going to be even more difficult to get approval to do, but even just incorporating their data into AI.

Whether it's IBISWorld or BoardEx or Vertical IQ or all these different similar data providers out there that have their own proprietary data, we can't just take their, "Oh, we have a license to use IBISWorld. Let's just throw all their information into these AI summaries." If the contract says you can do it, great. If not, then we have to go back to talk to the contracts. Same thing with this. It looks like things like CapIQ, PitchBook, Crunchbase, those things are included as part of the Rogo, but others are not just by default. That's where the whole agent-to-agent really comes into the play.

---

**Client** [00:16:25]
There's a handful of data providers that come with Rogo, but depending on your licensing with other data providers, you may or may not be able to use those also in addition to what comes out of the box with Rogo. Is that a fair replay?

**Expert** [00:16:39]
They're not all equal to one another. Dealogic's something that some of our corporate and investment banking clients or bankers are more interested in, and Vertical IQ is where the smaller, private business banking-sized clients are more interested in too. Sometimes the juice isn't worth the squeeze. It really depends on what the interest is at that point in time for our specific line of business. Each one of these is going to cost a decent bit of money.

As we go through, we can't tackle everything at one time. What's their number one priority, number two, number three? That's how we tackle it and see if we can get overlap between lines of business like how IBISWorld is, for industry information, pretty standard. I wouldn't say amazing, but non-offensive. It's just a good baseline. That's a good example of how maybe we just go with them even if they're not the best. They're just good enough.

---

**Client** [00:17:37]
I got you. You may have said this, and if you did, I apologize for asking this again. What are some examples of the internal content that you are looking to have Rogo ingest or Rogo to be able to use as a data source?

**Expert** [00:17:50]
Whenever you're asking for what are some comps to this client, analysis for that client, this client, if you're outside, you know you're asking, I'll just use AI giants, how is Anthropic doing versus another client, or what's Meta versus Google? You're just looking at it from a third-person perspective.

The information that we're looking to add to it is what's our relationship with these clients or relationship with clients in a similar industry or region maybe. What's the relationship as in who is covering that client and maybe what people are involved. If you're like, "Oh, what's going on with Meta, or what's going on with Home Depot?" it's like, "Oh, Home Depot, from an industry external perspective, this is how they're doing on the market. This is some latest news." That's Rogo-esque information.

Our information is, "This is who covers the client. So-and-so is the corporate banker. So-and-so is the investment banker." The calls, "This is the last time the client was called on. This is how often they've been called on." It shows not just what's happening with the client externally, but also what we're doing or not doing with that client.

If there's any open deals in the pipeline, Dealogic will tell you, "This is what we've closed on. This is what you're collecting fees on maybe externally, but then this is what you're working on. You're working on an FX and card. There's also this advisory deal going through. So-and-so is getting a bridge loan," that type of information that we have in our systems that Rogo would not have and would never have because it's our information.

---

**Client** [00:19:30]
It's your data. You mentioned Salesforce earlier in our conversation. Is some of that data coming from Salesforce records that you're storing some of this customer data at, or is it going across multiple sources and trying to bring that all together?

**Expert** [00:19:47]
It is primarily in a Salesforce instance or a couple instances of Salesforce. Some of that data is in data warehouses. If it's a credit, there's different credit and underwriting tools. There's different pricing tools. While some of that may not necessarily be in a particular Salesforce instance, there's ways to get to that data and put them in a Hadoop or whatever data lake of some sort that we can build into an orchestral type of layer that orchestrates the information between the different systems.

Primarily like a sales tool. It's because that's mainly what I deal with, but there's other instances across the bank too when it comes to these types of things where it's more of if you're trying to get information to a Rogo, for example, instead of having seven or eight different data repositories be sent to Rogo, how do you centralize that into a data lake that can then be integrated into a Rogo?

---

**Client** [00:20:43]
Very interesting. I know we went deep on the Rogo and everything else, but again, your insight was actually related to some other questions I was going to get further on. That's why I went there. Help me understand a little bit about going back to your LLM use. In a perfect world, you mentioned and you delineated between junior type of analysts, junior users, and then the senior users.

Is there a feeling one way or another where people want to work? Do people want to work in the native tool? Going back to our conversation about Rogo, you mentioned they're going there. In a perfect world, would they want to be there, or would they want to just be living in Copilot or ChatGPT or whatever tool they're spending all their time in their LLMs?

**Expert** [00:21:35]
What we've been doing is we've been trying to bring AI to where the users are working most of their day, wherever that may be. In general, our users are using a handful of applications on a more regular basis, and we just find it out from just seeing how they do it. A lot of times, our relationship managers and bankers are spending a lot of time in a Salesforce instance, for example. We would not necessarily tell them or ideally go to a Rogo to ask for that information or to go to whatever to ask that information.

If they're in their sales tools looking at sales information, they should be able to go into Agentforce and ask that information, and then you have behind the scenes, whether it is internal agents pulling that information and pushing certain things to the user and/or going to external vendors. That's not quite where we are just yet, just because we're getting to that point with Agentforce. Also, what you mentioned too, whether we like it or not, a lot of our bankers spend a ton of their time, some of the majority of their time, in their Outlook. Microsoft Copilot is in Outlook, whether we like it or not. Copilot is fine, but how do you get that information into a Copilot?

If you're thinking from a sales tools perspective, I'm going into a sales tool like a Salesforce and looking stuff up and logging calls or something like that. The ideal end state is I have a calendar, and my calendar is in Outlook. My calendar tells me who I'm meeting with, and they see when I'm meeting with those people. It says, "These are the people you're meeting with next week. This is the company. This is information about the company."

You're just in your Outlook. You can self-serve through Outlook that information. That could be Salesforce information, Rogo information, and elsewhere. That's the ideal end state. We're not quite there yet, but just meeting the users where they are on their day to day, instead of having them change their day to day to go to a different tool.

---

**Client** [00:23:39]
Makes sense. It's a common theme we hear when we talk to other experts like yourself. Also, at the same time, a lot of varying tools that you have to deal with because, to your point, there's the Copilot stuff that's embedded in Outlook and all that. There is just going to straight ChatGPT or if you're a Claude shop, using Claude or whatever.

Going back to the Rogo piece just because, again, my main focus of the discussion really is around financial data providers and data tools and how they integrate with LLM. That was the basis of this conversation. I'd like to understand a little bit. I know that it still sounds like things are a work in progress when it comes to bringing in your internal content, internal data, so that it can be integrated into the tool. Are you still in the testing and development phase, or is Rogo being used in production today just without the internal content?

**Expert** [00:24:39]
Yeah. It's being used in production today without the internal content piece.

---

**Client** [00:24:45]
Got you. How long has that been in place in production?

**Expert** [00:24:51]
It was technically in production very end of last year, November, December, but for a small pilot group of users, I don't know, depends on if it's a press release. Technically, it was in production end of last year. It did not have a true full-scale rollout until about March of this year. It started with a handful of bankers, went to maybe a sector or two, and then it was a full scale, "Hey, everybody. Get on this." Now, it's been a success story to the extent at which they're expanding it even more to even more people. It's been a while. It's actually been out there a while. That's the timeline for you.

---

**Client** [00:25:31]
How many users do you have live using Rogo today?

**Expert** [00:25:35]
I don't have the exact number. I think it's just under 5,000 at this time.

---

**Client** [00:25:40]
Okay. Do you have any insight into when you look at things, what has gone well that you didn't expect? Is there a certain use case that really has driven adoption of the tool?

**Expert** [00:25:53]
I think that the one thing that has initially driven adoption was just how it truly understand and spoke investment banking. It did a really good job of just speaking towards doing better analysis than Copilot. I think what's really is getting your foot in the door. That's all well and good, but that wouldn't really gain a critical mass. You go in there. You play around with it a little bit, and then maybe you forget about it and you don't use it again.

I think one of the key things that has changed the way that users work is the ability to input data into our documents is what I mean. We can give Rogo a pitch book, a this, a that, and it was multiple pages. It could be a Word doc. It could be whatever. This is what we need. This is where the data, and they can put it in their system. There's a library that you can schedule tasks to run daily briefs, daily this, email them to me. How do we get that?

I think it's taking the agentic part. Generative is fine and all well and good, but most of the time when people use generative, it's like, "Make this sound smarter." You're almost using it like a Google, but agentic is where it becomes more useful of instead of me having to fill out that PowerPoint every week or send that thing to this so-and-so group every week. It's not going to do 100%. AI never does 100%. If it gets you 80% there, it takes a three-hour task and makes it a 20-minute task, and I think that's where people have really started to realize the benefit. I'm not dumping on Copilot.

A lot of times, if you're like, "Hey, here's a template. Fill it with this information and that," it comes out and it looks all weird for some reason. It could just be because the way we've implemented it, it is a wide-scale implementation. Hundreds of thousands of people are using it, but it's more of a lowest common denominator approach where there's more guardrails around generation of images. It's turned off to an extent and content generation to be more compliant. It's unfair to compare it, but that's not turned off in Rogo. We can give them a pitch book or whatever, and they can pre-fill it. I think that's really helped.

---

**Client** [00:28:15]
Very cool. What has been some of the biggest disappointments or maybe unresolved frustration with Rogo on the forefront of what you just shared?

**Expert** [00:28:27]
I wouldn't say that it's necessarily the drawback of Rogo. I think it's more of our ability to get our data into their system. It's not their fault. If we say, "Here's all our data, and here's an API. Just go for it," they would do it. I think it's just us getting in our own way.

Things with AI are moving so quickly, and there's so many different parts of the enterprise looking at so many different things and ways to implement AI. We have to have proper controls and review boards to make sure that we're not making a mistake by just rolling out something. No one wants to be the headline such and such bank data did this, and people are denied loans because of AI or something that would be reputational risk. I think part of it is just being careful about reputational risk.

Whenever I've had these conversations before, what's the long-term viability of the tool which might be a question you have soon. It is hard to see Rogo going away anytime soon for at least the next year or two because it has carved out a foothold of it does certain things very well. It's very useful. It isn't the end-all be-all, but it is another tool in the tool belt of especially our investment bankers and how it can help their day-to-day.

It's hard to say what two, three, four+ years from now will be because a year and a half ago, there was very little AI capabilities. It was more of an LLM or NLP type of implementation. There could be a competitor out there, either from a Claude or ChatGPT. They themselves get as good at speaking the language in certain ways.

It could be that not only does Hebbia and Model ML join forces. They buy another couple start-ups. They become not only good at their workflow automation and deep data analysis, but they also start to do more of the generative back and forth better that we have to consider it too. I think contracts are going to end up being important when it comes to vendor selection in the future too.

Right now, things are relatively cheap. I know that sounds silly because if you look at the spend and how much things are costing, it's expensive. Some of the ways that enterprise licenses for AI are shaping up right now, it's almost like a seat license or an enterprise unlimited usage license. They're trying to get you hooked on it.

I know these vendors are going to switch to a much more tokenized model in the years to come. If they're keeping track of the tokens, we need to keep better track of our tokens because it could be use it to your heart's content for the next year or two. They see you're using thousands upon thousands of tokens and go, "Now, we're going to a token model," and you're hooked.

I think that a lot of it is if we're using Rogo like crazy and it's using a ton of tokens then another competitor comes in in a year or two and can do almost as good but it's 1/3 of the price, that's going to have to start to be considered with some of this. I think also Rogo's one of those tools where other competing financial institutions are also using it.

It's not necessarily raising the ceiling on investment banking. It is raising the floor because you'll see it across the industry. Investment banking revenue and generation overall has just increased bank by bank. There's no bank that's doing a bad job at it necessarily. It's just are you doing a good job, or are you doing a great job? I think a lot of it has to do with some of these tools at their disposal now too.

---

**Client** [00:32:09]
You actually hit on something I was going to get to here. You are paying currently per user for Rogo.

**Expert** [00:32:16]
That's correct and same for things like.

---

**Client** [00:32:19]
You're not paying by token.

**Expert** [00:32:22]
It is like an unlimited usage with Agentforce as well where it's use it to your heart's content for two years, and then we assess.

---

**Client** [00:32:31]
Okay. Has Salesforce or Rogo for that matter hinted at the move, or is that just your assumption tokenized solution?

**Expert** [00:32:41]
I would say that they hinted at it with Salesforce. They've hinted at it with the original implementation of Agentforce. Before any contract was finalized, they were looking at different options, and a tokenized model was an option. I know they changed it. Instead of it being token-based, some of the servicing cloud was solution-based, charge you per resolution for that. I think they're looking at more innovative ways instead of just a tit for tat.

There hasn't been any, "We're going to do this in the future." I think they're still trying to figure out themselves probably how useful of a model a tokenized version would be if all of a sudden they start switching, whether it's Salesforce, Rogo, whoever. When it comes to large companies, it's very easy right now. It's been easy forever to come up with your budgets year over year on a per person, per license, per seat, whatever, usage. You have X number of users. You plan to increase headcount 4%, decrease headcount 6%. If each one of those users uses FactSet, meaning FactSet or Bloomberg Terminals or whatever, costs this much per person per year, it's easy to do the budgets.

I don't think that companies really understand their token usage enough to comfortably switch to a tokenized model because they're still trying to figure out how useful AI is for each user, what type of AI, how much they're using it on their day-to-day. They're probably going to start to do analysis on that in the next year to say, "If we were to switch to a purely tokenized model, it's going to cost us $100 million a year more."

If you look at the $100 million a year, $70 million is based because of this thing, or $40 million because of this thing, things like that where maybe we definitely should not do tokenized tier or change our token usage. I think that's what's going to have to happen, is understanding the budget impact to switching the model of funding.

---

**Client** [00:34:43]
Just one or two more questions, and then we'll let you get back to your day. I know we have been having two parallel conversations. We've been talking about LLMs, and then obviously we've been going deep on Rogo especially. Let's look at the Rogo side of things again just because I've been researching financial data providers and tools like that.

If you were advising someone who was going to start even looking at these tools today, obviously just our conversation around price might be part of your answer, so I'm not going to lead the witness here. If you were advising someone looking at just implementing one of these tools today, what would you tell them. What would you do differently that you would advise them to do?

**Expert** [00:35:29]
For me, I would not necessarily tool. I would start with the individual person and what they're trying to solve. If I'm supporting consumer, if I'm supporting small business or corporate banking or whatever it may be, I would try to first understand what it is they do on a day-to-day and how much time they're spending doing those things and what's the critical mass for some of the stuff.

If you're a commercial banker, what are you doing on your day, and how much time are you doing? If you have eight hours in a day and you're spending three hours a day prospecting, that's the majority of your time. What are you doing with that time, and how are you prospecting? Just trying to understand where they're spending a lot of their time before trying to look at a specific tool. Once I figure out how they're using their time on a daily basis, I would then start to research what tools would help them with that work. If they are spending a ton of time researching, how are they researching? I'll just keep going down the path.

More than likely, they have a bunch of different websites and bookmarks. They're going to this website. They are going to that website. They're just going to all these random websites and searching and searching. How do we bring that information to them, so they don't have to go to it? Can we centralize some of it? Are there tools that centralize it? How do we bring it to the user?

I would start to see because that's how you're going to get usage. Instead of finding a niche tool or a specific use case that's like, "Oh, that's cool." Then it takes a one-hour task and makes it a 15-minute task, but if you only do that one-hour task once a week, it's not really super useful. It's useful, but it's not really going to move the ticker. That's how I would start to look at which tool and which segment of the population you're looking at.

---

**Client** [00:37:29]
That's really helpful. One last question for you. You may have shared feedback directly with Rogo, but what's on your wish list? What are they not doing yet, or what would you like to see that you haven't been able to figure out yet with the tool?

**Expert** [00:37:45]
I would say once they start to get our data, how do they proactively serve up information we would not necessarily immediately think to ask about. Once they know what clients we're covering, what clients we're talking to or not talking to or plan to talk to and they see that information, instead of us going into Rogo and saying, "If I'm meeting with ExxonMobil next month, what should I talk about, this, that, and the other, doing it the other way around," Rogo saying, "Hey, you're meeting with ExxonMobil next month. Do you want to set up an alert? I can give you daily updates. Here's some of the things you should know right now. This is what their last quarterly earnings have looked like."

That way, stuff that good bankers would know to do and look for and proactively seek out. How do we get the tool itself to serve it to the user without the user having to ask that question? I'm sure it can get to that point, but until we get them the data, we can't even really ask them to do that yet because they don't have our data to do it.

---

**Client** [00:38:42]
Does Rogo have access to your Teams calendars and team mail and things like that? ?

**Expert** [00:38:48]
Not yet. That would probably be one of those. Once we get Copilot, Copilot to Salesforce, Salesforce to Rogo, and then but those three. You're in your Outlook. It's like, "Hey, you have this coming up. Do you want to do blah, blah, blah?" You click yes. That initiates the token process, and it goes from Outlook to Salesforce, Salesforce to Rogo, Rogo to Salesforce with all the different MCP and translation in between. The user doesn't care about that. The user's like, "Oh, that was cool." They don't realize all these things happening in the background.

---

**Client** [00:39:30]
Thank you for taking the time to speak with me. Have a nice day.
