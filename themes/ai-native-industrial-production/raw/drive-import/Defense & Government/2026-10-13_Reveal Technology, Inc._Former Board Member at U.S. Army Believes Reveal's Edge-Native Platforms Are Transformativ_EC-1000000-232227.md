---
theme: "Defense & Government"
title: "Former Board Member at U.S. Army Believes Reveal's Edge-Native Platforms Are Transformative for Defense Applications"
doc_id: EC-1000000-232227
source_line: "Reveal Technology · Expert Call · Customer · 13 Oct 26"
date: 2026-10-13
company: "Reveal Technology, Inc."
pages: 2 of 2
saved: 2026-10-19T17:29:15.704Z
url: https://research.alpha-sense.com/search?search_id=tmp-0pnbg1kc8uodovl7vbczkp&sort=RELEVANCE&order=DESC&docid=EC-1000000-232227
---
# Former Board Member at U.S. Army Believes Reveal's Edge-Native Platforms Are Transformative for Defense Applications

Company Deep-Dive

DATE PUBLISHED

13 Oct 2026

INTERVIEW DATE

15 Jul 2026

EXPERT PERSPECTIVE

Customer

ANALYST PERSPECTIVE

Business-Led

PRIMARY COMPANY

Reveal Technology, Inc.

SMART SUMMARY

Summary

The interview covered Reveal's technical capabilities, competitive positioning, and adoption within the defense sector, focusing on its edge-native geospatial and biometric platforms. Discussion included the challenges of DDIL environments, procurement dynamics, and the significance of becoming a Program of Record with major military clients.

EXPERT BACKGROUND

- Former government civilian with expertise in tactical communications, networking, and intelligence, holding acquisition certification and extensive experience in military procurement and consulting roles focused on edge computing, cloud, and AI technologies for defense applications.

EXPERT SENTIMENT

- Reveal's technology is considered top-tier in edge environments, particularly for disconnected, denied, intermittent, and low-bandwidth (DDIL) scenarios, due to its robust architecture and rapid data processing capabilities.
- The expert views Reveal's progression from R&D and pilot programs to becoming a Program of Record as a strong indicator of product maturity, stickiness, and long-term viability in military applications.
- Reveal's hardware-agnostic, modular, and open architecture, along with its lightweight, edge-optimized AI, positions it as a unique and highly competitive solution in the defense sector.

TAKEAWAYS

- Reveal's Farsight and Identifi platforms are designed for offline, edge environments, enabling rapid processing of raw drone and sensor data into actionable 2D/3D maps and biometric analysis in under 10 minutes, which is critical for military missions.
- The platforms are hardware-agnostic, interoperable with a wide range of tactical radios and devices, and natively integrate with widely used military tools like ATAK, enhancing deployment flexibility and user adoption.
- Reveal has successfully transitioned from small R&D contracts (SBIRs) to large-scale Programs of Record, notably with USSOCOM and Air Force Special Operations, indicating strong validation and long-term customer commitment.
- The technical challenges of operating in DDIL environments—such as local data caching, syncing, cryptography, and identity management—are significant barriers to entry, and Reveal's ability to address these is a key differentiator.
- Reveal's use of lightweight, specialized AI models for computer vision and biometrics at the edge, rather than heavy, cloud-dependent models, is seen as both innovative and necessary for the operational environments they target.

AlphaSense Smart Summaries are AI Generated

Introduction and Expert Background

Procurement and Usage Context

Technical Capabilities of Reveal

Competitive Landscape and Differentiation

Deployment and Client Adoption

EXPERT BIO

Former Board Member at U.S. Army

Senior Account Executive at Amazon Web Services. The expert is responsible for driving operational growth and business value to achieve mission success through cloud and data-driven solutions.

Prior to Amazon Web Services, the expert was the Data and AI Technologist at Accenture Federal Services, leaving July 2025. The expert was responsible for driving transformation through data, analytics, AI/ML, and cloud-enabled technologies. Earlier, the expert served in executive and technical roles within the U.S. Army — including Chief Data Officer for Army Futures Command and civilian technology expert — and held board and advisory positions such as membership on the Army Science Board and other advisory councils.

The expert can speak to data strategy, enterprise AI/ML and cloud-enabled analytics, cybersecurity and data privacy, systems engineering, and defense acquisition and program management. The expert has 20+ years of DoW experience. The expert holds a Ph.D. in systems engineering and degrees and accolades in computer science, engineering management, cyber security, data privacy law, executive leadership and AI.

