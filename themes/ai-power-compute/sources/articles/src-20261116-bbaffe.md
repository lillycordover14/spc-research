---
id: src-20261116-bbaffe
type: article
title: Intel & SambaNova Disaggregated Inference at SC26 - CASRAI
date: '2026-11-16'
added: '2026-11-17'
url: https://casrai.org/news/intel-sambanova-d270-sn50-disaggregated-inference-sc26-2026
publisher: CASRAI
author: null
speakers: []
expert_background: null
companies: []
people: []
layers: []
tags:
- sweep
summary: ''
key_facts: []
takeaways: []
confidence: med
raw_file: null
hash: bbaffe117ce453033b8a8a7dce91e1c368098f3964d85ce123b9cdb38ba77bb7
word_count: 1371
status: unread
added_by: sweep.py
---

[feed snippet]
Intel & SambaNova Disaggregated Inference at SC26&nbsp;&nbsp;CASRAI

[page text]
On November 16, 2026, at the SC26 supercomputing conference in Chicago, Intel and SambaNova Systems showcased a live disaggregated AI inference architecture pairing air-cooled Intel GPU D270 accelerators with SambaNova SN50 Reconfigurable Dataflow Units (RDUs). By splitting large language model inference into dedicated GPU prefill and RDU decode tiers connected over standard Ethernet, the system delivers high token throughput for agentic AI workloads without requiring liquid-cooling retrofits in academic and enterprise data centers.

What Happened: Live Demonstration of Disaggregated Heterogeneous Inference at SC26

At the Supercomputing 2026 (SC26) conference in Chicago, running from November 15 to 20, 2026, Intel Corporation and SambaNova Systems demonstrated a heterogeneous, disaggregated artificial intelligence inference system. The live technical showcase executed the GLM-5.3 foundation model across a dual-tier pipeline: four Intel GPU D-Series accelerators handling prompt ingestion and context processing, coupled to a SambaRack SN50 appliance generating autoregressive tokens. The showcase marks the first public deployment combining Intel’s new discrete data center graphics architecture with SambaNova’s dataflow silicon for large language model (LLM) serving.

Rather than running complete inference cycles on a single homogeneous accelerator, the system physically separates model execution into two specialized phases: prompt prefill and token decode. The compute-dense prefill stage processes incoming context in parallel to build the Key-Value (KV) cache, while the memory-bound decode phase generates subsequent output tokens sequentially. Delegating each phase to specialized silicon maximizes accelerator efficiency and lowers total power consumption across institutional 
compute carbon footprint
 profiles.

Architectural Details: D270 Prefill Engine and SambaRack SN50 Decode Fabric

The prefill tier leverages Intel’s discrete GPU D-Series accelerator, codenamed Crescent Island and designated as the Intel GPU D270. Built on the Intel Xe3P architecture, the D270 operates within a 350-watt thermal envelope cooled by ambient airflow in standard dual-slot PCIe 5.0 form factors. Each card features 32 Xe3P cores and 256 Intel Xe Matrix Extensions (XMX) engines, backed by 160 gigabytes (GB) of LPDDR5X memory delivering 1.5 terabytes per second (TB/s) of memory bandwidth, with partner server designs scaling up to 480 GB. In full configurations, an 80-GPU D-Series reference rack provides 208 peak petaflops of FP4 compute and 12 TB to 38 TB of memory capacity with 120 TB/s of aggregate memory bandwidth.

The decode tier uses SambaNova’s fifth-generation SN50 Reconfigurable Dataflow Unit. Fabricated to bypass traditional kernel-launch overheads, the SN50 chains neural network graph operations across reconfigurable compute tiles and on-chip SRAM, streaming tensor values directly between units without repeated trips to external memory. Each SambaRack SN50 integrates 16 SN50 RDUs and draws roughly 20 kilowatts (kW) of typical power during inference. For large agentic workloads, up to 16 SambaRacks can link into a single logical cluster containing 256 RDUs, dispersing memory-bound execution across lower-power air-cooled enclosures.

Table 1: Technical Comparison of Disaggregated Inference Tiers at SC26

Dimension

Prefill Tier (Intel GPU D270)

Decode Tier (SambaRack SN50)

Operational Role

Prompt ingestion and KV-cache creation

Sequential autoregressive token decode

Compute Silicon

32 Xe3P cores, 256 XMX matrix engines

Reconfigurable Dataflow Unit (dataflow tiles)

Power Profile

350 W per card, passive air cooling

~20 kW per 16-RDU rack, standard air cooling

Memory Capacity

160 GB to 480 GB LPDDR5X (1.5 TB/s)

On-chip SRAM, HBM, and attached DDR memory

System Interconnect

Standard PCIe 5.0, RoCEv2 Ethernet

Internal dataflow fabric, RoCEv2 Ethernet

Software Stack

vLLM prefill engine, Dynamo frontend

vLLM decode engine, Dynamo cache routing

Inter-Tier Transport

NIXL over UCX/RDMA via RoCEv2

NIXL over UCX/RDMA via RoCEv2

Software Orchestration: Open Serving With vLLM, NIXL, and NVIDIA Dynamo

