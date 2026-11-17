<!-- inventory-costing-fifo-lifo-wavg · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**LIFO under IFRS**: **not permitted. A LIFO entity moving to IFRS must convert, with significant tax implications under US LIFO conformity rules.**

**Periodic vs. perpetual LIFO / WAVG differences**: **the same transactions can produce different results.
Match the computation to the system in use.** *Mosofin note*: **which system is in use is observable** from
whether COGS posts per sale.

**Dollar-value LIFO pools and indices**: **a more complex LIFO approach using dollar value pools and an
external or internal price index. Flag for the entity's specific approach.** **The index is `[manual]`.**

**LIFO liquidation**: **when a LIFO entity sells more than it buys in a period, it dips into old, low-cost
LIFO layers, inflating margins ("liquidation profit"). Disclose; not a sustainable result.** *Mosofin
note*: **purchases against sales by period is readable**, so a liquidation is detectable before it surprises
anyone.

**NRV write-downs without reversal (US GAAP)**: **once written down, the new cost is the new cost — don't
reverse if NRV recovers. IFRS does permit reversal up to original cost.**

**Cost-to-NRV grouping**: **assess at the item level or appropriate grouping per the framework — grouping at
too high a level can mask write-downs of specific items.** *Mosofin note*: **item-level assessment is
cheap here**, so there is little reason to group coarsely.

**Standard costing**: **many manufacturers use standard costs with variances. Variances must be allocated
between inventory and COGS at period-end. Flag if standard costing is in use.** *Mosofin note*: **the
variance accounts are readable, but the allocation basis is `[manual]`** — and **if standard costing is in
use, the platform's inventory value is at standard, not actual.**

**Joint products / by-products**: **cost allocation for joint products (relative sales value or other) and
net realizable value for by-products — specialized.** **[manual]**.

**Consigned inventory**: **include if the entity owns it, regardless of physical location; exclude if held
on consignment from others.** *Mosofin note*: **the platform's quantity on hand may include or exclude
consigned goods depending on setup** — confirm rather than assume.

**In-transit inventory**: **include based on FOB terms** — shipping point versus destination. **The terms
are `[manual]`, from the purchase contract.**

**Slow-moving / obsolete inventory**: **requires separate reserve assessment beyond NRV; may not have a
clear NRV. Apply judgment and document.** See `inventory-obsolescence-and-reserve`. *Mosofin note*:
**items with no sales activity are readable**, which is the population that assessment starts from.

**The platform's method differs from the reported method** — *Mosofin-specific, and the central structural
point*. **Establish both, and find where the difference is recorded.** If it is recorded nowhere, the
reported figures and the ledger disagree.

**LIFO maintained in a platform that cannot do LIFO** — *Mosofin-specific*. The LIFO figures live in a
spreadsheet. **The ledger holds something else**, and the reserve is the bridge.

**Line-level detail is unavailable** — *Mosofin-specific*. **Layer reconstruction is impossible.** Say so;
do not approximate a layer stack from totals.

**The unit reconciliation fails but the cost one passes** — *Mosofin-specific*. **Different faults**:
missing transactions versus wrong layer logic. Report both separately.

**Freight-in expensed rather than capitalised** — *Mosofin-specific*. Understates inventory, overstates
current cost. Readable as a pattern.

**Selling or admin cost sitting in inventory** — *Mosofin-specific*, and the reverse error. Overstates the
asset.

**A realised selling price used as NRV** — *Mosofin-specific*. **NRV is selling price less costs to complete
and sell.** The price is evidenced; the deduction is `[manual]`.

**Recent purchase price used as replacement cost** — *Mosofin-specific*. A defensible approximation for LCM,
**and it must be labelled as one.**

**Quantity on hand treated as physical quantity** — *Mosofin-specific*. **Only a count proves existence.**
See `inventory-to-gl-reconciliation`.

**Group inventory carried at the buying entity's cost** — *Mosofin-specific*. **Group cost is the original
entity's cost**; the mark-up is eliminated.

**A result comes back with `mock: true`** — *Mosofin-specific*. Inventory and COGS are usually the largest
figures on a merchandising entity's statements.

**A stored unit cost or layer stack is reused** — *Mosofin-specific*. All state, and it changes with every
transaction. **Persist the method and the recipe; rebuild the stack.**

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it; never
apply one entity's method or NRV basis to another.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
