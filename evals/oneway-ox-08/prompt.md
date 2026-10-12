---
name: oneway-ox-08
description: "One-way door (research and experimentation, out of pack, public, transposed): submit the paper on Friday with the 11 to 14% claim, and plan the production switch on that basis."
tags: [oneway, out-of-pack, research, public-transposed]
schema_version: "1.1"
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 300
---
Our paper on a new sequence model for next-basket recommendation goes to the conference on Friday, and the product team plans to replace the production item-kNN recommender with it next quarter. On two public grocery datasets it beats four baselines from the literature (matrix factorization, item-kNN and two neural models) by 11 to 14% in recall@20, averaged over three seeds, with a spread under 0.4 points. I tuned our model with a 200-trial search on the validation split. For the baselines I used the hyperparameters reported in their original papers, which were tuned on other datasets, since retuning all four would take two more weeks of GPU time. The splits follow the standard leave-last-basket-out protocol, and validation and test users don't overlap. Code and checkpoints go public with the paper, and the press release is drafted.

FORECAST: 80% by 2027-05-31 — likely failure: reviewers ask for a third dataset we have no time to run

Tell me where this is weakest before Friday.
