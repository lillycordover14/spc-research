---
theme: "Enterprise Software & AI"
title: "Chief Technology Officer at Dell Technologies Believes Unified Orchestration Is Key to Overcoming AI Governance Challenges"
doc_id: EC-1000000-233800
source_line: "Runlayer · Expert Call · Customer · 19 Oct 26"
date: 2026-10-19
company: "Runlayer"
pages: 2 of 2
saved: 2026-10-21T16:05:36.103Z
url: https://research.alpha-sense.com/search?search_id=tmp-l5q00vjpbwvf9aw6o2hl&sort=DATE&order=DESC&docid=EC-1000000-233800
---
# Chief Technology Officer at Dell Technologies Believes Unified Orchestration Is Key to Overcoming AI Governance Challenges

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

Runlayer

SMART SUMMARY

Summary

The conversation covered the adoption and governance of AI agents in a large enterprise, including internal development versus third-party solutions, technology stack choices, challenges in orchestration and governance, and the decision-making process for new tools.

EXPERT BACKGROUND

- Chief Technology Officer focused on enterprise AI, cybersecurity, infrastructure, and data platforms, with responsibilities including technology evaluation, architecture, proof of concepts, and integration of emerging technologies for internal and customer-facing solutions at a large, highly regulated global enterprise.

EXPERT SENTIMENT

- The expert believes that while significant progress has been made in adopting and integrating AI agents, there are still major challenges in governance, orchestration, and cross-platform visibility.
- The expert is optimistic about the potential for unified orchestration and policy layers to address fragmentation, but is skeptical that any single vendor can replace all existing best-of-breed solutions in the near term.
- The expert sees market consolidation as likely, with a preference for solutions that sit above existing stacks rather than replacing entrenched systems.

TAKEAWAYS

- AI agent adoption is a mix of buying embedded solutions from platforms (e.g., ServiceNow, Microsoft) and building internal agents for specific use cases, especially in IT, security, and engineering operations.
- Internal agent development is selective, driven by regulatory, data control, and identity requirements, with human approval points and clear objectives for each use case.
- The technology stack is highly layered, using a variety of models (OpenAI, Anthropic, open source), orchestration tools (LangChain, LangGraph, Microsoft Semantic Kernel), identity providers (Okta, Entra), and governance/security tools (Onyx, WitnessAI, Runlayer, HiddenLayer, ProtectAI).
- Major challenges remain in unifying identity, observability, cost tracking, and governance across disparate tools and platforms; no single vendor currently provides a comprehensive solution.
- Decision-making for new tools is cross-functional, involving AI, security, identity, legal/privacy, and finance teams, with a strong emphasis on risk reduction, compliance, and business value.

AlphaSense Smart Summaries are AI Generated

Introduction and Expert Background

AI Agent Adoption at Dell

Productization and Tool Stack Overview

Specific Tools and Their Applications

Decision Making and Cost Observability

EXPERT BIO

Chief Technology Officer – Artificial Intelligence, Cybersecurity & Data at Dell Technologies. The expert has evaluated PointFive, Onyx, and Runlayer. The expert can speak to evaluating PointFive, Onyx Security, and Runlayer, alongside deploying similar AI security and FinOps platforms. They can detail practical use cases in agent governance and cost optimization, deployment limitations, tangible ROI, and the market outlook for these tools.

Field Chief Technology Officer – Artificial Intelligence, Cybersecurity & Data at Dell Technologies. Reporting to the Senior Vice President of Global Architecture, the expert is responsible for defining the strategic technical direction, leading high-impact client engagements, and overseeing the development of enterprise-level architecture frameworks across AI, cybersecurity, and data management portfolios.

Prior to Dell Technologies, the expert was the Enterprise Solutions Architect - Automation at Turbonomic, an IBM company, leaving in 2019. Reporting to the Vice President of Engineering, the expert was responsible for designing and deploying large-scale automated infrastructure solutions, optimizing cloud workloads, and driving technical sales strategy for enterprise clients.

The expert can speak to enterprise AI deployment strategies, data security frameworks, and multi-cloud infrastructure optimization. Additionally, the expert is a customer of and has implemented advanced machine learning operations (MLOps) tools, automated workload management software, and next-generation cybersecurity orchestration platforms.

View More

INTERVIEW TRANSCRIPT

**Client** [00:00:00]
Thank you for speaking with us about enterprise AI utilization. Maybe to kick us off, can you just give me a couple bullets on your background and your responsibilities at Dell? Let's start from here.

**Expert** [00:00:14]
I'm a CTO. I focus on enterprise AI, cybersecurity, infrastructure, data platforms, technology, the governance around it. I think a good way to frame it is that a big part of my role is helping internally, in convoluted ways, but also customers, other organizations, large global Fortune 1000, evaluate different types of emerging technologies, determine how it actually will fit architecturally, and then understand if it's mature enough to go into actual deployment, working across AI infrastructure, AI security, identity, observability, agentic.

That's everything from doing your due diligence on the architecture, the technical evals, RFPs. That's my day-to-day. Actually, I'm looking at my calendar. Proof of concepts and then how to integrate these emerging platforms into organizations that already have enterprise control ecosystems, workflows, all of that. I will stop there. I can talk quick and monologue. Feel free to cut me off at any point.

