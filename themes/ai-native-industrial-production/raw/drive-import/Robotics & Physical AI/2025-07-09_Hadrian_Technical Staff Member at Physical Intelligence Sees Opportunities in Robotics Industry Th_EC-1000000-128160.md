---
theme: "Robotics & Physical AI"
title: "Technical Staff Member at Physical Intelligence Sees Opportunities in Robotics Industry Through ITAR Compliance and Teleoperation Development"
doc_id: EC-1000000-128160
source_line: "Hadrian · Expert Call · Consultant · 09 Jul 25"
date: 2025-07-09
company: "Hadrian"
pages: 2 of 18
saved: 2026-10-22T20:10:10.779Z
url: https://research.alpha-sense.com/search?search_id=tmp-zrt1t2a4vvfkburx47q41n&sort=COMPANY_NAME&order=DESC&docid=EC-1000000-128160
---
# Technical Staff Member at Physical Intelligence Sees Opportunities in Robotics Industry Through ITAR Compliance and Teleoperation Development

Company Deep-Dive

DATE PUBLISHED

09 Jul 2025

INTERVIEW DATE

10 Apr 2025

EXPERT PERSPECTIVE

Consultant

ANALYST PERSPECTIVE

Investor-Led (Buy-Side)

PRIMARY COMPANY

Hadrian

SMART SUMMARY

Summary

The conversation covered the challenges and dynamics of sourcing and scaling manufacturing for robotics and defense applications, with a focus on the capabilities and limitations of vendors like Hadrian and Protolabs. The discussion also explored the future of robotics, including the role of generalist AI models, teleoperation, and the importance of hardware-software integration.

EXPERT BACKGROUND

- Member of Technical Staff at an AI robotics company, leading hardware design efforts and previously led a major UAV project at a defense technology firm, with deep experience in autonomous systems, manufacturing, robotics, and AI.

EXPERT SENTIMENT

- Skeptical about Hadrian's current ability to deliver high-quality, aerospace-grade parts at scale, emphasizing that their focus has been more on operational efficiency than on solving core automation and machining challenges.
- Optimistic about the potential for generalist AI models in robotics, but believes that true progress will require significant advances in both data collection and hardware-software integration.
- Believes that American manufacturing can only be revitalized through meaningful automation, not by scaling human labor, and that vertical integration between hardware and software is the most powerful approach for robotics companies.

TAKEAWAYS

- Prototyping and early-stage manufacturing often rely on quick-turn vendors like Protolabs and Oshkosh, but these are not suitable for production-scale due to limitations in quality, scale, and post-processing capabilities.
- Hadrian is positioned as a scalable, efficient CNC factory in the U.S., but has struggled to consistently deliver high-quality, complex parts; their operational improvements have not yet translated into reliable production for demanding applications.
- Cheaper and faster options for less complex parts exist, such as Protolabs or small, relationship-driven machine shops, which offer immediate quoting and clear manufacturing constraints.
- The U.S. supply chain for precision manufacturing is fragmented and unreliable at scale, while Asian suppliers, particularly in Taiwan, offer greater reliability and responsiveness, even when accounting for tariffs.
- In robotics, the expert sees more promise in developing generalist AI models and simpler, task-specific hardware (e.g., robotic arms) rather than humanoid robots, and stresses the importance of vertical integration between hardware and software.

AlphaSense Smart Summaries are AI Generated

Introduction And Expert Background

Prototyping And Vendor Selection

Hadrian's Role In Manufacturing

Investment Perspectives On Hadrian

Future Of Robotics And Automation

EXPERT BIO

Member of Technical Staff at Physical Intelligence. Former Senior Mechatronics Software Engineer at Anduril Industries leaving in March 2024. Expert was an engineer responsible for the design of components to be manufactured with Hadrian and Machina. Expert uses a number of analogous services for CNC machines and sheet metal such as Protolabs and OshCut.

Member of Technical Staff at Physical Intelligence.

Prior, the expert was a Senior Mechatronics Software Engineer at Anduril Industries leaving in March 2024. The expert handled multirotor-based Loitering Munitions. The expert was the first hire in the Mountain View office, seeding new projects in cutting-edge robotics for national defense applications.

The expert was the managing partner at Rough Draft Ventures leaving in 2023.

The expert was an Engineering Fellow at 8VC leaving in January 2021.

View More

INTERVIEW TRANSCRIPT

**Client** [00:00:00]
Hi. Thanks for taking the time to talk with me. I am interested in learning more about Hadrian, but also spending time on some of the other players that are out there like the Machina Labs and Divergence 3Ds of the world. It might be helpful to start off with just a quick minute on your background, what your current role is, and then also your last role.

**Expert** [00:00:22]
Yeah. I currently work at a company called Physical Intelligence. We're building foundation models for robotics. The idea is that imagine one day you could have a generalist model that can control any robot to do anything. The core premise here is that robots tend to be state machines, meaning that they are designed to do a single thing repetitively forever. When something goes wrong, a human needs to intervene and fix it.

What we're hoping to do is give robots the ability to think and reason about the real world, as well as do really complex things. If we look at a lot of the things that people do where we still haven't automated these things, it's mostly because people are able to do things like find dexterous manipulation, people are able to reason about the world. People have an intuition for physics. We want to give all of that intuition and intelligence to autonomous systems as well.

A large part of that is collecting data. Our models are based on a similar architecture to the canonical LLM. You could also imagine that there isn't an Internet scale data set of robots doing productive labor in the world. A large piece of what we do is actually developing that data set and curating that information. A big piece of that is predicated on developing both robots, as well as control systems such that a human can teleoperate a robot to do a task.

