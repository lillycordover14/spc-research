---
theme: "Other"
title: "Senior Full Stack Engineer at Atlassian Corporation Believes Turbopuffer Enhances AI-Powered Search Capabilities and Drives Future Growth"
doc_id: EC-1000000-234918
source_line: "CORZ · Core Scientific Inc · Expert Call · Customer · 20 Oct 26"
date: 2026-10-21
company: "turbopuffer"
pages: 2 of 2
saved: 2026-10-21T15:37:13.258Z
url: https://research.alpha-sense.com/search?search_id=tmp-ffzr3ttvkmfy1lpfztggun&sort=DATE&order=DESC&docid=EC-1000000-234918
warnings: "expert bio did not load"
---
# Senior Full Stack Engineer at Atlassian Corporation Believes Turbopuffer Enhances AI-Powered Search Capabilities and Drives Future Growth

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

turbopuffer

SMART SUMMARY

Summary

The interview discusses the evaluation, adoption, and expansion of turbopuffer as a vector database solution for semantic search and AI-powered features across multiple products at a large software company. Key topics include decision criteria, use cases, architecture, and future adoption plans.

EXPERT BACKGROUND

- Senior backend engineer with direct experience implementing and scaling vector database solutions for search across multiple products at a large software company, including involvement in evaluating and onboarding new technologies like turbopuffer.

EXPERT SENTIMENT

- Views turbopuffer as a well-positioned and increasingly important infrastructure component for AI-powered search and related use cases within the company.
- Believes the decision to adopt turbopuffer was driven by its self-hosting capability, cost efficiency, and compliance advantages, despite some competitors offering better technical performance in certain areas.

TAKEAWAYS

- Turbopuffer was adopted to enable more context-aware, semantic search capabilities, moving beyond traditional keyword-based search.
- The primary driver for adopting turbopuffer was the need for AI-powered search (notably for the Rovo product), with expansion to other products and teams for similar use cases.
- Turbopuffer is used for semantic search and vector storage, while traditional keyword search remains on OpenSearch.
- Key decision factors in choosing turbopuffer over competitors like Pinecone and AWS OpenSearch included self-hosting (compliance), cost (S3 storage), and multi-tenant isolation, even though Pinecone had better recall and latency.
- There is an ongoing expansion of turbopuffer usage within the company, with expectations of 20-30% growth in adoption over the next year and current annual spend in the low seven figures.

Introduction and Initial Context

Adoption and Expansion of Turbopuffer

Technical Implementation and Use Cases

Evaluation and Comparison with Alternatives

Future Use Cases and Scalability

Strategic Importance and Financial Aspects

EXPERT BIO

INTERVIEW TRANSCRIPT

**Client** [00:00:00]
Nice to meet you.

I think just for time sake, I'll give a quick intro and then we can jump right into it.

We're spending some time around the company, turbopuffer, and vector databases and want to speak with customers who had evaluated and used the product and understand what the work like and the use cases are.

Maybe to get started, it'd be helpful to hear what your role is and contacts in which you're familiar with turbopuffer.

**Expert** [00:00:27]
I'm working as a senior engineer right now.

My role is mostly on the back end.

The product I work with is Loom.

Right now, we are using turbopuffer to power our search.

Across Atlassian, it is used for multiple products.

---

**Client** [00:00:44]
Got it.

Can you talk a little bit about what was the pain point that led you guys to look for a solution like turbopuffer in the first place?

What did you guys have in place, if anything?

**Expert** [00:00:57]
Before that, before using turbopuffer, we just had a normal search using OpenSearch, which is an internal service that we use.

Atlassian has created it.

It uses basic inverted trees.

The use case was that we wanted to answer more, I would say, context-based answer where user can ask questions, chat with all their knowledge info that is stored in the Loom itself, and then also able to answer some of the cross-product questions.

If they ask something and the answer is in another product like Jira or Confluence, then it is also able to pull some of that information.

---

**Client** [00:01:34]
Got it.

Before turbopuffer, you guys were using OpenSearch.

At what point did you guys decide to move off of OpenSearch?

What was the rationale for looking for something else in the space?

**Expert** [00:01:48]
We started evaluating all these vector databases for our search in 2025, around, I think, January.

My team was not responsible for it.

There is another team which was responsible for it.

They decided on the turbopuffer.

I can speak to some of the decision points if that is interesting.

They started using it for some of the other Atlassian products.

I think, right now, they have a service called Rovo.

Rovo was the primary reason they started looking into it, because Rovo was their AI-powered search engine which could directly answer your questions, and then they wanted to do some RAG stuff.

I think that was the primary trigger of looking into the vector databases and this particular use case.

Later, other products also started adopting turbopuffer and including that in their search.

---

