<!-- real-estate-and-property-accounting · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All eleven preserved, in order.

**US GAAP has no investment property category**: a US GAAP entity's "investment property" is PP&E at cost. **Do not apply IAS 40 mechanics under US GAAP.** `[manual]` — establish the framework first. This is the most consequential framework error available in this skill, and rental income in the ledger is exactly the thing that tempts it.

**IFRS fair value model**: changes go to **P&L, not OCI**, creating volatility. The choice between cost and fair value is largely a one-way election; switching back from fair value to cost is difficult. `[manual]` to elect; `[auto]` to show the historic volatility where prior valuations are in the books.

**Land versus buildings**: separate at acquisition for depreciation. **Do not depreciate land.** `[auto]` — Test 0a, both variants.

**Component depreciation**: IFRS **requires** identifying significant components with different useful lives and depreciating them separately — roof, HVAC, plant. US GAAP permits it but it is rarely applied in full depth. `[auto]` to detect its absence: **an IFRS reporter with a single depreciation line per building and no component accounts is not doing component depreciation**, and that is a compliance gap visible from the chart alone.

**Capitalised interest**: **stops when ready for intended use, not when finally rented or occupied. Do not over-capitalise.** `[auto]` — Test 0d supplies the strongest available evidence for the readiness date.

**Mixed-use property** (partly owner-occupied, partly rented): under IFRS, classify each portion separately **if they can be sold or leased separately**; if not separable and the own-use portion is insignificant, treat the whole as investment property. Under US GAAP, typically PP&E. `[manual]` for the judgment; `[auto]` for the signal — rental income against a property that also carries own-occupancy costs is the mixed-use pattern.

**Property transfers between classifications**: a change of use has specific transfer rules, **with potential fair-value remeasurement under IFRS at the date of change.** `[manual]` to decide; `[auto]` to detect — a property whose rental income starts or stops is a change of use with an accounting consequence, and it is visible in the month it happens rather than at the year end.

**Sale-leaseback**: complex under ASC 842 / IFRS 16. **First determine whether a sale occurred per 606** — there is no sale if leaseback features defeat the transfer of control. **If no sale, it is financing.** `[manual]` for the assessment; `[auto]` for the signature, which is unmistakable: **a property disposal followed by rent payments to the buyer.** Flag it every time; getting this wrong puts a gain in the P&L that should not be there and removes an asset that should still be on the balance sheet.

**Held-for-sale criteria are strict**: management commitment to sell, available for immediate sale in its present condition, active marketing, sale expected within one year. **Premature held-for-sale classification is a common error.** `[manual]` for the criteria — none of them are in the ledger. `[auto]` for the consequence (Test 0c) and for one corroborating fact: **a property classified held for sale twelve months ago and still on the books** fails the one-year expectation on its face and needs re-assessment.

**Real-estate-specific tax incentives** — depreciation rules, like-kind exchange rules, investment incentives: jurisdiction-specific. Coordinate with the corporate tax return preparation. `[manual]`.

**Construction loss or impairment during development**: where expected net realisable or recoverable amount is below capitalised cost, write it down. `[auto]` for the capitalised cost and the spend profile; `[manual]` for the expected recoverable amount.
