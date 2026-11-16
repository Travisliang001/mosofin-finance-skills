# MD&A draft — Northbrook Trading Ltd — period to 30 September 2025

**DRAFT FOR MANAGEMENT REVIEW.** Mosofin is not connected, so this run is manual: every figure comes from your uploads and every step is `[manual]`. (Connecting Mosofin would automate the reads: [docs.mosofin.com](https://docs.mosofin.com).)

## Read-back

Drafting MD&A for **Northbrook Trading Ltd** (user-asserted) for the **period to 30 September 2025**, in **USD**, report type **10-K** as you stated, from **your uploads**. Drivers as given in `mda_drivers.md` (management-asserted); known-trends section **left for management**; liquidity from balances plus the term-loan figure and capex plan you supplied; non-GAAP measure: Adjusted EBITDA as you defined it. Sign-off: **CFO and counsel**.

**Assumption to confirm (conservative reading):** a 10-K covers a full fiscal year, and the 2024 trial balance shows a 31 December year-end (it carries twelve months of P&L). A 30 September 2025 period is nine months, which is a 10-Q interim. I have drafted it as a **nine-month interim** narrative with September-month detail; confirm the report type before this goes further.

## Validation of the uploads (shown before any work — I would wait for your answer here)

| File | What it actually is | Company / period | Usable? | Step that uses it | Verdict |
|---|---|---|---|---|---|
| `profit_and_loss_2025_ytd.csv` | Monthly P&L, Jan–Sep 2025, 12 expense/revenue columns + net income | No entity or currency named; months 2025-01..2025-09 | Every month foots (revenue − costs = net income, 0 difference); YTD totals agree to the Sep TB line by line | Step 3 results, Step 7 seasonality | **Accepted with a limit:** company and currency user-asserted; no product/customer line detail, so no price/volume/mix bridge |
| `profit_and_loss_2025_ytd_final.csv` | **Not a P&L.** A staff shift roster: employee E08–E10 by week (days / nights / off) | No entity, no period, no money | Nothing financial in it | None | **Rejected:** the content is a rota, despite the name. If a "final" P&L exists, upload the real file |
| `trial_balance_2025-09-30.csv` | Trial balance at 30 Sep 2025, 33 accounts | No entity named; date in name only | Debits = credits = 6,546,018 | Steps 3, 5, 6 | **Accepted with a limit:** company user-asserted |
| `trial_balance_2024-12-31.csv` | Trial balance at 31 Dec 2024, full-year 2024 P&L | No entity named | Debits = credits = 6,433,544; 2024 NI 614,939 rolls into 2025 opening retained earnings 1,378,654 exactly | Comparative, Step 5 cash flow | **Accepted with a limit:** it is a **full year**, not nine months to Sep 2024; not checked against the issued 2024 statements |
| `mda_drivers.md` | Management's drivers, non-GAAP definition, loan, capex, sign-off | Northbrook, 2025 | Readable | Steps 3, 4, 5, 7 | **Accepted:** every driver is labelled management-asserted |

**Still missing:** (1) a nine-months-to-30-Sep-2024 comparative P&L, (2) the issued 2024 statements to check the comparative against, (3) invoice line detail by product (Fixings vs other) for a revenue bridge, (4) prior MD&A (recommended), (5) facility agreement / covenant terms, (6) consolidated figures — the TB shows an **Investment in Northbrook UK Ltd (104,800)** and an **intercompany payable (38,000)**, so a filed MD&A would be on the group, not this entity alone.

*Proceeding as if you answered "go ahead with the accepted files".*

## 1. Overview (headline results — computed)

| | 9M 2025 | FY 2024 | Monthly avg 2025 vs 2024 |
|---|---|---|---|
| Revenue | 4,038,600 | 4,597,600 | 448,733 vs 383,133 (+17.1%) |
| Gross profit | 1,667,744 (41.3%) | 1,930,992 (42.0%) | margin −0.7 pt |
| Net income | 597,741 (14.8%) | 614,939 (13.4%) | |

The only comparative supplied is a full year, so 9M 2025 vs FY 2024 is **not** like-for-like; the monthly-average column is a derived indicator, not a period-over-period comparison. Significant events traced in the ledger: term loan repaid 45,000 (5,000 a month); 67,500 debited to *Dividends and Adjustments* (nature to confirm); no capex (fixed-asset cost unchanged at 420,000); no new debt or equity.

## 2. Results of operations

**Revenue.** Grew each month from 371,000 (Jan) to 492,200 (Jun), then **fell three months running** to 455,400 in September (−7.5% from June; Sep vs Aug −21,700, −4.5%). *Management states* growth came from volume in Fixings with prices unchanged — **management-asserted**; no line detail was supplied, so price/volume/mix cannot be computed. The Q3 decline has no driver given — **reason needed from management**.

**Gross margin.** Exactly 42.0% Jan–Jun, exactly 40.0% Jul–Sep. The 2-point drop cost **28,468** of gross profit in Q3 (2% × 1,423,400 revenue). *Management states* steel prices rose and were not passed on until October — management-asserted. ▶ **[FORWARD-LOOKING — flag]** "passed on in October" describes post-period pricing; keep only with sign-off.

**Operating expenses.**
- Payroll 669,600; monthly run-rate up from 72,800 to 76,000 (2024 average 70,200). Driver needed (headcount or pay).
- Marketing 172,474, steady at 4.0% of revenue except September: 29,146 (6.4%), **10,930** above the 4% run-rate. *Management:* September trade show — management-asserted.
- Professional fees 36,500 vs a 2,500 monthly run-rate: June 16,500 includes **14,000** *management describes* as a one-time legal fee (contract dispute).
- **Software is nil in September** against 3,500 every other month (YTD 28,000 = 8 × 3,500). Likely a missed bill or accrual of about 3,500; confirm before figures are final.
- Rent 81,000, insurance 13,500, repairs 4,500, depreciation 37,800, bank fees 16,155 (0.4% of revenue every month): run-rate, no driver needed.

**Interest.** 10,474, falling monthly with the balance; effective rate ≈ 5.7% on the amortising loan (computed).

**Tax.** **No income-tax expense or liability appears in either trial balance.** For a 10-K filer this needs explaining (exemption, loss carry-forwards, or an omitted provision) before drafting a tax line.

**September month:** net income 56,423 vs 71,956 in August (−21.6%), from lower revenue, the lower margin and the trade show.

## 3. Non-GAAP measure — Adjusted EBITDA (GAAP net income shown first)

| Net income (GAAP) | 597,741 |
|---|---|
| + Interest | 10,474 |
| + Depreciation | 37,800 |
| = EBITDA | 646,015 |
| + Professional fees described as one-time (June) | 14,000 |
| **= Adjusted EBITDA** | **660,015** |

Definition is management's. Recurrence test: in 2024 professional fees were 30,000 = 12 × 2,500 with no spike, so the add-back appears **once in the two periods available** (monthly 2024 detail would confirm). No tax add-back is in the definition, consistent with no tax line.

## 4. Liquidity and capital resources

Cash 1,006,479 operating account + 500 petty cash (+202,613 on 31 Dec 2024); Stripe clearing 6,420. Derived cash-flow (indirect, from the two TBs): operating **+315,113** (NI 597,741 + depreciation 37,800 − receivables 196,217 − inventory 187,946 + payables 61,935 + accruals 1,800); investing **0**; financing **−112,500** (loan −45,000, dividends/adjustments −67,500). Ties to the cash movement exactly.

Working capital absorbed 320,428: receivables **+32.6%** and inventory **+38.0%** against revenue growth of 17% on a run-rate basis; days sales ≈ 54, days inventory ≈ 79 (9-month basis). Driver needed.

Debt: term loan **220,000** — agrees to the TB and to your statement; no revolver (management). Maturity, rate terms and covenants not supplied → **covenant status not stated**. Capex: ▶ **[FORWARD-LOOKING — flag]** *management plans 80,000 in 2026 for a second packing line* (source: drivers file). Cash on hand is not all available liquidity: restrictions, cash held for the UK subsidiary and the 38,000 intercompany payable are not confirmed. The twelve-month sufficiency statement is **not drafted** — management's to make.

## 5. Critical accounting estimates (scoped and sized; sensitivity `[manual]`)

- **Allowance for credit losses:** 9,000, unchanged while receivables grew 32.6%; coverage fell from 1.49% to 1.13%. Judgement and sensitivity needed.
- **Inventory valuation:** 683,100, up 38%, with input costs rising — net-realisable-value judgement.
- **Investment in Northbrook UK Ltd:** 104,800 at cost — impairment / consolidation question.
- **Income tax:** see the nil provision above.
No goodwill, intangibles or derivatives in the TB, so those estimates do not arise here.

## 6. Known trends and uncertainties — for management to write

Questions: Will the steel cost increase persist, and was the October price rise achieved? Why did revenue fall from June to September, and is that seasonal? (Only nine months of history — seasonality cannot be measured.) Customer concentration? Any FX exposure through the UK subsidiary? Rate exposure on the term loan? Safe-harbour language and legal review by counsel.

## Forward-looking statements log

| # | Statement | Source | Status |
|---|---|---|---|
| 1 | Steel cost increase passed on from October | mda_drivers.md | Flag for CFO / counsel |
| 2 | 2026 capex 80,000, second packing line | mda_drivers.md | Flag for CFO / counsel |

## Not done, and why

Revenue bridge (no line detail); like-for-like nine-month comparison (no 9M 2024 figures); comparative checked against issued 2024 statements (not supplied); consolidated narrative and intercompany elimination (UK subsidiary figures not supplied); covenant compliance (no agreement); sensitivity of each estimate (management's); Excel workpaper (I would ask before creating `MDA_2025_Northbrook Trading Ltd.xlsx`). Nothing was posted, sent or changed.

## Coverage sheet (manual run)

| Section | Entry |
|---|---|
| Environment | Northbrook Trading Ltd, 9M to 30 Sep 2025, USD — user-asserted; source: upload (Mosofin not used, by choice) |
| Files | P&L YTD accepted with limit; `_final.csv` rejected (shift roster); TB Sep 2025 accepted with limit; TB Dec 2024 accepted with limit (full year, unverified against issued); drivers accepted (management-asserted) |
| Capability map | Not applicable: no connection. Every task is `[manual]`. |
| Steps | 1 structure done with limit (report type to confirm); 2 overview done; 3 results done with limit (no bridge); 4 non-GAAP done; 5 liquidity done with limit (no terms); 6 estimates scoped, sensitivity not done; 7 left for management; 8 tie-out done (P&L = TB every line; TBs balance; RE rolls); 9 tables in chat |
| Not done | Comparative vs filed 2024; 9M 2024 comparison; consolidation; covenants; revenue bridge |

**Data sources:** uploads — `profit_and_loss_2025_ytd.csv`, `trial_balance_2025-09-30.csv`, `trial_balance_2024-12-31.csv`, `mda_drivers.md` (management-asserted).
