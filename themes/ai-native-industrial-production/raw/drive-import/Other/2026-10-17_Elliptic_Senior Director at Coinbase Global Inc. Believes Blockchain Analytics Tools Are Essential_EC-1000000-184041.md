---
theme: "Other"
title: "Senior Director at Coinbase Global Inc. Believes Blockchain Analytics Tools Are Essential Despite Market Limitations"
doc_id: EC-1000000-184041
source_line: "Elliptic · Expert Call · Customer · 17 Oct 26"
date: 2026-10-17
company: "Elliptic"
pages: 2 of 2
saved: 2026-10-19T16:55:44.202Z
url: https://research.alpha-sense.com/search?search_id=tmp-0pnbg1kc8uodovl7vbczkp&sort=RELEVANCE&order=DESC&docid=EC-1000000-184041
---
# Senior Director at Coinbase Global Inc. Believes Blockchain Analytics Tools Are Essential Despite Market Limitations

Company Deep-Dive

DATE PUBLISHED

17 Oct 2026

INTERVIEW DATE

20 Jan 2026

EXPERT PERSPECTIVE

Customer

ANALYST PERSPECTIVE

Investor-Led (Buy-Side)

PRIMARY COMPANY

Elliptic

OTHER COMPANIES

Chain

SMART SUMMARY

Summary

The conversation focused on the use, selection, and limitations of blockchain analytics tools for compliance and transaction monitoring in the cryptocurrency industry. The expert discussed provider differences, workflow integration, regulatory drivers, and the challenges of limited market competition.

EXPERT BACKGROUND

- Senior Director at a leading global cryptocurrency exchange with extensive experience in compliance, transaction monitoring, and the implementation of blockchain analytics tools for risk management.

EXPERT SENTIMENT

- The expert views the current blockchain analytics provider market as limited and not highly competitive, with each provider having notable gaps in coverage and attribution.
- Despite the limitations, the expert believes these tools are essential due to regulatory requirements and the need for ongoing transaction monitoring, but does not express strong preference for any single provider.

TAKEAWAYS

- Multiple blockchain analytics tools (e.g., Chainalysis, TRM, Elliptic) are used for different compliance and investigative use cases, such as transaction monitoring and deep-dive investigations.
- Providers differ in coverage, responsiveness, and cost; Chainalysis and TRM are seen as having better API responsiveness, while Elliptic may be cheaper.
- Coverage of blockchain addresses is limited, with only about 30-40% of addresses attributed to entities; none of the providers have over 50% attribution.
- Switching between providers is feasible but requires technical effort; workflows are ideally vendor-agnostic to allow flexibility.
- Regulatory requirements and the need for attribution and transaction monitoring ensure continued demand for these tools, despite their limitations.

AlphaSense Smart Summaries are AI Generated

Introduction and Use Cases

Comparison of Providers

Regulatory Impacts and Compliance

Tool Selection and Evaluation

Procurement and Market Dynamics

EXPERT BIO

The expert is currently a Director at Coinbase Global. Expert is a customer of Elliptic.

The expert is currently a Director at Coinbase Global, working at the company for 5 years. Within this role, the expert is the Director for the investigative unit, responsible for preventing any cyber attacks on-chain, AML/AMC, and running an international team of investigators conducting investigations using analytical software into the movement of funds. Within this role, the expert uses a number of tools including Etherscan and Kodex.

The expert can speak to Cryptocurrency as a consumer and an investigator. The trends in the present and the future in blockchain technology. As a consumer, he has used centralized and decentralized Ethereum and Bitcoin. He can speak to crime in the cryptocurrency area and compliance.

View More

INTERVIEW TRANSCRIPT

**Client** [00:00:00]
Hi. Thanks for taking the time to talk with me. I am interested in learning more about Elliptic. Would be good to get a recap of who do you use and potentially the setup, and then we can take it from there.

**Expert** [00:00:15]
Right. We use multiple different tools with different use cases. I think it depends what your use case is. Are you doing transaction monitoring? Are you doing deep dive investigations? The tools have different product offerings dependent on your use case.

You can consume the data provided by TRM, Chainalysis, Elliptic in your transaction monitoring systems. That would be something they do at scale via API integrations, either washing prospective transactions that might be leaving your platform, against their database or against their calls, to give you an indication of the risk of a particular address or whether or not you need to block it.

