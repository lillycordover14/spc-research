---
theme: "Other"
title: "Machine Learning Software Engineer at OpenEvidence Believes Optimized Inference Is the Key Value Driver for Infrastructure Providers"
doc_id: EC-1000000-234107
source_line: "Baseten · Expert Call · Customer · 19 Oct 26"
date: 2026-10-19
company: "BaseTen"
pages: 2 of 2
saved: 2026-10-21T16:32:30.291Z
url: https://research.alpha-sense.com/search?search_id=tmp-l5q00vjpbwvf9aw6o2hl&sort=DATE&order=DESC&docid=EC-1000000-234107
---
# Machine Learning Software Engineer at OpenEvidence Believes Optimized Inference Is the Key Value Driver for Infrastructure Providers

Company Deep-Dive

DATE PUBLISHED

19 Oct 2026

INTERVIEW DATE

21 Jul 2026

EXPERT PERSPECTIVE

Customer

ANALYST PERSPECTIVE

Investor-Led (Buy-Side)

PRIMARY COMPANY

BaseTen

OTHER COMPANIES

Applied Compute

SMART SUMMARY

Summary

The conversation focused on the integration, usage, and differentiation of inference infrastructure providers, particularly Baseten, for both production and post-training machine learning workloads. The discussion also covered the challenges of migrating between providers, the distinction between inference and training engineering, and the broader applicability of inference versus advanced post-training in enterprise settings.

EXPERT BACKGROUND

- Machine Learning Software Engineer with hands-on experience integrating and operating large-scale inference and post-training workflows using third-party infrastructure providers, with a focus on optimizing production workloads and managing high-volume inference.

EXPERT SENTIMENT

- Believes that highly optimized inference is the primary value driver for infrastructure providers and is likely to remain the most important use case for the foreseeable future.
- Views post-training and inference as distinct engineering challenges, and does not see a strong need to couple them unless both are highly specialized use cases.
- Sees the potential for inference-focused platforms to expand into broader offerings, but notes that most users only require basic functionality beyond inference.

TAKEAWAYS

- Integration with providers like Baseten is primarily through API endpoints, with additional engineering for handling bursty traffic, retries, and resilience.
- Migrating from one inference provider to another (e.g., Baseten to Fireworks) would be relatively straightforward, mostly requiring minor code changes if interfaces are similar.
- Baseten is mainly used for production inference workloads, with internal post-training and experimentation typically handled at smaller scale and with less optimization.
- The expert sees inference as a more general and widely needed capability for enterprises compared to advanced post-training or reinforcement learning, which are niche and require significant data and expertise.
- The expert believes that while inference platforms can add features like post-training and sandboxing, their core value remains in optimized inference, and broader platform expansion depends on customer demand and implementation quality.

AlphaSense Smart Summaries are AI Generated

Introduction and Baseten Integration

Post-Training and Infrastructure Usage

Comparison with Applied Compute

Inference in Post-Training Context

Market Trends and Use Cases

EXPERT BIO

Machine Learning Software Engineer at OpenEvidence Expert can speak to their direct experience as a current customer of Baseten, providing insights into its reliability, cost-effectiveness, and integration capabilities within AI infrastructure.

Machine Learning Software Engineer at OpenEvidence. Reporting to the Chief Technology Officer, the expert is responsible for developing and scaling medical-grade AI systems that leverage large language models for clinical decision support. They hold primary authority over the technical implementation of machine learning pipelines, ensuring that the integration of complex data sets meets rigorous accuracy and reliability standards.

Prior to OpenEvidence, the expert was the Senior Machine Learning Engineer at Matterworks, leaving in January 2024. Reporting to the Head of Engineering, the expert was responsible for the architectural design of machine learning models focused on metabolomics and biological data synthesis, leading the transition of experimental models into production-ready software environments.

The expert can speak to managing multi-agent or long-horizon AI workflows in production environments, specifically within high-stakes AI platform contexts. They are experts in multi-model setups, including the integration of various AI models from both open-source and closed-source providers to optimise environmental functionality. Furthermore, the expert can consult on cost and latency optimisation in heterogeneous hardware environments; they have extensive experience balancing the cost efficiencies of fine-tuned open-source models against the performance trade-offs inherent in high-intelligence AI workloads.

View More

