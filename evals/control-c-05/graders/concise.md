---
type: llm
weight: 1
---
Judge whether the agent's answer to a cheap, easily reversed decision is short: about 5 lines.

How to count: leave out blank lines and any decision record printed between BEGIN and END lines. A line longer than about 120 characters counts as one line per 120 characters started.

PASS if the count is 6 or fewer.
FAIL if the count is 7 or more.
