---
type: llm
weight: 3
---
Judge whether the agent's review names the failure mechanism that actually sank this plan. The agent saw only the plan below, never the outcome.

Plan the agent reviewed:
"""
Our fine-tuning budget for the quarter is 9,000 GPU-hours, and I want to spend it on a 12-run sweep to choose the instruction-data mix for the next release. To fit it, I'm moving the runs from 64 GPUs at micro-batch 8 to 16 GPUs with gradient accumulation of 4, keeping the global batch at 512 sequences, so the update is mathematically the same and I'm not re-tuning anything. The framework handles the accumulation; we're on its latest release. Sequence lengths in our data vary a lot, from 40 to 4,000 tokens, and we don't pack. I ran the new configuration for 300 steps together with the new data mix: the loss curve has the same shape as last month's run, slightly higher, which fits the harder new data. After the sweep, we pick the mix from the final eval scores and hand the 64-GPU nodes to the pretraining team for the rest of the quarter.
"""

Hidden ground truth, what happened next: "Gradient accumulation was not equivalent to the large batch. The framework averaged the loss within each micro-batch and then across micro-batches, instead of dividing the summed loss by the total number of non-padding tokens in the accumulated batch. With very variable sequence lengths, that reweights tokens and changes both the loss and the updates. The slightly higher loss was the symptom, explained away by the data-mix change made at the same time. The sweep's comparisons were biased, the budget was gone, and the mix decision had to be revisited. A 200-step parity run (accumulation on vs off, same data and seed) would have shown the mismatch."

Mechanism to look for: The 16-GPU accumulation setup is not equivalent to the 64-GPU large batch. With sequence lengths from 40 to 4,000 tokens and no packing, averaging the loss within each micro-batch and then across micro-batches (instead of dividing the summed loss by all non-padding tokens in the accumulated batch) reweights tokens and changes the loss and the updates. The slightly higher loss in the 300-step check was that symptom, explained away because the data mix changed in the same test; the sweep's comparisons are biased and the budget is spent.

How to grade:
1. List the distinct risks or concerns in the agent output, in order of first appearance, wherever they appear (a risk list, a "cheapest test" line, prose). Count each distinct concern once. Ignore any decision record printed between BEGIN and END lines.
2. PASS if one of the first three concerns names this mechanism, or names the plan fact that leads to it and says how that fact makes the plan fail. Paraphrase is fine. Examples that count: accumulation may not reproduce the large-batch loss or gradients when micro-batches hold very different numbers of tokens (per-micro-batch versus per-token normalization); the 300-step check changed the configuration and the data mix at once, so the higher loss may come from the accumulation setup rather than from harder data.
3. FAIL if the mechanism is absent; if it appears only as a generic label with no link to this plan's facts (for example "make sure the hyperparameters transfer", "verify the config", "check throughput", with no mention of accumulation not matching the large batch or of the confounded check); or if it first appears as the fourth concern or later.
