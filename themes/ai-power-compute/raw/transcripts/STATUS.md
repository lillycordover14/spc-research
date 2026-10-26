# Podcast/video transcript status (apc)

All free: publisher transcripts first, else YouTube auto captions (en-orig) via yt-dlp, else public RSS/enclosure audio transcribed locally with faster-whisper (small.en). No paid APIs, no paywalled audio, no AlphaSense. Audio stays out of git. One row per item; the transcript is the source body.

| id | method | status | words | note |
|---|---|---|---|---|
| src-20260826-03722b | publisher transcript (volts.wtf) | done | 21700 | Volts: Varun Sivaram (Emerald AI) on flexible data centers |
| src-20260803-db2641 | publisher transcript (latent.space) | done | 22000 | Latent Space: Inference Engineering Masterclass, Baseten |
| src-20260825-e500eb | YouTube auto captions (en-orig) via yt-dlp | done | 12189 | AGI House: Neil Movva, Sail Research (IJLZXnC2_-E) |
| src-20260723-741ec4 | YouTube auto captions (en-orig) via yt-dlp | done | 3729 | RAISE Summit: Zain Asgar, Gimlet, with Sid Sheth, d-Matrix (BFSAASFGuIo) |
| src-20260929-f57402 | YouTube auto captions (en-orig) via yt-dlp | done | 2057 | Altimeter First Pass Ep 10: Yash Patil, Applied Compute (QKNFBwsHo0s) |
| src-20251201-8903ad | YouTube auto captions (en-orig) via yt-dlp | done | 1905 | Slush 2025: Julien Launay, Adaptive ML (iehLFYvqvow) |
| src-20260805-572c12 | YouTube auto captions (en-orig) via yt-dlp | done | 6353 | Crux Climate: Varun Sivaram (zUhTzdcliUE) |
| src-20260326-771e89 | YouTube auto captions (en-orig) via yt-dlp | done | 13546 | Volts: Astrid Atkinson and Jesse Jenkins (UyKZpcCWU_c) |
| src-20250508-1afa13 | YouTube auto captions (en-orig) via yt-dlp | done | 11359 | Texas Energy & Power: Tyler Norris (0YXQsqNBL8Q) |
| src-20251202-9b5fb9 | RSS audio + faster-whisper small.en | done | 8942 | TWIML 757: Zain Asgar, Gimlet (YouTube GI0hWajiPaM blocked; no publisher transcript on twimlai.com) |
| src-20260501-1f0aeb | RSS audio + faster-whisper small.en | done | 6788 | No Priors: Tuhin Srivastava, Baseten (YouTube XAbKflCncDo blocked) |
| src-20261006-ba3eb2 | RSS audio + faster-whisper small.en | done | 10931 | Unsupervised Learning Ep 94: Applied Compute CEO (YouTube QeiYSLBCwD4 blocked) |
| yt:dcYqyhyS1o0 | YouTube auto captions | skipped | 9788 | Duplicate of Volts Sivaram episode; publisher transcript used instead |
| yt:FeS1th1Jz8A | yt-dlp captions (android/tv/web_safari) or RSS audio + faster-whisper | blocked | 0 | Sapphire, Gimlet: Run 3 retry: android client 429 on captions, tv/web_safari/ios/mweb bot-check, audio "page needs to be reloaded"; no cookies used |
| yt:2w-I4pASBDA | yt-dlp captions (android/tv/web_safari) or RSS audio + faster-whisper | done | 13696 | Cat Tang, Sail: Run 3: captions via yt-dlp android client, no login [src-20261016-e74533] |
| yt:Gpjr-PlehnQ | yt-dlp captions (android/tv/web_safari) or RSS audio + faster-whisper | done | 4449 | AI Council, Sail: Run 3: captions via android client [src-20260621-ed3bd8] |
| yt:o15AaYl7Wu0 | yt-dlp captions (android/tv/web_safari) or RSS audio + faster-whisper | done | 3966 | AI Engineer, Applied Compute: Run 3: captions via android client [src-20251209-40997e] |
| yt:E1FjgufU9qg | yt-dlp captions (android/tv/web_safari) or RSS audio + faster-whisper | done | 7660 | Simplismart: Run 3: captions via android client [src-20241024-c3f2ca] |
| yt:nDr6cZtnOY0 | yt-dlp captions (android/tv/web_safari) or RSS audio + faster-whisper | covered | 4630 | SeedToScale, Simplismart: Run 3: YouTube still blocked (429); same SeedToScale episode transcribed from RSS audio with faster-whisper [src-20250905-9d3aa9] |
| yt:8YeiI8L0ssE | yt-dlp captions (android/tv/web_safari) or RSS audio + faster-whisper | done | 3222 | Algorithmic Voice, Deep Cogito: Run 3: captions via android client; third-party explainer, low value [src-20250409-71ca9a] |
| yt:lQlO5Cb6_n8 | yt-dlp captions (android/tv/web_safari) or RSS audio + faster-whisper | covered | 0 | CERAWeek, Emerald: Run 3: YouTube still blocked; CERAWeek Podcast with Sivaram transcribed from RSS audio [src-20260114-9f862d] |
| yt:xAO3eh9hOMk | yt-dlp captions (android/tv/web_safari) or RSS audio + faster-whisper | done | 4781 | BCG, Emerald: Run 3: captions via android client [src-20261016-b16630] |
| yt:t0F6vzJhKH0 | yt-dlp captions (android/tv/web_safari) or RSS audio + faster-whisper | blocked | 0 | IQT, Emerald: Run 3: android 429 on captions; other clients bot-check; no RSS alternative found |
| yt:yd3a4cYINzk | yt-dlp captions (android/tv/web_safari) or RSS audio + faster-whisper | blocked | 0 | Energy Empire, GridCARE: Run 3: android 429 on captions; GridCARE covered by Clean Energy Today RSS audio [src-20260920-7822a2] |
| yt:OcxupZZsGj0 | YouTube auto captions via yt-dlp | pending | 0 | Data Center Richness, GridCARE: YouTube bot-check / HTTP 429 after retries with backoff; no free transcript found yet; run 3 spaced retry still queued at report time |
| yt:XGS3Hs_Rk14 | YouTube auto captions via yt-dlp | pending | 0 | Sources, Baseten: YouTube bot-check / HTTP 429 after retries with backoff; no free transcript found yet; run 3 spaced retry still queued at report time |
| yt:7PSXtru6mmY | YouTube auto captions via yt-dlp | pending | 0 | Latent Space video, Baseten (publisher transcript used): YouTube bot-check / HTTP 429 after retries with backoff; no free transcript found yet; run 3 spaced retry still queued at report time |
| yt:p6R_EeLheA4 | YouTube auto captions via yt-dlp | pending | 0 | vLLM / llm-d, Rob Shaw: YouTube bot-check / HTTP 429 after retries with backoff; no free transcript found yet; run 3 spaced retry still queued at report time |
| yt:cvNO9pZAhM0 | YouTube auto captions via yt-dlp | pending | 0 | Odd Lots, data center financing: YouTube bot-check / HTTP 429 after retries with backoff; no free transcript found yet; run 3 spaced retry still queued at report time |
| yt:OcxupZZsGj0 | yt-dlp android captions | filed | 4304 | GridCARE Data Center Richness |
