---
theme: "Other"
title: "Founder & CEO at Anterior Believes Document Ingestion APIs Are Commoditized and Recommends Leveraging Core Large Language Models"
doc_id: EC-1000000-233440
source_line: "Mecka Ai · Expert Call · Customer · 18 Oct 26"
date: 2026-10-18
company: "Reducto"
pages: 2 of 2
saved: 2026-10-19T14:55:04.713Z
url: https://research.alpha-sense.com/search?search_id=tmp-eukhj5xq27lojzryvjdyi&sort=DATE&order=DESC&docid=EC-1000000-233440
---
# Founder & CEO at Anterior Believes Document Ingestion APIs Are Commoditized and Recommends Leveraging Core Large Language Models

Company Deep-Dive

DATE PUBLISHED

18 Oct 2026

INTERVIEW DATE

20 Jul 2026

EXPERT PERSPECTIVE

Customer

ANALYST PERSPECTIVE

Business-Led

PRIMARY COMPANY

Reducto

SMART SUMMARY

Summary

The interview covers the expert's experience evaluating and using document ingestion APIs for health insurance workflows, detailing the decision process for selecting a vendor and current attitudes toward the commoditization of the technology.

EXPERT BACKGROUND

- Founder and CEO of a company focused on automating health insurance back office workloads, with extensive experience in handling unstructured data and implementing document ingestion solutions, including building internal tools and evaluating multiple vendors.

EXPERT SENTIMENT

- Views document ingestion as a largely solved and commoditized problem, with minimal differentiation among leading solutions today.
- Believes that future value will accrue to core large language model providers, and would recommend new projects use those directly rather than specialized vendors.
- Satisfied with current vendor due to reliability and continuous improvement, but would switch if costs increased significantly or priorities changed.

TAKEAWAYS

- Initially built internal document ingestion tools before evaluating and selecting Reducto over other vendors like Unstructured, Extend, and cloud providers, primarily due to accuracy and customer service.
- Reducto was chosen because it performed best on challenging medical document edge cases, though the margin over internal solutions was small; freeing up engineering resources was a key factor.
- Switching vendors is technically easy (just API calls), but not prioritized due to minimal business impact and higher priorities elsewhere.
- Accuracy for document ingestion is now in the 99.9% range, and further improvements would not meaningfully impact customer experience; cost is a minor consideration at current scale.
- If starting from scratch today, the expert would use large language models directly for document ingestion, as specialized services are no longer seen as necessary.

AlphaSense Smart Summaries are AI Generated

Introduction and Context

Initial Evaluation and Decision

Current Usage and Considerations

Evaluation Metrics and Comparisons

Future Perspectives and Recommendations

Introduction and Context

EXPERT BIO

Founder & Chief Executive Officer at Anterior. Expert can speak to their extensive experience as a key decision-maker in adopting and implementing Reducto at Anterior, showcasing their deep understanding of the product's applications and benefits.

Founder & CEO at Anterior. The expert is responsible for leading the company in addressing the burden of US Healthcare Administration and securing significant funding from top investors, including Sequoia, Neo, Blue Lion, Microsoft AI's CEO, and DeepMind’s founder Mustafa Suleyman.

Prior to Anterior, the expert was a Product Lead at Google, leading product initiatives within the Google APM cohort.

Before Google, the expert worked as a Doctor/Medical Student at NHS, completing rotations in various specialties at major hospitals.

The expert also participated in an Entrepreneurship Residency at Meta, building automated training scenarios for medical professionals.

The expert can speak to healthcare administration, medical training, product management in tech, AI applications in healthcare, and entrepreneurship in the healthcare industry.

View More

INTERVIEW TRANSCRIPT

**Client** [00:00:00]
Thank you joining today.

We're trying to understand a bit more about the document ingestion API category, if you will, companies like Reducto and Unstructured and Extend and a handful of others.

It seems like you are a big customer of Reducto, but I just want to confirm that's correct before moving forward.

It would be great to understand more about you, your company, and then we can go from there.

**Expert** [00:00:25]
That is correct.

I'm the founder and CEO of a company called Anterior.

We do workloads for health insurance back office, so things like prioritization, payment integrity, risk adjustment.

The crux of it, as you can imagine, there's a lot of unstructured data.

