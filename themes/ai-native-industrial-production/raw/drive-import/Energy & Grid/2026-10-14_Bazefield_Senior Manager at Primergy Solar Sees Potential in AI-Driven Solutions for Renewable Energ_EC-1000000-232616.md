---
theme: "Energy & Grid"
title: "Senior Manager at Primergy Solar Sees Potential in AI-Driven Solutions for Renewable Energy Asset Monitoring"
doc_id: EC-1000000-232616
source_line: "Bazefield · Expert Call · Customer · 14 Oct 26"
date: 2026-10-14
company: "Bazefield"
pages: 2 of 2
saved: 2026-10-19T16:44:37.533Z
url: https://research.alpha-sense.com/search?search_id=tmp-0pnbg1kc8uodovl7vbczkp&sort=RELEVANCE&order=DESC&docid=EC-1000000-232616
---
# Senior Manager at Primergy Solar Sees Potential in AI-Driven Solutions for Renewable Energy Asset Monitoring

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

Bazefield

SMART SUMMARY

Summary

The conversation covered the challenges and opportunities in deploying edge analytics and AI-driven solutions for asset monitoring and predictive maintenance in the renewable energy sector, with a focus on data model normalization and SCADA integration. The expert discussed current practices, industry adoption, and the potential impact of new products aiming to streamline these processes.

EXPERT BACKGROUND

- Senior manager with experience in performance engineering at a renewable energy company, with prior roles at other major energy firms, focusing on SCADA systems, data analytics, and onboarding of new sites.

EXPERT SENTIMENT

- Cautiously optimistic about the potential of edge analytics and AI-driven solutions, but emphasizes the need for real-world validation and proof of concept.
- Sees significant value in solutions that streamline data model normalization and onboarding, especially for organizations considering switching software platforms.
- Open to exploring new products and partnerships, provided integration and proof of concept are clear and manageable.

TAKEAWAYS

- Edge analytics and real-time anomaly detection are promising but not yet widely adopted in the industry; most current solutions are still in the sales pitch or early discussion phase.
- Key use cases for edge analytics include SCADA tag normalization, real-time predictive monitoring, anomaly detection, and preventative maintenance, particularly for PV and wind assets.
- A major challenge in deploying edge solutions is the lack of unified data models and inconsistent SCADA tag structures across different OEMs and sites, leading to significant onboarding and mapping work.
- AI and automation could potentially reduce the manual effort of SCADA tag mapping by at least 50%, especially as models improve and repositories grow, but early adopters will bear more of the initial workload.
- Internal analytics models are preferred for flexibility and speed, but a robust, centralized data model could make switching platforms and deploying analytics much easier.

AlphaSense Smart Summaries are AI Generated

Introduction and Initial Inquiry

Use Cases and Industry Trends

Challenges in Edge Deployment

Tagging and Data Normalization

Modeling and Collaboration Opportunities

EXPERT BIO

Senior Manager, Performance Engineering (Asset Management) at Primergy Solar. Expert can speak to the implementation and optimization of operational analytics and AI in utility-scale renewable energy systems, aligning with the project's focus on edge device orchestration and analytics deployment.

Expert is a data and atmospheric science leader with a track record of building and scaling advanced analytics capabilities across utility-scale wind, solar, and battery storage portfolios.

View More

INTERVIEW TRANSCRIPT

**Client** [00:00:00]
Thanks for joining the call today. We're currently doing due diligence on a company called Packet, and I'm not sure if you received the link to the company and some of the overview documents on what they do. Long story short, we're researching about edge computing and analytics space, particularly on ways to accelerate the way in which edge is deployed and scaled across different sites, and some of the main problems there.

Before we get into all that, I'd love to go a little bit just into some of the top use cases, cloud computing or edge, we don't need to go into which architecture, but generally speaking, what the top questions are that you're concerned with in your role as a senior manager of performance engineering at Primergy.

**Expert** [00:00:43]
Yeah. Are you referring to how they align with Packet? I did get the information, and I was able to review all of that stuff. Are you asking more so about SCADA onboarding-type frustrations?

---

**Client** [00:00:56]
Yeah. Let me reframe the question. Let me just start at a high level, and let me ask the question of, in your time over the last three years, have you seen an increase in interest in processing and doing analytics on the edge versus doing it on the cloud or somewhere more central? I'll start there. Have you noticed that trend in your work?