You would then also do, maybe, retrospective analysis on customer transactions. Have any customers received from this entity or this cluster, etc? Not just in terms of transaction monitoring, but maybe deeper dive into customer activity. Does your customer base only interact with a few other VASPs or exchanges? That's one use case.

The other use case is a more deeper dive investigation that your complex investigations unit might do, or those who are more free-ranging security operations, security investigations, etc. That's using the graphical user interface, or potentially just the data from each of those tools, to map out transactions from point A to point B to identify a source of attribution or, for example, where there might be a cash out.

---

**Client** [00:01:52]
Maybe on the difference between the first two, to understand the difference between, I want to call it pre-screening, maybe you call it something else, and the ongoing transaction monitoring, is the first one, I'm a customer, I want to send funds from one wallet to the other, you're running a check of how risky is that wallet? In that case, is Elliptic or Chainalysis doing the tagging in real time, or if the tagging is not there, even if it's a scam, they wouldn't report a risk to it.

**Expert** [00:02:22]
You can do one-hop, two-hop analysis. It depends on your risk threshold and certainly, retrospectively, the same again. For example, Chainalysis and Elliptic will maintain historic databases of addresses which have been flagged for either sanctions evasion, terrorism financing, CSAM, etc., then using their heuristics, depending on the chain, may extrapolate the attribution to cover more addresses. They have that information already, and you're essentially pre-screening against that database via an API call as the relative risk of a transaction.

---

**Client** [00:03:00]
Let me maybe ask you that question, because that's something I'm trying to understand. Obviously, they're running the heuristics and the nodes and they're tagging wallets. What if I created a new wallet today, and I'm a bad actor and I want to send funds from somewhere to this wallet? Is the tagging of the risk happening in real time or because that wallet was just very newly created, it will show a very low risk? Is the database static and they update it every month or week or whatever, but if it's not tagged in, then it will show nothing if it's a new wallet?

**Expert** [00:03:35]
First of all, you'd have to ask Chainalysis, Elliptic, how often do they push that data or how often is the database updated with new addresses? Of course, if someone created a brand new address, there's no history to it, there's no attribution, so you would probably attribute a low risk to it, but then you'd have another set of, for example, your controls, which is of course the Travel Rule requirement.

You'd be asking your customer, essentially, "Why are you sending these funds? Who is it to?" to then build up your risk profile of a particular transaction and, of course, the customer themselves. The attribution and tagging of addresses is one part of your framework.

---

**Client** [00:04:17]
Got it. If it's a new wallet, it wouldn't be, but it's not the only thing you rely on. You have other workflows and controls, which is part of the broader compliance systems and controls you set, to be able to understand it.

**Expert** [00:04:32]
Yeah. Of course, you've got the customer themselves as well, they're going to have a customer risk profile, aren't they? If it's, for example, an elderly person and they're emptying out their account, then you're probably going to stop that transaction, and that's not dependent on your provider, Chainalysis or Elliptic. You'd do that anyway.

For example, is it a large institutional company that's suddenly sending out rapid movement of funds to brand new addresses? Again, that might raise your risk as to, maybe, there's been an account takeover. Again, it's part of your monitoring framework, encompassing other alerts and monitoring and models, for example, logging activity, Travel Rule compliance, customer profile, etc.

---

**Client** [00:05:19]
Got it. I have a few follow-up questions on that. One question I want to ask is, are you familiar with a company called Hypernative?

**Expert** [00:05:30]
Not really.

---

**Client** [00:05:32]
Okay. I feel like what they're doing, they're more on the security layer. What they're doing is, they're saying, "We're monitoring the blockchain." If a new one is created, and then, automatically, when I send something to it, they do the attribution in real time, so it's not lagging like the likes of Elliptic and Chainalysis, where it gets updated. It's more like they are tracking behaviors at all times and are able to do the tagging in real time of the score.

**Expert** [00:06:03]
Yeah, that's like Alterya and Blockaid. That's not attribution. That's just providing a risk level for the address. It's not providing an entity name. Again, it's based on behavioral heuristics as opposed to hard identifiers, i.e., this address is a scam, this address is TF etc. It's behavioral. It could be something that you have in conjunction to Chainalysis, Elliptic etc., because that will give you hard identifiers, as an entity.

