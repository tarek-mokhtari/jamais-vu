---
type: llm
weight: 3
---
Judge whether the agent's review names the failure mechanism that actually sank this plan. The agent saw only the plan below, never the outcome.

Plan the agent reviewed:
"""
On 1 March we start enforcing a free-tier quota on our public maps API: requests without an API key get 1,000 per hour per client IP address, then HTTP 429. Keyless traffic is about 40% of our requests, and its CDN bill keeps rising. In February's logs, 98% of client IPs stayed under 1,000 requests in their busiest hour, so few users should notice, and anyone who needs more can create a free key in a minute. The 2% above the line, mostly mobile-carrier and cloud address ranges, send about half of keyless requests; we assume most of that is scraping. Many partners' mobile apps call us without a key, straight from their users' phones. We announced the change in the changelog and emailed every registered account 30 days ahead. The new prices for the paid tiers take effect the same day.
"""

Hidden ground truth, what happened next: "Mobile carriers put thousands of phones behind each public address. On 1 March, carrier gateways crossed 1,000 keyless requests within minutes of the morning peak, and partners' apps showed blank maps for whole carriers' customers. Partners could not ship keyed app versions for days (store review, users who do not update), so carrier ranges were exempted in an emergency and the quota suspended, while the new paid-tier prices stood; two large partners moved to another provider. The 98% of addresses under the line were mostly single users; the 2% above it were where most real users were."

Source: synthetic composite, grounded in RFC 6269, "Issues with IP Address Sharing" (IETF, June 2011), §13.1: "In the presence of widespread large-scale address sharing, penalty box solutions to service abuse simply will not work", and "one user who fails a number of login attempts may block out other users". https://www.rfc-editor.org/rfc/rfc6269.html

Mechanism to look for: The quota is keyed on the client IP address, and its impact was judged by the share of addresses under the limit. One address is not one user: mobile carriers (carrier-grade NAT) and cloud gateways put many users behind one address, and the 2% of addresses above the line, mostly carrier ranges, carry about half of keyless traffic, including partners' apps calling from users' phones. At enforcement those shared addresses are throttled together, and the apps of whole carriers' customers fail.

How to grade:
1. List the distinct risks or concerns in the agent output, in order of first appearance, wherever they appear (a risk list, a "cheapest test" line, prose). Count each distinct concern once. Ignore any decision record printed between BEGIN and END lines.
2. PASS if one of the first three concerns names this mechanism, or names the plan fact that leads to it and says how that fact makes the plan fail. Paraphrase is fine. Examples that count: one IP stands for many users behind carrier-grade NAT; the 98% of IPs under the limit says nothing about users; the mobile-carrier ranges above the line are partners' app users, not scrapers; partners cannot add keys to apps already on users' phones by 1 March.
3. FAIL if the mechanism is absent; if it appears only as a generic label with no link to this plan's facts (for example "communicate with partners", "scrapers will adapt", "set up rate-limit monitoring", "pricing backlash", with no link to many users sharing one IP address); or if it first appears as the fourth concern or later.
