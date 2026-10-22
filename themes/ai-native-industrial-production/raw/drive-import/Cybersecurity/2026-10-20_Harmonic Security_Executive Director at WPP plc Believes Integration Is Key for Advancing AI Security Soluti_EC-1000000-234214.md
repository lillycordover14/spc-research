---
theme: "Cybersecurity"
title: "Executive Director at WPP plc Believes Integration Is Key for Advancing AI Security Solutions"
doc_id: EC-1000000-234214
source_line: "Harmonic Security · Expert Call · Customer · 20 Oct 26"
date: 2026-10-20
company: "Harmonic Security"
pages: 2
saved: 2026-10-21T15:56:44.900Z
url: https://research.alpha-sense.com/search?search_id=tmp-l5q00vjpbwvf9aw6o2hl&sort=DATE&order=DESC&docid=EC-1000000-234214
---
# Executive Director at WPP plc Believes Integration Is Key for Advancing AI Security Solutions

Company Deep-Dive

DATE PUBLISHED

20 Oct 2026

INTERVIEW DATE

22 Jul 2026

EXPERT PERSPECTIVE

Customer

ANALYST PERSPECTIVE

Investor-Led (Buy-Side)

PRIMARY COMPANY

Harmonic Security

SMART SUMMARY

Summary

The conversation focused on the organization's use of AI security tools, particularly Harmonic, and the evolving needs for integration with broader cybersecurity and business systems. The discussion also covered market trends, vendor consolidation, and the importance of comprehensive, integrated security solutions for AI governance.

EXPERT BACKGROUND

- Executive Director overseeing enterprise AI, platform strategy, and governance at a large global organization, with direct responsibility for AI governance frameworks, security, and collaboration with cybersecurity and SecOps teams.

EXPERT SENTIMENT

- Believes current browser-based AI security solutions are valuable but limited, and sees the need for deeper integration with endpoint and network security tools.
- Expects the market to consolidate, with larger identity and security providers likely to subsume smaller pure-play vendors unless those vendors rapidly expand their capabilities.
- Views switching costs for current AI security tools as low and is open to moving to larger providers if they offer better integration and data.

TAKEAWAYS

- The organization uses Harmonic primarily for browser-based observability and enforcement of AI usage policies, but relies on other tools like Microsoft Defender and Zscaler for broader endpoint and network security.
- Harmonic's main value is in its browser extension, which provides visibility into user behavior and helps enforce AI governance, but it lacks comprehensive endpoint and network interception capabilities.
- Integration with other security tools (Defender, Zscaler, CrowdStrike) and business systems is seen as crucial for future AI security solutions; current integration is limited.
- The expert pays a low single-digit percentage of what is paid for major cybersecurity tools (like Wiz or CrowdStrike) for Harmonic, reflecting its narrower scope and overlap with other tools.
- The expert is skeptical about remaining a Harmonic customer in five years unless the company rapidly expands its capabilities and integrations, as larger players like Okta and Microsoft are moving aggressively into this space.

Introduction and Expert's Role

Harmonic's Implementation and Capabilities

Browser and Endpoint Security Discussion

Cost and Future of Harmonic

Integration and Broader Security Trends

EXPERT BIO

The expert is the Executive Director of Automation at WPP PLC. The expert is responsible for leading strategy and operations for global Automation programs, including technology direction (UiPath, Power Platform, Microsoft Fabric/Azure AI, Anthropic AI, Google Gemini AI) delivery units, infrastructure and support centre. The expert deployed 75+ process automation projects in Finance (AP/AR/Risk & Compliance), HR and Operations. Expert Delivered over USD12M in cost savings.

Prior to WPP PLC, the expert was the Managing Partner, Operations & Technology at Wavemaker, leaving in January 2021. The expert was responsible for directing the post-merger technology and operations consolidation (Dynamics365) as well as the Cloud & Remote Work transformation program (M365). The expert was in charge of the process Automation (UiPath, Automation Anywhere).