View More

INTERVIEW TRANSCRIPT

**Client** [00:00:00]
Thank you again so much for making the time. Would you please be able to provide a quick overview of your background, as well as your experience with Reveal's platform?

**Expert** [00:00:08]
Sure. I hold a PhD in system engineering, a master's in engineering management, and a bachelor's in computer science. I have several certifications in AI, leadership, cybersecurity, Lean Six Sigma, various certificates, and also data privacy as well. I was a former government civilian working specifically in the tactical communications, networking, intelligence area. I left government service about five years ago, and I went to industry. Did various roles in industry along the lines of still supporting the military, but more of a consultant and then in cloud data AI.

When I read the questions, I was really excited because we've dealt with a lot of platforms, edge to cloud, and specifically edge, where you're working in a varied environment where you might not have connectivity. I'll start off also by saying that I can speak extensively on architecture capabilities, edge integration, the market landscape.

I'm familiar with the technology, so I could talk a little bit more in depth, I think, on their technical capabilities for reconnaissance analysis on Farsight and Identifi. Of course, just providing you also some background on things, the capabilities, given this type of environment that they're running this software in. Does that sound good?

---

**Client** [00:01:30]
Yeah. We're trying to get a sense of where Reveal sits within its competitive landscape. Your experience as a customer, what drove you to procure it, how you went about the procurement process, your experience with the product and platform, both Farsight and Identifi. To start off with, when you were in the process, and remind me again, you were in charge of procurement for Reveal?

**Expert** [00:01:53]
I was on the acquisition side of not Reveal. I was on the government acquisition and procurement side. That's what I did. I was acquisition certified.

---

**Client** [00:02:06]
That makes sense. Could you maybe speak a bit more broadly about your experience using Reveal? What drove you to use it? What were the use cases in which you deployed it? We can go from there.

**Expert** [00:02:20]
Sure. Again, I just want to clarify, I didn't specifically use this technology. I know about it. Of course, since then, since I've been gone out of government, I've just been following along on some of the procurements that they've had in this space just because they still deal heavily military. I can probably go through where they have their software, like USSOCOM. They have some Air Force footprint, Army as well. I could talk probably more about how they use it, deploy it, if that's helpful.

---

**Client** [00:02:52]
Sure. That would be great.

**Expert** [00:02:55]
Okay. How far deep in the technical details versus what you guys already know, versus where I can really fill in?

---

**Client** [00:03:05]
I would say we're not technical experts, but we understand the industry landscape, if that makes sense?

**Expert** [00:03:11]
Yeah. Again, please just stop me if you guys are like, "We don't understand what you're saying," or if there is anything you want me to clarify, or if I go too deep into the details. Just let me know. As far as Farsight is concerned, I'm, of course, going to speak from my opinions, it's really created to be used in an offline environment. I can go into the architecture, I think, principles a little bit as well. I think that the way they have architected it to be mobile friendly, edge-native, cloud-native, working in this disconnected, intermittent, low-bandwidth environment is really their sweet spot.

For Farsight, specifically, they have an offline capability, so you don't have to be connected to the network or to a cloud environment to use their software suite for 2D, 3D modeling and tactical analysis. What they do is basically take raw UAS drone sensor data, I believe also including thermal imagery for night operations, and they process it into a quality map in under 10 minutes. I think the timing is key because if you're in a mission, you're conducting a mission, you want that to be as fast as possible. For the processing and the detail of work that they're doing, under 10 minutes is really good.

Of course, we always want that to be lower, but you also want to have the accuracy to make sure that the analysis is useful, and also, you don't want to make any mistakes. The other thing, I think, is also very valuable is the tactical line of sight. They also say that. They can do analysis on building and terrains and elevation, blind spots, helping squadrons to avoid enemy observation. That's very key. I think their helicopter landing zone surveying is probably very unique when it comes to tools in this space. That's really a very specific use case, but I think it's something that is not widely done in this space. That's where they automatically can calculate terrain slope. They have other capabilities.

I think tor the platform itself being hardware agnostic, if you will, the key there is that they're using standard commercial protocols, capabilities that can be used in any hardware. Right now, they are integrated with Android. They have a plug-in with Android, which is very much used in military today. That's a good thing. Their edge transport capabilities.

