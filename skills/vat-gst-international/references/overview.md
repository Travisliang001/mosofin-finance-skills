<!-- vat-gst-international · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# VAT / GST (International) — Mosofin Seed

Handles value-added tax and goods-and-services tax outside the US: registration thresholds, output and input VAT, place-of-supply rules, reverse charge, cross-border treatment, special schemes (EU OSS/IOSS), returns and reconciliation.

**VAT/GST is a transaction tax used by most countries worldwide, each with its own rates, rules and filing requirements.**

This is a **seed skill**, written to be rewritten the first time it runs against a real workspace.

---

## The discipline, stated by the source

> **Critical**: this skill does NOT hardcode VAT/GST rates, registration thresholds, or country-specific rules — they vary by country and change. The skill builds the framework and computes from rates and thresholds the user supplies or that are confirmed against current official sources at the time of use. **Unknown current values are flagged, not assumed.**

**The sixth source in this pack to state it.** The pattern across the tax skills is now fully established and it is correct: **nothing below supplies a rate, a threshold or a rule, and nothing persisted from a prior run may supply one either.** Gate 2 applies the same principle to capabilities.

---

## How this differs from US sales tax, and why it matters here

`sales-tax-us-multistate` is the closest sibling, and the two share a shape — a transaction tax, registration thresholds, jurisdiction-specific treatment. **But VAT sits in the ledger in a way US sales tax does not**, and that changes what is automatable.

| | US sales tax | VAT / GST |
|---|---|---|
| **Tax on sales** | Collected and held | **Output VAT — a posted amount in a named account** |
| **Tax on purchases** | Generally a cost, or a use-tax self-assessment | **Input VAT — a posted, recoverable amount in a named account** |
| **A control account** | Usually a single payable | **A VAT control account that nets input against output and reconciles to the return** |

**So VAT is a two-sided tax that the accounting system actually accounts for**, which makes Step 8's reconciliation genuinely automatic on three of its four legs, and makes several substantive errors directly detectable.

**Three that are worth the connection on their own:**

- **The reverse-charge net-nil trap** — see Step 4b. **The best detection target in the skill.**
- **Input VAT recovered in full while exempt supplies are being made** — a partial exemption restriction that was never applied.
- **A VAT control account that only grows** — VAT collected and not paid over, which in most regimes is trust money.

### Three near-substitutes

**1. A tax code is not a treatment determination.** Shared with `sales-tax-us-multistate`. The code records what somebody configured, possibly years ago, possibly by copying another customer. **Place of supply, zero-rating and exemption are determinations**, and the whole of Steps 2 and 3 exists because they are frequently got wrong.

**2. Nil net VAT is not a nil reporting obligation.** The reverse charge often nets to zero, and **both legs must still be reported.** An entity that omitted both has the right net position and a wrong return — see Step 4b.

**3. The VAT in the ledger is what was charged, not what was due.** If output VAT was charged at the wrong rate, or on a supply that should have been zero-rated, or not charged where it should have been, the ledger faithfully records the error. **Reading it tells you what happened, not what ought to have.**

---

## Related skills

| Skill | Relationship |
|---|---|
| `sales-tax-us-multistate` | The US equivalent, explicitly out of scope — same exposure-join and collected-not-remitted logic. |
| `balance-sheet-reconciliations` | The VAT control account reconciliation. |
| `revenue-recognition-asc606` | Its Test 0d checks that tax is out of revenue — the same amounts from the other side. |
| `invoice-data-extractor` / `three-way-match` | Supplier invoices, and whether VAT was charged on them. |
| `tax-return-prep-corporate` | The same blocked-cost population as the disallowables sweep. |
| `transfer-pricing-documentation` | TP adjustments affecting customs valuation and VAT. |
| `ar-aging-and-collections` | The aged receivables population for bad debt relief. |
| `month-end-close-checklist` | Where the VAT reconciliation belongs as a recurring task. |
| `quarter-end-close` | Where registration and threshold movement should be reviewed. |
| `multicurrency-fx-revaluation` | Cross-border supplies and the rate used for VAT on foreign-currency invoices. |
