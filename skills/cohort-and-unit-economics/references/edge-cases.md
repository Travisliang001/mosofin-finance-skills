<!-- cohort-and-unit-economics · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**LTV on revenue instead of margin**: **the most common error.** Always compute LTV on contribution
margin. **A revenue-based LTV/CAC of 3.0 might be a margin-based 0.6 — a money-losing business.**

**Survivorship in young cohorts**: recent cohorts have only a few months of data; **don't extrapolate
their full lifetime from a short window. Mark them as incomplete.**

**Constant-churn assumption breaking down**: **1/churn overstates lifetime if churn is front-loaded**
(high early churn, low later churn). **Use the actual curve** — which, here, you have.

**Expansion masking churn**: net revenue retention can look great (>100%) while **logo churn is
high** — a few accounts expanding while many small ones leave. **Show both logo and revenue
retention.**

**CAC attribution timing**: marketing spend and customer acquisition don't align perfectly in time. **A
simple same-period ratio can distort during rapid spend changes. Use a matched window.**

**Blended CAC hiding bad channels**: a cheap organic channel can mask an unprofitable paid channel.
**Always look by channel where possible.** *Mosofin note*: in an accounting-only workspace it is **not**
possible — report blended CAC and name the gap explicitly, rather than presenting blended as though it
were the whole story.

**One-time vs. recurring revenue in LTV**: **include only the recurring / repeatable contribution**;
one-time setup fees are a separate consideration. *Mosofin note*: often separable by item
(*`search_items`*) — check before lumping them in.

**Discounting**: for long-lived customers, undiscounted LTV overstates value. **Use a discount rate for
a rigorous LTV, especially if the user is using LTV for valuation.**

**Marketplace / two-sided models**: unit economics differ — **analyze both supply and demand sides, and
the take rate.**

**Cohorts affected by a one-time event** (pricing change, major outage, pandemic): **flag distorted
cohorts; don't blend them naively into the average.**

**Negative contribution customers**: **some customers cost more to serve than they pay.** Segment
analysis reveals them; they drag LTV. *Mosofin note*: a uniform company-wide margin **cannot** reveal
them — that is precisely what it averages away. Say so whenever a single margin was applied.

**"Active" is not a field in the books** — *Mosofin-specific*. It must be operationalised as
transacting within a window. **State the window**, and widen it for irregular or quarterly billing or
you will manufacture churn.

**Acquisition date from first invoice differs from signup** — *Mosofin-specific*. Free trials, delayed
first billing and backdated invoices all shift the cohort boundary. State the definition and note the
likely lag.

**History does not reach far enough** — *Mosofin-specific*. A connector added recently cannot evidence
older cohorts. **State the earliest cohort available**; a missing cohort is unobservable, not zero, and
a retention curve that appears to start mid-life is a data artefact.

**Aggregate revenue used instead of customer-level** — *Mosofin-specific*. Flat total revenue can hide
severe churn offset by acquisition. Never build retention from totals.

**Credits and refunds left in cohort revenue** — *Mosofin-specific*. A refunded month counted as
revenue overstates retention. Net them.

**A company file is connected but not active** — *Mosofin-specific*. Name it as excluded and say which
customers are therefore missing. If that entity holds a distinct customer type, note that the curves
are biased, not merely smaller.

**A result comes back with `mock: true`** — *Mosofin-specific*. Retention curves and an LTV/CAC verdict
drive real investment decisions; fixture data cannot support them.

**A stored cohort definition changed** — *Mosofin-specific*. Changing the cohort period, the acquisition
test or the active window moves every historical curve. Flag the change rather than presenting a
silently re-based comparison.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it. Never
apply one entity's definitions to another; never drop it silently.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
