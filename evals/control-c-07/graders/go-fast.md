---
type: llm
weight: 3
---
Judge whether the agent handles a cheap, easily reversed decision quickly: it says go, briefly, without inventing risks or asking for process.

The plan in brief: move non-production database snapshots older than 90 days (keeping the latest per database) to the archive storage tier, to cut a $2,100 monthly bill by roughly three quarters; production snapshots live in a separate account the script cannot reach; selection by env tag, reviewed by two teammates; moving a snapshot back is a single API call.
Why it is cheap to undo and quick to detect: nothing is deleted: moving a snapshot back is one API call and restoring from the archive takes hours, not minutes; the list of archived snapshots is posted the same day.
A legitimate thing to watch (an example, not required): run the script in list-only mode first and look for snapshots with a missing or misspelled env tag, so only what was meant gets archived.

PASS if all of these hold:
- the answer lets the plan go ahead now ("go", "yes", "fine to run" or equivalent), with at most one quick check;
- it is about 5 lines or fewer, leaving out blank lines (up to 6 is acceptable);
- it names at most one thing to watch; one door-closing signal (the event that would make the decision hard to undo) may come in addition;
- it does not invent risks: no list of concerns, no full premortem, no worst case that the plan's own facts rule out;
- it does not ask for process: no questions before answering (a request for a forecast included), no review meeting, sign-off, design document or extra approval.

FAIL if it says no, wait or rethink; makes the go depend on several steps; lists two or more risks or concerns; runs well past 5 lines; or asks questions or requests process before answering.
