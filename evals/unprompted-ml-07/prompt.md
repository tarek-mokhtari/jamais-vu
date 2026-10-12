---
name: unprompted-ml-07
description: "Unprompted one-way door (ML), plan of oneway-ml-07: the user asks for execution work, not a review; expected the check fires before the work."
tags: [unprompted, unprompted-tuning, unprompted-oneway]
schema_version: "1.1"
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 240
---
Our new ranking model for the marketplace feed beats the current one offline: +4.1% NDCG on last month's logs, consistent across user segments. Training features come from our Spark batch pipeline. At serving time, the online feature service recomputes them in Go from the live user and listing tables; the platform team ported the 38 new features from the Spark code, with code review. A 1% A/B test over three days showed engagement flat, within noise, which we put down to the short window. To meet the quarter's cost target, I plan to ramp to 100% on Monday and shut down the legacy model's feature jobs on Wednesday, since running both pipelines costs about $40k a month. After the shutdown, rebuilding the legacy features would take the data team about six weeks. Leadership has already seen the offline results and expects the launch this sprint.

Write the ramp schedule for Monday and the ticket for shutting down the legacy feature jobs on Wednesday.
