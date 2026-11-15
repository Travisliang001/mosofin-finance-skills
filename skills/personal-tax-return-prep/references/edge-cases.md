<!-- personal-tax-return-prep · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**Residency / domicile complexity**: **residency status determines worldwide vs. local taxation and treaty
positions. Dual-residence, part-year residence, and expatriate situations are complex — flag for
specialist.**

**Foreign income and foreign tax credits**: **foreign income may be taxable at home with credit for foreign
tax, subject to limitations and treaties. Cross-border returns need professional review.**

**Self-employment**: **net business income computation, allowable expenses, home-office, vehicle, and
self-employment or social contributions. Keep the business computation separate and well-documented.**
*Mosofin note*: **the accounting profit is `[auto]`; the tax adjustments are not.**

**Equity compensation**: **stock options, RSUs, ESPP have specific and often surprising tax treatment and
timing. Coordinate with `equity-compensation-accounting` concepts; flag for care.** **The cap table is not
on this surface** — see that skill.

**Capital gains nuances**: **holding periods, principal-residence exemptions, wash-sale-type rules, loss
carryforwards, and special asset rules vary widely. Confirm per jurisdiction.**

**Marriage / joint vs. separate filing**: **where a choice exists, compute both to find the better
outcome.**

**Rental property**: **allowable expenses, depreciation or capital allowances, passive-loss limitations, and
gain on sale recapture vary by jurisdiction.**

**Estimated payments and safe harbors**: **underpayment can trigger penalties; confirm the jurisdiction's
safe-harbor rules.**

**Life events**: **marriage, divorce, new dependents, relocation, inheritance, retirement — each changes the
return. Capture them.**

**High-net-worth complexity**: **trusts, multiple properties, business interests, international holdings —
well beyond a simple return; professional preparation strongly recommended.**

**Rates / allowances / brackets change yearly**: **never hardcode. Confirm current-year parameters from
official sources.**

**A whole-entity figure reported as the taxpayer's income** — *Mosofin-specific, and easy to do*. **A
partner or shareholder takes a share.** Establish the share before using any business figure.

**Another owner's data read into a personal return** — *Mosofin-specific, and a privacy failure*. **Read the
taxpayer's own accounts, not the others'.**

**The business year end and the tax year do not align** — *Mosofin-specific*. **A basis-period question**,
jurisdiction-specific, and it has changed in some places recently. **Ask.**

**Drawings assumed to be income** — *Mosofin-specific*. **They may be capital, a loan, or a distribution**,
and the entity type decides.

**An overdrawn owner's account** — *Mosofin-specific, and readable*. **In several jurisdictions it triggers
a charge on the company, a benefit on the individual, or both.** The balance is exact; the treatment is
`[manual]`.

**Distributions taken but never declared** — *Mosofin-specific*. **The ledger shows what was taken; the
paperwork determines what it was.** A common informality with real consequences.

**Accounting profit used as taxable profit** — *Mosofin-specific*. **Different sets of expenses.** See
`tax-return-prep-corporate`.

**A rate or allowance supplied from memory** — *prohibited*. Every one appears on Sheet 9 with its source and
year.

**A result comes back with `mock: true`** — *Mosofin-specific*. **These figures go on a signed return.**

**Anything about the taxpayer persisted** — *Mosofin-specific, and the rule here is "nothing"*. **A personal
tax computation is among the most sensitive documents a person holds.**

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the figure as `[gated]` in the coverage sheet.