Really, because Farsight processes raw data, it bypasses a lot of the bottlenecks. That's also where the timing can come in as well because they are processing a lot of this data. They're agnostic to any of the tactical radios that we may have like Silvus, TrellisWare, Harris. That's another good capability, is that they're keeping to like, "We don't care what hardware that you might have, we're using standards to integrate with all of these tactical hardware and software."

---

**Client** [00:06:15]
This all makes sense from a technical perspective, and it's really helpful. My question was, how do you think about this compared to the broader landscape of other offerings? We've talked about them being hardware agnostic. My question is, being closer to the edge, is this common across others in the same ecosystem, or do you find their differentiation from a technical perspective to be more robust?

**Expert** [00:06:41]
This is a great question. I would say in the broader landscape of what they do from a Farsight and probably, more specifically, the Identifi as well, is they are probably at the top of their game. From my opinion and what we've seen, is that there are so many hurdles in working in this type of environment because you have to have the right processing. You have to have the right standards. You have to be able to integrate and interoperate in a way that's very fast, and they do this very well.

If you pull back the covers on their technology, I think that they have really, truly adhered to the architecture principles. In terms of keeping it modular, keeping it open, using standard data formats. The network dependencies, you're always going to have that. The way that they've architected this loose coupling, I think, is very key. I think the standout for what they do is the timing. I think that if you're working in this environment, you do need a robust architecture foundation to help it run. You're always going to be dependent upon that. No matter what software that you run.

I think for them, specifically, the way that they've architected it and the way that they can run it in a denied environment is really key. Especially for their Identifi, where you have a piece of software that goes on the hardware, and so it can really work independent of the network because there is a lot of information loaded on it specifically. I think in the broader landscape, they have done really well. What I've also noticed is that they moved from this R&D like, "We're just going to do pilots. We're going to do some SBIRs, into this part of now, the defense budget."

They've moved from this pilot, "Let's feel this out. Let's test this out. Let's see how this is going to work," to truly becoming part of a Program of Record, which I think is very key when you're looking at this type of technology because that shows that the company has been used in these environments. The soldiers like it. They're getting good results, enough that they've become part of Program of Record.

---

**Client** [00:08:51]
Can you say a bit more about the competitive landscape? How would you map out the space the players in which Reveal fits in?

**Expert** [00:08:59]
I think from a competitive landscape, and I'm not going to name names, but if you look at who is in this space in terms of biometrics for doing what Farsight is doing specifically. Of course, there are companies that can do this type of work, but I think that they're very unique in this space just because of the edge components that they have to deal with. I think that that's really their sweet spot, is they really figured out how to be mobile-friendly. They've really figured out how to work with any hardware, which is very difficult when you're not connected and you're not getting that data back and forth.

As far as the landscape and the competitiveness, what's really telling also, I think, is the level of contracts that they've been awarded in this space. Geospatial, I think, is very hard, and especially to do it at the edge. There are capabilities that can work disconnected and offline. Especially for Identifi, doing biometrics at the edge on a mobile device in the time that they can do it. They're definitely competitive in this space, if not one of the top vendors in this space.

---

**Client** [00:10:08]
Maybe you could share with us. In your experience, if somebody's doing an RFP, there are usually these three people that typically are included, from your perspective.

**Expert** [00:10:18]
From a competitive perspective. If I can think about that, maybe we just come back to that. I'm really thinking of geospatial and biometrics software. I can tell you top vendors in this space, but I just want to make sure I narrow it down to the right.

---

**Client** [00:10:36]
Yeah. If I myself am looking at finding a solution for that geospatial and topology, who am I normally going to make sure I evaluate in that context, would be helpful probably to revisit.

**Expert** [00:10:49]
Yeah. Number one off the top of my head is Leidos. I don't know the specific technology, but they are definitely in this space, especially biometrics. In terms, I think, of just the big companies, I would say that they're probably in the competitive landscape. I'll think of a couple more.

---

**Client** [00:11:09]
It would also be helpful from a technical perspective to understand a bit more. You've talked a lot about how difficult it is to do what Reveal is doing at the edge in these denied environments. Can you help us understand a bit better? The context behind this question is I'm trying to understand why couldn't a competitor do exactly what Reveal is doing? How hard would it be to replicate?

