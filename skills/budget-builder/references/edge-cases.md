<!-- budget-builder · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**Startup with little history**: driver-based and bottoms-up — the only option without history.
Heavy assumption documentation; **build conservative / base / aggressive cases.** *Mosofin note*:
check what history actually exists before concluding there is none; a connector added part-way
through last year may still hold several usable months.

**Rapidly growing company**: linear growth assumptions break down. **Model capacity constraints
(hiring ramps, infrastructure scaling) explicitly** — revenue that requires staff you have not
budgeted to hire is not a plan.

**Highly seasonal business**: monthly seasonality is essential. **Don't divide annual by 12. Use
historical monthly patterns.** *Mosofin note*: this is directly measurable — pull the monthly P&L
across several years and use the entity's own shape. If the monthly breakdown is unavailable, say
the seasonal pattern is unevidenced rather than smoothing.

**Multi-entity / multi-currency**: budget each entity in its functional currency; consolidate at
budgeted FX rates. **Flag FX assumption sensitivity.**

**Project-based revenue (lumpy)**: budget by project with start / end timing rather than smooth
monthly revenue. Tie to the revenue recognition review for recognition timing.

**New product / market launch**: build the launch curve explicitly (slow ramp, inflection,
maturity) rather than assuming immediate run-rate.

**Cost-reduction mandate**: ZBB on discretionary lines; **document the savings vs. prior year and
the operational changes enabling them.** A saving with no operational change behind it will not
happen.

**Capex-heavy business**: capex feeds depreciation (which hits the P&L) and cash (which hits the
model). Coordinate with `three-statement-financial-model`.

**Headcount-driven cost base**: get the hiring plan right — **timing of hires materially affects
the annual cost. A hire starting in month 9 costs a third of a full-year hire.** This is the
single most common source of budget error, which is why Step 7 flexes it.

**Budget needs board approval with specific format**: match the board's expected presentation.

**A budget already exists in the system** — *Mosofin-specific*. Read it before building. Replacing
an approved budget without saying so destroys the comparison base every future variance analysis
depends on.

**An assumed rate was used where the entity's own is derivable** — *Mosofin-specific*. Inflation
and tax rates genuinely must be supplied, but the **payroll loading rate and cost ratios must not
be assumed** when the ledger holds them. Derive, show the derivation, and cite the period.

**Only annual figures are available** — *Mosofin-specific*. Seasonality cannot be derived from an
annual total. Ask for the pattern rather than dividing by twelve.

**Historical ratios are drifting, not stable** — *Mosofin-specific*. A COGS percentage that has
moved steadily over three years should not be projected flat at its average. Show the trend and
ask which point on it to budget.

**A company file is connected but not active** — *Mosofin-specific*. Name it as excluded and say
which part of the group is therefore unbudgeted. Surface any `reconnect_url`.

**A result comes back with `mock: true`** — *Mosofin-specific*. A budget built on fixture data will
still be approved and measured against. Say so at the top and do not present it as ready.

**A stored driver structure no longer fits** — *Mosofin-specific*. A business that has changed
model — added a subscription line, dropped a product — needs its structure revisited, not reused.
Check the stored structure against this year's actual revenue mix.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it.
Never apply it to a different entity; never drop it silently.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
