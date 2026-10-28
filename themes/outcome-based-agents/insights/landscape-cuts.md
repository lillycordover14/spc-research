# Landscape cuts: outcome-based agents (built 2026-10-27, grokbot)

Modeled on ai-native-industrial-production/insights/cross-sector-map.md: an inclusion test, one primary home per company per cut, a source id on every row, incumbents kept as context. Full reference; primer Section 8 carries the short version.

**Inclusion test.** A startup (private, Seed to late stage) that sells AI agents doing enterprise work, or the tools that run them. Sources: every company card in companies/, insights/startup-landscape.md (47 startups), companies/_candidates.md, and the sources/ records cited. 65 startups placed. Incumbents, labs and SIs are listed once in Cut 1 as context and not placed in Cuts 2 to 6.

**Rules.** Each startup sits in exactly one group per cut. Secondary fit is noted below a table only where it changes the read. Pricing and stage come only from a filed source; anything else is "not disclosed". Funding press releases and company pages are company claims. Cut 6 (thesis position) is my read: [inference].

## Cut 1. The five worlds

Incumbents by world (context):

| World | Companies | Src |
|---|---|---|
| Labs and hyperscalers | OpenAI, Anthropic, Google, Microsoft, Amazon Web Services | companies/openai.md, anthropic.md, google.md, microsoft.md, aws.md |
| Systems of record | Salesforce, ServiceNow, SAP, Oracle, Workday, Intuit, Atlassian, Box, Celonis, Thomson Reuters, Adobe, HubSpot | company cards |
| CX platforms (systems of record for service) | Zendesk, Intercom (Fin), NiCE, Genesys, Five9, Freshworks | company cards |
| Automation incumbents (enterprises build their own on these) | UiPath, Automation Anywhere, Pegasystems, IBM, Palantir | company cards |
| SIs and BPOs | Accenture, Deloitte, Cognizant, Infosys, TCS, Capgemini, Genpact, EXL, Concentrix, Teleperformance, TaskUs | company cards |

Startups by world:

| World | n | Companies (source) |
|---|---|---|
| Vertical apps | 39 | Actively AI [src-20260428-2d177a]; Attention [src-20260624-c59112]; Vida [src-20261008-fb6a3d]; Sierra [src-20260710-37d40b]; Decagon [src-20260515-de88a1]; Omilia [src-20260806-53e2bf]; respond.io [src-20260616-8a0be8]; Cresta [src-20260618-f36dc6]; Moveworks [src-20260402-8d84cb]; Adaptive [src-20260917-e6c847]; Basis [src-20260224-b6a4eb]; Definite [src-20261023-12e7f6]; Elimentary [src-20261023-c1d343]; Xelix [src-20250721-54e512]; Zolvo [src-20261023-d2a134]; Zomma [src-20261023-36cc4e]; Didero [src-20260212-5fd1e0]; Lio [src-20260305-fefcb3]; Magentic [src-20260917-25441c]; Walter [src-20261023-aee4fa]; Pactum [src-20260617-937cc1]; Pavus AI [src-20260617-937cc1]; Adonis [src-20260325-9a969a]; Amperos Health [src-20260422-d6ae9d]; Candid Health [src-20260722-e6a1e0]; GenHealth.ai [src-20261008-50f3eb]; Procode [src-20260728-5c2f73]; Prosper AI [src-20261023-cc2e6e]; ClearRisk AI [src-20260513-fb476a]; Notch [src-20260325-5584af]; Pace [src-20260527-cecfde]; Crosby [src-20260331-50e583]; Ivo [src-20260120-667118]; Wordsmith [src-20260603-a6ea11]; Orbio [src-20260614-1eab1f]; Spott [src-20260922-e2fd03]; Take2 [src-20260211-adbf96]; NeuBird AI [src-20260407-8cfa16]; Crescendo [src-20260724-865e53] |
| Horizontal orchestration and work context | 9 | Ema [src-20260930-9ee545]; Kestra [src-20260331-83a5c4]; Duvo [src-20260609-4b024f]; Sycamore [src-20260404-029771]; Airia [src-20260330-8d6266]; Maisa AI [src-20260330-8d6266]; Mimica [src-20250924-c1a4cf]; Skan AI [src-20260812-4cb1fc]; Workfabric AI [src-20261023-21a6d6] |
| SIs, BPOs and AI services | 4 | DeepOpinion [src-20250627-297f7b]; Otera [src-20260724-b4a442]; RapidCanvas [src-20261016-425bfa]; AuxoAI [src-20261022-d5ad54] |
| Agent infrastructure and tools | 13 | CopilotKit [src-20260505-826992]; Coval [src-20260624-2cae61]; Dash0 [src-20260323-e76c06]; Daytona [src-20261023-3f4b4a]; Flexprice [src-20260802-db6422]; InsightFinder [src-20260416-dfa630]; Natural [src-20260720-e50556]; Raindrop [src-20260917-29a2db]; Rein [src-20261008-418b1c]; Runlayer [src-20260624-0c6e18]; Tsuga [src-20260623-e97988]; LangChain [src-20261021-16f218]; ElevenLabs [src-20260310-e66bf3] |

