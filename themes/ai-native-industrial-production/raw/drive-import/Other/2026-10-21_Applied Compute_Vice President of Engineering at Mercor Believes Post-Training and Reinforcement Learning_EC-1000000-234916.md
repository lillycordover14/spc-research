---
theme: "Other"
title: "Vice President of Engineering at Mercor Believes Post-Training and Reinforcement Learning Are Crucial for Optimizing AI Model Reliability and Cost Efficiency"
doc_id: EC-1000000-234916
source_line: "Applied Compute · Expert Call · Customer · 21 Oct 26"
date: 2026-10-21
company: "Applied Compute"
pages: 2
saved: 2026-10-21T15:48:18.590Z
url: https://research.alpha-sense.com/search?search_id=tmp-l5q00vjpbwvf9aw6o2hl&sort=DATE&order=DESC&docid=EC-1000000-234916
---
# Vice President of Engineering at Mercor Believes Post-Training and Reinforcement Learning Are Crucial for Optimizing AI Model Reliability and Cost Efficiency

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

Applied Compute

SMART SUMMARY

Summary

The conversation explored how enterprises and application companies leverage post-training and reinforcement learning to optimize AI models for reliability, cost, and specific use cases. The discussion also covered the role of third-party providers in accelerating RL workflows and the technical components involved in the RL stack.

EXPERT BACKGROUND

- Vice President of Engineering at an AI-focused talent marketplace, responsible for overseeing data production and model performance, including post-training and reliability optimization for enterprise and application use cases.

EXPERT SENTIMENT

- Believes that current state-of-the-art models are generally sufficient for most enterprise use cases, but controlling error rates and reliability is more important than chasing incremental improvements in general intelligence.
- Views post-training and reinforcement learning (RL) as essential for customizing models to specific tasks, especially when proprietary data or bounded error rates are required.
- Sees value in using third-party providers like Applied Compute to accelerate RL processes and validate data improvements, given the complexity and evolving nature of RL.

TAKEAWAYS

- Enterprises and application companies use post-training and RL to optimize models for reliability, lower latency, and reduced hallucination, rather than solely for intelligence improvements.
- Maintaining control over models allows companies to avoid costly migrations and maintain consistent performance as upstream models are deprecated or updated.
- Cost optimization and differentiation are key drivers for companies to invest in post-training, with priorities varying by company stage (e.g., cost for mature companies, differentiation for startups).
- Applied Compute is used to validate data value and accelerate RL processes, providing expertise and infrastructure for efficient model tuning and evaluation.
- The RL stack involves iterative tweaking of model weights to align outputs with expected results, requiring fast, continuous feedback loops and specialized APIs from providers like Fireworks.

Introduction and Background

Enterprise Use Cases for RL Models

Challenges in Model Optimization

Applications of Post-Trained Models

Custom Use Cases and Applied Compute

EXPERT BIO

Vice President of Engineering at Mercor, a customer of Applied Compute.

Vice President of Engineering at Mercor. Reporting to the Chief Executive Officer, the expert is responsible for payments, contracts, infrastructure scaling, and the development of the evaluation service and reinforcement learning environments. Additionally, the expert oversees risk, fraud, supply referrals, and evaluation services, having successfully scaled revenue by two orders of magnitude.

Prior to Mercor, the expert was the SVP of Engineering and Head of Engineering Expense at Navan, leaving March, 2025. Reporting to the Chief Technology Officer, the expert was responsible for the Navan Expense and Issuing division, which achieved over 100% annual growth under their leadership. Key achievements included the launch of Navan Connect (third-party card integration), leading mobile unification, and managing admin web and commerce functions, including payments, reconciliation, risk, and fraud.

The expert can speak to scaling engineering infrastructure for high-growth fintech platforms, implementing complex payment and reconciliation systems, and managing risk and fraud detection at scale. They are also highly experienced in reinforcement learning environments and driving significant revenue growth through technical optimization.

View More

INTERVIEW TRANSCRIPT

