---
theme: "Energy & Grid"
title: "Founder & CEO at Fenxlabs.ai Believes Crusoe Energy Systems Faces Operational Risks and Customer Concentration Challenges"
doc_id: EC-1000000-261005
source_line: "Crusoe · Expert Call · Customer · 15 Oct 26"
date: 2026-10-15
company: "Crusoe Energy Systems"
pages: 2 of 2
saved: 2026-10-19T16:44:07.131Z
url: https://research.alpha-sense.com/search?search_id=tmp-0pnbg1kc8uodovl7vbczkp&sort=RELEVANCE&order=DESC&docid=EC-1000000-261005
---
# Founder & CEO at Fenxlabs.ai Believes Crusoe Energy Systems Faces Operational Risks and Customer Concentration Challenges

Credit Deep-Dive

DATE PUBLISHED

15 Oct 2026

INTERVIEW DATE

13 Oct 2026

EXPERT PERSPECTIVE

Customer

ANALYST PERSPECTIVE

AI Interviewer

PRIMARY COMPANY

Crusoe Energy Systems

SMART SUMMARY

Summary

The interview covers the expert's experience as a major customer of Crusoe Energy Systems Inc., discussing their use of Crusoe's GPU infrastructure, reasons for migrating away, comparative pricing and operational risks, and perspectives on Crusoe's business model, customer base, and future risks.

EXPERT BACKGROUND

- Founder and CEO of an applied AI lab with extensive experience in custom model training, inference strategy, and multi-vendor GPU infrastructure, including two years as a significant customer of Crusoe Energy Systems Inc.

EXPERT SENTIMENT

- Views Crusoe's behind-the-meter power generation as a double-edged sword: a cost advantage but a significant operational risk, especially for training workloads.
- Believes Crusoe's lack of grid connectivity and reliance on microgrids limits their appeal to enterprise customers with strict uptime requirements.
- Sees Crusoe's financial exposure and customer concentration, particularly with anchor tenants like Oracle, as major risks to their long-term stability.

TAKEAWAYS

- The expert's company used Crusoe for large-scale, bursty GPU workloads, primarily for custom AI model training, but migrated away due to operational risks tied to Crusoe's power generation strategy.
- Crusoe's pricing is consistently lower than competitors like CoreWeave, largely due to their unique power generation approach, but this comes with higher operational risk and less robust support.
- A significant outage (likely cooling-related) led to substantial financial loss for the expert's company, with Crusoe unwilling to reimburse due to SLA limitations, highlighting gaps in service agreements for performance degradation.
- Crusoe's customer base is heavily concentrated among anchor tenants (60-80%), with smaller customers mostly on flexible arrangements; the company is exposed if major tenants like Oracle reduce commitments.
- The expert expects continued growth in demand for custom model training and GPU compute, but sees Crusoe's long-term prospects as challenged by financial risks, lack of grid connectivity, and increasing competition in managed inference services.

AlphaSense Smart Summaries are AI Generated

Introduction and Initial Context

Vendor Selection and Usage

Pricing and Operational Challenges

Migration and Switching Costs

Service Quality and Comparisons

EXPERT BIO

Founder & Chief Executive Officer at fenxlabs.ai. Project Detail
Target: Crusoe Energy Systems Inc. and its commercial relationships and operational track record as a GPU cloud and AI infrastructure provider
Call Purpose: To understand how Crusoe performs on delivery and uptime, and how sticky its customer relationships are, including pricing, contract terms, and any moves to other providers, as the business continues to scale
Expert Relevance: Expert is the Founder and CEO of FenxLabs, where they own infrastructure strategy, vendor selection, and procurement. FenxLabs ran workloads on Crusoe from early 2024 until migrating away in early 2026, so the expert can speak to Crusoe's service continuity, commercial relationship, and the factors that led them to leave, including the risk profile of its behind-the-meter power generation model
Expert Geographic Focus: Europe

Founder and Chief Executive Officer at FenxLabs. Reporting to the Board of Directors, the expert is responsible for leading the strategic vision and engineering of AI infrastructure, specializing in scalable intelligence systems and modular agent-swarming engines

