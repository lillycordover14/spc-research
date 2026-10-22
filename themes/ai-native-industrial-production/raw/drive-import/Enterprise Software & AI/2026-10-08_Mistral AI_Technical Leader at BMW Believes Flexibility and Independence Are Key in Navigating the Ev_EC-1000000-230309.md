---
theme: "Enterprise Software & AI"
title: "Technical Leader at BMW Believes Flexibility and Independence Are Key in Navigating the Evolving LLM Landscape"
doc_id: EC-1000000-230309
source_line: "Mistral Ai · Expert Call · Customer · 08 Oct 26"
date: 2026-10-08
company: "Mistral AI"
pages: 2 of 2
saved: 2026-10-19T17:45:50.422Z
url: https://research.alpha-sense.com/search?search_id=tmp-dpwh5s830wf1fshuzdr6bp&sort=DATE&order=DESC&docid=EC-1000000-230309
---
# Technical Leader at BMW Believes Flexibility and Independence Are Key in Navigating the Evolving LLM Landscape

Company Deep-Dive

DATE PUBLISHED

08 Oct 2026

INTERVIEW DATE

10 Jul 2026

EXPERT PERSPECTIVE

Customer

ANALYST PERSPECTIVE

Business-Led

PRIMARY COMPANY

Mistral AI

SMART SUMMARY

Summary

The interview covers the company's approach to evaluating and deploying large language models for various business functions, the criteria for vendor selection, and the challenges and strategies related to cost, digital sovereignty, and vendor consolidation in the evolving LLM landscape.

EXPERT BACKGROUND

- Technical leader at a major German automotive manufacturer responsible for make-versus-buy decisions for software and infrastructure solutions, including enterprise architecture, cybersecurity, public cloud transformation, and data/AI platforms across North America, Europe, and Asia-Pacific (excluding China).

EXPERT SENTIMENT

- Believes that maintaining flexibility and independence from any single LLM vendor is crucial due to rapid innovation and changing market dynamics.
- Views cost control and digital sovereignty as critical, but recognizes the current limitations of European and Chinese alternatives compared to U.S. vendors.
- Predicts that the LLM vendor landscape will remain fragmented for a few years before consolidating to a few major players, similar to the cloud industry.

TAKEAWAYS

- The company began exploring LLM vendors as part of its public cloud transformation, initially through cloud providers, but now works directly with vendors like OpenAI, Anthropic, Cohere, and Mistral.
- Key AI use cases in production include hyper-personalized sales and after-sales offers, dynamic price management, AI-driven customer service, and self-writing code initiatives.
- Vendor selection is based on a detailed evaluation process prioritizing security, data privacy, cost, and digital sovereignty, with different LLMs chosen for specific use cases (e.g., Mistral for R&D, OpenAI for marketing/design, Anthropic for software development).
- European and Chinese LLM/cloud alternatives are being explored for sovereignty, but are currently less mature or trusted than U.S. options; Chinese models are only used in China due to trust and TCO concerns.
- The company aims to eventually abstract LLM choice from end users, allowing for easy switching between providers as needed, but currently manages multiple models due to uncertainty about future industry leaders.

AlphaSense Smart Summaries are AI Generated

Introduction and Expert Background

Catalyst for Exploring LLM Vendors

Vendor Selection and Use Cases

Evaluation Criteria and Regional Considerations

Vendor Comparisons and Ratings

EXPERT BIO

Founder and Chief Executive Officer at CuriousMinds Technology Advisory. Reporting to the Board of Directors, the expert is responsible for steering IT strategy and cloud transformation initiatives for enterprise clients. This includes leading cross-functional teams to modernize legacy infrastructure and overseeing the full Profit and Loss (P&L) responsibility for the advisory’s global operations.

Technical Leader at BMW Group. Reporting to the Chief Information Officer, the expert is responsible for defining the long-term technology roadmap and managing large-scale cloud migration projects across the Greater Munich Metropolitan Area.

The expert can speak to automotive IT infrastructure, enterprise-scale cloud architecture, and strategic digital transformation. Additionally, they are a customer of various SaaS management platforms and have implemented global DevOps frameworks and hybrid cloud solutions.

The expert is a current customer of Uptycs, Palo Alto Prisma Cloud, Mobileye, and Sysdig. The expert is a key decision-maker and evaluates software.