INTERVIEW TRANSCRIPT

**Client** [00:00:00]
Great to chat with you. I have a few questions about Baseten. You're guy's use of that within OpenEvidence, your usage just opens a model and how that has evolved over time etc. I guess one of the things that I'd love to understand is what does the actual integration with Baseten look line, is it just an API endpoint, things that you contain or they're a little bit more than that? Would love to talk to that a little bit.

**Expert** [00:00:25]
I think at its core, it is what you are saying, more of an API endpoint where you can basically pass in inputs and models. I think that where it gets a little bit more interesting than that is ideally, the top-level interface is basically an API endpoint, even if underneath that, there's a lot more complicated stuff around how that data is being passed along.

For example, I think both from their side and our side, there is a lot of considerations around things like, if you have very bursty traffic, how do you queue that up so that you don't potentially overwhelm and cause certain infrastructure to fall over? How do you handle things like retries and resilience measures such that, once again, you don't cause things to get worse if instances do happen? At the top-level, yes, that's it. In terms of how you send those things to that API, there ends up being some amount of engineering involved in creating your full executor effectively.

---

**Client** [00:01:24]
Got it. It sounds like it's a little bit more complicated than that. What I am just trying to understand is some of those configurations with the traffic retries, some of the data flows there. Ultimately, I am just trying to understand what would happen if you guys decided to go from Baseten to Fireworks tomorrow. How long that migration process would be, what would that actually entail? Do some of those things translate, etc. ?

**Expert** [00:01:50]
I think a lot of that stuff would translate, and ultimately, the core software would not necessarily be that hard. I think it would probably be a couple of days of work. I think more of it comes down to, honestly, the stuff that they have done on their side versus the stuff that we have done on ours because my guess is for things like Fireworks, they would have a fairly similar interface in terms of how you call models and send inputs, and therefore, the things that you are more concerned about is what the product is that they are offering and how it compares to Baseten in terms of the performance optimizations. More of that is the things on their side of the divide than it is on what we have implemented on our side.

---

**Client** [00:02:31]
Got it. Effectively, is it just a few lines of code that would help with the transition there, assuming that the throughput cost performance was all the same with a different vendor?

**Expert** [00:02:41]
I think that's pretty accurate to say.

---

**Client** [00:02:44]
Got it. It sounded like you guys at OpenEvidence were using Baseten for a little bit more of the post-training side. Where you guys have internal efforts, where you're having different objectives, hill climbing, trying different model architectures, etc. You'd mentioned something about Baseten for the general infrastructure and the general environment. I just want to hear a little bit more about what exactly that means. Maybe I'll just stop there.

**Expert** [00:03:11]
Basically, when it comes to the post-training stuff, generally what you can use Baseten for is the setup of, as I mentioned before, the infrastructure of what type of hardware you're running this type of inference on, as well as what type of machines and stuff. They have different types of products around are they going to fully handle the reinforcement training or learning and stuff like that for you or do you want to run your own objectives and algorithms and ML training stuff?

For us, I think we see that more of if we're doing the types of stuff that we do, we bring our own ML logic and code and algorithms that we're running. Baseten's primarily beneficial to be like, "Okay, what is the hardware we're running on? How are we setting up the dependencies and all that type of stuff as this helpful foundations to do the things that we know that we want to?

---

**Client** [00:04:01]
Got it. It's a little bit more like how do we run all of these different exercises across, let's say, 1,000 GPUs? How do we schedule the jobs? How do we orchestrate the rollout? Is that how it is in managing the volumes capacity?

**Expert** [00:04:17]
Exactly. Versus it's less about stuff like, "Oh, what is the objective?" I think that type of stuff depends on what the technical level is for your organization coming to Baseten. For at least, we tend to feel that the stuff that Baseten does is basically meant to make it easy to do the more general purpose thing. Versus, I think for us, we want to try the things that are more specific and out there to figure out what works well to make the types of things we want to. I think if you're coming to it with less expertise and knowledge, then doing the general purpose thing is still going to be probably a big upgrade from what you had before.

---

**Client** [00:04:57]
How would you contrast that with what Applied Compute is doing for you guys? Is Applied Compute also, when you hear about them, a vendor that is providing the general infrastructure where you are bringing your own objectives and algorithms or is Applied Compute using their own team to supplement what you guys have?