**Client** [00:02:39]
Did turbopuffer's usage end up expanding within Atlassian to other teams or other use cases or other workloads?

**Expert** [00:02:46]
I think the way expansion work is that there is one team which still owns turbopuffer and everything and then we have other internal APIs which we can use turbopuffer, so we can push data to it and then it would start showing up in the search.

It did expand in Atlassian and other teams started using it.

The use case for other teams was similar in the sense that they wanted more powerful search and they wanted to come back with actual answers instead of just returning a list of document or a list of videos or a list of tech tickets.

---

**Client** [00:03:19]
Can you walk me through a real example or use case that a customer or user might have with either Loom or an Atlassian product?

What's happening behind the scenes and where turbopuffer is involved, just end to end?

**Expert** [00:03:34]
For example, if a customer creates a Confluence doc, once they publish that doc, what happens is that we have an internal pipeline where we can push it to a queue.

Confluence will push that document.

It will push that document literally with everything onto that queue and then that queue is consumed by the StreamHub team.

StreamHub is the name of the queue.

That will pick up that event and do all the embedding, chunking, and all of that and then store that in the vector database.

Whenever someone will search anything now in the Rovo or in the Confluence, it will try to answer that question by doing vector matching from that particular database.

The searching is also hybrid right now.

It also uses lexical matching.

It also matches by the keyword.

Now, it is augmented with this vector search.

Earlier, what used to happen is if someone searches for something, it would just show up the Confluence doc, like, "These are the Confluence doc where this keyword was mentioned."

Now, instead of showing the Confluence doc, we also show the exact answer to the question.

If someone is asking, "Where is the runbook?"

or "What is the runbook?"

then it would show the list of docs, but it would also try to answer that question with the list of docs.

---

**Client** [00:04:57]
Are you using turbopuffer for both the semantic and exact search?

**Expert** [00:05:02]
We are using it for semantic search.

We are not using turbopuffer for exact keyword matching.

We are still using OpenSearch, which is our lexical inverted tree thing.

---

**Client** [00:05:13]
Got it.

Is turbopuffer powering the direct answers?

Instead of having just listing five articles, it gives you the right answer to what the customer's asking.

**Expert** [00:05:24]
You're asking, is it powering the semantic search?

---

**Client** [00:05:28]
No. You mentioned that instead of just surfacing the relevant articles, it also provides the right answer to whatever the user is asking.

What's powering that?

**Expert** [00:05:38]
The semantic search is powering that.

Basically, what is happening behind the scene is we are breaking it down into embeds, converting it into vectors, and then that vector is stored in the turbopuffer and then it is using approximate nearest neighbor thing to do the search and then it is finding the relevant vectors and then it is pushing that.

It is using that to power the search.

---

**Client** [00:06:01]
Got it.

Are you guys looking to move exact search onto turbopuffer as well?

**Expert** [00:06:06]
On the exact search, you mean the word moving?

---

**Client** [00:06:09]
Moving off of OpenSearch.

**Expert** [00:06:13]
No, we are not thinking about moving off the search right now.

I think it is working well for us.

---

**Client** [00:06:20]
Got it.

When you say that you're doing the embeddings and the chunking, who's doing that?

Is that turbopuffer or are you using another vendor to do the vector embeddings and the chunking?

**Expert** [00:06:31]
Turbopuffer is doing that for us.

We are not using anything else for that yet.

All the chunking and everything is done on turbopuffer.

---

**Client** [00:06:41]
Got it.

Do you understand the architecture of turbopuffer?

Can you speak a little bit to that or no?

**Expert** [00:06:48]
I can speak a little bit to it.

Do you have a specific question on that?

---

**Client** [00:06:53]
Yeah.

The broader question is more around, there's a lot of vector databases, I'm curious if you have a view on why they are doing better than Pinecone.

Is it built differently than Pinecone?

**Expert** [00:07:04]
I think the biggest competitor, when the evaluation was done on which vector DB to use, Pinecone was the biggest one.

Some of the decision points that we were looking at was recall and latency at the production scale.

They literally tested with the customer data.

We have internal Confluence tenant as well, which is also very big.

They tested it on that.

Pinecone performed better than turbopuffer on that.

The second point was around data residency.

Pinecone, because it is a managed vector DB, we would need to send the data out to Pinecone versus turbopuffer could be self-hosted.

I think this was the point on which turbopuffer won because sending customer data to another third party causes a lot of compliance problems for Atlassian.

They did not want to do that.

The other two points was cost and multi-tenant isolation.

On the cost point also, turbopuffer was really good because it stores everything in the S3, which is really cheap.

If it was just based on quality, Pinecone would have won.

Because Pinecone is managed and it requires us to send the data, that was a completely no to use Pinecone.

---

