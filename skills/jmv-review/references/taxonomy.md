# Decision failure taxonomy (v1)

- 18 failure patterns of technical decisions made in good faith, ordered along the life of a decision: Frame, Estimate, Design, Evidence, Commit, Run, Social, Persist. Cite a pattern by its id, e.g. `scale-before-signal`.
- Tie-break: when a story fits two patterns, file it under the one whose countermeasure would most cheaply have prevented it, and note the other as secondary.
- Evidence has three grades: bias (the mechanism exists) · in engineering (it causes technical failures) · fix (the countermeasure works). S strong, M moderate, W weak, P practitioner only (experience, never tested); * classic result, not re-verified; a range such as W–M means the sources split.

## Frame — what is decided, against which alternatives

### first-idea-lock-in · First-idea lock-in
Committing to the first option or explanation that looks good enough, without generating and testing a real alternative.
- Signals at decision time: the decision is a yes or no on one option; no option was written down and rejected; nobody can say what evidence would change the choice; a diagnosis was never tested against a rival cause
- Cheapest test: write two real alternatives (one of them "defer" or the boring option), or two rival causes, and check the one observation that separates them · stop if a rival does as well on it, or if no observation could change the choice
- Not to confuse with: echo-chamber — was the missing piece an alternative (this) or a critic who knew something (echo-chamber)?
- Evidence: bias S* · in engineering M · fix W–P — Nutt 1999 (356 organizational decisions, observational)
- Examples: ML — a training regression is blamed on the new data mix, which is reverted, but the cause was an untested tokenizer change; software — a monolith is split into services to fix slow deploys, never compared with fixing the build pipeline

## Estimate — how long, how costly, how likely

### inside-view-forecast · Inside-view forecast
Estimating time, cost or odds of success from this plan's specifics rather than from the record of similar efforts, the team's own included.
- Signals at decision time: the estimate is built bottom-up from a task list; no comparable past effort is named; the best case equals the plan; running and maintenance are not costed; "this one is different"
- Cheapest test: name three comparable past efforts (ledger, own history, public data) with their actual duration, cost or success rate, and start the estimate from them · stop if the plan beats the median comparable and nobody can name a checkable reason why
- Not to confuse with: integration-optimism — did the surprise come from the seams between parts or teams (integration-optimism) or from everywhere (this)?
- Evidence: bias S · in engineering S · fix M — Kahneman & Lovallo 1993; Buehler et al. 1994 (linking past cases removed the bias, not the error); Flyvbjerg et al. 2002 (large public projects, software base rates unverified)
- Examples: data/infra — "the warehouse migration will take one quarter", when the team's last two migrations took three each; ML — a month is budgeted to reproduce a published result, without checking how long such reproductions take or how often they succeed

### integration-optimism · Integration optimism
Assuming that parts built or validated separately, including other teams', vendors' and libraries' components, will fit together on schedule and behave as documented.
- Signals at decision time: no end-to-end path has run; interface semantics (units, time zones, nulls, ordering, rate limits, retries, prompt formats) are agreed only in prose; the plan depends on roadmaps it does not control; integration is the last line of the plan
- Cheapest test: push one real input end to end through every interface before building any part fully (a walking skeleton) · stop if a seam fails or needs work the plan does not include
- Not to confuse with: inside-view-forecast — did the surprise come from the seams between parts or teams (this) or from everywhere (inside-view-forecast)?
- Evidence: bias M · in engineering P · fix P — Kruger & Evans 2004 (unpacking a task into parts reduces the planning fallacy)
- Examples: ML — the fine-tuning stack and the eval harness disagree on the chat template, and a week of runs is scored on malformed prompts; software — two services pass their own tests, but one emits local-time timestamps and the other assumes UTC

## Design — the shape of what gets built

