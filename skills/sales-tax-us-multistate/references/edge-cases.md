<!-- sales-tax-us-multistate · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All eleven preserved, in order.

**Inventory in FBA or third-party warehouses**: **storing inventory in a state generally creates physical nexus there.** Amazon FBA can create nexus in many states. **Map where inventory sits.** `[manual]` — **and it is the single most important `[manual]` in this skill.** A ledger records inventory's cost and existence; it never records its location. A seller can have physical nexus in a dozen states they have never visited, established by a fulfilment network they do not control, and **nothing in their accounting system will ever mention it.** Ask directly, every time.

**Trailing nexus**: after nexus ends — closing a location, say — **some states require continued collection for a period. Confirm.** `[manual]`. Easy to get wrong in the relieved direction.

**Crossing a threshold mid-year**: **nexus begins when the threshold is crossed; the collection obligation starts shortly after, with a state-specific grace period. Do not collect before nexus or fail to collect after.** `[auto]` for the crossing date — this is the trigger-date computation in Step 1; `[manual]` for the grace period.

**Local-rate complexity**: **home-rule jurisdictions** — parts of Colorado, Louisiana, Alabama — **administer their own local taxes separately from the state. Returns may be filed locally.** `[manual]`, and note the practical consequence for Step 7: **the ledger's tax detail is frequently less granular than a home-rule return requires.** Where local returns are needed and the books carry only a state-level tax code, the return cannot be prepared from the ledger alone.

**Bundled transactions**: a taxable item bundled with an exempt item — **taxability depends on the state's bundling rules.** `[manual]`. `[auto]` for the signal: invoices combining item types that the matrix treats differently.

**SaaS and digital products**: **among the most state-variable areas. The same product can be taxable in one state and exempt in another. Never assume; confirm per state.** `[manual]`, and this is where an automated answer would be most confidently wrong.

**Drop-shipping**: three-party transactions — customer, seller, drop-shipper — **create complex nexus and resale-certificate issues. Flag for careful analysis.** `[manual]`. `[auto]` for the signal: a vendor shipping directly to a customer address.

**Exemption certificate gaps**: **a sale treated as exempt without a valid certificate on file = the entity owes the tax. Audit the certificate file.** **`[auto]`** — Step 5's join does exactly this, over the full population rather than a sample.

**Prior-period exposure**: **historical nexus without registration creates back-tax exposure. VDAs can limit look-back and waive penalties. Flag for specialist.** `[auto]` to quantify indicatively; `[manual]` for the strategy, and **flag before registering**, because sequencing affects what can be negotiated.

**Rate and threshold changes**: **these change often. Any figure used must be current-sourced. The skill flags, never hardcodes.** `[manual]`. **The original's own statement of the seed principle**, and it governs this file: no rate, no threshold, nothing carried forward.

**Origin versus destination sourcing**: **most states are destination-based, a few origin-based, and intrastate versus interstate can differ. Confirm per state.** `[manual]` — **and this is why the ship-to address matters**, per the near-substitute note. A destination-sourced state needs the delivery address, and a billing address is not one.
