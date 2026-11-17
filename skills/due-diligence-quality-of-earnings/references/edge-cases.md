<!-- due-diligence-quality-of-earnings · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**Overly aggressive add-backs**: **"one-time" items that recur** (e.g. annual "one-time" legal settlements)
**shouldn't be adjusted. Be disciplined; symmetric treatment** — don't only add back expenses; if there
were one-time gains, deduct them. *Mosofin note*: **this is now a test** — Step 3b runs it against the
prior three years.

**Owner-comp normalization (private companies)**: **a foundational adjustment.** The owner is often paid
above market (extracting earnings) or below market (building value). **Normalize to market for the role;
document the basis.** The market rate is `[manual]`; the actual compensation is `[auto]` once the owner is
identified.

**Related-party transactions**: rents, royalties, IP licenses, intercompany services — **all must be
normalized to market terms if they'll change post-deal.** *Mosofin note*: quantifiable once the parties
are named, and **the parties must be named** — no ledger flags a vendor as related.

**Recognition aggressiveness**: revenue pulled forward (**bill-and-hold, channel stuffing, premature
delivery**), expenses deferred, reserves released — **all inflate apparent EBITDA. Cutoff testing
matters.** *Mosofin note*: the period-end invoicing spike and subsequent credit notes are a strong
automated proxy.

**Working capital methodology disputes**: **the target is heavily negotiated. Method** (median, average,
peak-trough) **and period** (LTM, last 12, normalized) **affect the dollar amount. Be clear** — and show
more than one.

**Stock-based compensation**: **a real cost. Don't add it back to EBITDA unless the buyer explicitly
accepts that view** (some do, many don't). **Disclose either way.**

**Synergies / hypothetical adjustments**: **belong in valuation work, not in historical adjusted EBITDA.
Don't mix.**

**Tax exposures**: historical non-compliance — **sales tax nexus not collected, payroll classification,
transfer pricing** — can be material. **Flag for a tax DD specialist.**

**System and data quality**: **if the underlying data is poor, the QofE is limited. Note the limitations
explicitly.** *Mosofin note*: directly observable — how far the history reaches, whether dimensions exist,
whether the ledger supports the analysis. Report it as a finding, not an apology.

**Sell-side vs. buy-side perspective**: **sell-side aims to support the sale** (favourable presentation
within defensible bounds); **buy-side aims to identify risks. Same methodology, different emphasis. Be
transparent about which side.**

**QofE is not an audit**: **it doesn't opine on fair presentation; it identifies adjustments and risks.
State the limitation.**

**The target is not the connected entity** — *the central Mosofin-specific point*. On buy-side, your
workspace holds the acquirer's books. **Every target figure is supplied.** Never analyse the acquirer's own
data by accident, and never let an `[auto]` verdict imply target data was read.

**History does not reach three years** — *Mosofin-specific*. A recently connected file cannot support the
recurring-item test or a three-year trend. State the earliest period available before promising the
analysis.

**Reported figures disagree with the ledger** — *Mosofin-specific and worth checking*. Reports can be run
on different bases or include manual overlays. The difference is a finding about data quality, which is
itself a QofE observation.

**Adjustments exceed reported EBITDA** — *Mosofin-specific framing*. This is a reconstruction rather than a
normalisation. It may be entirely legitimate — a business emerging from a bad year — but it must be
labelled, because a multiple applied to a number four times the reported one deserves scrutiny.

**Capex sustained below depreciation** — *Mosofin-specific and directly measurable*. The business is being
run for cash and the buyer inherits a catch-up. Maintenance capex is being understated somewhere.

**A company file is connected but not active** — *Mosofin-specific*. If it is the target, say so and stop
rather than analysing a sibling.

**A result comes back with `mock: true`** — *Mosofin-specific*. A QofE sets a purchase price. Fixture data
multiplied by a valuation multiple is an expensive error.

**A stored net debt definition conflicts with the valuation's** — *Mosofin-specific*. The two must agree, or
the price bridge will not reconcile. Store one definition, shared with `business-valuation`.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. In a deal this may
mean completion, lapse, or expired data-room access. Ask rather than assuming.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