Therefore, from the beginning, we were using large language models to do a lot of these workloads.

From the beginning, a lot of our data was coming in via digitized faxes, so in PDF form.

All kinds of documents in all manner of different unstructured formats, where often the reliable way to see them is just as those images where you have to then do some sort of processing on.

From the beginning, we have always needed document ingestion tools.

We built our own one, then trialed a few different ones, and then moved on to Reducto, and have perspectives on document ingestion because it's upstream of everything else that we do.

---

**Client** [00:01:27]
Got it.

Curious, like everything you have used so far, I saw on the screener that you have tried internal parsing approaches and other vendors.

Why did you end up settling on Reducto ultimately?

**Expert** [00:01:40]
Initially, when the company was starting out, before we even came across Reducto, as I said, it was an upstream problem.

If it was going to be garbage, unstructured data passed into LLM, then everything downstream is not going to work.

From the beginning, we dedicated real engineering resource.

When we were about four or five engineers, that was one or two dedicated engineers to basically doing ETL or OCR plus some LLM approaches.

We were using some of the multimodal language models at the time.

We got it up and running, and it was working.

Remember, for our specific use cases, anything off the shelf at the time, before Reducto was founded, I think, the only things that were best were Microsoft had a text service and Google and so on.

They weren't perfect, so we built our own one because it was so important.

I know the Reducto founder reached out and said, "Hey, we think we have a best-in-class.

Can we have a go at this?"

We thought, "Okay, let's give it a shot."

We want to do it fairly, so we basically have a test case of 200 horrible PDFs where we know the right answer, where it's really messy, and I can go into detail as to why it's challenging.

Therefore, we ran an eval against Reducto, against, I think it's on Unstructured, Extend.

There were also some of the Google models and some other cloud providers.

Reducto came to be the best.

Now, I do believe it was roundabout the ballpark of what our internal performance was, but we switched over for a particular reason.

That reason was that if they are good enough and they are covering a lot of those horizontal use cases, I believe in specialization.

If they can take care of this problem and spend their best efforts and keep growing and really try to burn down all the issues on accuracy on that, I'd rather free up my engineering resource to work on more downstream things.

That's why we made the trade-off, even though they weren't miles better than what we had internally.

We are a small team, we are constrained.

I would rather spend those engineering hours on something else downstream and then assume that Reducto has the best engineers.

They gave us a fantastic customer service experience as we transitioned over to them, and where we felt and we trusted that they will keep staying ahead of the frontier, and I can free up my engineers.

That's why we went with them.

They were the best out of the rest, and also the customer service and experience and everything else.

We are still with them to this date, even though myself, I have perspectives that ultimately the language models themselves will offer this feature natively within them.

Multimodal models are more inherently designed to perform better, especially for the more complex edge cases of document ingestion.

Let me pause here.

---

**Client** [00:04:41]
That all makes complete sense to me.

Curious why you aren't using the models from the Frontier Labs or open-source models more specifically.

I've seen the benchmarks, it seems like they stack up pretty well.

Is it a cost thing, or is it something else that I'm missing?

**Expert** [00:04:57]
We're using Reducto mainly because of habit.

We switched over to Reducto about two years ago now.

It's working, it's perfect.

Uptime has been really good.

Also, because just to give you a sense of the work that we do, a prior authorization might cost our customer $50 to do manually, might cost $10 with us to do with AI, and then the document ingestion piece of that is a couple of cents.

If I ever try to optimize for cost, at the moment, we don't need to optimize for cost because cost of goods sold per basis points or tokens, we're profitable.

If it's working, there's no need to try and optimize.

The only reason we'd move off eventually, if we're about to IPO and want to get our cost structure perfect and so on.

At the moment, it's problem number 15, that there are equivalent, if not slightly better models that can do document ingestion to just migrate everything over.

We already have live customer deployments and stuff.

There are 100 other things that we want to do.

Also, right now, document quality and accuracy, Reducto hasn't been staying still.

It's been improving.

It's like in the 99.99% range.

We would acquire another 0.99% or something.

That just isn't enough to move the needle.

There's way more low-hanging fruits for us to overall optimize quality and accuracy that we haven't dedicated any time or effort.

Maybe in a year or two, three years, we have a new technology leader, we grow up, or we are under expectation to cut costs or whatever, then we'll turn around and do it.

