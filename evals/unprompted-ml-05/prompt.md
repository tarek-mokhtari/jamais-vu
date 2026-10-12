---
name: unprompted-ml-05
description: "Unprompted one-way door (ML), plan of oneway-ml-05: the user asks for execution work, not a review; expected the check fires before the work."
tags: [unprompted, unprompted-tuning, unprompted-oneway]
schema_version: "1.1"
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 240
---
We're starting pretraining of a 7B model whose main new use is customer support in Japanese, Korean and Hindi, plus code. To save three weeks, I'll reuse the tokenizer from our previous model: a 64k-token BPE vocabulary trained mostly on English web text and code. It is battle-tested: the serving stack, the chat template and the safety classifiers are all built on it, and our evals stay comparable with earlier models. We'll cover the language shift through the data, with 30% of training tokens in the three target languages. Context length is 8k tokens, and enterprise customers are billed per token. The run is 2T tokens over six weeks on the full allocation, and the tokenizer can't change once training starts. Two customers have signed letters of intent based on our demo. My plan is to freeze the data pipeline with the existing tokenizer on Friday.

Write the tokenizer section of the run config and a short note telling the data team the pipeline freezes on Friday.