Prior to FenxLabs, the expert was the Senior Solutions Specialist - Azure - Data and Artificial Intelligence at Microsoft, leaving in June 2023. Reporting to the Regional Solutions Lead, the expert was responsible for driving customer adoption and digital transformation through the delivery of Azure solutions across Data Platforms, Advanced Analytics, Internet of Things, Machine Learning, and Cognitive Services. They managed the entire project lifecycle from ideation to execution, collaborating with cross-functional teams to facilitate deployments that met complex enterprise business objectives.

The expert can speak to Large Language Models, artificial intelligence strategy, and the procurement and capacity planning of Graphics Processing Units and data centre infrastructure, including server configuration and high-speed networking. They have implemented and designed AI cluster software stacks involving Kubernetes, Slurm, Ray, and custom orchestration layers. Furthermore, they are an expert in the day-to-day operation of production clusters, maximising hardware utilisation, and utilising digital twin modelling for performance and capacity "what-if" scenarios.

View More

INTERVIEW TRANSCRIPT

**AI Interviewer** [00:00:00]
Thank you for taking the time to speak with me today. To start, could you please describe your professional experience and how it relates to Crusoe Energy Systems Inc?

**Expert** [00:00:09]
I am the founder of FenxLabs, which is an applied AI lab that both custom trains models and does inference strategy on behalf of customers, along with what we can describe as an AI middleware stack that we implement with customers along with the custom model training. We are former customers of Crusoe. We were customers right up until, I want to say February, March this year, when we started migrating out of Crusoe, mostly related to concerns around their behind-the-meter power generation and the way that they power their data centers. We had been running with them for the better part of two years preceding the exit.

---

**AI Interviewer** [00:00:45]
What specific products or services were you using with Crusoe during that time?

**Expert** [00:00:50]
We were using the neocloud or the cloud side of their business, meaning that we would be running in their modular data centers, which were set up next to their gas flaring power generation setup. As a wider consideration and risk management for operational purposes, we obviously went through Crusoe in depth when we did the risk management side of things late last year.

---

**AI Interviewer** [00:01:09]
What was the primary use case driving your compute needs on Crusoe's platform?

**Expert** [00:01:14]
Primarily custom model training and some inference, primarily running bare metal, so directly on their GPUs. For training, we really didn't have any choice but to run on their bare metal setup. That workload is inherently a bursty workload, which means that we would need a sufficient quantity of GPUs running for, say, anywhere from two weeks all the way up to eight weeks. For inference, it's a little different, but we still use their bare metal for this, but the risk is less simply because we can orchestrate more and load balance across other neoclouds as well. The primary risk assessment was around the training workloads that we ran with them.

---

**AI Interviewer** [00:01:51]
What was the scale of your GPU footprint with Crusoe at peak usage?

**Expert** [00:01:58]
We would provision up clusters for each individual project. Over the course of a year, that fleet in the aggregate could be a few thousand GPUs with Crusoe. Each individual project, I would say the most that we ever provisioned with them was around 200 GPUs. Obviously, this scales with the size of the model that we are training. There is a difference between training an 80 billion parameter model and, say, a one trillion parameter model, or even in the mid hundreds of billions parameters. Yes, inherently bursty workloads and in the aggregate, quite a few, but per cluster tended to be below 200.

---

**AI Interviewer** [00:02:36]
Were you involved in the vendor selection and procurement decisions when Crusoe was chosen and when the decision was made to migrate away?

**Expert** [00:02:44]
Yes. I was the final decision maker on that, along with my technical team.

---

**AI Interviewer** [00:02:49]
What other vendors or service providers were you using alongside Crusoe, and in what capacity?

**Expert** [00:02:56]
We actually have a multi-vendor strategy, which is built into the way that we do our training. We've also developed a hybrid infrastructure mesh that allows us to do workload placements across multiple different vendors. The vendors that we tend to use the most are CoreWeave, Nebius, Lambda, and IREN, as well as Fluidstack for spot-based capacity. Crusoe used to be in that group or cohort of vendors. We, to a certain degree, also use smaller regional players here in Europe, so you can think something like Nebul or Genesis Cloud, depending on sovereignty requirements.

---

**AI Interviewer** [00:03:30]
What drove the decision to build a multi-vendor strategy rather than consolidating with a single provider?

