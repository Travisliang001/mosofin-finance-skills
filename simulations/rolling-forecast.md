# Rolling forecast refresh — Northbrook Trading Ltd, actuals locked through September 2025

This run is manual: no Mosofin connection. Everything below comes from the files you uploaded.
Nothing has been posted, sent or changed. The forecast is yours; what follows tests it.

## Read-back

Refreshing the **12-month** rolling forecast for **Northbrook Trading Ltd**, **monthly**, in **USD**,
with actuals **locked through September 2025**, window **October 2025 to September 2026**, from
**the 36 months of P&L you uploaded**, against the **2025 budget (January to September only)**. Your
forward projection is the uploaded October 2025 to September 2026 forecast. **No prior forecast**:
this is a first rolling forecast, so there is no change bridge and no accuracy score. FX: none
stated; all figures USD. Company, period and currency are as you stated them; no file names them.

## Validation of the upload (before any work)

| File | What it actually is | Right company and period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `monthly_profit_and_loss_36m.csv` | Monthly P&L, 12 lines plus net income, Oct 2022 to Sep 2025 (36 months, none missing) | No entity or currency in file (user-asserted); ends at the last closed month | Yes. Net income recomputes from the lines in all 36 months | Steps 2, 3b, 5 | **Accepted with a limit**: company and period user-asserted |
| `budget_2025.csv` | Monthly budget, same 12 lines, Jan to Sep 2025 | Yes for 2025; **Oct to Dec 2025 absent** | Yes for 9 months | Step 5 (budget comparison) | **Accepted with a limit**: no full-year 2025 budget, so "will we hit budget?" can be answered for Jan to Sep only |
| `forecast_2025-10_to_2026-09.csv` | A 12-month forecast, same lines, Oct 2025 to Sep 2026 | Covers exactly the new window | Yes | Steps 3b, 4, 5 (your projection) | **Accepted with a limit**: it starts after the last closed month, so it is the projection for this refresh, not a prior forecast. Nothing to score or bridge from |
| `model_assumptions.md` | Three-year planning assumptions: revenue +8% a year, gross margin 41%, opex +4% a year, capex 80,000 in 2026, term loan 5,000 a month at 5.7% | No company named; horizon three years | Yes, as growth rates | Steps 3, 4 (drivers) | **Accepted with a limit**: general model assumptions, not updated drivers (no pipeline, hiring plan or known events). They also contradict the forecast file (see finding 2) |
| `monthly_profit_and_loss_36m_final.csv` | A four-week shift rota for employees E08 to E10 | No company, date or amount | Not for this skill | No step uses it | **Rejected**: the name suggests a final P&L; the content is a staff rota. Set aside. If a revised P&L exists, please upload it |

**Still missing:** a prior forecast (recommended; without it no bridge and no accuracy tracker), the
Oct to Dec 2025 budget, and the drivers behind the forecast: pipeline, hiring plan, price changes,
known events (required for a projection; only growth rates were supplied). I would stop here and
wait for your answer.

*You replied: go ahead with the accepted files.*

## Findings

**1. September 2025 locked as actual, with one question.** Recurring lines are present (depreciation
4,200, rent 9,000, software, insurance; interest continues its decline to 1,069) and revenue
activity is in line with trend, so the close looks complete. But **marketing is 29,146**, 6.4% of
revenue against exactly 4.0% in every other month: **10,930 above the pattern.** Is that real spend,
or an accrual or misposting still to be corrected? If it is wrong, it should be fixed before it
becomes the locked outturn.

**2. Your forecast is last year's actuals plus 10%, on every line.** Every line in every forecast
month is the same month a year earlier × 1.10. That has four consequences:

