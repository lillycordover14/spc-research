---
theme: "Enterprise Software & AI"
title: "Machine Learning and Engineering Manager at DoorDash Inc Sees Potential in Applied Compute for Cost-Effective AI Infrastructure"
doc_id: EC-1000000-234437
source_line: "Applied Compute · Expert Call · Customer · 20 Oct 26"
date: 2026-10-20
company: "Applied Compute"
pages: 2 of 2
saved: 2026-10-21T15:39:24.631Z
url: https://research.alpha-sense.com/search?search_id=tmp-ffzr3ttvkmfy1lpfztggun&sort=DATE&order=DESC&docid=EC-1000000-234437
---
# Machine Learning and Engineering Manager at DoorDash Inc Sees Potential in Applied Compute for Cost-Effective AI Infrastructure

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

Applied Compute

SMART SUMMARY

Summary

The conversation covers the expert's team's use of LLMs and reinforcement learning for large-scale personalized recommendations, their collaboration with Applied Compute for fine-tuning and evaluation, and the operational and cost considerations driving their AI infrastructure decisions.

EXPERT BACKGROUND

- Machine Learning and Engineering Manager with experience leading teams focused on recommendation systems, personalization, and large language model (LLM) applications, including prior experience at a major social media company managing similar recommendation and ranking systems.

EXPERT SENTIMENT

- The expert is cautiously optimistic about the collaboration with Applied Compute, noting promising results but emphasizing the need for further evaluation and real-world impact before committing to a longer-term partnership.
- The expert values both the technical capabilities and the level of engineering support provided by vendors, with a preference for platforms that can offer end-to-end solutions and efficient resource management.
- Cost reduction and improved performance are key drivers for adopting new AI infrastructure, but the expert remains conservative about future vendor relationships due to the fast-evolving nature of the field.

TAKEAWAYS

- The team initially used commercial LLM providers (OpenAI, Google) but faced challenges with cost, orchestration, and scalability, prompting a shift toward open-source models and in-house fine-tuning.
- Applied Compute is used primarily for fine-tuning LLMs and evaluation, with a recent contract incentivizing the team to explore using Applied Compute for inference as well.
- The collaboration with Applied Compute involves both direct engineering support and onboarding internal machine learning engineers to their platform, with a focus on reinforcement learning and evaluation automation.
- The team has achieved significant cost savings (5-6x cheaper) compared to previous commercial LLM solutions, with the potential for further improvements in performance and latency.
- A unified platform for both training and inference is highly desirable for operational efficiency, faster updates, and scalability, but Applied Compute's inference offering is currently less mature than its training and evaluation capabilities.

AlphaSense Smart Summaries are AI Generated

Introduction and Expert Background

Merchant Team Use Cases

Applied Compute Collaboration Details

Evaluation and Contractual Agreements

Fine-Tuning and Training Platforms

EXPERT BIO

Machine Learning and Engineering Manager at DoorDash Inc, customer of Applied Compute. Expert can speak to the evaluation and implementation of advanced AI/ML tools and their impact on engineering productivity, aligning with the project's focus on technical capabilities and business outcomes.

Machine Learning and Engineering Manager at Doordash. The expert owns the entire DoorDash homepage and oversees two teams. They can speak to transformers, different LLMs, and how AI tools like OpenAI make the day-to-day work more productive. The expert is also responsible for the Instagram reels recommendation system.

Former Senior Manager, Data Science at Meta, leaving in 2025. The expert started as a Manager, Data Science, and moved to the Senior Manager position at Meta.

View More

INTERVIEW TRANSCRIPT

**Client** [00:00:00]
Thanks for taking the time to chat. Just some super brief context on our end, we have been looking really closely at the AI infrastructure and agent infrastructure market, and particularly on some of these new RL-as-a-service and reinforcement learning infrastructure companies, and in particular, Applied Compute, which I understand you work with closely and know their work closely. Maybe as a quick background, if you can share a little more about your background with us, and how you got here, if that sounds good?