Put it this way, if I were to start a company today, I would actually just use large language models inherently under the hood and just throw the document at them into their context window and expect that they will get really good results.

---

**Client** [00:06:58]
Could you share more about what is locking you into the platform?

What makes it so sticky?

Would it be a list for your engineering team to actually move to the frontier models?

**Expert** [00:07:10]
No, it's not sticky.

It's just API calls.

We can switch them.

If we said this is a top priority right now for our team, we are about 25 engineers or so, we could have it done in probably under a week.

It's just that, for what benefit?

There are 100 other things the team could do in a week that would ship more features for our customers, our platform stability.

There is a bunch of other stuff that we could do that we haven't got around to it, for what benefit?

The open-source models are not an order of magnitude better, and even if they were, accuracy is already a largely solved problem.

That's why it's just insignificant to us.

Before, it was mission-critical.

We needed to have the best-in-class solution for document ingestion.

Right now, document ingestion, whoever we go to, is going to be in the rough ballpark of accuracy.

Therefore, if I were to start again from new, and I didn't have all these other conflicting priorities installed for our engineering team, I would actually just go straight to the models because it's simpler.

If there are 100 workflows that are up and running and stable for the customer and happy, it's just not worth it to go off, even though we can and probably can do in a matter of days.

It's just not worth to go in and mess around with that and just move on to other things.

To caveat, my understanding is we are experimenting now with just straight Gemini in some of the new workflows that we are doing.

Gemini seems to have the best one.

We are experimenting, but again, as CEO of the 100 different problems I have, this is very much on the lower end of that list.

---

**Client** [00:09:01]
Got it.

Even if there was a solution that was marginally better, it's not a part of the stack that you are thinking about all that often.

Is that a right characterization?

**Expert** [00:09:12]
Exactly.

If I was starting greenfield again, I would pick the best, and I probably wouldn't go with a specialized service.

We already have made a bunch of decisions and everything else, it's not worth going to revisit, for now.

Unless, if Reducto jacks up the prices 10X tomorrow, that will bump up the priority, and we will switch over.

---

**Client** [00:09:35]
Curious about how much it would move the needle for you from a business perspective.

Are you at the point where now that it's past a certain threshold in accuracy, it doesn't affect the customer experience, where a 10% jump meaningfully improves your product experience?

**Expert** [00:09:53]
I think that we're in the 99.9s percent of accuracy now.

There are way more low-hanging fruits that affect areas that we are controlling.

The orchestration platform, how we write skills and actions, and there's stuff within our scope of influencing what we build that moves the needle way more for the customer than swapping out an API for another one that has a marginally better performance.

That was the case two years ago.

It's no longer the case today.

It's a solved problem, so to speak, so we're not interested in relitigating that.

---

**Client** [00:10:30]
Got it.

I wanted to understand a bit more about your customer journey with Unstructured.

It seems like you were using that for quite a bit.

Would you mind just sharing how that shook out and what was the ultimate turn there in a little more detail?

**Expert** [00:10:46]
We weren't a customer of Unstructured.

We were never one.

---

**Client** [00:10:51]
You just evaluated?

**Expert** [00:10:54]
We just evaluated them alongside others.

---

**Client** [00:10:57]
Could you share more on the metrics that you were caring about when you were evaluating against Reducto?

I assume there's accuracy and latency, things like that, but would love a more comprehensive list.

**Expert** [00:11:10]
As you correctly alluded to, it was accuracy.

We had 200 hot topic cases where it was equivalent of find this particular information that to get it right, you'd have to have structured the document, understood it.

We had a mixture of those challenging edge cases.

A matter of concordance with the correct answers, Reducto was the highest.

It wasn't a perfect score, but it was the highest.

The other stuff was latency.

Some of the features of the API that were provided, could we improve it or add context.

Also, we felt like the Reducto team were way more responsive, because they were just starting out.

Maybe they treated us a bit more special.

Our team felt like migrating over to them was in safe hands.

I remember, we'd ask them for changes on things on API, whatever, and it would be done within a few hours.

Maybe that's changed now, I don't know.

At the time, it was quite a good relationship, and the team enjoyed working with them.

The main thing was accuracy and obviously cost.

