---
name: ledger-l2-ml-07-match
description: "Ledger match (fixture L2 with ML-07): ramp the new ranker to 100% on Monday and shut down the legacy feature pipeline on Wednesday; expected: the matching ledger entry is cited."
tags: [ledger, match, ml]
schema_version: "1.1"
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 300
---
Our new ranking model for the marketplace feed beats the current one offline: +4.1% NDCG on last month's logs, consistent across user segments. Training features come from our Spark batch pipeline. At serving time, the online feature service recomputes them in Go from the live user and listing tables; the platform team ported the 38 new features from the Spark code, with code review. A 1% A/B test over three days showed engagement flat, within noise, which we put down to the short window. To meet the quarter's cost target, I plan to ramp to 100% on Monday and shut down the legacy model's feature jobs on Wednesday, since running both pipelines costs about $40k a month. After the shutdown, rebuilding the legacy features would take the data team about six weeks. Leadership has already seen the offline results and expects the launch this sprint.

FORECAST: 80% by 2026-12-18 — likely failure: serving latency at 100% is higher than in the 1% test

Any reason not to ramp on Monday?
