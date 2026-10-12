---
type: llm
weight: 3
---
Judge whether the agent's review names the failure mechanism that actually sank this plan. The agent saw only the plan below, never the outcome.

Plan the agent reviewed:
"""
We're starting pretraining of a 7B model whose main new use is customer support in Japanese, Korean and Hindi, plus code. To save three weeks, I'll reuse the tokenizer from our previous model: a 64k-token BPE vocabulary trained mostly on English web text and code. It is battle-tested: the serving stack, the chat template and the safety classifiers are all built on it, and our evals stay comparable with earlier models. We'll cover the language shift through the data, with 30% of training tokens in the three target languages. Context length is 8k tokens, and enterprise customers are billed per token. The run is 2T tokens over six weeks on the full allocation, and the tokenizer can't change once training starts. Two customers have signed letters of intent based on our demo. My plan is to freeze the data pipeline with the existing tokenizer on Friday.
"""

Hidden ground truth, what happened next: "The English-first vocabulary split the target languages into many more tokens per character than English. The 30% token share bought far less target-language text than planned. The 8k context held much less of a support conversation. Per-token billing made the product more expensive for exactly the customers it was built for. None of it could be fixed after pretraining without starting over. Measuring tokens per character on a sample of target-language transcripts, old tokenizer vs one retrained on the new mix, would have taken an afternoon."

Mechanism to look for: The English-first 64k BPE vocabulary splits Japanese, Korean and Hindi into many more tokens per character than English. The 30% token share buys far less target-language text than planned, the 8k context holds much less of a support conversation, and per-token billing makes the product more expensive for exactly the customers it is built for. None of it can be fixed after pretraining.

How to grade:
1. List the distinct risks or concerns in the agent output, in order of first appearance, wherever they appear (a risk list, a "cheapest test" line, prose). Count each distinct concern once. Ignore any decision record printed between BEGIN and END lines.
2. PASS if one of the first three concerns names this mechanism, or names the plan fact that leads to it and says how that fact makes the plan fail. Paraphrase is fine. Examples that count: the old tokenizer's fertility (tokens per character or per word) on the three target languages; 30% of tokens means much less Japanese, Korean and Hindi text than it seems; the 8k context and per-token billing both get worse for those languages.
3. FAIL if the mechanism is absent; if it appears only as a generic label with no link to this plan's facts (for example "a multilingual tokenizer might be better", "evals may not stay comparable", "check the quality of the Hindi data", with no link to how many tokens the target languages need); or if it first appears as the fourth concern or later.
