---
theme: "Other"
title: "Lead Network Engineer at Verizon Communications Inc Sees Automation and AI Transforming Network Management with NetBox Labs and Infoblox"
doc_id: EC-1000000-234828
source_line: "Netbox Labs · Expert Call · Customer · 21 Oct 26"
date: 2026-10-21
company: "Netbox Labs"
pages: 2 of 2
saved: 2026-10-21T15:35:32.952Z
url: https://research.alpha-sense.com/search?search_id=tmp-ffzr3ttvkmfy1lpfztggun&sort=DATE&order=DESC&docid=EC-1000000-234828
---
# Lead Network Engineer at Verizon Communications Inc Sees Automation and AI Transforming Network Management with NetBox Labs and Infoblox

Company Deep-Dive

DATE PUBLISHED

21 Oct 2026

INTERVIEW DATE

23 Jul 2026

EXPERT PERSPECTIVE

Customer

ANALYST PERSPECTIVE

Investor-Led (Buy-Side)

PRIMARY COMPANY

Netbox Labs

SMART SUMMARY

Summary

The conversation covered the expert's approach to network management, focusing on the use of NetBox Labs and Infoblox for different aspects of network operations, automation, and change management. The discussion also included vendor evaluation criteria, integration strategies, and the growing role of automation and AI in network engineering.

EXPERT BACKGROUND

- Senior engineering lead focused on network and infrastructure architecture for a large global enterprise, responsible for designing, deploying, and scaling core routing platforms, edge nodes, 5G transport networks, and multi-cloud connectivity.

EXPERT SENTIMENT

- Strong preference for multi-vendor, API-first, and automation-driven network management solutions, emphasizing separation of operational and intended state systems.
- Confident in current network management approach but open to evaluating new solutions if they provide clear value, advanced features, or improved integration capabilities.
- Positive outlook on the evolution of network automation and AI-driven agentic workflows, seeing significant future potential.

TAKEAWAYS

- NetBox Labs is used as the network source of truth, supporting automation, zero-touch provisioning, device onboarding, and integration with ServiceNow for change management.
- Infoblox is retained for runtime DDI (DNS, DHCP, IPAM sync) and threat defense, while NetBox is preferred for its programmatic APIs, DCIM, and automation capabilities.
- The organization follows an industry-standard multi-vendor approach, avoiding vendor lock-in and leveraging best-of-breed solutions for different network functions.
- NetBox's automation and integration capabilities have significantly reduced manual work and accelerated deployment times, especially for IP address allocation and device onboarding.
- Competitors evaluated included Device42, BlueCat Networks, SolarWinds IPAM, and Nautobot, but NetBox was chosen for its scalability, API-first design, and lower operational noise.

AlphaSense Smart Summaries are AI Generated

Introduction and Background

NetBox and Infoblox Comparison

Industry Standards and Practices

NetBox Features and Evaluations

Competitor Analysis and Market Trends

EXPERT BIO

Lead Network Engineer / Engineer 3 at Verizon Communications Inc., customer of Netbox Labs. Expert can speak to their experience in evaluating and deploying network infrastructure solutions, which aligns with the project's focus on understanding customer evaluations of NetBox Labs.

Engineer 3 - Specialist in Networking Repair Bureau at Verizon. Reporting to the AVP of the Global Network Team, the expert is responsible for doing work with the network infrastructure team, including working on improving networks and providing solutions for optimal network performance, which includes automations, vendor selections and evaluations, escalations, setting up strategies, and infrastructure architecture.

Prior to Verizon, the expert was a Technology Analyst at Infosys, leaving April of 2025. Reporting to the AD of Technology, the expert was responsible for the global deployment and migration of SD-WAN across 60+ locations, significantly reducing circuit costs and boosting application performance, as well as the end-to-end management of headend infrastructure, proactive network monitoring, and the development of comprehensive SOPs to ensure high availability and industry compliance.

The expert can speak to the strategic deployment of global SD-WAN and 5G Core architectures, specifically to the optimization of network performance and cost reduction, scaling technical operations through AIOps, and managing zero-downtime migrations in regulated environments.

View More

INTERVIEW TRANSCRIPT

**Client** [00:00:00]
Great to meet you. Just a quick bit of background. We're looking at the networking space more broadly and trying to understand it a bit more. It would be great to hear a little bit about your role there at Verizon and what tools you're using today to help manage the network.