View More

INTERVIEW TRANSCRIPT

**Client** [00:00:00]
Thanks so much for this call. We're doing some research around LLM vendor landscape, where it seems that you and your firm have evaluated some of those companies such as Mistral, Anthropic, Cohere, OpenAI. Would love if you could just walk me through your background and your current responsibilities at your firm.

**Expert** [00:00:19]
Certainly. I am a technical leader at a leading German car manufacturer. In my role, together with my team, I'm responsible for make-versus-buy decision. That means whenever a business unit such as R&D, production, sales, and after sales needs a new software solution or infrastructure solution, my team decides what solution to buy and with whom to partner.

My department is divided into two groups. Enterprise architecture is one, and the second is cybersecurity. In enterprise architecture, we create a tool chain of the tools that we select and the partners that we partner with, whereas cybersecurity is responsible for IT, OT, and in-vehicle cybersecurity. Since 2021, I have an additional mandate of public cloud transformation, and since 2024, data and AI platforms. My region of responsibilities are North America, Europe, and Asia-Pacific. China has been removed out of my responsibility due to local regulations and local team setup. Happy to answer your questions, but these are my personal opinion and not the opinion of my organization.

---

**Client** [00:01:36]
Got it. If we spend time on the 2024 timeline when you started looking into data and AI, what catalyzed your organization to look for LLM vendors? What pain points were you trying to solve?

**Expert** [00:01:48]
In 2024, AI was not as hyped as it is today. The push or momentum towards AI was not there as it's today in 2024. In 2024, our primary touchpoint with AI partnerships was coming through cloud providers. Since 2021, we are trying to move our workloads away from data center into public cloud. As we did that, our partners from AWS, Microsoft Azure, Google Cloud, Ali Cloud in China, and Tencent Cloud in China, they started demonstrating or bringing their models on how they work with other providers like OpenAI and act as a middleman for us for using their large language models. This was our first use case that we started experimenting with.

Thereafter, based on several exchanges, my management realized the potential of customer interaction, how can we improve our customer interaction or how customers use our base today, followed by the demand for cost reduction because in a car company, we are facing massive headwinds in terms of cost. This was seen as an opportunity to improve efficiency, reduce cost, while trying to create better tailored offers for the customers. This is where the journey to AI started and experimentation with different players, with OpenAI, Anthropic. We also experimented with Cohere, and recently we partnered now with Mistral. We are experimenting and working closely with these providers, not via cloud providers any longer, but directly with them.

---

**Client** [00:03:26]
Got it. If you could just spend more time explaining why you decided to go directly with those vendors and in what forms, is it via public APIs, via on-prem services like with Mistral? Just trying to understand why you decided to go and have a direct relationship with those vendors instead of going via the cloud providers. How is that relationship? Is it mostly public via public APIs or on-prem, where you fine-tune with your own data?

**Expert** [00:03:55]
It is a combination. First of all, the idea was in 2024 that maybe large language model will be the differentiating factor. Why don't we create one of our own privately or we work with OpenAIs of this world to help us create one? Over the strategy planning over the next year, it became clear that large language model are changing so fast with DeepSeek and the others that came in that we might not be able to keep pace with it.

Our value-add in this whole discussion is the context and the data that we bring to the table, not the large language model. We created our architecture in a way that we remain large language model independent but we are able to plug in our data pipelines into any large language model and get the information. This is where the discussion started. We do not wish to push our data into a public large language model. That means if a customer asks which is the best car and the large language model says to the customer Mercedes is the best car, we don't want that to happen.

We started creating this large language model on our private instances. We first tried to do that over a private cloud. That means in our data center, with on-premise world we created, because we had enough GPUs and CPUs, we tried to run the models there, train the models there, but slowly and steadily, we have started using public cloud rooms, which are owned by us, and we own the intellectual property of the data there to run these models. We rejected the thought of creating our own large language model very early because the amount of capacity, investments, and GPUs that you need, we as a car company might not be able to compete with that.

---

**Client** [00:05:41]
Got it. Ballpark, how many use cases do you have in production? Two, what is the proportion in terms of vendors? Let's say we have 100 use cases in production. I'll say 30% with OpenAI, 40% with Mistral, 20% with DeepSeek.