---

**Client** [00:06:35]
Got it. I'm trying to understand, "When you're sending it, run your API, let me know if it's tasked to certain activities that I want to be tracking. Maybe, at the second layer, also test behavior, so, oh, if it was created minutes ago, then I want you to flag it with this risk," so that adds a layer on top but doesn't remove that. You still want to know if it's gambling, for example, based on the database of Elliptic and Chainalysis.

**Expert** [00:07:03]
Yeah. Also, you might have an exchange that creates new addresses for deposits. It depends on what are the heuristics, and of course, they can only give you an indication as to the level of risk. It's what you do with it afterwards that counts. Also, you can have different risk levels for different types of addresses on different chains. For example, a brand new address on ETH may attract higher risk than a brand new address on Bitcoin.

---

**Client** [00:07:31]
Got it. All those, are you setting those limits, or are you creating workflows around these tools, and how are you managing it? It seems like a very complex system.

**Expert** [00:07:43]
It is. I think there are lots of different workflows. You just have to do what's scalable for your own organization and what your risk tolerance is, depending on which jurisdiction you are in.

---

**Client** [00:07:56]
Yeah. These workflows, are they built on top of the solutions like Chainalysis, TRM, and even the Hypernative, or you're using their software to do it? How's the setup?

**Expert** [00:08:06]
This is hypothetical, so I'm not going to go into the ins and outs of our compliance framework. You wouldn't want it dependent on a provider, you'd want it vendor-agnostic, so that if you need to replace a particular vendor, your workflow stays the same, your ingest stays the same. It's just the source of data is different. You will probably move from one provider to another depending on the competitive market and also cost.

---

**Client** [00:08:32]
Yeah, you don't want to be over-reliant because they're quite mission-critical.

**Expert** [00:08:37]
Yeah, all the regulators will want you to use one of the big three firms.

---

**Client** [00:08:41]
That makes sense from a business perspective. One thing I wanted to touch on is a bit, the Travel Rule, and I think something around the EU regulations that they were mentioning. There are limits to how much money you can send to self-hosted wallets, that, a bit anonymized and haven't done the KYC. I also understand that the self-hosted wallet transaction is not a huge part of the total transaction, so most of it is already happening within the centralized world.

I want to understand how does that impact the value proposition of tools like Elliptic, Chainalysis, and TRM, given your perspective. Think of a world where Coinbase can only send to other regulated institutions or banks, like the way transfers between bank accounts happens today. Does that remove the value proposition, or not really? I'm going back and forth in how to think about that.

**Expert** [00:09:39]
Not really because people always use self-hosted wallets.

---

**Client** [00:09:43]
What if self-hosted wallets are illegal? You're a regulated institution, the regulators are telling you, "You are no longer allowed to send money to a self-hosted wallet," and it just becomes between KYC-known wallets?

**Expert** [00:09:59]
That might happen. If it does happen, then you'll just have to deal with that regulatory environment, won't you? Again, they're not going to get rid of the Travel Rule data, and you're still going to need to conduct transaction screening, etc. Who's to say, then, the address at Binance isn't a terrorism financing address. You're still going to need that attribution.

---

**Client** [00:10:23]
Isn't, then, Binance responsible for knowing if that account is terrorism?

**Expert** [00:10:29]
Yeah, that's down to the analytics providers and information fees, or an address is related to a scam, or, for example, there's a brand new exchange or a new entity.

---

**Client** [00:10:40]
How does it work today? Today, when you're sending from a bank account to the other, you need to make sure your own accounts are clean and you're doing the KYC and you're screening it, but you're not using someone like an Elliptic or a Chainalysis to do it for you?

**Expert** [00:10:57]
You could say that banks do do that, don't they? They use Refinitiv, Thomson Reuters, etc., to do screening of their customers. They're screening customers as they get onboarded.

---

**Client** [00:11:11]
Exactly. I think it will still happen by. Why can't, then, a Refinitiv or Thomson Reuters do it instead of an Elliptic and Chainalysis? Today, their power is in the data, but if the data becomes not anonymized, doesn't it reduce their value proposition? I'm speaking out loud at this point.

