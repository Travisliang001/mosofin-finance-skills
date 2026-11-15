# Prepaid amortization schedule — Northbrook Trading Ltd, September 2025

Mosofin is not connected, so this run is manual: every step is `[manual]`, on the files you uploaded. (Connecting Mosofin would automate the ledger reads — docs.mosofin.com. Not raised again.)

## (a) Read-back

- **Entity:** Northbrook Trading Ltd (user-asserted, not confirmed against a connection)
- **Period:** September 2025, as at 2025-09-30. **Currency:** USD.
- **Data source:** upload only.
- **Not answered at intake, so defaults applied and recorded:**
  - Prepaid account: taken from the uploaded trial balance — 1300 Prepaid Expenses (the only prepaid account in it).
  - Materiality threshold: none stated. None applied; every listed item is scheduled. Recorded as "not set".
  - Convention (whole-month or daily): not stated. The skill's default method, straight-line whole months, is used for every item. The daily-proration result is shown once for comparison.
  - Recoverable tax policy: not stated. Amounts are taken as given; no tax split can be tested without the bills.

## (b) Validation of the uploaded files (before any work)

| File | What it actually is | Right company / period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `trial_balance_2025-09-30.csv` | Trial balance, 29 accounts, columns account / name / debit / credit | No entity name inside the file; date only in the file name (2025-09-30); no currency stated. Accepted on your assertion. | Yes. Debits 6,589,681 = credits 6,589,681. Carries 1300 Prepaid Expenses 18,000 Dr. | Yes — Step 8 GL leg and chart of accounts | **Accepted with a limit**: it is a closing balance only. No opening balance, no movement on 1300, so Step 0 tests and the roll-forward cannot be run. |
| `prepaid_schedule.csv` | List of four prepaid items: item, vendor, paid_on, amount, covers_from, covers_to | No entity or currency in the file; coverage dates span the period. Accepted on your assertion. | Yes. Four rows, amounts total 40,500. No invoice reference, no expense account, no tax column. | Yes — Steps 3-5, 7, 8 (schedule leg) | **Accepted with a limit**: expense account per item and invoice reference are missing; tax treatment cannot be tested. |
| `prepaid_schedule_final.csv` | **Not a prepaid schedule.** Columns are employee, week_1..week_4 with values nights / days / off for E08-E10 — a staff shift rota. | No company, no period, no amounts. | Not for this skill — no vendor, amount or coverage date. | No step uses it. | **Rejected** on content, despite the name. Set aside, not read into the work. If a later version of the prepaid schedule exists, upload that file. |

**Still missing:** transaction detail of account 1300 (ideally 24 months) or at least the opening balance at 2025-08-31; the bills / contracts behind the four items; the expense account for each item.

I would stop here and wait for your answer. *(Assumed answer: "go ahead with the accepted files".)* What follows is therefore a schedule and a one-date tie-out, not a roll-forward.

## (c) Findings

### Schedule (straight-line, whole months; source of every date and amount: user upload)

| Item | Vendor | Paid | Amount | Coverage | Months | Monthly | Used to 30 Sep | Remaining 30 Sep |
|---|---|---|---|---|---|---|---|---|
| Insurance | Calder Mutual | 2025-01-02 | 18,000 | 2025-01-01 to 2025-12-31 | 12 | 1,500 | 9 = 13,500 | 4,500 |
| Software licence | Pinecrest Software | 2025-07-01 | 12,000 | 2025-07-01 to 2026-06-30 | 12 | 1,000 | 3 = 3,000 | 9,000 |
| Trade show deposit | ExpoWest | 2025-08-15 | 4,500 | 2025-11-10 to 2025-11-12 | event | — | 0 | 4,500 |
| Maintenance contract | Orchard Packaging | 2024-10-01 | 6,000 | 2024-10-01 to 2025-09-30 | 12 | 500 | 12 = 6,000 | 0 |
| **Total** | | | **40,500** | | | | 22,500 | **18,000** |

Checks on each item: monthly x months = total; closing balance after last period = 0; no rounding residue (all divide evenly).

### Tie-out at 2025-09-30

| | USD |
|---|---|
| GL 1300 Prepaid Expenses (trial balance) | 18,000 |
| Sum of remaining balances on the schedule | 18,000 |
| **Variance** | **0** |

The balance agrees to the schedule at this date. This is a schedule-to-GL agreement at one date, not a roll-forward: legs 1 and 2 of the three-way test (opening + movement) could not be run.
On daily proration the remaining balances would be 4,536.99 + 8,975.34 + 4,500 = 18,012.33, a 12.33 variance — a convention difference, not an error. Whole-month ties exactly, which suggests whole-month is what the books follow.

### Items needing attention

1. **Maintenance contract (Orchard Packaging, 6,000) expired on 2025-09-30.** Its balance is nil after September's 500. September is the last amortization month; nothing should carry into October. No renewal is on the list — either the service was cancelled or a renewal invoice has not been captured. Please confirm which.
2. **Trade show deposit (ExpoWest, 4,500) is not amortized.** It covers 10-12 November 2025, so nothing is used at 30 September and the whole 4,500 falls into November (not spread from the August payment date). It is called a "deposit": if it is refundable it is not a prepaid at all and belongs in Deposits; if it is applied to the event fee it is a prepaid released in November. The agreement decides — not seen.
3. **Insurance: paid 2025-01-02, coverage from 2025-01-01.** Amortization runs from the coverage start, not the payment date. 4,500 remains, ending December 2025.
4. **Software licence runs to 2026-06-30.** All 9,000 is within twelve months of the balance date, so all current; no non-current split is needed.
5. **The chart in the trial balance has no Insurance or Repairs/Maintenance expense account.** Only 6300 Software is an obvious match. The expense account for insurance and maintenance must be confirmed by you; I have not guessed one.

### Proposed September 2025 entry — PROPOSED, NOT POSTED

| | Dr | Cr |
|---|---|---|
| Insurance expense (account to be confirmed) | 1,500 | |
| 6300 Software | 1,000 | |
| Maintenance expense (account to be confirmed) | 500 | |
| 1300 Prepaid Expenses | | 3,000 |

Memo: Monthly prepaid amortization — September 2025. Because the 18,000 GL balance already equals the post-September schedule, the books appear to already include this entry; do not enter it again without checking the September movement on 1300.

Forward view (whole-month): October 2,500 (insurance 1,500 + software 1,000); November 2,500 + 4,500 trade show = 7,000; December 2,500; from January 2026, 1,000 a month to June 2026.

## (d) What was not done, and why

- **Step 0 ledger tests** (does the account come down, credit pattern, odd items, balance vs 12 months of additions): not run — no transaction detail for 1300.
- **Roll-forward** (opening + additions − amortization = closing): not run — no opening balance or movement. Only a closing tie-out is given.
- **Lumpiness scan for prepaids never set up:** not run — no expense ledger detail; the trial balance holds year-to-date totals only.
- **Recoverable tax test** (gross vs net in the asset): not run — no bills.
- **Coverage dates** are as supplied on the list; not checked to contracts or policy schedules.
- **Substance of the ExpoWest "deposit"** and the status of the Orchard Packaging renewal: your decision.
- **Materiality threshold:** not set; none applied.
- **Excel workpaper** (`Prepaid_Schedule_2025-09.xlsx`): not created — say yes if you want it.
- **Nothing was posted, sent or changed.** Every entry above is a draft for you to review and enter yourself.

Parameters used: account 1300; straight-line whole-month; no materiality threshold; tax as given; rounding to last period (none arose).
