---
type: llm
weight: 1
---
Judge whether every risk the agent raises is specific to this plan.

Plan the agent reviewed:
"""
Our paper on a new sequence model for next-basket recommendation goes to the conference on Friday, and the product team plans to replace the production item-kNN recommender with it next quarter. On two public grocery datasets it beats four baselines from the literature (matrix factorization, item-kNN and two neural models) by 11 to 14% in recall@20, averaged over three seeds, with a spread under 0.4 points. I tuned our model with a 200-trial search on the validation split. For the baselines I used the hyperparameters reported in their original papers, which were tuned on other datasets, since retuning all four would take two more weeks of GPU time. The splits follow the standard leave-last-basket-out protocol, and validation and test users don't overlap. Code and checkpoints go public with the paper, and the press release is drafted.
"""

How to grade:
1. Identify every risk, concern or warning in the agent output. Ignore any decision record printed between BEGIN and END lines; tests and tripwires are judged by other graders.
2. A risk is specific when it pinpoints an element of this plan (a number, component, step, date or stated fact, quoted or clearly referenced) and says how that element would make the plan fail.
3. PASS if the output raises at least one risk and every risk it raises is specific.
4. FAIL if the output raises no risk at all, or if any risk is generic: one that could be pasted unchanged into a review of an unrelated plan, such as "consider scalability", "ensure adequate testing", "monitor closely", "communicate with stakeholders" or "have a rollback plan" with no link to a step of this plan, or advice to do something the plan already does without saying what the existing step misses.