No startup sits in "enterprises building their own"; that world is served by the labs, the automation incumbents and the SIs. Secondary: Moveworks, Didero, Magentic, Walter and GenHealth.ai are vertical apps that also lean on a system of record (see Cut 4).

**What this means:** the venture-backed money is in vertical apps; the other four worlds are mostly incumbents, so startup risk there is being absorbed rather than out-competed.

## Cut 2. Buyer function

Who signs. One function per company, by the workflow named in its source.

| Group | n | Companies (source) |
|---|---|---|
| Customer service and contact center | 7 | ElevenLabs [src-20260310-e66bf3]; Sierra [src-20260710-37d40b]; Decagon [src-20260515-de88a1]; Omilia [src-20260806-53e2bf]; respond.io [src-20260616-8a0be8]; Cresta [src-20260618-f36dc6]; Crescendo [src-20260724-865e53] |
| Sales and revenue | 3 | Actively AI [src-20260428-2d177a]; Attention [src-20260624-c59112]; Vida [src-20261008-fb6a3d] |
| Finance, accounting and lending ops | 7 | Adaptive [src-20260917-e6c847]; Basis [src-20260224-b6a4eb]; Definite [src-20261023-12e7f6]; Elimentary [src-20261023-c1d343]; Xelix [src-20250721-54e512]; Zolvo [src-20261023-d2a134]; Zomma [src-20261023-36cc4e] |
| Procurement and supply chain | 6 | Didero [src-20260212-5fd1e0]; Lio [src-20260305-fefcb3]; Magentic [src-20260917-25441c]; Walter [src-20261023-aee4fa]; Pactum [src-20260617-937cc1]; Pavus AI [src-20260617-937cc1] |
| Healthcare revenue cycle and admin | 6 | Adonis [src-20260325-9a969a]; Amperos Health [src-20260422-d6ae9d]; Candid Health [src-20260722-e6a1e0]; GenHealth.ai [src-20261008-50f3eb]; Procode [src-20260728-5c2f73]; Prosper AI [src-20261023-cc2e6e] |
| Insurance and regulated ops | 5 | DeepOpinion [src-20250627-297f7b]; ClearRisk AI [src-20260513-fb476a]; Notch [src-20260325-5584af]; Pace [src-20260527-cecfde]; Otera [src-20260724-b4a442] |
| Legal | 3 | Crosby [src-20260331-50e583]; Ivo [src-20260120-667118]; Wordsmith [src-20260603-a6ea11] |
| HR and recruiting | 3 | Orbio [src-20260614-1eab1f]; Spott [src-20260922-e2fd03]; Take2 [src-20260211-adbf96] |
| IT ops and agent infrastructure (sold to engineering) | 14 | CopilotKit [src-20260505-826992]; Coval [src-20260624-2cae61]; Dash0 [src-20260323-e76c06]; Daytona [src-20261023-3f4b4a]; Flexprice [src-20260802-db6422]; InsightFinder [src-20260416-dfa630]; Natural [src-20260720-e50556]; Raindrop [src-20260917-29a2db]; Rein [src-20261008-418b1c]; Runlayer [src-20260624-0c6e18]; Tsuga [src-20260623-e97988]; LangChain [src-20261021-16f218]; Moveworks [src-20260402-8d84cb]; NeuBird AI [src-20260407-8cfa16] |
| Cross-function (no single buyer) | 11 | Ema [src-20260930-9ee545]; Kestra [src-20260331-83a5c4]; Duvo [src-20260609-4b024f]; Sycamore [src-20260404-029771]; Airia [src-20260330-8d6266]; Maisa AI [src-20260330-8d6266]; Mimica [src-20250924-c1a4cf]; Skan AI [src-20260812-4cb1fc]; Workfabric AI [src-20261023-21a6d6]; RapidCanvas [src-20261016-425bfa]; AuxoAI [src-20261022-d5ad54] |