They were all, if I remember correctly, within the ballpark.

Obviously, going with Google would have been the cheapest, but the accuracy wasn't great.

With the cloud providers, it was the cheapest, but the accuracy wasn't great.

---

**Client** [00:12:40]
Got it.

Can I just ask a quick follow-up question?

Since you mentioned that frontier models and open-source models have gotten better at doing this kind of data document extraction type of task, why do you think Unstructured wasn't able to perform as well on the edge cases compared to Reducto and other vendors?

**Expert** [00:12:57]
I don't remember at the time.

This was two, three years ago.

Just to be clear, if I try to remember the rough ballpark of scores, the cloud providers were maybe in the 70s percent of accuracy, 70s percent to low 80%.

I think Google was the best.

Within the Extend, Unstructured, there was one or two others, and Reducto, they were in the low 80s percent to low 90s percent range.

Reducto was the best.

I think they were ballpark.

If Reducto didn't exist, we would've probably gone with an Unstructured or others.

It was just that on that particular use case, Reducto did the best.

I could try and guess as to why.

I think from the beginning, Reducto was taking a lot more of, "Was using just those VR, was using a bit more clever techniques around segmentation, visual layouts, and ingesting that."

I think that probably was working better for medical records.

That's my hunch.

We just cared about who would perform the better on our hard dataset, and they did.

---

**Client** [00:14:09]
Got it.

The use case they were doing well in that Unstructured wasn't doing as well in, was extracting data from medical records?

**Expert** [00:14:17]
Exactly.

It was really tough.

Sometimes it was handwriting, sometimes it was four pages scanned onto one page.

Sometimes it was upside-down pages.

It was that kind of stuff, and for that test cases, Reducto did the best.

---

**Client** [00:14:37]
Sorry if I missed this.

What was the accuracy for Reducto in terms of percentage or success rate?

**Expert** [00:14:44]
I believe at the time, it was concordance with our test results, which was 92% or something.

---

**Client** [00:14:50]
If you were using an Anthropic, the most advanced Anthropic model or GPT model or Gemini model, is that close?

**Expert** [00:14:59]
If we were using the latest one today, because at the time, no, they were garbage.

We had to do a bunch of post-processing on top that I imagine Reducto has been doing.

Today, I would say close, if not better.

---

**Client** [00:15:14]
Interesting.

Which one is the best in your opinion?

**Expert** [00:15:17]
Today?

---

**Client** [00:15:19]
Yeah, today.

**Expert** [00:15:21]
This is not a strict answer, but I would say my hunch is Gemini, purely because Google specifically I know has spent a lot of time and effort on scanned documentation and things like that.

The most powerful capability is on the 3.1 and 3.5 Pro models is the best, but obviously not scientifically tested this.

---

**Client** [00:15:43]
Do you think Reducto's product has also improved over time since you started using them?

**Expert** [00:15:49]
They have.

They've definitely improved, and this is the point I was trying to make earlier, which is that they've continuously been improving in the background, and they will just update the API without us caring, and then the quality keeps going up.

We've definitely noticed that it's improved, and that's why if they've stayed static since two years ago, we would have switched off by now.

They keep getting better, whether it's in line with the others, it's ahead of the others or not, my hunch is that just natively, Gemini will be able to always provide a really good or stronger experience, but they have definitely been getting better.

That's why we just haven't bothered going around to change it to optimize the cost.

---

**Client** [00:16:31]
Got it.

Who would you say is the runner-up to Reducto?

**Expert** [00:16:35]
Runner-up today as it stands?

---

**Client** [00:16:38]
In terms of others you've evaluated.

I don't know if you've evaluated others beyond Unstructured.

**Expert** [00:16:45]
I personally haven't been involved in any evaluations for the last year or two.

I'm not sure how much of my team has evaluated, but I think it's very much we see Reducto as the best of a bunch, but this shouldn't be a specialized workflow.

If we were to evaluate, it'll be against the Gemini and others.

I've not played around with Unstructured, Extend, or anything else.

I feel like they're all going to be in the same ballpark.

Otherwise, I would have heard about it.

No one has an order of magnitude better than anyone else.

That's why I think this problem is generally a solved problem.

If something's commoditized and a solved problem, then the value will always accrue to the one that's giving you the LLM to begin with.