**Expert** [00:01:20]
I've noticed definitely the pitch from third parties. As for our appetite for it, being that we're still new and a small-ish company, we have not really been entertaining those types of products on the existing or the development side. The topic has definitely come up from third-party discussions.

---

**Client** [00:01:37]
Okay. For which use cases are you being targeted for here?

**Expert** [00:01:43]
I think for the ones that I've seen, the ones that stand out are along the lines of what we discussed, the SCADA tag normalization, also any near real-time predictive monitoring of anomaly detection. Right now, every package that I've ever worked on at any of the organizations, it's basically a look back from yesterday's data.

Having that more real-time focus, especially on the ROC side, the real-time operating center, those types of things where you have an anomaly detection for either preventative maintenance or just outside of bounds is something I think is pretty beneficial. Also, data quality. Once an individual tag flies outside of the boundaries of whatever you've set it to, whatever threshold, those are some pretty solid use cases.

---

**Client** [00:02:28]
Got it. When you say anomaly detection, predictive maintenance, can we go a little bit into what that ideal use case would look like to you? I understand a lot of things are more reactive in the status quo. What assets are you thinking about that you would want to do this for? Where are the typical problems and issues that pop up that would be a no-brainer for you to deploy this for?

**Expert** [00:02:54]
Yeah. I think that we can start on the PV side, you're talking tracker motors that are stuck or trackers that are straying from the rest of the fleet. If we have some that are maybe they're uncalibrated to a point where they're tracking a few degrees in a certain direction away from where they should be at any given time, those are some just mechanical use cases on a PV site. Inverter derates. If there's some sort of an anomaly on the internal temperatures of cabinets or any thermal or non-thermal-related derating of an asset, that could be something that this would be an interesting product for.

Even on the wind side, we don't have wind assets. Just thinking about my past lives at Clearway and NextEra, yaw optimization was always a hot topic, are the turbines actually in the wind as well as they should be, and having more of an in-the-field sensor or edge sensor that can detect those sorts of things. Offset blades. You've got three blades. Obviously, if one of them is offset from the other two, we know that creates some stress on the machine as well. Things like that, I think, could be a real-life use case for something like this.

---

**Client** [00:04:06]
Have you seen your peers, other companies, deploy this? I'm trying to understand the adoption curve in your industry, where other companies are at. Where do you think the industry is currently at with regards to deploying edge for these use cases?

**Expert** [00:04:22]
I personally have not heard of these deployed in the field. However, I've been at Primergy since basically AI really started taking off, and this trend, if AI continues on the path that it is on right now, I wouldn't doubt that this edge product would be something that's a lot more widely used and widely offered as well.

At Primergy, these have just been discussions and sales pitches, but real-time use cases, I think they would first need to be vetted that they're as functional as the sales pitch says that they are. As AI advances and the technology just behind the models gets better, I wouldn't doubt for a second that this type of edge product definitely takes off.

---

**Client** [00:05:03]
Yeah. What do you think some of the core challenges would be to deploy edge for this? I'm just looking at your pre-call responses. Building uniform data models, tag structures, things like that.

**Expert** [00:05:18]
Yeah. I think some constraints and something I was trying to piece together from the summary that was sent over and the website is if this sits outside of the actual software that a company is using. At Clearway, we started using Bazefield towards the end of my tenure there. If this sits outside of Bazefield, what's that type of compatibility between every single software platform that's out there, whether it's commercial or an in-house product?

How compatible Packet or any edge products, how they would be with the pre-existing product? Is it meant to replace that product or is it meant to enhance it? I think a better understanding of how it works together with the current infrastructure in place at a company would be beneficial to understanding what the possible shortcomings might be.

---

**Client** [00:06:03]
Understood. My understanding is, right now, the typical architecture for a company like Power Factors, I'm not too sure about Bazefield, is that the way that the architecture works is that you have your assets, inverters, whatever, sitting on the site. You have a PLC, then you have a gateway, you have some historian, some SCADA system, and that is then being pushed out into some cloud platform.

The data that's being pushed, again, because you don't want to incur significant egress costs, it's only polling the data every one minute, every five minutes, something like that. It's not sub-second data, the type of data that you would need in order to do a lot of the type of predictive modeling that you'd want to do on sub-second vibration, thermal, acoustic data, that kind of thing.