The expert can speak to 25 years of experience across 5 continents, founding and working at advertising agencies and technology startups. Exert can also speak to Agentic AI, Robotic Process Automation (RPA), custom business systems and integrations that empower teams to work at higher order tasks.

View More

INTERVIEW TRANSCRIPT

**Client** [00:00:00]
Hi. Thanks for taking the time to talk with me. I am interested in learning more about your background, your role at WPP, and just a sense of how big the organization is, how big the cybersecurity team is.

**Expert** [00:00:14]
I'm the head of enterprise AI. That's a relatively new role, about three months old, looking after platform, strategy, and governance as part of the center of excellence, which I lead. Enterprise AI at WPP, given the nature of our business, is a smaller part of our AI usage compared to creative AI and agentic media buying operations, strategy, etc. Enterprise AI typically comprises our governance frameworks, taps into TechOps, SecOps, that stuff, and looks at the, I'm going to say, slightly more boring AI than making Super Bowl ads.

We're a smaller team than our big AI product team, but we do look after governance frameworks, including security, identity, and trust, etc. My team is in charge of working with our CISO and our SecOps team on AI and agentic governance and security. We use Harmonic and other vendors for observability, for implementation of controls, for enforcement of those controls, etc.

---

**Client** [00:01:15]
Got you. How did you come to use Harmonic? What was the origin story?

**Expert** [00:01:23]
I inherited it, but it was very early days. It's been applied in layers. The first was just observability. We had no idea across our estate on who was using what, particularly when it related to the earlier days of web-based ChatGPT, claude.ai, Gemini type of stuff. Predominantly the concern was visibility.

Since I've joined, we've moved on to a roadmap of progressive enforcement of policy. We've moved beyond just observing to intercepting with their browser extension. If you land on something that either is or is not allowed or has some various degrees of governance and control, we can tell that if you're within our network and on our managed browser in our estate. We can tell that and give people a special message. "Hey, you're using an off-brand AI here. Be very careful. Here's a link to all of our acceptable use policies," etc. We have a green, amber, red simple criteria. If you're using something that's red light, it blocks you at the network level in a managed browser.

We have other tools that close some of the open doors regarding access when you're not using a managed browser, not in our network, or not on our device. Harmonic has some good intelligence of figuring out what is an AI thing that you are trying to do on the web or via the network, what are the prompts and other instructions going through, but it's not a comprehensive solution. We have other tools in there, including Microsoft Defender for Endpoint, including our network security, your Zscaler or or endpoint web proxies, etc., and then we have on-device endpoint protection, again, through Defender, logging and other calls through other parts of our SecOps estate. We also use another player, very similar, decent overlap with Harmonic, called AI Score, who are very small out of the U.K.

---

**Client** [00:03:15]
Got you. Maybe just to go a bit deeper on what you were saying around how it works. My understanding is they started with a browser extension.

**Expert** [00:03:25]
That was the foot in the door, and that was the first one we started with.

---

**Client** [00:03:30]
Yeah. It sounds like they're now doing enforcement on the browser, that they're also doing it maybe on the endpoint, but you've also got Defender for some of that endpoint stuff. It sounds like you're trying to enforce it via the network as well. Talk a bit about where Harmonic Security is operating.

**Expert** [00:03:50]
Currently the strength is the browser. It's browser intercept. If it's part of [Active DD] or something, you could probably ask them on what they're doing regarding identity and access management as well with the likes of Okta and Auth0 and stuff like that if they're looking at tapping into those.

The browser extension was their beachhead. They have a sophisticated set of models that understands what good and bad behavior within the browser looks like, not just hitting a domain, claude.ai or chatgpt.com or whatever, Midjourney or Higgsfield or something even worse. The actions you take within there are tracked as well and that they have a type of anomaly model.

We haven't seen it, and I don't recall that we've even thoroughly tested it. They purport to look at anomalous actions like data egress or things like that. We are just ramping up our movement from observability or tracing into controls and enforcement through the rest of the year.

