# Scenarios and sensitivities — Northbrook Trading Ltd, second packing line decision

This run is manual: no Mosofin connection. Everything below comes from the files you uploaded.
Nothing has been posted, sent or changed. The base case and the scenario stories are yours.

## Read-back

Testing **cash at 30 September 2026** and **minimum month-end cash** in **Northbrook Trading Ltd's
twelve-month forecast (October 2025 to September 2026)**, in **USD**, for the decision **whether to
take a second packing line in 2026**. Varying **revenue growth, gross margin, DSO and payroll**, with
ranges **proposed from 36 months of history (October 2022 to September 2025)**. Scenarios **Base,
Steel shock (margin down 3 points for six months), Lost customer (Harlow leaves in January)**.
Threshold **minimum cash 250,000**. No probability weights, so no expected value. These answers come
from `scenario_request.md`; company, period and currency are as you stated them.

## Validation of the upload (before any work)

| File | What it actually is | Right company and period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `scenario_request.md` | The decision, metric, drivers, three scenarios and the 250,000 threshold | No company named (user-asserted) | Yes. Two gaps: Harlow's share of revenue, and which six months the steel shock covers | Steps 1, 3, 7 | **Accepted with a limit**: "Lost customer" cannot be sized without Harlow's revenue |
| `forecast_2025-10_to_2026-09.csv` | A 12-month P&L forecast by line, Oct 2025 to Sep 2026 | Yes, the window in the request | P&L only: **no cash, receivables, inventory, payables, capex or debt lines** | Steps 3–7 (base case) | **Accepted with a limit**: the model cannot produce the chosen metric (cash). Cash below comes from an indicative bridge I built from your balance-sheet history, not from your model; you should re-run it there |
| `monthly_profit_and_loss_36m.csv` | Monthly P&L, Oct 2022 to Sep 2025, 36 months | User-asserted | Yes; net income recomputes every month | Step 2b (ranges) | **Accepted with a limit**: company user-asserted |
| `monthly_balance_sheet_36m.csv` | Monthly balance sheet, Oct 2022 to Sep 2025 | User-asserted | Yes. Balances every month; cash movement reconciles every month to net income + depreciation ± working capital − 5,000 debt repayment − dividends (60,000 Mar 2025, 7,500 Jun 2025) | Steps 2b, 7 (opening cash 1,114,699; DSO, DIO, DPO) | **Accepted with a limit**: company user-asserted |
| `forecast_2025-10_to_2026-09_final.csv` | A four-week shift rota for employees E08 to E10 | No company, date or amount | Not for this skill | No step uses it | **Rejected**: the name suggests a final forecast; the content is a staff rota. Set aside |

**Still missing:** the model with its cash lines (required: an XLSX whose cash, working capital and
capex respond to the drivers), Harlow's revenue (blocks that scenario only), the cost and timing of
the packing line, and the six months of the steel shock. I would stop here and wait for your answer.

*You replied: go ahead with the accepted files.*

**Assumptions in the indicative cash bridge** (yours to correct): DSO 52, DIO 75, DPO 33 days held at
September 2025; accruals +200 a month; debt repaid 5,000 a month; **no capex and no dividends** (none
in the forecast; 67,500 was paid in 2025); steel shock in Oct 2025 to Mar 2026.

## Driver history and proposed ranges (36 months, monthly)

| Driver | Obs | Min | P5 | Median | P95 | Max | Trend | Proposed range |
|---|---:|---:|---:|---:|---:|---:|---|---|
| Revenue growth, YoY | 24 | 15.37% | 15.37% | 15.39% | 15.41% | 15.41% | Flat | **None usable**: history moved 0.04 points. Range must be yours. Your forecast uses 10%, well below every month of history |
| Gross margin | 36 | 40.0% | 40.0% | 42.0% | 42.0% | 42.0% | Stepped down 2 points in Jul 2025 | 40% to 42% (observed). Forecast averages 41.4% |
| DSO, days | 36 | 42.0 | 42.5 | 47.0 | 51.5 | 52.0 | **Rising ~0.3 days a month, every month** | 42.5 to 51.5 observed; base 52 is the maximum ever, and the trend reaches 55.6 by Sep 2026 |
| Payroll, month-on-month | 35 | 0.53% | 0.53% | 0.58% | 0.64% | 0.65% | Steady | P5–P95 from Sep 2025's 76,000 |

