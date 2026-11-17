# Tax projection — Northbrook Trading Ltd — Sampleland corporate tax, tax year 2025

Mosofin is not connected, so this run is manual: every step is `[manual]` and every figure comes from your uploads. **This is a computation for a qualified tax professional to review, not tax advice.** Nothing is filed, paid or posted.

## Read-back

Projecting **2025 corporate income tax** for **Northbrook Trading Ltd** (user-asserted), taxpayer the company, jurisdiction **'Sampleland'**, calendar tax year 2025, in USD, on **nine months of actuals** (Jan–Sep 2025, uploaded P&L) plus **your forecast for Oct–Dec 2025**. Rates from **'sample rate card v1, tax year 2025'** — the file itself says *fictitious, not real tax law*; used only because you supplied it, and labelled as such throughout.

| Intake question | Treatment |
|---|---|
| C — rates and rules | Answered by `tax_rates_and_rules_SAMPLE.md` (source and year stated). Confirm it is the card you mean. |
| D — rest of year | Answered by the forecast file (Oct–Dec 2025 used; 2026 months not needed for this tax year). |
| E — book-to-tax adjustments / safe harbour | Safe harbour given (100% of prior-year tax 61,000). **Adjustments: not answered**; the depreciation swap needs asset cost, which no file gives. |
| F — decisions considered | **Not answered.** Default: base projection only, no options modelled. |
| Payments already made / due dates | Not supplied. Payments-made check cannot run. |

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Step that uses it | Verdict |
|---|---|---|---|---|---|
| `profit_and_loss_2025_ytd.csv` | Monthly P&L Jan–Sep 2025, 12 line items + net income; every month foots; YTD net income **594,241** | No entity named | Yes | Step 1 (actuals) | **Accepted with a limit**: company user-asserted |
| `forecast_2025-10_to_2026-09.csv` | Monthly forecast Oct 2025 – Sep 2026, same lines | No entity named | Yes | Step 1 (forward half: Oct–Dec 2025 only) | **Accepted with a limit**: a forecast, user-supplied; 2026 months outside this tax year |
| `tax_rates_and_rules_SAMPLE.md` | Rate card: 20% flat, disallowables, 25% SL tax depreciation, losses nil b/f, 4 instalments, safe harbour 61,000 | Sampleland, tax year 2025 | Yes | Steps 2, 3 | **Accepted with a limit**: marked fictitious sample rates; no instalment due dates |
| `profit_and_loss_2025_ytd_final.csv` | **Not a P&L.** A staff shift rota (E08–E10, weeks 1–4, days/nights/off) | n/a | No | None | **Rejected** on content. Upload the final YTD P&L if one differs from the file above. |

**Still missing:** fixed asset cost (for 25% tax depreciation — required for a tax-adjusted base); instalment due dates and tax payments made to date (required for the payments check); detail of any fines, client entertainment or donations (none is visible as a P&L line); cash balance and any tax reserve (for the affordability test). I would wait for your answer here; proceeding on the accepted files.

## Step 1 — Income base (basis: **book profit, unadjusted**)

| | Amount |
|---|---:|
| Actual net income Jan–Sep 2025 (revenue 4,038,600) | 594,241 |
| Forecast net income Oct–Dec 2025 (revenue 1,207,470) | 142,138 |
| **Projected 2025 book profit** | **736,379** |
| Book depreciation in that figure (37,800 actual + 13,860 forecast) | 51,660 |

Your forecast is used rather than a run-rate. A straight-line annualisation (594,241 / 9 × 12 = 792,321) would overstate the year by 55,942, because your Q4 forecast (142,138) is well below the Jan–Sep average quarter (198,080). Q4 has no actuals: labelled projected.

**Book-to-tax adjustments not made** (default for E): the rate card replaces book depreciation with 25% straight line on cost, but no asset cost was supplied, so the 51,660 book charge stays in. Each 10,000 by which tax depreciation exceeds book depreciation lowers the tax by 2,000. No fines, entertainment or donations lines are visible; their disallowance cannot be tested without account detail. Losses brought forward: nil per the card.

## Step 2 — Projected tax

| | Amount |
|---|---:|
| Taxable base (book basis) | 736,379 |
| Rate (sample card, flat) | 20% |
| **Projected 2025 tax** | **147,276** |
| Effective rate on book profit | 20.0% |
| Marginal rate on the next dollar | 20.0% |

**Threshold map:** the card has a flat rate and no thresholds, allowances or surcharges, so there is no cliff and no headroom figure to report. The only band-like rule is donations above 10,000 disallowed; donations to date are not identifiable.

## Step 3 — Estimated payments

| | Safe harbour (100% of prior-year 61,000) | Current-year projection |
|---|---:|---:|
| Four equal instalments | **15,250** each | 36,819 each |
| Annual total | 61,000 | 147,276 |

- Per the card, paying 61,000 in four instalments of **15,250** meets the safe harbour even though projected tax is 147,276; the remaining **86,276** would then fall due at final settlement (date not given).
- **Payments made: not evidenced.** No tax payments were uploaded and no due dates were given, so missed or short instalments cannot be identified. By 30 Sep at least two or three instalments would normally have fallen due — please supply what was paid and when.
- No penalty is quantified: the rules for it were not supplied.

## Step 4 — Set-aside

Reserving 20% of monthly book profit: Oct 2025 ≈ 10,113 × 20% … total Q4 set-aside **28,428** on the forecast, on top of a year-to-date requirement of **118,848** (20% × 594,241). **Affordability test not run** — no cash balance or tax reserve account supplied (the Step 4b check needs both).

## Step 7 — Sensitivity (Q4 forecast ±10%, actuals fixed)

| Q4 profit | FY base | Tax at 20% |
|---|---:|---:|
| −10% (127,924) | 722,165 | 144,433 |
| Forecast (142,138) | 736,379 | 147,276 |
| +10% (156,352) | 750,593 | 150,119 |

The range is mechanical ±10% (no history supplied for observed variability). The larger uncertainty is the depreciation adjustment, not Q4.

## Not done, and why

- Tax-adjusted base — asset cost missing; disallowables not identifiable.
- Payments-made check and missed-instalment test — no payments or due dates.
- Affordability (Step 4b) — no cash or reserve data.
- Options comparison — no decisions named.
- Excel workbook — would ask before creating `Tax_Planning_2025_Northbrook_Trading_Ltd.xlsx`.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd (user-asserted), company taxpayer, Sampleland, tax year 2025, USD. Basis: **book, unadjusted**. 9 of 12 months actual. Rates: sample rate card v1, tax year 2025 — **fictitious sample**. Files: 3 accepted with limits, 1 rejected (staff rota). |
| Capability map | Not applicable: no connection. Every task is `[manual]`. |
| Steps | 1 done with limit (no adjustments); 2 done; 2b nothing to map; 3 schedule done, payments check **not done**; 4 schedule done, 4b **not done**; 5 not requested; 6 n/a; 7 done (mechanical range); 8 tables in chat. |
| Unknowns | Asset cost; payments made and due dates; disallowable items; cash position; professional sign-off. |
| Parameters | 20% flat; 25% SL tax depreciation (unapplied); safe harbour 61,000; all from the sample card, to be re-confirmed every run. |