**Expert** [00:03:37]
Mostly the pricing advantage in that approach. Obviously, the GPU per hour pricing can vary wildly. On the cheaper end of the spectrum, if we were to use an H200 or an H100 as a baseline, that range can be anywhere from $2.50 all the way up to $8. Because our workloads largely depend on a very limited set of clusters, it's more about where we can source that cluster from for the cheapest price, and then allocate workloads according to the price in the market.

---

**AI Interviewer** [00:04:05]
Curious, where did Crusoe typically sit within that $2.50-$8 range during your time with them?

**Expert** [00:04:13]
I would say that in 2024, Crusoe actually made up a quite substantial footprint within our multi-vendor strategy. I would say that they would have anywhere from 40%-50% of the total workloads that we were running in 2024. This came down to the fact that the behind-the-meter power generation strategy that they settled on allowed them to bring capacity online quicker than their competitors. Back in 2024, we were extremely compute-constrained. As more capacity came online also with newer generations and the way that the pricing developed, that share actually started shrinking sometime late 2024, extending into 2025.

---

**AI Interviewer** [00:04:57]
What was Crusoe's pricing relative to the rest of the market during that period when they held 40%-50% of your workloads?

**Expert** [00:05:05]
Back then, they still commanded a premium. I want to say that was somewhere between $6 and $8 per GPU hour. That being said, that was the price point across the other vendors that had available capacity, with maybe the exception of Fluidstack. The interesting observation about Crusoe was that they maintained lower pricing for longer. Over the last six months, CoreWeave and Nebius in particular have increased their pricing, whereas Crusoe has stayed relatively stable. This is also the defining feature when it comes to price for Crusoe, is that they are consistently on the lower end of the price spectrum.

---

**AI Interviewer** [00:05:45]
How much lower, roughly, is Crusoe's pricing compared to CoreWeave and Nebius today?

**Expert** [00:05:50]
Nebius, I would say that they are close to parity. Nebius is maybe 5%-10% more expensive on average. This also has to do with the way that Nebius virtualizes their bare metal or bare metal virtualization. It isn't a direct one-to-one comparison as such. If I were to do a direct comparison, I would say that Nebius is maybe 15% on just the technical nuance. On CoreWeave, though, that's where the real difference is being felt. If we say that CoreWeave is somewhere below $10 for an H200 GPU, then Crusoe will be around maybe below $4 per GPU hour, which is nearly double for CoreWeave.

---

**AI Interviewer** [00:06:30]
What's driving that gap? Why is Crusoe able to price so much lower than CoreWeave?

**Expert** [00:06:38]
I suppose the biggest key differentiating factor here is the power generation and the way that affects the operational expenses, of which electricity is the largest single item when it comes to the OpEx. Crusoe has a fairly specific strategy where they will do behind-the-meter generation or microgrids, which means that they effectively supply their own electricity. That, combined with the fact that they are running modular data centers, so you can think containers that are essentially stacked on top of each other, specifically retrofitted for GPUs.

That clocks in at a further OpEx saving compared to that of CoreWeave, who are in the process of building mega campuses and retrofitting previously existing mega campuses. That, as well as I suppose the premium that comes in because of the larger anchor tenants that CoreWeave already has. You can think Microsoft, OpenAI, and Anthropic. I would say that those are the likely cost contributors to the difference in price.

---

**AI Interviewer** [00:07:36]
What's the strongest case a skeptic would make against Crusoe's behind-the-meter power strategy actually being a durable cost advantage?

**Expert** [00:07:43]
On the other side of the cost savings attached to Crusoe's particular approach to this, there is also the operational risk, which carries its own, I suppose, cost footprint that will look different from customer to customer and depending largely on what workloads is being run in Crusoe. You can say that if there is on-site disruption in the power being generated, say that you have a well collapse or something like that, then basically what happens is that you've got anywhere from three, maybe seven days with the latest battery upgrades that they've done, which is an extreme risk, especially if you're running training workloads where you run the risk of significant portions of that training run not being completed.

