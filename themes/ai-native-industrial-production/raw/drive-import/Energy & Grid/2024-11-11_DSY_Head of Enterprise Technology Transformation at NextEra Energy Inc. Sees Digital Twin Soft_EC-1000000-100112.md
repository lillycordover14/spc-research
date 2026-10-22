---
theme: "Energy & Grid"
title: "Head of Enterprise Technology Transformation at NextEra Energy Inc. Sees Digital Twin Software as Key to Reducing Wind Farm Costs and Improving Accuracy"
doc_id: EC-1000000-100112
source_line: "DSY.FR · Dassault Systemes SE · Expert Call · Customer · 11 Nov 24"
date: 2024-11-11
company: "DSY"
pages: 2 of 2
saved: 2026-10-19T16:54:46.736Z
url: https://research.alpha-sense.com/search?search_id=tmp-0pnbg1kc8uodovl7vbczkp&sort=RELEVANCE&order=DESC&docid=EC-1000000-100112
---
# Head of Enterprise Technology Transformation at NextEra Energy Inc. Sees Digital Twin Software as Key to Reducing Wind Farm Costs and Improving Accuracy

Company Deep-Dive

DATE PUBLISHED

11 Nov 2024

INTERVIEW DATE

13 Aug 2024

EXPERT PERSPECTIVE

Customer

ANALYST PERSPECTIVE

Investor-Led (Buy-Side)

PRIMARY COMPANY

DSY

SMART SUMMARY

Summary

The interview covers the end-to-end process of industrial drive selection, integration, and simulation in wind power projects, detailing the use of digital twin technology, simulation software, and data-driven maintenance strategies. The discussion also addresses procurement practices, software choices, and operational challenges in managing wind farm technology.

EXPERT BACKGROUND

- The expert has extensive experience in technology transformation for wind power projects, focusing on the integration, simulation, and maintenance of industrial drives, with significant involvement in both the U.S. and European markets.

EXPERT SENTIMENT

- The expert views digital twin technology and advanced simulation as essential for reducing O&M costs, improving predictive maintenance, and optimizing wind farm operations.
- The expert expresses a preference for high accuracy (aiming for 97%) and granular, cloud-based data integration to enable better decision-making and minimize unplanned downtime.

TAKEAWAYS

- The procurement and integration process for industrial drives in wind projects is highly structured, involving multiple stakeholders and a rigorous RFI/RFP process, with criteria including cost, digital integration, O&M models, and data accessibility.
- Simulation tools such as Siemens Xcelerator, Ansys, Dassault Systemes 3DEXPERIENCE, and Emulate3D are used at various stages, with cloud-based digital twin solutions being standard for ongoing operations and maintenance.
- Granular, real-time data from sensors is critical for predictive and preventative maintenance, with simulation models used to optimize performance and minimize costly downtime.
- Python is extensively used for custom simulation, anomaly detection, and data visualization, supplementing standard tools like CAD and MATLAB, especially in prototyping and lab environments.
- Challenges with OEMs include complex warranty clauses and lack of transparency, which can lead to unpredictable O&M costs and difficulties in timely support and customization.

AlphaSense Smart Summaries are AI Generated

Overview Of Wind Industry Processes

Differences In Oil And Gas Industry

Simulation Tools And Their Applications

Digital Twin And Maintenance Strategies

Use Of Python In Simulations

EXPERT BIO

Head of Enterprise Technology Transformation at NextEra Energy Inc. The expert can speak to energy and utilities in detail with a focus on nuclear, fusion, solar, thermal solar, waste to electric/gas, oil and gas, global oil both demand and supply and the North American pipeline. The expert can also speak to implementing simulation solutions, drive lifecycle and industrial drives in detail.

Head of Enterprise Technology Transformation at NextEra Energy Inc. The expert is responsible for translating strategic business objectives into actionable IT plans and roadmaps, digital transformation initiatives, optimizing processes and enhancing customer experiences. Collaborated with Federated IT teams to provide directions on day to day technology operations. The expert engages with Business unit leaders to provide updates on the operational. the expert manages IT infrastructure services delivery, ensuring reliability, security, and operational efficiency. The expert strategically managed the IT budget (capital & operational) for maximum ROI, leading annual budget proposals and approvals. Collaborated with vendors and supply chain for effective sourcing and negotiations. Implemented robust cybersecurity measures to safeguard IT assets, data, and information systems. Partnered with executive leadership to integrate technology solutions that fuel business growth. Actively tracked emerging tech trends, assessing their potential impact on the organization. Built and nurtured relationships with key technology vendors and partners. Effectively communicated IT plans, policies, and changes to stakeholders across the organization. Led change management initiatives for successful technology adoption and system upgrades. Provided regular reports to the executive board on IT performance metrics, project status, future solution roadmaps, and investment plans.