**Expert** [00:00:29]
Yeah. Basically, I'm in DoorDash. My team owns the home page recommendations. If you open DoorDash app, you see lots of carousels, which are horizontally scrollable collections of restaurants. We use LLM GenAI technology to generate those horizontal carousels. We do ranking, we do personalization. This is how Applied Compute and other fine-tuned LLM and also reinforcement learning, human-in-the-loop, auto-prompt tuning, those subjects come to the picture. We want to generate personalized, relevant recommendations for the user. We want to generate at scale. We want to make it personalized. We want to make it scalable, and traditional human annotation type of thing doesn't work. It doesn't personalize, and it's not scalable. We use LLM to do those things.

How the reinforcement learning comes into play is we want to really own our own fine-tuned LLM rather than just call Google, OpenAI, or Anthropic to use those commercial language models. We want to fine-tune open-source model so that we spend less. We can have our own in-house LLM to power all those services.

Before that, I was in Meta for more than five years. My team owned roughly similar things. We have the horizontal recommendation system for Instagram Reels, Facebook Reels, as well as some advertisement, as well as ranking. That's pretty much about me. Before, I was in a few other companies, doing recommendation, search, natural language processing type of thing.

---

**Client** [00:02:14]
Makes a lot of sense. I know Applied Compute did a case study with DoorDash a few months ago on this merchant onboarding use case. That's a different team from what you do.

**Expert** [00:02:26]
That's a different team, our sister team basically. That team is more of the merchandising or the merchant team. They work with all different restaurants, different grocery stores, all the retailer stores, all those types of things. They use LLM to do summarization, to do some merchant profiling so that we have more natural text format understanding descriptions about the merchant. We also have that team build different types on the restaurant. What's the cuisine type, whether it's vegan, vegetarian, or just regular, and whether it's spicy, sweet, portion of the dish, all those types of things?

Also, they look at the reviews from the user to give also the defect rate because sometimes the restaurant will decline the order. They don't deliver, and they look at all those things to give a holistic view for the restaurant. We take those as our input so that we can recommend relevant, as well as high-quality restaurants, to the users.

---

**Client** [00:03:28]
Makes a lot of sense. Can you elaborate specifically? We know your sister team uses Applied Compute. Can you break down for us what use cases you guys use Applied Compute and even in general use agents and fine-tuned agents or post-trained agents for?

**Expert** [00:03:45]
Totally. Let me talk about Applied Compute collaboration. We are in the collaboration with Applied Compute right now. The journey is this. Initially, we want to use LLM to generate recommendations for all the users. We first use OpenAI. We use ChatGPT. We need to do lots of coordination, orchestration of the pipelines so that we can run the generation of recommendations, the restaurant carousel for, say, 30 million users. We have more than 30 million users. We only generate for 30 million users. We need to coordinate. We need to submit our jobs and then download our jobs. That's all within certain SLAs.

It's still very tedious, and sometimes there will be faults. Probably some batch job gets declined by OpenAI silently, and then we don't know. When we download data, we have zero data. We need to resubmit. We need to do all those things. Also, it's very expensive. Their model sometimes just gets deprecated, like o3-mini, o4. All those things, there are just lots of coordination, orchestration. We definitely compare when we think about our collaborators or which one we use. We definitely consider the price as well, which is very important.

We switched to Google because they give us a little bit more discount. Also, they allow a larger batch size, which is very important. We want to submit as much as possible in one submission so that we don't have to keep monitoring. We don't want to submit, say, 1,000 jobs today, and then we need to monitor, and then we submit 1,000 jobs tomorrow. That will be very tedious, not best use of time. For Google, we can submit a lot more, probably 10X more than OpenAI, although their SLA is also longer. Still, we manage that. We make the work through. We get recommendation.

With all those things, at the beginning, we need to have evaluation for sure. We need to have human evaluation at the first place. When we have enough human evaluation results, we do our own prompt fine-tuning. We do our LLM as a jury. We have programmatic metrics to interpret the results, quantitatively measure each iteration performance.

Still, because we have lots of users, we need to generate a lot of content. Also, with LLMs, you need to think about the thinking tokens. In general, people feel if you have more thinking tokens, you have more inference capability, then your results will be better. We actually did some study or just small thought example. Even just say hello, if you set unlimited thinking tokens, Gemini will spend maybe 1,000 tokens or 2,000 tokens to just reply hello, "Hello, how are you?" type of thing. That doesn't make sense. That costs a lot because those thinking tokens are considered to be all true tokens. That basically has a higher cost.