**Client** [00:00:00]
Hi. Thank you so much for joining. Quickly by way of background, we are doing some research on the RL stack and understand that you are the VP of Engineering at Mercor and are a customer of Applied Compute. Maybe just to kick off, you can share a little bit about what your role at Mercor entails, and then we can dig into it and have a conversation, if that works.

**Expert** [00:00:25]
Happy to do that. Mercor is a talent marketplace where we produce data primarily for AI labs, but other enterprises too. What we do is essentially we use talent to produce this data. What we do is we take this data, and we see how much of an uplift we have on models, and all of that falls under my purview. The reason we do that is essentially the data that is valuable to these labs is data that can show model uplift, and post-training is probably the strongest way to show that there's actual value in the data that we produce.

---

**Client** [00:01:00]
You're saying, Mercor, you guys are helping produce a lot of the data that goes into the post-training process for both labs, but also increasingly application companies?

**Expert** [00:01:11]
Enterprises, like the Harvey of the world.

---

**Client** [00:01:14]
When you say enterprises, you mean companies building this into their product, like a Harvey, not like a Walmart?

**Expert** [00:01:21]
Not a Walmart, but there are some enterprises that are trying to take enterprise data and get value out of that. I can't tell you names, but there are bigger companies too.

---

**Client** [00:01:33]
Even names aside, because this is something we've been talking about, something we've been trying to better understand is, "Hey, who are the folks that may be interested in leveraging infrastructure and product for RLing models, including Mercor, but also other things." Clearly, the Harvey of the world and some of these application winners, they're doing this. One of the questions we've had is, "Hey, if you're a Walmart or a traditional enterprise out there and you're not building a product necessarily on models, but you're leveraging models for other things probably to improve your operations."

Even if you can't share names of companies, I don't want to say companies because I know you can't name them, but can you just help us understand, is it just these big applications that might do this? What would something like a Walmart, what would be the reason for them to post-train models?

**Expert** [00:02:24]
I think there are many reasons. I think the fundamental thing is, the DoorDash example is public. For them, what they are trying to do is they are trying to help with onboarding faster. How do you help onboard any restaurant? Right now it used to take multiple weeks. Can you get that down to the same-day onboarding because the effectiveness is much higher? Two things. One is the models are pretty good today that you don't need to wait for a better model. It's not that they are having a better model tomorrow that we can have better outputs. What needs to happen is the given models that are there, state-of-the-art models, can you constrain them so you get more consistent outputs? There's no hallucination, there's lower latency.

Those are the problems that these enterprises have. That's the use case that's interesting. Second thing is do things like voice, like latency-sensitive applications. It's better to host them and have bounded latency. If you were to use any inference for it doesn't matter which inference for it, there's always the last tail latency that's really high, the last 2%, 3%, and then you have to deal with that. You don't have a good answer for that today. By having a smaller model, you actually have lesser hallucination and bounded latency.

---

**Client** [00:03:44]
Yeah, that makes sense. You are saying that for some tasks that might be relevant for an enterprise, you want to optimize the ability for the model to do it correctly without hallucination, one, and two is speed and latency, which you can optimize with a smaller model, and those might be reasons why they post-train a model. That sounded like one of the things you said.

It sounded like the other thing you said was like for a Harvey, for instance, they want to reduce costs, and that is why they would do this. It sounds like for some of these other enterprises, it's, and here is maybe where I didn't fully understand what you were saying, but it sounds like it wasn't a model intelligence question. It wasn't like the model couldn't do the thing that they want. It's more like you want to do it with a certain level of fidelity, and there's certain product requirements, whether it's speed or reliability that just improves if you hill climb on a certain task, and use a smaller model instead. Something like that.

**Expert** [00:04:47]
Exactly. The other part is the models are good enough. You don't need to go to a newer model, and every time the model changes, there's a lot of work on your team to maintain your existing stack on a newer model. There were perfectly good applications running on GPT-4o that need to be deprecated, or need to move over to newer models just because they don't support older models.

---

**Client** [00:05:10]
Why wouldn't they support newer models?

