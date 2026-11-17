# Scenarios and sensitivities: Northbrook Trading Ltd, as at 30 September 2025

Mosofin is not connected, so this run is manual: every step works from your uploads, and every
"measured" range below was measured from the history files you supplied, not read from the books.
(Connecting Mosofin would automate the history reads: [docs.mosofin.com](https://docs.mosofin.com).)
Nothing is posted or changed anywhere. Scenarios are your stories; I only compute them.

## Read-back (please confirm)

> Testing **cash at 30 September 2026** and **minimum cash in the year** for the decision on a
> **second packing line in 2026**, on **your twelve-month forecast (Oct 2025 – Sep 2026)**, varying
> **revenue growth, gross margin, DSO and payroll**, with ranges proposed from **36 months of
> history** (Oct 2022 – Sep 2025). Scenarios: **Base, Steel shock, Lost customer**. Threshold:
> **minimum cash 250,000**. **No probability weights.** Cash bridged from 30 Sep 2025 cash
> (1,118,199) using forecast profit + depreciation − 5,000 loan repayment a month. USD. Go ahead?

The decision, metric, drivers, scenarios and threshold come from `scenario_request.md`; they count
as answered once you confirm. The forecast holds outputs only, not a live model: the scenarios
below are re-computed on a cash bridge, and you should re-run them in your own model.

## Validation of the upload (shown before any work)

| File | What it actually is | Company / period | Usable? | Step | Verdict |
|---|---|---|---|---|---|
| `forecast_2025-10_to_2026-09.csv` | 12-month P&L forecast, 12 line items, no cash or balance sheet, no formulas | No company named; Oct 2025–Sep 2026 | Yes; values only | Base case, Steps 3–7 | **Accepted with a limit**: outputs, not the model's structure; company user-asserted |
| `monthly_profit_and_loss_36m.csv` | Monthly P&L, Oct 2022–Sep 2025, 36 rows | No company named | Net income recomputes in all 36 months | Step 2b ranges (growth, margin, payroll) | **Accepted with a limit**: company user-asserted |
| `monthly_balance_sheet_36m.csv` | Monthly balance sheet, 36 rows | No company named | Balances every month; RE rolls by NI less dividends (60,000 Mar, 7,500 Jun 2025) | Opening cash; DSO history | **Accepted with a limit**: company user-asserted |
| `scenario_request.md` | Typed brief: decision, metric, drivers, scenarios, threshold | Northbrook context | Text | Intake B–F | **Accepted with a limit**: user-supplied, confirm in read-back |
| `forecast_2025-10_to_2026-09_final.csv` | **A staff shift rota** (employee, week_1..week_4: days/nights/off) | No financial content | Not a forecast | None | **Rejected**: despite the name it holds no figures. If a later forecast exists, upload it |

**Still missing:** nothing required. Recommended: the model itself (XLSX with assumptions), the
packing-line capex amount and timing, and customer-level revenue to evidence the 62,000/month for
Harlow Fabrication. I would wait for your answer; this run continues on the four accepted files.

## What the history says about each driver (Step 2b, proposed ranges, awaiting your yes)

| Driver | Obs | Min | P5 | Median | P95 | Max | Trend | Forecast base | Proposed range | Basis |
|---|---|---|---|---|---|---|---|---|---|---|
| Revenue growth (YoY) | 24 | 15.37% | 15.37% | 15.39% | 15.41% | 15.41% | none | **10.0%** | **none proposed** | History is flat (sd 0.01pp): no measurable volatility. Range is your judgment |
| Gross margin | 36 | 40.0% | 40.0% | 42.0% | 42.0% | 42.0% | step down: 42% to 40% from Jul 2025 | 42% Oct–Jun, 40% Jul–Sep | **−2pp / +0pp** | observed min/max |
| DSO (AR ÷ revenue × 30) | 36 | 42.0 | 42.5 | 47.0 | 51.5 | 52.0 | rising: 48.6 (Sep 2024) to 52.0 | AR held at 789,360 = 47.3 days of Sep 2026 revenue | **42.5 / 55.4 days** | P5; last-12-month drift continued |
| Payroll growth (YoY) | 24 | 6.74% | 6.79% | 7.21% | 7.68% | 7.74% | slowly falling | **10.0%** | **6.79% / 10.0%** | P5 observed; plan (nothing observed above 7.74%) |

**Ranges are mixed:** two measured, one partly measured and partly trend, revenue unmeasurable.
Correlations (36 obs): margin vs DSO −0.48 (both moved in the last quarter: a coincidence of trend,
not evidence of a link); growth correlations are meaningless on a constant series. I would stop
here for you to accept, adjust or override the ranges; the tables below use the proposals.

**Points in the forecast against the history:** (1) the forecast assumes margin returns to 42% in
October after three months at 40%; (2) growth drops to 10% from a steady 15.4%; (3) payroll rises
10% against a 6.7–7.7% history; (4) September 2025's software is 0 and marketing 29,146 (vs ~18,000
run-rate), and the same pattern is copied into September 2026 (software 0, marketing 32,061):
confirm it is a real reclassification and not a mis-posting rolled into the plan.

## Scenarios (Step 3)

| Scenario | Story (yours) | Cash 30 Sep 2026 | vs Base | Minimum cash (month) | Headroom over 250,000 |
|---|---|---|---|---|---|
| Base | Forecast as given | **1,913,292** | — | 1,169,583 (Oct 2025) | 919,583 |
| Steel shock | Margin −3pp, Oct 2025–Mar 2026 | **1,837,838** | −75,454 | 1,157,192 (Oct 2025) | 907,192 |
| Lost customer | Harlow leaves 1 Jan 2026, −62,000/month (15% of Oct revenue) | **1,708,692** | −204,600 | 1,169,583 (Oct 2025) | 919,583 |

Lost customer assumes COGS (at the month's margin), marketing (4.0%) and bank fees (0.4%) flex with
revenue; all other costs stay. Both are below the forecast's own history of shocks, which has none:
**this stress is beyond the observed data, by design.**

## Tornado: cash at 30 September 2026 (Step 5)

| Driver | Low | Cash at low | High | Cash at high | Swing | Range basis |
|---|---|---|---|---|---|---|
| DSO | 42.5 days | 1,992,987 | 55.4 days | 1,777,583 | **215,404** | P5 / trend continued |
| Gross margin | −2pp | 1,800,293 | +0pp | 1,913,292 | **112,999** | observed min/max |
| Payroll growth | 6.79% | 1,941,720 | 10.0% | 1,913,292 | **28,428** | P5 / plan |
| Revenue growth | — | — | — | — | not ranked | each ±1pp of growth = ±18,918 |

**Working capital outranks margin for this cash metric.** Ranking compares mixed bases, so it is a
ranking of these ranges, not a full risk ranking.

## Two-variable table: cash at 30 Sep 2026, margin shift × DSO (Step 6)

| Margin shift \ DSO | 42.5 | 47.3 (base) | 52.0 | 55.4 |
|---|---|---|---|---|
| 0pp | 1,992,987 | **1,912,837** | 1,834,356 | 1,777,583 |
| −1pp | 1,936,488 | 1,856,337 | 1,777,857 | 1,721,084 |
| −2pp | 1,879,988 | 1,799,838 | 1,721,357 | 1,664,584 |
| −3pp *(outside observed)* | 1,823,489 | 1,743,339 | 1,664,858 | 1,608,085 |

## Threshold (Step 7)

Under the requested bridge, **no scenario comes near 250,000**. Cash would breach it only with a
revenue loss of **375,631 a month from October (≈91% of revenue)**, a margin fall of **29.4pp**, or
DSO of **122 days**.

**But the bridge overstates cash, and the history proves it.** For Jan–Sep 2025 the same bridge
(profit + depreciation − 5,000) gives **+590,541**; actual cash rose **202,613**. Dividends explain
67,500; **working capital absorbed about 320,428** (AR and inventory grew with revenue). Headroom
from this bridge should not be used for the packing-line decision until working capital is modelled.

## Not done, and why

- Packing-line capex: amount and timing not supplied, so its cash effect is not computed. The decision is yours.
- Probability weighting and Monte Carlo: no weights given; not run.
- Covenants: none given; ledger profit is not covenant EBITDA.
- Re-running in the live model: only outputs were supplied.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, USD, as at 30 Sep 2025: **user-asserted**. Data source **upload** (Mosofin not used). Files: 4 accepted with limits, 1 rejected (shift rota). History: 36 months P&L and BS; 24 YoY observations. Metric: cash 30 Sep 2026 and minimum cash. Range basis: **mixed**. Model structure: **outputs only** |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 1 done; 2 done; 2b done (ranges proposed, awaiting yes); 2c done; 3 done; 4–6 done; 7 done with a limit (bridge omits working capital); 8–9 not run (no weights); 10 figures only; 11 tables in chat |
| Unknowns | Revenue-growth volatility unmeasurable; correlation on 36 points; working capital not in the bridge; Harlow revenue user-supplied |
| Parameters | Bridge: NI + depreciation − 5,000/month from 1,118,199; percentiles linear; DSO = month-end AR ÷ month revenue × 30 |

Would you like this as `Scenario_Sensitivity_Northbrook Trading Ltd_2025-09-30.xlsx`?