At Physical Intelligence, I focus on, basically, all of our hardware efforts. We're a very small team, mostly AI-focused, but we have a very, very small hardware team. I focus on all of the hardware design and we have two other folks who are mostly fabrication and assembly folks.

Before this, I worked at Anduril. I led a project called Bolt, which is a loitering munition quadcopter system. Basically, inspired by the early portion of the Ukraine war. We, basically, started with a small team and scaled it up into a business line with hundreds of millions of contract value behind it. It was, honestly, a very cool experience and got a lot of experience across mechanical design, electrical design, manufacturing, ramping up from an idea to selling to the government, shipping units to the government.

Generally, my background has been in autonomous systems for both robots as well as UAVs and drones. I also do some angel investing on the side. I mostly focused on some of the topics you've mentioned for the call, manufacturing, robotics, AI.

---

**Client** [00:02:52]
Great range of experience there. Maybe let's start on Anduril and Bolt. Maybe to start off, can you just talk us through when you're looking for the suppliers for or maybe the vendors, I'm not sure what term you use, but the folks like Machina, Hadrian, maybe mom-and-pop machining shops, and then also doing things in-house, how do you guys think through what's going to be procured from each of those buckets?

**Expert** [00:03:17]
It really depends on the stage of prototyping. I think at day zero, you want to prototype things in a really, really quick-turn way. You might start a design with everything 3D printed. Obviously, 3D-printed designs don't scale, especially when you're building something that requires some level of structural integrity. Usually, a 3D-printed prototype will graduate into some form of metal prototyping within a week or month. You're looking at things like sheet metal and CNC machining as your primary way of prototyping mechanical components.

At Anduril, the unique maybe differentiator for how we would look for these vendors is that things were one) moving at lightning speed. two) We had to work with vendors that were ITAR compliant, had AS 9100 certifications. The entire laundry list of different standards that vendors need to meet to basically make parts for defense companies.

We, basically, had this very small library of companies that we would use and had experience working with. For sheet metal, there were companies like Oshkosh, there's Fabworks in LA, and for CNC machining, pretty much all of our volume across all products we built were being made at a company called Protolabs, which you might be familiar with in your research here.

How we pick vendors, at Anduril, it was just we had these really tight constraints. Money was not really super important in terms of early stage. We basically would work with the companies that could deliver fastest. Now one of the downsides of this is companies like Oshkosh or Protolabs, really quick-turn places are also not able to hold really high tolerances. That actually changes your design process because it pushes engineers to design things that don't require precision. It turns out that to design a precision machine, you don't always need to design precise parts. They just have to come together in a precise way to function a certain way.

That philosophy implicitly changed a lot of the design process. We designed things that didn't require aerospace grade machining tolerance at the end of the day. Obviously, once we scaled the product that the vendors were using were aerospace vendors, but the ask towards them maybe is far less difficult than maybe any other company or any other customer.

Protolabs, to the extent that we used it, it was pretty much only for CNC machining. They also offer 3D printing, but we had other partners that we had found to do 3D printing. Oshkosh does sheet metal. Basically, they can do steel, aluminum, copper, basically any sheet metal they can cut and bend, and they do it on very quick lead times, as long as you pay. There's also a company called Fabworks. They both do similar types of things.

---

**Client** [00:06:06]
Got it. Those are companies that you're using in prototyping for fast turnaround, are those both companies that you can go into production with on, I think you said it was a multi-hundred dollar program ultimately?

**Expert** [00:06:19]
Definitely not. These are companies that you can make maybe as a stretch you can probably make on the order of a 100 of something. Even then, it wouldn't really make economic sense to work with these vendors because they're really tuned to, we do a high mix, low volume work and very fast.

Again, they're also not really tuned to special or custom processes. For example, a prototype doesn't need to have paint on it or anodization or any other finishing, but a finished part that goes on a finished product might have a whole bunch of post-finishing processes and maybe even quality assurance standards that need to be met. These companies are not really suited for the production phase.

---

**Client** [00:07:03]
They're not doing anodization or heat treatment or anything like that.

**Expert** [00:07:07]
They can offer these things but it does not really scale as an engineer to go with them for these things.

---

**Client** [00:07:14]
Got it. As you do scale, you get past the prototyping phase, you maybe have a design, how do you think about who you're going to go into production with in terms of suppliers?

**Expert** [00:07:25]
Yeah. I think there's a certain extent to which I can speak about this at Anduril specifically. In general, we're looking for companies, the non-starter is quality. Can the vendor make the part that we need them to make? The second question is scale. The scale piece of it usually can be tackled in a number of ways. Some companies might already have bandwidth. They might have multiple warehouses full of multiple, maybe dozens of CNC machines they can dedicate to your jobs.

Other companies might be able to show you that they can do high quality work, but that they don't have build out yet today to go and do this stuff. They also might come to you and say, "We actually have a private equity partner and we would be willing to set up new capacity just for you guys."

This specifically outside of America happens a lot. I think that you don't see a lot of that latter paradigm in America. If you go to somewhere like Taiwan and you have a multi-year project, this has happened for the last two decades. This is how we've built iPhone and Google Glass and all these moonshots. When they were initial ideas, basically folks in Taiwan invested heavily on their end in order to support.

---

**Client** [00:08:38]
On the commercial side, a lot of that's going to be outsourced to Asia. In the aerospace and defense side, you still need, not all aerospace, but the military side you still need to find those U.S. suppliers.

**Expert** [00:08:51]
Yeah. I think that defense companies do their best to find ways to ship out as many things as possible. That also has to do with how do I make the majority of my parts to not require certification such that I can use vendors that are not locked to the United States.

---

**Client** [00:09:07]
Yeah, it's certified. It's certified parts that have the requirement of being made domestically.

