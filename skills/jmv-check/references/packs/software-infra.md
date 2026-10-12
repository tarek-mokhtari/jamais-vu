# Pack: Software architecture and infrastructure (v1)
Scope: decisions about service design, deploys, configuration, data formats, backups, recovery and migrations in production systems.

Each entry instantiates a pattern of the general taxonomy (maps_to: primary id, then secondary) and is cited by its own id, such as sw-03, in check outputs.

### sw-01 · Changes that look reversible but write state old code can't read
- maps_to: paper-parachute (also: rushed-one-way-door)
- signals: the new version writes a new data, serialization or protocol format; readers and writers change in the same deployment; "we can always roll back"; staging never runs old and new versions side by side.
- cheapest_test: in staging, run old and new versions together, let the new one write, then roll it back; stop if any old instance fails on a record the new one wrote.
- source: https://builder.aws.com/content/3F04j2yRAAMBuPSPs50xwXZqg01/ensuring-rollback-safety-during-deployments — Amazon Builders' Library: "the most common reason for not being able to roll back is a change of protocol"; the fix is a two-phase deployment, readers first (prepare), then writers (activate).

### sw-02 · "Config" pushed everywhere at once because it must be fast
- maps_to: paper-parachute (also: lab-not-field)
- signals: rules, config or content skip the staged rollout "to respond quickly"; a log-only or simulate mode is assumed safe although the code still runs; validation checks syntax, not runtime cost or bounds; replication reaches every region in seconds.
- cheapest_test: canary the change to one location or 1% of traffic for minutes, and replay a traffic sample through it with a CPU or time budget per rule; stop if any rule exceeds its budget or the canary's errors or CPU rise.
- source: https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/ — Cloudflare, July 2019: a non-emergency WAF rule change went global without a staged rollout, and "even in the simulate mode the rules actually need to execute"; a 27-minute outage followed.

### sw-03 · Backups that have never been restored
- maps_to: paper-parachute (also: unowned-risk)
- signals: backup jobs are "green" but nobody has restored from them recently; failure notices go by email; several backup mechanisms, each assumed to be someone else's; no named owner for data durability.
- cheapest_test: restore last night's backup to a scratch host and compare row counts and the latest timestamp with production; stop if the restore fails, misses the recovery-time target, or the data is stale.
- source: https://about.gitlab.com/blog/2017/02/10/postmortem-of-database-outage-of-january-31/ — GitLab, January 2017: pg_dump backups failed on a version mismatch, the failure emails were rejected, disk snapshots were off, and the restore came from a manual snapshot about 6 hours old.

### sw-04 · Alerts that aren't alerts
- maps_to: paper-parachute (also: normalized-warning)
- signals: failure notices go by email to a group list; nobody owns them or has seen one fire in a test; messages are labeled "informational" and routinely go unread.
- cheapest_test: trigger on purpose each failure that should block a release or a backup, and record who gets paged; stop if no named person is paged within 15 minutes.
- source: https://www.sec.gov/litigation/admin/2013/34-70694.pdf — SEC order on Knight Capital (2013): 97 automated emails referencing "Power Peg disabled" went out before the market open, but such messages were not designed to be system alerts.

### sw-05 · Destructive command with an ambiguous target
- maps_to: rushed-one-way-door (also: paper-parachute)
- signals: commands run by hand against production, during an incident or late at night; IDs or hosts of different types that look alike; an API that "assumes the input is correct"; a tool that can remove more than the minimum safe capacity.
- cheapest_test: run the command in dry-run mode on the exact input and compare the listed targets, their count and their type, with the request; stop if anything differs or the targets have no soft-delete or restore path.
- source: https://www.atlassian.com/engineering/post-incident-review-april-2022-outage — Atlassian, April 2022: the IDs of entire cloud sites were supplied instead of app IDs, causing "an immediate deletion of 883 sites (representing 775 customers)".

### sw-06 · Recovery stampede
- maps_to: lab-not-field (also: paper-parachute)
- signals: every task restarts at once after a crash; retries without randomized exponential backoff; the dependencies behind the service are sized for steady state.
- cheapest_test: in staging, restart the whole fleet at once against a realistic copy of the dependency and watch its load; stop if its latency or error rate leaves steady-state limits or any client retries without jitter.
- source: https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW — Google Cloud, June 2025: restarting tasks "created a herd effect on the underlying infrastructure it depends on", with no randomized exponential backoff in place.

### sw-07 · Repurposed flags, dormant code and an unverified manual deploy
- maps_to: load-bearing-shortcut (also: paper-parachute)
- signals: a new feature reuses a flag, enum value or ID that once meant something else; old code is still deployed and callable; a manual deploy across many servers with no second check; nothing confirms every host runs the same build before the switch.
- cheapest_test: search the deployed code for every path that reads the reused flag, and have each host report its build hash before enabling; stop if the flag reaches dead code or any host reports a different build.
- source: https://www.sec.gov/litigation/admin/2013/34-70694.pdf — SEC order on Knight Capital: new code "repurposed a flag that was formerly used to activate the Power Peg code" and missed one of eight servers; over 4 million executions in about 45 minutes and a loss above $460 million.