**Expert** [00:00:17]
To give a quick introduction, I work as senior engineering lead, and my major focus is on network and infrastructure architecture at Verizon. My team is directly responsible for designing, deploying, and scaling our core routing platform, distributing edge nodes, 5G transport networks, multi-cloud connectivity, etc., for a global enterprise footprint.

I majorly work on these distinct pillars like core DDI and also real-time operational DNS, DHCP services, and also network source of truth, for which we are using NetBox Labs, and for DDI, we are using Infoblox, along with various other solutions we have evaluated. Our global infrastructure is vast scope where we keep on refining the infrastructure and keep on evaluating and using various vendors.

---

**Client** [00:01:14]
Got it. The main question I have is, using Infoblox for core DDI makes sense, so what value does NetBox add to your existing DDI? Because DDI is going to handle I forget the acronym. DNS, DHCP.

**Expert** [00:01:31]
DNS and DHCP.

---

**Client** [00:01:34]
Which is actually doing the work? A new node comes online, it will issue the IP address, DNS, and the likes. What is the value that NetBox is bringing to sit next to the DDI platform?

**Expert** [00:01:46]
To answer that, our architecture cleanly decouples these two things, like runtime operational network, which is executing right now or at the real-time, and also one is intended state modeling, which is to be configured or planned configurations. Infoblox definitely serves as runtime DDI engine where we use it for our DDI and threat defense for DNS security filtering and other aspects, whereas, coming to NetBox Labs, it is our network source of truth, which is being used for intended state like programmatic GraphQL, REST APIs, and also we use it for ZTP pipelines and also device racking and device tracking as well.

We use various modules from NetBox, like NetBox Enterprise Cloud, IPAM, VRF engines, DCIM modules, and configure context. We use that to simply say it is our network source of truth, where we use it for our zero-touch provisioning. Also, we use it to validate our templates, design templates, and automatically use this during our provisioning and activation of the devices and other aspects.

---

**Client** [00:02:54]
The DCIM functionality makes a ton of sense to me. I am assuming Infoblox doesn't have robust DCIM today?

**Expert** [00:03:02]
Yes. We majorly rely on Infoblox for our DDI as well as our threat defense. NetBox Labs, we majorly use for its IPAM and VRF engine and cloud and DCIM modules throughout.

---

**Client** [00:03:17]
you are using NetBox's IPAM, not Infoblox's IPAM?

**Expert** [00:03:22]
We are using Infoblox IPAM sync engine for our dynamic ARP and DHCP lease sync. We use IPAM and VRF engines from NetBox for hierarchical prefixes and aggregates. We use it as a source of truth where we use it for our automation and provisioning aspects, to validate the templates, and automatically reserve IPs from Infoblox via APIs.

---

**Client** [00:03:50]
Okay. What makes NetBox more of a trusted source of truth than Infoblox?

**Expert** [00:03:55]
Definitely NetBox has this advantage of having these DCIM modules, also it has various programmatic GraphQL or REST API functionality, which enables us to integrate into our workflows. For example, we have integrations for our zero-touch provisioning, where if we get a new hardware, we run this ZTP, which allows this to query NetBox via GraphQL, and it gets all the assigned subnets, loopback IPs, VLAN mappings, and all other configuration-related aspects from NetBox in a single automation script, which prevents much of dependency on manual configuration and also raises more errors which can be prone during manual configuration and also saves time as well.

Also, we have another aspect of integration where we have this ServiceNow automation integrated with NetBox Labs, where every network change, it queries NetBox Labs to validate the designs, like if there are any automatically reserved IPs, or if there is any configuration or templates created in NetBox, or if there are any additional information, it queries our NetBox Labs and runs the Ansible playbooks, so that everything is automated, which is our major use case when it comes to NetBox.

---

**Client** [00:05:07]
If you were to build that on top of, let's say, Infoblox, I'm assuming they don't have the modern tooling like the GraphQL endpoint. Could you build it on Infoblox, or is it just an impossibility?

**Expert** [00:05:19]
I don't think we can do that with Infoblox because it is right now dedicated for DNS, DHCP engine, and handling. Integrating this and migrating everything into a single vendor or solution is also not feasible at our organization level. We definitely keep that, as I said, runtime operational, and also whatever intended or planned modeling as a separate aspect. We definitely keep these two separated instead of integrating everything into a single solution and making it complex.

