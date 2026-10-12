---
type: llm
weight: 3
---
Judge whether the agent's review names the failure mechanism that actually sank this plan. The agent saw only the plan below, never the outcome.

Plan the agent reviewed:
"""
Next Tuesday our creator analytics page and the partner reporting API switch their headline number from total plays to a new metric, average watch time, and sales starts quoting it in the media kit for advertisers. It is total watch time divided by the number of qualified views. Total watch time comes from the playback events table, which logs every play; qualified views come from the views rollup, which counts plays of 3 seconds or more, our standard view definition since 2019. Both tables already feed billing, so they are well tested. On last month's data the new metric runs about 70% above the old time-per-play figure, which we put down to the 3-second rule screening out accidental autoplays. Advertisers will set next year's budgets with it, comparing us with other platforms. Partners' dashboards pull the API nightly, and our partner terms require 90 days' notice to change a published definition.
"""

Hidden ground truth, what happened next: "The numerator counted watch time from every play, while the denominator counted only plays of 3 seconds or more, so the metric overstated average watch time; the 70% jump was that mismatch, not autoplay screening. Advertisers budgeted on it for over a year, until an agency's own measurements did not match. The company had to publish a correction, replace the metric under a new name and answer advertisers' claims, and its self-reported metrics lost credibility. In the original case, the metric was defined as total watch time divided by everyone who played the video but calculated with only the views of three seconds or more in the denominator; an agency put the overstatement at 60 to 80% over about two years, and an advertisers' class action was settled for $40 million."

Source: public case, transposed. Facebook's statement of September 2016, quoted by TechCrunch (22 September 2016): defined as "total time spent watching a video divided by the total number of people who have played the video", calculated as "the total time spent watching a video divided by only the number of people who have viewed a video for three or more seconds"; Publicis Media told The Wall Street Journal the error inflated the metric by 60 to 80 percent. https://techcrunch.com/2016/09/22/facebook-miscalculation-significantly-inflated-average-video-view-times-for-years/ ; settlement: https://www.marketingdive.com/news/facebook-nears-40m-settlement-of-advertiser-lawsuit/564534/

Mechanism to look for: Average watch time divides watch time from every play (the playback events table) by only the plays of 3 seconds or more (the views rollup). Numerator and denominator count different plays, so the metric is inflated, and the 70% jump over the old figure is that mismatch, explained away as autoplay screening. Once it is published to partners and advertisers, with 90 days' notice needed to change the definition, the inflated number drives their budgets.

How to grade:
1. List the distinct risks or concerns in the agent output, in order of first appearance, wherever they appear (a risk list, a "cheapest test" line, prose). Count each distinct concern once. Ignore any decision record printed between BEGIN and END lines.
2. PASS if one of the first three concerns names this mechanism, or names the plan fact that leads to it and says how that fact makes the plan fail. Paraphrase is fine. Examples that count: numerator and denominator count different sets of plays; short plays add watch time but no views; the 70% rise is a symptom of the definition, not of autoplay screening; compute both consistent versions and compare before publishing.
3. FAIL if the mechanism is absent; if it appears only as a generic label with no link to this plan's facts (for example "document the metric definition", "validate the data", "partners may misread a new metric", "API load", with no link to the numerator and denominator counting different plays); or if it first appears as the fourth concern or later.
