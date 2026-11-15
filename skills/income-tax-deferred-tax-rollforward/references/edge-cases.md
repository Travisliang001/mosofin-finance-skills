<!-- income-tax-deferred-tax-rollforward · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

**The original has no Edge Cases section. Everything below is a Mosofin addition** — from the domain and
from the workspace model.

**A permanent difference put in the inventory** — permanent differences create **no** deferred tax. They
belong in the rate reconciliation, not the rollforward. A frequent and material error.

**The rate used is not the enacted rate for the reversal period** — where legislation changes a future
rate, **the reversal timing decides which rate applies**, and blending across a rate change misstates the
balance.

**A rate change folded into current period expense** — it revalues the whole balance at once. **Give it its
own line**; it is often the largest single movement on the schedule.

**DTLs credited as support for DTAs across periods or jurisdictions** — they only support DTAs where the
**timing and jurisdiction actually match**.

**A forecast outweighing a cumulative loss** — *the assessment error this skill exists to prevent*.
**Objective evidence outweighs subjective**, and a cumulative loss position is very hard to overcome.

**The cumulative-loss test never computed** — *Mosofin-specific*. It is **one query**, and it frames the
entire valuation allowance conclusion. Compute it either way.

**The rollforward does not tie to the balance sheet** — *Mosofin-specific*. The entry is usually one annual
journal from an outside workpaper, so drift is common and invisible.

**The movement does not agree to the deferred tax expense** — *Mosofin-specific*. Either something went to
OCI or equity, or an entry is missing. **Both are worth knowing which.**

**Two inventory items map to the same account** — *Mosofin-specific*, and it delivers the original's own
fourth quality check: **a double count.**

**A material balance sheet account has no inventory item** — *Mosofin-specific, and the direction nobody
checks*. A missed difference understates the deferred balance.

**An inventory item has no supporting account** — *Mosofin-specific*. A difference with no book basis; ask
where it comes from.

**Deferred tax on an OCI item routed through the P&L** — **the tax follows the item.** Hedges,
revaluations and pension remeasurements take their tax to OCI.

**NOL expiry ignored** — *Mosofin-specific emphasis*. **An NOL that expires unused is worthless**, and the
expiry schedule is `[manual]`. Ask for dates, not just amounts.

**Group net presentation without a right of offset** — *Mosofin-specific*. DTAs and DTLs across different
taxpayers or jurisdictions are not offset.

**A valuation allowance assessed once for a group** — *Mosofin-specific*. It is **per taxpayer**, and the
cumulative-loss test runs per entity.

**FX movement folded into deferred expense** — *Mosofin-specific*. It is a separate rollforward line.

**A company file is connected but not active** — *Mosofin-specific*. Name it as excluded and say whose
deferred position is therefore unexamined.

**A result comes back with `mock: true`** — *Mosofin-specific*. Deferred tax flows into the provision, the
effective rate and the published statements.

**A stored rate or deferred balance is reused** — *Mosofin-specific*. **Rates change by legislation**, and a
stale rate misstates every balance on the schedule. Persist the source; re-obtain the rate.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it; never
apply one taxpayer's inventory or rate to another.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
