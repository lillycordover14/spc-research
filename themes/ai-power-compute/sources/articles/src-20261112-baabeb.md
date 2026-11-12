---
id: src-20261112-baabeb
type: article
title: Google’s GKE Labs turns reinforcement learning into a Kubernetes workload
date: '2026-11-12'
added: '2026-11-12'
url: https://siliconangle.com/2026/11/11/model-fine-tuning-kubernetes-google-s-openrl-explained-kubeconna/
publisher: SiliconANGLE AI
author: null
speakers: []
expert_background: null
companies:
- google
people: []
layers: []
tags:
- sweep
summary: ''
key_facts: []
takeaways: []
confidence: med
raw_file: null
hash: baabebeaf49badd0509c11eeb519cb54034965b17fa5ac773790084067199128
word_count: 958
status: unread
added_by: sweep.py
---

[feed snippet]
Model fine-tuning through reinforcement learning is fast becoming one of the most demanding jobs in AI infrastructure. It mixes training, inference and sandboxed agent work in a single loop, often with research code tangled into the systems beneath it. Google LLC has been tackling that problem from inside its Kubernetes engineering group, and recently donated [&#8230;]
The post Google&#8217;s GKE Labs turns reinforcement learning into a Kubernetes workload appeared first on SiliconANGLE.

[page text]
UPDATED 20:51 EST / NOVEMBER 11 2026					

 
AI

Google’s GKE Labs turns reinforcement learning into a Kubernetes workload

																																	by								
Jonathan Anthony

Model fine-tuning through reinforcement learning is fast becoming one of the most demanding jobs in AI infrastructure. It mixes training, inference and sandboxed agent work in a single loop, often with research code tangled into the systems beneath it.

Google LLC has been tackling that problem from inside its Kubernetes engineering group, and recently donated the result, OpenRL, to the 
Cloud Native Computing Foundation
. The GKE Labs team got there by building an AI agent for Kubernetes tasks, then a benchmark to grade models on that work, according to 
Sunil Arora
 (pictured, left), senior software engineer at Google Cloud.

“If you look at reinforcement learning, I think of it as a kind of a super app of AI because it involves training. It involves sampling. It involves agents actually doing things in a sandbox and sometimes kind of evaluating the work,” Arora said. “It’s kind of a very diverse workload and it is, I think, pushing the boundaries of our infrastructure.”

Arora and 
Justin Santa Barbara
 (right), developer at Google, spoke with theCUBE Research’s 
John Furrier
 and 
Rebecca Knight
 at 
KubeCon + CloudNativeCon NA
, during an exclusive broadcast on theCUBE, SiliconANGLE Media’s livestreaming studio. They discussed model fine-tuning and their work in GKE Labs, which puts experimental projects in users’ hands early. 
(* Disclosure below.)

Model fine-tuning without the infrastructure tangle

OpenRL debuted as a 
research preview in June 2026
, offering a self-hosted training API for a company’s own Kubernetes cluster. It splits the reinforcement learning loop from the compute plumbing, so infrastructure engineers handle scaling while researchers keep control of experiments, Arora explained.

“With OpenRL, one of the things that we are trying to do is kind of abstracting away the infrastructure as kind of core primitives so that researchers and AI engineers can just focus on their RL loop,” Arora said.

Sandboxes are where that loop meets agent infrastructure, since calculating rewards can mean running millions of isolated commands. Google’s 
Agent Substrate
 packs more of those sandboxes onto limited compute, according to Arora. For Santa Barbara, the need surfaced one step at a time.

“We built kubectl-ai, and in theory, kubectl-ai could have formatted my hard disk,” Santa Barbara said. “I would quite like a sandbox for this so that if it formats a hard disk, it formats that sandbox and no damage.”

Here’s the complete video interview, part of SiliconANGLE’s and theCUBE’s coverage of 
KubeCon + CloudNativeCon NA
:

(* Disclosure: Google Cloud sponsored this segment of theCUBE. Neither Google Cloud nor other sponsors have editorial control over content on theCUBE or SiliconANGLE.)

Photo: SiliconANGLE

A message from John Furrier, co-founder of SiliconANGLE:

Support our mission to keep content open and free by engaging with theCUBE community. 
Join theCUBE’s Alumni Trust Network
, where technology leaders connect, share intelligence and create opportunities.

15M+ viewers of theCUBE videos
, powering conversations across AI, cloud, cybersecurity and more

11.4k+ theCUBE alumni
 — Connect with more than 11,400 tech and business leaders shaping the future through a unique trusted-based network

Are you an AWS customer?  
Support SiliconANGLE financially by buying your AWS services from our 
Marketplace portal page and links: 
https://siliconangle.com/aws-marketplace/

 

About SiliconANGLE Media

SiliconANGLE Media is a recognized leader in digital media innovation, uniting breakthrough technology, strategic insights and real-time audience engagement. As the parent company of 
SiliconANGLE
, 
theCUBE Network
, 
theCUBE Research
, 
CUBE365
, 
theCUBE AI
 and theCUBE SuperStudios — with flagship locations in Silicon Valley and the New York Stock Exchange — SiliconANGLE Media operates at the intersection of media, technology and AI.

Founded by tech visionaries John Furrier and Dave Vellante, SiliconANGLE Media has built a dynamic ecosystem of industry-leading digital media brands that reach 15+ million elite tech professionals. Our new proprietary theCUBE AI Video Cloud is breaking ground in audience interaction, leveraging theCUBEai.com neural network to help technology companies make data-driven decisions and stay at the forefront of industry conversations.

LATEST STORIES
IBM Quantum and the race to make scientific advantage useful to industry
Agile Robots raises $500M funding led by SoftBank at $8.5B valuation
Vanta launches AI Governance, Risk Quantification and a Vanta Agent for entire jobs
With $23M in funding, Luminal is the latest startup to put Nvidia's CUDA moat in its crosshairs
Computer vision startup Tristar AI pulls in $12.4M to automate quality control for manufacturers
Nvidia CEO Jensen Huang resigns following affairs scandal
LATEST STORIES
IBM Quantum and the race to make scientific advantage useful to industry
EMERGING TECH
 - BY 
DAVE VELLANTE
 . 
1 HOUR AGO
Agile Robots raises $500M funding led by SoftBank at $8.5B valuation
EMERGING TECH
 - BY 
KYT DOTSON
 . 
3 HOURS AGO
Vanta launches AI Governance, Risk Quantification and a Vanta Agent for entire jobs
SECURITY
 - BY 
DUNCAN RILEY
 . 
3 HOURS AGO
With $23M in funding, Luminal is the latest startup to put Nvidia's CUDA moat in its crosshairs
INFRA
 - BY 
MIKE WHEATLEY
 . 
4 HOURS AGO
Computer vision startup Tristar AI pulls in $12.4M to automate quality control for manufacturers
IOT
 - BY 
MIKE WHEATLEY
 . 
4 HOURS AGO
Nvidia CEO Jensen Huang resigns following affairs scandal
POLICY
 - BY 
KYT DOTSON
 . 
4 HOURS AGO
