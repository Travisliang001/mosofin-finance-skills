# KPI dashboard — Northbrook Trading Ltd, board, 36 months to September 2025

Mosofin is not connected, so this run is manual: every metric is computed from the files you uploaded and marked `[manual]`. (Connecting Mosofin would read the monthly statements and ageings directly — docs.mosofin.com. Not raised again.)

## (a) Read-back

- **Company:** Northbrook Trading Ltd (user-asserted). **As at:** 30 September 2025, closed months only. **Currency:** USD (user-asserted).
- **From `kpi_request.md` (please confirm):** audience **the board**; business model **distribution with some services**; **36 months to September 2025, refreshed monthly**; **no operational system connected** (orders sit in a separate order system, not uploaded); **no targets set**; current KPI "gross margin", **defined informally**.
- Files received: monthly P&L, 36 months Oct 2022–Sep 2025, 13 columns; monthly balance sheet, same 36 months, 11 columns; the request note; and `monthly_profit_and_loss_36m_final.csv` (see below).

## (b) Validation of the uploaded files (before any work)

| File | What it actually is | Right company / period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `monthly_profit_and_loss_36m.csv` | Monthly P&L: revenue, COGS, 10 expense lines, net income | No entity named; Oct 2022–Sep 2025, no gaps | Yes: every month foots (revenue − expenses = net income, 36/36) | Steps 1–7: every income metric and trend | **Accepted with a limit:** company user-asserted; summary lines, not account numbers |
| `monthly_balance_sheet_36m.csv` | Month-end balance sheet: cash, AR, inventory, prepaid, net fixed assets, AP, accrued, debt, equity | No entity named; same 36 months | Yes: assets = liabilities + equity every month; net fixed assets fall by depreciation every month | Steps 1–7: liquidity, working capital, leverage | **Accepted with a limit:** company user-asserted; retained earnings do not roll in 2 months (finding 6) |
| `kpi_request.md` | Intake answers: audience, model, period, systems, targets | Names the 36 months to Sep 2025 | Yes | Stage 1 B–F | **Accepted with a limit:** user-supplied |
| `monthly_profit_and_loss_36m_final.csv` | **An employee shift roster** (E08–E10, weeks 1–4) — not a P&L despite the name | No company, no period | No financial data | No step uses it | **Rejected:** a staff rota. If a revised P&L exists, upload that instead |

**Still missing:** AR and AP ageings (recommended; DSO/DPO below are balance-based approximations of the standard formula, not ageing-based); order-system export (needed for any order or customer metric); targets (none set). No cash-flow statement, so operating cash flow is not shown.

I would stop here and wait for your answer. *(Assumed answer: "go ahead with the accepted files".)*

## (c) The dashboard (board, 11 metrics, all `[manual]` from uploads, closed periods)

**Targets: none supplied — every target shows TBD; no status colours are applied.** Tie-out: dashboard revenue and net income equal the uploaded P&L for all 36 months.

| Group | KPI | Sep 2025 | Sep 2024 | Trend / note |
|---|---|---|---|---|
| Growth | Revenue (month) | 455,400 | 394,700 | **+15.4% YoY**; seasonal — peaks Jun/Jul, troughs Dec, so MoM (−4.5%) misleads |
| Growth | Revenue, trailing 12 months | 5,136,300 | 4,451,200 | +15.4%; prior year 3,857,500 |
| Profitability | **Gross margin %** | **40.0%** | 42.0% | **Exactly 42.0% for 33 months, then 40.0% from July 2025 (−2.0 pts)**; ~9,100 of gross profit a month at Sep revenue |
| Profitability | Operating margin % (before interest) | 11.9% | 14.2% | TTM net margin 14.1% vs 12.9% |
| Profitability | EBITDA (month) | 58,192 | 60,207 | TTM 788,250 vs 641,649 |
| Profitability | Marketing % of revenue | **6.4%** | 4.0% | **4.0% every month for 35 months; Sep 2025 = 29,146, 10,930 above the 4% run-rate** |
| Liquidity | Cash | 1,114,699 | 730,628 | Up every month since Jan 2025; cash-generative, so runway is not a constraint |
| Liquidity | Current ratio | 7.69 | 6.39 | Quick ratio 5.62 |
| Efficiency | DSO (AR ÷ month revenue × 30) | **52.0 days** | 48.6 | **Up steadily from 42.0 in Oct 2022 — +10 days in 36 months** |
| Efficiency | DIO (inventory ÷ month COGS × 30) | **75.0 days** | 69.9 | Up from 60.0 |
| Efficiency | Cash conversion cycle (DSO + DIO − DPO) | **94.0 days** | 83.7 | **Up from 64.0**; DPO fell 38.0 → 33.0 |
| Leverage | Term debt | 220,000 | 280,000 | Falls 5,000 a month |

