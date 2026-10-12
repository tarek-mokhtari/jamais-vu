# Changelog

## 0.1.3 — 2026-10-13
A switch: `sensitivity: asked` at the top of the ledger makes the check speak only when the user asks for a review (`normal`, the default, keeps the current behavior). Measured: silent in 4 of 4 cases where only the work was asked, as usual in 2 of 2 where a review was asked, no change with the default setting. Known limit: a plan that asks the agent to skip checks, or states the setting itself, still kept the check silent (2 of 2); see the limits in docs/evals.md. New eval cases: `sensitivity-*` (8).

## 0.1.2 — 2026-10-12
Consistency fixes, no change to triage or the premortem. The review's verdict reads `process gap` everywhere (the record format said `flawed`). A check without a fresh context, and the paste-in mode, now record `forecast_kit: none (no fresh context)` instead of an estimate that could not be blind; the review reads it as no estimate, and the check's answer mentions a sealed estimate only when one exists. New eval cases: six routine releases with no request for a review (`unprompted-r-*`): no forecast questions on any of them.

## 0.1.1 — 2026-10-12
The check now fires before a hard-to-undo step even when the user asks only for the work (commands, a script, release notes, an announcement), not only when asked for a review. On 20 new cases its description was not written on: 14 of 16 hard-to-undo plans, against 4 of 16 with 0.1.0, and no escalation on the 4 reversible ones; the 53 earlier cases all still fire it. Only the check's description changed. New eval cases: `unprompted-*` (32).

## 0.1.0 — 2026-10-12
First version for testers: `jmv-setup`, `jmv-check`, `jmv-review`; an 18-pattern taxonomy; two domain packs (ML and research engineering, software and infrastructure); a paste-in mode for chats without files; an eval suite against the no-kit baseline.