---

**Client** [00:05:54]
Would you say is that mentality Verizon specific? Is that industry wide? Is that how most networking groups would think about this?

**Expert** [00:06:04]
No, I think it's an industry-wide standard where we always look for multi-vendor solutions, where we are not dependent on a single vendor or we don't put everything into a single vendor and have it run in a complex mechanism. Definitely, they can do things, but as NetBox Labs is primarily tasked with this IPAM, automation, and DCIM module, definitely they have more advantage in terms of APIs and programmatic queries and integrations.

Definitely, we don't want to lose that, and I see that as industry trend, because most of us want to keep our configuration clean and wanted to have this automation run without any issues. Definitely, that's a standard we follow, and I even saw the same standard across the industry as well.

---

**Client** [00:06:51]
If tomorrow NetBox launched a product around DNS, DHCP that was perfect and completed with Infoblox, that's not something you would adopt because you would want them separate?

**Expert** [00:07:03]
It depends. If we see value in it and if we see it providing something out of the box and something relevant which is missing from the current solution, or if that is providing more advanced features or easier integration capabilities, then definitely that is something we can test. We will be testing and we will be running our POCs, and testing it in our lab environment.

We are not away from those ideas, but as long as we test it and evaluate it, then once we get the confidence, then only we will be able to proceed further with respect to this kind of integrations. We are open to it, and we'll be having our own testing mechanisms and our own evaluation criteria. If everything aligns and if we see the confidence and if we are confident enough, then we'd be definitely willing to that aspect as well.

---

**Client** [00:07:53]
I see. I think NetBox Labs has a handful of features aside from the core platform of discoverability and whatnot. It seems like they have an assurance product, where you can say the intended state and see what has drifted. There's probably some other functionality.

I'm curious to see. Where is the highest value in the platform today? I assume it's the core discoverability and reconciling against your heterogeneous hardware, but what are the different parts of the platform you value the most today? The different products or features within NetBox Labs platform today that you leverage the most?

**Expert** [00:08:33]
We majorly use their features for a few of our categories, definitely one is managing it as our network source of truth, using it for querying during our automations and whatever the configuration changes or whatever the configuration items we have and the changes we have, definitely everything has to come and go from NetBox and validate with the data, as it is our source of truth.

We even use that for subnet and IP allocation, where we have flash around lot of time. Earlier, it used to take around days of time, like three to four days to validate the IP subnets and validate its allocation and validate if that is previously allocated or not. Right now, because of this integration and automation, it has came down to minutes. We have accelerated our deployments, because of this speed in IP address allocation and provisioning and device onboardings as well.

In terms of various other features, we are currently using NetBox Enterprise Cloud, and we are using DCIM module to monitor and to validate our device data, rack, cable, and interface mappings as well. We not only map IP addresses and other aspects, we have these virtual interfaces, physical interfaces, and each device and their port level data, like routers and switches, their port interface configurations.

Everything is directly mapped and is present in the NetBox. We use these automations to query this NetBox, and get the information before any changing happens. It's our change management or change processing aspect as well. We definitely look forward for major integrations and other integrations, like having these recent AI and autonomous AI integrations. If we can have these kind of integrations where we, instead of going through the entire data, we can have direct integrations with the language GraphQL, so that we can query in a normal language.

Like, if we want to know the subnet details, I can say, "Find all the subnets which are with this branch and which are having 100-gig uplink capacity," etc. These kind of integrations, and also we majorly use cloud-related orchestrations, and we work with multi-cloud environment.

Major multi-cloud integrations as well, like with Azure, AWS, GCP, all major cloud integrations also can be more fine-tuned with respect to how NetBox gets queried and how it interacts with the cloud environments as well when spinning up the cloud instances and other aspects over that.

---

**Client** [00:11:13]
You're planning a larger change in the network. You're going to use NetBox to see the current state. You're going to model the intended state. Once everything looks good in NetBox, what does the process look like to enact that change in the network from NetBox?

**Expert** [00:11:31]
NetBox holds all our data. What we do before any change happens, we query the data into the NetBox, and we use those workflows in the NetBox. We allocate configurations or templates. We allocate subnets and other information in the NetBox itself. For example, if there is a device getting onboarded, before the provisioning itself, before the onboarding of the device itself, we configure the details, like the port details, what the interface configuration should look like, and what the links that are connected to the interfaces.