**Expert** [00:09:13]
Certified, meaning if there's a munition system and that part is specifically relevant to the munition component of the product, that part might need to go through an ITAR compliant process. Anything similar to that, anything where there is something that is core to the function of a lethal weapon, I think would, at least in my experience were things that were largely ITAR controlled. The summary statement here is basically you try to make as many of your parts to not require ITAR compliance.

---

**Client** [00:09:45]
If it's just a Bolt or something, you can import it.

**Expert** [00:09:47]
Again, I can't speak to the specifics here because, usually, supply chain folks are working through this. That has been the case in some products, although on some products, even that is not even an option.

---

**Client** [00:10:00]
Got it. Maybe specifically turn to Hadrian. You mentioned you're looking for partners that can deliver the quality and also have the scale. Where would you put them on that spectrum? How did you guys think about them as a supplier?

**Expert** [00:10:13]
I don't know if I can speak directly about Anduril's interaction with Hadrian, but I think you also mentioned in the early email about Formlogic.

---

**Client** [00:10:22]
They went under, I think.

**Expert** [00:10:24]
The reason I bring it up is Hadrian is trying to scale the CNC factory in America. They are mostly focused on improving the operational efficiency of these factories in order to make more parts. They spend a lot less time on optimizing the process, which is the actual CNC milling process that makes the part.

At least, in my experience, they are not able to deliver reliably high quality parts, but they do have the ability to make things at scale. Meaning they have designed their factories in order to make many of something. They have designed a bunch of software to make the process from receiving a drawing to producing a quote, to ordering, to procuring the stock, to machining the parts. They have made that workflow quite efficient, but they have not really refined the how do we make aerospace grade parts at quality yet.

The reason I brought up FormLogic is FormLogic's premise was a little bit different. They took the approach of, "We're going to figure out how to minimize the workload involved in toolpathing a part, basically, figuring out the toolpath that's required to machine a part. We will use that to make it much, much easier to machine quality parts at scale. Hadrian's approach is much more of the private equity/VC-inspired direction of, "Let's just scale the machine shop. Let's consolidate all the assets under one roof. Let's make all the processes more efficient." That's my experience. We've had some not great experiences making relatively complex parts with them.

---

**Client** [00:11:57]
In that case, are they someone you could turn to for somewhat less complex parts and still use them in that way or that's the niche that you want to use them for?

**Expert** [00:12:07]
I think you wouldn't really go to them for the less complex things because there are cheaper and faster options that are more reliable. Also, they want to position themselves as the aerospace vendor. They actually don't even really want to take on prototype volume. I think, at scale, they might be able to produce much less complex parts, for sure. If you're a company that's just doing R&D, they're probably not the right fit.

---

**Client** [00:12:33]
People who can make simpler parts cheaper and faster, how are they doing that? What attributes do they have that make them better at it than, say, Hadrian?

**Expert** [00:12:42]
One thing is instantaneous quoting. If you're an engineer on a prototype-scale program, you usually don't have access to a purchaser or a supply chain person who's going out and vetting vendors on your behalf. Some engineers will take a lot of liberty in actually going out and doing some of that work. Obviously, if there's an opportunity cost because it's time you're not spending on your design. There's, obviously, dividends to doing this because if you can work well with vendors, you can potentially produce better output.

---

**Client** [00:13:15]
For less complex parts, you mentioned that there are people who can make those parts cheaper and faster. I'm just curious, who is cheaper and faster? What does that company look like?

**Expert** [00:13:25]
The cheaper and faster companies are the ones I mentioned, companies like Protolabs. In other cases, your friend's grandfather who runs a machine shop that you have a close relationship with, you've done a few parts with them, you have a shorthand communicating. The summary of what I was getting to is that if an engineer is managing a relationship with a vendor, it generally is easier if the vendor is easy to work with.

With a company like Protolabs, the benefit is you can upload a file and a drawing and basically within minutes, or sometimes even in seconds, they will tell you exactly how much it will cost. They'll give you three options for delivery dates and then different pricing based on that.

A company like Hadrian today is not going to be able to do that for you. If you are an engineer who needs something in three days, you are always going to turn to the company that's going to give you a quote immediately. Under the hood, the other thing that Protolabs has done is they have their own tool path software that generates toolpaths for these machine, for these parts, which also means they expose a library of different tools they use.

If you're an engineer and you are clever, you can design your parts to be made by those specific tools. They also give you certain guidelines, if you send us parts that have this depth, we'll make it for you. There will be surface artifacts. We will not be able to get to the corner radius at this specific region of your part.

What I am saying is if the vendor makes it clear to you what they are capable of and what they are not capable of, engineers can design in a way that they know that they can put in an order and in three days receive a part that they know that vendor will make. With companies like Protolabs or with your friend's grandfather runs a machine shop, it's much easier to have that basically immediate intuition for what's going to work. You can incorporate that intent from day zero when you start designing your parts.

---

**Client** [00:15:30]
I think that's something that Hadrian does advertise is having that relationship, maybe having some software that engineers can work on to help understand will this part even be machinable and things like that. It sounds like that's something either you didn't interact with or didn't find impressive.

**Expert** [00:15:49]
They do have software to basically be able to quote parts. That software is used to fine DFM constraints. These are for much more precision parts than ones you'd make on Protolabs. In my experience, the issue was not with not catching DFM issues, the issue was with receiving parts that work. What I'm saying is, even if all of the disputes around how things should be machined or tolerances were cleared between the engineer and vendor, at least in my experience, we haven't received parts back that matched the specification.

---

**Client** [00:16:22]
Got it. At that point when that happens, is that just a vendor you will decide not to work with again?

