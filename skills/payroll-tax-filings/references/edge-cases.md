<!-- payroll-tax-filings · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**Deposit schedule changes**: **an employer's required deposit frequency can change year to year based on
prior-period volume. Confirm the current schedule; using last year's can cause late deposits.** *Mosofin
note*: **this is why the schedule is never persisted** — only the source and the cadence of re-confirming
it.

**Wage-base ceilings**: **contributions that stop at an annual cap mean later-in-year wages bear less tax.
Year-end computations must respect each employee's cumulative wages vs. the cap.** **Per employee, and not
recoverable from any aggregate.**

**Pre-tax deductions and differing bases**: **retirement and benefit deductions reduce some taxable bases
but not others. Compute each tax on its correct base.**

**Multi-jurisdiction employees**: **employees working across states or countries can create
multi-jurisdiction withholding and filing obligations. Flag for specialist; allocation rules vary.**

**Third-party payroll provider**: **even when a provider files and remits, the employer is generally
ultimately liable. Confirm the provider actually deposited — request proof; don't assume.** *Mosofin note*:
**the `[auto]` evidence stops at the company's bank account.** A perfect deposit reconciliation proves the
money left, not that it arrived.

**Penalties for late / short deposits**: **scale with lateness and amount. Flag exposure; recommend prompt
remittance. Don't compute exact penalties without confirming current rules.** *Mosofin note*: **lateness is
exact once due dates are supplied**, so the exposure can be described precisely even where the penalty
cannot be computed.

**Corrections and amended filings**: **errors in prior filings require amendments. Identify, quantify, and
flag the amendment process.**

**Year-end mismatches**: **if wage statements don't tie to returns and GL, resolve before issuing —
employees and tax authorities will reconcile them, and mismatches trigger notices.**

**New employer / new jurisdiction**: **registration and account setup must precede filing. Flag if the
entity isn't registered where it has obligations.** *Mosofin note*: **a liability accruing with no
corresponding payee or payment history is a signal** — it may be an unregistered obligation.

**Contractor vs. employee classification**: **misclassification creates payroll tax exposure — the entity
may owe employer contributions and withholding it didn't collect. Flag classification risk for specialist
review.** *Mosofin note*: **payments to individuals through accounts payable rather than payroll are
readable**, and a regular, sole-source, long-running arrangement is worth raising as a classification
question. **A question for a specialist, never a conclusion.**

**Rates / forms / deadlines change**: **confirm current every year. Never hardcode.** **The governing rule of
this skill.**

**A rate, cap or deadline supplied from memory** — *Mosofin-specific, and prohibited*. **There are no
reasonable defaults.** Every statutory value comes from a current source and appears on Sheet 8.

**A stored rate reused across a statutory year** — *Mosofin-specific*. **The most likely way this skill
causes harm.** Persist the source; re-confirm the value.

**A liability account with no obligation mapped, or an obligation with no account** — *Mosofin-specific*.
The second is the serious one: **the obligation may not be accrued at all.**

**The amount due differs from the liability balance** — *Mosofin-specific*. **The accrual was wrong**, and
better found before the filing.

**An over-deposit treated as harmless** — *Mosofin-specific*. It ties up cash and usually needs an
adjustment or a refund claim.

**The payment pattern does not match the stated deposit schedule** — *Mosofin-specific*. Either the schedule
changed and practice did not, or practice was never right.

**A group deposit reconciliation** — *Mosofin-specific*. **Filings are per employer**; a group view conceals
an entity with an unsettled obligation.

**A payment by one entity for another's liability** — *Mosofin-specific*. Intercompany, **and the other
entity's obligation is still unsettled on its own account.**

**A result comes back with `mock: true`** — *Mosofin-specific*. **These figures go on a statutory filing.**

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it; **never
file one employer's return under another's registration.**

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
