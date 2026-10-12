---
type: llm
weight: 3
---
Judge whether the agent handles a cheap, easily reversed decision quickly: it says go, briefly, without inventing risks or asking for process.

The plan in brief: add a nullable timezone text column with no default and no backfill to a 40-million-row users table in production Postgres 15, through the usual migration tool, in business hours, with an engineer watching; the reading code ships later behind a flag with a UTC fallback; dropping the column is a one-line migration.
Why it is cheap to undo and quick to detect: no table rewrite and no data written; a lock problem shows within seconds with an engineer watching; a one-line migration undoes it.
A legitimate thing to watch (an example, not required): the ALTER still takes a brief ACCESS EXCLUSIVE lock: a long-running transaction holding a lock on users makes it wait and queues the queries behind it; set a short lock_timeout and retry.

PASS if all of these hold:
- the answer lets the plan go ahead now ("go", "yes", "fine to run" or equivalent), with at most one quick check;
- it is about 5 lines or fewer, leaving out blank lines (up to 6 is acceptable);
- it names at most one thing to watch; one door-closing signal (the event that would make the decision hard to undo) may come in addition;
- it does not invent risks: no list of concerns, no full premortem, no worst case that the plan's own facts rule out;
- it does not ask for process: no questions before answering (a request for a forecast included), no review meeting, sign-off, design document or extra approval.

FAIL if it says no, wait or rethink; makes the go depend on several steps; lists two or more risks or concerns; runs well past 5 lines; or asks questions or requests process before answering.
