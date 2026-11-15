# Model review — Northbrook Trading Ltd lender model, actuals July–September 2025

Mosofin is not connected, so this run is manual: the model's figures are tied to the source statements you uploaded, every step `[manual]`. (Connecting Mosofin would tie the model straight to the books — docs.mosofin.com. Not raised again.) **I changed nothing in the model; every issue is for the model owner.** This is a review of mechanics and sources, not of whether the assumptions are right.

## (a) Read-back and frozen scope

- **Model:** `model_summary_for_review.csv` — for **the lender**; scope **whole model**; **materiality 10,000** (yours). Entity: **Northbrook Trading Ltd**, single entity (user-asserted), USD. Review date 15 Nov 2025; as-at 30 Sep 2025.
- **Unanswered, defaults applied:** when the model's actuals were extracted — **not supplied** (so STALE cannot be told from FAIL; see below). Known problem areas — none named, so all lines reviewed evenly. Review type: **source tie-out plus the statement checks the summary allows**; formula integrity cannot be reviewed (below).

## (b) Validation of the uploaded files (before any work)

| File | What it actually is | Right company / period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `model_summary_for_review.csv` | **A 5-line extract of the model** (revenue, COGS, cash Jul–Sep 2025; total assets and total L&E Sep only), values only, no formulas | No entity named; Jul–Sep 2025 | Values readable; Jul/Aug totals blank | Steps 2, 4 (tie-out, balance check) | **Accepted with a limit:** an extract, not the XLSX model — **formula integrity (Step 3) and scenarios (Step 5) cannot be reviewed**; "whole model" scope cannot be met |
| `monthly_profit_and_loss_36m.csv` | Source monthly P&L, Oct 2022–Sep 2025 | No entity named; covers the model's months | Foots every month | Step 2 (P&L tie-out), Step 5 (historical ranges) | **Accepted with a limit:** company user-asserted; extraction date unknown |
| `monthly_balance_sheet_36m.csv` | Source month-end balance sheet, same 36 months | No entity named | Balances every month (Sep: 2,713,959 = 2,713,959) | Step 2 (cash, totals), Step 4 | **Accepted with a limit:** company user-asserted |
| `model_summary_for_review_final.csv` | **An employee shift roster** (E08–E10, weeks 1–4) — not a model despite the name | No company, no period | No financial data | No step uses it | **Rejected:** a staff rota. Upload the model workbook instead |

**Still missing (required for the scope you asked for):** **the model workbook itself (XLSX)** with formulas, schedules and scenario controls; the **date the model's actuals were extracted**; recommended: the model-line-to-account mapping.

I would stop here and wait for your answer. *(Assumed answer: "go ahead with the accepted files".)*

## (c) Findings

### Source tie-out (materiality 10,000)

| Model line | Period | Model | Source | Difference | Status |
|---|---|---|---|---|---|
| Revenue | Jul 2025 | 490,900 | 490,900 | 0 | TIED |
| Revenue | Aug 2025 | 477,100 | 477,100 | 0 | TIED |
| **Revenue** | **Sep 2025** | **505,400** | **455,400** | **+50,000** | **FAIL** |
| Cost of goods sold | Jul / Aug / Sep | 294,540 / 286,260 / 273,240 | same | 0 | TIED |
| Cash | Jul / Aug / Sep | 920,237 / 1,016,530 / 1,114,699 | same | 0 | TIED |
| Total assets | Sep 2025 | 2,713,959 | 2,713,959 | 0 | TIED |
| **Total liabilities and equity** | **Sep 2025** | **2,701,959** | **2,713,959** | **−12,000** | **FAIL** |
| Total assets, total L&E | Jul, Aug | blank | 2,624,915 / 2,681,521 | — | **OPEN** (not in the extract) |

Mapping: each model line is a single source line (no aggregation), so the FAILs are not mapping artefacts. Without the extraction date, the September revenue difference could in principle be **STALE** (books changed after extraction) — but a stale figure would usually be lower, not 50,000 higher, and COGS for the same month ties exactly.

### Statement checks (internal to the model)

- **The model's September balance sheet does not balance: assets 2,713,959 vs liabilities and equity 2,701,959 — a 12,000 break.** The source balances, so the break is in the model's liabilities/equity build.
- **September revenue overstated by 50,000 while COGS ties** → the model's September gross margin is **45.9%** ((505,400 − 273,240) ÷ 505,400) against **40.0%** in the books and 40.0–42.0% in every month of the last 36. Any covenant or margin figure for the lender built on September is overstated.
- July and August balance checks: **not testable** (totals blank in the extract).

### Issue log

| ID | Severity | Location | Description | Impact | Suggested fix | Owner | Status |
|---|---|---|---|---|---|---|---|
| 1 | **Critical** | Revenue, Sep 2025 | Model 505,400 vs source 455,400 (+50,000, 5× materiality) | Overstates revenue, gross profit and margin (45.9% vs 40.0%) going to the lender | Re-link Sep revenue to source; confirm actuals vintage | Model owner | Open |
| 2 | **Critical** | Balance sheet, Sep 2025 | Total L&E 2,701,959 ≠ total assets 2,713,959 (12,000 break); source L&E 2,713,959 | Model does not balance | Find the 12,000 missing from liabilities/equity (e.g. RE roll after the revenue change) | Model owner | Open |
| 3 | High | Whole model | Only a values extract was supplied | Formula integrity, links, circularity, hardcodes and scenarios unreviewed | Supply the XLSX model | You | Open |
| 4 | Medium | Balance sheet, Jul–Aug | Totals blank | Balance check untestable for 2 of 3 months | Include totals | Model owner | Open |
| 5 | Medium | Scope | Actuals extraction date unknown | STALE vs FAIL undetermined | State the extraction date | You | Open |

### Call: **HOLD**

Two Critical issues (a material source mismatch and a balance-sheet break) remain, and the scope could not be reviewed in full. **This is not a pass on tabs I did not see.**

## (d) What was not done, and why

- **Step 3 formula integrity and Step 5 scenarios/sensitivities:** no model workbook, only values. **Debt, equity and cap-table ties:** not in the extract.
- **STALE classification:** no extraction date.
- Excel workpaper `Model_Review_Lender model_2025-11-15.xlsx`: not created — say yes if you want it.
- **`model_summary_for_review_final.csv`:** rejected (shift roster). **Nothing in the model or the books was changed.**

## (e) Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, lender model, actuals Jul–Sep 2025, USD — user-asserted. Source: upload (no Mosofin connection). 3 files accepted with a limit; `model_summary_for_review_final.csv` rejected (shift roster) |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 0 done (uploads); 1 done (scope frozen; extraction date missing); 2 done with a limit (13 figures: 10 TIED, 2 FAIL, 2 OPEN period pairs); 3 **not done** (no formulas); 4 done with a limit (Sep balance check only); 5 **not done** (no scenarios; historical GM range 40.0–42.0% recorded); 6 done (5 issues, HOLD); 7 in chat; 8 not offered until results approved |
| Not done | Formula review, scenario review, Jul–Aug balance checks, debt and equity ties (model workbook) |

**Data sources:** user uploads — `model_summary_for_review.csv`, `monthly_profit_and_loss_36m.csv`, `monthly_balance_sheet_36m.csv`.
