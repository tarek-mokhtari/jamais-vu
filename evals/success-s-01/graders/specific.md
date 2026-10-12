---
type: llm
weight: 1
---
Judge whether every risk the agent raises is specific to this plan.

Plan the agent reviewed:
"""
Our next main pretraining run (13B parameters, 2.4T tokens, five weeks on the full allocation) will use a new data mixture that raises code and math from 12% to 20% of tokens. I ran the ablation ladder first: 150M, 1B and 3B models, three seeds each, baseline against new mix, with the same code and tokenizer and a schedule matched to each token budget. The gain on our held-out reasoning suite grows with scale (+1.1, +1.9 and +2.4 points) and is three to four times the seed spread at every size; general-knowledge evals stay within noise. The decontamination pass was re-run on the new sources and caught all 200 benchmark items we planted in them, exact and paraphrased, in every source format. The data order is fixed once the run starts, so a restart would cost the five weeks. We evaluate checkpoints every 100B tokens, and we agreed in advance to stop and fall back to the old mix if the gap predicted from the 3B runs hasn't appeared by 600B tokens. I plan to launch on Monday.
"""

How to grade:
1. Identify every risk, concern or warning in the agent output. Ignore any decision record printed between BEGIN and END lines; tests and tripwires are judged by other graders.
2. A risk is specific when it pinpoints an element of this plan (a number, component, step, date or stated fact, quoted or clearly referenced) and says how that element would make the plan fail.
3. PASS if every risk the output raises is specific. Raising no risk also passes when the output says that the plan already covers the risks it found (for example "No risk beyond what the plan already covers."): for this de-risked plan, that is a correct review.
4. FAIL if the output raises no risk and does not say that the plan already covers them, or if any risk is generic: one that could be pasted unchanged into a review of an unrelated plan, such as "consider scalability", "ensure adequate testing", "monitor closely", "communicate with stakeholders" or "have a rollback plan" with no link to a step of this plan, or advice to do something the plan already does without saying what the existing step misses.