What I've heard is that the cloud-centric architecture is typically built for performance reporting, fleet benchmarking, that kind of thing. There are a set of use cases for which you have to have some type of edge architecture. The tricky thing we're trying to understand is, when you say compatibility between a Bazefield type and this edge type of architecture, do they even touch the same use cases, is what I'm trying to understand?

**Expert** [00:07:20]
Yeah. Essentially then, it's a separate product. You've got your Bazefield for reporting and your high-level analytics and then a product like Packet would be more of real-time monitoring, alerting, and anomaly detection at the site. It's on the edge as opposed to centralized up in the cloud. Is that correct?

---

**Client** [00:07:41]
Yeah, exactly. It's centrally managed from the cloud, but the actual computation and processing is happening at the edge.

**Expert** [00:07:53]
Got you. I think that definitely clears that one up. I think another challenge is, I can't speak for everybody, but on the AI front, the models are very good at language processing and reading documents to a degree. I've found that from a data analytics standpoint, there's still a lot left on the table. Maybe the sophistication of the models that are being used on Packet are going to be more fine-tuned for those types of anomaly detection.

Even just feeding tracker data into Claude, it will just throw these really wild hallucinations out there. It would be interesting to see proof of concept how well this product actually does or has done in real-life situations. I think that's the big question mark on a lot of people's mind is, are people just using AI as a sales pitch? How efficient and effective is it really?

---

**Client** [00:08:43]
I want to ask about one problem that we've heard, I want to get your feedback on. It's feasible and it's fairly doable to set up edge analytics for one site, but then when you want to go to two sites, three sites, there's an increase in cost that complicates the deployment of edge. One of those is the fact that there's no unified asset data model usually for a company. You have different OEMs. They all have different tags, different naming conventions, and you need to map the different tags onto a single standard. Is that a problem that you've encountered in your work?

**Expert** [00:09:19]
Absolutely, 100%. You nailed it with multiple SCADA providers, they're all mapped differently. Some of the SCADA integrators, I think Bazefield, Power Factors, those guys do normalize the SCADA tags into their platform, but some other ones do not. That poses a huge problem for developing models across a fleet because when you're extracting the data, everything is named differently. Absolutely experienced that.

---

**Client** [00:09:47]
Could you tell me a little bit about the actual process of tagging at the moment?

**Expert** [00:09:52]
Are you talking about when you're integrating or when you're onboarding a new site?

---

**Client** [00:09:57]
Yeah.

**Expert** [00:09:58]
You get the full tag list, essentially, from the SCADA provider, and those will generally have a description. Let's just say it's in a spreadsheet. That's normally the way I've seen it. You have the actual tag name, you have some sort of a description, some units, so on and so forth.

For a PV site, let's say you've got temperature. There's a tag for temperature at a specific location, but it'll just say cabinet temperature, where within the cabinet, how close is it to IGBTs. Is it the IGBT temperature but it's inside of the cabinet? The descriptions, depending on the O&M provider, is going to be very loose, and there is not always a person to go to at the O&M that knows the specifics of what that tag is. Getting that onboarding doc and the SCADA tag list, the points list is definitely an essential piece.

There's a lot of back and forth and human error that can go into those mappings. I've encountered this at multiple places where we thought a tag was a tag for a specific derate. We reported out that this amount of lost energy was due to a derate of this component when it turned out that it was a completely different component, and it wasn't really power limiting the equipment to the degree that we thought it was. There's that human error there, and that's where I would question and be very curious to see how AI does that better than just a couple of engineers.

---

**Client** [00:11:19]
Right. Now, just thinking about that process, just intuitively, do you believe that there are opportunities to accelerate that process with very well-trained models trained on OEM documentation, actually taking samples of the time series, for example, from these devices and trying to infer what the data could mean? How much opportunity do you think there is to accelerate this process?

**Expert** [00:11:43]
Yeah. I think, currently, there might be some capabilities there, meaning if the AI is able to identify because of the trend and ranges and whatnot of a certain variable, that it is probably SCADA A or SCADA tag A. It's definitely possible. Where I think there could be more of an upside is if you just have the AI holding onto that repository and being able to use it across different fleets, different companies. You know you always have for GE 1.5s, you have that list, and it's archived, and you know what that looks like. When the new company comes on and decides to use the product, they've already got all the tags.