**Expert** [00:11:34]
That's a great question. I love this question, by the way. First of all, there's not a lot of companies that specifically work in DDIL because it's a very hard problem. I think when there is a company that adheres to architectural details that can work, have easy ways to integrate with the mobile devices that are deployed today, for example, it's a lot of time. It's a lot of money spent. It's a lot of research and development that goes into this space to make sure that you are providing accurate and timely results.

I think that deters a lot of companies away from that because you're going to make more money probably being very good at some of the bigger problems in the spaces where you are connected, whether that's a lot of data or it's a lot of imagery or it's running heavy AI, LLM. More people may do it, but you can probably find a niche in that space and not spend so much R&D. We always say the disconnected environment's always not forgotten, but it's a space that not a lot of people really want to invest in because it's a very hard environment.

I think that for Reveal and some of the technologies that they have, you can see just the work that they've done to progress from being a small business, having a small business like IDIQ, or we call it a SBIR, all the way up to getting into a Program of Record. I think it's a very good metric at least to say that they transitioned from this R&D to something that can be deployed and trusted in this environment. It's an environment that you have to think through so many things like stale data.

If you're offline and you're caching data locally, making sure that it syncs back to the greater enterprise when you do get connected is really a very hard problem to solve, especially with the type of data that they're doing. Whether it's map data, they have drone data, they have to make sure that they're syncing when they connect.

I think the cryptography and the identity of capabilities that they have also is very difficult. You have to make sure that you have some kind of local identity and key management store that if you're not connected, that it's still running and that you can have users' credentials and authenticate locally, which is also a very hard problem to do because you're running things while you're offline. You're not being able to pull current data back and forth.

The timing, I think that they call out under 10 minutes, which is really very good. They can take all these results and all this data that they're caching and be able to provide some kind of data back to the user in a very short time frame. You always have to look at the timing of how long it takes, and then use the trade-off between accuracy. Is it the right type of data? When you sync back to enterprise, how fast is that going to do the syncing?

I think they also do a very good job. One of the other areas that you want to look at is size, weight, and power. They're processing 3D models, or they're running facial recognition algorithms. Their Identifi software locally, it requires heavy GPU and CPU processing. I think that the way that they've been able to overcome some of that is that they've done a lot of testing with ruggedized hardware at the edge. Again, it takes a lot of R&D, takes the users wanting to test out this software, and that they see some potential in it that they're going to help this company do the testing in these types of environments.

I think also probably in this, the DDIL or the disconnected environment, I could say transport, networking, all of these things, I believe even having zero trust execution in a disconnected space is also very hard. I think that they've thought through all of the hurdles or just due to environment. Working in this disconnected environment, I think they thought through it very well. I think that not only the contracts, but also the soldiers using it or the end users using it, they've seen a lot of value. I think the way that they have architected it, it goes to show that they have spent some time and money to perfect what they've been doing. Does that answer your question?

---

**Client** [00:15:50]
Yeah, I think so. Thank you. Can you maybe help us understand a bit more? Once Reveal is actually deployed and it's being used out in the field, what makes this product really sticky, and how difficult is it to then switch away from using their tech? I'm just trying to understand how sticky the platform is once the end user actually starts to use it.

**Expert** [00:16:14]
Okay. For an example, USSOCOM adopted their Identifi platform as a Program of Record just recently. I think it was probably just a couple of months ago. They're transitioning it to be institutionalized fleet-wide, which means they're going to deploy it across their organization. In terms of sticky, that's where you want to be because SOCOM is one of their premier combatant commands for the military. In our space, we know SOCOM is using it because they are on the critical edge, and they're at front of the missions. Their software that they're using has got to be exceptional. It's got to work. They are in very precarious situations and environments in countries where the threat is very high.

For them to say, "We are going to deploy this software and transition it across their fleet is very, very important." Just looking at who their client is, the client was able to make this commitment and basically put it through its paces before they were going to award it, acquire it, or even put it in the hands of the soldiers or the users for their safety. It is one of our stamps of approval because this is one of their premier units for the military.

I think in terms of it being sticky, that's the type of examples that really makes you be like, "Okay, this is a viable company, a viable software, a viable capability because of this client that they have." The ways that they're using it is in austere environments where they're not going to always have connectivity, and they are under heavy threats. I think just given that landscape alone makes you think like, "Okay, this is sticky. It is now part of a Program of Record." Acquisition-wise, that's where you want to be because then you have a long-term commitment from that client.

