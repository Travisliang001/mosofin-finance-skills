# Working capital assessment — Northbrook Trading Ltd, 36 months to September 2025, USD (upload path)

Mosofin is not connected, so this run is manual and works only from the files you uploaded. Nothing was changed: no terms, payment runs, credit limits or stock policy, and no customer or supplier was contacted. **Every lever below is a proposal for a person to decide**, and every figure sits beside its trade-off.

## Read-back

Assessing working capital for **Northbrook Trading Ltd** over **36 months, October 2022 – September 2025**, in **USD**, from **your uploaded monthly statements, AR ageing, 12-month bill history and inventory listing**. Inventory is held **at item level** (15 SKUs with last-sale dates). From `working_capital_terms.md`, used once you confirm: customer terms **30 days, Harlow Fabrication 45 days**; supplier terms **as recorded**; guardrails **Kestrel Supplies is strategic — no stretching; 98% order fill**; cost of capital **9%**; **no benchmarks**, so the business is compared only with its own history. Company and currency are user-asserted.

## Validation of the upload — shown before any work

| File | What it actually is | Company / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `monthly_balance_sheet_36m.csv` | Month-end balance sheets: cash, AR, inventory, prepaid, fixed assets, AP, accrued, debt, equity | 36 months Oct 2022–Sep 2025, no gaps; no company/currency | Yes: balances every month; retained earnings roll to P&L except Mar 2025 (−60,000) and Jun 2025 (−7,500), read as distributions | Yes: Step 1/1b | **Accepted with a limit**: company/currency user-asserted |
| `monthly_profit_and_loss_36m.csv` | Monthly P&L with revenue and COGS | Same 36 months | Yes: net income recomputes every month | Yes: Step 1 denominators | **Accepted with a limit**: company user-asserted; no purchases line, so DPO is on COGS |
| `ar_aging_detail_2025-09-30.csv` | Open AR by invoice, 13 customers, 14 lines incl. one credit memo | At 30 Sep 2025 | Yes. Total **798,360** vs balance-sheet AR **789,360**: difference 9,000, consistent with an allowance netted in the balance sheet — please confirm. No payment dates or order dates | Yes: Step 2 | **Accepted with a limit**: open items only; days-to-pay and DSO stage split cannot be measured |
| `bill_payment_history_12m.csv` | Paid bills, 8 vendors, 92 bills, Oct 2024–Sep 2025 | 12 months | Yes; **bills total 864,228 against 12-month COGS 3,007,522**, so this is part of the supplier base only; no discount terms | Yes: Step 4 | **Accepted with a limit**: covers these 8 vendors only |
| `inventory_listing_2025-09-30.csv` | SKU listing with qty, cost, value, last-sale date | At 30 Sep 2025 | Yes; total **683,100 = balance sheet** | Yes: Step 3 | **Accepted** (company user-asserted) |
| `working_capital_terms.md` | Your intake answers C–F | — | Yes | Guardrails, cost of capital | **Accepted**: answers confirmed in the read-back |
| `monthly_balance_sheet_36m_final.csv` | **Not a balance sheet.** A staff shift rota: E08–E10, week_1–week_4, nights/days/off | No company, dates or amounts | No | No step uses it | **Rejected** on content; I use `monthly_balance_sheet_36m.csv` |

Still missing: AR payment history with invoice and payment dates (for days-to-pay by customer and the DSO stage split); the full payables listing and any early-payment discount terms; the allowance figure.

*I would stop here and wait. Assumed answer: "go ahead with the accepted files".*

## Findings

**1. The cash conversion cycle has lengthened by about 10 days a year — deterioration, not seasonality** (actual days in each month; DPO on COGS).

| Month | DSO | DIO | DPO | CCC |
|---|---:|---:|---:|---:|
| Sep 2023 | 45.1 | 64.7 | 36.4 | **73.4** |
| Sep 2024 | 48.6 | 69.9 | 34.7 | **83.7** |
| Sep 2025 | 52.0 | 75.0 | 33.0 | **94.0** |

Same month year on year rises every year, so this is not the seasonal cycle; all three components moved the wrong way. (February dips each year are the 28-day convention, not behaviour.) On annual figures, FY25 DSO 56, DIO 83, DPO 36.

**2. Of the 264,687 rise in operating working capital (Sep 2024 → Sep 2025), 150,187 is growth and 114,500 is days.** Revenue in September rose 15%. Holding Sep 2024 days at Sep 2025 volume: AR +98,276, inventory +103,188, AP +51,278 (volume, not a problem). The residual: **AR +52,046, inventory +46,841, AP −15,614 (paying faster) = 114,500 of deterioration.**