**What this means:** Customer service is crowded and priced openly; finance, procurement, healthcare billing and insurance hold most of the early-stage picks, where buyers are less tested.

## Cut 3. Pricing model

From a filed source only. Sierra: under $2 per transaction, with about 10% of savings as a secondary term [src-20260710-37d40b]. Decagon: per meaningful conversation [src-20260515-de88a1]. Crescendo: per contact [src-20260724-865e53]. Cresta: mainly per minute, some outcome charging [src-20260618-f36dc6]. Duvo: per run, at a related-party customer [src-20260609-4b024f]. DeepOpinion: per task credits [src-20250627-297f7b]. Ema, Crosby, Procode, Vida: outcome pricing per their own announcements (company claims). Sycamore is unknown: its CEO says pricing is moving toward outcome [src-20260404-029771].

| Group | n | Companies (source) |
|---|---|---|
| Per outcome or savings share | 4 | Ema [src-20260930-9ee545]; Vida [src-20261008-fb6a3d]; Procode [src-20260728-5c2f73]; Crosby [src-20260331-50e583] |
| Per transaction, task, conversation or run | 5 | Duvo [src-20260609-4b024f]; DeepOpinion [src-20250627-297f7b]; Sierra [src-20260710-37d40b]; Decagon [src-20260515-de88a1]; Crescendo [src-20260724-865e53] |
| Hybrid (part outcome, part usage) | 1 | Prosper AI [src-20261023-cc2e6e] |
| Usage (minutes, GB, cloud consumption) | 3 | Tsuga [src-20260623-e97988]; Kestra [src-20260331-83a5c4]; Cresta [src-20260618-f36dc6] |
| Subscription or seat | 1 | RapidCanvas [src-20261016-425bfa] |
| Not disclosed in any filed source | 51 | CopilotKit [src-20260505-826992]; Coval [src-20260624-2cae61]; Dash0 [src-20260323-e76c06]; Daytona [src-20261023-3f4b4a]; Flexprice [src-20260802-db6422]; InsightFinder [src-20260416-dfa630]; Natural [src-20260720-e50556]; Raindrop [src-20260917-29a2db]; Rein [src-20261008-418b1c]; Runlayer [src-20260624-0c6e18]; LangChain [src-20261021-16f218]; ElevenLabs [src-20260310-e66bf3]; Sycamore [src-20260404-029771]; Airia [src-20260330-8d6266]; Maisa AI [src-20260330-8d6266]; Mimica [src-20250924-c1a4cf]; Skan AI [src-20260812-4cb1fc]; Workfabric AI [src-20261023-21a6d6]; Actively AI [src-20260428-2d177a]; Attention [src-20260624-c59112]; Omilia [src-20260806-53e2bf]; respond.io [src-20260616-8a0be8]; Moveworks [src-20260402-8d84cb]; Adaptive [src-20260917-e6c847]; Basis [src-20260224-b6a4eb]; Definite [src-20261023-12e7f6]; Elimentary [src-20261023-c1d343]; Xelix [src-20250721-54e512]; Zolvo [src-20261023-d2a134]; Zomma [src-20261023-36cc4e]; Didero [src-20260212-5fd1e0]; Lio [src-20260305-fefcb3]; Magentic [src-20260917-25441c]; Walter [src-20261023-aee4fa]; Pactum [src-20260617-937cc1]; Pavus AI [src-20260617-937cc1]; Adonis [src-20260325-9a969a]; Amperos Health [src-20260422-d6ae9d]; Candid Health [src-20260722-e6a1e0]; GenHealth.ai [src-20261008-50f3eb]; ClearRisk AI [src-20260513-fb476a]; Notch [src-20260325-5584af]; Pace [src-20260527-cecfde]; Otera [src-20260724-b4a442]; Ivo [src-20260120-667118]; Wordsmith [src-20260603-a6ea11]; Orbio [src-20260614-1eab1f]; Spott [src-20260922-e2fd03]; Take2 [src-20260211-adbf96]; NeuBird AI [src-20260407-8cfa16]; AuxoAI [src-20261022-d5ad54] |

