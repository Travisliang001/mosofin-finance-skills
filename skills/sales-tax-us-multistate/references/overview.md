<!-- sales-tax-us-multistate · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# US Sales Tax (Multistate) — Mosofin Seed

Handles US sales and use tax across states: nexus analysis, taxability determination, rate application, return preparation and reconciliation. US sales tax is uniquely complex — roughly 45 states plus thousands of local jurisdictions, each with its own rules, rates and thresholds.

This is a **seed skill**, written to be rewritten the first time it runs against a real workspace.

---

## The source already states the seed discipline

The original opens with it, in bold, and it is exactly right:

> **Critical**: this skill does NOT hardcode rates, economic-nexus thresholds, or taxability rules — these change frequently and vary by jurisdiction. The skill builds the framework and computes from rates and thresholds the user supplies or that are confirmed against current published state sources at the time of use. Where a current value is needed and not supplied, **the skill flags it for confirmation rather than assuming.**

**That is preserved in full and nothing below weakens it.** No rate, threshold or taxability rule appears anywhere in this file, and **nothing persisted from a prior run may supply one either** — a threshold stored last year is last year's threshold, and states change them.

The conversion extends the same instinct one layer outward, as it does in `r-and-d-tax-credit`: **capabilities change too, and must be read fresh at Gate 2** rather than remembered. Same argument, different subject.

---

## Where a live ledger genuinely helps, and where it must not be trusted

This skill splits unusually cleanly, and the automatic half happens to be the half that determines exposure.

**What the workspace supplies, exactly:**

- **Sales by state, by period** — the numerator of every economic nexus test
- **Transaction counts by state, by period** — the *other* threshold, which is measured separately and is routinely forgotten
- **The month the threshold was crossed** in each state — which is the **nexus trigger date**, and therefore the start of the back-tax exposure period
- **Exempt sales by customer and state** — the population that needs certificates behind it
- **Purchases with no tax charged** — the use-tax population
- **Sales tax collected and the tax payable balance** — the reconciliation, and the trust-money question

**What it cannot supply, at all:**

- **Thresholds.** Current-sourced, per state, every time.
- **Rates.** Same.
- **Taxability.** Product × service × state is thousands of determinations, each state-specific, many genuinely contested. The original is emphatic and it is right: **never assume; confirm per state.**
- **Physical presence facts.** Where inventory sits, where employees work, where a contractor visited. None of it is in a ledger.
- **Registration status.** A registration is a relationship with a state, not a transaction.

### A near-substitute is not a substitute — three of them, all consequential

**1. The billing address is not the ship-to address.** Most states source destination-based: **the rate and the state are determined by where the goods went**, not where the invoice was sent. Many accounting systems carry only a billing address on the customer record. **Computing state-by-state sales from billing addresses will misstate the nexus analysis** — a customer headquartered in one state taking delivery in six others produces one state's worth of sales in the data and six states' worth of obligation in reality.

**Check which address the data actually holds before computing anything by state**, and say which was used. Where only a billing address exists, the analysis is indicative and must be labelled that way.

**2. A tax code in the accounting system is not a taxability determination.** It is what somebody configured — possibly before *Wayfair*, possibly by copying another customer, possibly correctly. Reading tax codes tells you what the system did. It does not tell you what the law requires, and the entire point of Step 3 is that those differ more often than anyone expects.

**3. Tax collected is not tax owed.** They differ in both directions — under-collection is a liability the entity must fund itself, over-collection cannot simply be kept — and Step 8 exists to find the gap.

### And one scope boundary the original draws well

> **This skill validates and reconciles rather than serving as the real-time rate engine.**

Preserved with emphasis. **Mosofin is not a rate engine and must not be used as one.** For any material transaction volume the entity needs a proper tax engine doing address-level rating at the point of sale. This skill checks what that engine did, finds where it was not used, and reconciles the result. That division suits a read-only connection exactly.

---

## Related skills

| Skill | Relationship |
|---|---|
| `vat-gst-international` | The non-US equivalent, explicitly out of scope here. |
| `corporate-tax-provision-asc740` | Income tax, explicitly out of scope. |
| `balance-sheet-reconciliations` | The GL leg of Step 8's reconciliation. |
| `revenue-recognition-asc606` | Test 0d there checks that sales tax is *out* of revenue — the same amounts from the other side. |
| `invoice-data-extractor` | Untaxed purchase invoices, which are the use-tax population. |
| `fixed-asset-register-and-depreciation` | Out-of-state asset purchases — the largest single use-tax items. |
| `three-way-match` | Where a purchase's tax treatment is first visible. |
| `month-end-close-checklist` | Where the sales tax payable reconciliation belongs as a recurring task. |
| `quarter-end-close` | Where nexus and threshold movement should be reviewed each quarter. |
| `merchant-and-payment-processor-rec` | Marketplace and processor settlements, and their net-deposit problem. |
