<!-- gaap-vs-ifrs-conversion · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**LIFO inventory**: **a US GAAP LIFO entity must abandon LIFO for IFRS — often a large adjustment, with
significant tax implications** (LIFO is also a tax method in the US; **the book change can have tax
consequences**). **Flag for tax and technical review.**

**Development cost capitalization (IFRS)**: **requires capitalizing qualifying development costs that US
GAAP expensed — needs identifying which historical costs qualify, often difficult retrospectively.**
*Mosofin note*: **the expensed costs are readable in the ledger** (*`get_general_ledger`* on R&D accounts),
which gives the population to assess — **but which of them meet the capitalisation criteria is `[manual]`
and genuinely hard.**

**Impairment reversals**: **IFRS permits reversing prior impairments (except goodwill); US GAAP prohibits.
Converting requires reassessing whether reversals would apply.**

**Revaluation model (IFRS PP&E)**: **optional; if elected, requires fair values and ongoing revaluation,
with surplus in OCI. A policy choice, not automatic.** *Mosofin note*: **the valuations are `[manual]`**, and
electing this creates a permanent ongoing obligation, not a one-off adjustment.

**First-time adoption exemptions**: **IFRS 1's optional exemptions can dramatically simplify (or change) the
conversion — choosing them is a strategic decision with lasting effects. Technical input needed.**

**Deferred tax on every adjustment**: **each conversion adjustment generally changes temporary differences
and deferred tax. Easy to miss; flows through the reconciliation.**

**Converged-but-not-identical standards**: **revenue (606/15) and leases (842/16) are converged in principle
but differ in application. Don't assume "converged" means "identical."**

**Ongoing vs. one-time**: **a conversion isn't a one-time exercise if the entity must report under both
frameworks ongoing — it needs a sustainable dual-reporting process.** *Mosofin note*: **that is exactly what
the Step 9 stored scoping and methodology support** — the second period should cost a fraction of the
first.

**Direction matters**: **IFRS→US GAAP differs from US GAAP→IFRS** — e.g. **IFRS→US GAAP must remove
revaluations, reverse impairment reversals**, and so on. **Apply the right direction.**

**Materiality and effort**: **scope to material differences; converting immaterial items wastes effort. But
document why an area was assessed as immaterial.** *Mosofin note*: **Sheet 8 is where that documentation
lives**, and the scoping read makes it cheap to produce.

**Complexity warrants experts**: **financial instruments, pensions, business combinations, and
consolidations under different frameworks are highly technical. Flag for technical accounting specialists
and audit; don't oversimplify.**

**A balance is read as a policy** — *Mosofin-specific, and the central trap*. The ledger shows results.
**Every policy is `[manual]`.**

**An account's absence is treated as proof** — *Mosofin-specific*. No capitalised development could mean the
policy expensed it, or that there was no qualifying development, or that it was misposted. **A scoping
signal, not a conclusion.**

**The account evidence contradicts the stated framework** — *Mosofin-specific*. A revaluation surplus under
claimed US GAAP; a LIFO reserve under claimed IFRS; an impairment reversal under US GAAP. **Raise it before
converting.**

**Material rent expense with no lease liability** — *Mosofin-specific scoping finding*. Either no leases in
scope, or an unrecognised issue under both frameworks. One query.

**Presentation differences are dropped because they carry no number** — *Mosofin-specific*. They change
nothing in the bridge and still require real work. Track them separately.

**The reconciliation's opening figure is not tied to the source books** — *Mosofin-specific*. It is the one
figure here the workspace can prove. Tie it, with the tool call and as-at date.

**One entity's scoping is reused across a group** — *Mosofin-specific*. Live areas differ entirely by
business. Scope each entity.

**Consolidating before converting, or translating before converting** — *Mosofin-specific ordering*.
**Convert first**, then translate, then consolidate — otherwise effects mix in a single unexplainable
adjustment.

**A company file is connected but not active** — *Mosofin-specific*. Name it as excluded and say whose
conversion is therefore not done. For group alignment, that is a gap in the group's reporting.

**A result comes back with `mock: true`** — *Mosofin-specific*. A conversion bridge is often prepared for a
listing, a lender or a group parent. A fixture-based bridge is worse than none.

**A stored adjustment amount is reused** — *Mosofin-specific*. Amounts are state. **Persist the scoping,
the policies and the methodology; recompute the numbers.**

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it; never
apply one entity's scope or elections to another.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