**Expert** [00:11:34]
No. There's always going to be a market to understand what the exposure of an entity is. Say, for example, that you deal with institutional clients. You're going to want to know your institutional clients, what their wallets, what their exposure is, who else do they trade with. You can only do that with attribution.

Likewise, for example, another company, say you are trading with Binance a lot, and then you suddenly see Binance or Coinbase have a lot of exposure to scams or terrorism financing. Are you going to stop your customers interacting with them, or a gambling site, or a peer-to-peer entity? Secondly, your business would want to know what the flow of funds are.

---

**Client** [00:12:19]
I think that makes sense. Does that mean it reduces their value from just the ongoing transaction monitoring, to more on a KYC, one-off checks, and then you run it a bit less? Does it reduce the scope, or not really?

**Expert** [00:12:35]
No, I think you're still going to need that ongoing transaction monitoring. There's always that level of risk that for example, an address that a customer sends to may be tagged or flagged as something, even if it's at another entity.

---

**Client** [00:12:50]
Okay. How do banks do it today for normal transactions? And the NICE Actimize and all of that, but how are they monitoring these enormous flows from more normal payments?

**Expert** [00:13:04]
Obviously, they don't have the blockchain analytics element of it, but they do do the counterparty risk assessment. Are you sending funds, for example, a bank, or in Dubai? Where are you sending your funds to? You'd have the same things that we would do, like a customer risk profile. How much are they sending? Is this out of their normal activities? Is it in line with their normal expected activity? What has the customer said that their expected activity is? What was the last KYC? Do we need to refresh that? Do we need to get on a call with the customer?

---

**Client** [00:13:47]
Got it. Here, the data is not public, like the public ledger?

**Expert** [00:13:52]
It isn't. It's proprietary because they gather their own attributions and keep that to make their tools competitive, so you have to pay for it.

---

**Client** [00:14:04]
Got it. If anything, the blockchain is more transparent in that way because you're able to trace where flows are, versus, if a bank is sending flows to another bank, no one knows it except the bank.

**Expert** [00:14:17]
Yeah. Everyone can see all the transactions. Obviously, once you get the attribution in there, then you can have more visibility.

---

**Client** [00:14:27]
Got it. Last question on that topic is a bit of the Travel Rule. Can you just explain to me what does it entail? Just to understand if that's a tailwind or a headwind for solutions like Chainalysis, Elliptic, and TRM.

**Expert** [00:14:42]
Travel rule is separate, and there are other providers out there. Travel rule means that a certain piece of information must be transmitted and entered in by the customer, on a transaction, such as, who is it going to, what's it for, etc., where is it? For example, "I'm sending it to Binance to my friend's account, XYZ," so you'd have to have a system whereby that data is transmitted to the counterparty. That's separate to Chainalysis, TRM, and Elliptic. There are other solutions out there who cater simply for the Travel Rule data.

---

**Client** [00:15:17]
Got it. On the receiving end, then the other exchange will get the information from the Travel Rule, but also attribution from these tools. It's like two data inputs, correct?

**Expert** [00:15:30]
Yeah. You'd have two levels when you're checking your transaction, for example.

---

**Client** [00:15:36]
Got it. The reason why it wouldn't reduce the relevance for a Chainalysis and an Elliptic is more because like it's not enough for you to decide, are those funds compliant?

**Expert** [00:15:47]
Yeah, and it's a separate regulatory requirement.

---

**Client** [00:15:50]
Got it. Moving on, when we were talking a bit about the need for having two vendors, it felt like you were telling me that you use different ones for different use cases, whether it's the pre-screening or the ongoing transaction monitoring or the investigation.

**Expert** [00:16:05]
Yeah.

---

**Client** [00:16:06]
Which one do you use for the pre-screening, which one do you use for the transaction monitoring, which one for the investigation, and why?

**Expert** [00:16:14]
It depends on what your users like. If you're looking at the in-depth investigation, some people prefer Chainalysis, some people prefer TRM, some people prefer Elliptic. It really does depend on how they use it and how experienced they are. You may have a lot of investigators who say, "No, we only want to use Chain. That's all we've trained on, that's what we're used to." Others may say, "Don't like Chain because it only does things at the cluster level. Prefer TRM, which does it at the address level."