**What this means:** Most startups have no disclosed price. Where a price is on the record, it is per transaction, not a share of savings; only four claim true outcome pricing, all in their own releases.

## Cut 4. Go-to-market and deployment channel

How the product reaches the work. Didero, GenHealth.ai, Walter and Moveworks are placed under system of record because their sources say they run inside existing systems; Moveworks ownership status is unverified [src-20260402-8d84cb]. Otera, DeepOpinion and Workfabric have Cognizant as partner; Vida sells via channel [src-20261008-fb6a3d].

| Group | n | Companies (source) |
|---|---|---|
| Direct to the enterprise (no partner named in sources) | 45 | Coval [src-20260624-2cae61]; Dash0 [src-20260323-e76c06]; Daytona [src-20261023-3f4b4a]; InsightFinder [src-20260416-dfa630]; Natural [src-20260720-e50556]; Raindrop [src-20260917-29a2db]; Rein [src-20261008-418b1c]; Runlayer [src-20260624-0c6e18]; Tsuga [src-20260623-e97988]; ElevenLabs [src-20260310-e66bf3]; Ema [src-20260930-9ee545]; Duvo [src-20260609-4b024f]; Sycamore [src-20260404-029771]; Airia [src-20260330-8d6266]; Maisa AI [src-20260330-8d6266]; Mimica [src-20250924-c1a4cf]; Skan AI [src-20260812-4cb1fc]; Actively AI [src-20260428-2d177a]; Attention [src-20260624-c59112]; Sierra [src-20260710-37d40b]; Decagon [src-20260515-de88a1]; Omilia [src-20260806-53e2bf]; respond.io [src-20260616-8a0be8]; Cresta [src-20260618-f36dc6]; Adaptive [src-20260917-e6c847]; Basis [src-20260224-b6a4eb]; Definite [src-20261023-12e7f6]; Elimentary [src-20261023-c1d343]; Xelix [src-20250721-54e512]; Zolvo [src-20261023-d2a134]; Zomma [src-20261023-36cc4e]; Lio [src-20260305-fefcb3]; Pactum [src-20260617-937cc1]; Pavus AI [src-20260617-937cc1]; Adonis [src-20260325-9a969a]; Amperos Health [src-20260422-d6ae9d]; Candid Health [src-20260722-e6a1e0]; ClearRisk AI [src-20260513-fb476a]; Notch [src-20260325-5584af]; Ivo [src-20260120-667118]; Wordsmith [src-20260603-a6ea11]; Orbio [src-20260614-1eab1f]; Spott [src-20260922-e2fd03]; Take2 [src-20260211-adbf96]; NeuBird AI [src-20260407-8cfa16] |
| Runs inside or on top of a system of record (SAP, Oracle, ServiceNow, existing EHR or email) | 5 | Moveworks [src-20260402-8d84cb]; Didero [src-20260212-5fd1e0]; Magentic [src-20260917-25441c]; Walter [src-20261023-aee4fa]; GenHealth.ai [src-20261008-50f3eb] |
| Sold or delivered through an SI, BPO or channel partner | 4 | DeepOpinion [src-20250627-297f7b]; Workfabric AI [src-20261023-21a6d6]; Vida [src-20261008-fb6a3d]; Otera [src-20260724-b4a442] |
| Sells the finished work (AI-native service firm or BPO replacement) | 7 | Procode [src-20260728-5c2f73]; Prosper AI [src-20261023-cc2e6e]; Pace [src-20260527-cecfde]; Crosby [src-20260331-50e583]; Crescendo [src-20260724-865e53]; RapidCanvas [src-20261016-425bfa]; AuxoAI [src-20261022-d5ad54] |
| Open source or developer-led | 4 | CopilotKit [src-20260505-826992]; Flexprice [src-20260802-db6422]; LangChain [src-20261021-16f218]; Kestra [src-20260331-83a5c4] |