Also, the evaluation, we want to improve as well. We want to have a better loop to improve our generation prompt, evaluation prompts altogether. Given all of this, we think about, "Let's try open-source, open-weight models." Qwen is one. Right now, it's GLM-5.2. That is another, and also Kimi, all those open-source models. We do some benchmarking. We do some evaluation. Things are pretty good because we have the full control roughly.

Given also the successful collaboration between Applied Compute and our sister team of merchant team, we feel like we should really leverage Applied Compute as an extended team for us, basically. They're also very proactive as well. They talk with a couple of teams in DoorDash. They know which team is working on GenAI-related stuff, which team needs the help for evaluation, for training, fine-tuning. They can set up those things. They have contracts with DoorDash as well. We have a couple of meetings. We give them what we did, walk through all the steps and where we need the most help.

Also, we basically asked what they can offer in addition to what we have already done. We already do a few fine-tuning work, we use Tinker. Our serving or the inference part, we use Modal. We talked with them. They told us that they specifically have expertise on evaluation. They have reinforcement learning technology. It's called OPSD. They have their in-house fine-tuned version of OPSD, which has been proved by a couple use cases as their examples for effectiveness.

We just work together, and we basically hand over the evaluation part, the reinforcement learning implementation, and also some setup of the fine-tuning training part for them. They work on those things. Eventually, for the inference side, they still use Modal, but they help us to optimize the entire end-to-end process. That's basically how we really work with them.

Right now, the scale is same. We can generate 30 million users, and our target is to generate 50 million users recommendations. Also, the time frame to generate those 50 million users will be within a week. It has multiple steps. It has generation step. After generation, we need to do some moderation to make sure the carousel concept or the title makes sense. We need to generate the embedding for the text format, carousel title, so that we can do embedding-based retrieval. Basically, the entire process, our target is a week.

---

**Client** [00:09:57]
Makes a lot of sense. Just to clarify, the merchants team basically had Applied Compute, and that was probably pushed down from Andy, the CTO. After that, you guys heard about them on the commercial side, on the carousel side, and wanted to basically try them out to assist on your fine-tuning use case. Is my understanding correct there?

**Expert** [00:10:17]
Yes. We do lots of due diligence from our side. Still, we need to pay them. Although, we don't pay out of our team's budget. Our CTO, Andy Fang, he needs to pay. We want to use the best out of Applied Compute for our purpose. We have lots of discussions. We basically discussed pretty deep about their technologies and what they can offer to us incrementally.

---

**Client** [00:10:45]
When did you do this evaluation?

**Expert** [00:10:47]
It's pretty recent. I think last month. Early, I think mid-June.

---

**Client** [00:10:55]
Makes a lot of sense. You mentioned you used Modal for inference, and you're experimenting with some of these open-source models. You use Tinker as your infra solution to do the RL. What exactly do you use or were you using Applied Compute for? Did you try them alongside any other vendors or evaluate them across other vendors, or did you just decide to work with them? What exact use case are they doing there?

**Expert** [00:11:22]
Sure. Just making it super clear, we use Tinker to do the fine-tuning training part because we don't have much budget with Tinker. I think it's very interesting that for Tinker, the collaboration is very preliminary in some sense. It's basically from Andy's company credit card. He charged his credit card account to a couple of engineer teams, and then we can put charge of Tinker on that credit card. There's a limit, and we can't spend over that limit, which is pretty small.

With fine-tuning part, we don't need that much tokens, examples. We try, for example, 100 samples, 200 samples, 1,000 samples, 2,000 samples, 5,000 samples. We compare our evaluation criteria, and then we find that 1,000 examples are actually already enough for feature learning type of thing. That's how we train our fine-tuned LLM, and that is on Tinker.