**Expert** [00:06:02]
We have roughly 20-30 use cases in total, which are in the production. I would like to break it down to each use case so we understand. We are very active in sales and after sales, where we use a lot of AI. The primary use in sales and after sales for AI is to hyper-personalize the offering for a customer. We try to simulate and understand the purchasing history, driving history, taste of the customer to create an offer for sale and then eventually after sale to increase our footprint with them. This is currently active.

The second topic, which remains very active, is the price management. We have introduced a dynamic price management, which is AI-based. That means without human intervention, autonomously, we can decide the pricing of a used car and a new car at any given point of time without putting any human in the loop here. What that means is if similar brands like Mercedes-Benz, Rolls-Royce, Volkswagen, Ford, in the same class segment of a vehicle are selling a car in a certain price, we want to compete against it. This is something which we have set with AI. What we're also doing is selling a lot of cars in used car business with AI, deciding real-time whether this car should go into a wholesale auction or into a retail channel with a dealer. In the past, all these activities was done by a human, which we have taken over.

What is a very strong push in my organization is customer service with AI. Agentforce from Salesforce, we have integrated into our platforms to help guide the customer, create the best offer. Last but not least, we're also immensely active in self-writing code. Our vision is that at end of 2028, we should be in a position that 30% of the junior developers that we buy from Accenture, Capgemini, and all the third-party providers are self-writing code with copilot, should be at a maturity level that we don't need to do that. That's the business case behind the self-writing code. Very high level, these are the AI use cases. I'll be happy to deep dive into any that you wish to know more about.

---

**Client** [00:08:18]
Got it. As you think of those different use cases, how do you pick which vendor should do mainly the hyper-personalization? What is the selection process there? Who's involved? Do you have a centralized team, or each use cases have their own team that just tests and have their own.

**Expert** [00:08:37]
Do you mean how we select a provider or how we decide which large language model to use?

---

**Client** [00:08:43]
Yes, exactly. Out of the 20-30, do you start like, "Okay, we're going to use one vendor," or you just test them on a recurring basis and then you select?

**Expert** [00:08:53]
When we select a new vendor, we have a very detailed evaluation process. That is to make sure that the security, cybersecurity, data privacy guidelines are managed. Once they are selected, let's say OpenAI, Claude, and Mistral are selected, we want to offer our developers, our teams the flexibility of using any one of them.

The teams decide based on the use case. For example, Mistral is for us a tool of choice for engineering R&D crash simulation use cases. All the crash simulation and simulation regulatory use cases run on our product from Mistral in the future, whereas OpenAI is considered a very strong tool for topics related to design. Whenever we need to have a marketing slides design of images, we use OpenAI product portfolio on our website. All the cars you've seen on our websites, marketing, I would say, is the right word, is OpenAI, whereas Anthropic is becoming very strong in the self-writing code, software development pipelines, how developers can perform an activity. Not a front-end usage but something behind the scenes how the software is being developed.

The point I'm trying to make is that our ambition is to create a platform where the users are agnostic to which large language model is running. Today, they can clearly see whether they want OpenAI and Anthropic. In the future, we want to create a black box that the end user or developer does not know what is running and where is the data being trained on. Going forward, that's the ambition, but today we don't have that luxury. Today the developer knows that he's using OpenAI or not. In the future, we should have the possibility of plugging away someone if the price increases or getting new provider in if they are bringing some better solution.

---

**Client** [00:10:49]
Got it. When you evaluate these different vendors, is cost an important factor and, let's call it, European sovereignty as well?

**Expert** [00:10:57]
Cost and data sovereignty, I think these are the two points you mentioned.

---

**Client** [00:11:01]
Yes.

**Expert** [00:11:03]
Definitely as a car company struggling for free cash flow, cost is a reason. We try to evaluate every use case going in with a very clear business case and an ROI plan. The problem with the AI story today is that the costs are high, but the ROI is uncertain and is sometimes long term in the future. We try to quantify it right away.

The second topic, what we actively do is with respect to digital sovereignty. This topic became much more important after Trump administration tariffs came into the picture. Before that, this was a topic but not much focus. Since Trump administration started putting tariffs on automotive industry, we want to create an alternative solution where we are independent of the American hyperscalers and the large language models. We have started an initiative together where we are working with local players. Mistral is one of the examples, but at the same time, also cloud providers. STACKIT from the Schwarz Group in Germany is one example. They have come up with their own cloud. IONOS, OVH, there are multiple cloud providers.

