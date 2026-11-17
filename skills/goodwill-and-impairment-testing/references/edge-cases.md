<!-- goodwill-and-impairment-testing · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**Reporting unit vs. CGU**: **different concepts. A reporting unit (US GAAP) is an operating segment or one
level below; a CGU (IFRS) is the smallest identifiable group generating largely independent cash inflows.
They may differ — apply the right framework's definition.**

**Goodwill allocation**: **goodwill must be allocated to the units expected to benefit; the allocation
choice affects impairment outcomes** — goodwill allocated to a struggling unit is more likely to be
impaired. **Document the allocation basis.** *Mosofin note*: **store it, and reuse it** — reallocating
between periods changes which unit fails, and that must never happen by accident.

**Step acquisitions / non-controlling interest goodwill**: **NCI measurement choice
(`business-combinations-asc805`) affects goodwill carrying amount and impairment. The "grossing up" of
goodwill for partial-goodwill IFRS may be needed.**

**Cash flow projections must be defensible**: **optimistic projections that don't materialize lead to large
catch-up impairments and audit scrutiny. Anchor in actual budgets, not aspirational targets.** *Mosofin
note*: **the actuals are readable** — state how the projection compares to what has actually happened.

**Sensitivity to discount rate and growth**: **small changes in WACC or terminal growth swing values
materially — disclose sensitivity.**

**Restructurings not yet committed (IAS 36)**: **explicitly excluded from value in use until committed —
don't pre-credit future fixes.**

**Market capitalization below book value**: **a strong indicator (especially sustained) of impairment for
public entities. Don't ignore it.** *Mosofin note*: **net assets are `[auto]`** — supply the market cap and
the comparison is immediate.

**Long-lived assets — undiscounted vs. discounted test (US GAAP)**: **the recoverability test uses
undiscounted cash flows (a higher bar to find impairment); measurement uses discounted / fair value. Two
distinct steps.**

**Reversal differences**: **IFRS reverses non-goodwill impairments when conditions recover; US GAAP doesn't.
A material framework difference.**

**Asset group definition (US GAAP long-lived)**: **at the lowest level for which identifiable cash flows are
largely independent — similar concept to CGU but per US guidance.**

**Valuation specialist required for material tests**: **DCF and market-multiple work, especially for
goodwill at a reporting-unit / CGU level, is specialist work. Flag.**

**A segment dimension is treated as a CGU** — *Mosofin-specific, and the most tempting shortcut here*. **A
CGU is defined by independent cash inflows.** Use the dimensions to propose; confirm against the definition.

**A declining segment is reported as impaired** — *Mosofin-specific*. It is an **indicator that a test is
required**, nothing more. **The workspace cannot conclude impairment**, because it holds no recoverable
amount.

**An intangible has no amortization being charged** — *Mosofin-specific scoping finding*. Either it is
indefinite-lived, and an annual test may not be happening, or amortization stopped. Both worth raising.

**Triggering events are assessed once a year** — *Mosofin-specific opportunity*. Two of the eight are
measurable monthly. **Monitoring between tests is the point of a triggering event.**

**Goodwill sits in one company file and the business in another** — *Mosofin-specific*. Read both, and state
it: a carrying amount from one file against a recoverable amount from another needs that made explicit.

**A stale fair value or projection is reused** — *Mosofin-specific, and material*. **Recoverable amounts move
with exactly the conditions the test exists to detect.** Persist the approach; never the values.

**A carrying amount is compared to a valuation of a different date** — *Mosofin-specific*. Both sides must be
as at the test date. Record the as-at date on each.

**A company file is connected but not active** — *Mosofin-specific*. Name it as excluded and say which unit's
carrying amount or monitoring data is therefore missing.

**A result comes back with `mock: true`** — *Mosofin-specific*. An impairment charge is material and
audit-scrutinised. A fixture carrying amount makes the comparison meaningless.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it; never
apply one entity's CGU structure or allocation to another.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