It's the browser extension. The data they're collecting allows them to understand what good and bad looks like and what anomalous behavior looks like. Now that they have that data, they can make better decisions with different data sources. We don't yet, but you could connect something like a Defender for Endpoint, the logs out of that. Defender is a highly generic solution. It doesn't know what AI looks like unless you go type those URLs in, and there are lots of them.

At the end of the day, the browser extension is good for visibility. Could we hand roll our own? Yes, but could we keep up with the volume of both URLs and behaviors that are good and bad, and manage the policies there? No. We'll just pay someone to do that because it's impossible.

Every day, a new SaaS AI thing pops up. Defender doesn't have that subscription service. It wants you to put all the URLs in or all the devices or all of the binary signatures of all the endpoint installed desktop solutions that are good or bad, and that's the stuff we need to buy. That data is what we're buying off an [AI Score] or would be buying off someone like an Onyx, etc., and went with Harmonic, looking at AI Score, looking at where we need to solve our own issues at the deeper endpoint level as well.

---

**Client** [00:06:16]
Got it. What I'm curious about is it sounds like, obviously, it's got this pretty impressive browser product that's working for you guys. If I think about this space, part of what people seem to be worried about is a lot now, especially agentic security, is not happening in the browser. It's happening on the endpoint. It's happening in Claude Code or it's happening in desktop solutions now. How does the Harmonic help you address that? I'm actually more curious about what they do today than the roadmap.

**Expert** [00:06:49]
They don't yet have a network interception product. Many of these businesses are working on things like MCP gateways or LLM gateways, but that's very happy path governance. That's like, "We're going to set up all these hoops for someone to jump through. If they jump through all the hoops, we'll know what they're doing and can control it."

We're not that type of business. We have 85,000 people. They all want to get their work done. They're going to connect via OAuth to an MCP, and we need to figure out that they've done that and fix it on their desktop or in their cloud client. It's very hard for us to say, "Oh, we can put lots of security in if you only put this MCP endpoint in for a gateway or whatever."

Yes, they're probably working on a gateway-type solution, but really we need to be tapping into proper endpoint security and figuring out where the bad behavior is, correcting it via, hopefully, automatically. When someone is in Claude Code, adds an MCP or starts to connect to least our network, starts to [go back] to APIs and stuff that we can monitor that, look what good and bad behavior looks like, and either get into that Claude skill or Claude plug-in or code auto-magically and just correct the error, particularly as it moves from dev to prod as part of DevOps, or contact that person and be like, "Oi, we've sent you three emails. It says to use this MCP gateway. You're not doing it. Your Claude is getting shut down." That's the level of control we're implementing now.

What Harmonic has, if we were to use them as either a gateway product or at least as a data source, an intelligence layer of what good and bad anomalous behavior looks like, that's still better than we could get in Defender. Defender catches the data, but it doesn't really do as much about having sophisticated policies.

---

**Client** [00:08:40]
Yeah. That's my concern. They're very early start-ups, so I'd be surprised if they made it onto your radar. In my world, we're seeing a whole range of start-ups coming out that are really exclusively focused on the endpoint doing AI security there, and they're saying, "We'll plug in SentinelOne," or "We'll plug into Defender or into CrowdStrike. Whatever endpoint agent you have, we will sit on top of that, and we will look at the."

**Expert** [00:09:08]
You call it complimentary intelligence or parasitic intelligence. Palo Alto have a thing like this. It's the thing that a Palo Alto would've done for network type stuff, but it's for agent type stuff. Everyone wants to be the Palo Alto of agents.

---

**Client** [00:09:24]
Yeah. There's a lot of these businesses being built. If you're curious, it's stuff like Sun Security or Pluto or Bay Security. There's a bunch. I'm curious, because that feels to me a little bit like where the market is going as opposed to Harmonic, which strength is in the browser, which is a little bit where the market was. Is that fair, or is that unfair? I'm curious how you think about it.