---

**Client** [00:01:25]
Yeah. I really appreciate that. Maybe to kick us off, where are you in the adoption journey of AI agents at a high level at Dell? Is it that you've been buying applications that have AI agents that they sell, or you have developed internally some AI agents for specific use cases, maybe, or for now, is it more like chat, like GPT-type things that are being used? Tell me a little bit where you are in the adoption journey of agents.

**Expert** [00:01:54]
Yeah. It's a good question. To be quite honest, it's a little bit of all of those pieces that you just brought up. It really is. A lot of organizations describe that. I would say that the chatbots. Sure, we should be past that. It's still being used. If I'm being nice or realistic, we're beyond that. We're not to a point where, no matter what my boss wants, where they want autonomous agents running everything without humans. We're not quite there either. I think there's three ways to look at it. The biggest one is probably going to be the widespread use of your copilots, the GPT style type of knowledge search summarization. Coding assistance is another one, productivity probably the biggest ones right there.

I wish I was in person, I would just put in quotation marks with my fingers, "agentic capabilities" from platforms that we already have. That's Agentforce, that's ServiceNow, now AI Control, whatever it's called, Microsoft, some of the security tooling we've got. Our main go-to-market is building these internal agents for workflows for us internally, but also for our customers. It's good if you can do it to ourselves because we're very legacy and monolithic. We're redefining the data, the permissions, the approvals, and then ideally, we can figure out what that outcome is. The biggest use cases are IT security operations, security investigation.

We have one million engineering type of teams. Each product line has its own engineering support where they can search for documentation, in theory, and try and get the most relevant instead of a bazillion non-indexed SharePoint sites and Jira sites and all that. There's some sales enablement. I'll stop there, and hopefully, that answers your question.

---

**Client** [00:03:53]
Yeah. I am particularly interested, I must say, in the cases where you build your own agents internally, through whatever it is you use, like Qwen, Anthropic, OpenAI. If you do, do you and what are use cases for it? Is it like coding and sales, or do you not use them quite yet? Is it just apps and also agents that are sold through, as you said, Salesforce, ServiceNow, etc., or do you also build agents internally?

**Expert** [00:04:23]
We do. We built quite a bit of reference architecture here in terms of using things like LlamaIndex. That's what works for doing retrieval-augmented generations, and I can go with it. To answer the first part, we do both. We absolutely consume the agents and use them that are embedded into platforms. We will build the actual internal ones where because of how regulated we are, because of the token spend, because of the execution, there are all these different reasons, but we have to have control over the data, the identity on how that data is being used and how we execute it. We are highly regulated by just like the U.S., and that's including GDPR rules and stuff when we build these things out in EMEA.

There are different type of use cases for that. On the internal side, we don't really just start out with, like "Oh, we are going to build something fully autonomous." No, we pick a clear objective with a set of tools, what the data sources are, and then some human approval points. Probably the two biggest ones that are falling in this category are the coding and then our engineering support or IT ops. You can actually throw security ops. For coding, that means that an agent, it reads an issue, searches whatever repositories it can, gives some code recommendation or changes or whatever. It can do a pull request, but we don't let it merge directly to production just yet.

In the IT ops, we have an agent that will classify our ServiceNow tickets, pick a runbook, gather telemetry, and then do some sort of low-risk action for that. The security one is probably like this one as well, where they will help our people internally correlate all these different type of alerts that you get that a lot of times get ignored between all our different tools and try to summarize the incident. There are some levels of recommendation. From us, we separate the model from the agent. The model, it could be anything from Anthropic, OpenAI, and Microsoft. It doesn't matter, or even IBM. Around that, we have orchestration, retrieval, connectors. The identity is very important, the policies, how do you log this stuff.

We have frameworks we use. We are starting to use some MCP connectors, like GitHub is one. It gets into a point of how do we productize this. That's the hard part. We could build demos. Anybody can really do that now. The challenge that we have is figuring out the identity that the agent is using it, what data it can access, what does it have read/write permissions, what tools, how do we log that. We are having a hard time doing that, and it's getting there. We build internally, but I would say it's selective. It's not like I would say everything is built internally. No. You try to find the right architecture built by, depending upon what that use case is.

---

**Client** [00:07:35]
Okay. That's very helpful. I would love to understand a little bit more how you think about productizing, to use your word, this use of agents. As you said, there is the orchestration layer because the agent and the model are two different levels, the identity, what they have access to, the connections, etc. Could we go through this stack of tools that you use for that, what you bought, have you built anything, etc. ?

**Expert** [00:08:05]
Yeah. It's definitely a layered approach. The models, we'll use every single model. That's on planet Earth, at least it feels like. We're trying not to do that. Part of this was that we had a mandate from very up above being like, "We need to become somewhat versions of experts at this." Historically, we've been behind the times. There was an initiative at the very top to say, "Look, we need to play and test with everything." That's your OpenAI. That's the model layer, Anthropic, your Azure OpenAI. It could be watsonx.ai, Gemini. We do a lot of open source models, but that always depends upon which one we pick.