For us, the operational risk and the cost attached to that risk was the big thing that we assessed when it comes to Crusoe. How durable their power generation strategy is in the long term, aside from risk, is obviously that, I suppose, they rely on stuff like fuel cells and other types of power generation methods that are inherently vulnerable to supply chain disruption, especially around precious metals that are being processed in China. If the geopolitical side of things starts deteriorating even further, then that would obviously reflect on Crusoe's or increase those costs more broadly, which would have to force them to drive that cost up, which is another deficit of running behind the meter, is that you rely on a much more fragmented ecosystem than if you are connected to the grid.

---

**AI Interviewer** [00:09:04]
You mentioned the power disruption risk was a key factor in your decision to migrate away. How long did a typical disruption last when you experienced one, and what was the actual cost impact to your training runs?

**Expert** [00:09:18]
They had an outage last year. It is unconfirmed whether or not that was power-related or cooling-related. Based off of the telemetry that we have access to, we assume it was a cooling failure, but the cooling failure more or less directly maps on to what happens if you have a catastrophic failure in the on-site power generation. We treated those two as one-to-one in terms of the net effects for us. As we were running a training workload at the time, the big thing that we noticed was migration of workloads, which is something that their back-end auto-scaling system does automatically.

In that process of migrating customers for failover purposes, our performance suffered. The actual capacity was not being delivered as stipulated, which meant that we had to scrap a significant part of the training workload we were running with them. I would say that the total cost of that was probably in the $60,000-$80,000 range, even though we were able to mitigate some of that by rescuing snapshots and reworking from that and deploying on a different vendor.

---

**AI Interviewer** [00:10:18]
How did Crusoe respond when you raised that issue with them?

**Expert** [00:10:22]
Their basic premise, as it relates to this particular outage, was that because they managed to migrate or do failover migration as was stipulated in their SLA, we were not covered and not entitled to any damages. I would say that from a legal perspective, they had everything in the clear on the legal perspective, especially with their SLA. The problem for us was that obviously, we suffered performance degradation, which is very difficult to capture in an SLA. Crusoe was not willing to reimburse us for the losses even though we could very clearly show that that performance degradation resulted in a loss. Basically, it's an edge case that didn't fall into their SLA, which further exacerbated our relationship with them because their SLAs are then not effectively good enough to cover our use cases in case something happens.

---

**AI Interviewer** [00:11:12]
How did that experience shape the terms you sought from other vendors when you migrated?

**Expert** [00:11:18]
The terms are relatively homogenous across the board for the other vendors. Same basic setup. You have an SLA, everything that is covered by that SLA is eligible for damage recovery. Everything that's outside of that typically will not be covered, and that includes performance degradation, because performance degradation is not covered in uptime. They are two very different things. I would say that the mitigation strategy from our side had to change. We now pay a lot closer attention to the performance metrics and telemetry over time than what we did before. Any vendor that is displaying signs of performance degradation are being audited very carefully before we deploy training workloads on them.

---

**AI Interviewer** [00:12:02]
Got it. Let's move to demand trajectory. How has your overall spend on neocloud GPU compute trended over the past 12 months?

**Expert** [00:12:11]
It has increased considerably. I would say probably a 20%-30% increase, and probably closer to a 40% increase if I include inference, but that is mostly driven by agentic workloads.

---

**AI Interviewer** [00:12:24]
What's driving that increase on the training side specifically?

**Expert** [00:12:29]
Generally speaking, more demand for custom models. That means models that have been trained on proprietary data and knows stuff like industry and the company in more detail than a large generalized model. I would say that the market is by and large catching up to the fact that custom training your own model is a more cost-efficient and quality-aware approach to deploying AI and adopting AI more broadly.

---

**AI Interviewer** [00:12:53]
How do you expect that spend to trend over the next 12-24 months?

**Expert** [00:12:59]
I expect that trend to continue growing. We still haven't reached the part of the adoption curve where this is widely known. I would say that we are still very much in the early adopter phase of custom model training. I foresee that changing over the next 24 months with more demand for custom models, which will require more compute.

---

**AI Interviewer** [00:13:19]
What would have to be true for that growth not to play out the way you're expecting?

**Expert** [00:13:24]
I would say that there would have to be a breakthrough in the way that these models are built that would allow them to conduct stuff like RAG or other types of contextual knowledge operations, which is the big ball next, in a more generalized way. I rate that chance as fairly low by the virtue of how these systems work as probabilistic systems. when you look at them as probabilistic systems, the goal is often to skew those probabilities as much as possible in favor of something that is relevant or workload-relevant or company-relevant. I see that chance as fairly low.