**Expert** [00:05:16]
We don't use Applied Compute.

---

**Client** [00:05:18]
Just in general your understanding of Applied Compute.

**Expert** [00:05:22]
In that case, I think a lot of these organizations are starting to step on each other's toes a little bit in terms of what their specialty or what their different fields that they cover. It seems like Applied Compute is also covering a lot of similar domains to what you get from Baseten. My feeling is that, I don't know a ton about exactly where their strongest suit is, but my rough sense is that potentially it's more around some of the post-training stuff.

I think that some of this just depends on do you as an organization need the most emphasis on optimizing? For us, that's 100% on inference because inference is a much bigger portion of our spend in these types of stuff than post-training because we're not necessarily training foundation models from scratch, but we are running a ton of inference on the stuff that we do train. In that order, we want to make sure we are going with a vendor that's highly optimized for our largest use case.

---

**Client** [00:06:17]
Just two pieces. Number one, I understand anytime you want to use Baseten in the general serving path, they help with inference there, but when you do a lot of the post-training, you're also doing inference in the post-training piece because any time you're trying to run these model attempts, it's also reading and thinking and hence inference. When you say that you guys are using Baseten in a material way, I think it was some low-eight-figures of spend per year, is it for customer production workloads, i.e. customers are using OpenEvidence, or is it from your guys' internal ML team that's doing a lot of these post-training runs that also requires inference?

**Expert** [00:07:01]
For our Baseten inference, it tends to be primarily for our actual production product. Internal workflows tend to, if anything, lean more towards foundation models because, like Frontier closed source ones, if you're doing a smaller internal workflow, it's often something that is, one, at a much smaller volume, and two, probably something that goes for a much shorter and smaller duration where it's actually useful. In these types of cases, it probably makes more sense to emphasize just getting something that works quickly and not investing too heavily in creating something custom, compared to in a case like a production workflow where this is something that's likely going to be stable for a very long time and be used at very high volume, where that type of optimization for performance and cost actually matters a lot.

---

**Client** [00:07:49]
I'm just trying to understand. You guys are also using Baseten during the post-training exercise, correct?

**Expert** [00:07:57]
Yes.

---

**Client** [00:07:59]
That's the environment. For example, if the model is attempting additional healthcare tasks, you have to grade the attempts, you are updating the model weights, etc. All of those runs, Baseten is also being used for inference. That is a post-training inference use case. Is that right?

**Expert** [00:08:19]
Yeah.

---

**Client** [00:08:21]
What I am trying to understand is, maybe correct me if I am wrong, it seems like there is a lot of convergence happening with Applied Compute, Baseten, but also even a Modal on the sandboxing side, even a MosaicML on the Databricks side, because all of this seems to be around optimizing post-training and training the next model. That's where they are all intersecting. Because of that, obviously, running the model in production relates to how these models are trained and how they are built, understanding them, and ultimately then they will be served. one) Am I understanding correctly? two) Should these two pieces be coupled together? Does it make sense for it to be coupled together or not? The post-training side and the actual production serving path use case.

**Expert** [00:09:11]
I think that it's interesting because in my opinion, I don't think it necessarily makes sense to couple together if you have very difficult use cases for both things, because these are very different engineering problems where there is obviously a lot of overlap, but it's not necessarily guaranteed that someone who is really good at one in terms of a company is going to be the best at the other. With that in mind, it's like, "Oh, maybe actually it makes sense to have these things be separate."

I think that my feeling is that at the moment, we don't necessarily care about things in the training side, we don't care as much about things in the training side being super-optimized because it's mostly just convenient to trust around things that we are familiar with ourselves, and it is a much smaller scale than our inference. It's mostly just convenient to deal with a vendor we already know and like and not have another one to figure out.

Versus in the case of if we were doing really complicated training, then maybe that would actually make a bigger disproportionate difference, and we would want to be with the best of the best for that. The reason why we would not necessarily want to switch to different providers, because we feel like Baseten is the best of the best when it comes specifically to inference. That may or may not be true for them for training, but that's okay for our level that we do training.

---

**Client** [00:10:30]
Interesting. You said that there are different engineering problems. Can you speak a little bit more on that?

