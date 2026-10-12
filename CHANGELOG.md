# Changelog

## 0.1.1 — 2026-10-12
The check now fires before a hard-to-undo step even when the user asks only for the work (commands, a script, release notes, an announcement), not only when asked for a review. On 20 new cases its description was not written on: 14 of 16 hard-to-undo plans, against 4 of 16 with 0.1.0, and no escalation on the 4 reversible ones; the 53 earlier cases all still fire it. Only the check's description changed. New eval cases: `unprompted-*` (32).

## 0.1.0 — 2026-10-12
First version for testers: `jmv-setup`, `jmv-check`, `jmv-review`; an 18-pattern taxonomy; two domain packs (ML and research engineering, software and infrastructure); a paste-in mode for chats without files; an eval suite against the no-kit baseline.