| Issue | Evidence | 12-month effect on the forecast |
|---|---|---|
| **Revenue growth is understated** | Revenue has grown 15.4% year on year in every month of 2025 (FY Oct–Sep: 4,451,200 → 5,136,300, +15.4%; the year before also +15.4%). Forecast uses 10%; your model assumptions say 8% | At 15.4%, revenue would be 5,926,828, not 5,649,930: **276,898 higher.** Q4 2025 alone: 1,266,647 vs 1,207,470 |
| **The margin drop is ignored for nine months** | COGS was 58.0% of revenue every month to June 2025, then **60.0% from July 2025** (gross margin 42% → 40%). The forecast copies 58% for Oct 2025 to Jun 2026 and 60% only for Jul to Sep 2026 | At 60%, COGS is **81,684 higher** for Oct to Jun. Forecast gross margin 41.4% vs 40.0% now |
| **Two one-offs are repeated and inflated** | June 2025 professional fees 16,500 (normal 2,500) → forecast June 2026 18,150; Sep 2025 marketing 29,146 → forecast Sep 2026 32,061 | **15,400** and **12,023** of non-recurring cost carried forward |
| **Fixed and scheduled costs grown 10%** | Rent, depreciation, software, insurance, repairs flat for 36 months; interest falls as the loan amortises (5,000 a month at 5.7%) | Rent +10,800, depreciation +5,040, software +4,200, insurance +1,800, repairs +600; interest 15,831 vs about 10,972 on the loan schedule (+4,859) |

Payroll steps from 76,000 (Sep 2025) to 78,760 (Oct 2025), a jump of 2,760 against a steady +400 a
month; continuing +400 gives 943,200 for the window vs 974,160 forecast (+30,960). Is a hire planned?

**Questions for management:** what supports 10% when the business has run at 15.4% for two years;
is the 60% COGS ratio from July 2025 permanent; were the June fees and September marketing one-offs;
which growth rate is current, 8%, 10% or 15.4%?

**3. Test A (implied acceleration).** The forecast does not hold a number: it **decelerates.** Q4 2025
is forecast +10.0% on Q4 2024 against +15.4% achieved in each of the nine months to date. On revenue
the forecast is cautious; on costs it is inflated. Net income for the window is 795,803 vs 723,458
trailing twelve months (+10%).

**4. Test B (seasonality).** Supported by **three full years** (Oct to Sep, 2023 to 2025). Each month's
share of the year is the same in all three (for example October 7.31%, June 9.58%), and the forecast
keeps that shape, including the new far-end month (Sep 2026, 8.87%). No issue.

**5. Test C (run-rate benchmark, not a forecast).** Trailing-twelve-month revenue 5,136,300; net
income 723,458. The forecast sits 513,630 (10%) above TTM revenue. Q3 × 4 (5,693,600) is not a fair
benchmark: Q3 is the seasonal peak.

**6. Current-year outlook (calendar 2025).** Actuals Jan to Sep 4,038,600 + your Q4 forecast
1,207,470 = **5,246,070 revenue**; net income 594,241 + 142,138 = **736,379.** Against budget, Jan to Sep
only: revenue **+188,800 (+4.9%)**; COGS +137,972 (+6.2%, volume plus the margin drop); marketing
+18,482 (the September spike); professional fees +14,000 (June); net income **+13,990 (+2.4%).**
No full-year budget comparison: Oct to Dec 2025 budget not supplied.

**7. Accuracy tracker and bridge.** **Empty: first forecast.** Collection starts with this version;
save it and next month's refresh can bridge from it and score October.

## What was not done, and why

- **The projection itself**: not re-authored. The corrections above are figures for your decision.
- **Change bridge (Step 7)** and **accuracy score (Step 6)**: no prior forecast.
- **Scenario overlay (Step 8)**: not requested. Historical volatility is very low (growth 15.4% ±0.04
  points month to month), so any range should be argued from drivers, not history.
- **FX**: none stated, none applied. **External guidance**: none authored.
- **Excel workbook**: not created. Do you want `Rolling_Forecast_2025-09_Northbrook Trading Ltd.xlsx`?

## Coverage and provenance (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, USD, user-asserted; 12 months monthly; source upload; months locked Oct 2022 to Sep 2025, Sep verified by recurring-entry and activity test with the marketing question open; 3 years support seasonality. Files: P&L, budget, forecast, assumptions (each accepted with a limit), rota (rejected) |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 1 done; 2 done (Sep flagged); 3 done with a limit (growth rates only, no drivers); 3b done; 4 not authored (your file used); 5 done, budget Jan to Sep only; 6 and 7 **not done** (no prior forecast); 8 not requested; 9 tables in chat |
| Unknowns carried forward | Sep marketing 10,930; margin step to 60%; growth rate to use; payroll step 2,760; Oct to Dec budget |
| Parameters | Horizon 12, monthly; seasonality from FY2023 to FY2025; loan 5,000 a month at 5.7% from the assumptions; no FX |
