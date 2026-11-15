<!-- cost-accounting-process-costing · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

*The original did not carry an Edge Cases section; these are Mosofin additions plus the hazards implicit
in the steps above.*

**Equivalent units inferred from a WIP balance** — *the central Mosofin-specific hazard*. Dividing a
dollar balance by a standard cost to get units is circular: the standard cost is what the exercise
produces. **Never derive units from money.**

**The model reconciles internally but not to the ledger** — the arithmetic is right and the inputs are
wrong. Investigate the difference: unposted costs, costs without a department tag, transfers made in the
model but not the books, or a manual journal into WIP.

**Costs posted to WIP without a department tag** — they sit in the balance but belong to no process, so
every department's cost per unit is understated. Detectable directly; report the amount.

**A manual journal into WIP** — process costing assumes cost enters through production. A journal
bypassing that flow will break the reconciliation and usually indicates an adjustment nobody told the
cost accountant about.

**Material added at the start treated as added evenly** — ending WIP is **100% complete for materials**
when materials go in at the start, whatever the conversion percentage. Getting this wrong misstates both
the ending WIP value and the transferred-out cost, in opposite directions.

**Units in and units out disagree** — do not let the schedule absorb it. Distinguish normal loss (a cost
of good output) from abnormal loss (a period expense); they are accounted for differently.

**A method change between periods** — weighted-average and FIFO give different unit costs from identical
facts. Flag the change; never present the difference as a movement in cost.

**Transfer pricing above cost between departments** — creates internal profit sitting in inventory. At
department level within one entity it should generally be at cost; anything else must be eliminated.

**Completion percentages estimated by the person whose department is being measured** — a real
independence concern in practice. Record who supplied them; the coverage sheet exists partly for this.

**A stale count** — a completion percentage taken a week before period end does not describe period end.
Record the date of the count alongside the figure.

**A company file is connected but not active** — *Mosofin-specific*. Name it as excluded and say which
plant's costs are therefore unmeasured. Surface any `reconnect_url`.

**A result comes back with `mock: true`** — *Mosofin-specific*. Unit cost flows into inventory valuation
and into pricing; fixture data cannot support it.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it. Never
apply one plant's sequence or addition points to another; never drop it silently.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