All this data is configured directly into the NetBox, and once the device gets this zero-touch provisioning script ran, it directly communicates with our NetBox and gets all the configuration and then proceeds with the onboarding so that we save a lot of manual configuration with respect to the device onboarding. We can use the templates, automate these templates creation, and all this stuff.

Based on this, we definitely reduced our onboarding times, and we even increased our efficiency in terms of production and our device onboardings as well. This is actually how general device onboarding happens. We have various specifics when it comes to cloud instances and other aspects. In general cases, this is how we leverage NetBox's querying capacity and its programmatic approach with respect to our workflows.

---

**Client** [00:13:01]
How deep of the configuration for a given device will NetBox hold versus another system? I'm assuming they're probably heterogeneous switches. They're going to have a variety of different settings. Does all of the config for a given switch you plug in live in NetBox, or how does that work?

**Expert** [00:13:22]
It depends on the device, and it changes from device to device. For switches, NetBox holds all the configuration related to its interfaces and its connectivity modules, like what are the links connected to that interface, which interface is being connected to which link, and the other end of that particular interface. For example, if we have a switch at a particular geographical location and it is connected to some other router or if there are any virtual interfaces as well.

All these physical virtual interface device related and cabling and interface mapping. All these are definitely onto the NetBox, and all this configuration would be pulled from the NetBox to the device during its onboarding. Post that, various configuration would be through some other scripting and some other tools.

Definitely, we have various aspects like these onboarding and whenever there is change needed, for example, if we are going for a change or addition of another interface or usage of another interface onto the switch, then that configuration should come from NetBox instead of going into directly to the switch and making these configurations. We wanted to keep our source of truth up to date and accurate.

---

**Client** [00:14:37]
Everything syncs to NetBox. Any change that happens in NetBox is what I'm hearing.

**Expert** [00:14:44]
Yes.

---

**Client** [00:14:45]
How do you think about this, what NetBox is doing versus something like a Forward Networks or IP Fabric or something like that's, I think, more actively scans and pushes out into the network?

**Expert** [00:14:58]
You are talking about the configuration push from NetBox to the network?

---

**Client** [00:15:02]
Yes.

**Expert** [00:15:03]
Everything is in sync, and right now, we have had multiple use cases, and we have had multiple onboardings and provisionings. We don't see much issues with respect to this configuration sync and programmatic and automation provisioning. Occasionally, there are here and there misconfigurations or stale data entries which needs to be manually reviewed. Apart from that, I see we are getting whatever we are putting the value for.

---

**Client** [00:15:32]
Okay. Have you considered using? I think there's a few companies that will do more network assurance or digital twin of a network. The two I've noticed is IP Fabric or Forward Networks. Have you considered that type of functionality at all?

**Expert** [00:15:49]
No, because as a global infrastructure, we have a dependency on various vendors. We currently run with a multi-vendor approach, we have hardwares running with respect to Cisco, we have hardwares from Ericsson, Nokia, and other various vendors. As of now, we see NetBox is capable of having data ingested or data synced from all our infrastructure elements and devices.

We don't want to step into some other solution and become vendor locked in, we have to use another solution for some other vendor. Initially, we used to have various vendor-dependent solutions, but right now, since everything is moved into NetBox, and we are able to handle that efficiently. We are currently not looking into other solutions where we keep on integrating or we keep on changing configurations. Right now, we are confident with the solution, and we keep on pushing forward with this.

Earlier we used to have SolarWinds IPAM, which is legacy IP address management. It was using periodic SNMP and ICMP network sweeps to monitor and to get the information or sync the data from the network devices. We have sunsetted it because it's a lot of legacy, and it didn't have much with respect to this programmatic and automation approach, and it is lacking this API first infrastructure as code workflows.

We have put it down, and we have migrated to this newer API first approach solution. Right now we are in a stable position, and maybe if things arise and if needs arise, we'd be looking forward to what NetBox is going to offer and then evaluate that with the current market and other solutions or vendors, what they are offering.

---

**Client** [00:17:40]
Helpful. How do you do, for lack of a better term, assurance today, that what is in NetBox Labs is actually what is configured in the real world?

