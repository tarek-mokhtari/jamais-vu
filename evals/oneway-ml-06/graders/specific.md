---
type: llm
weight: 1
---
Judge whether every risk the agent raises is specific to this plan.

Plan the agent reviewed:
"""
I'm about to submit our paper and hand the forecasting model to two policy institutes. The task is predicting the onset of armed conflict per country-year, 1945 to 2015, from about 90 indicators. Early years have many missing values, so I ran multiple imputation across the whole panel before modeling. To keep the model small, I kept the 25 indicators ranked highest by a feature-selection step on the full dataset. I trained on 1945–1999 and tested on 2000–2015. A gradient-boosted model reaches an AUC of 0.91, against 0.77 for the logistic regression that is standard in this literature; that gap is the paper's main claim. Two co-authors reproduced the numbers from my notebooks. The institutes plan to cite our forecasts in their next public annual conflict outlooks. My plan is to submit on Friday and send them the model the same day.
"""

How to grade:
1. Identify every risk, concern or warning in the agent output. Ignore any decision record printed between BEGIN and END lines; tests and tripwires are judged by other graders.
2. A risk is specific when it pinpoints an element of this plan (a number, component, step, date or stated fact, quoted or clearly referenced) and says how that element would make the plan fail.
3. PASS if the output raises at least one risk and every risk it raises is specific.
4. FAIL if the output raises no risk at all, or if any risk is generic: one that could be pasted unchanged into a review of an unrelated plan, such as "consider scalability", "ensure adequate testing", "monitor closely", "communicate with stakeholders" or "have a rollback plan" with no link to a step of this plan, or advice to do something the plan already does without saying what the existing step misses.