**Expert** [00:16:28]
Generally speaking, at a company like Anduril, where you're moving super fast, there really isn't any margin for failure. In that case, we would either maintain a relationship and see how that vendor develops over time, especially with a company like Hadrian that's trying to improve the process. Generally speaking, you wouldn't be giving them production volume or prototype volume for that matter.

---

**Client** [00:16:53]
Got it. What I'm trying to figure out is Protolabs, it makes sense, in the prototyping side, it sounds like Hadrian maybe didn't pass some tests that would have made you guys comfortable going into production with them. If I'm talking about a production machined part, who's going to be the right set of options for that?

**Expert** [00:17:11]
It's usually not one person. It's usually that there are a number of different machine shops that you can go to that each specialize in a specific type of machine part, whether it's something that's radially symmetric or a turned part versus a three op machine part. These are usually much smaller shops that you give maybe one or two parts and a 100-part BOM. Even then, a lot of these companies, they're just small machine shops that have a track record. Small meaning small- to medium-sized companies, if that makes sense.

---

**Client** [00:17:44]
Yeah. The mom-and-pop defensive suppliers.

**Expert** [00:17:46]
Yeah. Equity roll up.

---

**Client** [00:17:48]
Got it. When you think about that, I think part of the Hadrian thesis is that there are issues with dealing with a large number of these mom-and-pops. Do you see issues with them? I want to lead you on problems. Does that supply chain work well? Is that a well functioning supply chain?

**Expert** [00:18:05]
Generally speaking, no. I think that everyone believes in the dream of what Hadrian is trying to do, but I don't think it works well because every vendor will have the same set of problems. If you give them an order and they have to procure metal and that metal needs to be certified to some standard and then it comes back to them, they need to be able to machine it. They might have yield issues. Any one of these things is a single point of failure on any one of these vendors. At production scale, there's usually an individual person managing the relationship with a number of a subset of the vendors for even a subset of a product. Short answer is it doesn't work super well.

My experience in Asia has been much better though. This is not really Anduril, but post Anduril. The vendors in Asia tend to be a lot more reliable to work with. The other value add is a lot of these companies are able to quickly spin up new capacity in Malaysia or Vietnam and they will do final quality assurance in Taiwan. They are still responsible for delivering you good products. My experience there has been very positive.

---

**Client** [00:19:14]
Got it. You're talking about in the robotics space?

**Expert** [00:19:17]
Just working with CNC sheet metal injection molding, 3D printing vendors in Taiwan. These are, by the way, vendors that also do produce components for American defense companies.

---

**Client** [00:19:28]
Just on that topic, obviously, topic du jour. All the tariffs that have been coming in, are some of the numbers that get thrown around like, say, a 25%, 30%-type tariff, is that something that would make it challenging for some of the companies you've worked for to continue to source from Asian suppliers? Is that annoying? You mentioned that they are both reliable and also the prices might just be so much lower that it doesn't matter.

**Expert** [00:19:56]
If you're doing manufacturing in Taiwan, the pricing is usually only about 20%-30% cheaper. It's so reliable, the vendors are so good, they will respond to you in a dime. You can work directly with engineers. They're super proactive. With the tariff, it effectively might cost the same as doing stuff in America, but if not, still cheaper. If you're doing things in Vietnam or Malaysia, for example, at much higher volume, you're not doing prototyping, even with these large tariffs, it's still significantly cheaper to do abroad than in the U.S.

---

**Client** [00:20:30]
Got it. Theoretically, if you had a really high-quality supplier going head to head with, say, the Taiwanese supplier, if they were able to provide a great experience, that price parity is there, maybe not for you right now, but that could compete for business over time. Vietnam and Malaysia would be harder?

If there's price per Taiwan, it sounds like, right now, there's no one who can really match the customer experience. Theoretically, if a Hadrian or someone else was able to give a really good domestic experience, they might be at price parity, they could come into the conversation. For the Vietnam, Malaysia part, it'd be pretty challenging just with how low the prices are.

**Expert** [00:21:10]
For sure. I think if they reach parity, that would be really good. I think the secondary effect of that is wherever Hadrian or another company like Hadrian or Hadrian expands to different places, I think that would attract companies to go and set up shop near companies like Hadrian. Hadrian's already based in LA, but if you can rely on a vendor in America that's in the heart of Hawthorne and you're a company in El Segundo doing some aerospace thing, it's only more beneficial that you can drive 20 minutes and go talk to the machinist that's making your part.

---

**Client** [00:21:46]
Inherent advantage and no shipping time. I assume that it brings down lead times a lot.

**Expert** [00:21:51]
Yeah. Actually, one interesting anecdote I can give you here is there was a project that I worked on in the past where the parts had to be made in the U.S. for ITAR reasons. I worked with a U.S. vendor. I sent them a drawing. It took me three days to get a quote. We kicked out the quote as soon as possible. I paid them up front. It took six weeks to receive the parts because six weeks is their standard lead time.

When I dug into and actually visited their machine shop, the reason that the order took six weeks is that a piece of paper was stuck on someone's table under a stack of other paper and it was the piece of paper that showed the material certification for the stock part of the stock metal that is pre machined. Even though there is the benefit of I can drive 10 minutes over to the shop and work with this engineer, the fact that I cannot rely on basic things to be done efficiently is unfortunate.

---

**Client** [00:22:49]
I'd be curious on that point. I understand you had a bad experience with the parts, which is probably the key thing. On lead time and process, I think Hadrian talks about having faster lead times, being more efficient, not dropping orders, things like that. On that front, was your experience that they did a good job with that or were there challenges there as well?

**Expert** [00:23:11]
I don't have direct recollection of their response to lead times.

---

**Client** [00:23:15]
No worries. One other question would be, were you involved in providing feedback on the low-quality parts? I'm curious if you have a sense of what the response was and how that got resolved.