**Expert** [00:05:14]
They would support numerous, meaning I have to migrate my stack over. Let's say there is a simple use case. I have a model running resume parsing. Millions of resume come into our pipeline. They all have different languages, different formats, different data. Some of them have coding information, some of them design information. How do I know who's a good designer or not? I have a bunch of things I've done, and I have this model running perfectly fine. Let's say two years from now or a year from now, they deprecate it. I need to migrate that over to the newer model. I need to have evals run. I need to do some work to migrate all of that. There's that maintenance step which I don't need if I control the model.

---

**Client** [00:06:02]
That makes sense. One thing I didn't fully understand was, you're saying, "Hey, this DoorDash example's public and their use case is onboarding of restaurants onto the DoorDash platform." What does that have to do with RL, though? What would you hill climb on exactly? I'm struggling to see the connection between that activity and post-training models.

**Expert** [00:06:26]
There's a bunch of custom logic you have. When a restaurant menu comes in, how do you know what are specials, what are weekday specials? How do you validate the data coming in is correct or not, and what are the steps you take? Let's say you were using the latest GPT model. You can't change what the model outputs, because you don't control that. Let's say there's some hallucination. I don't care about anything else, but this part of OCR. I can't tune the model.

Fundamentally, this model might have some quirks, but if I were to create a custom model, I can control that, because your hill climbing is your data, so your model is tuned for all you care about is OCR-ing these kinds of images with food, with these kinds of labels.

---

**Client** [00:07:13]
It feels like there's some trade-off where if your general intelligence is high enough, it can perform well or even better on specific tasks. Even this OCR thing, if your general intelligence is high enough, you can probably onboard restaurants better than a post-trained model that DoorDash creates for this specific purpose.

**Expert** [00:07:32]
Yes. That is correct.

---

**Client** [00:07:36]
Basically, the investment that DoorDash is making, I'm trying to think through, given that they know that intelligence is improving with successive model releases, how do you think they think about that investment they're making on the post-trained model? Why are they making that if they know that general intelligence is increasing and presumably there's some risk where maybe the next model release is going to be better than their post-trained model?

**Expert** [00:08:01]
Exactly. I think the thing is, let's say we have a few use cases. DoorDash has a few of these image cases, but the model is good enough today. I don't need a better model. Even if model improvement froze for the rest of time, I'm in a perfectly good spot. All I care about is not having these errors for these last 2% of restaurants, because when you onboard millions of people and there's 2% error, there's still a lot of support calls.

It's even worse if it's 2% of voice conversations if I get an error, because in the middle of a conversation, we have an interview that runs for an hour. Let's say there's a 2% error happening in there, in the middle of an hour, while somebody's talking, if something hallucinates, that conversation goes haywire. That whole conversation is wasted. What I care about is not having a better model tomorrow, but having a model that has lesser errors. By definition, these models that you get from closed source, you can't control the error rate. It has higher highs, but there may be lows, too.

---

**Client** [00:09:07]
You are saying even as general intelligence improves, it doesn't necessarily mean that the error rate lowers for some mundane tasks necessarily.

**Expert** [00:09:16]
Exactly.

---

**Client** [00:09:17]
It doesno't? It seems, just based on my own anecdotal usage, it seems like it does, but maybe you are saying that that's not necessarily the case?

**Expert** [00:09:28]
Do you see 100% reliability on any task?

---

**Client** [00:09:32]
No. Of course not.

**Expert** [00:09:35]
That's the thing. What you care about is not having failures.

---

**Client** [00:09:41]
Yeah. In your experience working with not the big labs necessarily, because I imagine the focus of the big labs is just to improve the model's capabilities in discrete areas like finance or whatever. They're doing RL for that. That makes sense. What about when you work with these apps like a Harvey or a DoorDash, are they more focused on reducing cost, or are they more focused on this reliability question? What's their focus, would you say?

**Expert** [00:10:09]
It depends. DoorDash clearly had this thing where they couldn't get additional headcount. They were trying to improve their bottom line numbers. Public company profitability and all of that mattered now. It's purely cost optimization and top-line growth. Harvey is more early stage. Their primary thing is differentiation. If they don't differentiate fundamentally, will OpenAI eat their lunch? It depends on the stage of the company and what they're trying to do.