---

**AI Interviewer** [00:13:57]
Let's move to switching costs. When you migrated away from Crusoe, what was the actual effort involved in moving those workloads?

**Expert** [00:14:06]
Mostly engineering time. They don't really charge egress costs the same way that hyperscalers do. If they did, that would make everything a lot harder. There wasn't a lot of, I suppose, direct costs outside of engineering and human costs to us, because this did just suck up quite a bit of resources on our end, where we needed to dedicate engineers for roughly a month, a month and a half, to just do this migration and also retire Crusoe as a vendor within our hybrid infrastructure mesh.

---

**AI Interviewer** [00:14:35]
How many engineers were involved in that migration, roughly?

**Expert** [00:14:40]
I would say 11 engineers. This is actually quite a significant resource consumption for us because we are around 50 FTEs. Roughly 1/5th was required to, number one, map out the plan and executing workloads on Crusoe, figure out where to migrate them based off of size and complexity, and then do the actual migration before continuing with the project itself. Several steps were included in that resource drain from our side.

---

**AI Interviewer** [00:15:08]
Given that level of effort, what would it take for a customer with a larger footprint than yours to justify switching away from Crusoe?

**Expert** [00:15:18]
It depends on how locked in they are, is the basic premise. If they are fully locked in and only use Crusoe as a single vendor, then that operation becomes fairly complex. Number one, you need to handle the agreement structure going out of Crusoe. If that is a long-term take-or-pay contract, then you need to consider stuff like break clauses and also the economics associated with breaking the agreements. This is mostly commercial, but it adds extra time and extra complexity.

You need to find a vendor that can provide you with the correct accelerated generation and the sufficient number of accelerators. You need to renegotiate the price for those accelerators, and then you can start thinking about the technological aspects of it and how you actually do the migration. I would say that depending on how locked in you are from a vendor perspective, that will largely dictate the complexity attached and by extension, the cost attached to migrating away from Crusoe.

---

**AI Interviewer** [00:16:17]
What share of Crusoe's customer base do you think operates on long-term take-or-pay contracts versus more flexible arrangements?

**Expert** [00:16:25]
It depends on whether we count the anchor tenants or not. The anchor tenants in this case would be hyperscalers. It would be frontier model laboratories. In particular, Oracle is in deep with Crusoe. It largely depends on the anchor tenants. The anchor tenants with the current market situation tend to make up anywhere from 60%-80% of the overall customer concentration.

---

**AI Interviewer** [00:16:52]
What proportion of Crusoe's remaining customer base outside those anchor tenants do you think is on flexible versus committed arrangements?

**Expert** [00:17:00]
I would say that probably 60%-70% are on more flexible arrangements. That would range from small startups all the way down to individual developers in need of GPUs. Enterprises tend to go with the take-or-pay contract. I would say probably the remaining 30% would be on longer-term take-or-pay, if we exclude, obviously, Oracle and Jane Street, which are the two biggest anchor tenants.

---

**AI Interviewer** [00:17:28]
Got it. Let's move to product and service quality. Outside of the outage you described, how would you characterize Crusoe's service quality relative to the other vendors in your stack?

**Expert** [00:17:41]
I would characterize it as fairly good. They were able to supply us with the number of GPUs that we needed, along with, call it, a reasonable pricing on the hourly GPU rate, which in the aggregate was very competitive against the other vendors. As a matter of fact, I would go as far as saying that if it wasn't for the operational and structural weakness tied to behind-the-meter power generation, they would probably still be a vendor that we would use. That experience we had last year was a real eye-opener to us in terms of the operational risks attached.

---

**AI Interviewer** [00:18:15]
How did Crusoe's uptime performance compare to the other vendors in your stack over the full two years you worked with them?

**Expert** [00:18:23]
Discounting the bigger outage events that I mentioned earlier, which even doesn't really count as an outage as such, it's a performance degradation. Aside from that, I would say that uptime and performance over the two years that we were with them was actually very good and very comparable to Nebius and CoreWeave in quality.

---

**AI Interviewer** [00:18:41]
How would you quantify that? What uptime percentage did you observe with Crusoe versus the others?