Most of the time it's four or five years commitment, and then that can get renewed. The commitments are yearlong, or years long, depending on the contract. You're there for a little while. You're not just there for a few months, "Let's just do this pilot." You are there like a long-term capability. Over these years, you are going to be asked to improve the software, take some of the real-world use cases, implement them. The software, you can say, because they're part of a Program of Record, that it's only going to get better.

---

**Client** [00:18:36]
Can I ask a question on that front, which is in the SOCOM example, which is really helpful, by the way. As you said, it's probably little, if any connectivity, the need for very high precision, quick turnaround. Do you feel like that is more the edge case? If I need a vehicle, that's the Ferrari. They need a Ferrari, but most of the market may need simpler geospatial solution, and therefore, I could use something that's maybe a little bit less sophisticated, cheaper, or doesn't have all the bells and whistles, or is that not the case?

**Expert** [00:19:10]
That's another great question. Very interesting. I would have to say it depends. For a unit like SOCOM, they want bells and whistles, but the capability has got to be, how do I say, exquisite for what they need it to do. They have the funding. They can get the funding because of their mission to be able to afford that. Now, another organization that may not have so much money can say, "Hey, we can just get by with this 3D map. Maybe we don't need GPUs. Maybe it's just CPUs. Maybe not as robust infrastructure. One, we may not have it, and then two, we don't have the money to go out and buy it."

Again, I think it depends on the client and who else is procuring this. One thing from an acquisition point of view, we always see that depending on the organization that's using it, people will start to adopt it because they are going to see, "Oh, okay, SOCOM is using it. If we don't have as much money as that organization, can we start to negotiate licenses? Where are the areas that we can negotiate?" Everybody wants the best tech, especially if we know a unit like SOCOM is using it. There are other trade-offs.

Maybe perhaps looking into how does Reveal sell their software. Is it based upon CPU? Is it based on user seats, how many users they're going to have? Where are their licensing costs, where there's some leeway? Is there a way to do an enterprise-level agreement where you can save some money? Like I said, I think we always want the best tech and if this is given where their posture is and who they've been selling to. As an acquisition officer, you're always like, "Hey, where is there room to negotiate?"

Like I said, there are other competitors in this space. You've got other people that do tactical edge 3D mapping. There are companies, Esri has a Drone2Map. Leidos is in the biometric space. You do have competitors in this space. Again, I think it's some of the uniqueness that Reveal has, that if SOCOM is using it and some other entities across the military, not just maybe the Air Force, then you're like, "Okay, that could be the premier software, and then if I don't have the money, how else do I negotiate that?"

Maybe looking at their business model a little closer can help you get there and try to figure out, "Okay, if an organization can't afford it, what is their wiggle room trade-off or just a different business model that they'd be willing to provide users?" Did that answer your question?

---

**Client** [00:21:48]
Got it. Thank you.

**Expert** [00:21:51]
Okay. One other thing I would offer up as well is, because I was looking, what AI can provide in this space is also an area that is very important that we understand. In the tactical environment, you don't have a lot of the size, weight, power that you would if you were connected, sitting in a building, and you have all these resources at your fingertips. At the edge, you know that you are denied in some way. Whether that's you don't have a lot of the hardware, you don't have a lot of the storage. You may be disconnected and not attached to connectivity. Some way that you are denied, you're degraded.

When it comes to AI, you think like, AI, you need a huge infrastructure to be able to process a lot of this data, run the models. What Reveal has done is that they haven't built a single massive general-purpose model. Instead, they've used very specialized and optimized things like computer vision, deep learning, and I would even say edge-native algorithms that are lightweight. I think that one of the things that makes them stand out in this space and against their competitors is the way that they're using AI.

The lightweight they're using, which is very clever, actually, the way that they're using, I think, the computer vision and some of the AI techniques, especially for the edge space. They've almost purposefully, I'm sure purposefully, have created an AI capability that can run this way based upon who they're trying to service as their clients in this space. Because they're not running these heavy generative models, puts them also in a very unique position.

I think that users in this space want it, but they also know that there's a trade-off to having running AI models. How well can it do locally? Do I need connectivity to run it? Is it going to be accurate? I think that the way that they've architected it is highly useful, and it's also very clever the way that they've deployed it. That could be one of your factors.

