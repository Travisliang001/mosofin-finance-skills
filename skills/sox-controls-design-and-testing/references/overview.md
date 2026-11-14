<!-- sox-controls-design-and-testing · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# SOX Controls Design and Testing (ICFR) — Mosofin Seed

Designs, documents and tests internal controls over financial reporting. Builds the risk-and-control matrix, documents control design, creates and executes test plans, and evaluates deficiencies.

**Framework-aware** — COSO Internal Control – Integrated Framework as the common basis, SOX for US public companies — and **process-agnostic**.

This is a **seed skill**, written to be rewritten the first time it runs against a real workspace.

---

## The distinction this whole skill turns on

Five other skills in this pack defer to a single line — *a population read is not a control test.* **This is where it gets worked out properly**, because getting it wrong here produces a control conclusion that is not supported by anything.

> **A control test asks: did the control operate?**
>
> **A ledger read asks: what does the data show?**

Those are different questions, and neither answer implies the other.

**A control can operate perfectly and the outcome still be wrong.** The reviewer performed the review, applied the stated criteria, documented it — and missed the item. The control operated; the misstatement got through.

**The outcome can be right with no control operating at all.** Nothing went wrong that month. The reconciliation nobody performed would have found nothing. Clean data is not evidence that a control ran.

So **outcome evidence and control-operation evidence are separate**, and most control operation is a **human act** — a review, an approval, an investigation, a sign-off. That evidence lives in email, ticketing systems, workflow tools, signed schedules and people's recollections. **Almost none of it is in a general ledger.**

**Which makes Step 7 largely `[manual]`, and that is the correct answer rather than a shortcoming.**

### And now the genuine contribution, which is substantial

**Some controls do leave a trace in the accounting data.** For those, a connected ledger changes the *quality* of the test rather than just its speed:

> **Where a control's operation is evidenced in the ledger, there is no need to sample. Test all of it.**

Step 6 builds a sampling plan — sample sizes calibrated to control frequency, because examining every instance by hand is impossible. **For a ledger-evidenced control that constraint disappears.** A 25-item sample from a daily control covering 250 occurrences gives you a conclusion with sampling risk attached. Reading all 250 gives you the answer.

That is a real improvement, and it is the same point `internal-audit-workpaper` makes about substantive testing. **It applies to a specific and identifiable subset of controls**, and Step 6b sets out which.

### Three near-substitutes

**1. An outcome is not an operation.** Covered above. It is the one that matters most.

**2. Segregation of duties as *configured* is not segregation of duties as *operated*.** A permissions matrix says what people **could** do. The transaction record says what they **did**. The second is stronger evidence and it is the one the ledger holds — see Step 4b.

**3. A sign-off is not a review.** The original's own edge case says this: *document the review criteria and evidence of investigation, not just a sign-off.* An initial in a box is evidence that somebody initialled a box.

### And one dependency that must be stated before any of it is relied on

**Mosofin's reads inherit the reliability of the system being read.**

If IT general controls are weak — if change management is uncontrolled, if access is unrestricted, if data can be altered without trace — then **the ledger data itself is not reliable evidence**, and every automated test in this skill inherits that unreliability. The edge case says it about system-generated reports and automated controls; **it is equally true of everything Mosofin reads.**

**So ITGC effectiveness is a precondition for relying on any of the `[auto]` work below**, not a parallel workstream. Scope and assess ITGCs first, and where they are deficient, say plainly that the automated evidence is correspondingly weakened. See Step 1 and the edge cases.

---

## Related skills

| Skill | Relationship |
|---|---|
| `internal-audit-workpaper` | The same population-versus-control distinction, and the six procedure types. |
| `audit-prep-pbc-list` | Substantive audit support, explicitly out of scope. |
| `journal-entry-review` | Journal approval and review controls — a ledger-evidenced set. |
| `three-way-match` | The purchase-to-pay control, and duplicate payment prevention. |
| `fraud-detection-and-forensics` | The fictitious-vendor exposure that SoD testing addresses. |
| `recurring-transaction-builder` | Whether the recurring entries a control depends on actually ran. |
| `month-end-close-checklist` | Where reconciliation controls are performed and evidenced. |
| `balance-sheet-reconciliations` | Reconciliation controls and their uncorrected exceptions. |
