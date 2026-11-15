# Debt and covenants — Northbrook Trading Ltd — test date 30 September 2025 (TTM)

Mosofin is not connected, so this run is manual: every step is `[manual]` and every figure comes from your uploads. Connecting Mosofin would read the debt accounts, ledger and P&L directly ([docs.mosofin.com](https://docs.mosofin.com)).

## Read-back

Tracking debt and covenants for **Northbrook Trading Ltd** at **30 September 2025**, tested on the **trailing twelve months (October 2024 – September 2025)**, **USD**, from **your uploads** (all user-asserted). **Borrowing group: Northbrook Trading Ltd alone** (your answer). One facility: the **Calder Bank term loan**, with covenant definitions supplied in a **summary of terms** (facts arriving inside a file; used once you confirm them here). **No forecast, certificate format or waivers supplied**, so this is the **current position only, with no projection** (the skill's default for question F). Go-ahead assumed.

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Needed for | Verdict |
|---|---|---|---|---|---|
| `term_loan_agreement_summary.md` | **Summary of terms** for the Calder Bank term loan: principal 580,000, 5,000/month + interest, fixed 5.7%, maturity 31 Dec 2029, two covenants with definitions, certificate 45 days after quarter end. Not the agreement | No borrower named; no currency | Yes, but definitions are paraphrased | Steps 1–5, 8 | **Accepted with a limit**: a summary — every term and definition is **user-supplied, not evidenced**; the agreement's verbatim wording, cure rights, cross-default and other covenants are not covered |
| `monthly_profit_and_loss_36m.csv` | Monthly P&L, Oct 2022 – Sep 2025, 36 rows; every month's net income foots to its lines | No entity or currency | Yes; TTM rows Oct 2024 – Sep 2025 present | Steps 4–5 (EBITDA, interest) | **Accepted with a limit**: company user-asserted |
| `term_loan_ledger_2025.csv` | Term-loan ledger movements, Jan – Sep 2025, 27 lines: 9 × principal 5,000, interest charged 1,900, interest paid 1,900 | No entity; **no opening or closing balance**; Oct – Dec 2024 absent | Yes for 2025 movements | Step 2 (actual vs scheduled), Step 1 (effective rate) | **Accepted with a limit**: company user-asserted; historic amortisation covers Jan – Sep 2025 only |
| `trial_balance_2025-09-30.csv` | Trial balance at 30 Sep 2025, 29 accounts; debits = credits = 6,589,681; P&L lines are **YTD Jan – Sep 2025** and agree to the monthly P&L to the dollar (revenue 4,038,600; interest 17,100) | No entity or currency named | Yes | Step 0b sweep, Total Debt | **Accepted with a limit**: company user-asserted |
| `term_loan_agreement_summary_final.csv` | **An employee shift rota** (E08–E10, weeks 1–4). Not a loan agreement, despite its name | None | n/a | No step uses it | **Rejected.** If a final or amended agreement exists, upload it instead |

**Still missing:** the **signed loan agreement** (or its definitions and covenant clauses verbatim) — required to move from "computed on the summary" to "computed on the agreement"; **forecast, certificate format, any waivers** (recommended; without them, no projection); **lease agreements** for the office (see the sweep); ledger for **Oct – Dec 2024**. Would wait here; proceeding on the accepted files.

## Debt schedule (facility inventory)

| Field | Value | Source |
|---|---|---|
| Facility / lender | Term loan, Calder Bank | summary (supplied) |
| Original principal / balance 30 Sep 2025 | 580,000 / **220,000** | summary / TB 2500 |
| Rate (stated) / **effective rate borne** | fixed 5.7% / **9.3%** (17,100 for 9 months, annualised 22,800, over average balance 245,000) | summary / ledger |
| Repayment / maturity | 5,000 a month + interest / 31 Dec 2029 | summary |
| Security, fees, prepayment terms | **not supplied** | — |

**Interest does not match the stated rate.** At 5.7% on the reducing balance (265,000 in January to 225,000 in September), Jan – Sep 2025 interest would be **10,473.75**; the ledger charges **17,100** (1,900 every month), **6,626.25 more**. 1,900 a month is 5.7% on **400,000**, and it has not moved in 36 months although principal fell 5,000 a month. Either fees are being charged as interest, the rate is not 5.7%, or interest is being booked as a fixed accrual rather than from the lender's statement. **Please check against the Calder Bank statement** before relying on the interest figures.

**Amortisation, actual vs scheduled (Jan – Sep 2025):** 9 principal repayments of 5,000 = 45,000, as scheduled; implied opening balance 265,000, closing 220,000 (agrees to TB). Interest paid equals interest charged each month. **Schedule vs maturity:** 220,000 ÷ 5,000 = 44 payments, so the loan is fully repaid at **31 May 2029**, seven months before the stated 31 Dec 2029 maturity — the summary's terms do not reconcile; please confirm.

## Debt-like item sweep (Step 0b) — run on the trial balance

| Item | Amount | On inventory? | In "Total Debt" per summary? | Effect |
|---|---:|---|---|---|
| 2500 Term Loan | 220,000 | Yes | Yes | included |
| 2050 Corporate Card Payable | 7,300 | No | **Yes** (named in definition) | included |
| Lease liabilities | **none on TB** | — | **Yes** ("any lease liabilities") | Rent of 9,000 a month (108,000 TTM) is expensed with **no lease liability recorded**. If the office lease runs over 12 months, a liability is missing from the books and belongs in Total Debt. Not quantifiable without the lease |
| 2300 Intercompany Payable – Northbrook UK | 38,000 | No | **Not named** — please confirm | If included, Total Debt 265,300, leverage 0.33x: no change to the conclusion |
| Overdraft | none (bank 1,230,316 debit) | — | — | — |

Also noted: an intercompany balance with **Northbrook UK** means a related company exists outside the stated borrowing group — please confirm it is outside the perimeter.

## Covenant compliance — 30 September 2025, TTM (computed on the summary's definitions)

**Covenant EBITDA bridge**

| Component | TTM |
|---|---:|
| Net income (book) | 739,050 |
| + Interest | 22,800 |
| + Depreciation | 50,400 |
| = Book EBITDA | **812,250** |
| + One-time professional fees (cap 15,000) | **0 as computed / 14,000 if confirmed** — June 2025 fees 16,500 against a 2,500 run-rate; not evidenced as one-time |
| − Gain on asset sales | 0 (none in the P&L or TB) |
| **= Covenant EBITDA** | **812,250** (826,250 if the addback is confirmed) |

| Covenant | Numerator | Denominator | Ratio | Limit | Headroom | EBITDA fall before breach | Status |
|---|---:|---:|---:|---:|---:|---:|---|
| Leverage: Total Debt / Covenant EBITDA | 227,300 | 812,250 | **0.28x** | ≤ 2.50x | 2.22 turns | **721,330** (to 90,920) | In compliance |
| Interest cover: Covenant EBITDA / Interest | 812,250 | 22,800 | **35.6x** | ≥ 4.0x | 31.6x | **721,050** (to 91,200) | In compliance |

With the 14,000 addback: 0.28x and 36.2x. **The conclusion is the same under either answer.** Total Debt could rise by 1,803,325 (to 2,030,625) before leverage breaches, so neither an unrecorded office lease nor the intercompany balance plausibly changes it.

Earnings quality notes (no definitional effect): COGS stepped up from 58% to 60% of revenue from July 2025; September marketing 29,146 is 6.4% of revenue against a steady 4.0% (≈10,930 above run-rate). Covenant EBITDA rose from 665,649 in the prior TTM to 812,250.

**This is a computation for an authorised officer to review and sign; it is not a certification.** Definitions came from a summary, so the result stands only once checked against the agreement.

## Maturity profile and compliance calendar

| Period | Scheduled principal |
|---|---:|
| Oct – Dec 2025 | 15,000 |
| 2026 / 2027 / 2028 | 60,000 each |
| Jan – May 2029 | 25,000 |
| **Total** | **220,000** |

Current portion (next 12 months): **60,000** — should be presented as current, not long-term. Single lender. **Q3 certificate due 14 November 2025** (30 Sep + 45 days); next, Q4, due 14 February 2026. Breach / waiver log: none reported.

## Not done, and why

- **Projection (Step 6)** — no forecast supplied. **Cure rights, cross-default, other covenants (Steps 3, 9)** — not in the summary.
- **Amortisation Oct – Dec 2024**, opening-balance tie — no ledger for those months.
- **Lease liability** — no lease supplied. **Workpaper file** — would ask first (`Debt_Covenant_2025-09_Northbrook Trading Ltd.xlsx`).

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, 30 Sep 2025, TTM, USD — **user-asserted**; perimeter Northbrook Trading Ltd alone. Data source: **upload**. Summary, P&L, ledger, TB accepted with limits; `term_loan_agreement_summary_final.csv` **rejected** (shift rota) |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps 0, 0b | Done; sweep found the card balance, the intercompany payable and an absent lease liability |
| Steps 1–2 | Done with a limit: terms from summary; history Jan – Sep 2025 only; interest anomaly flagged |
| Steps 3–5 | Done with a limit: two covenants computed on **summarised** definitions |
| Step 6 | **Not done**: no forecast |
| Steps 7–8 | Done: maturity profile, calendar |
| Step 9 | Not applicable: no breach |
| Step 10 | Done in chat |
| Not done | Agreement wording, lender statement tie, lease liability, Oct – Dec 2024 movements |

Nothing was posted, filed or sent to the lender. **Data sources:** upload — `term_loan_agreement_summary.md`, `monthly_profit_and_loss_36m.csv`, `term_loan_ledger_2025.csv`, `trial_balance_2025-09-30.csv`.
