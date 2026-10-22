---
theme: "Enterprise Software & AI"
title: "IT Director at PepsiCo Believes AI SRE Solutions Are Key to Boosting Productivity and Reducing MTTR"
doc_id: EC-1000000-209082
source_line: "Highradius · Expert Call · Customer · 14 Jul 26"
date: 2026-07-23
company: "Traversal"
pages: 2 of 8
saved: 2026-10-19T17:35:37.295Z
url: https://research.alpha-sense.com/search?search_id=tmp-hpf1dheo007kqfxozv3v&sort=DATE&order=DESC&docid=EC-1000000-209082
---
# IT Director at PepsiCo Believes AI SRE Solutions Are Key to Boosting Productivity and Reducing MTTR

Company Deep-Dive

DATE PUBLISHED

23 Jul 2026

INTERVIEW DATE

24 Apr 2026

EXPERT PERSPECTIVE

Customer

ANALYST PERSPECTIVE

Investor-Led (Buy-Side)

PRIMARY COMPANY

Traversal

SMART SUMMARY

Summary

The interview covers the expert's experience implementing and evaluating AI SRE solutions, focusing on the selection process, integration challenges, and desired future capabilities. The discussion includes vendor comparisons, evaluation criteria, and the evolving role of AI SRE platforms in enterprise IT operations.

EXPERT BACKGROUND

- Leads global observability platforms and command center operations at a large multinational company, with several years of experience overseeing engineering and SRE teams and implementing observability and AI SRE solutions.

EXPERT SENTIMENT

- Believes AI SRE solutions are essential for improving productivity and reducing mean time to resolution (MTTR) in complex enterprise environments.
- Views AI SRE platforms as evolving toward becoming core platforms for SRE operations, but does not expect them to become the most expensive tools in the tech stack.
- Is open to switching vendors if significant advancements in code analysis, integration, or financial terms are offered, but values partnership and technical capability over cost alone.

TAKEAWAYS

- The expert's team uses a variety of observability tools including ThousandEyes, SevOne, SolarWinds, ServiceNow ITOM, AppDynamics, and Elastic, with 20+ SREs operating 24/7.
- Prior to adopting AI SRE solutions, incident correlation was manual, time-consuming (40-60 minutes per incident), and required coordination across multiple teams and systems.
- The main drivers for evaluating AI SRE vendors were to reduce incident resolution time and improve SRE productivity by automating correlation and triage.
- Traversal was selected for its strong alert triage capabilities and ease of integration, with commercial terms based on the number of applications onboarded rather than data volume.
- The expert is monitoring competitors like Resolve AI and is interested in future capabilities such as automated code review, deeper business context integration, and predictive impact analysis.

AlphaSense Smart Summaries are AI Generated

Introduction and Expert Background

SRE Team and Manual Processes

Vendor Evaluation and Criteria

Traversal Selection and Costs

Competitors and Potential Switches

Consideration of Generic AI Solutions

Future of AI SRE Platforms

Introduction and Expert Background

EXPERT BIO

IT Director at PepsiCo. The expert can speak to their experience with Traversal AI, having been a decision maker for its adoption and implementation, which aligns with the project's focus on evaluating AI SRE solutions.

S&T Director at PepsiCo since March 2023.

Technology & Operations Executive with 18+ years of global leadership across Observability, ITSM, CMDB Data Governance, and Command Center Operations. Currently S&T Director at PepsiCo, leading global teams across India, the US, and Mexico to implement AI-enabled, proactive, and preventative IT operations. Stanford GSB alumnus (SEP), passionate about transforming IT into a predictive, business-aligned enabler of resilience and scalability.

They are responsible for transforming IT operations by integrating AI-driven monitoring and embedding anomaly detection into the observability platform. The expert also oversees CMDB data integrity through a Data Health Index to improve configuration compliance and control.

Prior to PepsiCo, the expert was the Senior Manager IT&D - Global Service Experience at Reckitt, leaving March 2023. The expert was responsible for the end-to-end service operations run by vendors. They owned the organization's ITSM process and managed key transformation programs to improve the overall IT service and work-from-home experience for employees.

The expert can speak to Observability, AI-driven IT operations, Command Center Operations, CMDB Data Governance, anomaly detection, predictive intelligence, and ITSM processes.

View More

