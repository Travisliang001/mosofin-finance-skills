# Debt and covenants: Northbrook Trading Ltd, test date 30 September 2025

Mosofin is not connected, so this run is manual: every figure comes from your uploads. **This is a
computation for an authorised officer to review and sign. Nothing is certified, posted or sent to
the lender.**

## Read-back

> Tracking debt and covenants for **Northbrook Trading Ltd** (USD) at **30 September 2025**, tested
> on the **trailing twelve months** (Oct 2024 - Sep 2025). **Northbrook Trading Ltd alone is the
> borrowing group.** One facility: the **Calder Bank term loan**, with covenant definitions supplied
> in your terms summary. That summary also says the June 2025 professional fees include a
> **one-time 14,000 legal fee**, confirmed by the CFO for add-back. No forecast, certificate format or
> waivers supplied, so the current position only, no projection. Shall I go ahead?

Assumed "yes". The 14,000 add-back and every term below are **user-supplied, not evidenced** (they
come from a summary, not the signed agreement).

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Used by | Verdict |
|---|---|---|---|---|---|
| `term_loan_agreement_summary.md` | Summary of the Calder Bank term loan: principal, rate, repayment, maturity, two covenants with definitions, certificate deadline | No borrower named | Yes, but a summary, not the agreement | Steps 1-5, 8 | **Accepted with a limit**: terms and definitions user-supplied; verbatim covenant wording, events of default, cross-default and negative covenants not available |
| `term_loan_ledger_2025.csv` | Term loan ledger Jan-Sep 2025: principal repaid, interest charged and paid, 27 lines | Not named; 2025 | Yes | Step 2 (actual vs scheduled) | **Accepted with a limit**: company user-asserted; covers 9 of the 12 test months (Oct-Dec 2024 from the P&L) |
| `trial_balance_2025-09-30.csv` | Trial balance at 30 Sep 2025, 33 accounts, foots at 6,546,018 each side; P&L accounts are year to date | Not named | Yes | Steps 0b, 1, 5 | **Accepted with a limit**: company user-asserted |
| `monthly_profit_and_loss_36m.csv` | Monthly P&L Oct 2022 - Sep 2025, every month's net income foots | Not named | Yes | Step 5 (TTM EBITDA, interest) | **Accepted with a limit**: company user-asserted |
| `term_loan_agreement_summary_final.csv` | **An employee shift roster** (employee, week_1-4: days / nights / off) | n/a | n/a | No step | **Rejected** on content, despite its name. If a later loan summary was meant, please upload it. |

Still missing: the **signed loan agreement** (for verbatim covenants, negative covenants and events
of default), any **lease schedule**, and the lender's certificate format. None blocks the
computation below; each is listed as a limit. I would wait for your answer here.

Tie-outs done: Jan-Sep 2025 of the monthly P&L equals the trial balance's P&L accounts exactly
(revenue 4,038,600; interest 10,474; depreciation 37,800). Ledger interest Jan-Sep sums to 10,474.

## Facility inventory

| Field | Value | Source |
|---|---|---|
| Lender / type | Calder Bank, amortising term loan | supplied |
| Drawn | 565,000 on 1 Jan 2020 | supplied |
| Balance 30 Sep 2025 | **220,000** | TB account 2500; ties to schedule (565,000 - 69 x 5,000) |
| Rate | Fixed 5.70%; **effective rate borne 5.70%** (14,392 TTM interest / 252,500 average balance) | supplied / computed |
| Repayment / maturity | 5,000 a month plus interest; matures 31 May 2029; no balloon | supplied |
| Security, fees, prepayment terms | not supplied | missing |

## Amortisation: actual against scheduled

All nine 2025 repayments were 5,000 on the month end, as scheduled. Interest charged each month
equals opening balance x 5.7% / 12 to the dollar (265,000 -> 1,259 in Jan; 225,000 -> 1,069 in Sep),
and was paid the same day. **No missed, late or extra payments.** Forward: 44 payments of 5,000
take the balance to nil on 31 May 2029, matching the stated maturity.

## Debt-like item sweep (trial balance)