However, when we do really large-scale inference, that is on Modal because we have our internal infrastructure to support Modal. We also have a better, more solid support for Modal. Also, the entire company right now, we evaluate. Basically, we compare Tinker and Applied Compute for the training part. For the inference part, we just started working with Applied Compute to understand how they can help us to do inference part as well. Because this is the initial step, the entire company still moves to Modal as the LLM inference platform.

For other platforms, I don't think we really have much comparison. I think initially, we used Fireworks to do some GPU inference, and we have Parquet to do LLM type of inference. All those things will be phased out, and then Modal is the current platform for us to do inference. Applied Compute is basically the platform for our fine-tuned LLM purpose.

---

**Client** [00:13:19]
Very cool. You started off with Tinker initially on the credit card, but then as you productionized, you moved to Applied Compute to own the training platform. Now, you're evaluating using them as well for the inference platform. Is my understanding correct?

**Expert** [00:13:33]
Yes, exactly.

---

**Client** [00:13:36]
What would convince you to move off of Modal onto Applied Compute? What would you need to see?

**Expert** [00:13:42]
To be very transparent, we have a contract with Applied Compute as a lump sum until 2027, until May next year, which means we already bought a lump sum from Applied Compute. We definitely need to use them.

---

**Client** [00:13:55]
That lump sum comes with compute?

**Expert** [00:13:58]
Exactly. We definitely need to think about how we can best utilize those resources. That's why, in addition to training, we want to explore whether they can help for inference as well. Also, another consideration is we always want to just have the pipeline run on one platform. That's much easier to maintain. We don't want to submit a job, some of them through Databricks, some of them through Parquet. We have internal Metaflow. It's just a little bit hard to manage.

If something can be run end-to-end with one platform, and that one platform offers a good performance, additional capability, especially for the reinforcement learning part, for our evaluation, so that we can make our evaluation more at scale, also we can improve our prompt, find the common cases, the nuanced examples, that will be very helpful to make this a whole LLM evaluation as a closed loop rather than open loop. That's another reason.

Another thing is, at least as of now, the evaluation work, we feel it's reasonable. It's better, although not significantly better than our previous work, but it's pretty promising. Given that, we definitely have some trust on their capability. That's why we want to see whether the inference part can be on that platform as well, that kind of thing.

Also, another point is when I say we want to leverage Applied Compute for inference, maybe in the future, it's that they could also manage our compute. The inference part is already pretty easy. Once you have LLM there, you just submit your prompt. Many work is on the prompt tuning and also what you put in the prompt, and also how you really evaluate your result. If they can better or more efficiently manage our compute, that's also a win for us. Even without performance improvement, even a better management of compute resource, that's also a win for us.

---

**Client** [00:15:56]
Earlier in the call, you mentioned how you started off with Applied Compute's training platform. Could you provide some more context on what the platform actually is or what it is that you're using from them?

**Expert** [00:16:08]
Yeah. Basically, we use them for the fine-tuned LLM. They have the integrated UI for us. We do both ways. One way is we just hand the data to them. We give them 100,000 anonymized users, all the history within the last year and then they can do whatever they want. That's one way we did. Another way is that they onboard my MLEs to use their integrated UI to do the fine-tuning part. That's that.

We also leverage the platform to automatically do the evaluation. When we have the result, we have the human annotation as well. How do we evaluate our result? Many cases, our distribution of our categories or classes will be very biased, very skewed. We leverage the platform to come up with more statistically sound metrics to come to a conclusion.

---

**Client** [00:17:05]
Did you say that they staffed nine people for you, or did I mishear that?

**Expert** [00:17:10]
No, they onboard my MLEs on their platform. They're basically consider to be our extended team. I don't say nine people. They gave us about two to three engineers to work on their own with our data, as well as onboard my MLEs to use their technology, their platform.

---

**Client** [00:17:31]
Okay. It was nine DoorDash MLEs and two to three engineers from Applied Compute's end?

**Expert** [00:17:38]
Roughly, yeah.

---

**Client** [00:17:40]
Okay. I understand that you had this contract with DoorDash in place, which was why your team was looking for use cases on which to use up the credit.

**Expert** [00:17:50]
Exactly, that's one reason.

---

**Client** [00:17:53]
Right. I saw that DoorDash had acquired a team called Metis, which I think does something very similar. Was there a reason why you didn't take this use case to them?

