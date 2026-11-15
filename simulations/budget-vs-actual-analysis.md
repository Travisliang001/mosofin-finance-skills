# Budget vs actual — Northbrook Trading Ltd, September 2025 (upload path)

Mosofin is not connected, so this run is manual: actuals and budget both come from the files you uploaded. Connecting Mosofin would read both sides from the books, by month ([docs.mosofin.com](https://docs.mosofin.com)). Nothing was revised or posted.

## Read-back and assumptions

Comparing **actuals to budget** for **Northbrook Trading Ltd** (user-asserted), in **USD**: **September 2025 (month), Q3 (Jul–Sep) and year to date (Jan–Sep)**. Unanswered at intake:

| Question | What this run does |
|---|---|
| **Which budget version** | Only one was supplied, `budget_2025.csv`, which carries no version name. It is labelled **"budget_2025 (version unnamed)"** throughout. Please confirm it is the board-approved budget, not a revision. |
| **Fiscal year** | The budget starts in January, so I read the year as **calendar 2025**. QTD = Jul–Sep. |
| **Materiality thresholds** | Not set, and the skill never assumes them. **Every non-zero variance is explained.** Only five lines vary, so the report stays readable. |
| **Prior-year actuals** | Not supplied. **No YoY column.** |
| **Known one-time items** | None given. |

## Validation of the upload (shown before any work)

| File | What it actually is | Company / period | Usable? | Used by | Verdict |
|---|---|---|---|---|---|
| `profit_and_loss_2025_ytd.csv` | Monthly P&L actuals, Jan–Sep 2025, 10 lines + net income. Net income recomputes every month. YTD revenue **4,038,600**, net income **605,615** | No company or currency in the file | Yes | Steps 1–8 (actual side) | **Accepted with a limit**: company user-asserted |
| `budget_2025.csv` | Monthly budget, Jan–Sep 2025, same 10 lines (no net income column). YTD revenue **4,159,758** | No company, currency or version name. **Covers January–September only** | Yes, for month, Q3 and YTD | Steps 1–8 (budget side) | **Accepted with a limit**: version unnamed; **no Q4 budget**, so no full-year comparison |
| `profit_and_loss_2025_ytd_final.csv` | **Not a P&L.** A staff shift rota: E08–E10, week_1…week_4, "nights / days / off" | No amounts or dates | No | No step | **Rejected** on content. The name suggests final YTD actuals. Upload them if they exist; otherwise the actuals above are used. |

**Still missing:** the budget version name; the **Oct–Dec 2025 budget** (for the full-year outlook); prior-year actuals (YoY); materiality thresholds; driver data (units, prices) to split revenue into volume and price.

*Here I would stop and wait for your answer. Assumed answer: "go ahead with the accepted files".*

**Alignment check (Step 1):** same 10 lines on both sides, no account in one and not the other, same months, currency taken as USD on both. Budget net income was computed from its lines. The budget is phased by month (not annual ÷ 12): revenue and marketing follow the season.

## Variance summary (F = favourable, U = unfavourable)

| Line | Sep actual | Sep budget | Var $ | Var % | | Q3 var $ | YTD actual | YTD budget | YTD var $ | YTD % | |
|---|---:|---:|---:|---:|:-:|---:|---:|---:|---:|---:|:-:|
| Revenue | 455,400 | 469,062 | (13,662) | −2.9% | **U** | (42,702) | 4,038,600 | 4,159,758 | (121,158) | −2.9% | **U** |
| Cost of sales | 273,240 | 267,775 | 5,465 | +2.0% | **U** | 17,081 | 2,370,856 | 2,323,438 | 47,418 | +2.0% | **U** |
| Gross profit | 182,160 | 201,287 | (19,127) | −9.5% | **U** | (59,783) | 1,667,744 | 1,836,320 | (168,576) | −9.2% | **U** |
| Gross margin | 40.0% | 42.9% | −2.9 pts | | **U** | | 41.3% | 44.1% | −2.8 pts | | **U** |
| Marketing | 29,146 | 18,216 | 10,930 | +60.0% | **U** | 10,930 | 172,474 | 161,544 | 10,930 | +6.8% | **U** |
| Payroll, rent, software, prof. fees, bank fees, depreciation | 97,022 | 97,022 | 0 | 0% | — | 0 | 872,555 | 872,555 | 0 | 0% | — |
| **Operating income** | **55,992** | **86,049** | **(30,057)** | **−34.9%** | **U** | **(70,713)** | **622,715** | **802,221** | **(179,506)** | **−22.4%** | **U** |
| Interest | 1,900 | 1,900 | 0 | 0% | — | 0 | 17,100 | 17,100 | 0 | 0% | — |
| **Net income** | **54,092** | **84,149** | **(30,057)** | **−35.7%** | **U** | **(70,713)** | **605,615** | **785,121** | **(179,506)** | **−22.9%** | **U** |

Operating margin: September 12.3% against 18.3% budget; YTD 15.4% against 19.3%.

## Commentary

**1. Revenue: 121,158 (2.9%) U YTD, the same 2.9% in every month.**
Revenue has come in 2.91% under budget in each of the nine months, with no catch-up. That pattern points to a **permanent** gap, not timing. The uniform shortfall would fit a planned price rise that did not happen (budget ≈ actual × 1.03 every month), but **the cause is not evidenced**: no unit or price data was supplied. Cause **to be confirmed**; owner: sales lead.

**2. Cost of sales and gross margin: 168,576 U on gross profit YTD, mostly from margin rate, not volume.**
- Lower revenue at the budgeted margin explains **53,485** of the gross-profit shortfall (volume).
- The other **115,091** is a **cost rate** effect. Cost of sales ran at **58.0%** of revenue in Jan–Jun (budget 55.2%) and **60.0%** from July (budget 57.1%).
- The budget itself stepped up in July, so a cost increase was expected, just a smaller one. The gap has held at about 2.9 points every month. **Permanent** unless supplier terms change.
- Cause to be confirmed: purchasing / supplier pricing. Owner: operations.

**3. Marketing: 10,930 (60%) U in September only.**
Every other month equals budget to the dollar. September is 29,146 against 18,216, so marketing was 6.4% of revenue against a usual 4.0%. A single-month spike is likely a **one-off or timing** item. The ledger detail was not supplied, so the transactions cannot be named. Cause **to be confirmed**; owner: marketing.

**4. No other variance.** Payroll, rent, software, bank fees, depreciation and interest equal budget in every month. **June professional fees of 16,500** (14,000 above the usual 2,500) were **budgeted**, so they show no variance. Note it as a known one-off when comparing run-rates.

## Full-year implication (arithmetic only, not an agreed outlook)

At the YTD run-rate, the revenue gap (2.9%) and the margin gap (about 2.9 points) are worth about **20,000 of operating income a month**, before any marketing one-off. Q3 averaged 19,928 a month excluding the September marketing excess. **The full-year effect cannot be measured against budget**, because no Oct–Dec budget was supplied. Both main variances look permanent, so a re-forecast in `rolling-forecast` is worth considering once Q4 is known.

## Not done, and why

- Revenue split into volume, price and mix: no units or prices.
- YoY column: no prior-year actuals.
- Materiality filter: no thresholds, so everything non-zero is explained.
- Full-year outlook vs budget: no Q4 budget.
- Naming the transactions behind the marketing spike: no ledger detail.
- Excel report `BvA_Analysis_2025-09_Northbrook Trading Ltd.xlsx`: not created. Would you like it?

## Coverage sheet (manual run)

**Environment:** Northbrook Trading Ltd, Sep 2025 / Q3 / YTD, USD, all user-asserted. Budget compared to: **budget_2025 (version unnamed)**. Data source: upload, because the Mosofin gateway is absent. Actuals and budget accepted with limits; rota rejected.
**Capability map:** Not applicable: no connection. Every task is `[manual]`.

| Variance | Status | Cause confirmed? | Gap and owner |
|---|---|---|---|
| Revenue (121,158 U YTD) | Computed, F/U labelled | **No: to be confirmed** | Units and prices; sales lead |
| Cost of sales / margin (115,091 rate, 53,485 volume) | Computed and split | **No: to be confirmed** | Supplier pricing; operations |
| Marketing (10,930 U Sep) | Computed | **No: to be confirmed** | Ledger detail; marketing |

Steps: 1 alignment done; 2–4 done (no thresholds); 5 decomposition done for margin, **not done** for revenue; 6 timing vs permanent proposed, for you to confirm; 7 **not done** vs full-year budget; 8 commentary drafted with causes open; 9 tables in chat.

**Data sources:** upload — profit_and_loss_2025_ytd.csv, budget_2025.csv.