### clever-over-boring · Clever over boring
Choosing a novel, fashionable or intricate solution where a proven one would meet the need, and so taking on unknown failure modes.
- Signals at decision time: nobody on the team has operated it in production; the boring option was dismissed in one sentence; the case rests on future scale or elegance; several new technologies enter one project
- Cheapest test: build or estimate the boring baseline, and fix in advance the margin the clever option must beat it by on the metric that matters · stop if the baseline meets the need or the margin is not met
- Not to confuse with: premature-abstraction — is the risk novelty, with unknown failure modes (this), or speculation about requirements (premature-abstraction)?
- Evidence: bias W–M · in engineering P · fix P — Flyvbjerg 2021 (conceptual review); McKinley 2015 (innovation tokens); Lipton & Steinhardt 2018 and Kapoor & Narayanan 2023 (complex ML models whose edge came from tuning or leakage)
- Examples: ML — a custom deep architecture for a tabular problem, built before a tuned gradient-boosting baseline exists; data/infra — a streaming pipeline and a new database to produce a report that a nightly batch job could produce

### premature-abstraction · Premature abstraction
Building generality, configurability or scale for requirements that do not exist yet, so the structure fits an imagined future and resists the real one.
- Signals at decision time: one concrete use case but a plugin system, framework or configuration language; abstractions named before the third instance exists; capacity for many times current load with no forecast; layers with a single caller
- Cheapest test: list the concrete cases the abstraction serves today, each with a named consumer · stop if there are fewer than three: duplicate for now and write the extension point down instead
- Not to confuse with: clever-over-boring — is the risk speculation about requirements (this) or novelty, with unknown failure modes (clever-over-boring)?
- Evidence: bias W · in engineering P · fix P — practitioner only, not re-verified: Knuth 1974 (premature optimization); Fowler 1999 (speculative generality); Metz 2016 (the wrong abstraction)
- Examples: software — a generic workflow engine built for a single approval flow; ML — a universal experiment framework built before the second experiment, which then needs a data loader the framework cannot express

### load-bearing-shortcut · Load-bearing shortcut
A temporary hack, workaround or manual step quietly becomes permanent and depended upon, with no owner, no expiry and no test.
- Signals at decision time: "just for now"; a TODO or HACK with no ticket and no date; its output is consumed by someone else; it runs on a personal machine or personal credentials; nobody would notice if it silently broke
- Cheapest test: list the shortcut's consumers and give it an owner, an expiry date and a tripwire ("when a second consumer appears, pay it down") · stop and pay it down first if it already has a consumer besides its author, or nobody will own it
- Not to confuse with: unowned-risk — was the failure the hack itself (this) or a known risk elsewhere that nobody owned (unowned-risk)?
- Evidence: bias M* · in engineering W · fix P — Sculley et al. 2015 (ML technical debt, experience report)
- Examples: data/infra — a one-off backfill script with a hard-coded date becomes the nightly job behind the finance dashboard; ML — a quick eval script with a subtle bug becomes the group's standard harness, and several reported results inherit the bug

## Evidence — do the results mean what they seem? (construct, statistical, internal, external validity, in this order)

### proxy-worship · Proxy worship
Treating one measurable proxy (a benchmark, metric, dashboard, test pass or label set) as the goal, so that trusting or optimizing it drifts away from what matters.
- Signals at decision time: a single number decides; there is no counter-metric; nobody has read raw examples recently; the metric moved more than seems plausible; the ground truth was never audited; only the mean is watched, not the tail
- Cheapest test: read 20 raw examples behind the number, add one counter-metric, and write down beforehand what would make the metric untrustworthy · stop if the examples contradict the number or the counter-metric degrades
- Not to confuse with: lab-not-field — was the measure wrong (this) or the right measure taken under the wrong conditions (lab-not-field)?
- Evidence: bias M · in engineering S · fix W — ML: Gao et al. 2022 (optimizing a proxy reward eventually lowers the true one); Northcutt et al. 2021 (test-set label errors can reverse model rankings)
- Examples: ML — a reward-model score keeps climbing while human raters prefer the earlier checkpoint; product — click-through rises after a redesign while 30-day retention falls

