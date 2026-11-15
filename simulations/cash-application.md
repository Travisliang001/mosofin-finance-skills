# Cash application — Northbrook Trading Ltd, lockbox 22–26 September 2025 (upload path)

Mosofin is not connected, so this run is manual and works only from your uploads (connecting Mosofin would read the open invoices and customer master directly: docs.mosofin.com). **Nothing was applied, posted or written off**; every application and entry below is a proposal for a person to enter.

## (a) Read-back

Applying **5 lockbox receipts (22–26 Sep 2025)** for **Northbrook Trading Ltd**, in **USD**, against **your A/R aging detail as at 30 Sep 2025**, using **your remittance advices** and **your cash application policy**. Population processed: **a supplied file of payments not yet recorded** (all five invoices are still open on the 30 Sep aging).

| Input | Status | Treatment |
|---|---|---|
| Tolerance (short / over pay) | In your policy file: short-pay write-off up to 50, credit-manager approval | Used once you confirm this read-back |
| Unapplied cash account | In your policy file: credit held in **1100 Accounts Receivable**; 2100 not used | Used instead of a separate "unidentified deposits" account |
| Application order (FIFO) | Not answered | Default oldest-first; no receipt in this batch needed it |
| FX / withholding tax | Not needed: every receipt and invoice is USD per your intake; no deduction cites tax | Step 5 not applicable |
| Customer master / payer aliases | Not supplied | Payer names matched against the customer names in the aging only |

## (b) Validation of the upload — shown before any work

| File | What it actually is | Company / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `ar_aging_detail_2025-09-30.csv` | Invoice-level open A/R: customer, invoice, dates, amount, days overdue. 13 invoices + 1 credit memo (CM-0312, −2,150), net 797,510 | As at 30 Sep 2025 (days overdue recompute to that date). No company or currency named | Yes. The "amount" column is taken as the **open balance**; the file does not say | Yes — Steps 1–4 (invoice side) | **Accepted with a limit**: company/currency user-asserted; open vs original amount not labelled |
| `lockbox_2025-09-22_to_26.csv` | Lockbox receipts: date, payer bank string, reference, amount. 5 rows, total **331,712** | 22–26 Sep 2025. No company, currency or lockbox account named | Yes | Yes — Steps 1–2 (payment side) | **Accepted with a limit**: company/currency user-asserted |
| `remittance_advice.txt` | Two customer remittance advices (Ridgeway 24 Sep, Castleton 23 Sep) | Sep 2025; matches two lockbox rows | Yes | Yes — Step 2 (Castleton) and Step 3 (Ridgeway short pay reason) | **Accepted** |
| `cash_application_policy.md` | Your policy: write-off threshold 50; unapplied cash held in 1100 | Undated | Yes | Yes — Steps 3, 4, 6 | **Accepted** |
| `lockbox_2025-09-22_to_26_final.csv` | **Not a lockbox file.** A staff shift rota: employee E08–E10, week_1–week_4, "nights/days/off" | No company, dates or amounts | No | No step uses it | **Rejected** on content. If a corrected lockbox file exists, please upload it; otherwise I use `lockbox_2025-09-22_to_26.csv` |

Still missing (recommended, not blocking): the customer master or known payer aliases; the chart of accounts, so I can name your cash account; payment terms, to evidence any early-pay discount.

*I would stop here and wait. Assumed answer: "go ahead with the accepted files".*

## (c) Findings

### Payment-to-invoice mapping

| # | Date | Payer (bank string) | Amount | Invoice | Applied | Residual | Match level | Confidence |
|---|---|---|---:|---|---:|---:|---|---|
| 1 | 22 Sep | PENNINE RETAIL GRP | 112,071 | INV-20537 | 112,071 | 0 | 1 — reference cites invoice | Name 0.947 vs "Pennine Retail Group" |
| 2 | 23 Sep | CASTLETON FOODS LTD | 88,056 | INV-20574 | 88,056 | 0 | 2 — name + amount, single open invoice; confirmed by remittance | Name 0.882; no other open invoice of 88,056 |
| 3 | 24 Sep | RIDGEWAY LOG | 71,546 | INV-20611 | 71,546 | **500** | 1 — reference cites invoice | Name 0.800 (bank truncation of "Ridgeway Logistics"; reference carries the match) |
| 4 | 25 Sep | ASHBY ENG | 56,036 | INV-20685 | 56,036 | 0 | 1 — reference "INV20685" read as INV-20685 (hyphen missing) | Name 0.692, truncation of "Ashby Engineering"; amount agrees exactly |
| 5 | 26 Sep | UNKNOWN PAYER 4471 | 4,003 | — | 0 | — | **6 — no match: unidentified** | Name matches no customer |

