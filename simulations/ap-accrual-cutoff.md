# AP accrual cutoff — Northbrook Trading Ltd, September 2025

Mosofin is not connected, so this run is manual: every step is `[manual]`, on the files you uploaded. (Connecting Mosofin would automate the PO, bill and ledger reads — docs.mosofin.com. Not raised again.)

## (a) Read-back

- **Entity:** Northbrook Trading Ltd (user-asserted). **Period:** September 2025, cutoff 2025-09-30. **Currency:** USD. **Data source:** upload only.
- **Not answered at intake — defaults applied:**
  - Materiality: none given. Per the skill, **everything identified is accrued**.
  - Tax jurisdiction / input-tax rule: not given. The skill's conservative default applies: accrue the expense **gross of recoverable tax**, no input-tax line.
  - Subsequent-event window: not given. The skill's common answer is "up to the date the books close" — but no bills dated after 30 Sep were uploaded, so Step 3 cannot run.
  - Accrued-liability and expense accounts: no chart of accounts uploaded. I have not invented account names; they are left for you to name.

## (b) Validation of the uploaded files (before any work)

| File | What it actually is | Right company / period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `purchase_orders.csv` | 5 purchase orders: po, vendor, item, qty, unit_price, approver, date | No entity/currency in file; dated Aug-Sep 2025 | Yes | Step 1 (GRNI unit prices) | **Accepted with a limit:** company user-asserted. PO-1044 is missing from the sequence |
| `goods_receipts.csv` | 3 goods-receipt notes (GRN-771, 772, 774) against POs | No entity; dated 4-10 Sep 2025 | Yes | Step 1 (received quantities) | **Accepted with a limit:** GRN-773 is missing from the sequence; services have no receipt record |
| `open_bills_2025-09-30.csv` | 12 open A/P bills, total 255,264, dated 3-25 Sep 2025, with PO link where one exists | No entity; dates in period | Yes; no service-period column | Step 1 (net invoiced), Step 2 (recurring vendor billed?) | **Accepted with a limit:** in-period bills only, no post-period bills; service periods not stated |
| `accrual_candidates_2025-09.csv` | 3 services received and not billed, with your estimate and evidence (11,850) | No entity; 26-30 Sep 2025 | Yes | Step 2 (recurring / service accruals) | **Accepted with a limit:** every amount is your estimate, not an invoice |
| `open_bills_2025-09-30_final.csv` | **Not an A/P listing.** Columns employee, week_1..week_4 with values nights/days/off for E08-E10 — a staff shift rota | No company, period or amounts | No | No step uses it | **Rejected** on content, despite the name. If a later bills listing exists, upload that |

**Still missing:** bills dated 1 Oct onwards (subsequent-invoice review, Step 3); the chart of accounts (accrued-liability and expense accounts); the 30 Sep trial balance (accrued-liability balance carried in); last month's accrual JEs (reversal check); an explanation of the gaps GRN-773 and PO-1044.

I would stop here and wait for your answer. *(Assumed answer: "go ahead with the accepted files".)*

## (c) Findings

### Step 1 — GRNI (goods received, not invoiced) from POs: nil to accrue