Now, in terms of transaction monitoring, you're going to have to decide that based on the responsiveness of each of those tools. How many transactions will you be processing each day? How are you going to screen them? Are you going to do an API call for every single transaction? That might be quite expensive.

Will you simply maintain a database of all attributions and get it updated by them, and simply wash a transaction across on them to generate alerts retrospectively? You'll have to decide which one of those vendors can meet your requirements, based on their responsiveness, how many API calls they can process, how expensive it will be.

---

**Client** [00:17:26]
Got it. On the transaction monitoring front, which one is able to have the fastest API response rate today? I guess, for a large-volume customer, that's important because I'm thinking of myself as an end user. If I'm waiting around, it's not a great user experience.

**Expert** [00:17:47]
Yeah, I think it's probably going to be either Chain or TRM. They've invested the most in their infrastructure. I would definitely ask them who's got the quickest one, and also ask them, "What's your coverage of different typologies?" You will find there'll be differences between each of those providers and what level of coverage they provide for each typology.

---

**Client** [00:18:08]
When you say typologies here, is it number of chains, or is it more like scams, gambling?

**Expert** [00:18:15]
Scams, terrorism financing, CSAM, sanctions.

---

**Client** [00:18:20]
Got it. You think that Chainalysis and TRM have faster API responses than Elliptic?

**Expert** [00:18:28]
I think so, but I think Elliptic might be cheaper.

---

**Client** [00:18:31]
Okay. Even if you have the same setup?

**Expert** [00:18:36]
Yeah.

---

**Client** [00:18:38]
Got it. What about the ability to handle large volume and uptime resilience? How would you rank them?

**Expert** [00:18:47]
I wouldn't. I haven't experienced any sort of downtime in either of them. I would speak to them and ask them, "What's your SLAs?"

---

**Client** [00:18:56]
In terms of usage, we talked about using different providers for different use cases, but there's also coverage by, maybe, blockchains because they don't have the exact same coverage. Do you also have a setup where, even within transaction monitoring, you would have one tool focusing on certain chains versus another tool on other chains?

**Expert** [00:19:16]
Yeah, definitely, you'd mix and match. You'd say, "I want Bitcoin from Chain, ETH from TRM," or vice versa, "Solana from this one." You can mix and match, so you've got the best coverage, especially if you're dealing in Tron and Solana.

---

**Client** [00:19:33]
Got it. Who's the best for Tron and Solana?

**Expert** [00:19:37]
Chain is better on Tron.

---

**Client** [00:19:40]
Okay. What about Solana?

**Expert** [00:19:43]
I think Chain again. What I would say is, you probably want to do vendor evaluations every year, is it still the same?

---

**Client** [00:19:52]
Yeah. Maybe on the choice of the tools, for large exchanges or more specifically for you guys, does procurement happen at global level, or each country can pick and choose what they want?

**Expert** [00:20:04]
Yeah, it depends on how your financing works really, doesn't it? Do you want this to be a shared service across all divisions and operating units? Don't forget, it's not just compliance who might use this data, might be your security operations team, might be insider threat. It might also be your marketing team, your market analytics. Lots of different teams can use this data for different purposes. I would probably address this as a global level procurement as opposed to entity level.

---

**Client** [00:20:37]
Got it. It would make more sense. Also, if I think about it from the outside in, your controls, you probably want them to be at the global level as well?

**Expert** [00:20:50]
Yeah, I'd say, you probably want base global level controls, and then each particular entity segregated by customer jurisdiction. You probably want some other types of protections or restrictions or flows working on top of that, depending on what the MLRO wants.

---

**Client** [00:21:08]
Got it. One question, maybe going back to the product. Is the transaction monitoring the same the pre-screen? Is it the same tool doing it or is it two different tools usually?

**Expert** [00:21:22]
It's multiple different tools depending how you implement it. You may just want to maintain the database of the attributions from those different providers and your own bespoke ones, or those generated by, for example, your customers who report a scam. What are you going to do with that? Are you going to block the address? You're going to keep it in there, you're going to do your own analysis? It really does depend. Also, whether the regulator is happy with your solution as well.

---

**Client** [00:21:54]
Got it. How easy is it to switch away from one provider to the other?

