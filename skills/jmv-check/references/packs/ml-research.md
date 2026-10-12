# Pack: ML and research engineering (v1)
Scope: decisions about data, evaluation, training runs and model releases, from a single-GPU experiment to a multi-node pretraining run.

Each entry instantiates a pattern of the general taxonomy (maps_to: primary id, then secondary) and is cited by its own id, such as ml-03, in check outputs.

### ml-01 · Leakage through preprocessing or the split
- maps_to: lab-not-field (also: clever-over-boring)
- signals: imputation, scaling or feature selection fitted on the full dataset before the split; a random split on temporal or grouped data; a complex model beats the field's standard model by a wide margin.
- cheapest_test: refit every preprocessing step inside the training folds and rerun with a time-based or group-based split; stop if the margin over the standard model falls within the fold-to-fold spread.
- source: https://arxiv.org/abs/2207.07048 — leakage errors in 329 papers across 17 fields; in civil-war prediction, claims that complex models beat logistic regression failed to reproduce because of leakage.

### ml-02 · Silent correctness bugs in the training stack
- maps_to: integration-optimism (also: confounded-change)
- signals: a new gradient-accumulation, parallelism, precision or optimizer wrapper is adopted as "mathematically equivalent"; no parity run exists; a slightly higher loss is put down to another change made at the same time.
- cheapest_test: parity run of a few hundred steps on the same data and seed with the setting off and on (accumulation 1 vs N, TP=1 vs TP=N, old vs new optimizer); stop if the loss curves differ by more than the seed-to-seed spread.
- source: https://huggingface.co/blog/gradient_accumulation — in Transformers, losses did not match between runs with gradient accumulation toggled on and off; the correct loss divides by the total count of non-padding tokens.

### ml-03 · Big-run recipe change without a one-variable ablation
- maps_to: scale-before-signal (also: confounded-change)
- signals: a change enters the main run "because it's standard" or because a paper used it; several changes land together; the only evidence comes from another model size or codebase; nobody can name the ablation behind it.
- cheapest_test: small-scale ablation on the exact candidate config (same data, tokenizer and code path): baseline, A, B and A+B, two seeds each; stop if a change does not beat the baseline by more than the seed-to-seed spread.
- source: https://huggingface.co/spaces/HuggingFaceTB/smol-training-playbook (partly verified) — Hugging Face's pretraining playbook: "Never change anything unless you've tested that it helps" and "Change only one variable per ablation".

### ml-04 · Benchmark scores inflated by reuse and memorization
- maps_to: lab-not-field (also: noise-as-signal)
- signals: months of checkpoint or data-mix selection on the same public benchmarks; web data crawled after the benchmarks were published; no near-duplicate scan between training and eval sets; gains concentrated on older benchmarks.
- cheapest_test: score the model on about 100 fresh items written to mirror the benchmark, and scan the eval items for near-duplicates in the training data; stop if the fresh score is lower by more than its sampling error or any near-duplicate turns up.
- source: https://arxiv.org/abs/2405.00332 — on GSM1k, a fresh set built to mirror GSM8k, accuracy dropped by up to 8%, with a positive relationship between memorization and the gap.

### ml-05 · Training/serving skew
- maps_to: integration-optimism (also: lab-not-field)
- signals: serving features re-implemented in another language or service; features built from joins on tables that change; an offline gain with a flat online test, explained as noise; the old pipeline scheduled for removal at launch.
- cheapest_test: sample about 1,000 serving requests, recompute their features with the training code and diff them with the values served; stop if any feature differs on more than 1% of rows.
- source: https://developers.google.com/machine-learning/guides/rules-of-ml — Rules of ML 29, 31, 32 and 37: train on features saved at serving time, beware joined tables that change, reuse code across training and serving, measure the skew.

### ml-06 · Hyperparameters carried across scale
- maps_to: lab-not-field (also: scale-before-signal)
- signals: init std, learning rate or warmup copied from a smaller or narrower model ("it was stable at 13B"); early attempts spike near the end of warmup; the model size is read from the config file, not from the running job.
- cheapest_test: short runs at the target width through the end of warmup, logging grad norm and loss scale, with parameter count and tokens per step printed by the running job; stop if grad norm spikes or the realized size differs from the design.
- source: https://github.com/bigscience-workshop/bigscience/blob/master/train/tr8-104B-wide/chronicles.md (partly verified) — BigScience 104B log: repeated divergences, a config bug that made it "a very lopsided 58B model instead of 104B all along", and a smaller init std (0.006) as the breakthrough.

### ml-07 · Undeclared consumers of a model's outputs
- maps_to: integration-optimism (also: unowned-risk)
- signals: other teams read the scores, embeddings or labels, and no list of them exists; downstream thresholds were tuned on the old model's score distribution; "it's just a model refresh".
- cheapest_test: list every reader of the outputs from access logs, and compare old and new score quantiles on the same inputs; stop if any reader was unknown to you or a quantile moves past a threshold a reader uses.
- source: https://papers.nips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html — Sculley et al. 2015 list undeclared consumers, entanglement and data dependencies among the hidden maintenance costs of ML systems.

