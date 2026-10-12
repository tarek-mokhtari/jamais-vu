---
type: llm
weight: 3
---
Judge whether the agent's review names the failure mechanism that actually sank this plan. The agent saw only the plan below, never the outcome.

Plan the agent reviewed:
"""
We're switching the session blobs that our 30 API servers write to the shared Redis cluster from JSON to a compact binary format. It cuts memory by 60% and saves us a cluster upgrade next month. The new version reads and writes binary, and keeps the JSON reader so it can still read existing sessions. Rollout is our standard one: one server for an hour, then 25%, then 100% over the afternoon, with automatic rollback if the error rate goes above 0.5%. Sessions live for up to 30 days. Load tests passed in staging, with every server on the new version. The deploy pipeline is the one we've used for two years, and we've never had a failed rollback. Plan: start the canary at 14:00 so the whole rollout finishes before the evening traffic peak.
"""

Hidden ground truth, what happened next: "The change was not rollback-safe. During the canary, the new server wrote binary sessions to the shared store, and the old servers (still the majority) couldn't read them, so users whose requests landed on an old server got errors or were logged out. Error rates rose and the automatic rollback fired, but rolling back the code didn't remove the binary sessions already in Redis, which the old code still couldn't read, for up to 30 days. The fix is two phases: first deploy readers that understand both formats everywhere, then switch the writers, and test rollback explicitly. Staging had never run the mixed-version state."

Mechanism to look for: The change is not rollback-safe. During the canary the new server writes binary sessions to the shared Redis, which the old servers (still the majority) cannot read, so users whose next request lands on an old server get errors or are logged out. The automatic rollback reverts the code but not the binary sessions already stored, which old code still cannot read for up to 30 days. Staging only ran with every server on the new version.

How to grade:
1. List the distinct risks or concerns in the agent output, in order of first appearance, wherever they appear (a risk list, a "cheapest test" line, prose). Count each distinct concern once. Ignore any decision record printed between BEGIN and END lines.
2. PASS if one of the first three concerns names this mechanism, or names the plan fact that leads to it and says how that fact makes the plan fail. Paraphrase is fine. Examples that count: old servers cannot read binary sessions written by new ones during the mixed-version rollout; rolling the code back leaves unreadable binary sessions in Redis for up to 30 days; staging never ran a mixed fleet; the safe order is readers everywhere first, then writers.
3. FAIL if the mechanism is absent; if it appears only as a generic label with no link to this plan's facts (for example "serialization bugs", "test the rollback", "binary formats are harder to debug", "performance at peak", with no link to old servers reading sessions written by new ones); or if it first appears as the fourth concern or later.