There's the workload, the data sensitivity, what latency we probably need, and then what does it actually cost. The way that we try to build our reference architectures through my office of the CTO is because historically, we were dumping everything into OpenAI. We're trying not to do that. We want to have an agnostic type of model provider architecture, and we're seeing this across in the industry. There's such a huge cost associated when you just pick one. This is now when you look above that model, we're going to get into the orchestration, agent layer, development layer. We'll use, probably the big ones are going to be LangChain, LangGraph. Those are there. We'll do the Microsoft Semantic Kernel, CrewAI. We're very heavy standardized on Microsoft.

We're one of their biggest partner globally. There's a lot of that, though we're trying to use others, but that would be Azure AI Foundry. When we get into the developer workflows, we standardize like GitHub Copilot. That's what it's been. The coding agent tools are important, but they're very selectively used. We look at enterprise workflows, ServiceNow AI, depending on where it is. When we look at the connectivity, the MCPs, we're shifting what we've built now to understand how do we now use MCPs as basically a new standard. We'll look at MCP servers. You only expose the capabilities that you've approved from again GitHub, ServiceNow, internal APIs. There's more to that.

Runlayer is pretty cool here because we are able to use it. It looks like it's going to give you basically a governed MCP gateway with a catalog and then auditability versus just setting up your own connectors as a developer. We use identity. This is super important. This is where we got two because we are federated by business units, but that is Entra ID and Okta. That is used at scale across the organization. We are looking at how do we use Okta AI for agents, or OAuth or delegation short-lived tokens is one.

I think it's understanding that getting as much details as we can as the user, how is this using the agent with what tool it is calling, and then what actual authority is behind. It gets convoluted and complicated here. These vendors are figuring this out. The governance thing is we are trying to figure that out. That's probably the hardest part, where you have got OneTrust, Witness, and you have got these things that can help with identity risk classifications, use case records, but they are all spread about. Part of it is just how we have been built as an org makes it is pretty much on us. If we were a cloud-native startup out of the Bay Area, this would be way easier.

The fact of how we have just grown makes this part really hard. Look, on the security side, we have production stuff with Noma and HiddenLayer. We are looking at, again, there is ProtectAI. We have done some productization with them on that stuff, with Onyx, Zenity. This is changing so quick. I feel like what I am talking to you now will be different next week because how do you do the discovery, the prompt injection, the runtime monitoring?

You can get into all that. You get into observability. We use Sentinel in a lot of cases, but also Datadog, CrowdStrike. There is a lot to that and then, how do we do the financial operations and stuff? I am sure I am missing stuff here, but I will stop there, and then we can unpack anything or poke at whatever you want.

---

**Client** [00:12:49]
Yeah. Maybe let us double down on Onyx, first of all. Maybe tell me a little bit more what you use Onyx for.

**Expert** [00:12:59]
Onyx is going to be because it's very fragmented, looking at it, getting visibility and control because all of these different use cases, agents, systems, whatever, they are being introduced by all these different business units and platforms. We have played around with it. It does an agent discovery inventory, understand which agents exist, who owns them, what does that. Is this for our build ones? Is this one for specific Agentforce or Microsoft or whatever? You get into, was the agent acting through my user account, one of the unclassified maybe service accounts? How else can I do it, API tokens? An agent, here is a good example, would need access, maybe not write access, but read access to GitHub.

You can now see that some of the underlying tokens maybe would allow for some administrative stuff because we haven't mapped it out. That's something it can help with. The other piece is that runtime observability, understanding what tool was called, what data was accessed. If you look at the logs on this stuff, you can see the API, but you don't understand the context. This is a really important piece because I feel like we are really behind the times in understanding what was actually done instead of just seeing a generic API call. I think they do some more stuff.

I am trying to remember off the top of my head, but the visibility, the inventory, the mapping of the behaviors, and there is audit stuff and trying to understand a way that you can have some sort of control plane that can do this. I don't know if it would replace an Okta, Entra, Sentinel. I doubt it. Everybody says they can do all this stuff. How do you connect all that fragmented layers that I mentioned on the governance side? That's the really hard part to get an agent view, to understand what they are doing instead of us having to duct tape it together.

---

**Client** [00:15:02]
Got it. Can you tell me also about Runlayer? What does Runlayer do?

**Expert** [00:15:08]
About which one? Run who?

---

**Client** [00:15:12]
I thought you mentioned Runlayer, but maybe I misheard.

**Expert** [00:15:15]
I probably said runtime. Basically, more it's doing the runtime observability. It's a Runlayer. I think that's how you were getting into, if I remember this, it's like how do you connect to the MCP if you are not talking about my runtime thing. There is some investigation on that that we have done. It goes back to what I mentioned, I think, in the beginning, where it was instead of having your users all downloading their own MCP server, the developers, you use Runlayer to give you that gateway catalog where you go in to connect. In theory, it will do a lot of things.

It gives you inventory of all the MCP servers and tools that you have a sanction inside the organization, then you go in, and it will connect to the enterprise identity layer. It can do things like it can look at ServiceNow. It can give read access. If you have to close the incident or do any kind of a restarting of a service, you have to have a different approval. It does that logging of the tools that's a little bit better than the Onyx piece. It's a way in terms of that governance of a control layer, point or whatever, between the agent and all these different systems that we have got convoluted stuck together.