**Expert** [00:17:49]
We have this organization-wide workflows integrated so that there won't be any other option other than going through the NetBox for all the configuration related changes and other aspects. We definitely have these audits and review process in place where we have these automations that fetch the data from NetBox and analyzes the data with real-time data pulled from the devices as well, so that we keep in sync with the data in the NetBox, and we make sure that it is the source of truth for us.

All the workflows are automatically in place for us. There is no other possibility where the data can go or if that data misses from the NetBox. Everything is automated into the workflows. We have the ServiceNow integration with the NetBox, so if there is any change request initiated, it has to check in the NetBox and update it and get it from the NetBox so that data is in sync instead of having the stale data or incorrect data. Even after that, we have these regular processes and audits and reviews happening with our team. We regularly review for the accuracy of the data.

---

**Client** [00:18:58]
I'm hearing you'll lock out any manual change from a given node. The only config change that can happen is NetBox Labs. On a periodic basis, it's automated but somewhat manual to confirm that the config on a given node matches what's in NetBoxes. Is that right?

**Expert** [00:19:16]
Definitely. It's a hybrid approach that we are following right now.

---

**Client** [00:19:21]
Okay. If we break apart all of the functionality, core DDI, I think there's a few players there. Who else is really competitive against NetBox's functionality today? Who else did you consider? Who else are you watching as they continue to evolve?

**Expert** [00:19:40]
During our evaluation process, we have evaluated other vendors as well. We initially used these open source, Nautobot to NetBox Labs, where we have run it internally, and we have self-hosted this, and it was taking a lot of time for us. We have evaluated these solutions. We have evaluated other competitors, to say Device42, where we have evaluated for its auto discovery and DCIM and application dependency mapping systems as well.

We have disqualified it based on, it is generating too much noise across our WAN infrastructure whenever it's polling or whenever it's getting that data from other devices. During our evaluation phases, we have ran testing with various other competitors, but we haven't seen a fixed or we haven't seen proper working. We definitely had the same working with NetBox as its dedicated solution provider for these areas. We finalized with NetBox during that phase.

Right now, if you ask, at the industry level, for this kind of solution, I see there are various small players also. We see NetBox is also integrating more and more features and also, with the advent of this AI and other automation in place, I definitely see that could be a tough competition in the market. Based on the features and how fast the solution or the provider is scaling up the solution, it definitely seems NetBox is holding its ground currently.

---

**Client** [00:21:09]
Got it. Maybe we can start with the DCIM first, and then we can talk a little bit about Nautobot. Device42, you said, I heard they were generating too much intelligence. Was that they were just pounding the network constantly? Was it the amount of traffic that they have to generate to service the product was too high, or they were collecting too deep of information on a given node that you did not want to collect?

**Expert** [00:21:36]
No. It's like what I said initially, we are seeing a lot of traffic or noise, like polling noise from this Device42 agents or Device42 integration. We don't want to have our WAN infrastructure being jammed up with these kind of noise. Definitely that was something we faced during our evaluation with respect to Device42, whereas with respect to NetBox, it gets queried and it gets its data sync whenever there is a trigger happens.

If there is a change request initiated or if there is a query or if there is an API call to the NetBox from a change or from a device, then it gets the data or it pushes the data to the device, rather than polling it continuously to check the status or to check the availability. Though that can be configured based on the requirements using various features.

---

**Client** [00:22:26]
I see. Besides Device42, who else would you consider viable today for DCIM? There's a lot of legacy players in DCIM, but curious in your mind, who are the top three or five that you would consider outside of Device42?

**Expert** [00:22:43]
I don't think I can name three to five vendors because, during our evaluation, we initially dismissed lot of players based on their offerings, where we just ended up with one or two valid players like BlueCat Networks. That is something we evaluated with respect to DDI and IPAM tracking as well. They were offering these solutions, but the total cost of ownership was too much for us with respect to the financial aspect. That reason, we haven't finalized with that vendor and went with NetBox.

Right now, Device42 is something that I have personally evaluated, and BlueCat Networks, that is also something I have evaluated, and I'm also familiar with this SolarWinds IPAM, which is a legacy vendor or a solution, and this Nautobot, which is open-source platform. I have some experience with that in running that and using that as an open-source in our network.

---

**Client** [00:23:39]
Understood. Let's go to the Nautobot evaluation. Nautobot is a fork of NetBox. Is that right?

**Expert** [00:23:48]
Yes.

