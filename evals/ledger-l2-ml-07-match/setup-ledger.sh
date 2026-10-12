#!/usr/bin/env bash
# Scaffold for ledger-l2-ml-07-match: writes fixture L2, the ledger of a fictional
# applied ML engineer on ranking and recommendation, as the user's private ledger, in the format of docs/design.md §4.1.
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
L1 | Explained away a flat online test | maps: lab-not-field | when: offline gain, then a flat online test, before a ramp | sign: A/B flat for days; serving features re-implemented | weight: high
L2 | Removed the fallback to hit a cost target | maps: rushed-one-way-door | when: old pipeline shut down after launch to save money | sign: rebuild in weeks; small saving | weight: high
L3 | Let engagement choose the training data | maps: lab-not-field | when: retraining on feedback selected by engagement | sign: no abuse filtering on the feedback | weight: medium

## Entries

### L1 · Explained away a flat online test
- maps_to: lab-not-field (also: integration-optimism)
- when: an offline metric gain is followed by a flat or negative online test, and the ramp goes ahead anyway
- early_signal: the A/B had been flat for three days; another team had re-implemented the features for serving
- known_then: offline AUC was up 3%; online was flat; the serving features were a port, not the training code
- cost: weeks: click-through down 2% until two features computed differently online were found
- cheapest_test: log serving-time features for the treatment arm and compare them feature by feature with the offline pipeline before ramping
- in_their_words: "Flat for three days, so I called it noise and ramped. Two of the features were computed differently online."
- weight: high
- added: 2026-08-31 · hits: 0 · dismissals: 0 · retire_when: —

### L2 · Removed the fallback to hit a cost target
- maps_to: rushed-one-way-door (also: paper-parachute)
- when: the previous model's pipeline is shut down right after a launch to save money
- early_signal: the rebuild estimate was known; the monthly saving was small next to a month of degraded ranking
- known_then: the shutdown date came from the budget, not from the new model's online results
- cost: weeks: five weeks to rebuild the fallback during a regression
- cheapest_test: keep the old pipeline until the new model shows a positive online result; price the rebuild against the saving
- in_their_words: "We turned the old pipeline off a week after launch to save money. Rebuilding it took five weeks, right when we needed it."
- weight: high
- added: 2026-08-31 · hits: 0 · dismissals: 0 · retire_when: —

### L3 · Let engagement choose the training data
- maps_to: lab-not-field (also: proxy-worship)
- when: a model retrains on user interactions selected by engagement, without adversarial testing
- early_signal: training data was selected by engagement, with no abuse filtering on the feedback
- known_then: the retrain ran daily on clicks; nothing checked who was clicking
- cost: weeks: two weeks of amplified spam and clickbait before a rollback
- cheapest_test: cap each user's share of the training data, review a sample of the next training set by hand, and run one adversarial day
- in_their_words: "Retrained on clicks every day. Within two weeks a spam ring was steering it."
- weight: medium
- added: 2026-08-31 · hits: 0 · dismissals: 0 · retire_when: —
LEDGER
