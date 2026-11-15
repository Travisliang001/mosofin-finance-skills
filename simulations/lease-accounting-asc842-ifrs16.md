# Lease accounting (ASC 842, lessee) — Northbrook Trading Ltd, at 30 September 2025

Mosofin is not connected, so this run is manual: every step is `[manual]`, on the files you uploaded. (Connecting Mosofin would search 24+ months of vendor payments for unrecorded leases — docs.mosofin.com. Not raised again.) **Every entry below is a proposal; nothing is posted.**

## (a) Read-back

- **Entity:** Northbrook Trading Ltd (user-asserted), **lessee**, **ASC 842**, at **30 September 2025**, USD. **Short-term expedient elected.** Low-value: not applicable under ASC 842. Lease register: the two leases in `lease_terms.md`; no modifications reported.
- **Discount rate (user-supplied):** **6.0%** incremental borrowing rate, from the lender's indicative quote dated **12 December 2023** — three weeks before the warehouse commencement, so it is a commencement-date rate. Applied as 0.5% a month (6.0% ÷ 12) — please confirm that convention.
- **Renewal option** (warehouse, one 3-year renewal at market rent): **the "reasonably certain" judgement is yours.** Not stated, so the term below is the **5-year non-cancellable period only**; renewal excluded. Tell me if you consider it reasonably certain and I will remeasure.

## (b) Validation of the uploaded files (before any work)

| File | What it actually is | Right company / period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `lease_terms.md` | Key terms of 2 leases (start, term, payment, escalation, option) + discount rate and its source | No entity named; leases from 2024-01-01 and 2025-03-01 | Yes | Steps 1–9 (term, payments, rate, measurement) | **Accepted with a limit:** a summary, not the agreements; every term is user-supplied, not evidenced. Fair value and economic life not given |
| `trial_balance_2025-09-30.csv` | Trial balance, 33 accounts | No entity named; date from the file name | Foots: 6,546,018 = 6,546,018 | Step 0b (expense without an asset), Step 6 tie-out | **Accepted with a limit:** company and period user-asserted |
| `profit_and_loss_2025_ytd.csv` | Monthly P&L Jan–Sep 2025, 13 lines | No entity named; 9 months | Yes; rent 81,000 and interest 10,474 tie to the TB | Step 0b Test 1, Step 6 level-expense check | **Accepted with a limit:** company user-asserted; no 2024 months, so 2024 rent is not evidenced |
| `lease_terms_final.csv` | **An employee shift roster** (E08–E10, weeks 1–4) — not lease terms despite the name | No company, no period | No lease data | No step uses it | **Rejected:** a staff rota. Upload the lease agreements or a revised terms list instead |

**Still missing:** the **lease agreements** themselves (recommended over key terms); **fair value and economic life of the warehouse** (needed for ASC 842 classification tests 3–4); **2024 rent postings** (to size the prior-year correction); vendor payment history (for the recurring-payment search).

I would stop here and wait for your answer. *(Assumed answer: "go ahead with the accepted files".)*

## (c) Findings

### Completeness (before measurement)

1. **Expense without an asset — the warehouse lease is not on the balance sheet.** The TB has **no right-of-use (ROU) asset and no lease liability**; account 6100 Rent carries **81,000 = 9 × 9,000**. A 5-year lease from 1 Jan 2024 is not short-term, so the expedient cannot exclude it. It must be recognised.
2. **The 3% January escalation is not in the ledger.** Contract rent for 2025 is 9,000 × 1.03 = **9,270 a month**; the ledger shows 9,000 every month. **Shortfall 270 × 9 = 2,430** to September — either the increase was not paid (arrears owed to the lessor) or not booked. The contract and the landlord's statement decide.
3. **Office printer — short-term, correctly off balance sheet.** 12 months from 1 Mar 2025, no purchase option → the elected expedient applies: expense 180 a month (1,260 to September), disclosed as short-term lease expense. It is not visible in 6100 Rent (exactly 9,000 a month), so it sits in another line — please say which. It ends 28 Feb 2026; a renewal past 12 months would need reassessment.
4. Recurring-payment search for other unrecorded leases: **not run** — no vendor payment listing.

### Warehouse — classification (ASC 842)

No ownership transfer, no purchase option; specialised asset: not indicated. **The economic-life and fair-value tests cannot be run without those figures**, so classification is **operating, provisionally** — confirm both. Schedules below are on the operating basis.

### Initial measurement at 1 January 2024 (proposal)