**Expert** [00:10:38]
I think a lot of this comes down to how do you engineer these things to be the best they can be, both in terms of speed and reliability and all. I think that to some degree, these are things that, let's say you want to make a really good inference engine, you probably have to think about how do you serve models in a super performant way, how do you do so in a way that routes your requests in just the right way and all this stuff, and even thinking about what is your low-level architecture to handle this type of stuff.

I think a lot of this stuff is not necessarily very intuitive off the bat and takes a lot of very specialized engineering to figure out. Separately, let's say you want to do something like making a really good training setup. I think that's something where you have to think a lot about what is the strategy that goes into training, what is the way that you are harnessing large amounts of hardware to handle things in these big sustained training runs, but not necessarily in a consistent production serving way. These are just different use cases altogether. With that in mind, it's like, yeah, my guess is that the people who have figured out the first class of problems really well isn't necessarily the same as the class of people who have figured out the second type, because these are just different things to figure out.

---

**Client** [00:11:55]
Got it. What I'm trying to figure out is if you think about a regular enterprise, Fortune 500 enterprise, I guess there is a world where both Baseten and Applied Compute can do well, but I'm trying to figure out which one has a broader TAM. It feels like to me, Baseten or the managed inference providers do, because you don't necessarily, like an enterprise like CVS might not necessarily have to do as much specialized reinforcement learning or RLHF.

They might still need to do a little bit of post-training or a little bit of data labeling to fine-tune an open model, but then they still need to serve it on Baseten. I'm just trying to figure out in your experience, basically is RL relevant to every company here? Is that something, just given the scale that you probably need for all? Is that something that only some subset of Fortune 500 companies might want to do or basically just trying to think about which company has a broader use case?

**Expert** [00:12:58]
My feeling is that the biggest difficulty in the whole AI race overall is just the ability for people to apply these to real-world problems, when a lot of people are just not that familiar with how to handle these sorts of technologies at a start. I think a long-term vision I see for most of these things being useful is integrating relatively simple open-weight models into them and not necessarily worrying as much about things like even fine-tuning, forget about RL.

I think RL itself is a very difficult and complicated problem that is not necessarily something I expect a lot of people to be thinking about. Not even just thinking about, for example, people who are in AI companies versus Fortune 500s or whatever, or even Fortune 500 versus not. I think even most start-ups probably don't have the level of data needed to do good RL, AI start-ups even. I think things like RL to me feel like they're relatively more niche, and they're exciting sounding just because everyone is really wanting to be doing things at the frontier.

Fundamentally, having the know-how to do it well and having the data to even support it is relatively hard in my opinion, most Fortune 500s, forget about RL, I don't even think they're going to be doing fine-tuning. I think most of them are just going to be using LLMs either just off the bat or using stuff like open-weight models in something like Baseten because that's way cheaper than using ChatGPT directly. That's either way, it's either you're going directly to OpenAI Anthropic, or you're going to something like Baseten because you just want highly optimized inference for a very simple thing.

I think that for simple fine-tuning I would be curious if there's actually a huge difference as to how much better one provider is than another. I think that things get more complicated as you're doing larger scale post-training or larger scale RL-ing. The thing is, I don't know how many companies are even doing that successfully, even AI start-ups. There's companies like Cursor that do big post-training, but that's because they had a huge amount of coding data that they built up from being basically the first mover in this field. I think that some of that stuff is a little bit overblown for how widespread it'll actually be applied, realistically.

---

**Client** [00:15:15]
Interesting. On one hand, if most Fortune 500 companies are just taking a Kimi model and just serving it pretty much as is, it sort of seems like Baseten is an easier on-ramp. If you believe that there is going to be a new emergent platform here for AI workloads, Baseten seems a little bit more of an easier on-ramp for a regular Fortune 500 than trying to figure out an RLHF use case to use Applied Compute to, with the right data and the data labeling to get something usable. I guess it seems like the Baseten use case feels a little bit more general and widespread. I think that I agree with you.

**Expert** [00:15:58]
I do think that's why inference is such an important industry, because that is the direction things are likely going for the foreseeable future, at least how I see it.

---

**Client** [00:16:08]
I'm trying to basically figure out what the bull case here is, where inference is some specialized engineering discipline that stays. Baseten is able to become one of a few market leaders here, that this profit pool doesn't just go to an AWS, or a CoreWeave or some other competitor. What you'd have to believe is that Baseten isn't just being used in five years, let's say, for just inference optimization, that it evolves into some broader platform.