DSO and DIO (60 → 75 days) have both drifted up for three years, so the historical median is not the
current central value. Growth has no variance, so a correlation with it means nothing; none is used.

## Results (cash from the indicative bridge)

**Base:** net income 795,803; **cash at 30 Sep 2026 1,791,152**; lowest month-end cash in the window
1,286,829 (Oct 2025), against opening cash of 1,114,699. **Headroom over 250,000: 864,699 at the
opening, 1,036,829 at the lowest month-end.**

| Scenario | Net income | Cash 30 Sep 2026 | vs base | Min month-end cash | Breaches 250,000? |
|---|---:|---:|---:|---:|---|
| Base | 795,803 | 1,791,152 | — | 1,286,829 | No |
| Steel shock, Oct 2025–Mar 2026 | 720,348 | 1,715,698 | −75,454 | 1,257,089 | No |
| Steel shock, Jan–Jun 2026 (alternative timing) | 709,501 | 1,704,851 | −86,301 | 1,286,829 | No |
| Lost customer (Harlow) | **Not run** | | | | Needs Harlow's revenue |

For Lost customer, per 10% of revenue lost from January: net income −162,703, cash at 30 Sep 2026
−33,794 (lower receivables and stock release cash). On these mechanics no loss up to 100% takes cash
below 250,000 within the year, because opening cash is 1,114,699 and working capital unwinds; treat
that as a property of the bridge, not comfort, until your model confirms it.

**Tornado on cash at 30 September 2026** (other drivers at base):

| Driver | Low | High | Swing | Range basis |
|---|---:|---:|---:|---|
| DSO 51.5 → 42.5 days | 1,799,501 | 1,949,783 | **150,282** | Observed P5–P95 |
| Gross margin 40% → 42% | 1,709,468 | 1,836,493 | **127,025** | Observed min–max |
| Revenue growth 8% → 12% | 1,776,753 | 1,805,551 | 28,798 | **Illustrative ±2 points, not history** |
| Payroll growth 0.64% → 0.53% a month | 1,814,468 | 1,821,275 | 6,807 | Observed P5–P95 |

Mixed bases: growth is illustrative, the rest observed, so the ranking of growth is not a risk
ranking. Working capital, not revenue, dominates cash. If DSO keeps its trend (55.6 days by Sep
2026), cash at 30 Sep 2026 is 1,731,040, 60,112 below base. Your forecast's payroll (974,160) is
23,000 to 30,000 above the observed growth path (944,037 to 950,844).

## What this means for the decision

On every case run, cash stays far above 250,000. The open question is the size and timing of the
packing line: the base case can absorb up to about 864,699 at today's balance before touching the
minimum. Monitor DSO and the July 2025 margin step; both have moved against you.

## What was not done, and why

- **Lost customer**: Harlow's revenue not supplied. **Expected value / Monte Carlo**: no weights asked
  for. **Stress case beyond history**: none authored. **Two-variable table**: not needed for this question.
- **Cash in your own model**: your forecast has no cash lines; every cash figure above is indicative.
- **Excel workbook**: not created. Do you want `Scenario_Sensitivity_Northbrook Trading Ltd_2025-09-30.xlsx`?

## Coverage and provenance (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, USD, user-asserted; source upload; request, forecast, P&L and balance sheet accepted with limits; rota rejected |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 1 done; 2–2b done (36 obs); 2c not meaningful; 3 done for two scenarios, Lost customer **not done**; 4–5 done; 6 not needed; 7 done (indicative bridge); 8–9 not requested; 10 findings only |
| Unknowns | Harlow revenue; packing line cost; shock timing; dividends; capex; model cash logic |
| Parameters | Window Oct 2022–Sep 2025; P5/P95 linear interpolation; DSO 52 / DIO 75 / DPO 33; metric cash |