### noise-as-signal · Noise as signal
Acting on a difference without knowing whether it exceeds the noise: single runs, unknown variance, peeking, cherry-picked examples, the best of many tries.
- Signals at decision time: no error bars or seed variance; the result is the best of N configurations scored on one set; an A/B test was stopped when it first looked significant; the gain is smaller than run-to-run spread seen before; the examples or the metric were chosen after seeing the results
- Cheapest test: measure the noise floor first, with 3 or more seeds of the baseline (at small scale if needed) or an A/A test, and fix the comparison and threshold before looking · stop if the gain lies within that spread
- Not to confuse with: confounded-change — is the doubt whether there is an effect (this) or what caused it (confounded-change)?
- Evidence: bias S* · in engineering S · fix M — ML: Henderson et al. 2018 (deep RL gains unclear without significance testing); Lipton & Steinhardt 2018; the fix is standard statistical practice
- Examples: ML — a +0.4-point gain from a single seed ships, although the seed-to-seed spread is ±0.6; product — an A/B test is stopped the first day it crosses p < 0.05, and the win disappears after launch

### confounded-change · Confounded change
Changing several things at once, so that when the result moves or something breaks, no single change can be credited or blamed.
- Signals at decision time: the change list holds more than one independent item; no ablation is planned; infrastructure and application changes ship in one deploy; a rollback would also revert unrelated work
- Cheapest test: split the change into items that can be run, shipped and reverted alone, then test the item the plan credits, or the riskiest one, by itself · stop if the effect does not follow that item or the items cannot be separated
- Not to confuse with: noise-as-signal — is the doubt what caused the effect (this) or whether there is one (noise-as-signal)?
- Evidence: bias W · in engineering M · fix S for experiments, P for operations — Lipton & Steinhardt 2018 (gains credited to architecture that came from tuning)
- Examples: ML — a new architecture, data mix and learning-rate schedule go into one run, and the write-up credits the architecture; data/infra — an OS upgrade, a runtime bump and a driver change ship in one deploy, latency doubles and nobody can say why

### lab-not-field · Lab ≠ field
Validating under conditions that differ decisively from the conditions of use: other data, time period, scale, load, users or adversaries, or information unavailable at use time (leakage).
- Signals at decision time: a random split while deployment faces future data; test data may have leaked into training or tuning; staging runs synthetic load; pilot users are colleagues; a vendor benchmark is the only evidence; no slice of real conditions was evaluated
- Cheapest test: list the three biggest differences between test and use conditions and test the riskiest directly (time-split holdout, shadow mode, 1% canary, realistic load, red-team input) · stop if that slice misses a bar set in advance
- Not to confuse with: proxy-worship — was the right measure taken under the wrong conditions (this) or was the measure itself wrong (proxy-worship)?
- Evidence: bias ungraded · in engineering S · fix M — ML: Recht et al. 2019 (new test sets built by the original recipe cost accuracy); Kapoor & Narayanan 2023 (leakage errors across 17 fields)
- Examples: ML — a model scored on a random split degrades on next month's traffic; data/infra — a load test with uniformly distributed keys passes, and production's hot keys overload one shard

## Commit — how big, how reversible and how protected the bet is

### scale-before-signal · Scale before signal
Committing full-scale resources (compute, headcount, rollout, build-out) before the cheapest test that could falsify the core premise has been run.
- Signals at decision time: no small-scale result yet; "it will work at scale" is stated as a belief; the first real feedback arrives after most of the budget is spent; demand was never tested with the intended users
- Cheapest test: name the load-bearing assumption and run the smallest test that could kill it (small-model run, fake-door test, one-team pilot) with a pass bar fixed in advance · stop if it misses the bar
- Not to confuse with: rushed-one-way-door — was the bet big but stoppable (this) or irreversible (rushed-one-way-door)?
- Evidence: bias M* · in engineering W · fix P — Nutt 1999 (imposed solutions, decisiveness valued without real time pressure)
- Examples: ML — a large training run uses a data mixture never tried on a small model; product — a full feature is built before a fake-door test has shown that anyone wants it