**Expert** [00:18:02]
Yeah, that's a good one. Basically, I don't have the full context because I'm not in the acquisition function or I'm not involved in that, for sure. At least based on my visibility and my connections, discussions with both teams, my understanding is Metis also works with Applied Compute a lot, probably even before the acquisition. Actually, our connection was partially introduced by the Metis CEO or CTO. That's how we worked with Applied Compute and also how Metis was involved.

Right now, I'm not sure. I'm guessing. When we think about fine-tuned LLM at the first time, actually, Metis people reached out to us, whether they can help us to significantly reduce our cost on LLM. Because we already started our fine-tuning work, we have some estimate about how much we will spend with fine-tuned LLM to generate all the recommendations. We gave that number to Metis people. They basically later decided, "Oh, we already squeezed lots of juice for the cost reduction," and it's probably not the best place for them to invest.

Recently, our company had another initiative, also led by our CTO, to further reduce our LLM cost. Because of this, the Metis, I think he's CTO or CEO, I don't remember his title, but that engineer told us, "Oh, there's an Applied Compute which did some good work. They have probably better management or better strategy to further reduce our cost. Also, because of this contract with DoorDash, we can leverage their resources." That's one partial connection. The other connection is through our partner team, merchant team. The merchant team has a successful collaboration or use case with Applied Compute. Based on those two pieces of evidence, we started talking with Applied Compute to make our collaboration happen.

---

**Client** [00:19:59]
Makes a lot of sense. Given all your AI initiatives and the new work with Metis, do you foresee churning off of Applied Compute at some point, or are you quite happy with the work they're doing today?

**Expert** [00:20:10]
I want to be honest. I think the direction and the work is promising, and we still need to further evaluate, that's for sure. Our contract is last year May. Whether to extend that and how much we want to extend and how much budget we want to spend there, it definitely will be based on the performance, efficiency, and their involvement. Right now, they have really active involvement for our work, but you never know what's going to be the future.

One example was the Fireworks. Actually, my team was working with Fireworks before, and the initial collaboration was very good as well. We basically talked with their principal engineers at a regular basis. They dove into our code base and also their code base to really make the library compatible, to add necessary functions, to do all the fields to function, activation function, and the transformation together.

Later, probably after half a year or maybe seven, eight months, Fireworks just built more collaborations. They have more use cases. They basically have very, very little involvement with us. That's why we stopped the collaboration with Fireworks. You never know what's going to be the trajectory for another company. I just want to be conservative here. Right now, it's pretty promising. Hopefully, we are still at the peak use case for them, and then they can invite more engineers to our work, and then we can see some better results.

---

**Client** [00:21:43]
Is the main driving factor really just how many engineers they're willing to staff to you and how much time and energy from their engineers they're willing to spend with you?

**Expert** [00:21:52]
I would say that's probably 60%-65%. Another 40% is still the technology. At least in my team, we are more like modeling engineers. We have some experience in reinforcement learning and also the reinforcement learning fine-tuning type of work. However, that area really evolves fast, and we don't really have the bandwidth to catch up the advanced technology. Also, recommendation side is naturally a complex area. The search space is huge. The actions are very, very diverse. The technology part is definitely one important factor we consider.

That's why when previously I was asked, "Do I foresee more collaborations or deeper collaborations or longer collaborations?" I was conservative because offline result is offline. We need to see online results. We need to make sure that online, we deliver more impact, we deliver better performance. That's under experimentation right now. We need to see that experimental result so we know whether Applied Compute, their reinforcement learning technology, works for our use cases.

If that works, definitely we want to go deeper. We want to take the wave of all the advancement in reinforcement learning work to make our recommendation more personalized, scalable, low latency, or even in real time. That's our ultimate goal, how we can make our recommendation real time. That's the ultimate goal with all the fine-tune online.

---

**Client** [00:23:28]
Just wondering, do you have visibility into how the merchant onboarding project went with Applied Compute? You mentioned it earlier as well as being semi-successful. That one is online, I presume, or do you have any visibility if it's online or what's the status and how that's going? It's a more simple use case as well.

