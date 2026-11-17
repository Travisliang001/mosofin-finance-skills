# Standard cost variances — Northbrook Trading Ltd, September 2025

Mosofin is not connected, so this run is manual, from the files you uploaded.

## (a) Read-back

> Analysing standard cost variances for **Northbrook Trading Ltd** for **September 2025**, in **USD**, with actuals and standards from **your uploaded files**. Material standards **set 1 August 2023**, labour standards **set 1 January 2024**. Production data supplied (5,200 units). Shall I go ahead?

Not answered at intake, with the skill's default applied:

- **Valuation policy and variance capitalisation (E):** not stated. Variances are reported; the **accounting treatment review is not run** and no entry is proposed.
- **Overhead rates and basis (F):** not stated, and no overhead actuals were uploaded. **No overhead variance is computed**, not even as one total.
- **Scrap and runs (D, part):** not supplied. Usage is taken from the per-unit figures in the standards file.
- **Bill of materials / routings beyond one material and one labour line:** not supplied; only what is in the file is used.

## (b) Validation of the uploaded files (before any work)

| File | What it actually is | Right company / period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `standard_costs.csv` | Standards table (price, usage, labour rate, labour hours, each with a set-on date) with a September 2025 actual beside each, plus units produced (5,200) and units purchased (11,000) | No company or currency in the file; actuals column is labelled 2025-09 | Yes. Four standards with dates. Actuals are single summary figures, not ledger detail. | Yes — Steps 1-3 | **Accepted with a limit**: actuals are summary figures I cannot trace to transactions |
| `inventory_purchases_2025-09.csv` | Purchase listing, 4 lines, date / sku / qty / unit_cost, 4-21 Sep 2025 | No company or currency; all dates in September 2025 | Yes — but it **disagrees with the standards file** (see findings): 5,500 units of SB-20, not 11,000. SKUs C-12 and FX-01 have no standard. | Yes — Step 2 price variance and Step 4 price evidence | **Accepted with a limit**: no vendor column, so no supplier analysis; two SKUs cannot be measured |
| `variance_account_history.csv` | Purchase price variance by month, Oct 2024 - Sep 2025, one column | No company, currency, account number or sign convention; 12 months ending in the period | Yes for the pattern. Not stated whether each figure is the month's variance or the account balance. | Yes — Step 0 (health of the standards) | **Accepted with a limit**: purchase price variance only; no usage, labour or overhead variance accounts shown |
| `standard_costs_final.csv` | **Not a standards file.** Columns employee, week_1..week_4 with nights / days / off — a staff shift rota | No company, dates, items or costs | No | No step uses it | **Rejected** on content. Set aside; `standard_costs.csv` is used. If a later standards file exists, upload it. |

**Still missing:** overhead actuals and rates; labour cost from payroll or the ledger; opening and closing SB-20 stock; vendor on each purchase; the valuation policy; confirmation of which purchase quantity is right (11,000 or 5,500).

I would wait here for your answer. *(Assumed answer: "go ahead with the accepted files".)*

## (c) Findings

### Step 0 — Health of the standards (read this before the variances)

- **A variance account exists** (purchase price variance), so standard costing is in operation for materials. No other variance account was supplied.
- **The purchase price variance has pointed the same way in 12 of the last 12 months and grown every month**: 9,000 in October 2024 rising by exactly 900 a month to 18,900 in September 2025 — more than double. Twelve months total 167,400. No step change appears anywhere in the series, so **no standard reset is visible in the last twelve months**.
- **The SB-20 standard price of 20.00 was set on 1 August 2023, 26 months ago.** September's actual is 22.50, 12.5% above it.
- **This pattern is consistent with a stale standard that is drifting further from current prices, not with purchasing performance.** It is the same price gap being reported again each month. I am not attributing it to a supplier or to any person; the file has no vendor or currency detail to test either.
- **Clearing:** if the monthly figures are balances rather than movements, the account is growing and has not been closed; the file does not say which. Please confirm.
- Labour standards were set on 1 January 2024 (21 months ago); no labour variance history was supplied, so one-sidedness cannot be tested there.

### Step 2 — Variances for September 2025 (direction and amount; positive = actual above standard)

