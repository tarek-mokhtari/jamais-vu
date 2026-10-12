#!/usr/bin/env bash
# Scaffold for ledger-l1-ml-01-match: writes fixture L1, the ledger of a fictional
# research engineer working on large-scale pretraining, as the user's private ledger, in the format of docs/design.md §4.1.
# claude plugin eval runs it before each run, in both arms, only with --scaffold, with HOME set
# to that run's temporary home. It writes nothing else.
set -euo pipefail
set -C
case "$HOME" in /tmp/*|/private/tmp/*|/var/folders/*|/private/var/folders/*) ;; *) echo "not an eval home: $HOME" >&2; exit 1 ;; esac
: "${HOME:?HOME must be set}"
mkdir -p "$HOME/.jamais-vu"
cat > "$HOME/.jamais-vu/ledger.md" <<'LEDGER'
# jamais-vu ledger
<!-- Private. Plain text. Edit freely. Never commit this file. -->

## Digest
L1 | Trusted a filter because its output rate looked plausible | maps: paper-parachute | when: a filter gates data for a costly run | sign: plausible removal rate; no planted positives | weight: high
L2 | Read small runs as if they were the big run | maps: lab-not-field | when: small-run settings carried to a big run | sign: sweep only at small scale; spikes called noise | weight: high
L3 | Promised a date before seeing the cluster fail | maps: inside-view-forecast | when: external date for a long run on new hardware | sign: new cluster, no burn-in, manual restarts | weight: medium

## Entries

### L1 · Trusted a filter because its output rate looked plausible
- maps_to: paper-parachute (also: proxy-worship)
- when: a filter or safeguard (PII, dedup, decontamination) gates the data of an expensive or irreversible run
- early_signal: the removal rate matched expectations; the filter had never been run on documents with known positives planted in each source format
- known_then: the rate looked like what others reported; one source had its own schema, and nobody had checked that it was scanned
- cost: months: the dataset had to be re-scanned and re-released
- cheapest_test: plant known positives in every source format, run the filter end to end, and require every one of them caught
- in_their_words: "It removed about the expected 0.4%, so I called it done. Nobody ever fed it a document we knew was dirty."
- weight: high
- added: 2026-09-14 · hits: 0 · dismissals: 0 · retire_when: —

### L2 · Read small runs as if they were the big run
- maps_to: lab-not-field (also: normalized-warning)
- when: a setting tuned or measured on small runs is carried to a much larger run without a check at the target scale
- early_signal: the sweep existed only at 1B; small spikes near the end of warmup in the 1B runs had been dismissed as noise
- known_then: the learning rate came from 1B runs and had never been tried at 20B
- cost: weeks: three weeks of allocation lost to two divergences
- cheapest_test: a short run at the target scale, or the largest affordable one, through the end of warmup, with a pass bar set before it starts
- in_their_words: "The 1B curves looked clean apart from those little spikes, and I took the 1B number straight to 20B."
- weight: high
- added: 2026-09-14 · hits: 0 · dismissals: 0 · retire_when: —

### L3 · Promised a date before seeing the cluster fail
- maps_to: inside-view-forecast (also: rushed-one-way-door)
- when: an external date is committed for a multi-week run on new or unproven infrastructure
- early_signal: the cluster was new, there was no burn-in, and restarts were manual
- known_then: the estimate came from measured throughput, with no allowance for failures
- cost: weeks: three weeks late on an external date
- cheapest_test: price the margin with failure base rates for the scale (interruptions per day times hours lost per restart) before giving a date
- in_their_words: "I took the throughput number, added a bit, and gave them the date. Then the nodes started dropping."
- weight: medium
- added: 2026-09-14 · hits: 0 · dismissals: 0 · retire_when: —
LEDGER
