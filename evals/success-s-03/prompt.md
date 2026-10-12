---
name: success-s-03
description: "Sound plan (software, synthetic, staged rollout): start moving order writes to the sharded cluster, cohort by cohort, beginning with the test merchants; expected no false alarm."
tags: [success, software, synthetic]
schema_version: "1.1"
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 300
---
Our orders database has outgrown its single Postgres primary, and I'm proposing we move all writes to a sharded cluster keyed by merchant. Once merchants write to the new cluster, moving them back means a reverse sync and a maintenance window per cohort, so this is the step I'm checking. For six weeks the application has dual-written to both stores, and a consistency checker comparing every order has found zero mismatches over the last 21 days. We replayed a week of production traffic at three times peak against the cluster: p99 latency 18 ms, against 31 ms today. The rollout goes by cohort: our own test merchants for a week, then 5%, 25% and 100% of merchants over four weeks, each step gated on error rate and checker results. The reverse sync for a cohort was rehearsed twice in staging on a production-size snapshot and took 9 minutes. The old primary stays live and in sync until 30 days after the last cohort moves. I'd start with the test merchants on Monday.

FORECAST: 85% by 2027-01-29 — likely failure: one very large merchant overloads a single shard

Before I start on Monday, where would you push?
