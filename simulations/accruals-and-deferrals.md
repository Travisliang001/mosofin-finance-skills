# Accruals and deferrals — Northbrook Trading Ltd, September 2025

Mosofin is not connected, so this run is manual: every step is `[manual]`, on the files you uploaded. (Connecting Mosofin would automate the ledger reads — docs.mosofin.com. Not raised again.)

## (a) Read-back

- **Entity:** Northbrook Trading Ltd (user-asserted). **Period:** 1-30 September 2025, as at 2025-09-30. **Currency:** USD. **Data source:** upload only.
- **Not answered at intake — defaults and assumptions applied:**
  - Categories in scope: not stated. Taken from what the files show: service/utility and professional-fee accruals (candidate list), payroll and interest accruals already booked, revenue and deferral items visible in the ledger.
  - Materiality: not stated. Per the skill, none applied; every item found is accrued.
  - Reversal policy: not stated. Reversals are drafted for 2025-10-01 (the skill's standard pattern). If your incoming invoices post straight against 2100, drop Sheet 4; the September amounts do not change.
  - Reporting framework and tax jurisdiction: not stated; no conclusion below depends on them. Amounts are taken as net of tax.

## (b) Validation of the uploaded files (before any work)

| File | What it actually is | Right company / period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `accrual_candidates_2025-09.csv` | List of 3 unbilled services: vendor, description, received_on, estimated_amount, evidence | No entity/currency in file; dates 26-30 Sep 2025 | Yes; 3 rows, total 11,850 | Steps 1, 3, 4 | **Accepted with a limit:** company user-asserted; every amount is your estimate, not an invoice |
| `general_ledger_2025-09.csv` | Ledger extract: 15 bank-feed lines (bank leg only) and 7 journal entries (JE-0901 to 0907) | No entity in file; dates 2025-09-02 to 09-30, plus JE-0905 dated **2025-08-31** | Each JE balances; bank lines are one-sided (Dr 179,979 / Cr 196,305), so the other leg of each payment is not shown | Steps 5, 6 (what is booked in 2100) | **Accepted with a limit:** no opening balances and no offset legs for bank lines, so 2100 cannot be fully rolled forward |
| `prepaid_schedule.csv` | Schedule of 4 prepaid items (40,500) with coverage dates | No entity/currency in file | Yes | Step 2 (deferred-expense category, cross-check only) | **Accepted with a limit:** prepaid amortisation itself belongs to `prepaid-amortization-schedule` |
| `trial_balance_2025-09-30.csv` | Trial balance, 29 accounts | No entity in file; date only in file name | Foots: 6,589,681 = 6,589,681 | Steps 4, 6 (2100 closing balance, account names) | **Accepted with a limit:** company and period user-asserted |
| `trial_balance_september.csv` | Trial balance, 29 accounts, foots 5,389,421 | **Not September 2025.** Against the accepted TB: accumulated depreciation 260,800 vs 311,200 (50,400 = 12 x the 4,200 monthly charge in JE-0901); term loan 280,000 vs 220,000 (60,000 = 12 x 5,000 principal); retained earnings 789,221 vs 1,422,317 | — | No step needs a second TB for the same date | **Rejected:** its content is a year earlier (looks like September 2024). Not used. If you meant to give me the prior month, upload the **31 August 2025** TB instead |

**Still missing (required or improving):** the 31 Aug 2025 trial balance or 2100 opening detail (roll-forward); the term-loan agreement (rate, day count, interest period); the payroll calendar (accrued wages); support for JE-0904 and JE-0907; the Tideswell Hotels deposit terms; October bills received to date (to confirm the candidates are not already invoiced).

I would stop here and wait for your answer. *(Assumed answer: "go ahead with the accepted files".)*

## (c) Findings

### 1. New accruals to propose — 11,850 (from your candidate list)

| Vendor | Service | Basis (your evidence) | Amount | Account |
|---|---|---|---|---|
| Summit Freight | Freight, last week of Sep | delivery log | 5,800 | Freight — **no freight account in the TB; please name one** (5000 COGS if freight-in) |
| Greyfriars Legal LLP | Contract review, Sep | engagement letter rate | 4,200 | 6400 Professional Fees |
| Northgate Utilities | Electricity, Sep | prior three months' average | 1,850 | Utilities — **no utilities account in the TB; please name one** |
| **Total** | | | **11,850** | Cr 2100 Accrued Liabilities |

None of the three appears in the September ledger. The utility figure is a run-rate estimate (least reliable basis). Freight is close to a goods-received cutoff item; if it relates to inventory receipts it belongs in `ap-accrual-cutoff` instead — do not book it twice.

### 2. Accruals already booked in September that do not hold up

| JE | Entry | Issue |
|---|---|---|
| **JE-0904**, 28 Sep (a Sunday) | Dr 1100 AR 50,000 / Cr 4000 Sales 50,000, "Revenue adjustment" | Round, no customer, no invoice, posted to AR not to an unbilled-receivable account. A revenue accrual needs a basis (hours, milestone, contract). **Unsupported — 50,000 of September revenue rests on it.** Draft correction if no support: Dr 4000 / Cr 1100 50,000. |
| **JE-0907**, 30 Sep | Dr 6200 Marketing 9,999 / Cr 2100 9,999, **no memo** | No vendor, no basis, amount just under 10,000. Unsupported accrual. Draft correction if no support: Dr 2100 / Cr 6200 9,999. |
| **JE-0905**, dated **31 Aug** | Dr 6400 3,800 / Cr 2100 3,800, "Legal fee missed in August" | Back-dated into August inside the September extract. If August is closed, book it in September as a prior-period true-up instead of changing August. |
| **JE-0906**, 30 Sep | Dr 7000 Interest 1,900 / Cr 2100 1,900 | A full month of interest, but the loan was paid on **22 Sep** (6,900 = 5,000 principal + 1,900 interest on the year-on-year principal movement). If that payment covered interest to 22 Sep, only 23-30 Sep should be accrued: 220,000 x 10.13% (implied from 1,900 x 12 / 225,000) x 8/365 = **≈ 489**, an overstatement of ≈ 1,411. If the 22 Sep payment settles the prior month's interest, 1,900 is right. **The loan agreement decides — shown both ways, not concluded.** |
| **JE-0903**, 30 Sep | Dr 6000 Payroll 8,400 / Cr 2100 8,400, "Accrued wages" | No computation given. Payroll of 52,310 is paid fortnightly on Fridays (12 and 26 Sep). If pay date = period end, 29-30 Sep are 2 of 10 working days: 52,310 x 2/10 = 10,462 (on net pay). The 8,400 cannot be recomputed without the pay calendar and gross pay. Note also CHECK 2287 on 3 Sep for exactly 8,400 — please confirm whether that was August's wage accrual being paid. |

### 3. Roll-forward of 2100 Accrued Liabilities — incomplete

| | USD |
|---|---|
| Closing balance per TB | 28,800 |
| Credits in the September extract (JE-0903, 0905, 0906, 0907) | 24,099 |
| Debits in the extract (reversals / settlements of August accruals) | **0** |
| Implied opening (or unexplained remainder) | 4,701 |

No August accrual was reversed or settled in this extract. With no opening balance, I cannot say whether last month's accruals are still sitting in 2100 (the compounding problem). After the three new accruals, 2100 would be 40,650 — or 30,651 if JE-0907 is removed.

### 4. Deferrals

- **Possible deferred revenue — Tideswell Hotels, 12,400**, received 30 Sep, described as a "Deposit". If this is a customer payment in advance of service, it is deferred revenue, not revenue. The TB has **no deferred revenue account**. Need the terms before an entry.
- **Prepaids (cross-check only):** the September ledger releases only 1,500 (insurance, JE-0902) from 1300, while the schedule implies 3,000 (insurance 1,500 + software 1,000 + maintenance 500). Yet 1300 = 18,000 equals the schedule's post-September balance. One of the two is incomplete. JE-0902 also posts to **6150 Insurance, which is not in the TB**. Hand to `prepaid-amortization-schedule`.

### Proposed September entries — PROPOSED, NOT POSTED

| JE | Dr | Cr | Amount | Memo |
|---|---|---|---|---|
| P-1 | Freight (account to confirm) | 2100 Accrued Liabilities | 5,800 | Accrue Summit Freight — Sep 2025 |
| P-2 | 6400 Professional Fees | 2100 Accrued Liabilities | 4,200 | Accrue Greyfriars Legal — Sep 2025 |
| P-3 | Utilities (account to confirm) | 2100 Accrued Liabilities | 1,850 | Accrue Northgate electricity — Sep 2025 |

**Reversals (Sheet 4), dated 2025-10-01:** each of P-1 to P-3 reversed (Dr 2100 / Cr the expense), 11,850 in total. Corrections for JE-0904 and JE-0907 are drafted above, only if no support exists.

## (d) What was not done, and why

- **Full roll-forward of 2100**: not done — no opening balance and no offsetting legs of bank payments.
- **Interest and wage accruals**: not recomputed — no loan agreement, no payroll calendar.
- **Check that the candidates are not already invoiced**: not done — no bills listing.
- **Bonus, commission, vacation, audit-fee accruals**: no data supplied, none proposed; not concluded that none are owed.
- **Tax split, multi-currency**: not applicable on the data given; amounts taken as net USD.
- **Excel workpaper** `Accruals_Deferrals_2025-09.xlsx`: not created — say yes if you want it.
- **Nothing was posted, sent or changed.** Every entry is a draft for you to enter yourself.

## (e) Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, Sep 2025, USD — user-asserted. Source: upload. Files: 4 accepted with a limit, `trial_balance_september.csv` rejected (prior-year content) |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 0 done with a limit (uploads); 1 done (3 candidates + 5 booked items reviewed); 2 done with a limit (deposit flagged, prepaids handed off); 3 done for candidates, not done for interest/wages (terms missing); 4 done (drafts); 5 done (drafted, policy assumed); 6 **not done** (no opening); 7 done — no threshold, all accrued, cumulative excluded 0; 8 tables in chat |
| Not done | 2100 roll-forward (needs 31 Aug TB / 2100 detail); prior-period reversal check (needs August JEs); interest recompute (loan agreement); wage recompute (payroll calendar) |

**Data sources:** user uploads — `accrual_candidates_2025-09.csv`, `general_ledger_2025-09.csv`, `prepaid_schedule.csv`, `trial_balance_2025-09-30.csv`.