**What this means:** Direct sale dominates. Only four startups ride an SI or channel on the record, so "SIs as channel" is still thin evidence at the startup level.

## Cut 5. Stage

Latest round in the filed source. Sierra placed late on its $950M raise at over $15B [src-20260504-c9d184]. Decagon, Crescendo, Cresta, LangChain and ElevenLabs have no stage in filed sources.

| Group | n | Companies (source) |
|---|---|---|
| Seed | 7 | Flexprice [src-20260802-db6422]; Sycamore [src-20260404-029771]; Definite [src-20261023-12e7f6]; Elimentary [src-20261023-c1d343]; Zolvo [src-20261023-d2a134]; Zomma [src-20261023-36cc4e]; Walter [src-20261023-aee4fa] |
| Series A | 22 | CopilotKit [src-20260505-826992]; Coval [src-20260624-2cae61]; Natural [src-20260720-e50556]; Raindrop [src-20260917-29a2db]; Rein [src-20261008-418b1c]; Runlayer [src-20260624-0c6e18]; Tsuga [src-20260623-e97988]; Kestra [src-20260331-83a5c4]; Duvo [src-20260609-4b024f]; Didero [src-20260212-5fd1e0]; Lio [src-20260305-fefcb3]; Magentic [src-20260917-25441c]; Amperos Health [src-20260422-d6ae9d]; GenHealth.ai [src-20261008-50f3eb]; Procode [src-20260728-5c2f73]; ClearRisk AI [src-20260513-fb476a]; Notch [src-20260325-5584af]; Otera [src-20260724-b4a442]; Orbio [src-20260614-1eab1f]; Spott [src-20260922-e2fd03]; Take2 [src-20260211-adbf96]; AuxoAI [src-20261022-d5ad54] |
| Series B | 18 | Dash0 [src-20260323-e76c06]; Daytona [src-20261023-3f4b4a]; InsightFinder [src-20260416-dfa630]; Ema [src-20260930-9ee545]; Mimica [src-20250924-c1a4cf]; Actively AI [src-20260428-2d177a]; Attention [src-20260624-c59112]; Omilia [src-20260806-53e2bf]; respond.io [src-20260616-8a0be8]; Adaptive [src-20260917-e6c847]; Basis [src-20260224-b6a4eb]; Xelix [src-20250721-54e512]; Pace [src-20260527-cecfde]; Crosby [src-20260331-50e583]; Ivo [src-20260120-667118]; Wordsmith [src-20260603-a6ea11]; NeuBird AI [src-20260407-8cfa16]; RapidCanvas [src-20261016-425bfa] |
| Series C | 2 | Skan AI [src-20260812-4cb1fc]; Adonis [src-20260325-9a969a] |
| Series D or later / late private | 2 | Sierra [src-20260710-37d40b]; Candid Health [src-20260722-e6a1e0] |
| Stage not in filed sources | 14 | LangChain [src-20261021-16f218]; ElevenLabs [src-20260310-e66bf3]; Airia [src-20260330-8d6266]; Maisa AI [src-20260330-8d6266]; DeepOpinion [src-20250627-297f7b]; Workfabric AI [src-20261023-21a6d6]; Vida [src-20261008-fb6a3d]; Decagon [src-20260515-de88a1]; Cresta [src-20260618-f36dc6]; Moveworks [src-20260402-8d84cb]; Pactum [src-20260617-937cc1]; Pavus AI [src-20260617-937cc1]; Prosper AI [src-20261023-cc2e6e]; Crescendo [src-20260724-865e53] |

**What this means:** Series A and B carry most of the universe; the late names are CX leaders, which sets price bars the vertical Series B picks will be compared to.

## Cut 6. Thesis position

[inference] Against the thesis: vertical apps and systems of record win, SIs as channel.