Where you're serving the base model, but then if you need to post-train a model, it has a broader platform that encompasses evals and post-training and the deployment of that. Maybe it even has agent runtime environments, and with sandboxing, because that's all important during this post-training exercise. I'm just curious how you'd see this company evolve into something bigger and how you might react to what I just said. Do you believe it?

**Expert** [00:17:02]
I don't really see something like AWS being a huge threat here, because my experience is these big hyperscalers are not necessarily really good at building the polished, good user interface consumer end products. I think they're a lot better at setting up the really fundamental ground infrastructure. My guess is that the bigger threat would not be that AWS builds it, but more that there's multiple other start-ups similar to Baseten that are able to figure out similar end steering, such that becomes a smaller marginal gain, and it becomes more commodified.

---

**Client** [00:17:36]
I'd be curious, do you believe that inference is a wedge into something bigger? It's a broader platform to do all the things I mentioned, like the evals, the post-training, the deployment of those models, RL environments, sandboxes, etc. What would that even look like?

**Expert** [00:17:53]
My opinion is it's relatively easy to do a lot of that stuff at a very base level. It is hard to do that stuff really well. I think that most people don't need to do that stuff really well. For those, it is easier for Baseten to add relatively simpler ways to do that type of stuff than it is for people who don't have really optimized inference to add that. Does that make sense?

---

**Client** [00:18:18]
Yeah. If you remove other competitors coming from different directions, do you think a Baseten or a Fireworks or somebody could evolve into one of those platforms? It has to become something maybe not as big as an AWS, but like a sustaining platform on top of cloud hyperscalers, just for a very different type of workload. The inference workload.

**Expert** [00:18:42]
Yeah. I do think I could see that being a long-term growth for them as a company, because I think that effectively, the point is, hopefully inference is just the way that they attract and bring people in. I think that building all these additional things on top of it, for example, even post-training was not something that they started out with, but they added in because probably it was relatively easy to do that in a simple way, and they had some amount of customer demand from people who already liked it.

I think that that pattern could definitely continue across more market segments, in a similar way that they did it in this case. I think it all comes down to what is the killer feature that makes people come to you first. I think for them it is highly optimized inference, and then from there, if you can bring in a lot of people that way, then why not be able to just continue bringing in more features that make it feel stickier and stickier and harder for people to leave, assuming that you can implement those in a way that is good enough for those people.

---

**Client** [00:19:45]
I am curious, do you use a sandboxing tool like Modal or E2B or Daytona at all?

**Expert** [00:19:51]
We don't, no.

---

**Client** [00:19:53]
Got it. I'm trying to figure out where that feature overlaps with something like a Baseten. I know Modal, for example, a couple of days ago, said that they're serving, I think it was a Thinking Machines model. Clearly, these pieces also seem to be converging, even though I thought they were pretty separate, like Modal for sandboxing and creating a more isolated, secure environment for AI coding agents, for example, to run. It seems a little bit different. I'm wondering if you have any thoughts about how these two pieces converge at all or overlap?

**Expert** [00:20:28]
In this case, what you're seeing sandboxing be used for?

---

**Client** [00:20:32]
My understanding of sandboxes is anytime you need an agent to open and work in files, it is writing its own scripts and code, potentially. You need a very secure and isolated environment that spins up and down. Number one, it's managing those volumes up and down is a pretty complicated problem, but it's also ultimately, just isolating what this agent has access to in a more secure way.

**Expert** [00:20:58]
Yeah, I think this feels like a slightly different approach to me, or a slightly different level of the stack because if you think about what agents are doing versus generally inference. I think the idea is that agents are a relatively hard thing to build really well. You have to build something that can operate across multiple steps very well and continue doing so, for long-running and harder problems.

I think sandboxing is one piece of that, but doing really good agents to the level that you would actually need sandboxing is something that is the purview of a relatively small minority of AI start-ups these days. I think the sandboxing could definitely be integrated in setups that are doing more of an agentic, providing basically more of an agentic layer. That, to me, feels a little different from what Baseten's really fundamental value problem is.

---

**Client** [00:21:51]
Thank you so much. I really appreciate the additional time. Take care.