### sw-08 · Big-bang rewrite
- maps_to: inside-view-forecast (also: paper-parachute)
- signals: "the code is a mess"; the estimate comes from the new design and a fast prototype, not from an inventory of the old system's behaviors; nothing ships until the new system replaces the old one; feature work is frozen while competitors keep shipping.
- cheapest_test: inventory the special cases of one representative module (blame its odd-looking lines: each is usually a bug fix), estimate them and scale by the module count; stop if the corrected estimate exceeds the feature freeze the product can afford.
- source: https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/ — Spolsky on Netscape's rewrite, "the single worst strategic mistake that any software company can make": "When you throw away code and start from scratch, you are throwing away all that knowledge."

### sw-09 · One service per unit, ahead of need
- maps_to: clever-over-boring (also: premature-abstraction)
- signals: one service, repo or queue per customer or integration, with the count rising; a small team; shared code copied into libraries every service imports; the real problem (isolation, head-of-line blocking) fits in one process; "ops will be automated with templates".
- cheapest_test: multiply per-service ops cost (deploys, library upgrades, alerts) by the count projected in two years, and prototype per-unit queues or workers inside one service; stop if the projection exceeds the team's ops capacity or the prototype already gives the isolation needed.
- source: https://www.twilio.com/en-us/blog/developers/best-practices/goodbye-microservices — Segment, 2018: with over 140 services, "our operational overhead increased linearly with each added destination", and "As our velocity plummeted, our defect rate exploded."

### sw-10 · Big-bang migration on a fixed date
- maps_to: scale-before-signal (also: rushed-one-way-door)
- signals: every customer moves in one cutover; the go-live date is fixed outside engineering; readiness is reported by the supplier building the platform; no production cohort has run on the new platform for weeks; the rollback is unrehearsed.
- cheapest_test: write go/no-go criteria with a reviewer independent of the builder, and check today's evidence against them; stop if no real cohort (staff, one region) has run on the new platform in production, or a criterion cannot be met by the date.
- source: https://www.bankofengland.co.uk/news/2022/december/tsb-fined-for-operational-resilience-failings (partly verified) — PRA and FCA, 2022: after TSB's April 2018 migration the platform "immediately experienced technical failures" affecting many of its 5.2 million customers; the firm "failed to plan for the IT migration properly".

### sw-11 · A single automated check as the last line of defense
- maps_to: paper-parachute (also: proxy-worship)
- signals: one validator or audit tool stands between an operator command and a global outage; the guard has never been fed a known-bad input; refactors touch safety code that has no tests.
- cheapest_test: feed the guard one known-bad input for each failure it is meant to block, and keep those cases in CI; stop if any known-bad input passes.
- source: https://engineering.fb.com/2021/10/05/networking-traffic/outage-details/ — Meta, October 2021: a maintenance command took down the backbone because "a bug in that audit tool prevented it from properly stopping the command".

### sw-12 · Changing a shared critical dependency at peak load
- maps_to: lab-not-field (also: paper-parachute)
- signals: one cluster of a core dependency serves many workloads; a new feature of it is enabled for a high-load service, often just before the busiest period; no isolated cluster to try it on.
- cheapest_test: enable the feature on a separate cluster serving one workload under replayed peak traffic for an hour, and time a full disable; stop if latency or CPU degrades or disabling takes more than a few minutes.
- source: https://about.roblox.com/newsroom/2022/01/roblox-return-to-service-10-28-10-31-2021 — Roblox, October 2021: a streaming feature enabled on the traffic-routing backend contributed to a 73-hour outage, made worse by "a single Consul cluster supporting multiple workloads".

### sw-13 · Monitoring and recovery tools that share fate with the system
- maps_to: paper-parachute (also: integration-optimism)
- signals: dashboards, auth, deploy tools or the status page run on the infrastructure they watch; the break-glass procedure has not been practiced recently; credentials time out during long incidents.
- cheapest_test: draw the dependency graph of the recovery path itself (telemetry, auth, deploy, status page) and run one break-glass login with the main system assumed down; stop if any recovery step depends on the system it is meant to recover.
- source: https://about.roblox.com/newsroom/2022/01/roblox-return-to-service-10-28-10-31-2021 — Roblox, October 2021: "There was a circular dependency between our telemetry systems and Consul", the system that had failed.

### sw-14 · Recovery built for a smaller failure
- maps_to: paper-parachute (also: lab-not-field)
- signals: restore or restart procedures exercised only for one tenant or one node; "we've never had to cold-start X"; recovery-time estimates nobody has measured.
- cheapest_test: in staging, restore or cold-start the largest batch you can, time it and extrapolate to the worst plausible event; stop if the extrapolated time exceeds the recovery target or any step needs per-tenant manual work.
- source: https://aws.amazon.com/message/41926/ — AWS S3, February 2017: the team had "not completely restarted the index subsystem or the placement subsystem in our larger regions for many years", and the restart took longer than expected.

### sw-15 · Automated failover acting outside its tested envelope
- maps_to: lab-not-field (also: rushed-one-way-door)
- signals: failover tested by killing hosts but never by partitioning the network; cross-region promotion allowed without a human; applications never run against a database in another region.
- cheapest_test: in staging, partition the primary's network for under a minute and inject cross-region latency into the application path; stop if the orchestrator promotes a primary across regions or the application fails at that latency.
- source: https://github.blog/news-insights/company-news/oct21-post-incident-analysis/ — GitHub, October 2018: connectivity returned in 43 seconds, but the orchestrator had already moved primaries to the West Coast; unreplicated writes made failing back unsafe, and service was degraded for 24 hours 11 minutes.