**Client** [00:08:19]
Is Pinecone also storing everything on S3?

**Expert** [00:08:23]
Pinecone is storing everything in their own cloud.

I don't know how they are actually storing it.

With turbopuffer, we are hosting it on our own AWS cloud and we are storing the vectors on S3.

---

**Client** [00:08:37]
Got it.

How did you guys find them?

What was the process of onboarding look like?

Was it word of mouth?

Was there a salesperson?

What does the implementation look like?

**Expert** [00:08:51]
I think it was just based on what is popular in the industry right now.

I think there were two engineers who did the research.

They were comparing all the popular vector DBs.

I think Pinecone was one, turbopuffer was one, and then they also compared AWS OpenSearch, which is AWS-managed search engine and they also support vectors.

Atlassian has its own search engine as well.

They compared these four options because I think these are the most popular ones in the industry right now.

The fourth one is Atlassian-specific, so not popular in industry, but the other three.

---

**Client** [00:09:28]
I know AWS has an S3 vectors product that's supposed to be the competitor to turbopuffer.

What did you make of that product?

Did you guys evaluate it?

Why did you guys end up choosing turbopuffer over the AWS one?

**Expert** [00:09:44]
With AWS OpenSearch, I think the quality was not up to the par.

The recall, which is how accurately it was able to return the corrected data, I think that was really low compared to Pinecone and turbopuffer.

---

**Client** [00:09:57]
Can you remind me when you guys had run this evaluation?

**Expert** [00:10:01]
Last year, first quarter, January, February.

---

**Client** [00:10:05]
Okay.

Have you guys reevaluated since adopting turbopuffer?

Have you looked at the AWS product since?

**Expert** [00:10:14]
No. I think we are still in the process of there are still few products in Atlassian which has not adopted it completely or are still adopting it.

We are still scaling it up right now.

---

**Client** [00:10:27]
Got it.

If you think about the use cases that you guys are expanding with turbopuffer or, like you mentioned, you guys are having other teams adopting it, what are the other use cases for turbopuffer?

**Expert** [00:10:39]
The other use cases that we are thinking is, with Rovo, it wants to find similar documents to one another, so grouping similar documents.

I think caching is another use case that they are looking into with this.

I think the biggest one is the search right now.

They are thinking what other ways it can be used.

I'm not really sure how every team is using it.

Code search is another one.

Bitbucket is a product that is used.

That is also an Atlassian product.

I think code search is a really big one, where they want to find similar code.

I know Rovo is trying to solve on how they can also include context from past conversations.

Remembering past conversation is another one that they are looking into.

---

**Client** [00:11:27]
What is Rovo?

**Expert** [00:11:29]
Rovo is an Atlassian product, which you can think of as an AI chatbot.

It has visibility into all the other Atlassian products like Jira, Confluence, Trello, Bitbucket.

You can ask it any question and it will look everywhere and then try to answer your question.

---

**Client** [00:11:48]
Got it.

Can you talk a little bit about what are the key strengths and weaknesses of turbopuffer?

**Expert** [00:11:54]
The biggest strength that, I think, was the deciding point is that it can be self-hosted, but the quality, recall, and latency are really good.

The cost at scale is really good, which is you can store everything in S3 and that's really cheap compared to storing everything in memory, which I think some of the other vector DBs are doing.

I'm not really sure on if the team has come across any real weakness for it right now.

I'm sure there are weaknesses, but I think I don't have any visibility into that.

I know why they chose it, but I think there has not been an open discussion around if there are any gaps that they're facing right now.

---

**Client** [00:12:32]
Got it.

Just a broader question would be around, if you take a step back and think about where Atlassian is in your software development life cycle and what your AI infra needs are and where they're headed, do you think turbopuffer is well-positioned as a vendor to serve the key initiatives or products that you guys have or the key priorities that you guys have?

How important is it as an infra vendor?

**Expert** [00:12:56]
You're asking, is there a major initiative around using turbopuffer as the AI search engine and is there a major push for turbopuffer?

---

**Client** [00:13:03]
Sure.

**Expert** [00:13:05]
I think, definitely, because, right now, there is a team that is working exclusively with turbopuffer and they are the team that exclusively manages turbopuffer and then they are also expanding a lot of use cases which will be using turbopuffer, there is a major push for using and expanding turbopuffer across the company.

I know there are other products and other use cases where they are also thinking of onboarding turbopuffer, which they have not yet.

At least I can think of 20%, 30% more increase over the next year.

---

**Client** [00:13:37]
Got it.

How much are you guys spending on turbopuffer today and what did that number look like 12 months ago?

**Expert** [00:13:44]
I think the exact number, it is around low seven figures per year.

---

**Client** [00:13:49]
Got it.

Thank you for taking the time to speak with me.

Have a nice day.