INTERVIEW TRANSCRIPT

**Client** [00:00:00]
Hi.

Thanks for taking the time to talk with me.

I am interested in learning more about AI SRE Solutions.

Can you share a brief overview of your background?

**Expert** [00:00:11]
Yeah, I can.

I lead the global observability platforms for PepsiCo.

Both the engineering and also the command center operations which use these platforms and products that we build.

That's predominantly my role, being in this for a couple of years now.

---

**Client** [00:00:28]
Got it.

Just what type of tech stack do you have from observability?

Just maybe go through some of the software vendors.

**Expert** [00:00:38]
You're talking about the what platforms we use.

We use ThousandEyes and SevOne from IBM for network observability.

We use SolarWinds for database and we also use ServiceNow ITOM for event management and correlation.

For application we use AppDynamics.

APM is on AppDynamics predominantly.

All of these MELT data coming from various techs is stored in Elastic.

---

**Client** [00:01:07]
Got it.

Can you walk us through how many SREs you have on staff?

**Expert** [00:01:13]
We have about 20+ SREs on staff, running 24/7 operations, looking at signals that are coming out of these observability platforms and taking actions and recommending actions and coordinating with various engineering teams.

---

**Client** [00:01:28]
Got it.

Do they do most of the work manually?

Do they have a critical operating system to run in or not today?

**Expert** [00:01:35]
When you say critical operating system, can you explain what you're looking at?

---

**Client** [00:01:40]
Yeah, previously, before any of the AI SRE vendors, did they have any operating system that they ran into that they used every day?

**Expert** [00:01:48]
No.

---

**Client** [00:01:49]
Can you walk me through that process of how they did correlation?

Did they have to do it manually?

What did that look like?

How much time did that take for certain issues?

**Expert** [00:02:01]
It used to take about 40, 45 minutes.

Let's say for example that there is a critical alert from a specific network device or a specific location of a network-related.

just taking a random example, that comes out from ServiceNow which is our ITSM and ITOM engine.

Engineers used to look at it, try to correlate that going to different other products like SevOne to understand where is this particular network, what are the switches, routers, etc.

What are the other devices that are there and then try to find out whether that is really down, what are the upstream and downstream other switches, routers, network devices, etc.

Are they available?

Is there a backup device that is available, whether network is being routed to and all of it?

Used to look at all of it manually, going through different systems, correlating that information that's coming from the alert, validating it, reaching out to certain individuals, pinging it manually, finding out that's a true alert or a false alert, and then making a decision on what needs to be done to escalate it to someone.

That used to be the manual process challenge
utilizing multiple systems, correlating multiple systems and different SREs have different knowledge, wisdom and experience.

Each of them used to look at the same issue in a different way as well sometimes.

---

**Client** [00:03:26]
Got it.

Can you talk about why you decided to evaluate these vendors, what was the catalyst to do so?

**Expert** [00:03:33]
I think the catalyst to do so is what I just said.

One of the key things catalyst to do so is the one that I explained, which is individuals, especially we the major incidents, major alerts, etc., it takes about, let's say for example, there is something majorly broken, whether it's an application, network, device-causing business impact, etc., whatever is it, majorly something's broken, an SRE engineer gets in and tries to correlate it, look at different applications, correlate the data, look at the various metrics and logs that are there, look at all of it.

It takes, if you ask me, about 45 minutes to one hour, a major incident call if an issue has happened to actually determine where the problem is.

Our assessment says that if you have four hours of downtime, most of the first one to one and a half hours, trying to just find out where the problem is.

That is reason number one.

Reason number two, another catalyst reason, as you asked, is these SREs are not experts in every technology.

You might need in that first one hour, experts from database, experts from network application teams, the server team, Windows team, Linux team, all of them together, looking at their own technology stack, trying to find out where the problem is.

If you look at complex organizations, you have various strategic partners, service providers who are actually doing that particular role.

It predominantly means that each partner is probably trying to say, "Hey, my application is all fine.

I think we moved to look at the database."

Someone says the database is fine.

I think the link between application and database is gone.

All of it takes a lot of time.

The productivity of these engineers is going high because you are actually not doing something productive like deploying the code, writing something good, writing a code to help something.

That's not what you're doing.

What all of them are doing is trying to find out where
the problem is, probably putting that blame game during the major incident, forgetting that it's impacting the business
and then causing the issue.