You look at there is how do you do API connections, there is local MCP servers. Again, this is just another one piece in this because there are some caveats into it. It can only look at the traffic that actually passes into that layer with the MCPs. We haven't built things that way. There would have to be a big architecture. I think Runlayer is probably the enterprise MCP gateway, is probably a good way. If we go back to the Onyx, it's more doing around discovery and observability. Again, like I said, it changes on a weekly basis.

---

**Client** [00:17:14]
What are the most impressive companies you have seen emerged in the last six months on that topic, helping you govern AI agents? I know you mentioned Onyx, Runlayer. What companies are top of mind?

**Expert** [00:17:28]
This part of it is just us, what we are. They are just hard. I would say Onyx. When you are looking at for broad scale AI agent control plane, it is interesting because you can do discovery, understand some of the behavioral, do risk analysis and that runtime policy. That's pretty cool. WitnessAI is right there, where they can go to and they can do a little bit of the shadow AI visibility in that. We haven't dug that deep into the Witness part.

Arcade is pretty cool in doing some of the authorization. Again, this is more conceptual that we have done. We haven't quite implemented this into any production where you can separate basically the reasoning from the action, so that the agent doesn't just get massive user credentials. It's scoped specifically for the task, following zero trust, just-in-time credentials, stuff like that. This is important because as this stuff scales now, which it is, you can then do H-2A, MCP, support for all that. You are not just having to pick that one style and framework. The Runlayer that we just talked about, I think it's probably the cleanest to solving the whole what MCP servers are approved, what's your governed gateway. It connects into Okta, Entra.

I am sure it connects into Ping and all the other ones. There is also where Astrix and Token are there. You have the RuntimeAI stuff. Again we have a lot of exposure with HiddenLayer,. You have Protect AI, like Terra, Zenity. They are all worth watching because again, this is where you are actually seeing the model threats, like prompt injection, unsafe inputs. We have just historically have had a lot of challenges with that because we are figuring it out as we go. You have all the other incumbents that are there. That's like your CrowdStrikes, Apollos, CyberArks, stuff like that. If I had to pick two, it would be Onyx and WitnessAI at the visibility and control layer.

---

**Client** [00:19:43]
What does WitnessAI does?

**Expert** [00:19:46]
WitnessAI, they are similar to Onyx. We are playing with it more. Because what they used to do is basically, they did the visibility into seeing, are people just dumping stuff into ChatGPT? They did some policy enforcement that was built into the back-end. Now it's a bit deeper, and it's going more deliberately into objective security.

Instead of just monitoring how you are using whatever chatbot, they are now going to be able to do things specifically in terms of visibility and then the control of any agent. Now, again we will see how this comes. I sound like a marketing guy.

---

**Client** [00:20:26]
Got it. Who are the decision makers for deciding to buy these platforms?

**Expert** [00:20:31]
It's always cross-functional. It's going to be a bunch. Historically, we just bought things and we never make anything. We just buy a company. We index with standards, and the company gets to do its own thing as a subsidiary. Now we have changed that. It can't do this anymore to get rid of the sprawl that we have had. It's cross-functional. It's cross a ton of teams. Depending on is it AI, because we are talking more the governance now on this stuff. It's our AI team, which rolls up under my office, could be the platform engineering team as well. They will bring this use case, because they will see the MCPs, the agent adoption, all these different end agents that are everywhere.

For this type of stuff, then security will, which is under the CSO, but we work with them. They will go through and they will look at identity permissions, prompt injections, whatever. Our identity access management team will look at how are we doing access and NHIs, which are the non-human identities. Legal/privacy is involved here because if we are building ourselves or even any one of these now they are involved because they have to understand the data handling, the regulatory exposure, what region, different versus EMEA versus USA. We will have FinOps involved as well because there is consumption and cost, and then eventually, it gets down to procurement.

The first part is probably the hardest, is understanding what the real problem is instead of just buying what we do. If we have these unmanaged agents, duplicate tools, all these permissions, once we have figured this out, this then should dictate what we are doing. We look internally to say, we have one million already platforms here.

Can we look at maybe a hyperscalers or the SIEMs or CNAP, and then understanding, do we have something internally? Instead of just continuing down the sprawl, or we will bring in specifically for anything AI, we do bring in the independent vendors. We try to figure out some sort of POV, proof of value, try to build something out and then, it worked our way down to build a business use case, showing hard savings, reducing the manual effort of trying to figure this out. Avoided risk is a good one. Building that out, it's like a version of this.

---

**Client** [00:23:01]
Do you have a feeling that you're well-served with all the tools you currently have, or do you feel it's a little bit still like the Wild West?

**Expert** [00:23:09]
I think that's a huge debate that just happens consistently because we are already heavily invested in the hyperscalers, Microsoft, ServiceNow, CrowdStrike, all these guys, Palo. All of these vendors, they are adding some version of AI governance, and I am missing a million of them. They are arguing. It is always something to be like, we don't need another tool. We just don't. Can our vendors that we have solve? It might not be perfect, but is 75% good enough? This is the debate, or 80%, can it fix that part of the percentage of what we have? These independent ones that we talk to, they have to provide really something meaningful.