**Expert** [00:22:00]
I would say there'll probably be a bit of an uplift because they might have different ways in which they integrate, their API feeds into yourselves. Sometimes, there will be a bit of an uplift.

---

**Client** [00:22:12]
Is it like one month, two months, three months?

**Expert** [00:22:16]
It really does depend on your engineering resources and how much you have.

---

**Client** [00:22:21]
Okay. Is there retraining of the workforce associated, or it's mostly a technical effort?

**Expert** [00:22:28]
Yeah, I think it's mostly the technical level. An alert should just be an alert, in how you deal with it on your end.

---

**Client** [00:22:36]
Got it. How would you rank stickiness on a scale of 1-10, 10 being the highest?

**Expert** [00:22:43]
Which one, sorry?

---

**Client** [00:22:45]
It's just stickiness, overall, of these solutions. How hard are they to replace?

**Expert** [00:22:53]
Because there are only a few providers, I don't think it's difficult to replace them because they're all looking for market share. I think the difficulty comes in deciding which one to go for because they all do things a little bit differently.

---

**Client** [00:23:07]
Got it. What are your key decision criteria for purchasing the tool?

**Expert** [00:23:13]
Yeah, coverage and responsiveness.

---

**Client** [00:23:15]
Responsiveness for API calls or just customer service responsiveness?

**Expert** [00:23:20]
API calls. How fresh is the database? How often do they update? Can they do bespoke attributions for you? Can you task them? If you don't have an incident response capability, can they provide one for you? The other thing would be what exposure does having one of these tools give to you? For example, TRM has a beacon chain, which is like a public-private partnership, which gives you exposure to law enforcement and some of those other regulatory-type entities which you can use to improve your reputation of your business.

---

**Client** [00:23:57]
Got it. How do they rank each one? Maybe we can go one by one. For coverage, how would you rank them? Maybe one, two, three. We can go through the rest as well.

**Expert** [00:24:11]
Chain has got the best coverage, then TRM, then probably Elliptic, but they're all very much within, I think, about 30%-40% coverage of the entire blockchain.

---

**Client** [00:24:23]
That's in terms of chains they cover or in terms of wallets they cover?

**Expert** [00:24:28]
That's in terms of how many attributions they have. The blockchain, all of the chains, all addresses, there's only 30%-40% which are actually attributed to an entity. The rest is unknown.

---

**Client** [00:24:42]
What about responsiveness, the API code, how fresh the data is? How would you rank them?

**Expert** [00:24:51]
Off the top of my head, I'd say Chain and TRM, one. Elliptic, two.

---

**Client** [00:24:57]
Got it. Can they do bespoke attributions?

**Expert** [00:25:01]
They've all got their own in-house investigative units, so they can do that. They're all pretty much the same.

---

**Client** [00:25:08]
Got it. From an NPS perspective, how likely are you to recommend each of these tools to a peer? How much would you rank each of them?

**Expert** [00:25:18]
You're going to have to use a tool, so it's one of those three. It's either/or, really.

---

**Client** [00:25:26]
No. My question is more, how likely are you to recommend Chainalysis to a peer in the industry, on a scale of 1-10?

**Expert** [00:25:35]
Seven.

---

**Client** [00:25:35]
What about Elliptic?

**Expert** [00:25:38]
Probably six.

---

**Client** [00:25:40]
What about TRM?

**Expert** [00:25:42]
Probably about a seven as well.

---

**Client** [00:25:46]
Got it. These are not very high. What do you not like about these solutions?

**Expert** [00:25:54]
It isn't a very competitive marketplace. None of them have got anything over 50% attribution. Each one of them has their issues around different chains, and certainly in terms of coverage as a whole.

---

**Client** [00:26:07]
Okay. Are they impacting the business cases?

**Expert** [00:26:12]
No, they're not impacting it. It's such a small number of companies involved in this, that they essentially have cornered the market. You have to use one of these tools or all of them or two of them. You have no other choice because regulators are also using these tools, so you need to see what the regulator sees. Until there's much more competition within the market, and certainly on features and products that each of them offer, you're not going to get high scores from me.

---

**Client** [00:26:42]
Got it. I think that's it. Thank you so much. Appreciate you spending time with me.