The expert can speak to energy and utilities in detail with a focus on nuclear, fusion, solar, thermal solar, waste to electric/gas, oil and gas, global oil both demand and supply and the North American pipeline. The expert can speak to manufacturing for both B2B and B2C and can speak to supply chain and systems.

View More

INTERVIEW TRANSCRIPT

**Client** [00:00:00]
Thank you for taking the time to speak with me today about digital solutions of industrial drives. To start off, could you please give us a quick overview of your background and experience in this space?

**Expert** [00:00:12]
Yes. Typically, the way the process starts is, I'm going to split this into two different industries. One is oil and gas. Oil and gas is separate. Let me focus on wind, which is my current industry specialization and then we can go to oil and gas as you desire. Typically, in wind, what happens is, you start with project assessment. The project assessment is initial assessment that you do where you have to create the technical design requirements and submit it to the regulators, depending on which market you are going to implement the wind power, and to which grid.

I've extensively worked in Europe and U.S., but in U.S. and Europe, there are slightly different process. Whatever my response is primarily for U.S. Once we start with the initial assessment, we call that as the initial project plan, it's called IPP. When the initial project plan gets approved, then we start the feasibility study. The feasibility study talks about the overall end-to-end feasibility of the wind farm, including EPA impact and all the stuff, and during this time, we make the list of all the parts that we need, one of them being the drivetrain integration.

We send out RFI. At this stage, we send out RFI, which is request for information. Parallelly, what we do is we build a finance business case, and sometimes, we hire a third-party company to do the requirements definition and sometimes we do it after depending on the scale, complexity and the technology used.

Once the RFI is sent, then when we receive the response, we shortlist it. Typically, we send to anywhere between eight to 10 industrial drive manufacturers and then we shortlist them. Then we release the RFP to the smaller shortlist number.

---

**Client** [00:01:58]
You mentioned you shortlist them. What is the basis of the shortlisting?

**Expert** [00:02:02]
Typically, our engineers, they look for the fitment of the OEMs solutions to our requirement. We have a standard set of 10, 15 industrial drive manufacturers across the globe. We know who, what capabilities they have because they've been doing business with us for a long time. Over time, we built a dossier on them, so we know exactly who are these people, but the reason why we still go through the RFP is to give a fair chance to everybody to ensure that they present their response, and most importantly, we learn from it because the technology keeps changing.

The best way for us to learn is to go in an RFP mode where most vendors will give a much detailed representation of their product and for other engineers, it is a learning opportunity too. That's the reason we conduct, and by the way, we do this almost every two years. It's been going on like that for the last 25 years, because industrial drives have long lead times to order and procure because many of them are custom-built.

At the RFP stage, here's a typical number. Let's say, if we send a request for information of 10 OEMs, we typically shortlist five, which is our standard ratio, which is 50%, and then we send the RFPs to five, and from RFP, we shortlist two. We shortlist three, two and one. Sometimes, depending on multiple projects where we try to get economies of scale, if two different projects in two different locations needing the same type of drive, we may shortlist two different vendors, and that might be purely because of pricing, it could be purely because we can look at having de-risk the delivery.

In some cases, for multiple sites, we might just select one vendor to negotiate economies of scale. In terms of the criteria we use for short selecting, cost is a big criteria, digital integration, O&M contract model, then we look at the financing model, then we look at the warranty and the parts and coverage for warranty. We also look at the amount of local content in the design versus imported content or outsourced content in the design. Then we also look at our ability to collect technical data from the drives that we can feed it to our software like Digital Twin.

We have a very big lab in Idaho, Boise. There, we actually use this data to do a lot of testing and we analyze efficiency and stuff. Those are the key RFP shortlisting criteria. Once that is done, after the RFP is shortlisted, we invite the shortlisted members to come and implement their drive system, design and engineering, be the prototype.

Before they start the mass production, when I say mass production, typically, a wind site, for example, let's say, if I am installing a 500-megawatt capacity wind turbine in a wind plant, you're looking at 50 to 75 to close to 100 drives. Before they start to build so many trials, we ask them to build a prototype.

The prototype goes to our prototype wind farm, and then there we actually test it, and we basically do the testing, results collection and then once we accept it, and if there is any modification to the design that we need or any potential cost impact, we tell it to the OEM, they do it, they will let us know if there is a cost impact to the original proposal or if there's a cost reduction. We use that mechanism to also negotiate price.

