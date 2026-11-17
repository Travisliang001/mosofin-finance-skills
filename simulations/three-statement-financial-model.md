# Three-statement model — Northbrook Trading Ltd — 36 months history, 36 months forecast (Oct 2025 – Sep 2028)

Mosofin is not connected, so this run is manual: the history comes from your uploads and every forward figure is your assumption or a labelled placeholder. Nothing is posted anywhere. History and forecast are marked **A** (actual) and **F** (forecast) throughout.

## Read-back

Building a **three-year monthly** model for **Northbrook Trading Ltd** (user-asserted), USD, for **internal planning**, with **36 months of history** (Oct 2022 – Sep 2025) from your uploads. Drivers per `model_assumptions.md`: revenue +8% a year, gross margin 41%, operating costs +4% a year; capex 80,000 in 2026 then equal to depreciation; the term loan on its agreed schedule (5,000 a month, 5.7% fixed); no new equity; tax at a single 20% effective rate (sample); circularity broken with prior-period balances.

| Intake question | Treatment |
|---|---|
| B, C, E, F | Answered by `model_assumptions.md` (used once you confirm it). |
| D — working-capital days | **Not answered.** Measured history shown below; the model holds DSO / DIO / DPO at their trailing-12-month averages **as a placeholder**, not my assumption — please set them. |
| Depreciation life of the 80,000 capex | **Not given.** Never assumed: the 80,000 is capitalised in Jan 2026 and **not depreciated** until you give a life. This overstates profit by 80,000 ÷ life a year. |
| Interest income on cash | Not given; not modelled. |
| Tax payment timing | Not given; tax treated as paid in the month incurred (no tax payable line). |

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Step that uses it | Verdict |
|---|---|---|---|---|---|
| `monthly_profit_and_loss_36m.csv` | Monthly P&L Oct 2022 – Sep 2025, 13 lines; every month foots to net income | No entity named | Yes | Steps 2, 3b, 7 | **Accepted with a limit**: company user-asserted |
| `monthly_balance_sheet_36m.csv` | Condensed monthly BS, same 36 months, 10 lines; **balances in all 36 months** | No entity named | Yes — condensed (no card, payroll or tax lines) | Steps 3, 3b, 5 | **Accepted with a limit**: condensed; cannot be checked line by line to a ledger (no TB supplied) |
| `model_assumptions.md` | Your drivers, capex, debt, tax and circularity choices | — | Yes | Steps 1–8 | **Accepted with a limit**: no working-capital days, capex life or tax timing |
| `term_loan_agreement_summary.md` | Summary of the Calder Bank term loan and its covenants | — | Yes, a summary | Debt schedule, covenant outputs | **Accepted with a limit**: a summary, not the agreement; terms user-supplied |
| `monthly_profit_and_loss_36m_final.csv` | **Not a P&L.** A staff shift rota (E08–E10, weeks 1–4) | n/a | No | None | **Rejected** on content. |

**Still missing:** working-capital day assumptions; useful life for the 2026 capex; the fixed asset register (to separate committed depreciation precisely); the trial balance at 30 Sep 2025 (to verify the history against the ledger); the corporate card balance (part of covenant Total Debt). I would wait for your answer here; proceeding on the accepted files.

## History checks (A)

- BS balances in all 36 months (guaranteed for history — not evidence by itself).
- Net income ties to the P&L lines every month. PP&E rolls by 4,200 depreciation a month; interest = prior-month loan × 5.7% / 12 in every month tested — the loan summary agrees with the books.
- **Retained earnings does not roll from net income in two months:** Mar 2025 **−60,000** and Jun 2025 **−7,500**. Equity movements with no P&L line (a dividend and an unexplained adjustment, judging by size); the model carries them as history, but the 7,500 needs explaining.
- **No tax expense in any of the 36 months**, yet profit is 438,557 (2023) and 614,939 (2024). The forecast's 20% tax charge is therefore a break from history, not a continuation.
- Debt schedule: 220,000 at Sep 2025 ÷ 5,000 = 44 payments → paid off **May 2029**, matching the stated maturity.

## Step 3b — measured drivers (36 months)

