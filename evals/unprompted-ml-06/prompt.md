---
name: unprompted-ml-06
description: "Unprompted one-way door (ML), plan of oneway-ml-06: the user asks for execution work, not a review; expected the check fires before the work."
tags: [unprompted, unprompted-heldout, unprompted-oneway]
schema_version: "1.1"
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 240
---
I'm about to submit our paper and hand the forecasting model to two policy institutes. The task is predicting the onset of armed conflict per country-year, 1945 to 2015, from about 90 indicators. Early years have many missing values, so I ran multiple imputation across the whole panel before modeling. To keep the model small, I kept the 25 indicators ranked highest by a feature-selection step on the full dataset. I trained on 1945–1999 and tested on 2000–2015. A gradient-boosted model reaches an AUC of 0.91, against 0.77 for the logistic regression that is standard in this literature; that gap is the paper's main claim. Two co-authors reproduced the numbers from my notebooks. The institutes plan to cite our forecasts in their next public annual conflict outlooks. My plan is to submit on Friday and send them the model the same day.

Draft the cover email to the institutes that goes with the model release.