Then we start with testing and acceptance of prototype, then we give them the go-ahead for mass production, it's called scaling the drive, and then we do the site preparation, installation, where site preparation and installation is where the OEM actually ships the drives to us. They are responsible for the logistics from door to door, which means that the burden of safety and the burden of proper delivery falls on the OEM, they deliver it to the wind site, but taking it from the logistics provider and putting it in the wind site, it is all our responsibility.

There is a point where the ownership and the risk shifts from them to us. Then we go into the site preparation model where the site has to be prepared, where you do subassembly of the drive before it can be fully commissioned. Once we do the commissioning of the drive, then of course, once the windmill is built out, we test it. Then we integrate that with our PCC, which is PCS, which is plant control systems. Then the necessary training. Parallelly, there's also training happening to the operators so that they understand how to maintain it.

Then we do monitoring, and optimization. Initially, when we are running the windmill for the first three months or two months or less, we run something called trial mode, where we really don't feed the power to the grid. We actually generate the power. We store it in the batteries because the windmill has to get optimized before we can start predicting how much power it is able to produce and how much reliability it has.

For that, we do a lot of data collection and that's where the digital twin comes in play, where we collect that data and our central team, which is in Florida, they actually analyze the data and perform simulations to figure out what is the test model, what kind of production load we can put on the drives and then, of course, it kicks in into maintenance and support and maintenance and support is multiple models.

Depending on the size and scale of the farm, we may buy O&M from the OEM, or we may outsource O&M to somebody else. If it is a very small or a critical one, we tend to do O&M ourselves and then we continuously improve over time to improve the efficiency.

---

**Client** [00:07:46]
That was really helpful. You gave me a very detailed answer to more understand. One, you mentioned where you have the RFP model and then you select the drives and some criteria you have. The decision is purely yours of connecting the vendor.

**Expert** [00:08:01]
Well, no. There are multiple stakeholders who are involved here. My responsibility is from a technology standpoint because many of the drives are nowadays operational technology, which is software-driven and hardware-driven.

My team comes in. We primarily deal with OT components drive integration with our overall plant control systems, which is software and then digital twin solution, the data flow, capturing of data, ensuring the network is good, ensuring that the digital control panels, which has got the HMI, which is human machine interface for each windmill is installed and they're connected to the network, which is GSM network.

---

**Client** [00:08:41]
Yes. My question is either your company is responsible or does the windmill.

**Expert** [00:08:46]
No. My team and my role is to decide on that portion. There are multiple stakeholders. For example, the engineering team is a separate team, and they actually basically look at the parts, whether the parts is good quality, design is good quality and all the stuff.

Then for example, there is an EPC team, engineering, procurement and construction team. They take care of dealing with the site erection contract. There are multiple decision-makers. Typically, up to five decision-makers are involved. We come together. Each of us have to make a decision in our area, which consolidatedly decides which vendor we want to go with.

---

**Client** [00:09:25]
That makes sense. Let's move to oil and gas. Is it the same in oil and gas? Or are there minor differences?

**Expert** [00:09:31]
See, oil and gas is a very fragmented process. The reason why it is a fragmented process is unlike where the number of use cases of industrial drive are very limited and has been same for a long time, oil and gas is you have different type of players, you have different use cases, different sizing processes. Oil and gas also require a very high O&M because of the way it is there, but typically, when you're looking at mature mills, you're looking at industrial drives that drive their exploration pumps, their rigs and stuff like that.

As far as the procurement process is concerned, I have worked for some of the large oil producer like Saudi Aramco, Phillips and BP. I haven't seen them having the same process. Most of the decision on the industrial drives is really run by the project. In fact, they don't even involve technology teams in oil and gas. It's all done by the engineering procurement.

If the process that I laid out, probably the initial process, it will be slightly shorter because oil and gas companies don't require much of regulatory review like power companies, so they can get started with the project quickly enough after they get sufficient EPA approvals. The EPA approvals are needed. They don't have any dependency on the drive because they don't ask for the information like the power generation regulators do.

Your overall lead time for the first, let's say, five to 10 steps of the process until the RFP drafting, probably you're looking at 25% or 40% shorter lead time as compared to the process I told you for wind power. Then in terms of the piloting and prototyping, this is a step that typically is a function and size of the project. Let's say, for example, I would like to say Shell. If they choose to outsource the build-out of the rig to a third-party, then it is the prerogative of the third-party to do the prototyping or not because it all comes down to cost and speed of enabling the well.

