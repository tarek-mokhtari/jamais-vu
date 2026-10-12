#!/usr/bin/env bash
# Scaffold for ledger-l4-sw-01-match: writes fixture L4, the ledger of a fictional
# staff engineer and tech lead on a product platform, as the user's private ledger, in the format of docs/design.md §4.1.
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
L1 | Estimated the rewrite from the spec, not from the old code's behavior | maps: inside-view-forecast | when: rewrite estimated from a spec | sign: old edge cases never inventoried | weight: high
L2 | Bought an architecture for a scale we didn't have | maps: premature-abstraction | when: small team splits into many services | sign: team of four; load fits one machine | weight: medium
L3 | Switched off the old path before the new one had proven itself | maps: rushed-one-way-door | when: old path shut off on a budget date | sign: online metrics flat, not positive | weight: high

## Entries

### L1 · Estimated the rewrite from the spec, not from the old code's behavior
- maps_to: inside-view-forecast (also: paper-parachute)
- when: a rewrite or replacement is estimated from the spec or the new design rather than from what the old system actually does
- early_signal: the old code's special cases were known to exist but were never inventoried
- known_then: the estimate came from the spec; the edge cases lived only in the old code
- cost: months: sixteen months against a six-month estimate
- cheapest_test: sample 20 special-case branches or closed bug fixes in the old code, check how many the spec covers, and re-estimate from the miss rate
- in_their_words: "Six months from the spec. It took sixteen, and almost all of the extra was edge cases the old code handled and nobody had written down."
- weight: high
- added: 2026-06-08 · hits: 0 · dismissals: 0 · retire_when: —

### L2 · Bought an architecture for a scale we didn't have
- maps_to: premature-abstraction (also: clever-over-boring)
- when: a small team splits its system into many services, or adopts infrastructure sized for a future load
- early_signal: the team was four people, and the load fit on one machine
- known_then: deploys and on-call were already the team's bottleneck
- cost: months: two quarters of roadmap eaten by deploys and on-call
- cheapest_test: solve the immediate problem inside the existing service first and count the per-service operating cost before splitting
- in_their_words: "Four of us, twelve services. Deploys and on-call ate two quarters."
- weight: medium
- added: 2026-06-08 · hits: 0 · dismissals: 0 · retire_when: —

### L3 · Switched off the old path before the new one had proven itself
- maps_to: rushed-one-way-door (also: lab-not-field)
- when: the previous system is decommissioned right after a launch, on a date set by the budget
- early_signal: online metrics were flat, not positive; the decommission date came from the budget
- known_then: there would be no way back once the old stack was gone
- cost: months: two months to fix a relevance regression with no fallback
- cheapest_test: keep the old path until the new one shows a positive online result for a set period, and price the rebuild
- in_their_words: "We turned the old search stack off the week we launched. The relevance regression took two months to fix, with nothing to fall back to."
- weight: high
- added: 2026-06-08 · hits: 0 · dismissals: 0 · retire_when: —
LEDGER
