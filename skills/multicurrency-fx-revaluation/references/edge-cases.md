<!-- multicurrency-fx-revaluation · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**Monetary vs. non-monetary classification**: **cash, receivables, payables, accrued items, debt =
monetary. Inventory, PP&E, intangibles, prepaid, deferred revenue, equity = non-monetary. Misclassification
leads to wrong remeasurement.**

**Prepaid revenue vs. deferred revenue**: **deferred revenue is typically non-monetary — it settles by
delivery, not cash — don't remeasure. Common error.** *Mosofin note*: **it sits among current liabilities
beside genuinely monetary items**, which is why it is misclassified so often.

**Non-monetary at fair value** — e.g. available-for-sale, certain investments: **may be remeasured to fair
value in the foreign currency, with the FX effect treated per the asset's measurement guidance.**
**[manual]**; there are no fair values here.

**Intercompany monetary balances**: **remeasured at the entity level; the FX may eliminate in consolidation
but the resulting CTA-like effect on long-term intercompany items can remain in OCI** — specific guidance
for long-term-investment-nature intercompany balances. See `intercompany-reconciliation`.

**Disposal of a foreign operation**: **the related accumulated CTA is reclassified from OCI to P&L on
disposal** — US GAAP and IFRS, with details. **Track the CTA per operation so it can be released.**
*Mosofin note*: **a single group CTA account cannot be released selectively** — the tracking must exist
before the disposal, not after.

**Goodwill in a foreign sub**: **denominated in the sub's functional currency; translated at the closing
rate each period, creating CTA on goodwill.**

**Rate volatility and intra-period activity**: **using a true period-average vs. month-end-average for the
IS can produce different translations. Pick a consistent approach for material periods.** *Mosofin note*:
**whether earnings are evenly spread is measurable** from the monthly P&L — test before relying on a simple
average.

**Hyperinflation**: **requires restatement before translation — different mechanics; specialized.**

**Foreign-currency loans designated as hedges of net investment**: **their FX effect goes to OCI, offsetting
the CTA, under hedge designation. Without designation, it goes to P&L.** **The designation is `[manual]`**,
and the difference between the two treatments is entirely documentary.

**Functional currency change**: **applied prospectively from the date of change; cumulative CTA carried
forward.**

**Balances are not currency-tagged** — *Mosofin-specific, and the gating question*. **Revaluation cannot be
performed from the ledger.** Say so; ask where the currency detail lives.

**The platform already revalues** — *Mosofin-specific*. **A proposed manual entry would double-count.**
Establish it at Step 0b and compare rather than propose.

**Posted FX does not match the computed FX** — *Mosofin-specific, and the most useful finding*. The rate,
the population or the classification differs. Investigate all three.

**Home currency and functional currency disagree** — *Mosofin-specific*. **Raise before revaluing.** It
decides which method applies and therefore which statement the difference lands in.

**Realized and unrealized reported together** — *Mosofin-specific opportunity*. **The split is readable**,
and it matters: **unrealized reverses, realized does not.**

**Transaction FX and translation conflated** — the original's own warning, and **it is easy to commit when
one entity has both.** They are computed separately and land in different statements.

**A rate supplied from memory** — *prohibited*, here as everywhere in this pack.

**A result comes back with `mock: true`** — *Mosofin-specific*. Revaluation against fixture balances.

**A stored rate or FX amount is reused** — *Mosofin-specific*. Rates are state. **Persist the source and the
policy; re-obtain the rates.**

**A stored classification applied to another entity's chart** — *Mosofin-specific*. Account numbers differ;
the classification would attach to the wrong accounts.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet, **naming the
entity**.