**Expert** [00:09:52]
It is. The browser is the data moat. The browser allows you to connect behavior that indicates, look, if you want to use Claude Code or Cursor or something and do stuff on the endpoint, you still have to auth through a browser. The browser behavior is a very good indicator of on-desktop behavior for us. We know if you are experimental or adventurous and you are visiting a lot of, call it, off-deck solutions, and we know you have Claude Code, Claude Desktop, GPT Desktop, fucking Manus, OpenClaw, etc., installed. The combination of those behaviors is very good data to indicate you're doing dodgy stuff, even if we can't see it.

If we didn't know what you did in your browser, then we wouldn't really have the proof that you're authenticating with the wrong things. The browser is still a very good tollgate of behavior. You need a browser to OAuth. Everything is OAuth. We have about, call it, 8,000 engineers out of about 85,000, 90,000 people. Of those 8,000, most of them are using browser-based OAuth. No one's hand-coding their own certificates and API keys and stuff.

The browser's still a very important data set, which is why we like that Harmonic has been in our browsers for so long because they are building up a very solid data set of what our people's good and bad behavior looks like, not some generic data sets. That's a strength, I believe. Everyone else is just going to have some generic anomaly model of what good and bad agent behavior looks like, but they don't know what our policies are by either definition or by inaction that could inform their generic models.

---

**Client** [00:11:36]
Thank you. I'm curious how much you are paying for a tool, willing to pay for a tool like Harmonic. How does that compare to what you pay for some of your other cybersecurity tools?

**Expert** [00:11:49]
I'm not going to tell you how much we're paying, of course. It's very hard with cybersecurity stuff because it's always so bundled. All the Microsoft stuff's bundled into your E3s and E5s. What are we paying for it? I don't know. It's very hard to tell. You get into your CrowdStrikes and your Wizes and stuff, and those are such big deals and, again, bundled with those hyperscalers.

---

**Client** [00:12:15]
Do you pay for Wiz, for example?

**Expert** [00:12:18]
Yeah.

---

**Client** [00:12:20]
Maybe if you had to guess, as a percentage of what you pay on Wiz or CrowdStrike, what percent do you pay to Harmonic? Is it 5%, 2%, 10%, 30%? Maybe just give a rough order of magnitude.

**Expert** [00:12:36]
Low. It'd be definitely down.

---

**Client** [00:12:40]
Single digits?

**Expert** [00:12:41]
Yeah, let's say low single digits. Those other tools just do so much more. The risk profile with an estate the size of ours, Harmonic is a very small pure-play provider. There's a lot of overlap with other tools. The space will converge, absolutely. You've got players now like your Oktas, etc., who are moving in with agent security and saying, "Well, we also know what good and bad behavior looks like. We're also at the identity layer, which is useful. We're also in the browser with Okta FastPass. We're also on the machine, so we've got a lot of these tendrils into the behavior," and that can be quite compelling as well to start to have them expand.

I was just saying there are players moving in such as Okta, such as other identity players, even Microsoft absolutely taking a space, just lumbering. These pure-play providers are a lot faster. They're a lot more flexible. We can work with them directly on roadmap. For the small amount we pay, the value is pretty real for now. Will the space converge and we just move on to someone bigger, whether it's Google's expanded SecOps capability or Microsoft or Okta? Who knows?

---

**Client** [00:14:01]
Yeah. How hard would switching be?

**Expert** [00:14:05]
Switching cost is very low. Switching cost is pretty low on this. There are some policies that make a browser thing installed. Yes, we would lose the historic data, but we'd only buy into something that had better and more data, maybe Google size or Okta size data sets. When they have a product, we would look at that.

---

**Client** [00:14:26]
Got you. Just on that point, if you had to guess, do you think you'll be a Harmonic customer in five years?

**Expert** [00:14:35]
They would need to scale their capabilities faster than they have been. That may happen. Look, at the speed and aggression that the bigger players are moving, my bet would be no. Don't put me on record for that. That's background only.