---

**Client** [00:10:42]
Actually, I know we just have 10 minutes, so I have a few more questions.

**Expert** [00:10:47]
No, let's keep going.

---

**Client** [00:10:49]
Why are you guys a customer of Applied Compute? I would have thought that somebody like a DoorDash would have been a customer of Applied Compute, and then they would have maybe used you guys for data, or something like that. What are you guys using Applied Compute for?

**Expert** [00:11:05]
Two things. One is, we produce this data that we sell to the OpenAI world and to others, NVIDIA and other enterprises. How do we prove that the data we have is valuable? Even the best salesperson is essentially taking a model and showing an uplift and having a third party do that. That's the primary reason. The second thing is we also want others to take the data and make model improvements for themselves. Meaning, the reason we got to work with Harvey is because Applied Compute works with us. They see the data improvements, then they work with Harvey, they build their own models. It's a mixture of confidence, and this is our sales go-to motion, if you think about it.

---

**Client** [00:11:52]
Yeah, that makes sense. It's not like you guys are post-training any models necessarily.

**Expert** [00:11:59]
We are, but that's a different story. We are, because we have our own resume parsing stack. We have our own stack for finding who the best candidates are. We have our own stack for AI interviews because we want to have no error rates. We have a bunch of support use cases, like all our support is automated by this agent called Melvin. All these use cases, we want to build our own stack, both for cost and for same thing, error rate. We have a bunch of support use cases. We can't have even a small error rate when people are asking financial questions and there's legal implications also if I have a support agent with some error rate.

---

**Client** [00:12:42]
You're saying for your own products with the experts you work with, you have a support stack, and you're saying you're leveraging post-train models for that?

**Expert** [00:12:51]
Exactly.

---

**Client** [00:12:52]
Maybe that's a good place to double-click for a second. Why don't you guys just use closed-source models for that? Why do you need to post-train models for that?

**Expert** [00:13:03]
A bunch of our questions also includes actions we take, like actually logging into Stripe, the bank account, finding out where the money is. A lot of it is mostly around error reduction. As I told you, we have a model from six months ago that's good enough. I don't need to ever change my model again. I have one GPU running this model with Fireworks, and I'm good.

---

**Client** [00:13:29]
It's not sufficient to just use an open source model, like through Fireworks? Just have Fireworks serve an open source model that works. You need to RL it?

**Expert** [00:13:43]
For example, RL helps with a bunch of use cases because we have custom use cases. We have more resumes that we have parsed than OpenAI's models have. There's more diversity of data we see. We want to get something that's richer.

---

**Client** [00:13:59]
You're saying your support application, it's specific to recruiting in a way, and you're trying to optimize the performance of that, something like that?

**Expert** [00:14:08]
Exactly. It's not that expensive, too, meaning if you can get better error rates, if you can control the outputs, then it makes sense to do it.

---

**Client** [00:14:17]
Got it. Why are people using Applied Compute? Why are you guys using Applied Compute? What would be a reason why somebody would use Applied Compute?

**Expert** [00:14:31]
Few things. I think one is still RL is an art, not a science, meaning, what should the reward function be? How do you know if there is convergence? What kind of open source models should I use? How many parameters should I use? All of these open questions. You can either think of it as a one-time cost used to build, or you could build it yourself. It just helps with accelerating that. In our use case, we also want to give this data to other customers, and Applied Compute can work with them.

In general, I think the primary use case is velocity, answering a bunch of open questions, and it's more recently that post-training libraries are more generally open. About a year ago, it's not as common. There were a few things and others. Right now, is when there are more APIs available. Thinking Machines APIs are available now. Fireworks has an API now, Together has an API now.

---

**Client** [00:15:31]
I'm honestly a little bit less clear how this stack works. My understanding is that makes sense that it's a little bit more of an art than a science, and you need to come in, build the right evals, and verifiers to make sure that you are hill climbing on the right thing. That all makes sense. What are the components of a stack? You have Applied Compute. I don't totally know what their product is, but it seems like they bring some of the expertise to figure out that art, and then you are saying, Fireworks has an API. What does that API do exactly? Maybe just help me understand behind the scenes what's actually happening.