We wanted that to also take away.

We wanted to improve that productivity as well.

To
reduce the time to resolution and to improve our productivity for our engineers
, SRE engineers or support teams, etc.

These are the two big reasons why we started looking into the market last year to find out, "Hey, what are the cases we have and then how do you think it will help?"

etc.

---

**Client** [00:06:11]
Got it.

Can you talk about the evaluation and how you found some of these vendors?

**Expert** [00:06:16]
Evaluation has been simple.

We wanted to look at what are the various products in the market.

We want to talk to them, get a demo, understand what they're doing.

A couple of things that we wanted to do is whichever vendor, one, should be easily be able to integrate with our stack.

Two, should be easily be able to workable.

When I say workable the because such a large organizations have large complex systems where we also sometimes discover something new over a period of time suddenly.

We wanted someone who can step up, help us navigate those technical complexities.

We wanted to ensure that during the evaluation process that it's actually helping us from both productivity and MTTR.

The evaluation was predominantly based on the facts.

Once we have done a pilot or POC, whatever we call it, only based on that we have made a call saying that "Yes, this is the product that we're going with."

---

**Client** [00:07:18]
Got it.

Can you talk about the evaluation criteria though, WHat what you are evaluating specifically across the vendors?

**Expert** [00:07:25]
A couple of evaluating criteria was we identified that there are about eight to 10 top integration systems.

The technology stacks that I spoke to you initially about what technology stacks we have for observability, etc.

At least out of those eight, we wanted to ensure that five to six integration should be seamless and fast.

That's what we wanted to look at.

During the evaluation period that was one of the key criteria to move from a pilot to a production phase.

The second criteria was very, very clear that we put a target to ourselves saying that we want to ensure that we at least have 20%-30% meantime for resolution once we onboard specific set of applications onto this particular AI SRE product.

At least 20%-30% reduction in meantime to resolution even for normal incidents or major incidents.

That was number two.

Part of evaluation criteria, what we also get is during the pilot we've deployed about three to four applications and we've run those products in parallel to what normally our SREs used to do.

For example, there is person A who is using this product and there is person B on the side who's not using the product.

We actually did tell them that someone's using, someone's not using.

We've actually did time and motion study to understand how long does an engineer who doesn't use the product takes and how long does an engineer use the product takes.

We did that experiment for a couple of weeks to find out that whether that is really showing benefit, even if it is not giving us accurate 100% confident results, but at least up to 70% confident results etc.

If you remember what I said earlier, I said that we said during the pilot phase we should integrate at least five to six systems only.

We didn't integrate everything.

We wanted to scope our pilot with a specific scope, not go overboard and set ourselves for failure from both sides
, by the way.

We did that.

During the entire evaluation criteria, we assessed a couple of weeks of assessment on time in motion study, whether that's beneficial or not.

We calculated that in soft savings in dollar value on how much an engine product of time is being sold.

We also evaluated in one of the live calls where we use this how much time we've actually saved for a similar incident we had before.

We extrapolated what would happen if that application had similar incidents over a period of year.

Taking the past data and we extrapolated and mixed it saying that "Hey, are we hitting the target that we have set ourselves"?

I think these are the different criteria that we set ourselves for successful evaluation.

---

**Client** [00:10:21]
Got it.

Can you walk us through how you first met Traversal?

**Expert** [00:10:26]
Every large enterprise's app, we have our own innovation teams who are on for organizations like Traversal, etc.

We generally go and tell what's our problem statement to that team and they go back into the market and look at who's trying to solve it, and they bring right teams across for demos and then we look at it and find out what's going on and then we go from there.

That's how we do it.

---

**Client** [00:10:48]
Got it.

Can you talk about what Traversal does well and why you picked Traversal?

**Expert** [00:10:54]
Yeah, I can.

One thing Traversal does well is there are a couple of things from the technology standpoint and there's from a culture standpoint.

Technology standpoint.

I think the alert priority that they do on the product is extremely great.

Just to give you an example, it does triage for the number of thousands of alerts that are there for a specific application or a device or a network, etc.

It triage this all the alerts that I have, multiple alerts, and tells me exactly which alert should I prioritize to pick.