Prototyping actually takes time. The power-generating companies, there are regulatory requirements where it goes through permitting process, so there is a luxury of time a little bit, even though they hate it, but for O&G companies, they don't have the time. They have to make sure that they get the oil out of the ground ASAP. Then, of course, it goes through the testing and acceptance, then you have drivetrain integration. Also, there is a lot of different custom design build-out that happens, especially for offshore rigs.

If you're talking about offshore rigs, you may see a very different custom build because these are very, very complex designs. Most offshore rigs, as you know, they are multiyear programs, which requires custom design and the other part of digital twin development, maintenance support, these are already started.

---

**Client** [00:12:25]
That is helpful. Let's move on to simulation and let's talk about it in detail. Let's talk about wind itself because that's pretty much the best. What simulation tools are you using at each stage. We are going to talk specifically with respect to drive.

I want to understand if you're using software to model the drive behavior before commissioning, like in the design phase and then during commissioning and also after commissioning where you said you collect the data and maybe to perform operations and maintenance, so can you explain me where all simulation is used in the drive life cycle? Maybe if you can point out to me some software also, it would be helpful.

**Expert** [00:13:07]
Yes. Let's start with the software, then I'll tell you how we use it. For example, we use Siemens Xcelerator. That's a very commonly used tool in power generation. Then you have Ansys. Ansys is a world leader when it comes for digital twin simulation tool testing. Then there's another company called DSL. It's called Dassault Systemes, a French company. They have a product called 3DEXPERIENCE, which actually provides quite a good digital twin capability. Then we have Emulate3D from Rockwell.

These are some of the softwares we use, but then there are many other softwares, which are in the market, but this is something that you will mostly come across in the context of industrial drives, especially in the U.S. For example, Dassault Systemes, DSL is used extensively in Europe because it's a French company. It all depends on the company capability. Now, with that said, you also have to understand that some of the drive manufacturers in the case of Siemens, they also have software. They also develop software. We have companies like GE.

We have ABB, then Schneider, and then we have Nidec. These are all digital drive companies who also happens to have software. Sometimes, they throw in the software free of cost to us, and we choose to use it, but we have standardized digital train across some of the softwares that I said. Now, typically, what happens is pre-commissioning simulation happens from the prototyping data, which the OEM gives us.

The OEM says, “Hey, we have run our prototype. It is a sample data. Now try to build your digital twin and then tell us what you think about it.” That data will have a lot of errors, will be just approximation, but that gives us a good idea of what is the output the drive can produce based on the sensors that are put on the trial.

---

**Client** [00:14:58]
The data that the OEM gives, they give it in the form of a data sheet or is it in the form of a model, which you then extract into a software?

**Expert** [00:15:07]
Basically, I will tell you, typically, it comes as data dump for us. They will give us a link to their server. We go and we basically say, “Okay, hey, you know what? This is where the data is.” We download it, we load it into our software, and we run some simulations on it. Nowadays everything is cloud. They don't ship us any CD or anything. They will give us a location in their cloud, and we go fetch the data, download it, and then we ingest that into our digital twin solution.

---

**Client** [00:15:36]
Yes.

**Expert** [00:15:37]
In the pre-commissioning stage, we are primarily focused on the prototype data and the test results. What we analyze there is whether the outputs are within the tolerances that we want, whether we have sufficient data points or the granularity of the data points that we want, it is getting generated, and number three is basically whether we are able to simulate digital train with the given data points. If it is not, then we actually tell them we need these additional data points.

The OEM then configures the drives and the corresponding sensors and the corresponding software that is sitting on the embedded sensors to fetch that information. That's a pre-commissioning. During commissioning, typically, the digital twin data that we collect is site-specific. The reason why we do it, actually, the digital twin data that we collect is visual data, and some bit of three-dimensional scanning, which is not produced by the drive sensor. Actually, we physically send a crew out for each windmill.

We put scanners, 3D scanners, profile scanners, and we take photographs. The reason why we do that is during commissioning, the parts are all exposed. We know exactly which part will go where and we catalog each windmill. That will then go into our digital maintenance manual for the wind tech, like after the commissioning has started, before we dispatch a wind technician to the site for any issues, repairs or maintenance.

The wind technician actually goes through the digital visual library, learns and understands what is put on the windmill before they are dispatched to the site. We also use that for training of our local technician who are placed all over the country for different sites. We have something called hub-and-spoke model, so our O&M team, operations and maintenance team is in a hub where there are multiple solar farm, battery farms or wind farms that are surrounded. Depending on where we need to dispatch the tech from the hub, they would go to spoke.