### Alerts and commentary (movements described; drivers need your evidence)

1. **Gross margin stepped down 2.0 points in July 2025** (42.0% → 40.0%) and has stayed there three months. A flat 42.0% for 33 months, then a clean step, looks like a pricing, cost or costing-method change — the cause is not in the books supplied. This is the board's first item.
2. **September marketing 29,146 (6.4% of revenue) is 10,930 above its 4.0% run-rate** — a one-month spike or a new level; confirm.
3. **June 2025 professional fees 16,500 vs 2,500 every other month (+14,000)**, which pulled June's operating margin to 15.2% from 17.7% in May.
4. **Working capital is deteriorating steadily**: DSO +10.0 days, DIO +15.0 days, DPO −5.0 days → cash conversion cycle **+30 days** in three years. Ageings would show whether specific customers or slow stock drive it.
5. **September operating margin 11.9% is the lowest since February 2025**, from points 1–2 together; revenue also fell for the third month (seasonal pattern, but YoY growth is intact).
6. **Retained earnings do not roll from net income in two months**: March 2025 moves 3,413 against net income 63,413 (**−60,000**, consistent with a dividend); June 2025 moves 66,427 against 73,927 (**−7,500, unexplained**). Equity metrics are unaffected in this set, but the June item needs an answer before the board pack.
7. **"Gross margin" is defined informally today.** Proposed definition: (revenue − COGS) ÷ revenue, monthly period total, COGS line as uploaded; confirm whether freight and the services cost sit in COGS.

### Not Available (declined — no data source; never approximated from the ledger)

Order count, average order value, fill rate and on-time delivery (order system); customer count, retention, repeat purchase rate (order or CRM system — invoice counts are not customers); services utilisation and realisation (time system); segment margins distribution vs services (revenue not split); operating and free cash flow (cash-flow statement); benchmarks (none supplied).

## (d) What was not done, and why

- **Targets and status:** none set; shown TBD. **Ageing-based DSO/DPO:** no ageings. **Order and service metrics:** no exports.
- **Excel or HTML dashboard** `KPI_Dashboard_Northbrook Trading Ltd_2025-09.xlsx`: not created — say which format, if any.
- **Nothing was posted, sent or changed.** Nothing is saved.

## (e) Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, 36 months to 30 Sep 2025, USD — user-asserted. Source: upload (no Mosofin connection). 3 files accepted with a limit; `monthly_profit_and_loss_36m_final.csv` rejected (shift roster) |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 0 done (uploads); 1 done (11 metrics, 9 declined); 2 done (formulas above, period basis stated); 3 done (tie-out: P&L foots 36/36, BS balances 36/36, RE roll fails 2 months); 4 targets TBD; 5 done (grouped table); 6 done (36-month series); 7 done; 8 tables in chat; 9 not offered until results approved |
| Not done | Ageing DSO/DPO (ageings); cash-flow metrics (cash-flow statement); operational metrics (order, CRM, time systems) |

**Data sources:** user uploads — `monthly_profit_and_loss_36m.csv`, `monthly_balance_sheet_36m.csv`, `kpi_request.md`.