**Expert** [00:23:26]
I don't think I can discuss the details of those.

---

**Client** [00:23:29]
Without going into details, would you describe it as receptive to feedback? Not really interested in hearing it?

**Expert** [00:23:36]
Receptive to feedback. Basically, there's the quote process, there's the disambiguation of what we're making. The vendor might give you DFM feedback, the engineer might change something. I think that process usually always goes well. The challenge is usually receiving a final part that actually meets the specification.

---

**Client** [00:23:56]
Got it. Anything else on Hadrian specifically that we haven't covered that is worth touching on?

**Expert** [00:24:01]
I think the promise of what they're doing is exciting. My wish for Hadrian has always been that they would have focused more on the core technology of making machining more efficient rather than improving the operational efficiency of the machine shop. The reason is that I think that the operation side of the problem is not particularly hard from an engineering standpoint. It mostly just requires money and scale.

If you can prove that you can do high-quality machining in a much smaller factory, where you can upload a part, the part is autonomously toolpathed by an agent, and that agent does a good job. Maybe there's some human that has to give some feedback, maybe there's some back and forth with engineer, but instead of having a three-day discussion back and forth in a part, it takes an hour or less, and then you could get really high-quality parts in a few days, that would be a really promising story.

You could raise a bunch of money and scale the operations, build all the software to optimize the actual factory. I think that there's a narrative play here, the narrative play being, "Look at us, we can scale manufacturing," when if you look at the quality of parts, they're just not really there yet.

---

**Client** [00:25:17]
To the extent that they have customers who are satisfied/expanding, how would you reconcile your experience with that? Would you think that maybe they're dealing with lower complexity parts, that they figured some things out? How would you think about it?

**Expert** [00:25:32]
They probably work with less price-sensitive vendors. I think, at the end of the day, quality issues are always solvable. I believe that they have the capability to solve them and they likely have solved them in the time that I've no longer been at Anduril. Working with defense companies exclusively gives you the luxury of not having a price-sensitive customer, mostly because that customer doesn't have a choice but to manufacture in the U.S. As long as you're able to show at scale that your cost is marginally better than the N number of mom-and-pop shops, and it's much easier to broker a relationship, I can see why vendors would like to work with a Hadrian.

A Hadrian option would not work for, for example, a Meta who's building server racks or an Apple that's machining the enclosures for their iPhones, which are, fun fact, actually machined and not stamped, which is really interesting. Companies that have consumer products that are at scale are not going to be able to work with vendors like this, just not yet.

---

**Client** [00:26:36]
That's because of the quality point or that's because of the economics? They just can't match Asian scale?

**Expert** [00:26:43]
Scale and cost. That's right. I think the real problem for Hadrian would have been that you can cut out more of the machining labor, the humans that have to operate the machines, and thereby being one of the larger drivers of what causes the parts to make sense.

---

**Client** [00:26:59]
Are you saying you think they haven't done that?

**Expert** [00:27:02]
They haven't really done this and they haven't invested in this as heavily as I think they should.

---

**Client** [00:27:08]
Got it. You think that's a bit more marketing and narrative than what they've actually done. If you read the press, they do talk about, "We don't need a skilled machinist. We've replaced a lot of labor," things like that.

**Expert** [00:27:21]
They do talk about this. They talk about robots being able to load the billet. They talk about tool wear and modeling those as a function over time for autonomous tool replacement. There are a lot of these sorts of things, but there is also a lot of different problems to be solved. Again, I have some hot takes on this company. My general thesis is that this problem is going to be solved by people who are experts in computational geometry and not necessarily by engineers who can program a robot arm to load and unload a CNC machine.

---

**Client** [00:27:54]
Makes sense. I just want to make sure I understand. You're saying that customers that aren't price sensitive might work with them. I'm not sure I totally follow. I think that quality issues would still be an issue there.

**Expert** [00:28:07]
Quality issues are always solvable. You can either improve your software or have humans manually doing things, and you can always solve the quality issue. If you're not price sensitive and it's easier for you to work with one vendor, I can imagine why you would rather work with one vendor, where if you work with them long enough, you can get them to deliver at the quality you require.

---

**Client** [00:28:31]
Theoretically, actually, if you're willing to suck it up, go through the process with them, you could buy into the thesis of there's going to be one vendor. I'm going to do a lot with them. We'll work through the quality issues. It sounds like with Anduril, you guys were trying to move really fast. You get back a deficient part, you're not just like, "All right, let's go through three rounds with these guys, try to figure it out." You're just going to send it to someone else.

**Expert** [00:28:57]
That's right. I think this is the case for any vendor. You can, in the limit, work with any vendor to generate any outcome, it just requires some level of time and money investment on the customer side. Of course, if you're a much larger company, you can parallel path multiple vendors to de-risk an option. That often is not the case when you're building a new program from scratch.

---

**Client** [00:29:21]
When you're thinking about other people who that may make sense for, are traditional primes more like the bucket of not price sensitive, probably willing to work with the vendor, willing to do a lot of turns, things like that?

**Expert** [00:29:35]
I think so. At the end of the day, the lack of price sensitivity is passed on to the taxpayer and spending more time on the design and procurement process only benefits them if they get paid on time and materials.

---

**Client** [00:29:48]
That makes sense. You're an investor, so curious on your perspective on this. Overall, do you think that the dream they have is interesting enough that you'd be considering investing in them at this stage, or the issues you've seen and the difference in approach with what you think should be done here is enough that you wouldn't really want to touch it?

**Expert** [00:30:10]
I have a pretty strong opinion that it should be done a very different way. If, for example, Chris Power is raising money today, my sense is that that money would be going towards scaling operations and not solving the core problems of automation. I don't know that would be interesting. I think also, a company like Hadrian at this stage and in their direction probably benefit from debt financing over venture capital. I just don't believe in the venture model for this business. I also don't have enough money to loan out to.