I'd rather just keep it simple.

That's why we've even stopped bothering to measure because it's a solved problem.

Hallucinations on documents or mistakes on documents is such a rare thing at the moment, at least for what we're doing, that we've stopped caring who's better than who.

---

**Client** [00:17:52]
They also claim in their blog post or something, that current models, if you just use the raw models themselves, that long context, perfect recall becomes an issue.

Is that just not as much of a concern for your use case, or have you noticed that at all if you were just using Gemini?

**Expert** [00:18:11]
Yes.

I can see Reducto would make that claim.

My personal opinion, that's a bit of an unfair claim in the sense that any extraction we are doing from Reducto, I know there are people that have different use cases with Reducto, but in the use case that we use Reducto for, which is, "I'm going to send you a 300-page medical record."

Sure, Reducto probably has some clever techniques or whatever to make sure that it doesn't get lost, but then I'm going to take the outputs of Reducto and pass it to a frontier model.

If I'm going to go then pass it to the frontier model, any problem that Reducto points out in those model will reappear again in that model.

What the argument against Reducto is that to say, "Why am I doing a two-step process of sending the documents first to Reducto, then getting the output, and then passing it to a frontier model, which I will always need to do in any agentic workflow?"

Instead, I could pass the whole thing from the beginning into the frontier model.

Therefore, if that was an issue with the model, that's the issue with the model.

There was nothing to do with Reducto to begin with.

Do you see what I mean?

---

**Client** [00:19:25]
That makes sense.

Another question was, which APIs do you use from Reducto?

**Expert** [00:19:32]
Again, I'm not in the code anymore, but it's probably the oldest one.

It's the ingest API or something.

It's where you throw a document, literally throw some files over at them and get it back a structured response with citations or bounding boxes about where the data was pulled from.

If you're asking about whether we use any of their fancy new agentic action-type stuff, then we don't.

Just the dumbest one.

Look, that stuff is interesting, but I think that ultimately that's my job.

Everything outside of cleaning up and doing the document is the job of the downstream start-ups.

All the frontier labs, I feel like it's hard.

I don't know what they're trying to offer there, but maybe I'm not the target customer.

---

**Client** [00:20:23]
Got it.

I know on their website, they also claim that there is a different level of complexity to each of the API.

That's automatically determined when the customer sends the documents over.

Is that something that you have noticed?

You burn more credits if it is a more complex document.

**Expert** [00:20:42]
My understanding is that we cost off more per page of documents.

Maybe we are not using those clever new features, but I feel like it's all icing on the cake.

That's what my point earlier about largely we have solved some of the hardest challenges and anything else it's not worth our attention.

I'm sure maybe there is some clever, fancier thing with newer endpoints, API endpoints, and some cleverer things, but maybe we should go revisit it and see if there is anything interesting there.

My hunch is because before document ingestion used to be such a broken thing that even with Reducto being the best or so, it wasn't perfect.

A lot of when we are doing QA of outputs of AI, we noticed that the root cause was just a badly ingested document.

Now that's no longer a problem.

Even if they have this fancy new stuff on top, I either care that they do it behind the API I already have, so therefore amazing accuracy keeps going up, or if it's some new other stuff, it's not even worth thinking about switching over.

There are a lot of other things for us to do.

I'm sharing that not because I don't think they are great.

I think they are great, it's I'm sharing it to you to get a sense of a customer's attitude towards how much of this is solved.

I put it this way, do I care if Google Cloud went down?

I would probably go to AWS or Azure.

In my head, yes, they have these fancy new features they ship.

Largely speaking, I need to deploy some code on a cloud.

I am going to use one of those three, if one didn't exist, I will use the other.

Do you see my point?

---

**Client** [00:22:32]
For sure.

Maybe to get your reaction to this, for example, if it is a document with nested tables or merged cells or a chart with a ton of numbers on it.

Instead of using OCR or computer vision, they would also run through that document with VLM, a vision language model to make sure that they have high confidence of what the extracted data.

Does that sound novel or interesting in any way?

**Expert** [00:22:58]
Yes.

This was what was novel two years ago.

We were using VLMs two years ago.

We were also doing something like that before we switched over to them.

Two years ago, yes, I think maybe this is what would have given Reducto the edge.