The spoke will be one of these plants. Let's focus only on the wind farms. For these hubs, they become a digital catalog, which is used by the techs to learn and understand and diagnose the problem before they actually go to the site. Because in the site, sometimes the connectivity is poor, they will not be able to download rich three-dimensional drawings into their system, so that's one of the limitations why we have it in the hub. Once we have commissioned it, I told you earlier that there is typically anywhere between 30, 60 or 90 days of trial run.

We collect a lot of production data. There we basically trial the windmill till it achieves a good level of optimization, any fine-tuning that we need to do, and then basically, that information is collected as what we call initial training data or what we call base train data. The base train data is used in the digital twin, and then we continuously improve the data using simulation software. Why? We want to understand given the wind speed and the circulation speed of the blades, what is the impact on the drive, how we should optimize it.

The drive is a very integral part of the windmill. If it fails, the whole windmill basically cannot be functioned. Maintaining the digital drive or the drive is very critical for us. We install a lot of sensors on it, which measures temperature, rotation speed, RPM, sonic disturbances, and then we also look at the wear and tear of the parts. We install camera into the gearbox of the windmill. All this data is collected in the wind farm. They are stored and then they are post-processed for making sure that we upload it.

---

**Client** [00:19:23]
You mentioned after commissioning, you mentioned during commissioning and simulating the digital twin. The next stage would be to understand where you're currently hosting the simulation software. I understand is it in the cloud? Or is it on site or on-prem?

**Expert** [00:19:38]
Pretty much all of our solutions are cloud-based solutions. I've been with the company for five years, but I've not come across an on-premise software. Of course, our Analytics software is on-premise software, which is a custom-built software, but to most extent, we have Siemens digital twin, we have GE digital twin. They are all cloud hosted.

---

**Client** [00:20:00]
They are all cloud hosted in the vendor space.

**Expert** [00:20:02]
Typically, we procure the software. Let me tell you. Yes, in some cases, it can be the vendor cloud or it can be our cloud.

---

**Client** [00:20:10]
It's both the models.

**Expert** [00:20:11]
Yes.

---

**Client** [00:20:12]
You mentioned the simulation software that you integrate your digital twin software. Can you tell me more about that simulation software? Why did you choose to build the digital twin software?

Or were there limitations of any of the software that you were using where maybe the speed was not good or maybe the accuracy was not good, maybe the simulation models were not good? I want to talk more about the features of the simulation software that you've built and why you chose to build, maybe some technical challenges that you face to the existing ones in the market.

**Expert** [00:20:47]
So first of all, digital twin is a natural evolution of how we used to maintain wind farms. So a different way to put it is that with digital twin, my O&M costs significantly reduces. I'm able to get failure mode for that drive well by simulating various types of loads on the drive and the gearbox.

And then also the changes in ambient conditions, weather condition, cold, heat and also the wind speed, let's say, we have had a tornado nearby or something like that, what happens to the blade and how it impacts the gearbox and the drive inside. And then this information is then used to simulate the load in a three-dimensional model like using software, like GE Predix kind of analytical models, C3.ai.

---

**Client** [00:21:32]
No, I just want to understand where the drive manufacturer software is coming in and where you prefer and where your simulation model is coming in. So I just want to understand the link click, so you mentioned you simulated using GE Predix for an Analytics software, so where is this marriage happening? Is the export of data or the connection of data from here to one software to other software?

**Expert** [00:21:56]
So it's typically what happens is the sensors, which are inside the wind mill, sitting on top of the gearboxes, they send the data. They send the data to a software. The OEM has already installed. The data comes in like telemetry. It's a telemetry data, it comes in form of various numbers.

And that data is then ingested into digital twin simulation software, so which is what we're talking about GE Predix, C3.ai, Siemens, Alteryx, and Ansys. So the way the telemetry happens is there is something called head-end system.

The head-end system collects millisecond, microsecond, nanosecond data slices from the sensors. That is stored in the edge system, which head-end system. Let's say, I have a wind farm of 100-plus windmill just 100 windmills. So each windmill will have a small edge data logging system.

The data logging system then sends all the data to the edge data center in the wind farm. And from the edge data center where the head-end system sits, it is then uploaded into cloud. Once it is uploaded into cloud, we get the data into the simulation software.

Now albeit, my old wind farms, which are 15 years old or 20 years old, they are not very well cloud integrated. But nowadays, we are connecting all of our wind farms using fiber. So we have a very good idea and since its fiber, high data throughputs are possible, and we can get most current information about wind farm or a windmill using the fiber technology. Before it was a different situation where we had to rely significantly on the data to be uploaded from the wind farm to the cloud and then we would download it. There will be some lag.

---