**Expert** [00:23:48]
First, I will be a little biased because my team owns the hom page, so we are basically to the user end, and that team is more to the merchant end. That team is more considered to be a little bit back-end or foundational type of thing. Their impact is not really that evident from online perspective. When we have better merchant understanding, it's a little bit long chain to show the impact for the user side. Because of that, in my personal opinion, it's not really online, although they say it's online.

---

**Client** [00:24:20]
It is in production, is what I meant to say.

**Expert** [00:24:23]
Yeah, it's in production, that's for sure. It has been used, but the use is limited, I would say. It's limited. We also have our own merchant understanding, all the restaurant understanding as well. Their data, their knowledge is part of our entire feature space or our entire knowledge base. It's not the most widely used technology or knowledge base, but it's part. It's in production for sure.

How that was initiated, I basically talked with the engineer working on that because we had collaboration with them previously. Initially, my team also owns the restaurant understanding, and then we gave that ownership to them. I think initially, based on all the conversations, we asked, "Try to compute a little bit as well."

At that time, DoorDash probably was in the process of acquiring Metis, the evaluation AI company. Definitely, our CTO, he usually has interactions or collaborations work with couple of start-ups. That's his style. He always works with some start-ups with the mind of work and then buy. Applied Compute was one in that case as well.

Basically, Applied Compute was like other vendors of LLM or this reinforcement learning or maybe this compute resource platform. They reached out to a couple of engineer teams. The merchant team was the most ready team in some sense. It's very natural to use LLM capability to understand the restaurant because it's just lots of text information. There are also dish or image there. It's very natural to use LLM. That team was the most-ready team to onboard for this Applied Compute type of paradigm.

Also, that team is also evaluation-heavy. They need to make sure any description about the restaurant makes sense. It should be factual. It shouldn't be any brand there. It shouldn't be any missing information or some integrity issues. One side, they are ready. The other side, they also need advanced technology to speed up their knowledge base building. That's how they initially work together.

Another factor was that team was a little bit far from the actual consumer. The impact of that, if there's a bad impact, that has less risk because we have multiple layers after that to filter the bad content, all the issues. That's another reason why that team was the first to work with Applied Compute. That's the other thing.

---

**Client** [00:26:58]
Yeah. On your team, you mentioned that it's offline in the RL sense, but are any of the models that Applied Compute helped you fine-tune in production yet, or that evaluation is still ongoing?

**Expert** [00:27:10]
That's what I said. Basically, they help us to fine-tune Qwen and the parameter. It's not a small one. It's the medium big one.

---

**Client** [00:27:21]
You're saying that model is already in production? The continuous learning RL online just isn't in production yet. It's still offline.

**Expert** [00:27:32]
No. The production definition is this. Basically, we use that fine-tuned LLM to generate the recommendation. That generation process is offline because right now we can't serve the fine-tuned LLM online in real time. That's why it's the ultimate goal. Right now, all the generation is still offline, but the generation result has been pushed online for testing, and we want to see better performance of this generation compared to Gemini 1.5 Pro.

---

**Client** [00:28:04]
What are the initial results showing you on the models fine-tuned from Applied Compute?

**Expert** [00:28:09]
The fine-tuned model, like I said, we have human evaluation, we have LLM as a jury, we have programmatic quantitative metrics. This fine-tuned LLM shows better results for a couple of dimensions, not all, but a couple of dimensions. We have some good confidence on the performance, and that's why we are experimenting this version.

We have some metrics to evaluate relevance, diversity, factual, and information prioritization, all different dimensions. Also, we have the LLM as a jury to evaluate whether the recommendation meets users' dietary preference. We cannot give meat to vegan. For example, if someone wants to eat chicken wings, but they are vegetarian or vegan, then we need to find the cauliflower alternative for chicken wings, which probably have the same flavor, but it's not meat. That's all the different evaluations.

---

**Client** [00:29:06]
Makes a lot of sense. The lump sum contract that you have with them, that basically covers the compute for this training. In theory, all the excess compute, you can use it for whatever you want. You can use it for inference. You can use it for continual post-training, whatever you want.

