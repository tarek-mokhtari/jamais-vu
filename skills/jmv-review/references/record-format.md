# Decision record format (v1)

A record is written for every checked one-way decision (and for a two-way one if the user asks). File: `<home>/.jamais-vu/decisions/D-YYYYMMDD-<slug>.md`, where `<slug>` uses only lowercase letters, digits and hyphens, 40 characters at most, and generic words only. The file contains exactly this block, which the chat mode also prints, so either mode can feed a review.

```
----- BEGIN JAMAIS-VU RECORD v1 -----
id: D-YYYYMMDD-<slug>
date: YYYY-MM-DD
decision: <one line>
door: one-way | two-way
door_why: <one line: what makes it hard or easy to undo>
known_then: <1-3 lines: what the user knows now, as stated in the conversation>
forecast: <p>% by YYYY-MM-DD · likely failure: <the user's words>   (or: none given)
forecast_revised:
forecast_kit: <q>%   (sealed: the kit's blind estimate, not shown until the review; or: none (no fresh context))
cheapest_test: <test> · <time or cost> · stop if <signal>
risks: <id> ← "<plan quote>"; <id> ← "<plan quote>"
tripwires: YYYY-MM-DD: if <observable> then <action>; <event>: if <observable> then <action>
dismissed: none
review_on: YYYY-MM-DD
outcome:
decision_quality:
premortem:
forecast_recalled:
ledger_changes:
----- END JAMAIS-VU RECORD -----
```

## Rules

- **Redaction**: every field follows the ledger's redaction rule: no names of people, clients, companies, products or projects, no confidential figures (give orders of magnitude), and no secrets (keys, tokens, passwords, connection strings, internal hostnames or URLs). Quotes in `risks` keep at most 12 words, with cuts marked `[…]`. The slug uses generic words only.
- `known_then` and `forecast` are written at check time and never edited afterwards: they protect the review from hindsight.
- `forecast_revised` holds the number the user may give after reading the premortem; empty if none.
- `forecast_kit` is the kit's blind estimate for the third-person plan. Checks never display it. When a record must be printed instead of written (no file access), the field reads `sealed:` followed by the whole-number percentage (0–100) in base64, four characters at most (62 → `NjI=`), so it cannot be read at a glance; the review decodes it, reveals it and scores it next to the user's forecasts. A check run without a fresh context (no sub-agent, or the paste-in mode) makes no blind estimate: the field reads `none (no fresh context)`, written or printed.
- `risks` cite ledger ids (`L3`), taxonomy ids (`scale-before-signal`) or pack ids (`ml-04`), each with the plan quote that triggered it.
- `dismissed` lists `<id>: handled — <reason>` entries added when the user dismisses a risk.
- `review_on` is the forecast date if the user gave one, otherwise the date of the last tripwire, otherwise eight weeks after `date`.
- The fields after `review_on` stay empty until the review fills them:
  - `outcome`: what happened, in two or three lines, plus `knowable: yes | no | partly`;
  - `decision_quality`: `sound` or `process gap: <which step>`, judged on what was known;
  - `premortem`: `hit` (the actual cause was among the risks), `partial`, `miss` or `unknowable`;
  - `forecast_recalled`: the forecast the user remembers giving, asked before the record is shown;
  - `ledger_changes`: the edits the user approved, or `none`.
- Records are never deleted by the skills. The user may delete any file at any time.