Having that repository and getting, managing, maintaining that repository on the back end so that the front-end user has less to do I think could be a huge advantage. The only issue with that is you have to front-load that, meaning the early adopters are going to have more work than the ones that are a couple of years down the road after the product is vetted and been used across many technologies and so on.

---

**Client** [00:12:44]
Right. Just going back to the idea of how much pre-work could an external party do to accelerate the process of deployment without being a repository. You know what I mean? I understand you want to archive, have better site memory that's shareable. That makes complete sense.

My one push on that is just that's an organizational problem that goes back to any problem, essentially, which is people are bad at storing information. If everyone's diagrams and point registries were super well-organized, then this would never be a problem. If it's something about just organizations in general, whether it's laziness, or I don't want to call it laziness, but people can be a bit disorganized, then it makes sense. You change hands. The sites change hands a bunch of times. It makes sense.

I'm just trying to understand in lieu of good data hygiene and discipline of keeping the site data in a repository, how much can you just infer from going on a site? Let's say you have a box connects to the devices on your site. How much can you just infer what the tags mean enough to map it onto a standard without having to really rely on the expert who's worked there for three years at that site?

**Expert** [00:14:05]
Yeah. I think, unfortunately, it involves or it's heavily weighted on the OEM themselves and the SCADA product. I know that, in my experience, some are a lot better archived and described and logically listed. Inverter power AC, very intuitive as opposed to inverter one AC power out three, and you're like, "Well, what's the three for? What are these random numbers?" I think that that's definitely an issue that's a wide range depending on the OEM.

I also think that a lot of them are going to be very intuitive. You're going to see two SCADA tags. One is DC inverter power, one is AC, and you're automatically going to be able to just put those two, plot them out real quickly on time series and see DC is higher than AC. These are probably just the inverter outputs. Like I was saying earlier, the temperatures, that's where it gets a little trickier because you physically need to know where those sensors are. For instance, I've seen ambient temperature listed at the inverter. You assume that's outside. It's the ambient temperature inside of the cabinet, but it doesn't say anything about the cabinet.

For things like that, you might be able to intuitively figure that out with some analysis where it's probably not 140°F outside. I'm assuming this is an internal temperature. It's not something that just by looking at a tag, the name or the description that you can really decipher that. You would have to put together some analytics. That might be where an AI-type tool is pretty powerful.

---

**Client** [00:15:38]
Got it. I'm just trying to imagine what's possible here. I'm just trying to validate a claim being made. Again, let's assume that product one is just a very simple, nice UI environment, where you can manually do things, just keep everything in one place. Level two is, "Okay, we have some inference and suggestions. We're not telling you what the tag is, but we've severely limited the set of possibilities down to three for you to choose."

The next level is, "Okay, here's 95% confidence on these tags." In the future, it's near full automation. Let's just say that's the end goal. Today, if you had to guess with a team that's just focused on this problem, how much automation do you think is possible for a site to do the tagging and mapping, if you had to guess how much of the work could be cut down?

**Expert** [00:16:34]
I would say at least 50%. I think it depends also.

---

**Client** [00:16:39]
You think 50%?

**Expert** [00:16:41]
Let's say you just can dump in the SCADA tag list and say, "Spit out what you say this is a map of and give me your own description and have those in one spot where you've got the original tag list, you've got their description from the OEM, and then you've got the next two columns, maybe what you would want to have it as a normalized tag and then their description and the justification or something." I think that could be massive.

Depending on the complexity of the site, if we're talking a DC-coupled BESS hybrid site, that's going to be a lot different than just a 100-MW PV site. I've seen a 100-MW PV site with basically 100 tags, most of which you probably would never use. That could be an onboarded or a mapping exercise that could take place in a day, especially if there's options. I didn't even think about that, where it's like, "Here are the three that we think that this could be. Your engineers decide which ones they are." I think that would cut down on a drastic amount of time.

---

**Client** [00:17:39]
Got it. Another thing is, there's the SCADA tags, but then also we'd be able to pull samples of the time series too. We can look at a one-week time series, let's say, or a one-day or two-day time series. That would be additional information. I'm assuming that would be very helpful.

**Expert** [00:17:59]
Yeah, absolutely. There are usually corrections anyways. You onboard and then you realize like, "Hey, this isn't what we thought it was." To be able to cut that down instead of waiting a week, cutting it down to a few hours and having the robot tell you like, "Hey, this is probably not what we originally thought," that would be great.

