# Inventory costing — Northbrook Trading Ltd — September 2025

Mosofin is not connected, so this run is manual: every step is `[manual]` and every figure comes from your uploads. Connecting Mosofin would read purchase and sales lines by item directly ([docs.mosofin.com](https://docs.mosofin.com)).

## Read-back

Costing inventory for **Northbrook Trading Ltd** (user-asserted) for **September 2025** (as at 30 Sep 2025), **USD** (user-asserted), under **US GAAP**, **perpetual** system, **no standard costing** (you). Method: **weighted average cost, lower of cost and net realisable value** — from `accounting_policies.md` (a fact inside a file; please confirm). Perpetual + weighted average means **moving average** (recomputed after each purchase). Eligible under US GAAP.

Not answered, and the skill's default applied:
- **E — opening quantities and costs, and cost components (freight, duties):** not supplied. Default would be weighted average on the opening balance — but **no opening balance was supplied either**, so there is nothing to start the average from. **Layers / opening position not supplied.** Freight-in treatment unknown.
- **F — costs to complete and sell:** not supplied. Default: compare cost with recent selling prices only — but **no selling prices were supplied**, so the value test cannot run.

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Needed for | Verdict |
|---|---|---|---|---|---|
| `inventory_listing_2025-09-30.csv` | Closing stock listing: 15 SKUs, qty on hand, unit cost, value, last sale date; total **683,100** | No entity or currency; date from file name | Yes. `unit_cost` is rounded to whole dollars (value ≠ qty × unit cost by up to 25 a line); value used | Steps 4 (closing check), 5, routing | **Accepted with a limit**: company user-asserted; closing position only, not a cost flow |
| `inventory_purchases_2025-09.csv` | September purchases: 4 lines, 3 SKUs (SB-20, C-12, FX-01), date, qty, unit cost; total **270,840** | No entity; dates 4–21 Sep 2025 | Yes; no freight or duty lines | Steps 2, 3, 4 | **Accepted with a limit**: company user-asserted |
| `accounting_policies.md` | Accounting policies | No entity; US GAAP, private | Yes | Intake C, Step 1 | **Accepted** (method user-supplied) |
| `inventory_purchases_2025-09_final.csv` | **An employee shift rota** (E08–E10, weeks 1–4: days / nights / off). Not purchases despite its name | None | n/a | No step uses it | **Rejected.** If a revised purchase file exists, upload it instead |

**Still missing (required):** (1) **sales / issues by item, with dates** — the consumption side of the cost flow; (2) **opening inventory at 1 Sep 2025** by item, quantity and cost. **Recommended:** selling prices and costs to complete and sell; freight-in and duty postings. I would wait here; proceeding on the accepted files as instructed.

## What can and cannot be computed

**The September cost flow cannot be built.** A moving average needs the opening quantity and cost and every issue in date order; neither was supplied. I do not rebuild opening positions by assumption. So **COGS for September is not computed**, and the **units and cost validation (opening + purchases − sales = closing) cannot run** — both halves are missing their opening and sales legs.

## Findings

**1. SB-20 is listed at 20.00 a unit, below every September purchase (22.50).** 11,000 units were bought in September at 22.50 (6,000 on 4 Sep, 5,000 on 15 Sep; 247,500), and 2,985 remain, valued at **59,691 (19.997 a unit)**. Under a moving average, the average after the 15 Sep purchase blends ≥ 5,000 units at 22.50 with whatever was held; for it to be 20.00, the stock held on 15 Sep would have to satisfy *quantity × (20.00 − its average) = 5,000 × 2.50 = 12,500*, i.e. a large holding well below 20.00 surviving the 6,000-unit purchase at 22.50. That is possible only with substantial cheap opening stock. **Either the listing's cost is stale or not a moving average, or the opening stock explains it — the opening position will settle which.** For scale only (not a method choice): at the latest purchase cost the 2,985 units would be 67,162.50, **7,471.50 above the listed value**.

**2. FX-01 listed at 32.00 (72,952 for 2,280); September purchase 600 at 35.00 (21,000).** Consistent with a moving average over older, cheaper stock; cannot be confirmed without the opening position and issues.

**3. C-12 listed at 26.00; September purchase 90 at 26.00.** Consistent.

**4. The other 12 SKUs had no September purchases** (382,561 of the 683,100), so their listed costs come entirely from before September and cannot be tested from these files.

**5. Value test (lower of cost and NRV) not run.** No selling prices and no costs to complete and sell. Items with no recent sale, routed to `inventory-obsolescence-and-reserve` (no write-down concluded here):

| SKU | Last sale | Value |
|---|---|---:|
| PN-55 Panel 55mm (discontinued) | 2024-02-19 | 26,528 |
| LK-09 Lock set legacy | 2024-06-03 | 39,792 |
| TR-07 Trim seasonal | 2024-11-28 | 19,896 |
| HG-22 Hinge soft-close | 2025-07-14 | 53,056 |
| FX-02 Fixing kit pro | 2025-08-30 | 92,849 |

## Proposed entries (proposals only — not posted)

Perpetual system: COGS posts with each sale, so **no period-end COGS entry is proposed**. **No NRV write-down is proposed** (value test not run). No costing adjustment is proposed for SB-20 until the opening position explains or contradicts the 20.00.

## Method comparison

Not requested, and not computable without sales. Observed price direction for the three SKUs bought: **flat or rising** (SB-20 22.50 vs 20.00 listed; FX-01 35.00 vs 32.00; C-12 26.00 flat). No comparison is a recommendation to change method.

## Not done, and why

September COGS and the moving-average cost flow (no sales, no opening). Units and cost validation (same). Tie to the GL inventory balance (no trial balance uploaded; listing total 683,100 untied — hand to `inventory-to-gl-reconciliation`). Freight-in check (no freight postings). NRV / value test (no prices, no costs to sell). Consistency with the prior period (no prior data). Workpaper `Inventory_Costing_2025-09_Northbrook Trading Ltd.xlsx` offered; not created without your yes.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, September 2025, USD, US GAAP, perpetual, no standard costing — **user-asserted**. Source: **upload** (Mosofin not used, your choice). Listing and purchases: accepted with limits; policies: accepted. `inventory_purchases_2025-09_final.csv`: **rejected** (shift rota). Line-level detail: purchases yes; **sales none** |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 0 on uploads · 0b method from policy (WAVG), system perpetual (you) — not observed · 1 done: WAVG eligible under US GAAP; consistency **not done** · 2 purchase price only; freight **not done** · 3 moving average identified · 4 **not done** — no opening, no sales; closing listing tested against purchases (SB-20 finding) · 5 **not done**; no-sale items routed · 6 none proposed · 7 not requested · 8 tables here; xlsx offered · 9 not offered |
| Not done | Sales/issues by item; opening inventory; selling prices and costs to sell; freight postings; trial balance for the GL tie |

Nothing was posted, sent or changed. **Data sources:** upload — `inventory_listing_2025-09-30.csv`, `inventory_purchases_2025-09.csv`, `accounting_policies.md`.
