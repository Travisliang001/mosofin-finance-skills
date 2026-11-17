<!-- year-end-close · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Year-End Close — Mosofin Seed

Plans and executes the year-end close — **the most rigorous accounting cycle, with audit and statutory implications.** Extends the monthly and quarterly close with annual procedures.

**System-agnostic in its logic**, applying whichever reporting framework the user specifies — US GAAP, IFRS, local GAAP. **The evidence, as elsewhere in this pack, comes from one specific connected ledger**, which is a gain in usefulness and a loss in portability. Both are stated.

This is a **seed skill**, written to be rewritten the first time it runs against a real workspace.

---

## The layering, and what it means for the verdicts

Step 1 states it plainly: **year-end is also a month-end and a quarter-end.** So this skill sits on top of two others and inherits their profiles:

| Layer | Skill | Character |
|---|---|---|
| **Monthly close** | `month-end-close-checklist` | **Largely `[auto]`** — the ledger does most of the work; entry-based tasks self-verify |
| **Quarterly increment** | `quarter-end-close` | **Largely `[manual]`** — estimates, judgments, subsequent events, going concern |
| **Annual increment** | This skill | **More manual still** — and for a specific reason set out below |

**The annual layer is the most manual of the three**, and it is not because the gateway is weak. It is because **year-end is the point at which the accounts are examined by someone outside the business**, and external examination requires external evidence.

### Confirmations are the defining absence, and this is where it lands

Step 2's audit prep asks for **bank confirmations, AR confirmations, debt confirmations and attorney letters.**

**These are third parties attesting directly to the auditor**, independently of the entity and independently of its books. That is the whole point of them — and it is precisely what a read-only gateway into the client's own ledger cannot supply, by construction.

Throughout this pack I have noted that **bank statements are not on this surface** — in `bank-reconciliation`, `merchant-and-payment-processor-rec`, `payroll-clearing-reconciliation`, `quarter-end-close`. **At year-end that absence stops being a limitation on a reconciliation and becomes a named audit procedure with a form and a signature.**

`internal-audit-workpaper` makes the general point: of the procedure types available to an examiner, **confirm is one the workspace cannot perform at all.** Year-end is where confirming matters most.

**The same applies to the physical count.** Step 2's fixed asset block asks for a **physical asset count, typically annual** — and a petty cash count states the principle exactly: **the ledger says what should be there; only counting says what is.** Inventory counts sit alongside it.

### What the workspace does contribute, and it is substantial

**Three things, and the first compresses the timetable materially.**

**1. The ledger-derived PBC and the lead schedules.** Most of what an auditor asks for in week one is **trial balances, transaction detail, ageings and account roll-forwards** — every one of which is a live read. **Assembling that before the auditor arrives is the difference between a close that spends three weeks answering requests and one that starts with them answered.** See Step 2a.

**2. The completeness tests on the close itself.** All twelve months closed, not just December. The books actually locked. The new year opened clean. **Each is one query, each is routinely assumed, and each fails silently.** See Steps 1b, 5b and 5c.

**3. Everything the two lower layers already do**, inherited whole.

### Three near-substitutes

**1. Locked is not unchanged.** Step 5 locks the books. **A lock is a control, controls fail, and a year that was reported and then posted into is the problem a restatement review exists for.** Verify rather than assume — Step 5b.

**2. A ledger extract is not a lead schedule.** `[auto]` can produce every account's composition and roll-forward. **A lead schedule is that extract plus the preparer's tie to supporting evidence and their analysis of the movement** — which is what makes it a workpaper rather than a printout. Mosofin builds the first part; a person makes it the second.

**3. The auditor's adjusting entries are the auditor's.** Step 4 says **review, accept or push back.** That is a negotiation between the entity and its auditor. **Mosofin quantifies an adjustment's effect and accepts nothing on the client's behalf.**

---

## Related skills

The year-end close is the point in the cycle where most of this pack converges.

| Skill | Relationship |
|---|---|
| `month-end-close-checklist` | The foundation. Run in full; year-end sits on top. |
| `quarter-end-close` | The middle layer, also run in full — and Q4 belongs here, not there. |
| `closing-entries-and-trial-balance` | Step 5's closing entries. |
| `audit-prep-pbc-list` | The PBC, of which the ledger-derived portion is assembled here. |
| `financial-statement-builder` | The statements — and the caution that a balancing balance sheet proves only arithmetic. |
| `cash-flow-statement-indirect-method` | The annual cash flow statement. |
| `payroll-reconciliation` and the payroll quartet | Payroll year-end, and the register that is the missing half. |
| `bad-debt-and-write-offs` / `inventory-obsolescence-and-reserve` | The reserves needing a fresh look. |
| `fixed-asset-register-and-depreciation` | The register, the count, and the two-directional reconciliation. |
| `intercompany-reconciliation` | The consolidation block. |
| `sox-controls-design-and-testing` | The filing, its controls, and its tagging. |
| `journal-entry-review` / `recurring-transaction-builder` | The close-completeness checks behind Step 1b. |
| `rolling-forecast` | Where the closed year becomes the base for the next one. |