We were also exploring certain things.

It's the same thing two years ago.

If they are repackaging it, that's not that advanced.

The reason that Reducto, and I have seen some of the others, were a leapfrog above the cloud providers at the time was because they were doing these kind of innovative techniques on top, and these were techniques that we were looking at doing, and that's why we outsourced to them.

I am assuming whatever I am using behind the API is already using that today because we wouldn't have switched over to them because that was the best-in-class way of doing it.

That is all implementation details.

I don't think it is a new set of capabilities that didn't exist two years ago.

---

**Client** [00:24:03]
Got it.

I just want to see any feature gaps, not necessarily with the edge cases that it can handle, but any feature gaps that you think would meaningfully improve the experience for you, maybe to the extent that it would give a definitive advantage over the frontier labs.

Is there anything they could build that would get them there?

**Expert** [00:24:24]
Yes.

I see why they're doing all this clever action stuff on top because anything else they would do, they would start competing with the frontier labs themselves.

That's why they could do that, but I still wouldn't use it because I'd rather just go to the frontier labs for that, if you see what I mean, or portions of that I'm going to be building myself anyway.

That's my two cents on this.

Again, I don't spend as nearly as much time on it as those companies do, you're getting squeezed on both sides, from the cloud providers on one side and the frontier labs on the other.

That's why I always believe this is a capability that's ultimately going to just be collapsed into the cloud companies or the frontier labs, as a core capability.

They could do that stuff, but I don't want it.

Anything else beyond that, if I wanted it, I would've got it or built it myself, because it's specific to the use cases.

I'm sure if we ask them, they'll build it.

Our experience with them has been great.

They're fantastic.

There's nothing much more I want.

I just want an API.

I can send over a document, I get back the cleaned-up text outputs of what was inside that document that I can then use downstream.

That's all I want.

Whoever gives it to me at the best price is going to be the best one.

It's just that the price now is so cheap relative to everything else.

We've got to do that.

We haven't even bothered switching over to the cheapest one yet, so we're not there.

That's the obvious.

---

**Client** [00:26:07]
Curiously, have you seen any meaningful variations in performance over the past year?

From what I can tell, it seems like they might have switched around, that their models are experimented with their internal routing.

Have you seen any drastic changes in accuracy or anything like that?

**Expert** [00:26:24]
I don't think we have seen either.

We would have noticed a drop.

My understanding is that would have come to my desk, a drop in accuracy with any customer because we monitor those everywhere.

We've noticed accuracy has been steadily climbing, so any changes they have made have probably just helped.

There has been no significant drop in the quality or accuracy with our end customers.

That's as much as I can comment on that.

---

**Client** [00:26:52]
Great.

I think last question from our side.

On a scale of 1-10, how likely would you be to recommend Reducto to a friend or colleague?

**Expert** [00:27:03]
This one is a tricky one.

In the sense, as a customer, I am happy they take care of a problem.

I don't think about it anymore.

In that sense, it's 10.

In the sense if I was advising a friend who is about to start, honestly and candidly, a friend that's about to start a new project or a new company, I would say there's no need to be going to these companies.

A lot of the frontier labs already offer good document ingestion support.

I wouldn't recommend Reducto in that sense.

From a customer experience, I would recommend.

I'm advising someone technically on their stack starting today in 2026, I would not recommend it, if you see what I'm trying to get at here.

---

**Client** [00:27:49]
Got it.

What would the delta in cost have to be for you to make the switch today to an equivalent player?

If there was someone that was 20% less but with similar performance, would you immediately make that switch, or what would that threshold have to be?

**Expert** [00:28:07]
If they even double pricing, we will add it on our item list to eventually think about switching over.

For a venture-backed company, for us that was growing, that had a $100 problem.

If I was a public company and I had millions and billions of pages I need to read each day, and I was spending $20 million or $50 million with Reducto, then jacking up the price, I would be concerned.

Because of where we are as a company, that is my honest answer on the price, is that it is quite insignificant at the moment for us to prioritize it.

There are loads of other things we can do around distillation, open-source models, everything downstream that would save us way more money that we haven't even begun doing yet.

---

**Client** [00:28:53]
Got it.

I think those are all the questions we have.

Appreciate you making the time to chat.

Thanks so much.