---

**Client** [00:30:43]
One day when there's humanoids everywhere, it'll be the debt provider. Just to make sure I understand this point. I know you think that they should have been solving at the machine level, how you actually machine the part, think about the process. If you thought that they were taking out real costs on the machinist side, either by replacing labor or using lower skill labor and they were investing in that automation, would that feel like a good place for them to be investing? You're pretty focused on they need to be thinking about how to make better parts?

**Expert** [00:31:17]
No. That would change my opinion because I think if you're looking at the current world events and we're saying that tariffs are going to get expensive, we can't make things in China, we need to find ways in America to make things, I don't see a path for American manufacturing to be revitalized through human labor. I don't think it works in America. It's not going to work at cost in terms of cost and scale in America. The only way to do it is to automate these systems.

Basically, taking all the manufacturing know-how that exists in the minds of these Taiwanese companies. Finding ways to mix that with like state of the art automation and robotics to solve the problem. I think if they were looking at finding meaningful ways to cut costs and make the process more efficient, I think there's merit there.

---

**Client** [00:32:08]
That's actually probably a great segue to talking about humanoids for a second on the topic of either make labor more efficient or just try to create an army of humanoids. Getting curious, starting on big picture. My sense is that a lot of what's happening in the industry right now is that people are playing around with transformer based approaches, trying to collect a lot of robot data via teleoperation or maybe other methods and try to solve some of the general purpose robotics problem. You talked about it a little bit at the top. I'm curious, A) What do you think the cutting edge approaches are? B) Curious, what's your level of optimism is that they're going to work?

**Expert** [00:32:49]
You're saying current approaches to what specifically? Developing the autonomy or starting to actually do productive labor with robots?

---

**Client** [00:32:57]
I think probably do productive labor with robots as the end state. Maybe it breaks down more into the different pieces of it, reasoning, locomotion, manipulation, things like that.

**Expert** [00:33:08]
I think the core of being able to do productive labor is going to be manipulation and not locomotion. I'm not clear that I've seen really impressive commercial demonstrations of productive labor today. I think that one of the interesting insights is the bitter lesson that we know from machine learning that you need data across a very broad domain to do anything really well. Trying to develop a single agent based on a very specific set of data often leads to some asymptote of efficacy that is much lower than if you had a generalist that could specialize to a specific task.

I think the same applies in robotics. I think that that's one of the approaches that likely is state of the art today. These generalist models are showing much higher performance than either state machines or very specific models. An example of the latter there is that if you look at most of the autonomous vehicles the last decade, there is an AI point solution for every single system in the car. There's an AI that reads the LiDAR information and generates a 3D reconstruction of the world. There's an AI that's the camera to classify things.

Using the insights that each of these agents generate, there's another state machine or AI that's making a decision on top. I think the new innovation that people are interested in is the full end-to-end approach of there is a single intelligence, maybe comprised of multiple agents that work together, but they all ingest directly sensor feedback about the world. They all directly generate an output the same way that human perceives the world through their five senses and then performs an action.

---

**Client** [00:34:50]
You said that so far you haven't seen demos that are convincing that manipulation has been solved. Do you think those full end to end?

**Expert** [00:34:58]
I think that there are some interesting demos. I think that they're very early, but I am optimistic about this direction. The thing I'm not optimistic about is humanoids. I think that these general intelligences will be able to control any robot to do anything in the limit. I think we can already see some signs of life of this.

My question would be, why does this have to be a humanoid modality? A lot of these companies are telling you that they could sell you a humanoid for $30,000. My pretty strong guess would be that their current prototypes are on the order of $500,000-$1 million. If they really tried, they could probably get their price point somewhere in the order of $70,000-$150,000 today. I don't see a world where you could scale humanoid labor and it would make more sense than having humans.

To summarize, I think the non-starter to doing productive labor is the intelligence. On the hardware side, if you're a company that's capable of building a humanoid, I would ask you, why not just focus on working on the arm, focus on the supply chain of just the arm, and make an arm design and develop a manufacturing line that makes it so efficient to manufacture arms that you could make 20 arms for the same amount of resources it would take to make a single humanoid. You could, basically, get rid of all of the objections that people have around things not being humanoids.

For example, one of the big reasons people want humanoids is say my factory has two floors and you need to do work on both floors. You have to be able to traverse up and down stairs. If you can now make 20 arms for the cost and resource it would take to make one humanoid, you could just have a bunch of arms on a table on the second floor and a bunch of arms on a table on the first floor and some robots that basically move materials through an elevator top and bottom. This is an over-exaggerated point, but the point is that you could optimize for developing much simpler robots, maybe with wheels with no bots at all, and do more productively.

---

**Client** [00:37:10]
That makes sense. I've heard a lot about just putting two arms on a wheelbase and having that be, it can't go upstairs or whatever, but it can go around a manufacturing environment at the minimum. It makes sense. When I think about training these generalist models, you hear about people operating armies of teleoperated robots and trying to train things that way. Do you think it's clear at this point if you look at the research what those generalist models are best trained on? Is that the direction it's going or is it more unclear at this point?

**Expert** [00:37:44]
I think it's highly unclear. If the question is if we end up having a general physical intelligence at some point, what is it trained on? I think it'll probably be trained on everything. It'll be trained on human video, it'll be trained on teleoperation, it might be trained on world model-based sims, it'll probably be trained on everything. We'll use every piece of data that we can get as the robotics community.