### ml-08 · Memory and throughput plan validated on a smoke test
- maps_to: lab-not-field (also: paper-parachute)
- signals: the plan rests on a smoke test of a few steps; checkpoint save and restore not yet exercised; tensor parallelism spans nodes; a very large data-parallel degree with no check of compute/communication overlap.
- cheapest_test: run the exact config for a few hundred steps, including one checkpoint save and restore, profiling memory and step time; stop if memory after the first optimizer step leaves no headroom, the restore fails, or step time misses the plan.
- source: https://huggingface.co/spaces/nanotron/ultrascale-playbook (partly verified) — memory rises after the first step once optimizer states exist; tensor parallelism is usually kept within a node; past about 512 GPUs, data-parallel communication can no longer be fully overlapped.

### ml-09 · Budgeting a long run for the happy path
- maps_to: inside-view-forecast (also: paper-parachute)
- signals: timeline = tokens / measured throughput, with a thin margin; a new cluster with no burn-in; manual restarts; a checkpoint interval set by habit; an external date committed before launch.
- cheapest_test: write a failure budget from published interruption rates scaled to your GPU count, and set checkpoint interval, restart automation and on-call from it; stop if the committed date does not survive that budget plus a one-week burn-in.
- source: https://arxiv.org/html/2407.21783 — Llama 3 paper, §3.3.4: 466 job interruptions in a 54-day pre-training snapshot, 419 of them unexpected, about 78% of those attributed to hardware.

### ml-10 · No playbook for loss divergence
- maps_to: paper-parachute (also: normalized-warning)
- signals: no written response to loss spikes; only the last few checkpoints kept; loss scale and activation norms not tracked; "we'll deal with spikes if they happen".
- cheapest_test: write the divergence runbook (how far to roll back, how much to lower the LR, whether to skip batches), keep checkpoints spaced well back, alert on loss-scale collapse, then rehearse one restart from an old checkpoint; stop if the rehearsal fails or takes more than an hour.
- source: https://ar5iv.labs.arxiv.org/html/2205.01068 — OPT-175B, §2.5: divergences coincided with the dynamic loss scaler crashing to 0 and spikes in final-layer activation norm; the team restarted from earlier checkpoints with a lower learning rate.

### ml-11 · Stragglers and hangs nobody is watching for
- maps_to: paper-parachute (also: normalized-warning)
- signals: no per-GPU benchmark before launch; no collective-communication timeout and no hang watchdog; in-loop eval and checkpoint code rarely exercised; a few percent of throughput lost without explanation.
- cheapest_test: run a per-node burn-in benchmark, set collective timeouts with async error handling and a heartbeat that pages a person, then force one hang; stop if any node runs more than 5% below the median or the forced hang pages nobody within 15 minutes.
- source: https://github.com/bigscience-workshop/bigscience/blob/master/train/tr11-176B-ml/chronicles.md — BLOOM 176B log: one slow GPU cut throughput from 149 to 140 TFLOPs; an eval hang with no NCCL timeout left GPUs "spinning at 100%" for about 18 hours.

### ml-12 · Learning from inputs you don't control
- maps_to: lab-not-field (also: paper-parachute)
- signals: user conversations, clicks or ratings feed training or memory automatically; testers were cooperative; an open public launch with publicity; no cap on what one user or a coordinated group can push into the loop.
- cheapest_test: have a few accounts coordinate on one target behavior against a staging copy of the loop, then trigger the kill switch; stop if outputs move on that behavior, nothing caps one account's share of the next update, or the switch fails to halt learning.
- source: https://blogs.microsoft.com/blog/2016/03/25/learning-tays-introduction/ — Microsoft on Tay (2016): "a coordinated attack by a subset of people exploited a vulnerability"; the team had not foreseen the possibility.

### ml-13 · Tokenizer locked in without a downstream probe
- maps_to: rushed-one-way-door (also: first-idea-lock-in)
- signals: a tokenizer trained for other languages or domains is reused; no tokens-per-character measurement on target data; context length and price are counted in tokens; "the data mix will fix it".
- cheapest_test: measure tokens per character on target samples with the current tokenizer and with one retrained on target data; stop if the current tokenizer needs more than 20% extra tokens for the same text.
- source: https://arxiv.org/abs/2305.15425 — the tokenized length of the same content differs up to 15 times across languages, which changes cost, latency and usable context.

### ml-14 · Scaling-law extrapolation from runs set up differently from the target
- maps_to: lab-not-field (also: proxy-worship)
- signals: the small runs share one LR schedule or token budget that doesn't match their size; losses at smaller budgets read from intermediate checkpoints; the fit extrapolates an order of magnitude or more with no held-out scale point; R² is the main argument.
- cheapest_test: refit without the largest small run and predict its loss, then rerun two small points with schedules matched to their token counts; stop if the prediction misses by more than the run-to-run spread or the optimum moves.
- source: https://ar5iv.labs.arxiv.org/html/2203.15556 — Chinchilla: earlier fits used one token count and LR schedule for all model sizes; with matched schedules, Chinchilla (70B) "uniformly and significantly outperforms Gopher (280B)" at the same compute.

### ml-15 · Decontamination filter never tested with planted positives
- maps_to: paper-parachute (also: lab-not-field)
- signals: the removal rate "looks plausible"; per-benchmark format adapters; normalization choices nobody tested; the run cannot be redone.
- cheapest_test: plant exact and lightly perturbed benchmark items in a shard, run the filter and log hits per benchmark; stop if any planted item survives.
- source: https://ar5iv.labs.arxiv.org/html/2005.14165 — GPT-3, §2.2: "a bug in the filtering caused us to ignore some overlaps", and retraining was not feasible given the cost.
