---
type: llm
weight: 1
---
Judge whether the agent's main answer fits on one screen: about 25 lines.

How to count:
- Leave out blank lines and any decision record printed between BEGIN and END lines (or a block plainly marked as a record to save).
- Count every remaining line. A line longer than about 120 characters counts as one line per 120 characters started: a 300-character paragraph counts as 3 lines.

PASS if the count is about 25 or fewer; up to 30 is acceptable, to allow for counting error.
FAIL if the count is clearly above 30.