**Expert** [00:29:26]
Exactly. That's why we want to use part for inference as well. We don't want to waste the compute. The training part is not much expensive. The inference part is pretty expensive.

---

**Client** [00:29:42]
Yeah. Can we ask, approximately, high level, how big this lump sum contract is?

**Expert** [00:29:49]
Yeah. Let me give you the rough estimate. Our job costs, for 50 million users, we need to spend under $100,000-$150,000. That's for 50 million users. We need to generate this scale roughly monthly. Basically, early this month was the first generation, and we need to generate July, August, September. Probably, we need to generate eight times because we don't generate anything new for Christmas, for the holiday season. That's risky. You look at probably about a seven figure budget if we generate until May next year.

---

**Client** [00:30:29]
Makes a lot of sense. Around $100,000, $150,000 a month in inference is the high level. Post-training, I assume, is smaller than that.

**Expert** [00:30:40]
Yeah, that's not a big chunk. That's probably maybe $10,000 at most. That's definitely pretty small. We don't need that much sample.

---

**Client** [00:30:51]
How do you think about the value of this, or the ROI? Is it worth the $100,000-$150,000 you're spending? How do you think about that?

**Expert** [00:31:02]
If we can really deliver better business impact, basically more orders, more conversions, this will be much, much better. Previously, our spending on Gemini, the budget will be around $20 million or $15 million.

---

**Client** [00:31:18]
A year?

**Expert** [00:31:21]
A year, yeah, so roughly the same time range.

---

**Client** [00:31:24]
10X cheaper?

**Expert** [00:31:26]
Ten is probably a little bit aggressive, at least 5X, 6X cheaper. It's much cheaper.

---

**Client** [00:31:33]
And hopefully better? The results will hopefully be more accurate as well and better latency.

**Expert** [00:31:41]
Yeah. Even 1X better, and in the future, it's all the same, still it's a good win. It's still pretty good.

---

**Client** [00:31:50]
Makes a lot of sense. Just going back to the competitive dynamic side, you mentioned Tinker, you played around with for smaller use case. Did you evaluate any of the other, or have you heard of any of the RL providers, like the Engram or Trajectory or Prime Intellect, or evaluate them at all at DoorDash?

**Expert** [00:32:09]
No, sorry, unfortunately not. We are a little bit late for this game. We basically started the LLM adoption for production roughly last May. All we have is very, very high lifting for the coordination, orchestration for OpenAI jobs, Gemini jobs. That actually spared lots of cycles for my MLEs. That's why, right now, we want to leverage the advanced technology and also the expert in the domain. Also, we have to catch up the fine-tuning part.

Initially, we used just supervised fine-tuning. Later, we evolved to this reinforcement fine-tuning. We try to leverage the good here. We are not really evaluating other companies yet. Because the area moves super fast, we probably will evaluate other competitors very soon and also other different models.

Right now, initially, for example, for cloud, we just used the Anthropic, their own model, whether it's Opus and other things. We're also on it. Right now, we encourage the team to move to just use GLM-5.2 as our day-to-day regular tasks. We only use the higher-end models when we have complex jobs. That's the direction we are moving in. We also have other things to deliver. Limited bandwidth, that's one thing, and just step by step.

---

**Client** [00:33:39]
Yeah. I'm curious, do you guys use any of the eval providers at all, like the Braintrust or the Judgment Labs?

**Expert** [00:33:45]
Yeah. We use Arize. Have you heard of that?

---

**Client** [00:33:50]
Yeah, I have heard of Arize. You guys use Arize.

**Expert** [00:33:55]
Initially, we used that for our evaluation, the very early stage, probably last year, maybe October, November-ish, when we really developed our first version of the carousel. We want to use LLM as a jury type of thing. We have three LLMs to do a majority vote. We developed our in-house evaluation platform on Arize. Other teams, that's also the merchant team, the team that worked with Applied Compute before. They also use the same platform. They basically put their examples there, their samples there, their evaluation criteria there.

On our in-house platform, you can configure which language model is your jury, and then how do you make the final decision, whether it's majority vote or other ways. We output all different first evaluation results, as well as how does that compare to the consistency between LLM and the human judgment. We have Cohen's kappa, the corrected consistent metric. That was our initial version. We feel that's not optimal, and that's why we have some connection with Metis, and then right now the Applied Compute.

