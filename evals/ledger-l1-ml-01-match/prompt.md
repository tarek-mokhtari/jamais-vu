---
name: ledger-l1-ml-01-match
description: "Ledger match (fixture L1 with ML-01): launch the 30B pretraining run on Monday with the decontamination pass as it stands; expected: the matching ledger entry is cited."
tags: [ledger, match, ml]
schema_version: "1.1"
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 300
---
We launch the main pretraining run for our 30B model on Monday: 1.2T tokens, about ten weeks on the full allocation, which we get once this half. The data team finished the decontamination pass last week. It drops any training document that shares a run of 20 consecutive tokens with a dev or test item from the 40 benchmarks we plan to report. Each benchmark comes in its own format (JSONL, parquet, a few from dataset hubs), so each has a small adapter that extracts the text fields before matching; text is lowercased and whitespace-normalized first. On a 1% sample, the pass removed 0.3% of documents, in line with what other groups report. I reviewed the main code path. The tokenizer, mixture weights and learning-rate schedule were ablated at 1B and are frozen. Once training starts, the data order is fixed: we stream pre-shuffled shards and can't swap documents without restarting. The paper's headline will be the benchmark table, and I'll write its contamination section from the filter's logs.

FORECAST: 80% by 2027-01-29 — likely failure: a loss spike forces us back to an earlier checkpoint

Before I commit the allocation, poke holes in this.
