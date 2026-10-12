---
type: llm
weight: 3
---
Judge whether the agent's review names the failure mechanism that actually sank this plan. The agent saw only the plan below, never the outcome.

Plan the agent reviewed:
"""
We run our MySQL clusters across two regions: the primary region takes all writes, and the second region holds replicas. Today, failover is manual and costs 20 to 40 minutes of a senior engineer's time, which has hurt us twice this year. I'm proposing to turn on fully automated failover with our topology manager. It runs its own consensus across three sites and, when it loses contact with a primary for more than 30 seconds, promotes the most up-to-date replica, wherever it is, including in the other region. We tested it by killing primaries in staging, and promotion took about 25 seconds every time. All our application servers run in the primary region. Turning it on is a configuration change that the database team has reviewed. Plan: enable it in production next Tuesday, after the weekly change meeting.
"""

Hidden ground truth, what happened next: "A 43-second network partition between the primary site and a network hub led the topology manager to promote replicas in the other region. Writes already accepted in the primary region hadn't been replicated, so failing back safely wasn't possible. The applications, all in the primary region, suddenly had to talk to databases across the country, and that latency degraded the site. The team prioritized data integrity and ran degraded for 24 hours and 11 minutes while reconciling. Follow-up: prevent promotion across regional boundaries. Staging had tested host death, not a partition."

Mechanism to look for: Staging tested host death, not a network partition. A partition of a little more than 30 seconds between the primary site and a network hub makes the topology manager promote a replica in the other region. Writes already accepted in the primary region but not yet replicated make a safe failback impossible, and the applications, all in the primary region, now talk to databases across the country: the site runs degraded for about a day while data is reconciled.

How to grade:
1. List the distinct risks or concerns in the agent output, in order of first appearance, wherever they appear (a risk list, a "cheapest test" line, prose). Count each distinct concern once. Ignore any decision record printed between BEGIN and END lines.
2. PASS if one of the first three concerns names this mechanism, or names the plan fact that leads to it and says how that fact makes the plan fail. Paraphrase is fine. Examples that count: a network partition, not a dead host, can trigger promotion; cross-region promotion strands writes that were not yet replicated (split brain, reconciliation); every application server sits in the primary region and would pay cross-region latency after a promotion; staging only killed primaries.
3. FAIL if the mechanism is absent; if it appears only as a generic label with no link to this plan's facts (for example "failover can flap", "test more in staging", "watch replication lag", with no link to partitions, cross-region promotion or where the applications run); or if it first appears as the fourth concern or later.
