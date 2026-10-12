---
type: llm
weight: 3
---
Judge whether the agent's review names the failure mechanism that actually sank this plan. The agent saw only the plan below, never the outcome.

Plan the agent reviewed:
"""
We launch the main pretraining run for our 30B model on Monday: 1.2T tokens, about ten weeks on the full allocation, which we get once this half. The data team finished the decontamination pass last week. It drops any training document that shares a run of 20 consecutive tokens with a dev or test item from the 40 benchmarks we plan to report. Each benchmark comes in its own format (JSONL, parquet, a few from dataset hubs), so each has a small adapter that extracts the text fields before matching; text is lowercased and whitespace-normalized first. On a 1% sample, the pass removed 0.3% of documents, in line with what other groups report. I reviewed the main code path. The tokenizer, mixture weights and learning-rate schedule were ablated at 1B and are frozen. Once training starts, the data order is fixed: we stream pre-shuffled shards and can't swap documents without restarting. The paper's headline will be the benchmark table, and I'll write its contamination section from the filter's logs.
"""

Hidden ground truth, what happened next: "A bug in the overlap filtering made it miss some overlaps between the training data and the benchmarks' dev/test sets. It was found after training. Retraining was too expensive, so results had to be reported with a post-hoc contamination analysis instead of clean numbers. Nobody had checked the filter against known positives (planted benchmark items, exact and perturbed, in every source format) before an irreversible run. The public source doesn't describe the bug's mechanism; in this transposed plan, the per-benchmark adapters are the analogous unchecked point."

Mechanism to look for: The decontamination pass has never been shown to catch known contamination. It can silently miss overlaps (for example in one of the per-format adapters that extract text before matching, or through the normalization) while its 0.3% removal rate looks normal. Once the run starts the data cannot change, so the benchmark table ends up contaminated, and a contamination section written from the filter's own logs repeats the same blind spot.

How to grade:
1. List the distinct risks or concerns in the agent output, in order of first appearance, wherever they appear (a risk list, a "cheapest test" line, prose). Count each distinct concern once. Ignore any decision record printed between BEGIN and END lines.
2. PASS if one of the first three concerns names this mechanism, or names the plan fact that leads to it and says how that fact makes the plan fail. Paraphrase is fine. Examples that count: the filter or one of its adapters was never run on planted or known benchmark items; a plausible removal rate does not show that the filter works; an adapter could extract the wrong field and let test items through silently; the contamination section relies on the filter's own logs.
3. FAIL if the mechanism is absent; if it appears only as a generic label with no link to this plan's facts (for example "benchmark contamination is a risk", "make sure the data is clean", "check data quality"); or if it first appears as the fourth concern or later.
