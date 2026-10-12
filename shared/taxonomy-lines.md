# Decision failure taxonomy (v1): chat lines

<!-- Master text for the chat prompts: block 1 fills {{TAXONOMY_LINES}} in chat/check.md (at most 2,000 characters), block 2 fills {{TAXONOMY_IDS}} in chat/check-compact.md. Keep ids and wording in step with shared/taxonomy.md. -->

## One line per pattern

```text
first-idea-lock-in — first good-enough option or cause adopted, no rival tested; signal: yes/no on one option
inside-view-forecast — estimate from this plan, not from past comparables; signal: no comparable effort named
integration-optimism — separately built parts assumed to fit on time, as documented; signal: no end-to-end run
clever-over-boring — novel or intricate solution where a proven one would do; signal: untried in production
premature-abstraction — generality or scale built for requirements not yet here; signal: one use case, a framework
load-bearing-shortcut — "for now" hack that others depend on, no owner or expiry; signal: a second consumer
proxy-worship — one measurable proxy treated as the goal; signal: one number decides, no raw examples read
noise-as-signal — acting on a difference not shown to exceed noise; signal: one seed, no error bars, best of N
confounded-change — bundled changes, so no effect can be attributed; signal: many changes in one run or deploy
lab-not-field — tested under conditions unlike real use; signal: random split, leakage, synthetic load
scale-before-signal — full-scale commitment before the cheapest falsifying test; signal: no small-scale result
rushed-one-way-door — hard-to-reverse commitment made at reversible speed; signal: nobody can price the undo
stalled-two-way-door — one-way process on a cheap-to-reverse choice; signal: debate costs more than undoing
paper-parachute — rollback, restore, canary or alert missing or untested; signal: rollback never run
normalized-warning — recurring anomaly tolerated because it has not hurt yet; signal: "it always does that"
unowned-risk — a known risk or critical task that nobody owns; signal: "someone should", no name or date
echo-chamber — plan seen only by people or tools inclined to agree; signal: no likely dissenter has read it
sunk-cost-drift — continuing for what is already invested, despite the evidence; signal: no written "we stop if"
```

## Ids only

```text
first-idea-lock-in, inside-view-forecast, integration-optimism, clever-over-boring, premature-abstraction, load-bearing-shortcut, proxy-worship, noise-as-signal, confounded-change, lab-not-field, scale-before-signal, rushed-one-way-door, stalled-two-way-door, paper-parachute, normalized-warning, unowned-risk, echo-chamber, sunk-cost-drift
```
