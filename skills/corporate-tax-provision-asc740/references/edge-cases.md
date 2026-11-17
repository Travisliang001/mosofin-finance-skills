<!-- corporate-tax-provision-asc740 · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**Enacted rate change**: when a new rate is enacted, **remeasure all deferred balances at the new rate
immediately** (US GAAP: enacted; IFRS: enacted or substantively enacted). **The remeasurement can swing
the provision materially in the enactment period** — and it is a reconciling item on its own ETR line, so
it should never be buried in "Other".

**Cumulative losses (strong negative evidence)**: **a recent history of losses is significant negative
evidence making it hard to support DTA realizability — often drives a full valuation allowance. Document
carefully.** *Mosofin note*: measure it. Three years of pre-tax results is one read, and a measured
cumulative loss is far stronger documentation than a narrative assertion.

**Multi-jurisdiction / foreign operations**: each jurisdiction at its own rate; **the foreign rate
differential is an ETR reconciling item.** Consider **global minimum tax regimes (e.g. Pillar Two)** where
applicable — **flag for a specialist as these rules are evolving.**

**Return-to-provision true-up**: **when the actual return is filed, differences from the estimated
provision are trued up in the next period. Track the true-up.** *Mosofin note*: the true-up is visible as
a journal entry against the tax accounts — reconcile it rather than letting it disappear into the
current-year charge.

**Outside basis differences**: deferred tax on undistributed foreign earnings and investments in
subsidiaries — **recognition exceptions apply** (the **indefinite reinvestment assertion** under US GAAP;
specific IAS 12 rules). **Complex; flag.**

**Stock-based compensation**: book vs. tax deduction timing and amount differ; **excess tax benefits /
deficiencies flow through the provision** (US GAAP). Coordinate with `equity-compensation-accounting`.

**Tax on OCI items (backwards tracing)**: **IFRS requires tracing tax to where the item was recognized;
US GAAP has specific intraperiod allocation rules. Apply correctly so the continuing-ops provision is
right.** *Mosofin note*: the ledger shows where each deferred tax movement was posted, which is direct
evidence for this step.

**Interim provisions**: interim periods use an **estimated annual effective tax rate applied to
year-to-date income**, with **discrete items recognized in the period they occur. Different from the
annual computation** — do not simply pro-rate the annual provision.

**NOL carryforwards with expiration / limitation**: **track expiration and any usage limitations** (e.g.
ownership-change limitations). **Affects DTA and valuation allowance.** `[manual]` — expiry schedules
come from the tax returns.

**Valuation allowance release**: when evidence shifts to support realizability, **releasing an allowance
creates a large benefit — significant judgment and disclosure.** It also distorts the ETR dramatically in
that year; give it its own reconciling line.

**Tax holidays / incentives**: reduced or zero rates in certain jurisdictions **affect current tax and the
foreign rate differential.**

**A tax rate was supplied from memory** — *Mosofin-specific, and the gravest failure here*. There is no
tax-rate datasource. **Every rate needs a source and a year**, or it goes on Sheet 9 as outstanding.
Rates change frequently and a wrong one misstates every deferred balance simultaneously.

**A book balance presented as a temporary difference** — *Mosofin-specific*. A temporary difference is
the **gap between book and tax bases**, and the workspace holds only the book side. The tax column must
be supplied; a schedule with the book figure copied across is not a temporary difference schedule.

**Deferred tax movements taken to OCI or equity left in the P&L charge** — *Mosofin-specific and
detectable*. The ledger shows the counterparty account of every deferred tax entry. Reconcile the
computed intraperiod allocation against how entries were actually posted.

**The ETR "Other" line is material** — *Mosofin-specific discipline*. A large unexplained residual means
a reconciling item is missing. Set and state a threshold above which it must be broken out.

**A company file is connected but not active** — *Mosofin-specific*. Name it as excluded and say which
jurisdiction is therefore unprovided-for. A group provision missing an entity understates the charge.

**A result comes back with `mock: true`** — *Mosofin-specific*. The provision feeds published financial
statements and ultimately a filing position. Fixture data cannot support it.

**A stored rate is reused** — *Mosofin-specific*. Persist the rate *source*, never the rate. Re-confirm
every year.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it. Never
apply one jurisdiction's schedule to another; never drop it silently.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