### Application summary

| | USD |
|---|---:|
| Total receipts processed | 331,712 |
| Applied to invoices (4 receipts) | 327,709 |
| Unidentified, held as a credit in 1100 Accounts Receivable | 4,003 |
| Short-pay residual left open | 500 |
| Overpayments / customer credits created | 0 |

### Exceptions

| # | Issue | Evidence | Proposed action |
|---|---|---|---|
| 3 | **Short pay 500 — customer-claimed deduction** (Ridgeway, damaged pallet, their ref DM-118) | Remittance 24 Sep; INV-20611 open 72,046 − 71,546 = 500. No Ridgeway credit memo on the aging | **Not written off**: 500 exceeds your 50 write-off limit. Apply 71,546 and leave 500 open on INV-20611 as a **disputed deduction**; credit manager to investigate the damage claim. The invoice was 41 days overdue at 30 Sep |
| 5 | **Unidentified receipt 4,003** | No payer name, no reference | Hold as an unapplied credit in **1100** (per policy; not 2100). The amount equals Foxhall Garden Centres INV-20907 (4,003, 130 days overdue), but **an amount-only match is not a match**: ask the bank for the originator of "4471" or ask Foxhall for a remittance before applying |
| 4 | Reference format | "INV20685" lacks the hyphen | Applied on reference plus exact amount; confirm "ASHBY ENG" as an alias for Ashby Engineering |
| — | Calder Print credit memo CM-0312 (−2,150) still open beside INV-20796 (32,020) | Aging | Not part of this batch; noted so it is applied when Calder pays |

**Other checks.** No receipt exceeds its invoice, so no duplicate or overpayment arises. No two open invoices share any receipt amount. All dates and currencies agree; no early-pay discount was taken (Ashby paid 2 days before due at full amount).

### Proposed journal entry — proposal only, nothing posted

The cash account name was not supplied; it is shown as a placeholder. 1100 is your policy's account.

| Line | Account | DR | CR |
|---|---|---:|---:|
| 1 | Cash — lockbox bank account *(name needed)* | 331,712 | |
| 2 | 1100 Accounts Receivable — Pennine Retail Group, INV-20537 | | 112,071 |
| 3 | 1100 Accounts Receivable — Castleton Foods, INV-20574 | | 88,056 |
| 4 | 1100 Accounts Receivable — Ridgeway Logistics, INV-20611 (500 stays open as disputed) | | 71,546 |
| 5 | 1100 Accounts Receivable — Ashby Engineering, INV-20685 | | 56,036 |
| 6 | 1100 Accounts Receivable — unapplied credit, unidentified receipt 26 Sep | | 4,003 |
| | **Total** | **331,712** | **331,712** |

Memo: Cash application — lockbox 22–26 Sep 2025. No discount, bank fee, WHT or FX line is needed. After it, the four applied invoices close except 500 on INV-20611.

## (d) What was not done, and why

| Step | Status | Gap |
|---|---|---|
| 1 Parse | done from uploads | Lockbox account and currency not in the file |
| 2 Match | done; 4 applied, 1 unidentified | No customer master; aliases unconfirmed |
| 3 Short pay | done | Reason is the customer's claim; damage not verified |
| 4 Overpay / duplicate check | done — none | Prior-period payments not supplied, so duplicates checked within this batch only |
| 5 Multi-currency | not applicable | All USD |
| 6 Journal entry | proposed | Cash account name needed; nothing posted |
| 7 Workbook | not created | Would you like `Cash_Application_2025-09-26.xlsx`? Only on a yes |
| 8 Save aliases | not offered yet | Only after you review: "ASHBY ENG", "RIDGEWAY LOG" and others would be saved, no payment data |

**Coverage (manual run).** Environment: Northbrook Trading Ltd, USD, user-asserted; data source upload; file verdicts as in (b). Capability map: not applicable, no connection; every task `[manual]`. Not done: tie of the aging to the A/R control account; review of recorded payments and deposits for netted fees; credit-memo search beyond the aging — each needs a GL or payments export.

**Data sources:** user uploads only — `lockbox_2025-09-22_to_26.csv`, `ar_aging_detail_2025-09-30.csv`, `remittance_advice.txt`, `cash_application_policy.md`.
