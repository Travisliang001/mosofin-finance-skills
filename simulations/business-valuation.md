# Business valuation — Northbrook Trading Ltd, as at 30 September 2025 (upload path)

Mosofin is not connected, so this run is manual and works only from the files you uploaded (connecting Mosofin would automate the company-side reads: docs.mosofin.com). **This is valuation analysis, not an opinion of value.** Nothing was written anywhere.

## (a) Read-back

Valuing **Northbrook Trading Ltd** (interest not stated, see below) at **30 September 2025**, for **management planning**, on **fair market value**, going-concern premise, in **USD**, from **your uploaded statements, your 12-month forecast and the market data you supplied**. Three approaches; per-share value only as indicative (no cap table).

| Intake question | Status | Treatment |
|---|---|---|
| B — business, purpose, standard | Company from your intake; purpose and standard arrived inside `market_data_supplied.md` | Used as confirmed in this read-back |
| C — valuation date | 30 Sep 2025 (intake period and market-data file agree) | Every figure read as at 30 Sep 2025 |
| D — forecast, normalised earnings | Forecast uploaded; **no normalised earnings** | Reported EBITDA used; candidate normalising items listed, not applied |
| E — rate inputs, comps, deals | Supplied in the market-data summary; several without a source or date | Used, each labelled user-supplied; unsourced ones listed as open |
| F — diluted shares, instruments | 1,080,000 diluted shares in the file; **no instruments, no cap table** | Equity in total; per share shown as indicative only |
| Level of value (control / minority, % held) | Not answered; skill states no default | Assumed 100%, no control premium, no DLOM (marketability discount) applied; precedents shown on their control basis, separately |

## (b) Validation of the upload — shown before any work

| File | What it actually is | Company / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `monthly_balance_sheet_36m.csv` | Month-end balance sheets: cash, AR, inventory, prepaid, net fixed assets, AP, accrued, debt, share capital, retained earnings | 36 month-ends, Oct 2022–Sep 2025. No company or currency named | Yes. Balances every month; retained earnings roll equals P&L net income every month. Debt is one line (cannot split term loan from card) | Yes — historical FCFF (Step 3), bridge (Step 7) | **Accepted with a limit**: company/currency user-asserted; net debt cannot be itemised to your definition |
| `monthly_profit_and_loss_36m.csv` | Monthly P&L by expense line, with net income | 36 months, Oct 2022–Sep 2025. No company or currency | Yes; each month's net income recomputes. **No income-tax line** — net income is pre-tax | Yes — LTM EBITDA (Steps 3–5) | **Accepted with a limit**: company user-asserted; tax status unknown |
| `forecast_2025-10_to_2026-09.csv` | Your 12-month P&L forecast | Oct 2025–Sep 2026 | Yes, but P&L only: **no capex, no working capital, no tax**; one year, not 5–10 | Yes — DCF (Step 3) | **Accepted with a limit**: DCF is indicative only |
| `market_data_supplied.md` | A typed summary of market inputs, not the source data | Dated 30 Sep 2025 | Yes as a summary. Sourced: risk-free rate (govt bond, 30 Sep 2025), comps (your data provider, 30 Sep 2025). **No source or date**: ERP, beta, size premium, cost of debt, tax rate ("sample"), debt weight, precedents, terminal growth. No peer or deal names | Yes — Steps 3–5, 7 | **Accepted with a limit**: every figure user-supplied, not evidenced |
| `monthly_profit_and_loss_36m_final.csv` | **Not a P&L.** A staff shift rota: employee E08–E10, week_1–week_4, "nights/days/off" | No company, no dates, no amounts | No | No step uses it | **Rejected** on content. If a final P&L exists, please upload it; otherwise I use `monthly_profit_and_loss_36m.csv` |

Still missing: cap table / dilutive instruments (required for per-share value); sources and dates for the unsourced inputs; peer and deal names; the interest being valued; capex and working-capital forecast; tax status of the company.

*I would stop here and wait. Assumed answer: "go ahead with the accepted files".*

## (c) Findings

**1. Historical reality check (FCFF = EBIT × (1−20%) + D&A − capex − Δ working capital; years to September)**

| USD | FY23 | FY24 | FY25 (LTM) |
|---|---:|---:|---:|
| Revenue | 3,857,500 | 4,451,200 | 5,136,300 |
| EBITDA (reported) | 500,021 | 665,649 | 812,250 (15.8%) |
| Capex (net fixed assets fall exactly by depreciation every month) | 0 | 0 | 0 |
| Δ working capital | n/a | 202,950 | 262,287 |
| FCFF | n/a | 339,649 | **397,593** |

Zero capex for 36 months, with net fixed assets down to 108,800, is not sustainable; working capital absorbs about 38% of each dollar of revenue growth.

**2. The forecast is last year × 1.10, line by line — including last year's one-offs.** Every line of every month is exactly 1.10 × the same month of FY25: the June professional-fee spike (18,150 vs 2,750 run-rate), the September marketing spike (6.4% of revenue vs 4.0%), and the July–September gross-margin step-down (COGS 60% vs 58%). Depreciation (+10%) and interest (+10%) also rise despite no capex and an amortising loan. Forecast EBITDA 893,474 (15.8%).

