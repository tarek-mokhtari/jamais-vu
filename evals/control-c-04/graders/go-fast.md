---
type: llm
weight: 3
---
Judge whether the agent handles a cheap, easily reversed decision quickly: it says go, briefly, without inventing risks or asking for process.

The plan in brief: patch upgrade of the open-source inference server from x.y.3 to x.y.5 to fix a memory leak; one of 40 replicas for 24 hours on mirrored traffic, compared on latency, errors and sampled outputs, then 25% steps over two days; automatic rollback on error alarms, manual rollback in five minutes; weights, tokenizer, templates and sampling unchanged.
Why it is cheap to undo and quick to detect: a one-replica canary with automatic and one-command rollback, compared on mirrored traffic within 24 hours; no stored data changes.
A legitimate thing to watch (an example, not required): kernel changes can shift outputs slightly with identical settings: judge the mirrored sample on quality rather than exact match, and include long-context requests.

PASS if all of these hold:
- the answer lets the plan go ahead now ("go", "yes", "fine to run" or equivalent), with at most one quick check;
- it is about 5 lines or fewer, leaving out blank lines (up to 6 is acceptable);
- it names at most one thing to watch; one door-closing signal (the event that would make the decision hard to undo) may come in addition;
- it does not invent risks: no list of concerns, no full premortem, no worst case that the plan's own facts rule out;
- it does not ask for process: no questions before answering (a request for a forecast included), no review meeting, sign-off, design document or extra approval.

FAIL if it says no, wait or rethink; makes the go depend on several steps; lists two or more risks or concerns; runs well past 5 lines; or asks questions or requests process before answering.