| Driver | Range | Median | Last 12 mo | Assumption | Note |
|---|---|---|---|---|---|
| Revenue growth (TTM) | — | — | **+15.4%** (5,136,300 vs 4,451,200) | **+8%** | Deliberate slowdown vs history — visible, your call |
| Gross margin | 40.0% – 42.0% | 42.0% | 41.4% | 41% | Within range |
| DSO (days) | 40.3 – 53.4 | 47.6 | 51.1 | 51.1 placeholder | Trend up |
| DIO (days) | 57.6 – 77.1 | 68.4 | 73.7 | 73.7 placeholder | |
| DPO (days) | 31.7 – 39.3 | 36.1 | 34.3 | 34.3 placeholder | |
| Capex % revenue | n/a — net PP&E only falls by depreciation; no capex in 36 months | | | 80,000 in 2026 | |

## Forecast summary (F), fiscal years to September

| | FY to Sep 2026 | FY to Sep 2027 | FY to Sep 2028 |
|---|---:|---:|---:|
| Revenue | 5,547,204 | 5,990,980 | 6,470,259 |
| Pre-tax income | 818,832 | 948,434 | 1,090,362 |
| Tax at 20% | (163,766) | (189,687) | (218,072) |
| Net income | 655,066 | 758,747 | 872,290 |
| Depreciation (existing assets) | 50,400 | 50,400 | 50,400 |
| Capex | 80,000 | 37,800 | 50,400 |
| Interest (prior-period balance) | 10,972 | 7,552 | 4,132 |
| Closing term loan | 160,000 | 100,000 | 40,000 |
| Closing cash | 1,632,744 | 2,246,546 | 2,953,487 |

Revenue and opex are grown off the same month a year earlier, so the history's seasonality carries forward. **Balance check: zero in all 36 forecast months** (max absolute difference 0.000000002); ending cash from the cash flow = BS cash; NI in the equity roll = IS NI. No revolver: none exists, and cash never approaches zero. No plug.

## Covenants (Calder Bank, trailing twelve months)

Covenant EBITDA = NI + interest + depreciation + one-time professional fees (cap 15,000) − gains on sale. The **14,000 June 2025 legal fee** is added back (June 2025 professional fees 16,500 vs a normal 2,500).

| Test date | Covenant EBITDA | Interest | Term loan | Interest cover (≥ 4.0x) | Leverage (≤ 2.50x) |
|---|---:|---:|---:|---:|---:|
| Sep 2025 (A) | 802,250 | 14,392 | 220,000 | **55.7x** | **0.27x** |
| Sep 2026 (F) | 716,438 | 10,972 | 160,000 | 65.3x | 0.22x |
| Sep 2028 (F) | 926,822 | 4,132 | 40,000 | 224x | 0.04x |

Compliant at every quarter end in history and forecast, with wide headroom. Two caveats: the definition adds back **interest and depreciation but not tax**, so once the 20% tax starts the forecast EBITDA is net of tax (Sep 2026 falls below Sep 2025 for that reason); and **Total Debt includes the corporate card**, which the condensed BS does not show — even 100,000 of card debt would leave Sep 2025 leverage at 0.40x.

## Not done, and why

- Working-capital days, capex life, tax timing — yours to set; placeholders labelled.
- History verified against a ledger — no TB uploaded.
- Scenarios — the measured ranges above are ready for `scenario-and-sensitivity-analysis`; not run.
- Excel workbook — would ask before creating `3Statement_Model_Northbrook_Trading_Ltd_2025-09-30.xlsx`.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, USD (user-asserted); entity-level; 36 months history (Oct 2022 – Sep 2025); horizon 36 months monthly; circularity: prior-period balances. Files: 4 accepted with limits, 1 rejected (staff rota). |
| Capability map | Not applicable: no connection. Every task is `[manual]`. |
| Steps | 1–2 done; 3 done (capex depreciation blocked); 3b done; 4–5 done, balance check 0 every month; 6 prior-period balances; 7 checks done, ledger check **not done**; 8 not run; 9 tables in chat. |
| Unknowns | WC days; capex life; tax timing; card balance; the Mar/Jun 2025 equity movements; no historical tax. |
| Parameters | Growth 8%, GM 41%, opex +4%, tax 20%, loan 5,000/mo at 5.7% — all user-supplied; WC days = trailing-12-month averages (placeholder). |