| Item | Amount | On inventory? | In "Total Debt" per summary? | Effect |
|---|---:|---|---|---|
| Corporate Card Payable (2050) | 7,300 | No | **Yes**, named in the definition | Included below |
| Lease liabilities | **none on the TB** | No | **Yes**, "any lease liabilities" | Rent runs 9,000 a month (81,000 YTD) with no lease liability recorded. If this is a lease that should be on the balance sheet (ASC 842), Total Debt is understated. Please supply the lease. |
| Intercompany Payable - Northbrook UK (2300) | 38,000 | No | Not named | If counted, leverage 0.33x. Is it interest-bearing? |
| Overdraft | none (bank 1,006,479 debit) | | | |

## Covenant compliance at 30 September 2025 (TTM Oct 2024 - Sep 2025)

**Covenant EBITDA bridge**

| Component | Amount |
|---|---:|
| Net income (book) | 726,958 |
| + Interest (book) | 14,392 |
| + Depreciation (book) | 50,400 |
| = Book EBITDA | 791,750 |
| + One-time professional fee, June 2025 (cap 15,000 a year; user-supplied, CFO-confirmed; June fees 16,500 vs the usual 2,500) | **14,000** |
| - Gain on asset sales (none in the P&L or TB) | 0 |
| **= Covenant EBITDA** | **805,750** |

**Total Debt** = term loan 220,000 + corporate card 7,300 + leases 0 (none recorded) = **227,300**.

| Covenant | Build | Ratio | Limit | Status | Headroom |
|---|---|---:|---:|---|---|
| Leverage | 227,300 / 805,750 | **0.28x** | ≤ 2.50x | **In compliance** | 2.22 turns; Covenant EBITDA could fall by **714,830 (88.7%)** to 90,920 before breach; or Total Debt could rise by 1,787,075 |
| Interest cover | 805,750 / 14,392 | **55.99x** | ≥ 4.0x | **In compliance** | Covenant EBITDA could fall by **748,182 (92.9%)** to 57,568 before breach |

Neither covenant is close to its limit. The ratios rest on a summary of the agreement; confirm the
definitions against the signed document before an officer signs.

## Maturity profile

| Period | Scheduled principal |
|---|---:|
| Oct-Dec 2025 | 15,000 |
| 2026 | 60,000 |
| 2027 | 60,000 |
| 2028 | 60,000 |
| Jan-May 2029 | 25,000 |

60,000 falls due in the next twelve months; the TB carries the loan in one account, so check it is
split between current and non-current in the financial statements. One lender, small balance: no
refinancing pressure.

## Compliance calendar

Q3 2025 certificate (test date 30 Sep 2025) **due 14 November 2025** (45 days). Missing it can itself
be a default.

## Other observations

- Dividends and adjustments of 67,500 YTD: the summary gives no dividend basket; check the agreement.
- September 2025 shows software 0 (usually 3,500) and marketing 29,146 (usually about 19,000):
  possibly a misposting. It does not change EBITDA, but confirm before the P&L goes to the lender.

## Not done, and why

- Projection and sensitivity (Step 6): no forecast supplied. The debt side is known (above).
- Verbatim covenant register, negative covenants, events of default, cross-default (Steps 3, 9):
  need the signed agreement.
- Breach / waiver log: none supplied; none assumed.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, USD, test date 30 Sep 2025, TTM: **user-asserted**. Perimeter: Northbrook Trading Ltd alone (user-stated; the TB holds an investment in Northbrook UK Ltd, outside it). Source: upload. 4 files accepted with limits; 1 rejected (staff roster). No mock data. |
| Capability map | Not applicable: no connection. Every task is `[manual]`. |
| Steps | 0 Evidence: done. 0b Sweep: done (card included; no leases recorded; intercompany 38,000 queried). 1 Inventory: done with a limit. 2 Amortisation: done (2025 from ledger; Oct-Dec 2024 from P&L). 3-4 Register and definitions: done with a limit (summary only). 5 Ratios: done. 6 Projection: **not done**, no forecast. 7 Maturity: done. 8 Calendar: done. 9 Breach: not applicable. 10 Output: tables here; Excel (`Debt_Covenant_2025-09_Northbrook Trading Ltd.xlsx`) offered, not created. |
| Not done | Ledger for Oct-Dec 2024 (to evidence those repayments); lease schedule; signed agreement. |

Would you like this as an Excel workpaper?

**Data sources:** uploads only: term_loan_agreement_summary.md, term_loan_ledger_2025.csv, trial_balance_2025-09-30.csv, monthly_profit_and_loss_36m.csv.
