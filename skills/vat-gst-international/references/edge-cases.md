<!-- vat-gst-international · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All eleven preserved, in order.

**Zero-rated versus exempt confusion**: **the single most consequential VAT distinction. Zero-rated preserves input recovery; exempt blocks it. Misclassifying changes net VAT materially. Always confirm which applies.** `[manual]` to determine; **`[auto]` to detect the consequence** — Step 5b.

**Partial exemption**: **an entity making both taxable and exempt supplies can only recover input VAT on the taxable portion. Apply the country's partial-exemption method. This is complex — flag for careful calculation.** `[manual]` for the method; `[auto]` for the turnover-based arithmetic and for detecting that no restriction is being applied at all.

**Non-established businesses**: **selling into a country without establishment often triggers registration with a nil threshold and may require a fiscal representative. Country-specific.** `[manual]`. **`[auto]` for the trigger** — any local supply at all, which is a different query from a threshold test.

**Digital services to consumers (B2C)**: **taxed where the consumer is located, regardless of supplier location. OSS/IOSS or local registration may be needed. Requires evidence of customer location.** `[auto]` for B2C supplies by country **where consumer location is recorded**; **`[manual]` for the evidence**, which typically requires two non-contradictory pieces and is not in a ledger.

**Reverse charge net-nil trap**: **both sides must be reported even where the net effect is nil. Omitting them is a reporting error even with no cash effect.** **`[auto]` — Step 4b, the best detection in the skill.**

**Invalid customer VAT number**: **relying on a customer's VAT number for zero-rating or reverse charge that turns out invalid can shift the VAT liability back to the supplier. Validate (e.g. VIES).** `[manual]` to validate; **`[auto]` to find supplies zero-rated to customers with no number recorded at all** — which is the weaker case and the easier fix.

**Import VAT**: **VAT on imported goods, paid at customs or postponed (postponed import VAT accounting in some countries). Recoverable like input VAT if conditions met. Coordinate with customs documentation.** `[auto]` for import VAT posted; **`[manual]` for the customs documents**, which are not on this surface. **And note: postponed accounting means the VAT never leaves the bank**, so an entity using it will show import VAT on both sides with no cash movement — which looks like an error and is not.

**Intra-EU movements**: **dispatches and acquisitions have specific treatment, EC Sales Lists, and Intrastat above thresholds. Distinct from imports and exports outside the EU.** `[auto]` for the transactions; `[manual]` for the thresholds and the treatment.

**E-invoicing and real-time reporting mandates**: **many countries now mandate e-invoicing or real-time or near-real-time VAT reporting — SAF-T, SII, various clearance models. Flag the entity's obligations.** **`[manual]`, and flag early.** This is a **systems** obligation, not a filing one — transactions may need clearing with the authority as they are issued, which cannot be retrofitted at period end.

**Bad debt relief**: **VAT on unpaid invoices may be recoverable after a period — country-specific conditions.** **`[auto]` to identify the population** — receivables aged beyond the relevant period, from `ar-aging-and-collections` — `[manual]` for the conditions. **This one is in the client's favour and is routinely unclaimed**, because nobody goes looking for it.

**Rate, threshold and rule changes**: **VAT rules change frequently — rate changes, threshold changes, new digital-reporting mandates. Any figure must be current-sourced. The skill flags, never hardcodes.** `[manual]`. **The source's own statement of the seed principle.**