**Client** [00:23:39]
Got it. Perfect. That was the exact idea because I was not able to visualize how the data is coming out and then where it's been. Now, it's pretty much helpful. Thank you so much. Now, you were talking about nanoseconds, milliseconds and microseconds. So is there a level of accuracy of the simulation model?

**Expert** [00:23:58]
The problem with the windmill is the maintenance overhead. It can fail very fast. And the cost of failure or the cost of downtime is very high. Because let's say, if a windmill fails, typically, these wind farms, they are called lights-out farm, meaning I don't have people, human being sitting in the wind farm because these are all in the remote places.

So typically, depending on the situation, it could take anywhere between one hour to five hours, six hours and even 10 hours to dispatch somebody, some technician to go to the site. So imagine a windmill being gone for 10 hours, that's a massive loss of revenue for us.

So the more granular data slice we are able to get, it's called time series data, the better we understand the behavior of the components. And where if we can understand the behavior of components well, we will be able to build good more detailed model, and we will be able to perform more microanalysis or microsimulation that will help us to predict the failure rate of the component.

And let's say, if I have to do a predictive maintenance or preventative maintenance, it gives me a better idea. Because simply put, the way it works is, let's say, I have a windmill, it is expected to produce, it is forecasted to expected to produce X megawatt hour of output, and that is what our power team sells it to the market or the regulators or the market makers.

If the windmill ended up in an unplanned maintenance, then according to the contract, the amount of power commitment lost has to be fulfilled by somebody else. And that time that somebody else would most likely trigger something called peaker plant, I don't want to get into that.

And so our unplanned downtime could be somebody else's revenue. So what we need to do in order to make sure that there is a power commitment that we gave and the grid is continued to be balanced by a third party who has the capacity, is we have to give curtailment. The curtailment is a fine imposed by the regulator on us.

And so the longer the duration of outage of our windmill, the higher is the curtailment fine because it is. With that said, it is very critical for us to preventatively maintain the part.

So when I do a planned maintenance of the parts, then I can inform the grid regulator saying that, “Hey, I'm going to bring my windmill down for plant maintenance for five hours or 10 hours,” so there is no curtailment, go figure out, talk to somebody else and make sure whatever the offset and the drop in power on the grid is offsetted by somebody else. Sorry, I dragged you into business process, but I just wanted to inform that it is important.

---

**Client** [00:26:42]
Got it. So just coming back to the simulation question, is there a level of accuracy that you require or you keep for the simulation software?

**Expert** [00:26:51]
We would prefer 100% accuracy, but we know 100% is impossible to get. So anywhere between 90% to 95% accuracy is good. We typically aim for 97% accuracy, which is basically two-sigma.

---

**Client** [00:27:05]
And the speed, in terms of simulation speed?

**Expert** [00:27:08]
That depends. So basically, the more the granular data, the higher, the longer the term duration of simulation. Simply because the granularity talks about the data resolution and higher the resolution of data, better the simulations.

---

**Client** [00:27:22]
But do you have a preference or is the longer the better you think?

**Expert** [00:27:26]
Well, so the way this works is that instant, first of all, there's nothing called instantaneous simulation. So once the data comes in, we have to feed it to the simulation software. It builds models. It takes time for it to build model. And then we vary the parameters of the model to understand the stress and strain on the model due to various scenarios.

---

**Client** [00:27:49]
Can you explain it with maybe a customer example of where you used simulation to identify or maybe mitigate risks in the drive integration process, maybe during maintenance also customization. Can you give me an example?

**Expert** [00:28:03]
So the typical drive integration, so you have a gearbox in the windmill, that has basically the gearbox is attached to the stem of the windmill and then that stem is basically attached to the turbine. So when the windmill rotates, the gearbox kicks in, that is the one which we use to basically or just the speed at which the windmill can operate remotely because we don't want to put too much of load on the windmill and impact the parts wear and tear. So we have to constantly monitor that.

So let's say, if I have a bad weather predicted, and I am expected to, let's say, I have 10 windmills each of one megawatt hour output. And let's say, I am predicted to produce 100 megawatt hour output over the 24-hour period. And let's say, we are forecasting a storm. And the storm could have high wind gusts, which creates problems of nonlinearity between the 10 windmills because the wind actually flows in different parts of the farm in different ways.

So we will have to simulate to understand that given a weather impact like a storm event, let's say, if the storm duration is for two hours. How we need to throttle the windmill blades, meaning we have to change the pitch and yaw we have to change the direction so that the blades are safe and the windmill is safe and they don't take too much of strain or doesn't put too much of strain on the rotors of the drive.

