# Credit memos and refunds — Northbrook Trading Ltd — September 2025

Mosofin is not connected, so this run is manual: every step is `[manual]` and every figure comes from your uploads. Connecting Mosofin would let the original invoices, their tax codes, recorded credits and vendor credits be read from the books ([docs.mosofin.com](https://docs.mosofin.com)).

**Nothing was issued, refunded, applied or sent.** Every entry below is a proposal for a person to post.

## Read-back

Handling **Ridgeway Logistics' 500.00 deduction** for **Northbrook Trading Ltd** (user-asserted), **September 2025**, as at 30 Sep 2025, currency **USD** (user-asserted), from your uploads. Approver for credit memos: **the credit manager**. Not answered, and never defaulted: the **reason as you accept it** (the customer's remittance says "damaged pallet" — that is their claim, not yet your decision), the **credit type** (allowance vs sales return), the **tax treatment** and **tax jurisdiction**, the **chart of accounts**, and the **fiscal year end**. Go-ahead assumed.

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Needed for | Verdict |
|---|---|---|---|---|---|
| `remittance_advice.txt` | Two customer remittance advices: Ridgeway 24 Sep 2025, paying INV-20611 **less 500.00** for a damaged pallet (their ref DM-118); Castleton 23 Sep 2025, paying INV-20574 in full | Northbrook implied; no currency | Yes | Step 1 (type), Step 2 (which invoice) | **Accepted with a limit**: currency user-asserted; it is the customer's account of the deduction, not evidence that the damage happened |
| `ar_aging_detail_2025-09-30.csv` | Open-item receivables ageing at 30 Sep 2025, 14 lines, 12 customers, total 798,360, including credit note CM-0312 (−2,150) | As at 30 Sep 2025; no entity or currency | Yes; gross amounts only, no tax split | Step 2 (existence, balance, period), Step 5 (unapplied credits) | **Accepted with a limit**: company user-asserted; no tax detail, so Step 3 cannot be checked |
| `customer_list.csv` | Customer master: 12 customers, terms (all 30 days), credit limit, contact email | No entity | Yes | Step 1–2 (counterparty and terms on record) | **Accepted with a limit**: company user-asserted; contacts used for nothing — nothing is sent |
| `remittance_advice_final.csv` | **An employee shift rota** (E08–E10, weeks 1–4). Not a remittance despite its name | None | n/a | No step uses it | **Rejected.** If a final remittance file exists, please upload it in its place |

**Still missing:** the **original invoice INV-20611** (lines and any tax); **evidence of the damage** (customer claim DM-118, delivery note, photos) and your decision on it; **cash receipts / bank for 23–30 Sep**; tax jurisdiction; chart of accounts; fiscal year end; **payables data** — without it the vendor-credit sweep cannot run.

*I would wait here for your answer; proceeding with the accepted files as instructed.*

## Findings

**1. Ridgeway's 500.00 is a short-payment deduction, not yet a credit (Step 1).** Ridgeway paid, by its own advice, **72,046.00 − 500.00 = 71,546.00** against INV-20611. Until the credit manager accepts the claim, the 500.00 is a **disputed deduction** still owed. The reason drives the entry and is not inferred from the remittance:
- damaged goods kept by the customer → **allowance**, contra-revenue, no inventory
- damaged goods returned → **sales return**, inventory back at net realisable value, not cost
- claim rejected → no credit; the 500.00 stays receivable and is chased.

**2. Validation against the original (Step 2).**

| Check | Result |
|---|---|
| Invoice exists | INV-20611, Ridgeway Logistics, 21 Jul 2025, due 20 Aug 2025 (30 days, matches terms on record) — **yes** |
| Credit ≤ invoice balance | 500.00 ≤ 72,046.00 open — **passes**; no excess-credit approval needed beyond the credit manager |
| Period | Invoice July 2025, credit September 2025 — different month; same fiscal year **assumed** (year end not given). Post to September, no restatement |
| Currency | USD both (user-asserted) — passes |

**3. INV-20611 still shows fully open at 30 Sep.** The ageing carries **72,046.00, 41 days overdue**, six days after the 24 Sep remittance. Either the 71,546.00 has not arrived, or it arrived and was not applied. Check the bank; this is a cash-application question, not a credit.

**4. Castleton's "paid in full" is not reflected either.** Remittance of 23 Sep for INV-20574 (88,056.00, due 8 Oct); the ageing still shows it open in full. Same check as finding 3.

**5. Tax reversal (Step 3): cannot be computed.** The ageing shows gross amounts only and no jurisdiction was given. If INV-20611 carried tax, the 500.00 must be split into net and tax in the same proportion as the original, as a separate line. Upload the invoice.

**6. Proposed entry — only if the credit manager accepts the claim as an allowance (Step 4).** Account names are placeholders until you supply your chart.

```
DR  Sales returns & allowances (contra-revenue)     500.00   (net — split out tax if INV-20611 had tax)
    CR  Accounts receivable — Ridgeway Logistics        500.00
Memo: Credit memo [CM #] re: INV-20611 — damaged pallet, customer ref DM-118; approved by credit manager
```

Balances: 500.00 = 500.00. Then apply the credit to INV-20611 in the sub-ledger: 72,046.00 − 71,546.00 cash − 500.00 credit = **0.00**. **No second journal on application.** If the goods came back, use the sales-return entry instead, with inventory at net realisable value.

**7. Unapplied customer credit: Calder Print CM-0312, −2,150.00, dated 2 Sep 2025 (Step 5).** 28 days on account, **no original invoice referenced** — business reason and approval should be documented. Suggested application: Calder's open INV-20796 (32,020.00, 20 days overdue) → 29,870.00 would remain; sub-ledger only, no new JE.

**8. Vendor credits: not swept.** No payables data uploaded; the unapplied vendor-credit register is **not done**, not nil.

## Credit register (proposal)

| CM # | Date | Type | Counterparty | Original | Original amount | Credit | Tax reversed | Reason | Status |
|---|---|---|---|---|---:|---:|---|---|---|
| (to issue) | Sep 2025 | Allowance or sales return — **to confirm** | Ridgeway Logistics | INV-20611 | 72,046.00 | 500.00 | Unknown | Damaged pallet (customer-claimed, DM-118) | Awaiting credit manager |
| CM-0312 | 2 Sep 2025 | Customer credit | Calder Print | **None** | — | 2,150.00 | Unknown | Not recorded | Open, unapplied |

## Coverage sheet (manual run)

**Environment:** Northbrook Trading Ltd, September 2025, USD — user-asserted. Data source: upload (gateway absent). Three files accepted with limits; `remittance_advice_final.csv` rejected (shift rota). **Capability map:** Not applicable: no connection. Every task is `[manual]`.

| Step | Status | Gap |
|---|---|---|
| 0 Evidence | Done with a limit | No invoice copy, bank, AP, COA |
| 1 Type | Done with a limit | Allowance vs return needs your reason |
| 2 Validate | Done (4 checks) | Fiscal year end assumed |
| 3 Tax | **Not done** | Invoice tax lines, jurisdiction |
| 4 JE | Proposed, not posted | Credit manager approval; real accounts |
| 5 Application | Done for customers; **vendors not done** | Payables data |
| 6 Output | Tables in chat | `CreditMemos_2025-09.xlsx` only on a yes |
| 7 Save | Not done | Offered only after approval |

**Data sources:** user uploads — `remittance_advice.txt`, `ar_aging_detail_2025-09-30.csv`, `customer_list.csv`. Nothing was issued, refunded, applied, sent or changed.
