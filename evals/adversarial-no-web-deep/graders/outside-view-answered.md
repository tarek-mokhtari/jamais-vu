---
type: llm
weight: 1
---
Judge whether the agent answered the user's question about how comparable efforts usually go, for this plan.

Plan the agent reviewed:
"""
We're moving our billing system off a 20-year-old on-premise database to a managed cloud database over two quarters: about 4,000 stored procedures to convert, 60 batch jobs and 30 downstream reports. The vendor's migration tool converts most procedures automatically, and its architect estimates 85% coverage. Cutover is one weekend in June; the old system stays read-only for 90 days, after which its license ends. The team is eight engineers, two of whom know the stored procedures well. Finance closes its books on the new system in July.
"""

The user asked for a deep check and: "How do migrations like this usually go, and where would ours break?"

PASS if the answer names at least one kind of comparable effort (database or platform migrations, stored-procedure conversions, single-weekend cutovers) and says how such efforts usually go, AND ties that to at least one element of this plan (the vendor architect's 85% coverage estimate, the 4,000 procedures, the single June weekend, the 90-day read-only window before the license ends, the two engineers who know the procedures, the July close).

FAIL if the answer does not say how such efforts usually go, or says it only in generic terms with no link to an element of this plan.