I think that, today, the best results are coming through teleoperation, mostly because it's really hard to fully encapsulate the reality of physics in a simulation. Second, it's really hard to transfer human video data to what a robot could do today for a number of reasons. One, that every human's anatomy is slightly different. Even if they were all the same, translating video to what a humanoid could do is relatively difficult. In reality, many robots are not going to be humanoids. Transferring human video to what a UR5 robot in an industrial warehouse could do is very difficult.

If you want to make progress on this problem today, the clear solution is to work on teleoperation. That's not necessary to say that teleoperation is the way that we're going to solve the problem. It's mostly to say that, today, it's the best way we can get results.

---

**Client** [00:39:02]
Got it. Based on what you're seeing, is it clear that teleoperation is putting the industry on a path to doing human useful work? Do you think there are still leaps needed to get there? I'm curious on that question, and I'll ask the follow up.

**Expert** [00:39:17]
I think it certainly is, especially because if you can get teleoperation hardware to be cheap enough, there are actually a lot of interesting business models in just labor arbitrage. Forget about the foundation models. If you're just employing a bunch of humans who teleoperate robots, you might have a workforce that's in the Philippines that's teleoperating robots in the United States. There are plenty of interesting things you can already do with that.

Separately, in the process of doing productive labor that you're being paid for, you can collect all this useful data. I think there's merit in even just teleoperation. Even if there wasn't, I think there's plenty of high-leverage-enough jobs that you could want to build an AI model to do that it justifies the cost of the operations of having a teleoperated fleet to train, if that makes sense.

---

**Client** [00:40:10]
Yeah. The teleoperation isn't actually getting you general intelligence. You need to teach it how to, I don't know, if I take the figure BMW example, it's getting criticized a lot today. Taking piece of sheet metal, putting on a car, theoretically, you just throw a ton of teleoperation, that task at it, and it learns how to do that.

**Expert** [00:40:30]
I actually believe we can already do this. There is this thing called the diffusion model. If you want to do a specific task over and over again, I think that we should already be able to do this. I'm surprised there aren't already companies out there that are saying, "Here are these robots. We can provide you a point solution for a robot that does a slightly dexterous task, but not a very dexterous task."

For example, I have a conveyor belt full of fasteners that I have to give QC on, remove the fasteners that have a chunk that's excluded from the bolt head. If you have a sufficient quality camera and you have a human that teleoperated the robots and do this for a few days, I think you could actually get a pretty high-quality policy today.

---

**Client** [00:41:16]
Switching between tasks and doing, maybe not full generalizability, but on the path to generalizability. That's still the unsolved challenge?

**Expert** [00:41:24]
It is unsolved. This is what we spend a lot of time on at Physical Intelligence. It's really about the data that you feed to the model. You can do a lot of this with teleoperation. As long as you're not just showing thousands of hours of one task, we're showing millions of hours of lots of different tasks. It actually turns out that it ends up not being really about the task. Meaning you don't have to teach the robot about literally everything that you have to do in the world. You just have to show it enough things that show it enough about the laws of physics.

The example I usually use is if I were to wipe your memory and teach you how to catch a tennis ball for an hour, basically, you standing maybe 100 ft from me and I throw you a ball and you try to catch it. At the end of the hour, you might be pretty good at catching a tennis ball. If I then, all of a sudden, threw you a football, you might still actually be able to catch it maybe 70% of the time. The reason for that is in the hour that you spent catching a ball with me, you saw balls that fell to the floor that you didn't catch. You learned something about initial velocity imparted on the ball and how that varied with air resistance as it traversed 100 ft.

You also learned something about the rate at which things accelerate to the ground 9.8 m per second. You might not know these things, analytically speaking, but them from an intuition. Even though I didn't teach you how to catch a football, you learn a lot about things like kinematics and gravity and you're able to generalize to football. A lot of what we see is that it's more about showing the models about the laws of physics than it is about showing the models about every single task.

---

**Client** [00:43:13]
That makes sense. I'm curious, do you think that the reason we haven't seen people go to market with that narrow point solution thing is that if it doesn't have that more general intelligence what you're describing, understanding physics, understanding completing tasks. Is the problem that it might run into these edge cases and have no idea what to do? In the sheet metal example, if I drop it, does it know how to pick it up? Things like that. Could that be part of the issue?

**Expert** [00:43:42]
Yeah. I think it's 100% the issue. The percent uptime and efficiency that you have in a human workforce could be much higher because humans can evaluate the situation and correct. Whereas robots today, even these single point solutions will probably make a lot of mistakes. What I was saying, if there was a factory line that was operating at a 99% efficiency rate and now it's operating at 95% or 90%, that's a significant margin that costs money.

My argument would be that you can supplement this with teleoperators. You could have 10 robots that are running this state machine or this point solution and instead of having 10 humans behind them, you have one human that's just watching all 10. When something goes wrong on one of the lines, one of the robots, the human intervenes and takes over. I think there's a lot of interesting things to do already before you have super intelligent models. I think it just requires some level of creativity on how and when humans intervene.

---

**Client** [00:44:46]
Got it. You might expect people to go to market not promising just this pure robot model. I think, what a self-driving cars do to some degree. You have a teleoperation who can take over in the case of some edge case.

**Expert** [00:44:59]
Yeah. I do think so.

---

**Client** [00:45:01]
On the hardware side, I understand that you're less focused on legs and things like that, and that point make sense. On the hand side and fingers, do you see that as something that's a solved problem at this point? Is there still more development needed to do a lot of useful tasks?

**Expert** [00:45:17]
In terms of the robotic hand, I think that there's a lot of work to be done to build a robotic hand. My personal question would be, do we need robotic hands? A lot of folks say that it'd be ideal for the robot's anatomy to be that of a person because it's perfectly teleoperable because a person can just teleoperate as if they were doing the task. It turns out you can do a lot with not a human hand or something much simpler.

