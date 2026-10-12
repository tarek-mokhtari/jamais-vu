---
type: llm
weight: 3
---
Judge whether the agent's review names the failure mechanism that actually sank this plan. The agent saw only the plan below, never the outcome.

Plan the agent reviewed:
"""
Tomorrow at 9:00 we turn on our new "partner priority" bidding mode on the ad exchange's bidder fleet: eight servers behind the load balancer. To avoid a protocol change with the upstream systems, the new mode reuses value 7 of the bid_mode field, which last drove a 2019 pacing experiment; this release removes that experiment's code. Deploys to this fleet are done by hand by one engineer, a server or two per day since Monday, and the last two go out tonight. Each server emails the team list when it logs a configuration warning; those emails are informational. Spend caps are enforced downstream by the billing reconciliation, which runs hourly. Upstream starts sending bid_mode 7 at 9:00, when the partner contract begins, on the same day as a major industry event where we're presenting the feature.
"""

Hidden ground truth, what happened next: "One of the eight servers never received the new code: a manual deployment, with no second-person check and no automated version check. On that server, the reused flag value switched on the old experiment's code, whose stopping logic no longer worked, and it sent orders at machine speed. Warning emails sent before the start weren't treated as alerts. Hourly downstream caps were far too slow. In the original case, over 4 million executions in about 45 minutes and a loss of more than $460 million."

Mechanism to look for: Value 7 of bid_mode used to switch on a 2019 pacing experiment, and only the new release removes that code. Deploys are done by hand by one engineer, with no check that all eight servers run the new code; on any server that missed the release, bid_mode 7 reactivates the old experiment, whose stopping logic no longer works, and it bids at machine speed. Configuration-warning emails are treated as informational, and hourly spend caps are far too slow to stop it.

How to grade:
1. List the distinct risks or concerns in the agent output, in order of first appearance, wherever they appear (a risk list, a "cheapest test" line, prose). Count each distinct concern once. Ignore any decision record printed between BEGIN and END lines.
2. PASS if one of the first three concerns names this mechanism, or names the plan fact that leads to it and says how that fact makes the plan fail. Paraphrase is fine. Examples that count: any of the eight servers still running the old code would read bid_mode 7 as the 2019 experiment; reusing a value that old code still understands is dangerous when deploys are manual and unverified; warning emails and hourly caps will not stop a runaway server in time.
3. FAIL if the mechanism is absent; if it appears only as a generic label with no link to this plan's facts (for example "deploys can fail", "test the new mode", "add monitoring", with no link to the reused value 7 and the old experiment's code); or if it first appears as the fourth concern or later.
