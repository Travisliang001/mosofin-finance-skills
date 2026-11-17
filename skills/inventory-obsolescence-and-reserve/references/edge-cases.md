<!-- inventory-obsolescence-and-reserve · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

**The original has no Edge Cases section. Everything below is a Mosofin addition** — from the domain and
from the workspace model.

**No-move treated as obsolete** — **the central error here.** Spare parts, seasonal lines and end-of-life
stock with commitments all read as no-move. **The query produces candidates; the business decides.**

**Aging built on a last-purchase proxy and presented as lot age** — *Mosofin-specific*. A fast-turning item
bought last week looks new even if some units are years old. **Label the basis.**

**Slow-moving and below-cost reserved twice** — **LCNRV covers items you expect to sell; the obsolescence
reserve covers items you expect not to.** Reserve once, on the more severe basis.

**Aging model and forecast-based excess added together** — the same double-count in a different form. **One
method per population.**

**A write-off posted to expense while a reserve exists** — **double-counts the cost.** The write-off should
use the reserve. Readable as a pattern.

**Raw materials written down because their own price fell** — **wrong test.** Raw materials are written down
only if the finished goods they go into cannot be sold above cost.

**Damaged or expired stock assumed to be visible** — *Mosofin-specific*. **It is not.** Condition is
physical, and nothing in the ledger distinguishes a pristine pallet from a ruined one. **Ask.**

**Months of supply computed on the wrong usage window** — seasonal goods measured on a trailing three
months in the off-season look catastrophically overstocked. **State the window; choose it deliberately.**

**"Compare to forecast demand" answered with historical demand** — *Mosofin-specific*. A weaker test, and it
must be labelled as history rather than forecast.

**Reserve rates assumed rather than derived** — *Mosofin-specific opportunity*. **The history is readable.**
Derive the rate and present it against the one in use.

**A reserve never back-tested** — *Mosofin-specific*. A reserve consistently far above what is ever used is
a cushion; one consistently exhausted is too low. **The pattern is readable.**

**The roll-forward does not tie to the reserve account** — *Mosofin-specific*. It is a schedule about a real
account; it must agree to it.

**A short movement history** — *Mosofin-specific*. Three months finds nothing. **Pull at least two years.**

**Line-level sales detail unavailable** — *Mosofin-specific*. **Movement analysis cannot run.** Say so
rather than substituting totals.

**Stock aging restarted by an intra-group transfer** — *Mosofin-specific*. Old stock moved between entities
looks new. Check for it.

**Reserving against an inflated intra-group cost** — *Mosofin-specific*. **Reserve on group cost**, or the
group double-counts a loss it never had.

**Dead stock in one entity, current in another** — *Mosofin-specific*. **Demand elsewhere in the group is
readable**, and it changes the answer before anything is written down.

**A result comes back with `mock: true`** — *Mosofin-specific*. Fixture movement produces a fictional
slow-moving list.

**A stored exception list is reused** — *Mosofin-specific, and self-fulfilling*. Last quarter's slow item may
be this quarter's best seller. **Persist the categories and the method; rebuild the list.**

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it; never
apply one entity's buckets or exclusions to another.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
