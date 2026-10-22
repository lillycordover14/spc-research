---
theme: "Automotive & Mobility"
title: "Former CTO at Torc Robotics Believes Simulation Tools Are Key for Early-Stage Autonomous Vehicle Development but Face Market Maturity Challenges"
doc_id: EC-1000000-212564
source_line: "Applied Intuition · Expert Call · Customer · 06 Aug 26"
date: 2026-08-06
company: "Applied Intuition TM"
pages: 2 of 6
saved: 2026-10-19T17:47:32.147Z
url: https://research.alpha-sense.com/search?search_id=tmp-dpwh5s830wf1fshuzdr6bp&sort=DATE&order=DESC&docid=EC-1000000-212564
---
# Former CTO at Torc Robotics Believes Simulation Tools Are Key for Early-Stage Autonomous Vehicle Development but Face Market Maturity Challenges

Company Deep-Dive

DATE PUBLISHED

06 Aug 2026

INTERVIEW DATE

08 May 2026

EXPERT PERSPECTIVE

Customer

ANALYST PERSPECTIVE

Investor-Led (Buy-Side)

PRIMARY COMPANY

Applied Intuition TM

SMART SUMMARY

Summary

The interview covered the expert's experience with a leading simulation and validation tool for autonomous vehicles, discussing its use cases, product strengths and limitations, customer support, and the company's evolving business strategy.

EXPERT BACKGROUND

- Former Chief Technology Officer at a leading autonomous trucking company, responsible for all engineering and product, with direct experience integrating and managing simulation and validation tools for autonomous vehicle development.

EXPERT SENTIMENT

- Believes the simulation product is highly polished and easy to onboard, but sees its market as plateauing due to a lack of new autonomous vehicle startups and the tendency for larger or more advanced companies to build their own solutions.
- Views the company's expansion into new software and defense markets as a logical growth path, but questions whether the core simulation tool can avoid being outgrown by customers as they scale.

TAKEAWAYS

- The expert's former company used the simulation engine primarily for object detection and replay, leveraging their own data and models, but did not use the sensor simulation due to insufficient fidelity.
- The simulation product is cloud-based, easy to integrate, and offers strong customer service, making it attractive for smaller companies or those not building full autonomy stacks in-house.
- Larger OEMs and advanced autonomous vehicle developers typically build their own simulation and validation environments, using commercial tools like this only for early-stage or integration purposes.
- The company is expanding beyond simulation into development tooling, infotainment, embedded stacks, and the defense sector, but the core simulation business appears to be reaching maturity.
- Contracts with the company can reach tens of millions per year, and the company is willing to provide significant on-site support for large customers.

AlphaSense Smart Summaries are AI Generated

Introduction and Background

Client's Relationship with Applied Intuition

Product Features and Usage

Market Position and Competitors

Future Opportunities and Closing Remarks

EXPERT BIO

Former Chief Technology Officer at Torc Robotics, a customer of Applied Intuition TM. Expert can speak to being a key decision maker and a paying customer of Applied Intuition, with extensive experience in using their products.

Former Chief Technology Officer at Torc Robotics. The expert is responsible for leading and driving the unification of all of Torc’s product development efforts to align with the company’s roadmap and key milestones for the commercial launch of Torc’s autonomous truck solution.

The expert is a customer of Applied Intuition.

View More

INTERVIEW TRANSCRIPT

**Client** [00:00:00]
Thanks for taking the time to chat. Maybe to give you a little bit of context, we're doing a little bit of research on Applied Intuition. Maybe just start with a quick background on you and your current role.

**Expert** [00:00:14]
My current role, I run software factory for Ford Motor Company. Basically anything you build, validate, release, and deploy out to vehicles comes through my organization.

---

**Client** [00:00:26]
Got it. Sorry, what company was that?

**Expert** [00:00:30]
Ford Motor Company.

---

**Client** [00:00:32]
Okay. Were you at Torc Robotics before?

**Expert** [00:00:37]
Yeah. I was the CTO there up until last year.

---

**Client** [00:00:41]
Sorry, that's what the profile was listed as, so I was just a little confused by that.

**Expert** [00:00:46]
Yeah. I just switched in January, so they might have my old one still on there.

---

**Client** [00:00:52]
Got it. You're a customer of Applied at Ford, or were you a customer when you were at Torc, or both?