**Expert** [00:18:49]
The SLA covers, I believe, a 99%+ uptime, and that is also broadly in line with what we've experienced. What that means is, effectively there are no outages outside of the ones that are announced, and they would typically announce this anywhere from two weeks to a month ahead of time.

---

**AI Interviewer** [00:19:06]
How did that compare to CoreWeave and Nebius on the same metric?

**Expert** [00:19:11]
They have, broadly speaking, the same metric. Because of the size and scale of both CoreWeave and Nebius, the big differentiator is the capability of their support apparatus, which is a lot more robust than Crusoe. That is also because Crusoe at the time was somewhere right in the middle of a neocloud and a crypto miner. I think that they, since we left, have divested their crypto mining operation, which means that they theoretically should have more capacity to focus on customer engagements. That could have corrected since we left. Definitely support was slower and less overall quality on the support item than compared to CoreWeave or Nebius. For us as a technical organization, that wasn't really a big deal breaker either way.

---

**AI Interviewer** [00:19:58]
Got it. Let's move to competitive dynamics. When you were evaluating alternatives to Crusoe, what was the primary reason you landed on the vendors you did rather than others?

**Expert** [00:20:10]
You can say that our multi-vendor strategy has been built over the course of two or almost three years at this point. Throughout that development of our multi-vendor strategy, the general through line is that vendors have been added based off of capacity, so do they actually have the sufficient numbers of GPUs? Based off of that, ranked by price. I would say that the current vendor list as such has been built in a very modular way, but it maps on fairly well to when they would have the capacity to actually sell us.

---

**AI Interviewer** [00:20:40]
What would it take for Crusoe to reenter your vendor stack?

**Expert** [00:20:44]
The one big thing would be grid connection. Even though the microgrid strategy looks sound on paper, the extra security that would come from having an actual grid connection would definitely make us reconsider taking them back into our stack.

---

**AI Interviewer** [00:20:58]
Are you aware of any moves Crusoe has made toward grid connectivity, or is that purely hypothetical from your vantage point?

**Expert** [00:21:06]
From my vantage point, that seems like a bit of a pipe dream at the moment. They seem to be doubling down into, in particular, microgrids and the flaring strategy that they started out with. As if that is not enough, I think that they also recently announced that they will try and bring small modular reactors, so nuclear reactors, online to power data centers by 2028. I am skeptical to that claim because the earliest I can see small modular reactors happening will be sometime in the early 2030s, so I'm not sure how they're going to bring that forward.

As if that's not enough, they are also talking about data centers in space, with, I think, the company called Starcloud. It seems like they're focusing on really anything else and anything that is hype-driven rather than actual grid connections. I think that when they look into the crystal ball, they see the same thing as I do, which is that in most major markets, the grid connection or grid interconnection time can stretch anywhere from five to 10 years. When we also add in the supply constraint of electrical equipment more broadly and also grid upgrades, especially in their U.S. operations, it doesn't seem to me like they have any big plans of going for grid interconnected data centers.

---

**AI Interviewer** [00:22:23]
How does that trajectory affect your view of Crusoe's ability to win and retain larger enterprise customers who might have stricter uptime and reliability requirements than you do?

**Expert** [00:22:34]
I think that that is going to be a hard sell for them. The only way that I can see this becoming feasible or realistic for them to target enterprise customers, and especially enterprise customers that have, for one reason or another, very strict uptime or uptime risk management routines. I think that this will be an uphill sell unless they manage to bring online small modular reactors. Again, I think their timeline for this is very optimistic.

---

**AI Interviewer** [00:23:02]
On that point, there is a view that Crusoe’s managed services and software layer create enough stickiness to retain hyperscaler-level customers, even if the power setup carries more risk. How do you see that playing out?

**Expert** [00:23:17]
It depends on how we define hyperscaler-level customers. If we are thinking about enterprises that have an IT estate that is somewhat similar to that of a hyperscaler, I don't know who that would be, but say that we are talking about that caliber of customers, then maybe. It depends on how technically proficient they are. For the hyperscalers themselves, though, if you are an actual hyperscaler or even a frontier model laboratory, I would say that the ecosystem, number one, is not why they go to Crusoe. They go to Crusoe for the bare metal compute, and then they will also bring their own orchestration and their own software layer and their own tooling, and just run that on the bare metal GPUs. I'm not sure I'd buy that statement as is.

