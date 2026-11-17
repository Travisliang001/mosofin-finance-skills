<!-- intercompany-reconciliation · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**Three-party intercompany flows** — A sells to B who sells to C, both within the group: **match A↔B and
B↔C separately; full elimination at consolidation removes both legs.** **Do not attempt to reconcile A to
C** — there is no direct balance between them.

**Intercompany loans with interest accruing**: **ensure interest accrual is recorded on both sides at the
same period and amount. Common mismatch.** *Mosofin note*: **both accruals are readable**, so this one is
directly testable — and it recurs every period until someone fixes the process.

**Foreign-currency IC loans**: **revalue periodically**. **The FX gain
on the lender side and FX loss on the borrower side should be equal-and-opposite in group currency; in
individual books they may not be.**

**IC transactions with related but not consolidated parties**: **not eliminated at consolidation, but still
need disclosure and matching to ensure both sides recorded correctly.** *Mosofin note*: **confirm which
connected entities are group members and which are merely related** — the two are treated completely
differently and both may be connected.

**Service fees with different tax treatments per jurisdiction**: **one side may include VAT / GST recovery;
the other doesn't because it's tax-exempt. Reconcile pre-tax and document tax handling separately.**

**Transfer pricing adjustments at year-end** — a true-up to a target margin: **one side may post a year-end
adjustment that the other doesn't immediately mirror. Coordinate.** *Mosofin note*: this appears as a
**large journal entry with no document**, which is exactly the Step 4 check.

**Cross-border IC with withholding tax**: **paying entity withholds tax and remits it; receiving entity
records gross revenue and a WHT receivable. Both sides' net cash impact differs from gross — confirm both
record the WHT.**

**Intercompany dividends**: **paying entity reduces equity; receiving entity may record dividend income.
Eliminate at consolidation. Watch for timing differences if the dividend is declared in one period and paid
in another.**

**Internal recharges with no formal invoice** — shared services often work this way: **rely on internal
allocation schedules; ensure both sides agree on the allocation basis and amount.** *Mosofin note*: **with
no document, reference matching is unavailable** — these match on amount and date alone, and should be
flagged as the weaker basis.

**Pending acquisitions or divestitures**: **an entity in the process of acquisition may not yet be in the IC
system, or one leaving may still have open balances. Document and coordinate.**

**Mismatches that persist for several periods**: **escalate to controllership. Long-aged IC mismatches
signal a process breakdown.** *Mosofin note*: **ageing is readable**, so persistence is measurable rather
than remembered.

**Only one side of a pair is connected** — *Mosofin-specific, and the primary failure mode*. **A single-sided
figure is not a reconciliation.** Mark the pair not reconcilable and name the missing side.

**An entity is in a different, unconfirmed workspace** — *Mosofin-specific*. Same effect as disconnected.
Confirm the workspace at Gate 0 or mark its pairs unreconcilable.

**One side returns `mock: true`** — *Mosofin-specific*. Matching fixtures against real data produces an
entirely fictional mismatch list.

**Entities read at different moments** — *Mosofin-specific*. **Batch the reads.** Version skew between sides
creates phantom mismatches that disappear when you look again.

**Matching on amount alone with a wide date window** — *Mosofin-specific*. That is not matching. **State the
window, keep it tight, and flag every match not made on a reference.**

**A journal entry posted straight to an IC account with no document** — *Mosofin-specific, and usually where
the answer is*. List them separately.

**Entities have different year-ends** — *Mosofin-specific*. Read the **same calendar period** from each and
say so.

**A stored pair rule applied to the wrong pair** — *Mosofin-specific*. Conventions are pair-specific.
**Key every stored rule by both entity names.**

**A tool is `permission`-gated on one side** — *Mosofin-specific*. **The pair is `[gated]`, not the
entity.** Ask, then proceed; record the verdict per pair.