I must say these cloud providers are not that mature or not that far in terms of how we would like a cloud provider to work in comparison to AWS, Azure, or Google. Last but not least, we are working with them, but I do not see in near future we will be moving to them because they need another year or so to get mature. Digital sovereignty is important, but the alternatives are very limited in terms of cloud. In terms of AI and large language model, Mistral is the only strong option, but that is currently very limited to R&D-related use cases.

---

**Client** [00:12:56]
Got it. Is it because the U.S. vendors like Anthropic and OpenAI are just so far ahead in terms of quality in other use cases that you only limit Mistral to the R&D use cases?

**Expert** [00:13:07]
Yes. Mistral is currently limited because we do not want to put all our eggs in one basket. Simulation is something which is considered high-volume AI. That means you can predict in advance how much GPU you need. This is something custom-made for a new large language model provider. Once we know that it is capable of doing more, there are many use cases that we would like to shift left to them.

---

**Client** [00:13:34]
Going back to your point, with cost, we're seeing more and more AI-native start-ups leveraging Chinese open-source models. Is this something that you feel enterprises in Europe that are big like yourself will start using, or is it more AI-natives?

**Expert** [00:13:48]
Did you say Chinese open-source models?

---

**Client** [00:13:52]
Yes. Exactly, with open weights that you can download and have on-prem.

**Expert** [00:13:58]
Thing is that we are reviewing these models but only for our China strategy. What we have done is that with China, we have a local-to-local strategy. We partner with Tencent, with Baidu, with Ali Cloud there, and also with the local AI partners, but we do not plan to use this here. We do not plan to use these use cases here.

---

**Client** [00:14:20]
What is the rationale, given that it's open weights and you can have it on-prem? Is it more legal and compliance? Is it more something quite subjective of "We do not want to use China as well"? Would love to understand that.

**Expert** [00:14:34]
There are a couple of factors. The first factor is the trust factor. Since we moved out a lot of Huawei and other IT equipment in the past, the trust factor with the Chinese offering is very limited in Europe. Second factor is if we have an open-source on-prem based system, then my TCO is very high. I need to maintain the open-source model. I need to operate the hardware on which it runs and pay for it. As a car company, I'm trying to increase my free cash flow and bring down my capital expenditure, so that goes against that direction.

Trust factor, acceptance in Europe, and plugging in your intellectual property data into a Chinese ecosystem, this is something I rely only in China. In China, I'll be happy to experiment with it, but I doubt that in North America and in Europe, we will do that.

---

**Client** [00:15:28]
Got it. When it comes to U.S. vendors, do you think it's just a transition period due to the Trump administration, and if they were to revert back, you might change your strategy, or is it now irrespective of what's going to happen in the U.S., "We want to rely more on European technology"?

**Expert** [00:15:46]
This is a very geopolitical topic. I think the focus is more on a European footprint, although it's very limited. We have two options, either we completely move out of American ecosystem or we wait until the Trump administration change. Both needs time. My personal view is that we will continue to work with the American ecosystem while investing on the European ecosystem so that we have a fallback in place. Right now, there's no fallback. Chinese ecosystem integration, I just do not see that as a possibility.

---

**Client** [00:16:20]
Got it. I would love if you could just walk me through the pros and cons of the different LLM vendors that you are currently using. What is good about OpenAI, Anthropic, Mistral? Maybe you can start with a score from 1-10, with 10 being the max, the best, and zero the least, and then you just explain why you give that score.

**Expert** [00:16:41]
You want me to rate Anthropic on a scale of 1-10?

---

**Client** [00:16:46]
Exactly, and explain why you give that ranking, and then you can do the same with OpenAI and Mistral.

**Expert** [00:16:52]
I would say Anthropic is a nine. They have a very clear strategy what they want to do. The speed of innovation since last November with Anthropic is very high that I sometimes worry that they oversell. For example, this Mythos came in right now. They create a lot of frenzy, which I sometimes believe is marketing. That we have to be careful about, but as a product, it's very stable.

---

**Client** [00:17:19]
Yeah. OpenAI?