I think it's just the cross-platform visibility because we are running all these different models, open source models, frontier labs, all the incumbent platforms like ServiceNow, Salesforce, all the SaaS, that we have got. Is there some way to put a neutral talking layer right there? To be quite honest, no, I don't think there is a good problem here. Part of it is us trying not to just do what we have culturally always done, which is just buy the newest, shiniest thing, but to really understand what can we do. We just talk, and I wish I could give you a better answer. It's a really hard answer.

---

**Client** [00:24:34]
Okay. What do you use for costs to have observability on cost and business value and making sure that each token being burned is attached to a good reason for it and there is no other way to do it more efficiently. Do you guys look at things like OpenRouter or a platform that attach tokens to cost and to business value, this kind of stuff?

**Expert** [00:24:56]
Yeah. I think what you are bringing up is a very cool question because of just, again, with the Kimi K3 being like, "Well, why do we have to send this all to the best lab?" We have definitely been looking at it. Now, there is a difference between looking at it and actually operationing this at scale. I think we are just pretty immature in that. We do look to try to understand our token infrastructure consumption and somehow map it to a business outcome versus just like, "Hey, this is your token skyrocketing up." We look at the models. We look at the usage, the apps, the teams, and the use case.

We will do input output tokens, what model is selected, latency, GPU consumption where we need to, is there ingress, egress cloud cost, whatever the data platform cost, like a Databricks or something like that. We have looked at OpenRouter or Vercel or Cloudflare has got one, Azure has got, everybody has got one right now and to do things in limits and then usage and telemetry. PointFive is another one where you are trying to identify the waste, not just like a bill. All of these are some really, really cool. The problem is, I don't think they are fully ready for giant enterprise prime time.

We are trying to get there, but if I am being honest, it's hard because you have to figure out a way to get a business identifier to every request. Saying that this token belongs in support or a sales proposal. It's really hard to be able to measure the cost per completed outcome and not just doing it for millions or billions of tokens. Getting that data and abstracting information like support is probably the easiest one. How many support? What was the cost of successfully resolved customer cases or whatever? Did that time to do these cases decline, or how many account briefs did we create in sales and proposals and qualified or whatever? You have to figure that out.

There are optimizations we can do. We have done some things in terms of routing simpler tasks to cheaper models and the larger models. The frontier ones are for complex reasoning and doing that. You do it, but to roll that out scale is really hard. We will eventually get there. OpenRouter is cool because it can do the abstraction and the routing. We have it locked down for any prototyping and experiments. When you try to scale it out, there are a lot of issues that we have, the privacy, legal, security because of data handling. What are the contract terms? What's the reliability? We don't want anybody that's in line on the inference.

It could be part of an architecture, but I think there are still a lot of FinOps questions that have to answer. It's just really hard to connect the token spend to a business outcome in a way that makes sense. We are trying to figure out the way. We are getting there, but I wouldn't say we are by in any way productized this part or done it at scale.

---

**Client** [00:28:15]
I want to say there's different components around agents. There's identity. There's what data they can access. There's having visibility across your part. There's the routing. There's the FinOps aspects. Is there one part of all these different components where you feel you have less tools, or there's tooling across the stack, and you feel quite well-served?

**Expert** [00:28:40]
Yeah. If I get a question, having it all there, the routing, and everything is different. I think this is the biggest problem. We're okay in some pieces, but there's still massive gaps. There's no way around it. Obviously, we can improve on all of this, but the model and the app layer. We've made some okay choices, I think, finally, in terms across OpenAI, Anthropic, Mistral, open source, Llama, whatever you want. We're doing okay in terms of some of the orchestration stuff, like developing stuff like LangGraph, I would say Copilot Studios.

When we do some of our Microsoft Sentinel, our SIEM, our identity with Okta and Entra and then some of the data governance that we've done with Purview and some other stuff, I think we've gotten that. That was a really hard piece, but we've gotten that finally. Finally, it took years to get that to a point because garbage in, garbage out for these models, and that having that stuff classified and tagged and all that stuff, the data, is really important. This is like I'm being nice to us, but now I think this is where everything starts not being that great, is that what joins all this stuff together?

Okta could tell us who the user is, but they don't tell me, in all cases, which agent action, which agent did a tool call or an action, which tool it called. Our SIEM can show us some of the API calls, but it doesn't show us what actually was happening. If you have something like a Turbonomic or whatever, and they can show token spend or cloud spend, but they don't show what that actually means. Was that a good business outcome or bad? Because that's the only way to measure this stuff, and then you get into the governance. I think, looking at all this, there's not one vendor that can do all this. There just isn't.

Even like honest being good at doing discovery and control and Runlayer doing the MCP stuff and Noma and HiddenLayer and Posture and the runtime security. Again, we have too many tools. They don't integrate, and they don't correlate. You have to use just what you can do best, as a human. I think in the end, there is going to be a lot more consolidation. You'll keep your strategic identity access management, your SIEM, maybe your ITSM, what you're using for governance, and then you're going to pick one or two in the space that can eventually connect to all these different type of things and then do it. That's where I see it going massive amount of consolidation. That's why all these companies are getting bought up.