**Expert** [00:00:59]
I was at Torc. I don't use them. Ford might use them, but I don't use them at Ford.

---

**Client** [00:01:06]
Got it. What were you responsible for at Torc?

**Expert** [00:01:09]
All engineering and product.

---

**Client** [00:01:12]
Got it. Maybe we just start with quick background, I am not too familiar with Torc, so quick overview of the company, and then we can get into to Applied if that works.

**Expert** [00:01:23]
Yeah. Torc is a company majority-owned by Daimler Trucks. They build L4 autonomous trucks for hub-to-hub trucking, so L8 semi-trucks.

---

**Client** [00:01:34]
Got it, so building autonomous trucks. Sorry, were you saying something?

**Expert** [00:01:41]
Nope.

---

**Client** [00:01:42]
Okay. The relationship with Applied, can you maybe say when you guys became a customer, and what drove that?

**Expert** [00:01:50]
They were a customer of Applied before I joined about three or four years ago. Applied was for all their simulation. They're easy to onboard. They have a physics-based engine that allows them to do all the object simulation and all the replay, so that's what they onboarded them for. We continued to use them because we weren't large enough that I'd want to build my own when I was there, and we kept integrating. We did not take on their new stacks. We stayed with their, I forgot what they're called, but basically their object replay and the detection replay. We didn't do any of their sensor simulations because they didn't have high enough fidelity for what we were looking for.

---

**Client** [00:02:33]
Got it. Can we maybe go through the different parts there? It sounds like there's object sim, sensor sim, a few others. It would be helpful just to talk through these one by one to help me understand the products a little bit better. Maybe we start with what you guys were using because that's what you'll be most familiar with. What modules of the product were you using?

**Expert** [00:03:01]
Yeah. I don't know their official naming of it because that's their product names, and they were always branding that. We basically would take in, we'd pull all of our sensor data and all of our information, and we would replay it. We would put in and run object detection and replay through theirs so that we could run our ego simulation. We did the basic trajectory planning, object detection, replay, and simulation on that, based on after we put our models into it.

---

**Client** [00:03:32]
Got it. When you say simulation, is that the creation of synthetic data, or what does simulation actually mean?

**Expert** [00:03:40]
Simulation is using the synthetic data. We actually created and generated our own synthetic data, or we gave data that we recorded. They were the engine that allowed us to build a world and replay it. All the data was Torc, and we used their simulation engine. They built up an engine. If you're looking at a gameplay, it's like real Unreal Engine for a graphics display, but they built a physics-based engine, so that was real.

Basically, you could actually do all your trajectories and all that planning and built it out so they had their proprietary language that you could put all your models and all your data in, and then you could reconstruct, and then you could build different scenarios and all that inside their system and then run it, but you would feed it with your own data set and structure.

---

**Client** [00:04:27]
Okay. Is this a software application that runs on a computer, or do you need to push it to something else?

**Expert** [00:04:34]
No, it runs in the cloud. It's a high-end compute. We ran ours in AWS, and we ran large cycles of it so that you could run and revalidate all your models and all, so all the training we would do of our model, and then we'd put it up into their simulation so we could get results, whether it's regression results, testing failure points and pain points, and all that.

---

**Client** [00:04:59]
Is it very different customer to customer? If you're a customer, and let's say, Ford Motors is a customer, are you guys using very different products, or is it pretty much the same thing?

**Expert** [00:05:09]
No, they have multiple different product suites, but if you're using their simulation, almost everyone's using the same type of simulation base, that's why you use them, because they built it up and then you just use them instead of building yourself, so you don't have to pay for the full development cycle for that physics engine. Now, big companies like a Waymo or Cruise, they would've built their own simulation engines. Even when I did it the first time I was at Ford, that became Argo AI, we had built our own simulation engine instead of using someone else's.

---

**Client** [00:05:44]
That makes sense. That's one product. Do you remember the name of that product?

**Expert** [00:05:50]
No, I don't remember exactly what it was called. If you look at it, they have a simulation portfolio, and you look at that, and that's what it would be called. I forgot the different moniker that they used for it, because we were well into the lower level, into the integration part, so I didn't pay attention to the marketing stuff, because we were already using it.

---

**Client** [00:06:12]
Got it. That sounds like that was object sim, and then you mentioned there's sensor sim or sensor simulation.