---

**Client** [00:14:50]
I'm not super surprised. That's helpful. I'm curious, when we talk about scaling the capabilities, what capabilities would you like them to see? Where would you like them to go? I'm just curious, where do they need to go to be a broader platform?

**Expert** [00:15:10]
I'd say, I think their strength is data and the modeling. They need one-click integrations or much simpler integrations with the key network and endpoint security things, so better integration into Defender, better integration into Zscaler, CrowdStrike, etc., so that that promise can be realized. It's just SecOps system integration and more sophisticated policy management. The policies are pretty simple right now.

I would love them to be able to tap into third-party policy services, something like a Cedar or an OPA type server, so we could have policies that are written across things that don't tap into Harmonic. Let's say we're running our own agentic framework, building our own kit, and we have some policies of what good and bad stuff looks like and what we will allow and won't. Right now, we need to go reconfigure those policies into Harmonic. It'd be fantastic to just have those structurally ingestible. Those are all achievable.

---

**Client** [00:16:05]
Totally. To me, that first point you made seems crucial, which is if you need to integrate into Zscaler and Defender to actually do AI security efficiently, because you have to move not just off the browser, you need to have those integrations. Otherwise, you're just stuck at the browser, and that seems like a very tough spot to be in, my view. I don't know if that resonates.

**Expert** [00:16:28]
We were talking about integrations being key.

---

**Client** [00:16:31]
Exactly, we were talking about integrations being key. I was checking whether you agree with that.

**Expert** [00:16:38]
In addition, what we want to see is integration two ways, is consumption of data from system logs. We want an intelligent way to pass over things such as our access to SaaS systems, whether there are authentications there. Think Workday, Google, Meta ad buying systems, we want to know if there is behavior in those that looks unusual or agentic, whether there are OAuth authentications on there. We would love Harmonic to be a middle layer, an intelligence layer that we can ingest logs from things that don't have good reporting, do a pass over it on does this look good or bad, and then pipe that back out to a SIEM or back out to our system as well.

It's integrating with our endpoint and network data in those integrations, integrating with our business systems as well because we don't have good threat intelligence of those businesses. Workday doesn't have a good threat intelligence. It assumes any work happening on Workday is good work, but that may not be the case. Google and Meta assume if you are buying tens of millions of dollars of ads very quickly that that's you having a good time, not you being hacked, and they won't do anything about it. We want a system that can in very much close to real time identify bad agent behavior on those third-party systems as well. Business system integration and security framework integration would be the key things we want to see out of them.

---

**Client** [00:18:00]
That makes a lot of sense. In the last bit of time we've got, anything else you're seeing in agent security or AI security or security more broadly that you're excited about that you think, "This tool is really awesome. I couldn't live without it"?

**Expert** [00:18:14]
Just what the identity players are doing. Microsoft haven't really moved as fast as we would like around connecting Entra and their other security stuff, the Purview, etc., into Agent 365. That was a bit of a bust. I think they had a very good opportunity there to look at an enhanced security solution.

I think where Okta are heading, which is that they are combining their identity threat model. If I log into Okta from four different countries in 300 milliseconds or something, it's probably wrong. That looks bad. They have some decent security products through acquisition under the hood there that can identify bad behavior as it relates to identity and authentication. They're also bringing that tech into agent behavior. If you use them as a gateway, if you use them for agent identity authentication, pass-through, etc., I think they have a good, strong position.

They're not a start-up. They're a fairly established player. They're well-positioned. We are keeping a close eye on what they can bring in. We have 100,000 people on Okta. They use it to auth on most of our important business systems, and so they have a really good view on who's doing what. We just need them to upgrade that to assume that we're authenticating not on behalf of ourselves as humans, but also on behalf of systems and agents. What are those agents doing with that auth is something that they can tell us.

---

**Client** [00:19:41]
Thank you for taking the time to speak with me. Have a nice day.