**Expert** [00:17:21]
OpenAI is 8/10. It's also a solid product, but if I look at the technical advances in R&D which Claude and Anthropic has put in versus what has the OpenAI, definitely I have to give them an eight because they're not as far in terms of R&D as Anthropic is. That's why I give them one point less.

---

**Client** [00:17:41]
Got it. Mistral?

**Expert** [00:17:43]
Mistral is a seven. It's a solid product, but it's a relatively new product. It has a lot of advantages. It's a European product, it's better integration, but it's too early to say that it's at a point that it can compete with Anthropics of this world. If I see Mistral, I see potential and promise, but it is not working at a scale which OpenAI and Anthropic is working. These products, they stop performing at scale, not at individual setups.

---

**Client** [00:18:14]
Got it. Have you tried Cohere? You mentioned the Schwarz Group. I would love to understand if it's something that you have tried.

**Expert** [00:18:23]
Yes, we tried Cohere as a product actively. The thing is that it is very popular in terms of integrating or creating RAG-based models, retrieval-augmented model. We experimented with how we can have a private deployment, an on-premise, or our sovereign cloud, so to speak, and how we can integrate it into our ecosystem.

As a product, we were happy with it. It works well. Our primary use case around Cohere was to create enterprise search. In a large company with over 100 years of history, we have knowledge spread across your Confluence, your different Word documents, and how to bring everything together was our target. This is why we had this ambition of using Cohere, but we slowly gave it up because our partnership with Anthropic was becoming very stronger, and they also had similar offerings, so we decided to bundle it.

---

**Client** [00:19:20]
Got it. The point of bundle, do you see yourself consolidating on fewer models like you just did with Anthropic and then not use Cohere, or do you believe that it's going to be more fragmented, and then you just have this routing that you spoke before, where based on use cases, you just have 10 different models?

**Expert** [00:19:37]
It happens, as a matter of fact, that we would like to have less models because the cost of managing the model is also a cost. The problem that we have is that we do not know today which model could be the industry leader next, and we don't want to be left behind. I'd hesitate to say that we will go and really reduce the number of large language model right away, but I am afraid we cannot invest that much in multiple providers. I don't know today who is the industry leader, and we don't want to miss out on the bus. That's the problem.

---

**Client** [00:20:11]
Got it. You mentioned Mythos here. How important is it for you to use the latest and greatest models? Is it just a branding, or is it more cost or something else which is more important? How important is it for you to have access to the latest and greatest models?

**Expert** [00:20:31]
That's very important. No one is going to visit the website of my company to buy a car in the future. Everyone is going to ask a chatbot that "I want to buy this car. Which car is the best?" I want the latest large language model to guide the customer to us. From that point of view, it has to be a setup wherein we would be in a position to have the regular access to any upgrades, any new technologies, not that we are left behind with any provider which has old large language model and does not provide the right information.

---

**Client** [00:21:04]
Maybe last question on my end. In your opinion, what does the frontier lab landscape look like in the long term? Do you see OpenAI, Anthropic still being ahead, or do you see it much more fragmented with different modalities, like in image generation like Black Forest Labs, they're doing that with voice, Mistral? Sovereignty, how do you see this.

**Expert** [00:21:27]
I believe this will remain fragmented for the next two to three years, and then there will be a vendor consolidation amongst them. Large language model is a very expensive business to operate, especially with your high GPU cost, and none of them are making profit right now, so eventually, what they will do is they will start to do IPOs, they will start becoming more open. Eventually, they will be cannibalizing each other, and there'll be two or three providers, exactly what happened in cloud industry. There were many small cloud providers or infrastructure providers, and now they're only top three. I believe it will remain fragmented for the next couple of years based on who has the maximum customer base and is able to drive these topics at economy of scale, and then we will see a bit more consolidation.

---

**Client** [00:22:17]
Got it. Maybe last question, are there any other questions or topics that I haven't asked that you think should be interesting for you to mention?

**Expert** [00:22:26]
No, I think we talked about cybersecurity. One important factor is that if any of these providers have a cybersecurity attack, those providers will definitely go down the rank because if they lose the data, then their game is over. They have to be very strong in terms of their cybersecurity and how they store their data. Apart from that, I think we spoke about everything.

---

**Client** [00:22:49]
That was really helpful. Thank you so much for taking the time for this call.