| Variance | Working | Amount |
|---|---|---:|
| Material price (PPV), on quantity **purchased** | (22.50 − 20.00) × 11,000 | **27,500** |
| Material usage, on quantity **used** | (10,920 used − 10,400 allowed) × 20.00 | **10,400** |
| Labour rate | (46.00 − 44.00) × 2,496 actual hours | **4,992** |
| Labour efficiency | (2,496 − 2,600 allowed) × 44.00 | **(4,576)** |
| Overhead (all four) | not run — no data | — |
| **Total computed** | | **38,316** |

Quantities: used 2.1 × 5,200 = 10,920; allowed 2.0 × 5,200 = 10,400; actual hours 0.48 × 5,200 = 2,496; hours allowed for actual output 0.5 × 5,200 = 2,600.

### The purchase figures do not agree with each other

| Source | SB-20 quantity | Price | PPV |
|---|---:|---:|---:|
| Standards file summary | 11,000 | 22.50 | 27,500 |
| Purchase listing (4,000 @ 22.15 + 1,500 @ 23.40 = 123,700) | 5,500 | 22.49 average | 13,700 (8,600 + 5,100) |
| Variance account, September 2025 | — | — | 18,900 |

Three different figures for the same variance. The listing shows exactly half the summary's quantity. I have not chosen between them or adjusted any: the table above uses the summary file because the other variances come from it, and **the PPV is 13,700 if the purchase listing is the complete record**. Neither equals the 18,900 in the variance account. This needs your answer before the PPV is relied on.

Within the listing, the SB-20 price rose from 22.15 on 4 September to 23.40 on 15 September (+5.6% in eleven days) — the gap to standard is still widening.

**C-12 (90 @ 26.00 = 2,340) and FX-01 (600 @ 35.00 = 21,000) have no standard in the file.** No variance is computed for them and no standard is inferred.

### Step 3 — Bridge from standard to actual (materials and labour only)

| | USD |
|---|---:|
| Standard cost of 5,200 units: materials 10,400 × 20.00 = 208,000; labour 2,600 × 44.00 = 114,400 | 322,400 |
| + PPV 27,500 + usage 10,400 + rate 4,992 − efficiency 4,576 | 38,316 |
| + 80 units bought but not used (11,000 − 10,920), at standard 20.00 | 1,600 |
| **= Actual cost incurred**: materials 11,000 × 22.50 = 247,500; labour 2,496 × 46.00 = 114,816 | **362,316** |
| Residual | 0 |

The bridge ties on the summary figures because both ends come from the same file; it is arithmetic, not a tie to the ledger. No ledger cost was supplied, so the genuine cross-check is **not done**. Against the purchase listing the materials end does not tie (5,500 units bought against 10,920 used — possible only if at least 5,420 units came from opening stock, which was not supplied).

### Step 4 — Cause hypotheses (labelled as hypotheses)

1. **PPV: stale standard.** 26-month-old price, one-sided for 12 months and growing 900 a month. A price review of the SB-20 standard is indicated; the new standard is your decision and is not set from recent actuals here.
2. **Usage 10,400:** 2.1 units used per finished unit against 2.0 (5% over). The usage standard is the same age. Scrap or yield cannot be tested — no scrap data.
3. **Labour:** rate 4.5% above a 21-month-old standard; hours 4% below standard. The two nearly offset (net 416). Cause not in the data.
4. **FX:** purchase currency not shown; an FX effect inside the PPV cannot be ruled out.

## (d) What was not done, and why

- **Overhead variances (spending, efficiency, volume):** no rates, basis or actuals supplied.
- **Accounting treatment review and proposed entries:** valuation and capitalisation policy not stated; no entry proposed.
- **Supplier price analysis:** no vendor on the purchase listing.
- **Variances for C-12 and FX-01:** no standards supplied; none invented.
- **Tie of actuals to the books:** no ledger or trial balance uploaded; the September PPV of 18,900 in the account is not reconciled to either computed figure.
- **Scrap, mix, downtime:** not supplied.
- **Operational actions:** yours; none recommended.
- **Excel workpaper** (`Standard_Costing_Variances_2025-09_Northbrook Trading Ltd.xlsx`): not created — say yes if you want it.
- **Nothing was posted, sent or changed.**

Parameters: standards as dated above; September 2025; quantities from the standards file; overhead not run; freight and duty treatment unknown.