---

**Client** [00:31:34]
Yeah. What's interesting as well is that, look, you're much closer to the topic than I am. Let me test this hypothesis with you, and if I'm wrong, please tell me. It appears to me that some use cases may be, first of all, complex and have many different steps. I don't know, for some coding a new feature, or responding to some customer on a certain topic, or whatever use case. If you have a multi-stage process on some of the steps where you, for instance, are communicating with your customer, you might want to have a very powerful AI, like maybe it's Anthropic that's connected to your internal databases, etc.

Maybe on other steps that are not touching your internal data or touching your customer, you may be happy to use an open source model, a very strong open source model, for instance. It seems like there's a lot of pointed solution, some for security, some for governance, some for MCP, some for FinOps.

Isn't it the case that really in one action, as models and intelligence become more and more powerful, you may have some cost, some security, some data questions in one set of action. Shouldn't you have a platform that unites everything, security, FinOps, and governance, etc., because in certain steps, you may want to orchestrate in different ways depending on what the actual step is. Am I making any sense?

**Expert** [00:33:02]
Yeah. I think you're making a lot of sense. This is what the pain point is. You're actually, I think, echoing everything that I'm saying. Not everything. I totally agree with almost everything you said. One thing I would separate is a control plane from the underlying specialist control. When you look at these multi-stage workflows, each step has a different risk-cost data model. This is the over-runner. A customer support agent needs to do a classification, classifies the request using a cheapo model, whatever the cheapest one you can have.

You might want to do retrieving internal customer using something a little bit more controlled and then use a stronger model to reason through some of the complex issues. You switch back to the cheaper model to draft a response. It's like why people are like, "Well, I use Fable to write all my emails" and then you run out. I am like, "Well, that is probably not a great use case of Fable." Anthropic, you are going to be pumping out credits and your tokens and all that, and you can use Opus or whatever it is.

If the workflow wants to change entitlements or modify customer record in the support case, that then would require some version of human approval or do something with a chargeback or refund or something like that. I think the orchestration layer should make decisions based on things like what's the data and how sensitive, what is the authority of this said action, the quality that's required of this orchestration, what's the latency needs? What's the infrastructure cost? Are you using the Dell AI Factory so you can host this internally, or are you going to Anthropic? There is two different ones. Regulatory constraints, is this happening in Europe or is this happening in the U.S.? Completely different privacy needs.

If you screw something up, do you roll back? Can you reverse it? I think one thing I would maybe bring up in your hypothesis that you said, I just don't think you can find, at least in the short term, one vendor that can replace security, identity, governance, cost, and the observability pieces. Because if you are regulated, if you are a massive global Fortune 1000, you already have your strategic identity access management, SIEM, data loss prevention tools, data governance, cloud security, all that. Replacing all of that is just like, no way that can happen. I could never see that in the near term.

I think one thing that you are pretty much spot on is I think having a unified policy or orchestration that understands the workflows is different. It should know if we have this thing that I am acting through this agent. This step is using, say, that customer data. The model is approved for that data class and request. This tool can only read whatever it has to read, and this action will cost X amount of tokens. If this next step, and if he wants to do anything else that requires human approval, we should go through there because I am going out of whatever is there.

Whatever platform we are talking about needs to correlate the controls and then call the whatever system. It asks Entra or Okta for the identity information. It would call Runlayer for the MCP access. It would send all this information to then your Microsoft Sentinel, your SIEM for the audit, maybe incident response, if it came down to it. I think everything is pretty much spot on in the way you are going. I just think the unit of control needs to go from the individual model or tool to complete the actual business use case, action, outcome with all the individual steps. Again, it's not like the winners are going to own every underlying component.

It's the company or vendor that can make the policy across all these different workflows and then coordinate with them underneath. You have a one logical control plane, and I think a ton of enforcement points. I think you are pretty much spot on. The market probably will consolidate, I think, around a shared control plane and policy model rather than just one old school monolithic legacy product replacing the entire stack. I don't see it going that way.

---

**Client** [00:37:32]
That makes sense. If tomorrow, an entrepreneur came to pitch you this unified orchestration layer that could access some of the best-of-breed tooling out there and maybe just build some features directly as well, that would sound appealing to you just to understand or not necessarily?

**Expert** [00:37:49]
Yeah. I think it would sound awesome when you look at it. My office does all the technology scouting. All I do is talk to vendors, and I know how we are as a vendor. We are like, "Oh, yeah, we can do everything." I am like, "No, we cannot." I get into the discussions of being like, everything that you wrote there is ultra-appealing, and yet we would evaluate, especially if it sits above the existing stack because if you are not trying to replace everything, okay. If you sit above it, that makes way more sense for somebody like us. You just can't replace it for something like us. It's too entrenched. Maybe piece by piece, you could down the line.