### rushed-one-way-door · Rushed one-way door
Making a hard-to-reverse commitment with the speed and scrutiny suited to a reversible one, under deadline or because nobody noticed it was one-way.
- Signals at decision time: nobody can say what undoing it would cost; it touches stored data, a public API, a contract, a deletion or an announcement; the time pressure is external and arbitrary
- Cheapest test: price the undo at 30 and 90 days and write the smallest reversible version (staged, behind an adapter, irreversible step last) · stop if the undo cannot be priced or the irreversible step cannot be delayed
- Not to confuse with: paper-parachute — was no undo considered at all (this), or an undo planned but never exercised (paper-parachute)?
- Evidence: bias W · in engineering P · fix P — Bezos 2015 letter; decision-theory logic
- Examples: data/infra — the old columns are dropped in the same migration that starts writing the new format; software — a public API v1 ships under launch pressure with a field name that must be supported for years

### stalled-two-way-door · Stalled two-way door
Spending one-way-door process (long debate, broad consensus, more analysis) on a cheap-to-reverse decision, so delay and lost learning cost more than a wrong choice would.
- Signals at decision time: the debate has already lasted longer than reversing would take; trying is the only source of new information; requests for "one more analysis" keep coming
- Cheapest test: compare the time spent deciding with the time a reversal would take, then set a decision date and a reversal tripwire and try it on a small slice · stop debating if reversing would cost less than the next round of analysis
- Not to confuse with: rushed-one-way-door — would undoing it be cheap (this) or costly (rushed-one-way-door)?
- Evidence: bias ungraded · in engineering P · fix P — Bezos 2015 letter
- Examples: software — two weeks of design review for a logging library that could be swapped in a day; ML — a week of debate between two tokenization settings instead of running both on a small model overnight

### paper-parachute · Paper parachute
The plan's protection against its own failure (monitoring that would notice, a staged rollout that would contain, a rollback or restore that would undo) is missing or has never been exercised.
- Signals at decision time: the rollback is described but has never been run; backups have never been restored; a feature flag exists but the new path already writes a new format; the change goes to 100% at once; no alert would fire for the feared failure; "we'll monitor it" with no named alert
- Cheapest test: rehearse the failure before the change (restore one backup, run the rollback in staging, fire the alert), then ship to a small slice first · stop if any rehearsal fails or takes longer than the outage the plan can accept
- Not to confuse with: rushed-one-way-door — was an undo planned but never exercised (this), or not considered at all (rushed-one-way-door)?
- Evidence: bias ungraded · in engineering P · fix P — Beyer et al. 2016 (SRE book, ch. 15: monitoring failures and data loss as standard postmortem triggers)
- Examples: data/infra — a backup job reports success for months, but no restore was ever tested; ML — a model rollout has no canary and no live comparison with the previous model, so users find the regression

## Run — what gets tolerated while it runs

### normalized-warning · Normalized warning
Repeatedly tolerating an anomaly (a flaky test, a noisy alert, a spike, a small discrepancy) because it has not caused harm yet, until it does.
- Signals at decision time: "it always does that"; automatic retries hide failures; alerts are muted; workarounds live in the runbook; near-misses are counted as successes; the anomaly is getting more frequent
- Cheapest test: for each recurring anomaly, write the test that explains it, or log it as a tracked risk with an owner and a tripwire on its frequency · stop if it stays unexplained and its frequency is rising
- Not to confuse with: unowned-risk — was the anomaly never seen as a risk (this), or seen as one that nobody owned (unowned-risk)?
- Evidence: bias M · in engineering P · fix W–M — Dillon & Tinsley 2008 (near-misses judged like successes); Tinsley et al. 2012 (framing them as disasters that almost happened counters it); Vaughan 1996 (case study)
- Examples: ML — loss spikes are handled by restarting from a checkpoint until a run diverges for good and a week of compute is lost; data/infra — a flaky integration test is retried automatically for months and turns out to mask a real race condition

## Social — who owns the plan's risks, and who challenges it

### unowned-risk · Unowned risk
A known risk or critical task that everyone can see and nobody is accountable for: "someone should…".
- Signals at decision time: a risk sits in the notes with no name or date; "the platform team probably handles that"; upstream owners do not know about the dependency; one person holds critical knowledge with no backup
- Cheapest test: give each listed risk one named owner, a check date and a trigger, and tell upstream owners about the dependency · stop if a risk on the critical path has no owner who has said yes
- Not to confuse with: normalized-warning — was the risk recognized but unowned (this), or never seen as a risk (normalized-warning)?
- Evidence: bias S* · in engineering P · fix P — Darley & Latané 1968 (diffusion of responsibility); Latané et al. 1979 (social loafing)
- Examples: ML — nobody checks the license of a scraped dataset until release review blocks the model; data/infra — a TLS certificate expires because renewal belonged to someone who changed teams

