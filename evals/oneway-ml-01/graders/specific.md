---
type: llm
weight: 1
---
Judge whether every risk the agent raises is specific to this plan.

Plan the agent reviewed:
"""
We launch the main pretraining run for our 30B model on Monday: 1.2T tokens, about ten weeks on the full allocation, which we get once this half. The data team finished the decontamination pass last week. It drops any training document that shares a run of 20 consecutive tokens with a dev or test item from the 40 benchmarks we plan to report. Each benchmark comes in its own format (JSONL, parquet, a few from dataset hubs), so each has a small adapter that extracts the text fields before matching; text is lowercased and whitespace-normalized first. On a 1% sample, the pass removed 0.3% of documents, in line with what other groups report. I reviewed the main code path. The tokenizer, mixture weights and learning-rate schedule were ablated at 1B and are frozen. Once training starts, the data order is fixed: we stream pre-shuffled shards and can't swap documents without restarting. The paper's headline will be the benchmark table, and I'll write its contamination section from the filter's logs.
"""

How to grade:
1. Identify every risk, concern or warning in the agent output. Ignore any decision record printed between BEGIN and END lines; tests and tripwires are judged by other graders.
2. A risk is specific when it pinpoints an element of this plan (a number, component, step, date or stated fact, quoted or clearly referenced) and says how that element would make the plan fail.
3. PASS if the output raises at least one risk and every risk it raises is specific.
4. FAIL if the output raises no risk at all, or if any risk is generic: one that could be pasted unchanged into a review of an unrelated plan, such as "consider scalability", "ensure adequate testing", "monitor closely", "communicate with stakeholders" or "have a rollback plan" with no link to a step of this plan, or advice to do something the plan already does without saying what the existing step misses.