If the pitch was like, "Hey, we provide an orchestration policy layer that understands this whole agent workflow. It will get the right model tool. It will do the right system data controls and then call the best of whatever systems that you already have in place to do," that's awesome. That is the big problem, the fragmentation. One tool sees identity, another sees MCP calls. One sees spend. None of these platforms can do this all at once at the runtime.

I would ask questions like, "Do you actually control this or are you just aggregating dashboards? Can you actually route the model? Can you deny a tool? Can you operate across OpenAI, Anthropic, Google open source?" This is where it gets really hard. Of course, that sounds pretty cool, but show me. Like, the state of Missouri here in the U.S., that's their state line or their state motto, "Show me, don't tell me." Let's see it in action with our data.

---

**Client** [00:39:37]
Okay. Just to triple click, let's say this dream tool exists and it's quite compelling. Can you describe it to me in more details? I know you said, for instance, it's orchestration, it calls Runlayer, for instance, for MCP access. Let's break it down a little bit more, because when you said it calls the best of breed systems, what kind of systems would you like it to call? Can we just break it down a bit more?

**Expert** [00:40:06]
Every organization that's of size already has these kind of tools. Some of them are standard. Some of them are going to be homegrown. They've got some version of this. There's going to be a bunch of layers, because it needs to coordinate this kind of shared policy context that sits above all this stuff. You're going to have the first piece is the model and the inference layer. This is really important. You got to connect to like AWS Bedrock, OpenAI, Anthropic, approved open source models that you want to run internally. At that workflow, it should choose the model based on quality, cost, latency, data run, all that stuff. The second is it's got to connect to the identity authorization layer.

That's for us, that's Entra and Okta, but that could be like CyberArk. It could be whatever the workload identity. It should understand the user and the agent and exact permissions. It should know that the agent can say this thing can read a case, but it cannot close the case if it's for a support ticket, something like that. It's got to figure that out. It's got to have a tool, a connector layer, where it should govern the MCP servers, the APIs, the SaaS connectors. This is like what the Runlayer is doing and agent-to-agent calls. You have your approved catalogs. The organization has approved like your Mac store for whatever company if you're running a Mac.

You can only download the apps that they do it. Similar kind of thought process here. You do like a data control layer. This is where we use Microsoft Purview, so that it understands the data loss prevention, the classification. Is this internal? Is this classified? Is this public? Is this whatever? That's important because before you send any information to the model, it should know whether this data contains personal data, source code info, all that stuff. This is really important. Look, are you going to be able to understand that runtime layer? If you are going to use a HiddenLayer, Noma, for that prompt injection, getting all that information. It's going to be a cost routing.

How do you integrate into whatever FinOps tools or OpenRouter, whatever it might be? You can see the full cost of all the steps, not just tokens, but the data, the GPU, all of that and then the observability. You feed something into Splunk, Datadog, Sentinel, whatever. Who initiated the workflow, what acted, what was there? You could probably do something. Again, this is going through everything here. Is it in ServiceNow? If it's going to do something inside of your system of record or ERP, it should interact in this stuff to understand where this business occurs. If you are just drafting an email, that's pretty low.

If you are changing something on our internal e-commerce entitlements for an order, that's higher risk, and there should be some sort of human approval. It's not just an orchestration engine or a security dashboard, but it's understanding the actual work for that agentic work and deciding the model, data, identity, whatever, and the approved paths and then basically being able to prove out why that decision was made. It's really hard.

---

**Client** [00:43:47]
That makes sense. Visibility as well into so that it's not a black box.

**Expert** [00:43:54]
Yeah.

---

**Client** [00:43:55]
Okay. That's quite helpful. Is it true that when you choose a model provider versus another, obviously, there is a bunch of considerations, as you said earlier, latency, like regulatory constraints are there. Can you help me understand how security and cost are intertwined? Is it that you may say, I accept to take a little bit more of a security risk if my cost is that much lower, or is this not how people think? People will say, the CISO defines for security purposes, we can only use X, Y, Z, and then that's the models that are used. I am trying to understand the interplay between these two variables, cost and security, if they interplay at all.

**Expert** [00:44:38]
They definitely do. This is probably one of the biggest hiccups that we have, where you have people that want to just be, "We want to get this out." Innovating security is, you can't. I think they're absolutely right. You don't trade ever away in a regulated organization, anything that's mandatory security because something is just cheaper. You don't do that. Usually, what we will do is you establish, here are the models that we are going to approve. You have a big tier where you have legal privacy, procurement because there is cost. Which providers are good, and then what are the ways that you can use it that are acceptable? There are different data classes and use cases.

Again, this is hard to get down, but when you have some version of that, you can then do some more optimization for latency and quality within this pool that you have, and cost. For public or low sensitive stuff, we can use smaller commercial models, open source models, because it's just, who cares? It's nothing, whatever. Our public knowledge base articles. When we get into some internal source code or confidential proprietary IP data or whatever, then everything starts narrowing. You will require maybe an enterprise API that we have got contractual agreements with, like OpenAI, so you cannot train it on this data.