---

**Client** [00:23:49]
How do you think about those two products today and going forward?

**Expert** [00:23:54]
We ran that open source NetBox, and also we evaluated Nautobot during our initial setup around three years ago. We have self-hosted and managed our PostgreSQL and caches as well. We have used it for basic IP tracking and Python script apart from other aspects, not with respect to much integration workflows and other aspects.

We have used it internally for basic IP tracking and just custom scripts whenever we are running some provisioning or device onboarding. It was too much of a time or consuming aspect for us. Also when we deal with cloud infrastructure, that is not something we would be able to scale or use confidently when it comes to cloud integrations.

---

**Client** [00:24:38]
That makes sense. You evaluated purely the open source. I'm not sure if they have commercialized anything since.

**Expert** [00:24:46]
It was purely open source when we ran it around three years ago.

---

**Client** [00:24:50]
Okay. In that functionality, the network source of truth functionality, anyone besides NetBox or Nautobot that you would consider today or if you had to reevaluate in the next couple of years, any other players in this network source of truth space you would add?

**Expert** [00:25:06]
In network source of truth, I see various other vendors are also coming up with their CMDB kind of solutions. Like for example, ServiceNow has its own CMDB, and there are these legacy CMDBs as well. It depends on what the requirement that we have. If that aligns or if that requires for reevaluation, then in that case, we have a dedicated setup process where we do the market research at that particular instance and see what are the solutions or vendors that are currently out there providing what competitive solutions.

Based on that, we finalize the list for our POC and proceed forward. Right now, I don't think I noticed any other solution in par with NetBox with respect to this IPAM and DCIM capabilities on how it is API first aspect as well. Maybe in coming future, other solutions like, as I said, ServiceNow, CMDB, and other aspects would be coming up with their own IPAM solutions.

---

**Client** [00:26:09]
This is helpful. It sounds like NetBox Lab is a next generation CMDB in your mind. Does it cover all of the use cases of CMDB, or does it completely replace a legacy CMDB in your mind, but it also has modern tooling around API access, and then, of course, the DCI modules and everything else?

**Expert** [00:26:30]
Definitely, when it comes to IPAM and these API-first automation scope, definitely this is a game changer or this is other stuff which NetBox is providing. In terms of CMDB and change management systems, we still have ServiceNow ticketing system in our organization. What we did is we have integrated this NetBox Labs with that ticket querying.

Whenever we have any change created or whenever we have a ticket created, it gets queried with NetBox to validate that design then. In such a format, there is interdependency or interlocking between these two solutions. I definitely see the scope for NetBox to expand to CMDB and other aspects. Considering whatever the players right now that are offering these solutions, it should definitely have its own spin on that, and it should have its own integration.

---

**Client** [00:27:23]
That's helpful. Probably NetBox today doesn't have 100% of the functionality of a legacy CMDB player, but it's more modern and easier to tool around. It's much more useful, is what I'm hearing.

**Expert** [00:27:38]
Yes.

---

**Client** [00:27:40]
On IPAM specifically, help me understand the decision to use NetBox's IPAM over Infoblox's IPAM.

**Expert** [00:27:47]
Definitely. Infoblox, we dedicatedly use it for our runtime operational network, where we use it for our DNS, DHCP leases across our 45,000+ endpoints for dynamic host IP lease and automated DNS threat filtering. When it comes to this source of truth and IPAM requirement, we wanted more automation scope in that.

That is a major reason why we kept it separate from these DDI platform and threat intelligence platform, with respect to how IPAM is aggregated, because we wanted to have automation capability and programmatic approach so that we can automate our workflows and we can have our zero-touch provisionings and integrations with other aspects. That is a major key change where we have looked in terms of why we have separated these two aspects.

---

**Client** [00:28:39]
Infoblox's IPAM will basically just read NetBox's IPAM, is how it's set up today, I assume.

**Expert** [00:28:47]
Yes.

---

**Client** [00:28:49]
By moving it to NetBox Labs, you're able to query it in a more modern way and automate around it instead of having it stuck in Infoblox. That's the main driver for moving that functionality up to NetBox?

**Expert** [00:29:02]
Definitely. We wanted to have more in terms of automation and programmatic approach.

---

**Client** [00:29:08]
If you left IPAM in Infoblox today, they don't have the API-driven access to enable that functionality today, is what it sounds like.