---

**Client** [00:23:56]
As we've talked to a number of companies using building AI at the edge capability, either small models, highly tailored small models, they fit larger numbers of them on a GPU, which may drive either a lower latency. It seems to me that anybody who's got a successful AI at the edge capability has done that. From what we've seen, do you think they're doing something beyond that, or are you just calling out those core components for somebody that's using a traditional like, "Hey, send everything to the cloud-type processing model"?

**Expert** [00:24:27]
Yeah. I think that one is very important, that they are using AI efficiently at the edge. I think where they may go a little bit further is the type of data that they're dealing with. Their on-device translating faces, fingerprints into a compact mathematical vector, embeddings, which is a very different type of data that they're dealing with than just saying that we're just running regular language processing, regular data components. I would focus on the type of data that they're doing this with, which is not biometrics, facial, fingerprints, voice. It's all very specific. You would expect the regular models to be very heavy because you're running heavy computer vision. You need the compute, and you need timeliness.

When you're connected, you're like, "Okay, it happens in an instant." I think the mathematical embeddings that they have to do disconnected because you're not connected, and you're just scanning somebody's face, like a perpetrator's face, to figure out who they are, where they're from. Are they in this database disconnected? You've got to do all those vector embeddings very quickly and accurately at the edge with no connectivity is impressive. I think that maybe just look at the type of data that they're working with and the high complexity of what they need to do with it, especially in their Identifi capability, is very impressive. That was a great question too.

---

**Client** [00:25:57]
We've talked a lot about how unique it is that they're hardware-agnostic and a number of others in the space are not that way. In your view, is there any limitation or any drawback of them being hardware-agnostic because they're able to work at the lowest common denominator in terms of hardware? Do they have to sacrifice anything in terms of technical capability?

**Expert** [00:26:18]
That's another great question. In the military space, they are moving fast. They're making decisions based upon budget. You want to be agnostic as you can be. I think what we've seen is there is an optimal pairing between their software and hardware that they would like. I'm sure if you ask them, "What would you rather run on?" they would be able to tell you. This is what optimal pairing would be. Whether it's a Klas Voyager or a Dell, I'm sure they would be able to tell you, "This is the configuration that we need to run optimally. Here's the CPUs we need. Here is the power. Here is the storage. Here are all the things that we need to run optimally."

There are so many variations of hardware in this space, whether it's mobile or it's physical servers. They could probably run on many different configurations. I think every company has their optimal like, "Here's what we would want you to have to be able to do this." I think, though, through a lot of their R&D and through just some of their pilots that they run, they probably have experienced a lot of different versions, a lot of different configurations. They probably optimized the software as much as they could, but also, like you said, keeping the low-level minimum of configurations that they probably can run on.

I'm sure that if you ask them, they would be like, "Here's what we would like to be able to run this very quickly." One of the things that is probably very good, interoperability, I think, is very key. You want to say, "I can be interoperable with these types of other pieces of software." Whether it's legacy, whether it's next-gen, you want to be able to have that API to be able to say, "We are native, and if we don't have it, we can build it. That is not a big deal."

We have seen some companies that show us their software, and we're like, "Hey, can you integrate with one of our military systems?" They're like, "Yeah. It's going to take three months for us to go build that API." You're like, "Well, if you designed this properly, it should not take you that long." I think one of the key components that they have is looking deep into the architecture, you want it to be a modular open system. That is really where the military is trying to foot stomp. You've got to be able to have software portability, decoupled architecture.

What Farsight does specifically is they have an ATAK plug-in. I don't know if you guys have heard of this. It's Android Team Awareness Kit, so it's basically an Android device. Identifi works with it. Farsight works with it. Farsight is fully integrated with this plug-in for ATAK. That's what a lot of operators use today, so that 3D terrain renders directly onto this device. You don't need months to be able to integrate with it. It's already native to the capability.

I think it's things like that they've done really well to think like, "Okay, what is the most propagated, deployed, mobile handheld out there?" It's ATAK. It's government-owned. ATAK is government-owned. They have said, "Okay, we're going to invest in natively, plugging in to an Android device and making it very user-friendly." I think just some of those design principles that they have already incorporated, and they have XML protocols that could easily integrate with legacy and next-gen systems as well.

---