| PO | Vendor | PO value | Received (GRN) | Received value | Billed | Net to accrue | Note |
|---|---|---|---|---|---|---|---|
| PO-1040 | Kestrel Supplies | 4,000 x 21.7542 = 87,016.80 | 4,000 (GRN-771) | 87,016.80 | 88,583.00 (#4502) | 0 | **Billed 1,566.20 (1.80%) over PO price** — 22.1458/unit vs 21.7542 |
| PO-1041 | Orchard Packaging | 100 x 416.87 = 41,687.00 | **90** (GRN-772) | 37,518.30 | 41,687.00 (INV-4573) | 0 | **Billed for 10 units not received: 4,168.70** |
| PO-1042 | Summit Freight | 23,449.00 | no receipt record | — | 23,449.00 (INV-4644) | 0 | **PO has no approver and no approval date** |
| PO-1043 | Brightline IT | 6 x 2,171.17 = 13,027.02 | 6 (GRN-774, 10 Sep) | 13,027.02 | 13,027.00 (#4715, 9 Sep) | 0 | **PO approved 12 Sep, after the bill and the receipt** |
| PO-1045 | M. Okafor Consulting | 7,816.00 | no receipt record (service) | — | 7,816.00 (INV-4857) | 0 | Service; billed in full |

Every received PO line is fully billed (PO links are taken from the bill's `po` column, so these matches are **linked**, not inferred). Nothing is GRNI. The two exceptions run the other way — **invoiced but not received** — and are not accruals: hold them for the three-way match before payment.

### Step 2 — Service and recurring-vendor accruals: 11,850 proposed, two with a double-count risk

| Vendor | Service | Basis | Amount | Already billed in September? | Treatment |
|---|---|---|---|---|---|
| Summit Freight | Freight, last week of Sep | delivery log | 5,800 | **Yes, possibly:** PO-1042 "Freight, September" billed 23,449 on 7 Sep | Accrue only if PO-1042 did **not** cover the whole month. Shown both ways below |
| Greyfriars Legal LLP | Contract review, Sep (work 26 Sep) | engagement letter rate | 4,200 | INV-4999, 15,633 on 17 Sep — dated before this work | Accrue (inferred: a bill dated 17 Sep cannot cover 26 Sep work) |
| Northgate Utilities | Electricity, Sep | prior three months' average | 1,850 | Bill 5141, 13,027 on 21 Sep — service period not stated | Accrue, but **flag**: a 13,027 bill against a 1,850 monthly average is a 7x variance. Confirm what bill 5141 covers |

| Scenario | Accrual total |
|---|---|
| PO-1042 covers only part of September (accrue all three) | **11,850** |
| PO-1042 covers all September freight (drop Summit 5,800) | **6,050** |

The 13,027 on bill 5141 is also exactly the amount of Brightline bill 4715 — worth checking it was keyed correctly.

### Step 3 — Subsequent invoices: not run

No bills dated after 30 Sep were uploaded. In-period bills with no service period (all 12) cannot be tested for straddling the cutoff.

### Other A/P exceptions found while matching

1. **Likely duplicate bill — 6,480.** Kestrel Supplies INV-4471 (5 Sep) and "Kestrel Supplies Inc." INV4471 (6 Sep): same amount, same invoice number once punctuation is removed, vendor name variant. Open A/P is overstated by 6,480 if both stand. Do not pay twice; the correction is yours to make in the books.
2. **Numbering gaps:** GRN-773 and PO-1044 are missing. An unrecorded receipt is exactly what GRNI looks for — please confirm whether either exists.

### Step 4-5 — Proposed entries — PROPOSED, NOT POSTED (gross, no input-tax line)

| JE | Dr | Cr | Amount | Memo |
|---|---|---|---|---|
| A-1 | Freight expense (account to name) | Accrued liabilities (account to name) | 5,800 | Accrue Summit Freight, last week Sep 2025 — invoice expected Oct. **Only if PO-1042 did not cover it** |
| A-2 | Legal / professional fees (to name) | Accrued liabilities | 4,200 | Accrue Greyfriars Legal contract review, Sep 2025 — invoice expected Oct |
| A-3 | Utilities (to name) | Accrued liabilities | 1,850 | Accrue Northgate electricity, Sep 2025 — invoice expected Oct |

**Reversals dated 2025-10-01:** Dr Accrued liabilities / Cr the same expense, for each of A-1 to A-3.

### Step 6 — Materiality: none set; all items accrued; nothing excluded (cumulative excluded: 0).

## (d) What was not done, and why

- **Subsequent-invoice review** (Step 3): no post-period bills.
- **Prior-period reversal check / creeping balance**: no TB or prior accrual JEs.
- **Variance against prior months by vendor**: no spend history; only the utility average you supplied.
- **Bills sitting unposted in an approval queue**: cannot be seen; the schedule assumes the queue is clear.
- **Real account names**: no chart of accounts — every account above is to be named by you.
- **Excel workpaper** `AP_Accruals_2025-09_Cutoff.xlsx`: not created — say yes if you want it.
- **Nothing was posted, sent, paid or changed.** Every entry is a draft for you to enter yourself.

## (e) Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, Sep 2025, USD — user-asserted. Source: upload. 4 files accepted with a limit; `open_bills_2025-09-30_final.csv` rejected (shift rota) |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 0 done with a limit; 1 done (5 POs, receipt evidence per line: GRN or none); 2 done with a limit (double-count risk on freight, variance on utilities); 3 **not done** (no post-period bills); 4 done (gross default); 5 done (drafts + reversals); 6 done (no threshold); 7 tables in chat |
| Not done | Subsequent invoices (bills from 1 Oct); reversal check (Aug accrual JEs + TB); vendor variance (12 months' spend by vendor) |

**Data sources:** user uploads — `purchase_orders.csv`, `goods_receipts.csv`, `open_bills_2025-09-30.csv`, `accrual_candidates_2025-09.csv`.