---

**Client** [00:35:10]
Makes sense. What use cases is Metis helping you with internally today?

**Expert** [00:35:16]
Metis was helping us for another project. They were evaluation company. I'd say they also do fine-tuning a lot. In another project, the agentic project, we didn't discuss that a lot. DoorDash also has right now the agentic assistant product offering. If you see your app, at the bottom, there's a search box. You can do voice search. You can also do very natural search.

For example, Friday night, I want to have a cozy dinner at some place. That one originally used our user profile. My team built the user profile. At that time, we also used ChatGPT, we used Gemini, which is still pretty expensive. Metis got acquired by DoorDash, and then they started to help us to fine-tune LLM there and to make the profile cheaper.

Metis also helped our taxonomy work. We have user profile. Some of the fields of the user profile is natural language, free-text format. Some of the field is the taxonomy, the type. We have different levels of categories. Metis team helped us to have a fine-tuned LLM to really get slightly better performance, accuracy for those category relations for different cuisine categories. That was also used. That was initially by LLM, but later Metis team got a functional model for that.

---

**Client** [00:36:46]
Super cool. I'm curious, you've worked with the Applied Compute team now for a while, over the last few months and a lot recently. How would you rate your overall interactions with them, out of 10, where 10 is they're amazing, you'd recommend it to other engineer friends of yours, and zero is really awful?

**Expert** [00:36:58]
I still would say they are good. Out of five, I would give four or 4.5.

---

**Client** [00:37:04]
Okay. Any recommendations or anything you'd like to see them add to the Applied Compute product that would make it even better for you guys?

**Expert** [00:37:12]
Yeah. I think probably better inference. Right now, they mostly do fine-tuning, evaluation. That's their maybe bread and butter or their flagship thing. When we discuss with them, I definitely sense a little bit hesitance when we talk about inference part. They are super excited, very energetic to sell the evaluation part, the training part, fine-tuning. Everything is very good. When we ask them to also help us to evaluate the inference offer or options from their side, I sense a little bit hesitance, so that's hard. I hope they can have a better offering eventually, at least for my team.

---

**Client** [00:37:53]
Can you maybe explain to us really simply why it's easier or better for your team to run the inference on the same platform that you do the post-training, the fine-tuning? Why would it be so valuable for them to also have a really good inference platform rather than you having to use another vendor like Modal, except for if they offer cheaper?

**Expert** [00:38:13]
Yeah. The most simple reason is our hope is we press one button, everything is done. Right now, if we have two platforms, we need to press the button twice. That's probably the most simple.

---

**Client** [00:38:26]
How difficult is it to press that button twice? Do you have to move the data or move the model over? How much overhead or pain is there?

**Expert** [00:38:35]
It's move the data. Move the model, I think it's probably okay. If we don't update model, that's fine, but move the data. Also, we want to have higher cadence for updating our recommendations. Even with the same model, we could have new orders, they could order a different dish. How to capture those things, the most straightforward way is to do more frequent updating. Every time, we cannot forecast or have a prediction when the previous job is finished. That adds lots of pain.

Our engineers, in extreme case, they need to wake up super early to start job so that they meet their deadline. They need to stay super late to debug or to make everything work to meet their deadline. I'm in the same experience before. One platform end-to-end or maybe there's a seamless connection between different platforms, that also works. It would be better for us to have one thing that can trigger the entire job, and then anything wrong in between can alert us. We can have on-call to look into it rather than just passively waiting for the problem to happen. That's a waste of time.

---

**Client** [00:39:48]
Makes a lot of sense. Just allow the online or even the offline updates to happen much faster would be much easier if it was on one platform.

**Expert** [00:39:57]
Exactly. Also, in the future, it has to be seamlessly triggered all real-time. In that case, no one is going to sit in front of the screen to see whether it works or not. It's not scalable. It's just that future, it will be all real-time. It will be one thing, press button, then everything is done.

---

**Client** [00:40:18]
Makes a lot of sense. Thanks so much for your time. This was really helpful. Thank you so much.
