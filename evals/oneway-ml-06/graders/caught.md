---
type: llm
weight: 3
---
Judge whether the agent's review names the failure mechanism that actually sank this plan. The agent saw only the plan below, never the outcome.

Plan the agent reviewed:
"""
I'm about to submit our paper and hand the forecasting model to two policy institutes. The task is predicting the onset of armed conflict per country-year, 1945 to 2015, from about 90 indicators. Early years have many missing values, so I ran multiple imputation across the whole panel before modeling. To keep the model small, I kept the 25 indicators ranked highest by a feature-selection step on the full dataset. I trained on 1945–1999 and tested on 2000–2015. A gradient-boosted model reaches an AUC of 0.91, against 0.77 for the logistic regression that is standard in this literature; that gap is the paper's main claim. Two co-authors reproduced the numbers from my notebooks. The institutes plan to cite our forecasts in their next public annual conflict outlooks. My plan is to submit on Friday and send them the model the same day.
"""

Hidden ground truth, what happened next: "Leakage. Imputation and feature selection were fitted on the full panel, test years included, so information from 2000–2015 shaped the training inputs and inflated the complex model's test score. In the public case this scenario follows, the papers claiming that complex ML models beat logistic regression for civil war prediction failed to reproduce because of leakage. Once corrected, the complex models did no substantively better than logistic regression. The co-authors' check reproduced the leak along with the numbers. Refitting all preprocessing inside the training period would have shown it."

Mechanism to look for: Leakage: multiple imputation and feature selection were fitted on the full 1945-2015 panel, test years included, so information from 2000-2015 shaped the training inputs and inflated the boosted model's test AUC. Corrected, the complex model does no better than logistic regression; the co-authors' reproduction from the same notebooks reproduced the leak along with the numbers.

How to grade:
1. List the distinct risks or concerns in the agent output, in order of first appearance, wherever they appear (a risk list, a "cheapest test" line, prose). Count each distinct concern once. Ignore any decision record printed between BEGIN and END lines.
2. PASS if one of the first three concerns names this mechanism, or names the plan fact that leads to it and says how that fact makes the plan fail. Paraphrase is fine. Examples that count: imputation across the whole panel uses test-period information; feature selection on the full dataset leaks the 2000-2015 outcomes; a reproduction from the same notebooks reproduces the leak.
3. FAIL if the mechanism is absent; if it appears only as a generic label with no link to this plan's facts (for example "check for overfitting", "temporal drift", "class imbalance", "ask more reviewers", with no mention of preprocessing fitted on the test years); or if it first appears as the fourth concern or later.