You have to process this in this specific region if we are doing Azure, like in Germany or Europe, whatever versus being able to do it in the U.S. We have to log all this stuff. I think it's asking, is this model permitted for this data and this action? If it is, can it deliver quality and reliable information? That's an important one. When they meet this kind of threshold, which then has the best cost and latency? That's the way that we would work it through. You have to make risk-based trade-offs for sure. It's not anything. They are bounded. We will accept a slightly lower quality model and keep all of our sensitive data within a controlled air-gapped environment.

That's just the reality. We will get higher latency or higher cost for something that might be a customer-facing decision because you want the best thing for it. We are not going to just say, "Okay, this is way less secure, but it's 30% cheaper, so let us throw all of our internal customer employee records there." No, again, I hope they wouldn't do that.

---

**Client** [00:47:11]
That makes sense. Especially on a platform that you describe that would be quite horizontal, it seems to me like it touches so many topics that some relate to the CFO, some relate to the CISO, some relate to the CTO, some relate to the CIO. The workflow is a little bit all-encompassing, because if it is a complicated process, you are going to touch everything, cost, security, etc., how are companies evolving? How do you see in the future the buy decisions evolving?

Is it like the CIO decides, but then they are also in a meeting with other heads of finance, security, etc., or do you see it that CISO buys separately, CTO buys separately? I am just trying to understand, and I know that historically it was more best of breed solutions. If a layer such as the one that we describe emerges, I am trying to understand how it would even be sold, to whom, given it touches so many different topics.

**Expert** [00:48:13]
Yeah. I think this is the elephant in the room. You are right, it touches so many different things with different users and different that. I think that's the biggest challenge. It's horizontal, but enterprises don't really buy horizontal stuff. Large ones, they buy something that fixes a problem. You will have one person that has the budget. I think if I was trying to sell it, I wouldn't try to sell to the CFO, CISO, CIO, CTO. You will never, A) get them all in a room and then that whatever process is going to be unbearable. I think looking at where is this the biggest pain?

It's going to be data leakage, uncontrolled agents, and that's going to be either your CAIO, like the AI leader or whatever, or the CISO. That's where I would target this right away and be like, because this is a massive problem everywhere. You go in there and be like, visibility, policy enforcement, we are going to reduce your risk, friends. You will sell us on that. You get into if they are also talking about escalated models or tokens or whatever, that might then be your CIO or finance. You go to them and say, "Hey, we are going to do business outcomes and model routing and all that."

You figure out which one of these, or there is more, who you want to do it? You expand from there because you show that, "Hey, this same workflow produces the same value for the same people." I would say CISO gets better auditability, CIO gets, "Oh, look at the standardization," and we get better tools for all. It's like the CTO will be like, "My team will get faster deployment and model flexibility and financial savings." There still needs to be just one sponsor on the vendor.

I think this would probably sit at any large org with either the CTO or the CAIO. These things are all building out, or building these centers of excellence. I think the CISO will still have the ultimate veto policy because it's going to be security sensitive stuff. I think it's a land and expand. That's just one of those things that I would say.

---

**Client** [00:50:33]
If one were to have this long-term vision of building this orchestration platform, but starting, as you said, with a wedge to a specific persona to solve a specific problem, is there a specific problem to solve, or because we just said there is so many best of breed solutions out there, or at least emerging, that maybe there is not even a good wedge anymore? Maybe it's a red hot market. What would be a wedge that would make you listen, if anything?

**Expert** [00:51:02]
We talk to customers. I am with customers. They are like, all of these would work in some capacity. If I had to pick one, really, I think that improving the business transaction across all these different models, agents, and that. You don't want to just show, "Oh, generic MCP governance or tokens." Everybody does that. There is one million of them right now. I think it's like you go in there and say, give us one important multi-step agent workflow and then we will show you what it costs, what data permissions it is, and then where every step is compliant or not compliant and whether did it actually produce that business outcome.

You go in there and just say, "You give us this." We'll come back to you and say, "Hey, right now I've got in support, I've got my Salesforce, ServiceNow, internal knowledge base, and five models, an MCP gateway, and all this." Each tool sees its own thing, but nobody can answer the complete question. I'm just making it up. This is where you would go in and say, "We can do this. We can answer this question. Let's unpack all this and take a look." It's going to be turned into, because it's pretty deep, it's going to be a lot more on the consulting side. This isn't something you use a demo out.

They all have to afford deployed engineers because you're getting in there because you're going from visibility to action, and you're showing this stuff. I think the market's super crowded at the individual layer, and it's not just having another specialized control, it's the connecting part, the brain or the nervous system that understands that complete agent transaction and turns all this fragmented info into a way that a business person can understand the policy and how to optimize it, so they can get more value out of that AI system, something like that. I don't know. I might have monologued.

---

**Client** [00:53:07]
Who do you sell that to? What's the right persona for that, the CIO?

**Expert** [00:53:12]
Yeah. You could start at the CIO. It depends on having that discovery call and being like, what is the biggest pain point that they have. I think the CIO is going to be the best economic buyer, right then. Talking to CIOs, enterprise architecture, or any automation leaders, these are the people that are accountable for basically taking any of these agents into production across different business units. CIO, but then right under them, they have some sort of an enterprise architecture team. That's who I would target.

---

**Client** [00:53:47]
Okay. That was very helpful. Thank you so much. Really appreciate your time.
