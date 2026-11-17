<!-- tax-planning-and-projections · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All ten preserved, in order.

**Marginal versus effective rate confusion**: **planning decisions hinge on the marginal rate — the rate on the next or last dollar — not the average. Use the marginal rate to evaluate incremental moves.** `[auto]` to compute both, **and both are always shown.** Presenting only the effective rate is how this confusion happens.

**Crossing a threshold or bracket**: **some decisions push income across a threshold — a higher bracket, loss of an allowance, a surcharge. Model the cliff effect, not just a smooth rate.** **`[auto]`** — Step 2b, and note that a withdrawal can create a band whose **effective marginal rate exceeds the top rate**, which no bracket table shows.

**Timing benefits are often deferral, not savings**: **deferring income usually defers tax rather than eliminating it — a timing and cash benefit. Be clear whether a move is a permanent saving or just deferral.** `[auto]` to distinguish; **a column on Sheet 5, not a footnote.**

**Owner-managed business extraction**: **salary versus dividend versus retained profit has significant combined — corporate + personal + social-contribution — tax effects. Model the total, not one layer. Highly jurisdiction-specific.** **`[manual]`** — see Gate 1. **The corporate layer alone is available and modelling it alone is the characteristic error.**

**Estimated-payment safe harbours**: **paying based on prior-year tax can avoid penalties even where the current year is higher — jurisdiction-specific. Use the safe harbour to size estimates when the current projection is uncertain.** **`[auto]` for the prior-year figure**; `[manual]` for the rule. **This is genuinely useful when the projection is shaky**, because it substitutes a known number for an uncertain one.

**Self-employment and social contributions**: **often a large component alongside income tax; include them or the projection understates the true burden.** `[manual]` for the rules; `[auto]` for the base. **A projection omitting these is not a partial answer — it is a wrong one**, and it is wrong in the direction that leaves the taxpayer short.

**Capital gains timing**: **holding-period thresholds, annual exemptions and loss harvesting can materially change tax — but watch anti-avoidance**, such as wash-sale-type rules. `[auto]` for realised gains in the books; `[manual]` for the rest. **The anti-avoidance interaction makes this a specialist area**, not a modelling exercise.

**Cross-border**: **residency, foreign income and treaties make planning complex — specialist required.** `[manual]`, entirely. **`[auto]` for one relevant fact**: whether the books show foreign income, foreign currency transactions or foreign entities — which establishes that the question exists. See `foreign-currency-translation-asc830` and the transfer pricing documentation.

**Anti-avoidance rules**: **aggressive arrangements can be challenged under general anti-avoidance rules even where technically compliant. Flag and recommend specialist advice; don't promote aggressive schemes.** `[manual]`. **"Technically compliant" is the operative phrase** — a model can show a scheme working arithmetically and say nothing whatever about whether it survives challenge.

**Rules change**: **rates, brackets and reliefs change, often annually and sometimes mid-year. Always confirm current parameters; mark projections as estimates subject to rule confirmation.** `[manual]`. **The original's own statement of the seed principle**, and it governs this file.