So all those aspects, we simulate using this data, the data that I initially set. Once we have that information, depending on how much impact the storm is going to have, we inform the grid controllers/regulators saying that, “Hey, I'm going to shut down my windmill or I'm going to slow down the production of power by dragging my blades,” so that I don't end up damaging my power generation turbine. So we predict those things using digital twin and then we inform the regulators. That's one use case. I guess a very common use case.

---

**Client** [00:30:03]
So you understood how much you must adjust the pitch and the yaw and all the meters. So what is the next stage? So how does the information go back to the trial? So you've simulated it and how does it get affected in real time at the windmill?

**Expert** [00:30:18]
So once we've simulated, then we basically look at something called parameter setting. The parameter setting is the commands we sent from our renewables control center, which is a centralized control center, where we monitor the health and power production output for all the plants that we have.

And then we figure out, okay, which windmills I need to specifically target and then we send Digital Commands. So Digital Command is then sent. It positions the blade, the pace, the yaw, the direction, the rotation and also we put something called wind breaks or it's called wind sharing of the blades, where we put the blades at 90 degrees to ensure that the wind doesn't impact the blade or the windmill. So wind just basically passes through.

---

**Client** [00:31:05]
So the commands are also directly aimed at the drives because without that, it is not possible?

**Expert** [00:31:11]
It's really not that drives. It is the controllers that are sitting on the drives are within the turbine. There are many controllers. There are actuators, there are controllers that are sitting, and we send those commands to those actuators and controllers.

---

**Client** [00:31:27]
And those will decide on the commands that should be given to the subsystems with the drives or whatever has to be done?

**Expert** [00:31:34]
It is done by our renewables control center. The renewable control center is like, to lack of better word, it's like your air traffic control tower, where they're sitting, they're monitoring and watching all the performance parameters and we have sensors that detect any anomalies or issues and then they quickly dispatch or they take action. The control center is the one that manages all this stuff.

---

**Client** [00:32:00]
Got it. So you mentioned about this is one example. Can you talk to me about maintenance example also?

**Expert** [00:32:06]
Another very common example in digital twin is training simulation. So when we bring technicians on board, when we bring in new technicians, when we want to training the technician to perform more complex tasks.

We actually use a subset of this real production data, and we build training models where when our technicians go through the learning process, they actually use the 3D simulations to learn to understand how the parts look, what kind of parameter settings they need to look at it and stuff like that, which is the most common digital twin example, mostly used in industrial context.

The other big common use case that we use is basically what is called the maintenance use case. The maintenance use case, before technician has just passed to attend to any O&M issues, they actually download the digital twin profile for that particular wind farm or windmill and then they take it with them.

So think of it this way. You are on the top of windmill, 250, 300 feet tall and the technician is in the turbine room on the windmill. And let's say, this is a third technician coming before him or her two other technicians would have performed some updates. So how will this technician know what was done before.

So they will go to the digital twin model. They pull up the versions of the digital twin to compare what they are seeing in real time in person like LivePerson and what was done previously. So that will give additional health and insight to a technician to perform better job to ensure that the O&M, the person is doing is properly taken into account.

In addition to that, we catalog each O&M, meaning, let's say, if you are a technician, I am a technician, you would have performed some work on that six months ago, you would have cataloged all the changes that was done or fine-tuning that was done in your O&M maintenance model. And then when I go next, I will have access to that maintenance model that will help me to understand what you did.

So that's one way to ensure that there is no dependency on the text and that knowledge of change, everything is documented accurately. And in many cases, those are required even for our regulators, especially if I'm having wind farms in regulated market.

We have to capture all this information for potentially letting the regulator know why or in the event of a situation, let's say, unplanned downtime, we will have to substantiate as to what cost it and then the government might ask shows the evidence that you do maintenance planning for your windmills. So this information comes also in hand.

---

**Client** [00:34:48]
So is there any support from the drive manufacturers, for instance, in any maintenance regarding the drives?

**Expert** [00:34:55]
If the drive is new and within the warranty and if let's say, there is a major failure that we cannot fix it or fixing it could potentially wide the warranty, we send the data to the manufacturer or OEM, they look at the data and then they decide whether they want to dispatch a tech for warranty coverage or not.

So it is also used in warranty by the OEM. So we have to collect the data. We keep the data and before the OEM actually dispatches their own tech, they ensure that they're taking into consideration all the aspects.

---

**Client** [00:35:28]
So that would be a second approach. Like first, you will see whether the maintenance can be done by yourself and only then if it cannot be fixed or if it requires replacement or something else, then it would go to the drive OEM and manufacturer.

So coming back to examples, I'm specifically looking if you have any examples with related to drive where you had to conduct predictive maintenance or you had to do prescriptive maintenance kind of examples, especially?