Otherwise with a limited set of engineers,
which alerts to actually give importance is pretty tough at times
because all we generally get in ITSM or ITOM tool is a critical major alert.

Understanding that alert, correlating that with the metrics, events and logs and traces and then giving us saying that "Hey, this is an alert that you need to pick and here is probably the impact if you don't act on it" I think that's the most interesting part for Traversal product.

---

**Client** [00:12:03]
Got it.

Can you talk about the ingress into Traversal?

It seems like there is a lot of requirements to integrate lots of systems and pump in a lot of data.

Can you walk us through what exactly is needed and how much exactly that costs?

**Expert** [00:12:18]
I wouldn't know the cost of it because we don't have a commercial model on the data ingress.

We have a different commercial model based on number of applications on board rather than rails and NPLs.

The data ingress part of it is interesting.

For all the technology stack that I mentioned, the data ingress is pretty much out of the box and it was easy to configure, etc.

The one that we're trying to crack on board is complex enterprise ERP logs and data which is not in any of these tech stacks that I've mentioned to you.

Let's take for example Oracle or SAP etc., their MELT data, all the code and everything resides in that.

What we need to crack is that because that's when we'll see more data because what I'm ingesting is only certain set of data from observability stack.

There's a lot of data that every application like SAP Focused Run.

For example is another product which in SAP stores all of the whatever happens within SAP ERP.

The integration of that into Traversal or any other AI SRE product would be interesting.

I don't think any of the AI SRE products have cracked that.

Maybe
someone has cracked it, but the challenge
is the security protocols etc, considering the ERP, the personal information that it contains and financial and HR-related information.

That's something that we are currently working on, I would say.

---

**Client** [00:13:51]
Got it.

Can you talk about how much you pay currently to Traversal?

Is it above $250,000?

**Expert** [00:13:58]
Yes, it is.

What I can say is we have chosen not to go with data ingress charges or number of nodes, like any other products do.

We've chosen the number of applications or systems that are getting onboarded on Traversal rather than data storage that we're using, so on and so forth.

Because this is pilot, we don't know the cost of data that they will consume.

We don't know the cost.

We wanted to know what we're going to spend the first year and ensure that we call out the true productivity and outcomes are delivered in the first year before we look at any other model.

Our commercial model is a little different probably from others.

To answer to your question, yes.

---

**Client** [00:14:43]
Is it above $1 million currently?

**Expert** [00:14:48]
No.

---

**Client** [00:14:49]
Got it.

Can you talk about some of the other vendors that you looked at in the POC beyond Traversal?

**Expert** [00:14:56]
We also looked at Flip AI.

We looked at it, we tried to do a POC, the product demo and everything went well, but for some odd reason didn't work out.

Whether it's timing or whatever we call it, it didn't work out.

I did look at Now Assist and other ServiceNow stuff, but not really a true AI products that are available at that time.

I'm currently seeing Resolve AI being a great competitor today.

While we haven't explored in detail or did a pilot with them, I see they're making huge waves as of now.

---

**Client** [00:15:32]
That was my next question.

What would cause you to switch away from Traversal and look at Resolve AI?

**Expert** [00:15:39]
I don't know.

Maybe a great financial deal, but financial deal is secondary.

The partnership that I want to look at what's there in Resolve AI is, "Hey, can you read the code base from," whether it's GitHub or other code bases, etc.?

Can the product help us in running the code before we deploy the code into the production?

Basically identifying if there is a new code being deployed.

Can it actually look at the entire code, identify what test case and scenarios we should test based on the change that we are doing in the current code?

Can it also predict what might happen if
this code goes in and tell us that "Hey, if this threat
goes in, there is a high risk that XYZ, another system might break, impact, etc."

I think these are few things that I would look at.

I'm not sure how much whether Resolve AI is into this, but I would love to explore that later this year on code reviews, test use cases, etc.

---

**Client** [00:16:39]
Got it.

When you were looking at this product, did you guys ever consider maybe using something more generic like a Claude or a ChatGPT connected to the right data sources and seeing what the performance would be there?

Was that ever an experiment?

**Expert** [00:16:56]
We didn't do that experiment to be honest, but it did come to my mind since last couple of months with Claude and ChatGPT making so much changes in the way that they are expanding.

Last year when we were doing this, no, it didn't come to our mind that we should try.