**Expert** [00:06:19]
Yeah. They actually were trying to build out and model real-world sensors and get the data from the sensors. You have to basically a model of the sensor so it could then take in raw data and then spit out what a sensor would see. They were in the middle of doing that. We never saw anything that showed that it was high enough fidelity that we would want to do that, so we would just feed in our own detected objects into their stack.

They also had that sensor simulation where you basically take real-world images and videos and just play it into it, and then they would have a model set up for the different types of sensors from different companies, whether it was LiDAR camera, whatever, and then they would do detections on it, so you would get what you would see out of those sensor suites. We didn't use it.

---

**Client** [00:07:07]
What did you guys use instead?

**Expert** [00:07:10]
We did our own. Basically, their fidelity didn't target what we were working with. We used our integration with our sensor suppliers, and then we actually did all of our own detections because we actually built those models that we deployed on the sensor stack. Basically, we only replayed and leveraged detected data in their system. All of our simulation and all that stuff was done on real-world testing and replay that we built ourselves based on the CARLA open-source stack.

---

**Client** [00:07:41]
Got it. What was your overall impression of Applied and the Applied team, quality of the product and whatnot?

**Expert** [00:07:48]
Their quality's pretty good. It's very polished. They're very product-centric. They're a good sales organization. They're starting to hit probably their plateau in that sim market because there's not a ton of new start-ups in autonomous vehicles, so they're expanding. They do a lot of work in dev tooling and that kind of stuff. They had partnerships with some European OEMs that they were always trying to bring that tool set and tool chain back to us.

They acquired a company called Embark, which was an autonomy stack, and they're also trying to offer some of that that they do with Isuzu. They've announced it and built out, so they're always trying to extend what they were doing, but their core value in the AV space was always tied to their object sim.

---

**Client** [00:08:35]
Got it. What do you think of their full autonomy stack approach?

**Expert** [00:08:41]
I don't think they'll build you a full part in the offering that they do. It is really expensive to bring it in, and then you do not own the IP. They are not giving you a differentiation in cost reduction. I don't see them providing a full stack because they do not want to take the liability and that stuff on. They're in that middle ground. Maybe they will eventually build out some middleware or OS middleware combination platform, but they did not have any plans on that.

Their integration and what they were doing with Isuzu was almost like a purchase service contract. I did not see it scaling or being beneficial to others in the space. For those types of interfaces that aren't building up their own stacks or looking to shortcut that, it might be used, but there's not really a market for that, because if you're going to do it, I would be looking to go to a full stack provider, something like what Waymo does to some or others like that.

---

**Client** [00:09:37]
Yeah. What's different between what Applied does and what Waymo does?

**Expert** [00:09:43]
Waymo will deliver all the way through the full stack. They will do all the object detection, all the path planning, all the prediction, the entire algorithm and the entire stack. Think of it as they do not only sensing, but they do understanding, and then they also do the path planning and actually setting the path and driving the vehicle. They do the motion control and everything, whereas the Applied stack was just giving you the foundation to do the sensing, which is the very first part. They were only coming in to do the core piece to get the understanding of the world, but it wasn't actually applicable to sensor suites.

It wasn't then doing the prediction models for not only your ego vehicle, which is your vehicle, but all the other vehicles, humans, and anything that you're tracking. They weren't doing prediction models on that. That's really where you separate if you can do AV or not, and then that's how you also create and generate synthetic data. They talked about it, but they never, ever had a data set that they could share. They were always using every customer brought their own data set. That would have been the advancement that they could have separated themselves, but I haven't seen any other synthetic data unless it changed in the last three months. They didn't have it on their roadmap, and it wasn't part of this year's plan.

---

**Client** [00:11:05]
Got it. At Ford, what do you guys use there for this?

**Expert** [00:11:10]
We have our internal, we have our own because of our company called Latitude AI. They built out their own sim, and they have their own validation and sim environment that we run and drive for all of our ADAS suites.

---

**Client** [00:11:23]
Do you think most OEMs will do that over time?

**Expert** [00:11:27]
Right now, I believe most OEMs already do that, unless there are some that are trying to churn it out. I don't believe all OEMs will do it. I think the OEMs that are investing and wanting to build it in-house will do it. The ones that are just looking to buy an L2 plus L3-type system, eventually an L4 system from a supplier, would use something like Applied Intuition because they could easily throw it in there and do their pseudo checks, their integration checks, those types of things. They would be able to see it because they are not actually building the models themselves. There is two worlds.