**Expert** [00:35:57]
So I already gave you the predictive maintenance example. I told you how we use that for predictive maintenance where we collect the real-time data. And then we basically analyze it and say if a particular part meets conditional maintenance, we then dispatch the tech or the issue planned downtime situation. That was the case of preventative maintenance, where we analyze the data and we decide that, yes, the wear and tear here is higher or lower, and we need to make sure we take the thing.

In the case of predictive maintenance, it's mostly done for simulation process, meaning, we tend to predict for a given part condition, what is the expected failure rate? The predictive maintenance will then drive the decision for preventative action.

Because you're predicting that a part is going to fail and then you are going to preemptively take precautionary action by declaring a planned downtime or you would declare a more sourced downtime, meaning if the parts required or complexed and sometimes the parts would also be made to order. Then, in that case, you would have sufficient time to order those things from the OEMs.

---

**Client** [00:37:07]
Other question is, what kind of support from the drive manufacturers would be useful for better in customization requests?

**Expert** [00:37:15]
I think what happens is, see, the industrial trials are very expensive components of the overall system. And warranty and proper dispatch or a timely dispatch, let's say, the technicians, especially during warranty period can be improved.

Typically, OEM tend to avoid warranty dispatches as much as possible because remover warranty is a cost for them. So they try to keep their costs go. So that's part of the problem, which is a common problem in the industry, especially when it comes for complexed parts, which we have seen quite a bit of challenge.

The second piece that is important to understand is the cost. The warranty clauses are typically complexed. If one doesn't understand, what is the implication of cost and which component covered, which compound is not covered? How much has to be self replaceable? How much has to be OEM intervention?

The cost of O&M can be very unpredictable. Unpredictable O&M cost is the biggest enemy of any utility, okay, or any power generating company. They want to be able to predict O&M cost. And for that, they have to make sure that they have full transparency from the OEM on any particular item. So typically, it is challenged from the OEMs. They don't disclose all the complexities upfront, the culture is more so a fact of, “Okay, I'm going to do it this way.” I'm not going to sell everything.

---

**Client** [00:38:39]
One question that I forgot. We did a survey to understand what kind of software are being used in simulation. So basically, we had four types of software like CAD, MATLAB software and Python based tools and Power System Analysis and planning software. One interesting thing that came about is that we expected CAD and MATLAB to be at the top being used by everybody, and that was the case. One interesting thing that came out was Python based tools. Do you have experience using these tools?

**Expert** [00:39:09]
So CAD and MATLAB is the most commonly used simulation software because it's extremely cheap. And most importantly, that is what is covered in colleges. So in the engineering colleges, many of these young engineers who are deployed on all this data simulation analysis work, they know that very, very commonly. And that's one of the reasons why you will find.

And in a production scenario, of course, there are many companies who use that in production scenario, like for us, we don't use those things in production scenario. We always use that in prototyping and labs.

Now Python. Python is a very different animal. Now Python, we extensively used to perform parametric analysis, which is not offered out of the box or where there is a custom analysis or simulation that needs to be done. This can range from data heat mapping to data simulation with predictive inputs, there could be a custom output that you want to produce about this data that you have and all the stuff. So Python is also extensively used for customized point simulation solution development.

---

**Client** [00:40:16]
I understand because it's a kind of tailoring a simulation tool for your particular use case. I get that. Can you give me an example? Like have you used it maybe, I don't know, if it fits a drive, but if you have used it for simulation?

**Expert** [00:40:30]
Yes, I will give you a simple example. One of the very common use cases of Python is basically data anomaly detection algorithms. So early on in our call, I said we received millions of million granular data. Even sensors can make errors.

So typically, when we do simulation, a small error can amplify and it can actually create wrong outputs. One of the things that we use Python is we have built customer algorithms using Python that helps us to remove data anomalies.

So that is one example where we kind of run through slices of data through a custom algorithm builders using Python that helps us remove or detect data patterns, anomaly patents. The second example is heat maps, data heat maps. For example, when a simulation software provides an output, let's say, we need another view of the same output in form of more to put it on a PowerPoint or put it in our document using a report or something like that.

We use Python to again create visual outputs very commonly. What I was trying to tell earlier is just like the way you would use Excel spreadsheet to perform all your Analytics from the surveys and the discussions you're having with many of the experts, Python is a friend of an engineer doing the same thing. So Python is a very handy tool. There is no limit to how you can use that tool for data analyst. During in our labs, during the testing, we use Python to build small simulation engines with limited data sets.

---

**Client** [00:42:00]
Perfect. Thank you for your time. This was very helpful.