Again, if the AI model is being trained and used across all the fleets, all the companies being used, and it's just getting better and better, then again, it's front-loaded, so the early adopters are going to be the ones that are going to have more training involved. I could see that being if you have 50, 100 sites in there, it could have it fine-tuned to where the later-stage sites are going to be a lot quicker to onboard.

---

**Client** [00:18:44]
Got it. To understand the scale of the value here, help me understand how many times a year do you need to think about this for your organization? How much of a cost is it? Help me understand that.

**Expert** [00:18:58]
Yeah. It depends on, obviously, the organization, if they're onboarding new sites. Once you've got a site onboarded, unless something is just glaringly wrong, once it's in there, you're done. It's not really an ongoing maintenance practice. What I could say is it could make jumping from one software platform to another more appealing because right now, if you're in Power Factors, even if their product is awful and you want to go to Bazefield, you're like, "Man, that's going to be a lot of work to transfer that over."

If there's something that can expedite that onboarding and transfer, that could be a selling point as well. I don't know if that's what Packet's even thought about, but part of their sales pitch could be like, "Yeah, if you're unhappy with your provider, this is going to streamline your off-boarding and onboarding." That's a thing as well.

---

**Client** [00:19:49]
Yeah. That was one of the ways this idea came about, this first wedge that I'm talking about, because we've spoken with a number of folks, ex-Power Factors employees, and they agree that a lot of their defensibility comes from the data engineering. They see that some customers want to move off of Power Factors, but it's just difficult for them to. The idea behind Packet is, "You can't do any analytics, whether it's in the cloud or edge, without having a central data model that you own, and we want to give that to our customers." That's the idea.

**Expert** [00:20:25]
Yeah. I think that could be a big one for a lot of people because I agree. That's part of their business model on the software side is like, "We got you, and you're not going anywhere because it's a pain in the ass." I think that that's a great selling point.

---

**Client** [00:20:41]
Got it. The idea here is once you have the central data model, then you can do analytics. Building models is increasingly, I don't want to say trivial, but it's much easier to do. You now have cleanly normalized tags that you can then build an analytics model off of, do ML, etc. Now, the next problem is deploying analytics to numerous sites and keeping it consistent. Now, again, I think this is a tricky question to ask you guys because you're not there yet. You're not doing edge computing, but have you heard or encountered any problems of this sort, managing analytics models running on different nodes across different sites?

**Expert** [00:21:25]
Yeah absolutely. I live in that world right now. The data model piece is tricky because essentially within the model, you have to do the normalization, which it's not that difficult to do, but it is cumbersome. It would be a lot better, especially in the centralized software world, if you didn't have any translation that needed to take place. Again, it comes down to possible human error as well. If you've already done the vetting on what everything is during the onboarding piece and then you're building the model, I think that can minimize or decrease some of the possibilities for error.

The issues are real, and especially when you have a new analyst, then it becomes more internal knowledge as opposed to something that you can just intuitively go in and start analyzing the data. For me to find the tracker motor data for inverter one at site A, that's going to look completely different across all three or four sites. That is something that takes the extra time to train. You're running up against possible error and that's things that are just clogging your brain. Instead of actually solving the problem, you're trying to figure out which tags am I supposed to be using?

---

**Client** [00:22:32]
That makes sense. Do you guys train any analytics models or anything like that, or do you use other vendors for that?

**Expert** [00:22:40]
No, our analytics are all internal. At Clearway, it was internal as well. All the places I feel are internal if you've got a performance engineering team that's capable of doing those sorts of things. I honestly feel like the folks that are using the Power Factors as that's their truth of all of their data, they're at a disservice to themselves and they should probably move their stuff internally. Internal models give you the full control. Turnaround time for implementation and modification of a model through a third party is painful. We're talking weeks to months where it's a couple of hours of work. Internal is definitely better.

---

**Client** [00:23:20]
Right. Can you give me an example of the type of modeling that you do? Can you run me through the process of calling the data in? You gave me some examples, but are you building thresholds? Are you building predictive models? What are you building?

**Expert** [00:23:39]
Yeah. I think the biggest one is probably predictive energy, whether you're extracting data via API from the SCADA itself, or you have it warehoused in a database somewhere, but based on your weather inputs and other items, what is your expected output? That's used for doing your actual versus predictive-type KPIs, where you're seeing how far off you are from where you should be.