**Client** [00:29:49]
Are there a set of geospatial mapping solutions that integrate or come pre-installed, or with ATAK already today, making them an easier choice for somebody to pick?

**Expert** [00:29:59]
Yeah. I think 3D terrain rendering, they have RESTful APIs, and they use JSON, so making it easy to connect with, whether it's vehicles or servers. They have very lightweight protocols that makes it very clean to integrate with legacy binary integrations as well. I think they do that right out the box. They don't have to build that.

---

**Client** [00:30:24]
Sorry, my question maybe was a little different. Meaning, as an alternative to Reveal, would an ATAK device come preinstalled with some lightweight geospatial mapping capability? Like, "Hey, there are five geospatial mapping tools that integrate already easily out of the box if I wanted something besides Reveal."

**Expert** [00:30:44]
I believe that it has some geospatial capabilities, but it's very basic. I think that to get anything that is going to give you the capabilities like geospatial analysis, like what they do with the landing zone biometrics, none of that comes with ATAK. ATAK is just a very generic device with, I think, very baseline capabilities. I think for these use cases that you're going to use this type of capability, you have to bring it and integrate it with ATAK. ATAK itself supports offline or even online base maps. They don't necessarily have to bring the mapping engine, but they have to bring all the algorithms and the protocols to be able to render all of that data on the map. Does that make sense?

---

**Client** [00:31:30]
Just quickly pivoting back, you mentioned earlier that SOCOM, as the customer, really indicates how strong Reveal's tech is. Are there any other customers you're aware of that have procured Reveal that you would also consider really indicative and validating of the tech as well?

**Expert** [00:31:47]
I believe that they have contracts with the Air Force Special Operations community. I think you can probably look it up as well, just to be more accurate. I believe that they are deployed within the Air Force, in the Army, at SOCOM. I know the SOCOM thing was very recent. I want to say May or June that it happened. They did do some SBIRs, from what I remember. I think they had an SBIR Phase III that was quite big, actually. I think it was over $100 million. I want to say it was with the Air Force, or at least it was through the Air Force contract.

They had another SBIR with the Air Force. They have an Air Force, I think it's the Special Operations Command. They have a contract with them as well. I believe in R&D, they had a contract with the Marine Corps in their Warfighting Lab. It was like $3 million, but I think that was more of when they were more on the R&D side. I think that they've had considerable progression, which is good for them. They went from having some contracts as little as, I think, it was like $3 million, all the way up to $104 million. The SBIRs go away. They have to transition into a Program of Record or else they die.

Just showing that they are now a part of a Program of Record that does get budgeted for at least five years in the budget cycle, that's really where success happens. The other thing I would also tell you, maybe you have already done this, but look at who their partners are. Any good software company has partners. I think that partners that can either bring them into a Program of Record that they're not necessarily a part of.

For example, if Booz Allen is like, "Hey, we are on this biometric project. We've got some holes. We have some gaps. We would like you to come in, do some demos. Let's take it out to an exercise fielding. Let's test it out." Booz Allen can pull them in that way as well into their contracts, in with their clients. Leidos, the same thing. I think just understanding their partnership landscape and where they fit in the sector that they are in with geospatial and biometrics could also set them apart. Instead of being competitive, they are now a partner.

It's a very, very good technology. I think, in the space, it's very hard. It's a very, very hard space to be in. It takes a lot of R&D. It takes a lot of partners just to be willing to put them on their hardware, bring them into the architecture, really test it out. It would be interesting to even find out what exercises they've been a part of, where have they really tested this.

Success comes when you become a Program of Record. In the acquisition community, that's the gold star. That is, somebody deems that you're worthy. You've met cost schedule performance. You're going to improve. You become now a partner of not just that client, but of other organizations that are affiliated with it. Now you've become a partner. You've become like, "How do we make this better? How do we grow?" Once you're inside the wire, as we say, you get to find out all the unique business cases. You find out all of the use cases that you would not necessarily have access to.

Now, for example, if they're with SOCOM now, SOCOM is going to open up the kimono and be like, "Okay, here's some of our really unique cases. Can you help us solve this?" Like I said, I think it makes them competitive for becoming part of other ecosystems and other organizations because of what they do and in the space that they've just succeeded becoming a part of.

---

**Client** [00:35:48]
Thank you again so much for the time. Have a great rest of your day.