**Expert** [00:29:17]
Yes, because that is completely regional. Infoblox has all these regional boxes, so it's all regional instead of scaling and automation for that.

---

**Client** [00:29:27]
I see. This is very helpful. When you think about how mission critical NetBox is today. If NetBox had a 48-hour outage. You couldn't deploy new hardware, but the network would still run, is what it sounds like.

**Expert** [00:29:45]
Yes. There could be some entries that could be missing, there would be some mismatches with respect to how IPs are configured or during that time, and we'd lose visibility on our infrastructure or the device level aspects, like we not have visibility on what the interface is for and what the device is for, those kind of stuff. Also, definitely, it would hinder any changes, which if there is any issue or if there is an outage or anything. In that case, the change management would have some effect due to this, which needs a dependency on NetBox for source of truth.

---

**Client** [00:30:19]
Got it. From a pricing perspective, I am curious how much you pay Infoblox versus NetBox Labs. Is that one to one? Is it three to one? You pay 3X as much for Infoblox as you do for NetBox? How do you think about the relative pricing here?

**Expert** [00:30:38]
I would say maybe around 2%-3%, or 2X more, than what we pay for NetBox, to Infoblox. Right now, our budget for entire IT software spend sits somewhere around low eight digits per year, with budget to combine DDI and network source of truth would be around 20% of that. Could be somewhere around low seven digits. In that, we spend around, I'd say, 40% or 30% on NetBox, and rest on Infoblox and other threat intelligence and other solutions.

---

**Client** [00:31:10]
That's helpful. What would it take for you to double your spend with NetBox, where you're paying same as Infoblox today? Is there functionality that they could deliver where you would very readily switch over or I'm curious how you think about that relationship with NetBox.

**Expert** [00:31:26]
Definitely, right now, if they expand their scope towards this DDI platform, as well as if our usage increases with respect to our global footprint, if that increases, we'll get more devices, which in turn have more data to sync to NetBox, and our usage increases. In that aspect also, the spend increases for NetBox. For it to drastically increase, we would definitely be picking up any new features or integrations provided by NetBox.

As I said, if there are any integrations in terms of AI and language model integrations or analytical dashboard processes and major cloud integrations and refinements. These aspects would definitely drive more into the NetBox spends. If NetBox ventures into different solutions and offers something that is relevant to us and that can save our time and cost and increase our efficiency, then definitely we would be testing it out. If everything works well, we'd be migrating from legacy to NetBox as well.

---

**Client** [00:32:31]
Great. Taking a big step back. I think everything we've talked about makes a lot of sense for something Verizon's scale. Spending that much money on network management Obviously, very complex network across a variety of points of presence, hosting providers, internal, external.

What level or what complexity of the network does it start to make sense to use NetBox Labs? I'm assuming if I'm all cloud and in one cloud, it doesn't make any sense. If I'm hybrid and low complexity, does it make sense? How do you think about when this becomes very interesting for an enterprise to deploy NetBox?

**Expert** [00:33:11]
If you are asking about recommendation or when to best use NetBox, I definitely say NetBox, right now, based on our usage, even though if that is a cloud instance or even though if that is a hybrid, definitely there is scope for NetBox integrations because we have these virtual interfaces, virtual pods, or we have these virtual instances as well, which needs to be tracked and maintained. Definitely there is a scope for inventory and IP address management whenever there is a network element or instance or a device is in place.

Major scope would more be on legacy or on-prem and hybrid, because if we go for cloud instances, each cloud provider have their own system for managing their instances and other aspects. Definitely the major scope would be with hybrid and on-premises or data center approach.

---

**Client** [00:34:02]
I see. I assume if you're in one location, it's probably less useful than several locations or multiple clouds.

**Expert** [00:34:11]
Definitely. If there is more span with respect to geographies, then definitely there would be more dependency on data centers and other interconnects. That would definitely increase the network architecture and infrastructure, which in turn drives these solutions and the use cases.

The more complex the network is, the more visibility we need and the more accuracy we need. If that network is a complex network and if it is having lot of interconnectivities with cloud, on-prem, and other aspects, then definitely that's the area to have more accuracy and visibility. In that case, also NetBox would be crucial to have entire network visibility.

---