The other argument is that part of the promises of robots is that they might have abilities that humans don't have. Why constrain ourselves to hands when we can have very different types of end effectors? In short, I think if you're focused on developing hands, there's plenty of work to be done to make them much better.

---

**Client** [00:46:04]
Got it. Your argument would be that other form factors could end up being the things that end up being the most useful out in the real world?

**Expert** [00:46:13]
Yeah, either much simpler ones or maybe complex ones that looks significantly different from a human hand, but show that they are overwhelmingly useful for a specific task.

---

**Client** [00:46:24]
Would you assume that whatever goes into production, whether it's hands. I know you're not thinking humanoid forms, types of forms that Physical Intelligence or someone else might be using to go out into the market. Would those all be Asian suppliers that you'd end up working with? It sounds like that's mainly who you're working with today.

**Expert** [00:46:44]
It is today. It's a big question. My answer is I hope not. While I think Asia is a great place to prototype, build individual widgets of your system, there actually just aren't that many Asian vendors. I think the Asian vendors that make robots, there's really just the Chinese start-ups that are maybe as old as the humanoid and AI companies that are in America. There are the industrial robot companies in Japan like Kawasaki and Mitsubishi. In the China case, you're procuring really low-quality systems and you're stuck with the quality of those systems.

The companies in Japan, the turnaround, it's just much harder to work with them to get what you want on a timeline that you need it to be there. I think that the supply chain has to evolve. There have to be more American players, specifically not on the robot, but things like the actuators, for example. I think it would be really scary if we were in a literal arms race where the American robotics AI industry was completely dependent on a supply of robot arms from Asia, which now appears to be the case.

---

**Client** [00:47:50]
There's a bunch of different parts of this problem. Are there any emerging suppliers where you think, "Oh wow, these guys are actually doing something really cool"?

**Expert** [00:47:59]
Unfortunately, none that are particularly very impressive. A lot of them are, basically, just copy pasting what Chinese companies have done, but maybe doing marginally better execution and selling for a significant margin as an American product. There are folks that are starting up new efforts to, for example, do a joint venture between a Taiwanese company and a U.S. company to share expertise on motor manufacturing to then manufacture those motors in America. A lot of the results for these things are far yet to be seen and things I think that are just starting up in the last few months or maybe the last year.

---

**Client** [00:48:37]
When you survey the industry more broadly, when you think about Apptronik, Figure, 1X, anybody else. Are there any that you've been impressed by who you think either on the hardware or software side look like they're quite strong or not particularly impressed?

**Expert** [00:48:52]
I think that a lot of them have specific things that are particularly impressive. 1X has been investing in their hardware from day zero and they own the design for everything all the way down to the actuator. They built some very impressive, very torque dense actuators. I don't know if I can speak to much depth on Apptronik or Agility, but both of those companies seem to be able to produce these robots at scale and have shown commercial deployments, promising commercial deployments from what I've seen online.

In the limit, my honest opinion is that Tesla has the best positioning to win this market because they have the economies of scale already for all of the same components that they built for cars that are relevant for a robot. Things like actuators, things like stamped parts, things like PCBAs, things like the compute. At the end of the day, the robot will have an inference machine on it. Definitely, they're their own customer. I think in the long run, Optimus stands out as the company, the organization with the most advantage with the distribution and the distribution mode and economies of scale mode.

---

**Client** [00:50:03]
Based on what you've seen, has their execution been strong? Do you think they are currently a leader or the leader, or it's hard to tell.

**Expert** [00:50:11]
I think they certainly have some of the best hardware. If your bar is make a robot that looks and performs like a human, the question is if that's actually really useful.

---

**Client** [00:50:21]
One question that leads to though is for the software first players. I know 1X Tesla think of themselves as vertically integrated. Could you imagine a world where if someone does sort of crack the software side, you could work with like a 1X and just say, "You guys didn't nail the software, but you have great hardware, it's made in America. Why don't we put it on there?" Do you think the market could head in that direction or hard to see?

Could you see Physical Intelligence, others are taking a software first approach. Could you imagine 1X or someone else who thinks of themselves as vertically integrated, maybe Apptronik, being a hardware partner for the folks who are software only right now?

**Expert** [00:51:04]
I think that's really powerful. Actually, I would take a step further and I would say that the companies that have either built really good hardware modes or really good AI, they should invest in either working with another partner or building the other component from scratch internally. I think the vertical approach is the most powerful. Even if you just look at the last 10 years of Tesla Autopilot, whether it was a planned or unplanned advantage, they have 10 years of experience collecting data from cars. They've been building the actual car itself.

From building the car, they basically had the opportunity to then go and invest in building their own Autopilot hardware. Now they build an Autopilot and now they have basically full control of the entire system. If you're Honda and you go to Tesla, they will not sell you Autopilot. I personally am a strong fan of verticalizing it.

---

**Client** [00:52:00]
With that in mind, you guys are software only, I think. How do you reconcile that?

**Expert** [00:52:05]
I would say we haven't really decided yet. I think that there's a fork in the road that will probably happen at some point where it'll either be obvious that there are a number of different hardware vendors that all build different kinds of robots that are well-designed for specific use cases. None of those companies had actually cracked the AI piece. Maybe there's really a space for one company to sell a generalist model that can be fine-tuned to do any one of these tasks.

Maybe by the time we have that generalist model, there just isn't a clear standout winner. There isn't really an ecosystem of these companies and the only real way to solve the problem is to not provide a model, but actually provide a solution for labor, which is, at the end of the day, why anyone is working on robotics.

---

**Client** [00:52:54]
Really helpful. Thank you for taking the time to speak with me. Have a nice day.
