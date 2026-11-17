# Flux analysis — Northbrook Trading Ltd, September 2025

**Read-back.** Flux for **Northbrook Trading Ltd** for **September 2025** (as at 2025-09-30, USD), against
**August 2025** and **September 2024**, from **your uploads** (manual run: Mosofin is not used, so every
task below is `[manual]`). Flagging a movement over **10% and 2,500** on the income statement and
**10% and 10,000** on the balance sheet (**your thresholds**, not the default). Questions go to the
**controller** for every account. No known events, so explanations come from the files only.
*I would wait for your yes here; proceeding on "go ahead with the accepted files".*

## 1. Upload validation (before any work)

| File | What it actually is | Company / period | Usable? | Used by | Verdict |
|---|---|---|---|---|---|
| `monthly_profit_and_loss_36m.csv` | Monthly income statement by account, 36 rows (2022-10 to 2025-09), 12 expense lines + net income | No entity or currency named | Every month foots: revenue − expenses = net income (36/36) | Steps 1–4 | **Accepted with a limit:** company and currency user-asserted; no ledger detail, so movements can be flagged but not fully explained |
| `monthly_balance_sheet_36m.csv` | Monthly balance sheet, 36 month-ends, 5 asset and 5 liability/equity lines + a dividends/adjustments column | No entity or currency named | Balances every month; retained earnings rolls (prior + net income − dividends/adjustments) every month; fixed assets fall by depreciation every month | Steps 1, 2, 5 | **Accepted with a limit:** company and currency user-asserted |
| `recurring_entries.csv` | Recurring-entry schedule: 5 entries, amount, posting day, posted yes/no for Jul–Sep 2025 | No entity named | Readable; amounts agree to the P&L (rent 9,000, depreciation 4,200, insurance 1,500, interest 1,069 in Sept) | Steps 3–4 (evidence for nil balances) | **Accepted with a limit:** a schedule, not ledger postings; company user-asserted |
| `monthly_profit_and_loss_36m_final.csv` | **Not a P&L.** A staff shift roster: employees E08–E10 with week_1–week_4 set to days/nights/off. No accounts, no amounts, no months | None | Nothing this skill can use | No step | **Rejected:** its content is a rota, whatever its name says. If a "final" P&L exists, upload it in place of this file |

**Still missing (recommended, not required):** general ledger detail or a journal list for September 2025.
Without it, marketing and the margin change cannot be explained from evidence (see section 4).

## 2. Thresholds and the line

- Income statement: **10% and 2,500**. Balance sheet: **10% and 10,000**. Both must trip. User's values.
- Always flagged regardless: drop to nil / appear from nil, sign change, gross margin moving ≥ 1 point.
- **Largest movement that did not trip:** income statement, payroll YoY +4,800 (+6.7%, passes amount only);
  balance sheet, receivables MoM −33,070 (−4.0%, passes amount only).
- No sign changes. Revenue Sept 2025 455,400 vs Aug 477,100 vs Sept 2024 394,700.

## 3. Flux schedule — income statement (flagged rows in bold)

