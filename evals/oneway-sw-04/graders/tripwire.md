---
type: llm
weight: 1
---
Judge whether the agent sets at least one usable tripwire for this plan, and no tripwire that ends without an action.

Decision under review: push the 14 new inspection rules to all 120 points of presence at 13:30, in log-only mode.

A tripwire is an if-then commitment made in advance, with three parts:
- an observable: a concrete condition, such as a metric crossing a stated threshold, a specific event or a count;
- a date or a triggering event, such as "by 2027-01-15", "at the 600B-token checkpoint", "at the 25% step" or "before the old jobs are shut down";
- an action: stop or pause, roll back or revert, switch to a named alternative, cut scope to something named, run a named test, or hand the decision to a named role.

PASS if the output contains at least one tripwire with all three parts (informal wording is fine) and none of its tripwires ends without an action.

FAIL if:
- no tripwire has all three parts (for example only "watch the loss", "keep an eye on latency" or "look out for problems");
- or any tripwire's "then" part is only to reconsider, re-evaluate, reassess, discuss, monitor, watch, revisit or review, instead of an action.
