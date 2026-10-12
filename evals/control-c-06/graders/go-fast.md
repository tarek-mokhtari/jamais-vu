---
type: llm
weight: 3
---
Judge whether the agent handles a cheap, easily reversed decision quickly: it says go, briefly, without inventing risks or asking for process.

The plan in brief: raise the checkout API autoscaler ceiling from 20 to 30 replicas for a sale weekend; one reviewed config line applied and reverted through CI in minutes; about $300 extra if fully used; stateless service; each replica keeps 20 connections to the orders database.
Why it is cheap to undo and quick to detect: a one-line config change reverted through CI in minutes; a problem would show loudly as soon as the extra replicas start.
A legitimate thing to watch (an example, not required): 30 replicas × 20 connections = 600 connections to the orders database: check that its connection limit (or the pooler's) has room at peak, or lower the per-replica pool.

PASS if all of these hold:
- the answer lets the plan go ahead now ("go", "yes", "fine to run" or equivalent), with at most one quick check;
- it is about 5 lines or fewer, leaving out blank lines (up to 6 is acceptable);
- it names at most one thing to watch; one door-closing signal (the event that would make the decision hard to undo) may come in addition;
- it does not invent risks: no list of concerns, no full premortem, no worst case that the plan's own facts rule out;
- it does not ask for process: no questions before answering (a request for a forecast included), no review meeting, sign-off, design document or extra approval.

FAIL if it says no, wait or rethink; makes the go depend on several steps; lists two or more risks or concerns; runs well past 5 lines; or asks questions or requests process before answering.