| Account | Sep-25 | Aug-25 | Sep-24 | MoM | MoM % | YoY | YoY % | % of rev Sep-25 / Aug-25 / Sep-24 |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| **Revenue** | 455,400 | 477,100 | 394,700 | −21,700 | −4.5% | **+60,700** | **+15.4%** | |
| **Cost of sales** | 273,240 | 286,260 | 228,926 | −13,020 | −4.5% | **+44,314** | **+19.4%** | 60.0 / 60.0 / 58.0 |
| Payroll | 76,000 | 75,600 | 71,200 | +400 | +0.5% | +4,800 | +6.7% | 16.7 / 15.8 / 18.0 |
| Rent | 9,000 | 9,000 | 9,000 | 0 | 0% | 0 | 0% | 2.0 / 1.9 / 2.3 |
| **Marketing** | 29,146 | 19,084 | 15,788 | **+10,062** | **+52.7%** | **+13,358** | **+84.6%** | **6.4 / 4.0 / 4.0** |
| **Software** | **0** | 3,500 | 3,500 | **−3,500** | **−100%** | **−3,500** | **−100%** | 0.0 / 0.7 / 0.9 |
| Professional fees | 2,500 | 2,500 | 2,500 | 0 | 0% | 0 | 0% | 0.5 |
| Bank fees | 1,822 | 1,908 | 1,579 | −86 | −4.5% | +243 | +15.4% | 0.4 |
| Depreciation | 4,200 | 4,200 | 4,200 | 0 | 0% | 0 | 0% | 0.9 |
| Insurance | 1,500 | 1,500 | 1,500 | 0 | 0% | 0 | 0% | 0.3 |
| Repairs | 500 | 500 | 500 | 0 | 0% | 0 | 0% | 0.1 |
| Interest | 1,069 | 1,092 | 1,354 | −23 | −2.1% | −285 | −21.0% | 0.2 |
| **Net income** | 56,423 | 71,956 | 54,653 | **−15,533** | **−21.6%** | +1,770 | +3.2% | 12.4 / 15.1 / 13.8 (net margin) |
| **Gross margin** | 40.0% | 40.0% | 42.0% | 0.0 pt | | **−2.0 pt** | | |

Net income MoM bridge: revenue −21,700, cost of sales +13,020, marketing −10,062, software +3,500, other −291 = −15,533.

## 4. Explanations (one driver each)

1. **Software, 3,500 to nil — Timing (missing posting).** Evidence: `recurring_entries.csv` shows the
   3,500 software subscription (day 5) posted in July and August and **not posted in September**;
   the line was 3,500 in every one of the prior 35 months. Accrued liabilities rose only 200 (its
   usual monthly step), so no accrual was made either. **Not a saving.** Proposed entry below.
2. **Marketing +10,062 MoM (+52.7%), +13,358 YoY (+84.6%) — unexplained: asked.** Marketing ran at
   exactly 4.0% of revenue in every month of the 36-month history; in September it is 6.4% while
   revenue fell 4.5%. At the usual 4.0% it would be 18,216, so **10,930 is above the run rate**. No
   ledger detail was supplied, so a campaign, a mis-coding or a duplicate cannot be told apart.
3. **Gross margin −2.0 pt YoY (42.0% to 40.0%); cost of sales +44,314 YoY (+19.4%) vs revenue +15.4% —
   unexplained: asked (price/rate or mix suspected).** Cost of sales was 58.0% of revenue every month
   to June 2025 and stepped to 60.0% from **July 2025**. Of the +44,314, 35,206 is revenue growth at
   the old 58% and **9,108** is the rate change. No supplier, product or ledger detail to assign it.
   MoM margin is flat (0 pt): the change is not new this month.
4. **Revenue +60,700 YoY (+15.4%) — unexplained: asked (volume suspected).** Consistent with the
   36-month trend; no unit or price data to split volume from price. The −4.5% MoM is below the
   10% line and matches the same Aug-to-Sep fall in 2023 and 2024 (−4.5% both years).
5. **Net income −15,533 MoM (−21.6%).** Fully explained by items 1–4 per the bridge above; booking the
   software accrual would lower September net income to 52,923.

## 5. Balance sheet flux and cash proof

| Line | Sep-25 | Aug-25 | Sep-24 | MoM | YoY | Flagged / explanation |
|---|---:|---:|---:|---:|---:|---|
| Cash | 1,118,199 | 1,016,530 | 730,628 | +101,669 (+10.0%) | +387,571 (+53.0%) | **Both flagged; proved by the bridge below** |
| Receivables | 789,360 | 822,430 | 639,038 | −33,070 (−4.0%) | +150,322 (+23.5%) | **YoY flagged:** grows faster than revenue (+15.4%); about 52.0 days of sales vs 48.6 — asked |
| Inventory | 683,100 | 711,561 | 533,071 | −28,461 (−4.0%) | +150,029 (+28.1%) | **YoY flagged:** about 75.0 days of cost of sales vs 69.9 — asked |
| Prepaid | 18,000 | 18,000 | 18,000 | 0 | 0 | Not flagged |
| Fixed assets, net | 108,800 | 113,000 | 159,200 | −4,200 | −50,400 (−31.7%) | **YoY flagged:** 12 × 4,200 depreciation, no additions (books) |
| Payables | 300,564 | 316,249 | 264,900 | −15,685 (−5.0%) | +35,664 (+13.5%) | **YoY flagged:** volume, in line with cost of sales growth (books) |
| Accrued | 38,000 | 37,800 | 35,600 | +200 | +2,400 | Not flagged; note it holds no software accrual |
| Debt | 220,000 | 225,000 | 280,000 | −5,000 | −60,000 (−21.4%) | **YoY flagged:** 5,000 repaid every month (books) |
| Retained earnings | 1,908,895 | 1,852,472 | 1,249,437 | +56,423 | +659,458 (+52.8%) | **YoY flagged:** net income 726,958 less dividends/adjustments 67,500 (60,000 Mar-25, 7,500 Jun-25) |