---

**AI Interviewer** [00:24:02]
What evidence would change my mind on that? What would you need to see to believe the software layer is actually driving retention?

**Expert** [00:24:11]
I think the biggest, greatest signal would be if their customer footprint starts growing over that of the other neoclouds. Because if that starts happening, then it would be safe to assume that that is because something is creating the underlying stickiness, and that is also appealing enough to get customers to move to Crusoe. Seeing as the software stack is really the only discernible moat that I can see, then it would be reasonable to infer that that is because of the software ecosystem. Again, I have a hard time seeing this being the case at this moment in time.

---

**AI Interviewer** [00:24:43]
Got it. Let's move to pricing power. You mentioned Crusoe has stayed relatively stable while CoreWeave and Nebius have increased pricing. How much room do you think Crusoe actually has to raise prices from here?

**Expert** [00:25:00]
I actually think that they have some room to do this. I don't think they have the same ability to charge a premium as a CoreWeave or Nebius. I don't think that they could get to, say, $6 per GPU hour, simply because of that lacking grid interconnection and a lot of CIOs and CISOs and CTOs would likely buckle at the pricing if that got similar to that of a CoreWeave, given the behind-the-meter power generation.

Broadly speaking, given that the market is still constrained, I would say that there is probably room for them to increase prices by, say, at least 10%, maybe 15%-20%, if they really wanted to. I also think that, strategically speaking, if in order to maintain or even grow business, keeping pricing at the current level is beneficial for Crusoe, because they come out ahead as one of the cheaper alternatives on the market.

---

**AI Interviewer** [00:25:52]
How has Crusoe’s pricing actually moved over the past 12-24 months? Have they raised, held, or reduced prices during that period?

**Expert** [00:26:02]
I would say that they've been relatively stable. There's been a slight increase, so you can think in a few cents per GPU hour. That is I would say broadly stable within $0.03-$0.05.

---

**AI Interviewer** [00:26:17]
Got it. Let's move to forward-looking risks. Outside of the power generation concerns you've already described, what do you see as the single biggest risk to Crusoe’s business over the next two years?

**Expert** [00:26:31]
It is the financials of the company, and more specifically, the SPVs and the raised debt in order to finance the build-outs that are the specific sticking points. This is a big concern across the industry. Crusoe have been for some time employing the same strategies as the other neoclouds. The problem with this is that it's hard to tell what their exposure is compared to the other neoclouds in this category, especially when it comes to the use of special purpose vehicles, which means that debt and liabilities aren't necessarily showing up in their balance sheet. That, along with the fact that in, I believe it was, Wyoming, one of their projects was put on hold earlier this year.

They haven't disclosed who that customer was, but the fact that they've been put on hold suggests to me that there are several risk factors here outside of the financing. I would highlight the customer concentration. Big anchor tenants versus a durable customer mass that can carry, say, a dropout of an anchor tenant. The fact that that is also missing, or that seems to be a big part of the overall arrangement here, also is something that I consider as a big risk.

---

**AI Interviewer** [00:27:39]
On the Wyoming project specifically, what's your read on what caused that hold? How representative do you think that is of broader demand risk for Crusoe?

**Expert** [00:27:49]
This is very difficult to say without knowing who the customer in question there was. If that customer was, say, Anthropic or one of the other major frontier model laboratories, then I would say that this is a big signal to the AI industry as a whole, because that means that the compute demand from the frontier model laboratories are decreasing in nature. However, if this customer was a hyperscale anchor tenant, then that is also a broader warning sign to the wider industry, because what that means is that demand from hyperscalers are decreasing, which in turn means that either they are bringing online more capacity that they operate directly or some other major shift. It largely boils down to who that anchor tenant is before you can infer the consequences of this stalled project.

---

**AI Interviewer** [00:28:35]
Stepping back from that specific project, how do you assess the risk that one of Crusoe’s major anchor tenants, like Oracle or Jane Street, reduces or exits their commitment?

