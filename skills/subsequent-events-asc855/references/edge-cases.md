<!-- subsequent-events-asc855 · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

*(A Mosofin addition — the original has no Edge Cases section.)*

**The window extends after the review is done.** The commonest practical failure. The issuance date slips, or the review is completed early, and the last stretch before issuance is unexamined. **`[auto]` to re-run at no cost** — and the sign-off sheet should record the date of the **final** sweep, not the first.

**Reissued financial statements and dual dating.** Where statements are reissued, a further subsequent events evaluation may be required, and the report may be **dual-dated** — the original date for most matters and a later date for the specific subsequent event. `[manual]`, and it changes the window's shape rather than its length.

**An event discovered after issuance.** No longer a subsequent event in the ordinary sense; it is a question about whether previously-issued statements can still be relied on. Route to `restatement-and-prior-period-adjustment` and, for a filer, to `sec-10q-10k-prep`.

**A dividend declared after the balance sheet date.** Generally **non-recognised** — the liability did not exist at the date — but disclosable, and treated differently in some frameworks. `[auto]` to detect; `[manual]` to treat. See `statement-of-equity-changes`, where the declaration-versus-payment distinction is worked through.

**Going concern events after the period end.** These get special treatment: information about conditions after the balance sheet date can be relevant to the going concern assessment **even where the event itself is non-recognised**, because the assessment looks forward from issuance. `[manual]` — see `quarter-end-close` and its rule that **no forward-looking statement is ever authored here.**

**A business combination after the period end.** Non-recognised, generally, but with specific and extensive disclosure requirements. `[manual]`.

**Recognised events that reduce a provision.** The mirror case nobody sweeps for, because it is good news: a receivable provided against and then paid, a contingency settled for less than accrued. **`[auto]` finds these as readily as the adverse ones** — and a review that only ever finds adjustments in one direction is not a review, it is a bias.

**A transaction dated before the period end but posted after it.** **Not a subsequent event** — it is a period-end transaction recorded late, and belongs in cutoff testing. `[auto]` to distinguish by comparing transaction and posting dates. See `revenue-cutoff-testing`.

**An event that is Type 1 for one estimate and Type 2 for another.** A customer's insolvency may be Type 1 evidence for their receivable and Type 2 for a contract with them signed in January. **Classify per effect, not per event.** `[manual]`.

**Proximity that misleads.** A customer failing on 3 January is probably evidence of a December condition; one failing on 3 January **because of a fire on 2 January** is not. **Proximity is evidence, never proof**, and the sweep must present it as such.

**No events found.** A legitimate and common outcome — **and it must be documented as a performed procedure with a scope, not as an empty sheet.** *"The full post-period transaction population from X to Y was examined against the period-end position; no recognised event candidates were identified. Management enquiry covering the categories at Step 2 identified none."* That is a conclusion. A blank log is not.