**Cash proof, Aug→Sep 2025:** net income 56,423 + depreciation 4,200 + receivables decrease 33,070 +
inventory decrease 28,461 − payables decrease 15,685 + accrued increase 200 − debt repaid 5,000 =
**101,669; actual change 101,669; difference nil.**
**Cash proof, Sep-24→Sep-25:** net income 726,958 + depreciation 50,400 − receivables 150,322 −
inventory 150,029 + payables 35,664 + accrued 2,400 − debt 60,000 − dividends/adjustments 67,500 =
**387,571; actual 387,571; difference nil.**

## 6. Proposed entry (proposal only, nothing posted)

```
September 2025 software subscription not posted
DR Software                      3,500
    CR Accrued liabilities           3,500
```
Account names are the column names in the upload; no chart of accounts was supplied.

## 7. Owner questions — draft, to the controller (nothing sent)

1. **Software:** 0 in Sept vs 3,500 in Aug and Sept 2024; the schedule shows the day-5 subscription not posted. Was it billed? Confirm before the accrual is booked.
2. **Marketing:** 29,146 vs 19,084 (+10,062) and 15,788 YoY; 6.4% of revenue vs a steady 4.0%. Please send the September marketing ledger: was there a campaign, or is ~10,930 mis-coded or duplicated?
3. **Cost of sales rate:** 60.0% of revenue since July 2025 vs 58.0% before (9,108 YoY effect in Sept). Supplier price rise, product mix, or a costing change?
4. **Revenue +15.4% YoY:** volume or price? Unit or price-list data would let me assign the driver.
5. **Receivables and inventory** grew 23.5% and 28.1% YoY vs revenue 15.4%: any slow payers or slow stock?
6. **Dividends/adjustments:** 7,500 in June 2025 sits in that column with no description: dividend or adjustment?

## 8. Not done, and why

- Ledger drill-down (Step 3): no general ledger or journal list uploaded; items 2–4 stay "unexplained: asked".
- Accounting method could not be confirmed from the files; assumed the same for every period.
- Excel workpaper not created: would you like `Flux_Analysis_2025-09.xlsx` (Northbrook Trading Ltd)?
- Saving thresholds/owners (Step 7): only after you have reviewed these results.

## 9. Coverage sheet (manual run)

**Environment:** Northbrook Trading Ltd, September 2025, USD — user-asserted. Data source: upload.
Files: P&L accepted with a limit; balance sheet accepted with a limit; recurring schedule accepted with a limit; `..._final.csv` rejected (shift roster).
**Capability map:** Not applicable: no connection. Every task is `[manual]`.

| Step | Status |
|---|---|
| 1 Line up accounts, % of revenue, margins | Done |
| 2 Apply both thresholds + always-flag rules | Done |
| 3 Drill into flagged accounts | Done with a limit: recurring schedule only, no ledger |
| 4 Driver and explanation | Done with a limit: 1 evidenced (software), 3 unexplained: asked |
| 5 Cash proof | Done: MoM and YoY tie to nil |
| 6 Proposed entries and owner questions | Done (drafts) |
| Not done | GL drill-down and journal review — needs the September ledger detail |

**Data sources:** upload — `monthly_profit_and_loss_36m.csv`, `monthly_balance_sheet_36m.csv`, `recurring_entries.csv`.