To avoid proprietary software lock-in, Intel and SambaNova deployed an open serving stack to coordinate requests across both accelerator types. NVIDIA Dynamo acts as an open-source frontend router configured for context-aware request scheduling. Dynamo tracks incoming prompt structures and routes queries to accelerator nodes holding matching prefix caches. The core execution engine uses vLLM, running kernel paths optimized for Intel D270 GPUs during prefill and handing off intermediate representations to vLLM execution targets on SambaNova RDUs during decode.

Transfer of the active KV cache between the Intel prefill tier and SambaNova decode tier relies on NIXL (Node-to-Node Inference Exchange Layer). Running over unified communication X (UCX) with Remote Direct Memory Access (RDMA) over Converged Ethernet (RoCEv2), NIXL moves tensor state across standard network fabrics without host CPU memory copies. In addition, the SN50 preserves common system prompt prefixes in high-capacity attached DDR memory. When an autonomous agent revisits a shared conversation prefix or code repository context, Dynamo routes the query directly to the SN50 node holding that cached state. The Intel GPU computes only incremental context tokens, reducing network traffic and latency to first token (TTFT).

Industry Context and Brownfield Data Center Constraints

The SC26 showcase addresses mounting infrastructure bottlenecks across enterprise clouds and academic high-performance computing centers. Clean-tech research from Sightline Climate indicates that nearly half of data center projects planned for 2026 face delays due to electric grid interconnection queues, transformer shortages, and municipal zoning disputes. As a result, facilities must expand AI serving capacity within existing brownfield data centers engineered for air-cooled rack densities between 15 kW and 25 kW.

Modern monolithic GPU clusters drawing 100 kW to 130 kW per liquid-cooled rack often require multimillion-dollar facility retrofits. The Intel-SambaNova architecture avoids facility modifications by keeping accelerator power within standard air convection boundaries. This deployment follows SambaNova’s earlier partnership integrating SN50 RDUs with NVIDIA systems, reported in 
Supermicro and SambaNova’s 10,000-chip deployment
, while broadening the disaggregated model to Intel’s discrete accelerator lineup.

Stakeholder Reaction and Independent Industry Analysis

Semiconductor analysts highlighted the significance of combining merchant graphics processors with specialized dataflow silicon. Igor Wallossek of Igor’s Lab observed that Intel’s SC26 strategy emphasizes modular heterogeneous systems rather than serving every workload through a single monolithic processor. Wallossek reported that by pairing Xeon 6 host CPUs with GPU D-Series accelerators and open software, Intel offers research centers an alternative to proprietary platforms, though he noted that comprehensive performance figures remain manufacturer claims subject to independent verification.

Analysis from Unite.AI and Superpower Daily emphasized that while the GLM-5.3 demonstration verified live functional interoperability and automated KV-cache transfers across RoCEv2 fabrics, the partners published no audited benchmarks comparing cost-per-token or end-to-end latency against monolithic hyperscale setups. Industry observers noted that real-world economic advantages depend on whether production workloads achieve sufficient prefix cache hit rates to offset inter-chassis network transfer overheads.

Implications for University Research Facilities and Campus Supercomputing

For university research computing directors and academic supercomputing facilities, air-cooled disaggregated architectures provide immediate operational benefits. Academic institutions operating within 
national data infrastructure
 networks face fixed power ceilings across campus server rooms. Because prefill and decode resources sit in separate modular enclosures, system administrators can scale compute-heavy D270 cards for large researcher datasets or scale SN50 dataflow capacity for campus agentic coding assistants without overprovisioning entire server clusters.

The architecture also supports grant procurement and institutional sustainability goals. Standardized metrics like 
compute FLOPs estimates
 and open-source software stacks (vLLM and UCX) help universities maintain compliance and avoid single-vendor capture. Academic consortia advancing 
federated data infrastructure
 can integrate PCIe D270 cards into existing chassis while networking specialized inference appliances across campus Ethernet backbones, preserving capital budgets and providing local access to foundation models.

What Happens Next: Deployments, Evaluations, and Benchmarks

Intel and SambaNova are presenting live technical demonstrations in Chicago through November 20, 2026, at SambaNova booth 2246 and Intel booth 2819. The companies plan to release production software configurations to early-access enterprise clouds and research computing centers in the first quarter of 2027.

Subsequent deliverables include audited MLPerf Inference benchmarks measuring throughput-per-watt and cost-per-token on disaggregated GLM-5.3 and Llama architectures. Academic supercomputing centers are scheduled to begin pilot testbed evaluations in early 2027 to measure prefix cache hit ratios and multi-tenant reliability under continuous campus workloads.

Sources

SambaNova Systems: The Air-Cooled Token Factory: Intel GPU D-Series + SambaRack SN50
, checked 2026-11-16

Unite.AI: SambaNova Pairs Intel GPUs with SN50 for Air-Cooled AI Inference
, checked 2026-11-16

Superpower Daily: SambaNova pairs Intel GPUs with its AI chips in an air-cooled inference demo
, checked 2026-11-16

Igor’s Lab: Intel outlines the next HPC step: Xeon, GPU D-Series and open software
, checked 2026-11-16

Intel Corporation: Why Intel GPU D270 Belongs in the HPC Conversation
, checked 2026-11-16
