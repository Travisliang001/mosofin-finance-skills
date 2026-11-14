<!-- kpi-dashboard-builder · edge-cases.md · read for: Stage 3, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**Vanity metrics**: **total registered users, cumulative downloads, gross bookings without churn context —
these can look good while the business struggles. Steer toward metrics that reflect real health** — net
retention, unit economics, cash.

**Definition inconsistency over time**: **if the entity changed how it defines a KPI — e.g. redefined
"active user" — historical trends break. Note the definition change and restate history if possible.**
*Mosofin note*: **a stored query recipe prevents this for `[auto]` metrics**, which is most of the financial
set.

**KPIs that conflict**: **optimizing one metric can hurt another — growth vs. burn, utilization vs. quality.
Show the trade-off rather than a single metric in isolation.**

**Insufficient history for trends**: **a young company may have only a few months. Show what exists; don't
fabricate trend lines.** *Mosofin note*: **how many periods exist is `[auto]`** — check before designing a
24-month trend.

**Cohort metrics with small cohorts**: **retention and LTV from tiny cohorts is noisy. Flag the sample size;
avoid over-interpreting.**

**Seasonality**: **MoM comparisons can mislead in seasonal businesses. Use YoY or trailing-twelve-months for
seasonal metrics.** *Mosofin note*: **seasonality is measurable** from the monthly history — test for it
rather than assuming either way.

**Targets not provided**: **don't invent targets or benchmarks. Show actuals and trends; mark targets as
"TBD" until the user supplies them.**

**Benchmark data quality**: **industry benchmarks vary widely in reliability. Only show benchmarks from
sources the user trusts; cite the source.**

**Audience mismatch**: **a board dashboard differs from an operational one. Match the metric depth and
granularity to who's reading it.**

**Real-time vs. period-close metrics**: **some metrics — cash, pipeline — can be real-time; others — margin,
net income — need a closed period. Label which is which to avoid mixing unclosed estimates with final
numbers.** *Mosofin note*: **this is sharper here, because every read is live.** **A margin computed from an
open period is a partial-month figure**, and it will be read as a monthly result. **Label the period status
on every tile.**

**ARR derived from recognised revenue** — *Mosofin-specific, and the most damaging error available*. **They
diverge constantly.** Without a billing system, **leave it blank.**

**Churn derived from revenue decline** — *Mosofin-specific*. Same problem. A large customer paying annually
in arrears looks like churn every year.

**A customer count derived from invoice counts** — *Mosofin-specific*. Not the same thing, and it breaks
every per-customer metric built on it.

**A dashboard built entirely from financial metrics** — *Mosofin-specific*. **Financial metrics are lagging
by construction.** Say so when scoping; let the user choose knowingly.

**A tile with no data source** — *Mosofin-specific*. **Worse than one fewer tile.** Decline the metric at
selection and record it on the Not Available tab.

**Ratios averaged across entities** — *Mosofin-specific*. **Compute group ratios from group components**,
never from entity ratios.

**Group revenue including intercompany** — *Mosofin-specific*. Overstates revenue and every metric built on
it. Eliminate first.

**Growth that is entirely FX** — *Mosofin-specific*. In a multi-currency group, **state the rate basis**.

**A result comes back with `mock: true`** — *Mosofin-specific*. **Dashboards go to boards and investors.**
Label it on the face.

**A stored metric value is reused** — *Mosofin-specific*. It would be shown as current. **Persist the
recipe; recompute the value.**

**A stored recipe applied to another entity** — *Mosofin-specific*. Recipes name accounts. The same label
would compute something different.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the metric as `[gated]` in the coverage sheet.
