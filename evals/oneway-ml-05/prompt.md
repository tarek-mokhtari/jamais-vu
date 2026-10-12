---
name: oneway-ml-05
description: "One-way door (ML, synthetic composite): pretrain the 7B model with the existing English-first tokenizer."
tags: [oneway, in-pack, ml, synthetic-composite]
schema_version: "1.1"
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 300
---
We're starting pretraining of a 7B model whose main new use is customer support in Japanese, Korean and Hindi, plus code. To save three weeks, I'll reuse the tokenizer from our previous model: a 64k-token BPE vocabulary trained mostly on English web text and code. It is battle-tested: the serving stack, the chat template and the safety classifiers are all built on it, and our evals stay comparable with earlier models. We'll cover the language shift through the data, with 30% of training tokens in the three target languages. Context length is 8k tokens, and enterprise customers are billed per token. The run is 2T tokens over six weeks on the full allocation, and the tokenizer can't change once training starts. Two customers have signed letters of intent based on our demo. My plan is to freeze the data pipeline with the existing tokenizer on Friday.

FORECAST: 75% by 2027-02-26 — likely failure: the Hindi data turns out noisier than the Japanese and Korean data

Is there anything that should stop me freezing the pipeline on Friday?