**Client** [00:34:56]
At what point does just using BlueCat or Infoblox, the DDI players, not become enough? At what point would you say it becomes a necessity to use NetBox instead of just what's internal to Infoblox?

**Expert** [00:35:09]
Definitely, if you want to reduce manpower or if you have a lot of changes coming in, if the network is growing rapidly, if an organization, if an enterprise is expanding its wings to multiple regions, multiple locations, having various solution integrations, for example, if they are implementing or migrating from their legacy WAN infrastructure or MPLS infrastructure to SD-WAN or another software-defined architecture, in that case, there would be lot of changes in terms of network and device and the solutions and vendors.

In those aspects, definitely, this automation would definitely save a lot of time and lot of engineering power. Those aspects would be very crucial for these automations and scripting and workflow integration.

At that aspect, it would be definitely useful for an enterprise or organization to scale up their approach instead of having just a regular IP address management system which just works as a core database dump. Rather than that, they can expand and have these API first architecture or solutions where they can have it as a source of truth and use it for automated zero-touch provisioning and as a source of truth for querying and getting the information and getting their network visibility.

---

**Client** [00:36:23]
Got it. Just a couple little bit more random questions. If you were on the board at NetBox, what changes would you make day one?

**Expert** [00:36:32]
I'd definitely add more in terms of cloud integrations. I'd have these dedicated options or features for major cloud providers, be it AWS, Azure, GCP. With respect to their cloud instances and their cloud elements and infrastructure, I'd add more workflows or integrations with that. The other aspect would be, as I said, I'd definitely look forward to integrating more and more of these AI and agentic solutions where workflows or agents can be deployed for this provisioning and these language models can be integrated with NetBox for easier analytical approach and easier data visibility.

Instead of going through the entire database or entire set of data, we can have these querying aspects with respect to natural language models. These easier integrations, because as the entire world evolves to a point where the traditional approaches like querying large set of data or databases, other aspects are fine-tuned into language models or casual approaches, definitely that is something, the route that I would make the NetBox to follow.

---

**Client** [00:37:40]
Got it. If I said, "Hey, it's a good day. I want to give you $10,000. You can have $10,000 of NetBox stock or $10,000 of cash." Which would you take?

**Expert** [00:37:53]
I'd definitely go for stock because that is something not stagnant. It will definitely grow in future, because how this NetBox is evolving, from just an IPAM solution to right now, their API first and programmatic approach and how it is easy to integrate into our infrastructure. I definitely see a better way or better future for NetBox. Definitely I'll go with stocks instead of just hard cash.

---

**Client** [00:38:21]
Great. Putting aside a lot of the networking players we've talked about today, any new start-ups or new products you've fallen in love with recently that's made your job much easier?

**Expert** [00:38:34]
With respect to what NetBox is offering or in general?

---

**Client** [00:38:38]
In general.

**Expert** [00:38:40]
In general, I definitely fell in love with how these agentic way of handling the workflows or tasks is growing, how these AI or agents are helping in terms of coding and automations. That is something definitely changing the process across various enterprises and organizations. With this earlier, the development and CI/CD pipelines development and other coding aspects used to be a lot of manual work, and a lot of thinking has to happen in there.

Right now, with these advanced models that can run autonomous tasks with little to minimum human intervention and human oversight, that is definitely something intriguing and definitely something that is pivoting in a new direction to all the technology or other enterprises out there. Not only to tech and other services, but to all possible areas and aspects that is changing how the things are getting done and how these are evolving.

---

**Client** [00:39:35]
Are you guys using a specific agentic framework, or is this not using a framework or any products around there that you've adopted to make that easier?

**Expert** [00:39:43]
Yeah. We have various agentic models. We use Google Vertex AI platform to build agents. We have various other platforms, like specific to agentic AI. We use other coding aspects like Claude Code, Claude Cowork, etc. There are definitive teams which are focusing now more on agentic aspect of this, and definitely, I see the major shift of focus towards these solutions.

---

**Client** [00:40:12]
Very helpful. I think that's most questions I had. I don't know if anyone else on the call has any last questions here. I'm all set. Thanks. Awesome. Thank you for your time. We'll reach out if we have any follow-ups. This has been very helpful.

**Expert** [00:40:33]
Thank you so much for your time, and it's nice connecting to you and sharing what I know, and I hope that is useful to you in some way or the other.

---

**Client** [00:40:42]
Absolutely. Thank you so much.