| Group | n | Companies (source) |
|---|---|---|
| Fits: vertical app that owns a workflow | 29 | Actively AI [src-20260428-2d177a]; Attention [src-20260624-c59112]; Vida [src-20261008-fb6a3d]; Sierra [src-20260710-37d40b]; Decagon [src-20260515-de88a1]; Omilia [src-20260806-53e2bf]; respond.io [src-20260616-8a0be8]; Cresta [src-20260618-f36dc6]; Adaptive [src-20260917-e6c847]; Basis [src-20260224-b6a4eb]; Definite [src-20261023-12e7f6]; Elimentary [src-20261023-c1d343]; Xelix [src-20250721-54e512]; Zolvo [src-20261023-d2a134]; Zomma [src-20261023-36cc4e]; Lio [src-20260305-fefcb3]; Pactum [src-20260617-937cc1]; Pavus AI [src-20260617-937cc1]; Adonis [src-20260325-9a969a]; Amperos Health [src-20260422-d6ae9d]; Candid Health [src-20260722-e6a1e0]; ClearRisk AI [src-20260513-fb476a]; Notch [src-20260325-5584af]; Ivo [src-20260120-667118]; Wordsmith [src-20260603-a6ea11]; Orbio [src-20260614-1eab1f]; Spott [src-20260922-e2fd03]; Take2 [src-20260211-adbf96]; NeuBird AI [src-20260407-8cfa16] |
| Fits: rides on the system of record | 5 | Moveworks [src-20260402-8d84cb]; Didero [src-20260212-5fd1e0]; Magentic [src-20260917-25441c]; Walter [src-20261023-aee4fa]; GenHealth.ai [src-20261008-50f3eb] |
| Fits: sells the outcome as a service | 5 | Procode [src-20260728-5c2f73]; Prosper AI [src-20261023-cc2e6e]; Pace [src-20260527-cecfde]; Crosby [src-20260331-50e583]; Crescendo [src-20260724-865e53] |
| Channel: SI, BPO or managed service | 4 | DeepOpinion [src-20250627-297f7b]; Otera [src-20260724-b4a442]; RapidCanvas [src-20261016-425bfa]; AuxoAI [src-20261022-d5ad54] |
| Exposed: horizontal orchestration or context | 9 | Ema [src-20260930-9ee545]; Kestra [src-20260331-83a5c4]; Duvo [src-20260609-4b024f]; Sycamore [src-20260404-029771]; Airia [src-20260330-8d6266]; Maisa AI [src-20260330-8d6266]; Mimica [src-20250924-c1a4cf]; Skan AI [src-20260812-4cb1fc]; Workfabric AI [src-20261023-21a6d6] |
| Neutral: picks and shovels (infra, evals, security) | 13 | CopilotKit [src-20260505-826992]; Coval [src-20260624-2cae61]; Dash0 [src-20260323-e76c06]; Daytona [src-20261023-3f4b4a]; Flexprice [src-20260802-db6422]; InsightFinder [src-20260416-dfa630]; Natural [src-20260720-e50556]; Raindrop [src-20260917-29a2db]; Rein [src-20261008-418b1c]; Runlayer [src-20260624-0c6e18]; Tsuga [src-20260623-e97988]; LangChain [src-20261021-16f218]; ElevenLabs [src-20260310-e66bf3] |

**What this means:** Six in ten startups fit the thesis directly; the exposed horizontal group is where lab and system-of-record absorption risk is highest.

## Sharpest observations
- [inference] Outcome pricing at the startup level is mostly a press-release claim (Ema, Crosby, Procode, Vida). Every buyer-verified price on file is per transaction (Sierra, Decagon, Crescendo, Duvo, DeepOpinion).
- [inference] The thesis-fit picks cluster in finance, procurement, healthcare billing and insurance, not CX. CX is already a late-stage price war (Sierra, Decagon, Fin).
- [inference] "Sells the finished work" (Pace, Crosby, Procode, Prosper AI, Crescendo) is a distinct group: they price the job, not the software, and Crescendo's margin fell under that model [src-20260724-865e53].
- [inference] SI-delivered startups (Otera, DeepOpinion, Workfabric) all run through Cognizant. One SI is the whole channel evidence.
- Fourteen of 65 startups have no disclosed stage, and 51 have no disclosed price; those rows need an expert call or a pricing page.

## Not placed
Named in market maps but not filed as startups, so not placed: Temporal, Inngest, Restate, Braintrust, Helicone, AgentOps, LiteLLM, Portkey [src-20260515-76034a]; Giga, PolyAI [src-20260226-87dd95]. Unverified: Stuut, Judgment Labs, Orkes.