**3. EBITDA used is reported, not normalised.** Candidate adjustments in FY25 for you to accept or reject: June professional fees +14,000; September marketing +10,930 → normalised EBITDA **837,180** if both are one-off. The COGS step to 60% has lasted three months; I treat it as a margin change, not a one-off.

**4. WACC (weighted average cost of capital) — your inputs:** cost of equity 4.2% + 1.1 × 5.5% + 2.0% = **12.25%**; after-tax cost of debt 5.7% × 0.8 = 4.56%; WACC = 80% × 12.25% + 20% × 4.56% = **10.71%**. Cross-check: actual interest 22,800 on average FY25 debt 247,500 = **9.2%**, well above the 5.7% supplied. Beta is a single figure, not unlevered/relevered from peers. The 20% debt weight is a target; current debt is about 3% of the concluded EV.

**5. DCF — indicative only (one-year forecast; terminal value is 93% of it)**

| Case | FCFF year 1 | EV at 10.71%, g 2.5% | Range (WACC ±1%, g ±0.5%) | Implied exit multiple |
|---|---:|---:|---:|---:|
| A — forecast as supplied (capex 0, Δ WC 0) | 725,867 | **8,839,104** | 7,473,921 – 10,814,470 | 10.1× EBITDA |
| B — history-consistent check (Δ WC at 38% of growth = 196,641; terminal capex = D&A, Δ WC = g × WC) | 529,227 | **7,656,369** | 6,459,731 – 9,388,228 | 8.9× EBITDA |

Case A's FCFF is 1.8× FY25 actual FCFF, and its implied exit multiple (10.1×) is above every comparable; Case B is my reality check, not your forecast. Exit method at the comps median 8.1× gives EV 7,192,542, implying perpetual growth of only 0.6%.

**6. Trading comparables** (EV/EBITDA, your provider, 30 Sep 2025): 6.8 / 7.4 / 8.1 / 8.9 / 9.6×; mean 8.16×, median 8.1×, quartiles 7.4×–8.9×. On LTM reported EBITDA 812,250: **6,010,650 – 7,229,025, mid 6,579,225** (normalised: 6,195,132 – 7,450,902). Minority, marketable basis.

**7. Precedent transactions** (7.0 / 8.5 / 10.2×; mean 8.57×, median 8.5×; no source, date or names): **5,685,750 – 8,284,950, mid 6,904,125**. These carry a control premium; they are not mixed unadjusted with comps.

**8. Triangulation — proposed, for your judgment.** Comps 50% (best sourced), precedents 25% (control basis, unsourced), DCF Case B 25% (one-year forecast): central **6.93m**. **Concluded EV range: USD 6.0m – 7.7m, central about 6.9m.** DCF Case A (8.8m) sits outside the market evidence; that gap is itself a finding.

**9. Bridge to equity (itemised as far as the files allow)**

| USD, 30 Sep 2025 | Low | Central | High |
|---|---:|---:|---:|
| Enterprise value | 6,000,000 | 6,900,000 | 7,700,000 |
| − Debt (one line; term loan and card balance not separable) | (220,000) | (220,000) | (220,000) |
| + Cash (restricted cash unknown) | 1,237,236 | 1,237,236 | 1,237,236 |
| **Equity value, 100%** | **7,017,236** | **7,917,236** | **8,717,236** |
| Indicative per share on your 1,080,000 diluted shares (no cap table) | 6.50 | 7.33 | 8.07 |

Net cash of 1,017,236 is 13% of equity value; card balance, restricted cash and any debt-like items (leases, shareholder loans, tax payable) are unconfirmed.

## (d) What was not done, and why

| Step | Status | Gap |
|---|---|---|
| 0 Evidence | done from uploads | No trial balance or GL; debt not itemised |
| 1–2 Engagement, approaches | done, user-asserted | Level of value / interest not stated |
| 3 DCF | done with a limit | One-year forecast; no capex, WC or tax forecast; 6 of 8 rate inputs unsourced |
| 4–5 Comps, precedents | done with a limit | No peer/deal names; precedents unsourced and undated |
| 6 Triangulation | proposed | Weighting is my proposal, for your judgment |
| 7 Bridge | done with a limit | Card balance and restricted cash unknown; per share needs a cap table |
| 8 Control premium / DLOM | **not done** | Level of value not given; not stacked |
| 9 Sensitivities | done | WACC ±1% × g ±0.5% above |
| 10–11 Report, workbook | not created | Would you like `Valuation_Northbrook Trading Ltd_2025-09-30.xlsx`? Only on a yes |
| 12 Save preferences | not offered yet | Only after you review; no market data would be saved |

**Coverage (manual run).** Environment: Northbrook Trading Ltd, 30 Sep 2025, USD — user-asserted; data source upload; verdicts as in (b). Capability map: not applicable, no connection; every task `[manual]`. Not done: tie to GL totals, itemised net debt, tax provision — need a trial balance at 30 Sep 2025 and a debt schedule.

**Limiting condition:** company figures come from your uploaded monthly statements as at 30 Sep 2025; all market data was supplied by you and none was sourced here. A qualified valuer must sign before anyone relies on these figures for tax, litigation or reporting.

**Data sources:** user uploads only — `monthly_balance_sheet_36m.csv`, `monthly_profit_and_loss_36m.csv`, `forecast_2025-10_to_2026-09.csv`, `market_data_supplied.md`.
