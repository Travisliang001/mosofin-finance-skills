# Standard cost variances — Northbrook Trading Ltd — September 2025

Mosofin is not connected, so this run is manual: every step is `[manual]` and every figure comes from your uploads. Connecting Mosofin would let the actual side and the variance accounts be read directly ([docs.mosofin.com](https://docs.mosofin.com)).

## Read-back (Stage 1)

Analysing standard cost variances for **Northbrook Trading Ltd** (user-asserted) for **September 2025**, currency **USD** (user-asserted; no file states a currency), with actuals and standards **from the files you uploaded**. Standards: SB-20 price **20.00, set 1 Aug 2023**; usage 2.0 units and labour 0.5 h at 44.00/h, **set 1 Jan 2024**. Production volume **5,200 units** and purchases **11,000 units** are taken from `standard_costs.csv` (facts that arrived inside a file; used once you confirm them here). Scrap: not supplied. Valuation policy (E): **not answered** — variances reported, treatment review not run. Overhead basis (F): **not answered** — and no overhead data was supplied at all. Go-ahead assumed.

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Needed for | Verdict |
|---|---|---|---|---|---|
| `standard_costs.csv` | Standards table with effective dates, plus September actual price, usage, labour rate and hours per unit, units produced and purchased (6 rows) | No entity or currency; column `actual_2025-09` matches the period | Yes. Actuals are per-unit summary figures, not a cost listing | Steps 1–3 | **Accepted with a limit**: company user-asserted; actual labour rate/hours and usage are user-supplied summaries, not evidenced by a payroll or production listing |
| `inventory_purchases_2025-09.csv` | Purchase listing, 4 lines, 4–21 Sep 2025: SB-20 11,000 units at 22.50 (247,500), C-12 90 at 26.00 (2,340), FX-01 600 at 35.00 (21,000); total 270,840 | No entity, currency or vendor | Yes; SB-20 quantity 11,000 agrees to "Units purchased" | Step 2 PPV (quantity purchased), Step 4 | **Accepted with a limit**: company user-asserted; no vendor column, so no supplier analysis; C-12 and FX-01 have no standard |
| `variance_account_history.csv` | Monthly PPV posted, unfavourable, Oct 2024 – Sep 2025 (12 months) | No entity named | Yes | Step 0 (one-sidedness, last reset) | **Accepted with a limit**: company user-asserted; amounts posted per month, not balances, so clearing (Test 0b) cannot be tested |
| `standard_costs_final.csv` | **An employee shift rota** (E08–E10, weeks 1–4: days / nights / off). Not a standards file despite its name | None | n/a | No step uses it | **Rejected.** If a revised standards file exists, please upload it in its place |

**Still missing:** overhead actuals and overhead rates (required for the four overhead variances — not run); scrap data; a variance account balance listing (for the clearing test); standards for C-12 and FX-01.

## Findings

**1. The PPV is a stale standard, not a purchasing problem (Step 0, Test 0c/0d).** PPV has been **unfavourable in 12 of the last 12 months**, rising every month by about 1,682, from **9,000 (Oct 2024) to 27,500 (Sep 2025)** — 3.06 times in a year; 219,000 in total. The SB-20 standard of 20.00 was set on **1 Aug 2023** and no reset appears anywhere in the series. September's actual price of 22.50 is **12.5% above standard**; September PPV is 11.1% of SB-20 purchase value. This pattern is consistent with a standard price drifting further from the market, not with purchasing performance. The standard needs reviewing — that decision is yours; no new standard is proposed from actuals.

**2. Variances for September (Step 2).** Direction and amount only; no performance verdict.

| Variance | Formula | Amount | Direction |
|---|---|---:|---|
| Material price (PPV), SB-20 | (22.50 − 20.00) × 11,000 **purchased** | 27,500 | Unfavourable |
| Material usage | (10,920 used − 10,400 allowed) × 20.00 | 10,400 | Unfavourable |
| Labour rate | (46.00 − 44.00) × 2,496 actual hours | 4,992 | Unfavourable |
| Labour efficiency | (2,496 − 2,600 allowed for actual output) × 44.00 | 4,576 | Favourable |
| Overhead (all four) | — | **not computed** | No overhead data |
| **Net of the four computed** | | **38,316** | Unfavourable |

Quantity used (10,920) = 2.1 × 5,200 and actual hours (2,496) = 0.48 × 5,200 are derived from your per-unit actuals; standard quantities are for the **actual** output of 5,200. September PPV computed here (27,500) **agrees exactly** to the PPV posted in September in the history file.

**3. Bridge, standard to actual (Step 3).**

| | Amount |
|---|---:|
| Standard cost of actual output: materials 10,400 × 20 = 208,000; labour 2,600 h × 44 = 114,400 | 322,400 |
| + Material PPV / usage / labour rate / labour efficiency | +27,500 / +10,400 / +4,992 / −4,576 |
| + Stock build at standard: 11,000 purchased − 10,920 used = 80 units × 20 | +1,600 |
| = Bridged actual | **362,316** |
| Actual: SB-20 purchases 247,500 (purchase listing) + labour 2,496 h × 46 = 114,816 | **362,316** |
| Residual | **0** |

Caution: only the 247,500 material side is evidenced by a listing. Labour actual cost is rebuilt from your per-unit figures, so the labour half ties by construction and is **not** a cross-system tie. Overhead is outside the bridge entirely. C-12 (2,340) and FX-01 (21,000) purchases carry no standard and are excluded, not forced in.

**4. Root causes (Step 4) — hypotheses only.** Supplier price: SB-20 at 22.50 on both September buys; the listing has no vendor, so which supplier and when the price moved cannot be shown. Usage of 2.1 against 2.0 may include scrap; scrap was not supplied, so this cannot be separated. Labour rate 46 against a January 2024 rate of 44 may also be an un-reset standard; one month of data cannot tell. Learning curve, downtime and mix: not in the data.

**5. Accounting treatment (Step 5).** Policy not given, so no treatment review. Flag: if adverse PPV is being capitalised into inventory, a 20.00 standard against a 22.50 market would carry SB-20 stock **below** actual cost, with the 12.5% gap sitting in variance; how it is closed matters. Illustrative proposal only — **PROPOSED, NOT POSTED**: DR Purchase price variance 27,500 / CR Inventory or AP 27,500; DR Usage variance 10,400 / CR WIP 10,400. Account names are captions; no chart of accounts was supplied.

## What was not done, and why

- **Overhead variances (all four)**: no overhead actuals, rates or basis supplied.
- **Test 0a/0b, variance accounts exist and clear**: needs a chart of accounts and variance account balances; the history shows postings only.
- **Supplier root cause**: purchase listing has no vendor.
- **Scrap / yield split**: no scrap data. **Mix**: one product only.
- **C-12 and FX-01 variances**: no standards.
- **Treatment review, NRV exposure**: valuation and capitalisation policy not given.
- **Workpaper**: shown as tables; say if you want `Standard_Costing_Variances_2025-09_NorthbrookTradingLtd.xlsx`.
- **Posting, operational actions**: nothing posted, sent or changed; operational decisions are yours.

## Coverage and provenance (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, September 2025, USD — **user-asserted**. Data source: **upload**. Quantities: user-supplied per-unit figures (not a production listing). Standards: SB-20 price 1 Aug 2023; usage, labour 1 Jan 2024. Files: `standard_costs.csv` accepted with limit; `inventory_purchases_2025-09.csv` accepted with limit; `variance_account_history.csv` accepted with limit; `standard_costs_final.csv` **rejected** (shift rota) |
| Capability map | Not applicable: no connection. Every task is `[manual]`. |
| Steps | 0: 0c/0d done (PPV only), 0a/0b **not done**; 1 done (standards recorded with dates); 2 done for materials and labour, overhead **not done**; 3 done, labour half ties by construction; 4 hypotheses only; 5 **not done** (no policy) |
| Not done | Variance clearing, chart check, GL tie of actual cost, overhead — need GL variance balances, chart of accounts, overhead actuals |
| Parameters | Standards as above with dates; period Sep 2025; quantities from `standard_costs.csv`; overhead basis unknown; freight and duty treatment unknown |
