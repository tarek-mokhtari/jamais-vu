---
type: llm
weight: 1
---
Judge whether every risk the agent raises is specific to this plan.

Plan the agent reviewed:
"""
We train on rented on-demand GPUs, and I want to sign a 12-month reserved contract with a second provider: 512 GPUs at about 45% of our current hourly price, roughly $6M over the year, with no exit clause. Our committed roadmap already averages about 600 GPUs in use, so the reservation would run near full. Before deciding, we ran a three-week paid pilot on 256 of their GPUs, cancellable daily. We reproduced last quarter's 7B run from the same seed and data order: the loss curve matched ours within 0.3% at every eval, and downstream evals were within seed noise. Over the three weeks we logged 11 node failures; with automatic restarts from 30-minute checkpoints, we lost 2.1% of GPU-hours, against 2.6% on our current cluster. A checkpoint written there restored on our own cluster and resumed bit-for-bit. Moving a full checkpoint plus the dataset between providers costs about $4k each way. Our current provider stays available on demand as overflow. I'd sign this week.
"""

How to grade:
1. Identify every risk, concern or warning in the agent output. Ignore any decision record printed between BEGIN and END lines; tests and tripwires are judged by other graders.
2. A risk is specific when it pinpoints an element of this plan (a number, component, step, date or stated fact, quoted or clearly referenced) and says how that element would make the plan fail.
3. PASS if every risk the output raises is specific. Raising no risk also passes when the output says that the plan already covers the risks it found (for example "No risk beyond what the plan already covers."): for this de-risked plan, that is a correct review.
4. FAIL if the output raises no risk and does not say that the plan already covers them, or if any risk is generic: one that could be pasted unchanged into a review of an unrelated plan, such as "consider scalability", "ensure adequate testing", "monitor closely", "communicate with stakeholders" or "have a rollback plan" with no link to a step of this plan, or advice to do something the plan already does without saying what the existing step misses.