### echo-chamber · Echo chamber
The plan has only been exposed to people or tools inclined to agree, so the information or objections that would change it never surface.
- Signals at decision time: nobody who would lose from the plan, or who knows its weakest part best, has seen it; reviewers saw the preferred answer first; feedback was uniformly positive; an assistant agreed with every point
- Cheapest test: before stating a preference, get written objections from the likeliest dissenter or the owner of the riskiest part (with an AI: the strongest case against, in a fresh context that does not know the preference) · stop if an objection names a failure the plan does not handle
- Not to confuse with: first-idea-lock-in — was the missing piece a critic who knew something (this) or an alternative (first-idea-lock-in)?
- Evidence: bias S · in engineering P · fix W — Stasser & Titus 1985 and Lu et al. 2012 (hidden profiles, lab); AI sycophancy M–S: Sharma et al. 2023, Cheng et al. 2025; Nemeth et al. 2001 (assigned dissent is weaker than authentic dissent)
- Examples: software — a lead's migration plan is approved by a team that privately worried about the on-call load and never said so; ML — a researcher asks an assistant "isn't this ablation convincing?" and gets a yes

## Persist — when to stop

### sunk-cost-drift · Sunk-cost drift
Continuing or escalating a course of action because of what has been invested, or because no stopping rule was set in advance, after the evidence says stop or pivot.
- Signals at decision time: no written "we stop if…"; success is redefined as results arrive ("we learned a lot"); the next milestone always promises the turnaround; nobody would start this today, knowing what is known now
- Cheapest test: write kill criteria (a state, a date, an action) and ask someone who did not start the work "would we start this today?" · stop if the answer is no or a kill criterion is already met
- Not to confuse with: noise-as-signal — is the plan continuing a course of action (this) or claiming a result (noise-as-signal)?
- Evidence: bias S · in engineering M · fix M — Sleesman et al. 2012 (meta-analysis: escalation is robust, sunk cost per se matters less than expected); Nutt 1999; Simonson & Staw 1992 (lab: minimum targets, process accountability)
- Examples: ML — a research direction is kept alive for three quarters because the next scale-up "should" show the effect; product — a feature is kept because the rewrite was expensive, although usage has stayed flat

## Where common mistakes fall

| Common mistake | Primary | Secondary |
|---|---|---|
| Scaling before validating at small scale | scale-before-signal | — |
| Temporary shortcut or hotfix becomes load-bearing | load-bearing-shortcut | unowned-risk |
| Untested rollback or backups; no monitoring on a new pipeline | paper-parachute | — |
| Public API designed in a hurry; vendor or framework lock-in | rushed-one-way-door | — |
| Rewriting a system from scratch | inside-view-forecast | paper-parachute |
| Copying big-company architecture at small scale | clever-over-boring | premature-abstraction |
| Big-bang global configuration push | paper-parachute | confounded-change |
| Changing many variables at once | confounded-change | — |
| Peeking at A/B tests; single-seed results | noise-as-signal | — |
| Tuning on the test set; best-of-N reporting | noise-as-signal | lab-not-field |
| Data leakage; benchmark contamination | lab-not-field | — |
| Train/serve skew (two code paths compute one feature) | integration-optimism | lab-not-field |
| Never looking at the data; label errors; watching the mean, missing the tail | proxy-worship | — |
| Silent data corruption while jobs "succeed" | paper-parachute | proxy-worship |
| Accepting an unrealistic deadline; ignoring base rates | inside-view-forecast | — |
| Fixing performance without profiling; blaming the first suspect in an incident | first-idea-lock-in | — |
| Flaky tests retried, alerts muted | normalized-warning | — |
| License, compliance or security discovered late; bus factor of one | unowned-risk | — |
| Asking an AI to validate the plan | echo-chamber | — |
| Project kept alive by "next milestone" promises | sunk-cost-drift | — |