Somehow it crossed my mind twice or thrice saying that why shouldn't we look at this opportunity.

Again, to be very honest, we're not an engineering organization to experiment but would love to try that out of curiosity and see how it goes.

---

**Client** [00:17:26]
Got it.

Not enough resources to run an experiment like this.

That's probably the reason why it never came to mind.

**Expert** [00:17:34]
Yeah, probably that's right.

---

**Client** [00:17:38]
Helpful.

When you think about how these platforms need to grow and just become more embedded in your workload, what does Traversal need to do to really be a vendor that you're going to consider to be growing with?

Is it getting deeper on root cause analysis?

Is it getting deeper on embedding into some of your downstream systems?

What might be the things that they need to do to provide more value for you to stick around?

**Expert** [00:18:02]
I think it's going to be a combination of what you said and couple of more in my personal opinion.

It's true for any product whether it's Resolve AI, Traversal or any other product in the market today.

Let me talk about what you haven't spoken and what I think in my mind.

I did speak about code reviews and testing the code itself, etc.

I would want a platform or a product which does end-to-end SRE for me.

It's just not root cause analysis, it's just not alert, triaging, etc., but also it looks at my infrastructure code or application code and tells me that "Hey, you need to perform these ABCD tests, you're changing this code and I predict that this might impact ABC system or application".

As you rightly said, I want these platforms to be corely embedded into core enterprise applications which are running the business for business where they will actually understand the context of it.

Let's take an example of any AI SRE product.

You have an AI SRE product which is looking at all of the observability data and telling us that "Hey, this is the probable cost for this particular instant," what I would also want a platform to do is additionally should understand what that application is doing for business, what is the impact of it and also call out that "Hey, you know what, this application is used in Australia.

It's non business hours.

It's okay.

It's not supposed to be a major incident."

It should understand the business, the context of the business which is probably lying somewhere in technical documentations or business documentations, etc.

That's something will be a future for all of these products.

---

**Client** [00:19:46]
Makes sense.

As you think about what you just said, are there any products that you're currently using that you think would go away over time?

Maybe because you're just using more Traversal in your stack.

**Expert** [00:19:59]
I don't think so.

There will be products that will go away because Traversal is just getting aggregating and traversing all my causal inference and telling me what am I supposed to do.

Giving me direction.

It's not storing data or anything, it's just utilizing all the data that's available across multiple platforms, etc.

The way that I look at it, any of these products, and again not talking about what I'm using but including Resolve AI or anything, is it has to be a platform on top of all of the other observability stacks and help aggregate all the data that's getting generated across the board, applications, network, infrastructure, database, etc., and then give us direction to the AI SREs.

That's what I would look at.

What I look forward in the future is I would expect the number of AI SRE engineers would go down because of products like these.

When I say go down, I'm not saying they get laid off or anything.

All I'm trying to say is there will be a shift in what they're currently doing to what they will be doing in the next couple of years or maybe just in a year's time.

That's what I would say.

---

**Client** [00:21:12]
Makes sense.

Maybe last question, could you picture this being a top three spend item compared to all the other tools that you guys are buying or is this going to be below that line?

Is this going to become a very expensive tool?

**Expert** [00:21:27]
I don't think so.

If it becomes very expensive tool, then
it's going to be a problem for everyone
.

I'm not talking about for a company like us or for the product company.

I'm talking about if this becomes a top three spend,
it's going to be a very dangerous situation in my opinion
.

I'll tell you why.

I'm assuming that most of the observability products today, if you look at any of the observability products in the market, whether it's AppDynamics or anyone, everyone has their own AI layer embedded on top of it.

No one has correlating other data into their own stack.

Products like these is what they're doing.

I don't think so they'll be in top three because
other products are pretty costly
.

I'm talking about the core observability products.

I think they will be in top five or six spend, but every enterprise will look to bring something like this into their ecosystem for sure.

I don't think so it might become the top three five spent to be very honest because I know the dollars that we spend on various other products.

If this also costs as much as that, then there is something predominantly wrong.

I would say that this will become top five or six spend.

I have a very strong feeling
just as a last point that these AI SRE products will become platforms rather than a product.

In my opinion, they become the core platform to run any SRE engagement in organizations and enterprises.

---

**Client** [00:23:00]
Really helpful.

Appreciate that last comment and thank you so much for your time.
