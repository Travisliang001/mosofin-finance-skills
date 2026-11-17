# Budget FY2026 — Northbrook Trading Ltd (upload path)

Mosofin is not connected, so this run is manual: the history comes from the file you uploaded and the plan from your inputs. Connecting Mosofin would read the history and any existing budget directly ([docs.mosofin.com](https://docs.mosofin.com)). Nothing was loaded into any system.

## Read-back

Building the **FY2026 monthly budget (January–December 2026)** for **Northbrook Trading Ltd** (user-asserted), in **USD**, from **36 months of history (Oct 2022 – Sep 2025)**. Method from your inputs file: **driver-based revenue, incremental overheads**. **No 2026 budget exists**, so nothing is being replaced. Target: **12% operating margin**.

Your intake period was "September 2025". I read that as the date of the latest actuals, with the budget year taken from your inputs file (FY2026). Please confirm.

**Assumptions applied where nothing was supplied:**
- **No inflation** on any cost except rent. Those lines stay flat at current levels.
- **No merit rises** for existing staff. Payroll is held at the September 2025 run-rate.
- **No tax rate** assumed. The budget stops at operating income, with interest shown below it.
- No capex plan, so depreciation is held flat.

## Validation of the upload (shown before any work)

| File | What it actually is | Company / period | Usable? | Used by | Verdict |
|---|---|---|---|---|---|
| `monthly_profit_and_loss_36m.csv` | Monthly P&L by line, 36 rows, Oct 2022 – Sep 2025: revenue, COGS, payroll, rent, marketing, software, professional fees, bank fees, depreciation, interest, net income. Net income recomputes on every row | No company or currency in the file | Yes. LTM (Oct 2024 – Sep 2025) revenue **5,136,300**, operating income **761,850** | Steps 1–5, 8 (base, seasonality, ratios) | **Accepted with a limit**: company user-asserted. **No actuals for Oct–Dec 2025**, and payroll is one line, so the employer loading cannot be derived |
| `budget_inputs_2026.md` | Your plan: drivers, hires, rent, target | FY2026 | Yes, as user-supplied assumptions | Steps 2, 4, 6, 8 | **Accepted** (every figure taken from it is labelled "supplied by you") |
| `monthly_profit_and_loss_36m_final.csv` | **Not a P&L.** A staff shift rota: E08–E10, week_1…week_4, "nights / days / off" | No amounts or dates | No | No step | **Rejected** on content. The name suggests a final P&L. Upload it if one exists; otherwise the 36-month file is used. |

**Still missing:** Oct–Dec 2025 actuals or forecast (the base for Q4); payroll split into wages and employer taxes/benefits (needed to load the new hires); any inflation or merit assumptions; a tax rate if you want net income.

*Here I would stop and wait for your answer. Assumed answer: "go ahead with the accepted files".*

## What the history shows (derived, 36 months)

- **Seasonality is stable.** Every year has the same shape: a low in Nov–Dec (about 7.0% of annual revenue per month) and a peak in Jun–Jul (about 9.6%). Revenue grew **15.4% a year** in each of the last two years. The 2026 months use this shape: base = same month of the last 12 months.
- **COGS was exactly 58.0% of revenue for 33 months, then 60.0% from July 2025.** That is a step up, not noise. A supplier cost rise is the likely cause. Please confirm.
- **Marketing is 4.0% and bank fees 0.4% of revenue** in every month except one: **Sep 2025 marketing is 29,146, which is 10,930 above 4%**.
- **One-off items:** professional fees **14,000 above** the 2,500 norm in June 2025, and the Sep 2025 marketing excess. Both are excluded from the base. LTM operating income normalised for them: **786,780 (15.3%)**.

## FY2026 budget (USD)

| | Q1 | Q2 | Q3 | Q4 | **FY2026** | LTM actual |
|---|---:|---:|---:|---:|---:|---:|
| Revenue | 1,322,421 | 1,646,727 | 1,643,390 | 1,281,081 | **5,893,620** | 5,136,300 |
| Cost of sales | 770,342 | 959,259 | 957,315 | 746,261 | 3,433,177 | |
| **Gross profit** | 552,079 | 687,469 | 686,076 | 534,820 | **2,460,443 (41.75%)** | |
| Payroll | 236,667 | 254,000 | 274,500 | 274,500 | 1,039,667 | 885,600 |
| Other opex (rent, marketing, software, prof. fees, bank fees, depreciation) | 115,787 | 130,056 | 131,409 | 115,468 | 492,719 | |
| **Operating income** | 199,626 | 303,413 | 280,166 | 144,853 | **928,057** | 761,850 |
| **Operating margin** | 15.1% | 18.4% | 17.0% | **11.3%** | **15.75%** | 14.83% |

Monthly operating margin runs from 19.0% (June) down to **10.9% (December)**. Oct–Dec are each below 12%.

## Assumptions register

| Line | Driver and value | Origin |
|---|---|---|
| Revenue, existing | Same month of the last 12 months × **1.08 volume × 1.03 price** | Drivers supplied by you; base and shape derived (Oct 2024 – Sep 2025) |
| Revenue, new customer | **20,000 a month from April** (240,000 a year) = 180,000 in 2026 | Supplied by you |
| Cost of sales | Current unit cost (60% of 2025 prices), no cost inflation, so **58.25% of 2026 revenue** (0.60 / 1.03) | Derived (Jul–Sep 2025 level); "no inflation" is my default |
| Payroll, existing | **76,000 / month** (Sep 2025 run-rate), flat | Derived; flat by default. History rose 400 a month, about 6% a year |
| Payroll, hires | 2 warehouse × 52,000 from March (86,667 in 2026); 1 sales × 82,000 from July (41,000) | Supplied by you. **Salary only, no employer loading**: not derivable from the files, so cost is understated by the loading |
| Rent | 9,000 Jan–Jun, **9,500 from July** | Supplied by you |
| Marketing / bank fees | **4.0% / 0.4% of revenue** | Derived, 36 months, excl. the Sep 2025 one-off |
| Software 3,500, professional fees 2,500, depreciation 4,200 a month | Flat | Derived; one-offs excluded; no capex plan |
| Interest | 1,900 a month, below operating income | Derived |

## Flex and reconciliation to target

| Case | Operating income | Margin | Change |
|---|---:|---:|---:|
| Budget | 928,057 | 15.75% | — |
| Revenue +10% / −10% | 1,148,170 / 707,945 | 17.71% / 13.35% | ±220,112 |
| Suppliers also pass on +3% (COGS 60% of revenue) | 825,062 | 14.00% | −102,995 |
| Hires 2 months earlier / 3 months later | 897,057 / 974,557 | 15.22% / 16.54% | −31,000 / +46,500 |

- **Against target:** 15.75% beats 12% by **220,823**. Every case above still clears 12% on the year.
- **Q4 does not clear 12%.** The weaker Q4 is also the least evidenced: its base is **Oct–Dec 2024** (1,097,700), because 2025 actuals for those months do not exist yet. At the 15.4% growth your history shows, that base would be about 168,947 higher. I have not used that figure. Please send a Q4 2025 forecast.
- **Against prior year:** revenue +14.7%, operating income +21.8% on reported LTM and +18.0% on normalised LTM. Gross margin is 41.75% against 40.0% at the current cost level, a gain that comes only from the price rise.

## Not done, and why

- Loaded cost of hires: payroll is not split into wages and employer taxes.
- Net income after tax: no tax rate supplied.
- Unit economics (CAC, LTV): no customer-level data.
- Excel workbook `Budget_FY2026_Northbrook Trading Ltd.xlsx` with live driver formulas: not created. Would you like it?

## Coverage sheet (manual run)

**Environment:** Northbrook Trading Ltd, FY2026, USD, user-asserted. Data source: upload, because the Mosofin gateway is absent. P&L history accepted with a limit (no Q4 2025, payroll unsplit); inputs accepted; rota rejected.
**Capability map:** Not applicable: no connection. Every task is `[manual]`.

| Step | Status |
|---|---|
| 1 Method | Done: driver-based revenue and COGS, incremental overheads |
| 2 Revenue | Done with a limit: Q4 base is 2024 |
| 3 Cost of sales | Done: unit-cost basis derived; drift shown |
| 4 Opex | Done with a limit: hires unloaded |
| 5 Assemble | Done to operating income; tax not done |
| 6 Assumptions | Done, origin marked |
| 7 Flex | Done |
| 8 Targets / prior year | Done; benchmarks and unit economics not done |
| 9 Output | Tables in chat; xlsx on request |

**Data sources:** upload — monthly_profit_and_loss_36m.csv, budget_inputs_2026.md.