**3. Receivables.** Ageing at 30 Sep: current 425,953; 1–30 days 200,127; 31–60 72,046; 61–90 48,031; **90+ 52,203**. **Harlow Fabrication** holds 248,157 (31% of AR); its agreed terms are **45 days but the ledger dates invoices at 30 days** (INV-20418: 28 May → due 27 Jun). On 45 days INV-20418 is still **80 days past due (48,200)**. Foxhall Garden Centres 4,003 at 130 days and Tideswell Hotels 48,031 at 67 days need follow-up; Calder Print has an unapplied credit memo (−2,150). The DSO stage split (invoicing delay vs collection) cannot be measured without payment dates.

**4. Inventory** (item level; listing ties to 683,100). **No sale in over 300 days: LK-09 Lock set legacy 39,792 (484 days), PN-55 Panel 55mm discontinued 26,528 (589 days), TR-07 Trim seasonal 19,896 (306 days) — 86,216 at cost (12.6%).** HG-22 (53,056) last sold 78 days ago. Realisable value is unknown; liquidation would take a P&L hit, and the same list raises an obsolescence-provision question.

**5. Payables — paying early.** Kestrel Supplies and Orchard Packaging are paid on day 18 of 30-day terms, every month (12 days early). Summit Freight, Brightline, M. Okafor, Kestrel Inc. and Greyfriars are paid on the due date; Halden (rent, terms 0) one day after. No discount terms are recorded, so I cannot confirm the early payments are not capturing a discount.

**6. Levers — sized in days and cash, internal levers first, each with its trade-off** (value at your 9%; daily revenue 14,072, daily COGS 8,240 on FY25).

| Lever | Type | Cash | Value/yr at 9% | Trade-off / risk (not scored) |
|---|---|---:|---:|---|
| Pay Orchard Packaging on terms, not day 18 | Internal | 6,194 | 557 | None if no discount is being earned — check first |
| Fix Harlow's recorded terms to the agreed 45 days; chase INV-20418 | Internal, then customer | 48,200 | 4,338 | Largest customer: collection call needs the account owner |
| Collections cadence on 61+ days (Tideswell, Foxhall) | Customer-facing | 52,034 | 4,683 | Relationship; Foxhall may be a credit-loss case |
| DSO back to Sep 2023 level (52.0 → 45.1) | Mixed | ~97,000 | ~8,700 | Tightening terms can cost sales; no benchmark used |
| Clear slow movers (LK-09, PN-55, TR-07) | Internal | up to 86,216 at cost | up to 7,759 | Write-down on sale; realisable value unknown |
| DIO back to Sep 2023 level (75.0 → 64.7) | Operational | ~84,900 | ~7,600 | **98% fill guardrail**: stock cuts risk lost sales |
| Kestrel Supplies paid on terms (13,555) | Supplier | — | — | **Not proposed: your guardrail says do not stretch Kestrel.** Paying on terms is not stretching, but it is your call |

**Not proposed:** stretching any supplier beyond terms; factoring (no cost data).

## What was not done, and why

- Industry benchmarks, supplier lead times, stockout rate and supplier satisfaction: not in the files; the 98% fill guardrail is **unmonitored**, not satisfied.
- Days-to-pay by customer and DSO stage split: need AR payment and order dates.
- Discounts available vs captured: no discount terms recorded.
- Roadmap owners and cash-forecast integration: yours to assign. No Excel file; I would ask before making `Working_Capital_Optimization_2025-09_Northbrook-Trading-Ltd.xlsx`.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, USD — user-asserted; source: upload; 36 months read (36 observations per series); item-level inventory: yes; DPO denominator: COGS (no purchases line). Six files accepted (five with limits); rota rejected |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 1 CCC: done. 1b decomposition: done (volume/days; seasonality by same-month comparison). 2 AR: done with a limit (ageing only). 3 inventory: done. 4 AP: done with a limit (8 vendors). 5–7 levers and trade-offs: done as proposals. 8 roadmap: not done (owners yours). 9 KPIs: baselines above; guardrails unmonitored. 10: chat only |
| Not done | AR 9,000 difference to the ledger (needs allowance detail); AP balance 300,564 to bill listing (needs full open-AP listing) |
| Unknowns carried forward | Guardrail data; realisable value of slow stock; discount terms; Harlow terms set-up; whether customer payment is deteriorating generally |
| Parameters | Actual days in month; DPO on COGS; history 36 months; slow-moving threshold 300 days without sale; cost of capital 9% |