The ones that are building an AV stack and building all those models and that prediction and path planning and path following algorithms won't want to use Applied Intuition long term, unless they're really small like were as a start-up. That's where Torc started using them, but we were already in the process of migrating away from them because they were going to get not cost-effective for the scale and size that we needed to, and they didn't solve all the needs that we needed to build the entire stack.

---

**Client** [00:12:32]
Got it. How much per year were you guys spending on Applied?

**Expert** [00:12:37]
I want to say it was tens of millions.

---

**Client** [00:12:40]
Are there alternatives in the market? That's obviously a lot to be spending. I'm curious how you thought about that.

**Expert** [00:12:47]
There are. They're the most complete, so they're the easiest to stand up and use, and they have the best customer service and sales org. They have a really good sales engineering force, so they're easy for a lot of folks that don't know or want to invest some time. There's companies like Foretellix that's integrated into the NVIDIA platform. NVIDIA sells the same environment, but theirs is pretty far behind compared to Applied's.

A lot of the companies and where it's going now is you actually build on top of some open source stacks like CARLA and others. Out of the box, they're very easy. Someone that's just looking to validate and use it, not necessarily build an entire stack, they're very turnkey, easy to use. When you want to scale up and actually develop an entire stack, they don't become cost-effective for that environment.

If you look at some of the traditional OEMs, whether we were in the trucking side but automotive OEMs, the ones that are just outsourcing their services or getting from a supplier like traditional Tier one or others, they're going to use stuff like Applied Intuition because it's very easy to integrate. It's very user-friendly, and you don't have to be an expert in model development to leverage it and get the feedback, and they automate a lot of things out. They have really good customer service. They have probably one of the best customer services in the space.

---

**Client** [00:14:11]
Are they very working with you hand in hand, or is it really a tool that they give you and let you use? I'm trying to figure out how forward-deployed they really are in the process.

**Expert** [00:14:22]
It's both. If you're good, they'll help set it up and let you run it yourself. I was pushing them because I was spending so much money with them. I had a pretty big contract. I was able to say, "Hey, I want blue-green deployment. You cause downtime in my environment. I need faster throughput. I'm looking at spends, and your clustering and how you're setting up the Kubernetes network and all that is not optimized."

I got to push, and they had teams inside my facilities because of that to make sure that they weren't having any downtimes, but it was because we were probably one of the ones pushing and leveraging them a little bit more on their product roadmap and that because they wanted to keep us as a customer. We also spend enough that it justified them putting on-site. I think I had eight their engineers sitting on-site in my Germany office before we closed that, and then they are in Michigan. They're regularly over to our Michigan office that I opened when I was at Torc.

---

**Client** [00:15:21]
Got it. When you think of them as a company long term, what do you think their future opportunity is? What's the case for the business where it continues to do well?

**Expert** [00:15:31]
Qasar and Peter are doing a really good job of looking at how to extend their core tools and enablement business, and that's where you can see them getting into the other software stacks on infotainment development or embedded stacks for the OEMs. That's where they're getting into those AV footprints where they can help out and be that. They know not everyone will go software-centric and deliver all these large stacks. They're doing a good job extending that.

They're starting to get into the defense space. They did some acquisitions in that into the defense space, probably a little over a year ago they announced it, then to aerial and to defense. I think they had a good path and a good structure. I think they're growing in how they deliver that and connect into the ecosystem. What I haven't seen is how they become not just a tool that people outgrow when they really get through the development cycle.

---

**Client** [00:16:28]
Got it. I think this covers most of what I wanted to hit. Anything else you think is important to mention?

**Expert** [00:16:35]
No. Depending on what you're looking, what I would look at is what is their forward-looking contracts in their new space look like. I think their sim is probably pretty plateaued out, but where are their growth opportunities? That's the one thing that I would be interested in in what they're doing, because they had a lot of starter spaces. It would be super interesting to see how those new product lines have growth trajectories, and most of them have been started long enough that they should be able to map that out and show revenue.

---

**Client** [00:17:09]
Got it. Awesome. This has all been really helpful. Thanks for taking the time to chat.
