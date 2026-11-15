# MD&A — Northbrook Trading Ltd, nine months to 30 September 2025

**DRAFT FOR MANAGEMENT REVIEW.** Mosofin is not connected, so this run is manual: every figure is from the files you uploaded and marked `[manual]`. (Connecting Mosofin would compute the price/volume bridge from invoice lines — docs.mosofin.com. Not raised again.) The narrative is management's; nothing here is published or filed.

## (a) Read-back

- **Company:** Northbrook Trading Ltd (user-asserted). **Period:** nine months to **30 September 2025**. **Currency:** USD.
- **From `mda_drivers.md` (please confirm):** report type **10-K**; sign-off **CFO and counsel**; drivers as listed there; **known trends left for management**; term loan 220,000, no revolver; 2026 capex plan 80,000. **Non-GAAP measures: none named → GAAP only.**
- **Report type vs period conflict:** a 10-K covers a full fiscal year; you have asked for September 2025 (nine months, a 10-Q-type period). **I have drafted the nine-month results and flagged every annual comparison.** Please say which report this is.
- **Comparative:** only the 31 Dec 2024 ledger TB (full year 2024) was uploaded — **not the nine months to Sep 2024, and not the issued 2024 statements.** Comparisons to 2024 below are on a **monthly-average basis, provisional, and not yet checked against what was issued.**

## (b) Validation of the uploaded files (before any work)

| File | What it actually is | Right company / period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `profit_and_loss_2025_ytd.csv` | Monthly P&L Jan–Sep 2025, 13 lines | No entity named; 9 months 2025 | Yes; every line ties to the Sep 2025 TB (differences 0) | Steps 2, 3, 7 (results, seasonality, margins) | **Accepted with a limit:** company user-asserted |
| `trial_balance_2025-09-30.csv` | Trial balance, 33 accounts | No entity named | Foots 6,546,018 = 6,546,018 | Steps 2, 5, 6 (balances, liquidity, estimates) | **Accepted with a limit:** company and period user-asserted |
| `trial_balance_2024-12-31.csv` | Trial balance, same 33 accounts, FY2024 | No entity named | Foots 6,433,544; RE 763,715 + 2024 profit 614,939 = 1,378,654 = Sep 2025 opening RE — ties | Step 3 comparative; Step 5 movements | **Accepted with a limit:** ledger, not the issued statements; full year, not nine months |
| `mda_drivers.md` | Management's drivers, liquidity facts, report type, sign-off | Names no period | Yes | Steps 2–7 (every driver) | **Accepted with a limit:** management-asserted, not evidenced |
| `profit_and_loss_2025_ytd_final.csv` | **An employee shift roster** (E08–E10, weeks 1–4) — not a P&L despite the name | No company, no period | No financial data | No step uses it | **Rejected:** a staff rota. Upload a revised P&L if one exists |

**Still missing:** **nine-month 2024 comparative P&L** and the **issued 2024 financial statements** (required for a like-for-like, checked comparative); prior MD&A (recommended); invoice line detail (price/volume/mix); cash-flow statement.

I would stop here and wait for your answer. *(Assumed answer: "go ahead with the accepted files".)*

## (c) Draft MD&A

### Overview
*[Management: describe the business and the lens used to judge performance.]* Revenue for the nine months was **4,038,600** and net income **594,241** (14.7% of revenue). Significant events visible in the ledger: **term loan reduced 265,000 → 220,000 (45,000 repaid)**; **67,500 debited to Dividends and Adjustments** — management to describe (no dividend is mentioned in your drivers).

### Results of operations (nine months 2025; monthly averages vs FY2024 provisional)

| Line | 9M 2025 | Avg/month 2025 | Avg/month 2024 | Change | Driver | Basis |
|---|---|---|---|---|---|---|
| Revenue | 4,038,600 | 448,733 | 383,133 | **+17.1%** | Volume in Fixings; prices unchanged | **Management-asserted** (no line detail to decompose) |
| Cost of goods sold | 2,370,856 | 263,428 | 222,217 | +18.5% | Steel prices | Management-asserted |
| **Gross margin** | **41.3%** | | 42.0% | **−0.7 pts** | **42.0% every month Jan–Jun; 40.0% Jul–Sep** (computed). Steel price rise not passed on until October (asserted) | Movement computed; cause asserted. Q3 effect ≈ 2 pts × 1,423,400 Q3 revenue = **28,468** of gross profit |
| Payroll | 669,600 | 74,400 | 70,200 | +6.0% | *[driver needed from management]* | — |
| Marketing | 172,474 | 19,164 | 15,325 | +25.0% | 4.0% of revenue Jan–Aug; **Sep 29,146 (6.4%)**, ≈10,930 above run-rate; trade show (asserted) | Computed + asserted |
| Professional fees | 36,500 | 4,056 | 2,500 | +62.2% | **June 16,500 vs 2,500 every other month (+14,000)**; one-time legal fee, contract dispute (asserted) | Recurrence test: no comparable spike in 2025 or in FY2024 (30,000 = 12 × 2,500) — one-time **consistent with the data available** |
| Rent, software, depreciation, insurance, repairs | flat | | | 0.0% | Unchanged monthly amounts | Computed |
| Interest | 10,474 | 1,164 | 1,413 | −17.6% | Lower balance: loan 265,000 → 220,000 | Computed (rate vs balance) |
| **Operating margin** (before interest) | **15.0%** | | 13.7% | +1.2 pts | Operating leverage on revenue growth | Computed |
| Net income | 594,241 | | 614,939 (FY) | | | |