It's also for lost energy during downtime events or derates. Where should this piece of equipment have been, and where was it based on what was happening from a meteorological standpoint? There's a trillion use cases for predictive. Outlier detection is, again, a nice use case for predictive modeling as well. We touched on those earlier with yaw misalignment for wind or blade tracker outside of where it should be, things like that.

---

**Client** [00:24:28]
Got it. Where are you building the model from?

**Expert** [00:24:33]
It's usually just a programming language, R or Python.

---

**Client** [00:24:36]
Got it. This is interesting because you guys build your own models. If you wanted to deploy more, let's say, predictive maintenance models on the edge, if somebody gave you the infrastructure to do it, like what Packet is doing, then you would be able to build your own model and deploy it.

**Expert** [00:24:54]
There's access to the data, sure, but I think that what we're doing on the, what we call modeling is more so for reporting purposes. What was the lost energy which rolls into availability? We do the anomaly detection. We can also deploy field ops to correct things when we see, "Hey, the temperatures of this cabinet are a lot hotter than everywhere else. Can you look and see if there's filters that are clogged or something like that?" We can deploy, but we're not actioning off of it in real time.

That's something that I think that could be very interesting from an O&M perspective, where you have more real-time alerts. Again, that's the tricky part about real-time alerts is false positives are costly. You'd have to have a lot of trust in the models.

---

**Client** [00:25:39]
For sure. I think if you got a better sense of what Packet is doing, again, helping you build that core data model and then helping you deploy analytics from a central place on the edge and then enables various use cases like predictive maintenance, alarm management, fault detection, etc. You mentioned that you're being pitched some other vendors and all that. Can you give me a sense of who the main players are in this space, whether they're doing exactly what Packet is doing, or whether what Packet is doing is just fairly more unique? Just give me a sense of that. That'd be helpful.

**Expert** [00:26:17]
I have not heard or seen something that is doing exactly what Packet is doing. I'm sure that there may or may not be out there. The more edge real-time type alerting, the really solid analytics packages, like the Bazefields, are pitching these sorts of things. Again, the validity I have not seen or heard. I don't know, other than in their sales pitch, how well it can actually be used. There are products, I think the other one, GreenBridge.AI have products that they're pitching, but I've never seen them in action. They're not the same level as Packet. They're within more of a centralized data structure as opposed to edge.

---

**Client** [00:26:57]
Interesting. Let's say Packet were to reach out to your firm. Would the company pick up the phone? Would you take a meeting? Are there use cases for which you think this would be valuable for now that you've heard what the company.

**Expert** [00:27:16]
Yeah. We'd definitely. We're pretty open to discussing products that are out there, especially new ones, and seeing what it is. Folks, especially on the new side of a product, can typically pitch a free trial-type deal, depending on what the intensity of getting the equipment out in the field, how that looks, what the integration looks like. Doing some sort of a proof of concept-type deal could be interesting.

Just being able to also see what the interface looks like, what we're looking at when something is triggered, when we're doing onboarding, things like that, to see what everything looks like, how it all works together, and also how it would layer with our current data model and add or make a more robust capabilities on our end. I would be interested in hearing more.

---

**Client** [00:28:01]
Yeah. Are you guys the type of company where you would explore early-stage design partnerships where you can play a role in the direction of the product vision, and in return you get early access probably with a highly-discounted cost and everything, being a first-mover on a platform like this?

**Expert** [00:28:20]
That wouldn't be my decision, but we have done that before. I don't know if we're trying to move away from that because there's a lot more work on our side. We're a small company. We're already really lean on the employee side. For us to spend extra time helping build a product, but we have done it before. Depending on the product, it might be a good fit. I wouldn't lean either way. I would just say it has been done, and we would definitely at least entertain a discussion.

---

**Client** [00:28:48]
Great. Look, the company is in very early stages. If they find a right partner, in my opinion, the business will be well-capitalized, and they'll have a really good, strong founding team. Typically, with the design partnerships, they keep them very structured, and they're very lightweight, I would say, for the other partner.

It's really just feedback, a bit of time just for maybe testing or seeing if the product fits with the mandate that they have and the use cases. Typically, it's not really super hands-on for the other side. Anyways, thanks for your time and your valuable points. Hope you have a great day.
