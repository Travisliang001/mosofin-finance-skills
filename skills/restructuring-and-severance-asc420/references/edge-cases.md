<!-- restructuring-and-severance-asc420 · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

*(A Mosofin addition — the original has no Edge Cases section.)*

**Communication after the period end.** The plan was approved before the year end and communicated after it. Under both frameworks recognition generally follows the communication, so **there is no liability at the balance sheet date** — but there may be a subsequent-events disclosure. `[manual]`. See `subsequent-events-asc855`. Getting this backwards accrues a cost a period early.

**A plan announced and then abandoned.** The provision must be released in full. `[auto]` to detect via Test A; `[manual]` to confirm the abandonment.

**Employees who resign before their termination date.** They may forfeit the enhanced element, reducing the obligation. `[manual]` for the terms; `[auto]` for the signal — someone leaving the payroll earlier than the plan expected.

**Enhanced benefits under an existing plan versus a one-time arrangement.** A benefit paid under a pre-existing severance policy is generally an ongoing benefit arrangement rather than a one-time termination benefit, with different recognition. **The distinction turns on whether the policy existed before the restructuring** — `[manual]`, and easy to overlook when the amounts look identical.

**Statutory minimum notice and redundancy pay.** Frequently a legal obligation independent of any plan, arising on the notice rather than on the announcement, and varying by jurisdiction. `[manual]`. **Do not fold statutory entitlement and discretionary enhancement into one figure** — they can have different recognition dates.

**Pension and benefit consequences of termination.** A curtailment or settlement in a defined benefit plan is a separate calculation, not part of the restructuring provision. `[manual]`. See `pensions-and-postretirement-asc715`.

**Restructuring costs incurred in a business combination.** Costs to restructure an acquired business are generally **not** part of the purchase price allocation — they are post-combination expenses of the combined entity. `[manual]`. A frequent and material error.

**Asset impairments arising from the plan.** Writing down a facility's assets is impairment, **not a restructuring provision.** Keep the two apart; they are different standards and different disclosures. `[auto]` for the signal — a facility exit alongside assets still carried on the books.

**Onerous contracts other than leases.** Where a contract will lose money once operations cease, IFRS in particular has a specific onerous-contract model. `[manual]`. See `construction-percentage-of-completion` for the analogous immediate-loss principle.

**A revision to the estimate.** Prospective — a change in estimate, not an error, and **not a restatement.** `[manual]` to conclude, `[auto]` to quantify. See `restatement-and-prior-period-adjustment`.

**Discounting.** Where payments extend well beyond a year, IAS 37 requires discounting where the effect is material; ASC 420 measures at fair value at initial recognition, which incorporates the time value of money. `[auto]` for the arithmetic given a rate; `[manual]` for the rate. **Do not supply a discount rate** — it is entity- and period-specific.