**Expert** [00:28:46]
Jane Street is hard to tell. It has been reported that they are training some models for their own quant operation, which I find to be probably more sustainable because there is an actual use case and an actual incentive from Jane Street to continue developing these models. For Oracle, though, I assess the risk as much greater. The underlying problem with Oracle is that they have based their build-out, also subsequently the partnerships and the special-purpose vehicles that they're building capacity under on frontier model laboratory commitments, in particular, OpenAI.

There are signs now that the frontier model laboratory, especially with, call it, Anthropic's S1 filing, there are significant questions of whether or not the frontier model laboratories have the financials to actually support the commitments that they've made. If it turns out that they do not have the financials or the economic prospects to service these agreements, then that would be a catastrophic outcome for Oracle, because there is ostensibly nowhere else or nobody else that can absorb the capacity that Oracle is currently building to replace the frontier model laboratories. I would say that Oracle is probably the bigger risk or the more riskier, I suppose, relationship out of the two.

---

**AI Interviewer** [00:29:58]
How exposed do you think Crusoe is to an Oracle pullback specifically? What share of Crusoe's revenue do you think flows through that relationship?

**Expert** [00:30:09]
It's hard to say revenue-wise, but this would ostensibly be tied to Oracle's Stargate project in Abilene. There are already signs that the Abilene project as a whole is at risk in that I think the original number of campuses that was supposed to be built was five. To date, only one has been built, and there is even question as to how operational that one campus is. I would say that the Oracle relationship is already looking a little risky from my perspective.

---

**AI Interviewer** [00:30:37]
How do you see the long-term sustainability of Crusoe's software-enabled managed inference offering as a revenue stream compared to their core commodity GPU rental business?

**Expert** [00:30:47]
When it comes to inference clouds or managed inference, I suppose services more broadly, they are cropping up left and center, and this is becoming a very crowded space. You can think you have a Fireworks, a Baseten, the other neoclouds also have similar inference cloud solutions, in particular Nebius. I would say that it's hard to forecast. It depends on whether or not Crusoe is able to create a sustainable moat around the inference or the inference cloud. In that sense, they are in the same boat as all the other vendors, which also needs to do the same thing.

I think that the bare metal or raw GPUs is likely where the underlying value is going to come from also in the future, simply because when we make that transition away from, call it, the frontier models the way that we know them today into, call it smaller, more specialized models. The compute that this is hosted on is actually more valuable than, I suppose, the managed inference and model access more broadly.

---

**AI Interviewer** [00:31:49]
On the question of Crusoe building out gigawatt-scale projects, how do you see the risk that developers or customers get disintermediated as Crusoe moves toward larger vertically-integrated deployments?

**Expert** [00:32:01]
It depends. This is too early to tell. First of all, the vertical integration would have to happen, and then we would need to know something about the customer composition before I can accurately answer that question.

---

**AI Interviewer** [00:32:15]
What would you expect to observe in the market if that disintermediation were actually happening?

**Expert** [00:32:20]
That's a good question. Could you define what you mean by disintermediation for me?

---

**AI Interviewer** [00:32:26]
What I mean is, as Crusoe moves toward building and operating very large-scale data centers, potentially with anchor tenants consuming most of the capacity, smaller customers like developers or startups might find themselves squeezed out or deprioritized. What signals would you look for to know if that's starting to happen?

**Expert** [00:32:47]
The simple answer to that is revenue mix. Obviously, we don't know today what their revenue mix is, but based off of some public data sources, I would look at where individual teams and developers are consuming model capacity from. You can think something like an Artificial Analysis. I would look for Crusoe as an endpoint. If that share shrinks, then it's safe to assume that Crusoe’s priorities will be geared more towards enterprises and large anchor tenants.

---

**AI Interviewer** [00:33:15]
Looking ahead, what's the single biggest risk to Crusoe’s position in the neocloud market over the next two to three years that you haven't already mentioned?

**Expert** [00:33:26]
I would revisit the financial risk, because it seems that Crusoe is the one with the least diversified customer portfolio in terms of anchor tenants. Also, the financial risk that their onboarding seems to be increasing, especially that Oracle relationship. I would keep a very close eye on the financials of Crusoe in terms of risks and liabilities, especially attached to debt.

---

**AI Interviewer** [00:33:50]
Thanks for your insights today. I enjoyed our conversation and appreciate you taking the time to share your expert perspective. Have a great rest of your day. Goodbye.