Payments in advance: 9,000 (2024), 9,270 (2025), 9,548.10 (2026), 9,834.54 (2027), 10,129.58 (2028); **total 573,386.64**. PV at 0.5% a month = **lease liability and ROU asset 495,030.73** (no initial direct costs, incentives or prepayments). **Straight-line lease expense = 573,386.64 ÷ 60 = 9,556.44 a month.**

### Schedule extract (effective interest; operating-lease ROU as the balancing figure)

| Month | Payment | Interest | Liability (closing) | ROU asset | Straight-line accrual |
|---|---|---|---|---|---|
| Jan 2024 | 9,000.00 | 2,430.15 | 488,460.88 | 487,904.44 | 556.44 |
| Dec 2024 | 9,000.00 | 2,059.64 | 413,987.98 | 407,310.65 | 6,677.33 |
| Jan 2025 | 9,270.00 | 2,023.59 | 406,741.57 | 399,777.80 | 6,963.77 |
| **Sep 2025** | 9,270.00 | 1,728.61 | **347,450.60** | **338,195.28** | 9,255.32 |
| Dec 2028 | 10,129.58 | 0.00 | 0.00 | 0.00 | 0.00 |

Total lease expense is **level at 9,556.44 a month** by construction (the ROU amortisation is the plug). At 30 Sep 2025: liability **current 96,058.73**, **non-current 251,391.87**.

### Proposed catch-up entry at 30 September 2025 (PROPOSAL — NOT POSTED)

| Account | Debit | Credit | Memo |
|---|---|---|---|
| Right-of-use asset — warehouse (new account) | 338,195.28 | | Recognise ROU, Unit 4 |
| 6100 Rent (lease expense), 2025 | 5,008.00 | | Straight-line 86,008.00 vs 81,000 booked |
| 3100 Retained earnings (2024 correction) | 6,677.33 | | Straight-line 114,677.33 vs **108,000 assumed booked in 2024 — confirm** |
| Lease liability — current (new account) | | 96,058.73 | |
| Lease liability — non-current (new account) | | 251,391.87 | |
| 2100 Accrued Liabilities | | 2,430.01 | Unpaid 2025 escalation (finding 2); 0.01 rounding |
| **Total** | **349,880.61** | **349,880.61** | Balanced |

The 2024 line is a prior-period correction; whether it goes through opening retained earnings or 2025 expense depends on materiality, which is yours to set. Going forward, the monthly proposal is DR lease expense 9,556.44; CR lease liability (interest), CR ROU (plug); payment DR lease liability / CR cash.

### Disclosure data (warehouse, at 30 Sep 2025)

Undiscounted maturity: Oct–Dec 2025 **27,810.00**; 2026 **114,577.20**; 2027 **118,014.48**; 2028 **121,554.96**; total **381,956.64**, less imputed interest 34,506.04 = **347,450.60**. Weighted-average remaining term **3.25 years**; rate **6.0%**. Short-term lease expense (printer) 1,260 YTD. Cash paid for leases: 81,000 per ledger (not 83,430 per contract). **The 347,451 liability is debt under many covenant definitions** — check the term-loan covenant.

## (d) What was not done, and why

- **Classification tests 3–4:** no fair value or economic life. **Renewal judgement:** yours; excluded until you decide.
- **Recurring-payment search:** no vendor payment history. **2024 tie:** no 2024 P&L; 108,000 is an assumption, labelled.
- Excel workbook `Lease_Accounting_2025_Northbrook Trading Ltd.xlsx`: not created — say yes if you want it.
- **`lease_terms_final.csv`:** rejected (shift roster). **Nothing was posted, recognised or changed.**

## (e) Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, 30 Sep 2025, USD, ASC 842 lessee — user-asserted. Source: upload (no Mosofin connection). 3 files accepted with a limit; `lease_terms_final.csv` rejected (shift roster) |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 0 done (uploads); 0b Test 1 done (rent, no ROU), Test 2 not done (no payment listing), Test 3 done (printer); 1 done with a limit (terms only); 2 done (renewal excluded, your judgement); 3 done (6.0%, user-supplied); 4 provisional (operating); 5–7 done; 8 escalation surfaced; 9 done; 10 done; 11 tables in chat; 12 not offered until results approved |
| Not done | Vendor recurring-payment search (payment listing); 2024 rent tie (2024 P&L); classification tests 3–4 (fair value, economic life) |

**Data sources:** user uploads — `lease_terms.md`, `trial_balance_2025-09-30.csv`, `profit_and_loss_2025_ytd.csv`.