**Seasonality (computed):** revenue rises Jan–Jun (371,000 → 492,200) and falls Jul–Sep (455,400 in Sep); a nine-month figure should not be annualised without that context.

### Liquidity and capital resources
Operating bank balance **1,002,979** (31 Dec 2024: 803,866, +199,113); petty cash 500; Stripe clearing 6,420 (unchanged since December — reconcile). **Debt: term loan 220,000**, repaid at 5,000 a month on the evidence of the balances; **no revolver** (management). Covenants and maturities: *[agreement not supplied]*. Uses: debt service 45,000; Dividends and Adjustments 67,500. **Cash on hand is not the same as available liquidity** — restricted or committed amounts *[management to confirm none]*. No cash-flow statement was supplied, so operating/investing/financing flows are not drafted.

### Critical accounting estimates (scoped and sized; sensitivity is management's)
Inventory **683,100** (up from 495,154; +38.0%) — valuation and obsolescence. Allowance for doubtful accounts **9,000, unchanged**, while receivables rose 602,143 → 798,360: coverage **1.13%** (from 1.49%). No goodwill, no tax accounts, no stock compensation in the TB. Investment in Northbrook UK Ltd 104,800 — impairment judgement if relevant.

### Known trends and uncertainties — questions for management (nothing authored here)
1. Will the October steel price pass-through restore the 42% gross margin, fully or partly?
2. Is Fixings volume growth expected to continue; any customer concentration?
3. Was the September trade show a one-off?
4. Is the contract dispute behind the June fee resolved, or is a contingency disclosure needed?

### Forward-looking statements log (each needs safe-harbour language and counsel review)

| # | Statement | Source | Status |
|---|---|---|---|
| F1 | Capex of 80,000 in 2026 for a second packing line | `mda_drivers.md` (management) | Flagged; for CFO and counsel |
| F2 | Steel price increase passed on from October | `mda_drivers.md` — partly a post-period fact | Flagged; confirm wording |

### Consistency checks
P&L lines tie to the TB (all 12 lines, difference 0); RE rolls 2024 → 2025; percentages recomputed. **Not done:** comparative vs issued statements; narrative vs notes.

## (d) What was not done, and why
- **Like-for-like comparative and the check against issued 2024 statements:** not uploaded. **Price/volume/mix bridge:** no invoice lines — "volume, prices unchanged" stays management-asserted. **Cash-flow drivers:** no cash-flow statement. **Off-balance-sheet and market risk:** no FX balances or floating-rate debt visible; confirm.
- Workpaper `MDA_2025_Northbrook Trading Ltd`: not created — say yes if you want it.
- **`profit_and_loss_2025_ytd_final.csv`:** rejected (shift roster). **Nothing was published, filed or changed.**

## (e) Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, nine months to 30 Sep 2025, USD — user-asserted. Source: upload (no Mosofin connection). 4 files accepted with a limit; `profit_and_loss_2025_ytd_final.csv` rejected (shift roster) |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 0 done (uploads); 1 done (10-K vs 9-month conflict flagged); 2 done; 3 done with a limit (drivers asserted, comparative provisional); 4 N/A (no non-GAAP); 5 done with a limit (balances only); 6 done (scoped, sized); 7 questions only; 8 done with a limit; 9 in chat; 10 not offered until results approved |
| Not done | Comparative vs issued 2024 statements (issued statements, 9M 2024 P&L); revenue bridge (invoice lines); cash-flow analysis (cash-flow statement) |

**Data sources:** user uploads — `profit_and_loss_2025_ytd.csv`, `trial_balance_2025-09-30.csv`, `trial_balance_2024-12-31.csv`, `mda_drivers.md`.