**Expert** [00:16:14]
At a high level, this is what's happening. Two things. One is you have what your current model does, you have what the output should be. You take the current model, you run it against your inference, and then you have the exact output. You hill climb against that. If the output matches, good. If the output doesn't match, you tweak it, so it starts making sure that the current policy matches the policy you want. If you tweak the parameters and it improves, that's good. If it doesn't improve, you tweak it in the reverse. You keep tweaking these parameters and you are hill climbing your output against expected output until the model's parameters match what your policy is.

---

**Client** [00:16:58]
This part I do understand, but when Fireworks exposes an AP, what have they actually built? I'm trying to think about under that API, what is it that Fireworks is exposing? I know Fireworks, their main business is they have a bunch of GPUs to serve open source models. Maybe help me understand, for fine-tuning, what exactly does that technology do? I know the process you mentioned. That makes sense, but I'm struggling to understand the technology a little bit.

**Expert** [00:17:35]
I think the main thing is it has to be fast enough. The same GPU needs to interleave this prediction, changing weight, new inference. Prediction, changing weight, inference. You need to do that fast enough so your GPU isn't blocked. How do you update all these weights and get inference running fast enough and have the next prediction? This whole thing needs to be a continuous loop that's effective.

---

**Client** [00:18:04]
Yeah. How do the weights get changed exactly?

**Expert** [00:18:09]
You are updating it based on what you expect versus what's happening.

---

**Client** [00:18:14]
Yeah. Here's where I lose my understanding a little bit, because my understanding is whatever is output from the model, what even is it exactly? It's just a bunch of vectors in vector space that are some representation of whatever the output is?

**Expert** [00:18:31]
Exactly.

---

**Client** [00:18:32]
How does that output and the deviance of that output from whatever was expected, how do you turn that into changes in the weights?

**Expert** [00:18:41]
Essentially, what you know is what prior weight changes caused this. Let's say you did even random, but directionally, if you chose a random weight, you have the vectors. You know that this parameter defines this expert. You have a mixture of experts. You know which expert is responsible for which part of the data. You know that you need to tweak in certain directions. It's probabilistic learning that you try, and every change can be positive or negative. You keep making the positive changes.

---

**Client** [00:19:13]
I see. That's what this API does, is it does these iterative tweaks to the weights and quickly measures, "Hey, is this getting closer to what we want?" It pushes and pushes until it gets closer to what we want.

**Expert** [00:19:28]
Exactly. You need to do this billions of times. You need to have something that's fast enough running across multiple cores and knowing which expert to call if you have thousands of experts on the same parameter.

---

**Client** [00:19:42]
Interesting. I know we're up on time. We may find more time with you because this was a really good conversation, and hopefully it feels like I'm asking the right questions, but let me know if you think I missed anything. That would be helpful to know.

**Expert** [00:19:58]
I think these are the right questions. I can explain it a little better maybe next time. I think the fundamental thing is, over time, if models get good enough and you want to have bounded errors, then you need to control what outputs come. I think that's the way to think about it. Effectively, if you have years and years of your data, which is proprietary, like a Cadence, they have a bunch of RTL gates. How do you extract that information? It's not out there on the internet, and you want to use your proprietary information. Those things are useful.

---

**Client** [00:20:32]
I think that is a really interesting insight, and that is helpfully phrased. Your belief is, that doesn't come from general intelligence improvement, though because my assumption would have been that in general, even bounded tasks, imagine one discrete bounded task. I don't even know what. Just this restaurant one, for instance. I would have thought that the performance on that would get better and better as frontier intelligence improves. I think what I got from the conversation with you is maybe that's not actually the case.

**Expert** [00:21:07]
Meaning it might get better, but it doesn't guarantee to make lower errors. The model right now is good enough to get most of the use cases. It just doesn't know that it needs to be bounded to these sets of outputs. The biggest thing, the model doesn't know when it's wrong.

---

**Client** [00:21:26]
This is super helpful. Really, really appreciate the time. Thank you. Have a great rest of your day. Goodbye.
