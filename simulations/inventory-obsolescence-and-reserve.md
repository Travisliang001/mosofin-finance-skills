# Inventory reserve — Northbrook Trading Ltd — as at 30 September 2025

Mosofin is not connected, so this run is manual: every step is `[manual]` and every figure comes from your uploads. Connecting Mosofin would read movement, prices and the reserve account directly ([docs.mosofin.com](https://docs.mosofin.com)).

## Read-back

Assessing inventory for **Northbrook Trading Ltd** (user-asserted) **as at 30 September 2025**, **USD** (user-asserted), from **your uploads**. Buckets **0–90, 91–180, 181–365, over 365 days**; **no reserve rates set — I am to propose them**; **weighted average cost**; **no damaged stock known** (you — I have not assessed condition); **TR-07 is seasonal**.

Not answered: **F — demand forecast and write-off approval limits.** Default applied: excess measured against **past usage only** (12 months), labelled as history, not forecast. Ageing basis: **last sale date** from the listing — a proxy, not lot age.

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Needed for | Verdict |
|---|---|---|---|---|---|
| `inventory_listing_2025-09-30.csv` | Stock listing: 15 SKUs, qty, unit cost, value, last sale date; total **683,100** | No entity; date from file name | Yes; **no location or lot dates** | Steps 2–4 | **Accepted with a limit**: company user-asserted; ageing on last-sale proxy |
| `inventory_movement_12m.csv` | Units sold by SKU by month, Oct 2024–Sep 2025: 180 rows (15 × 12) | No entity | Yes; units only, **12 months** (not 24); no write-offs | Step 2 | **Accepted with a limit**: no history of write-offs or below-cost sales, so rates cannot be derived from outcomes |
| `selling_prices.csv` | Recent selling price per SKU, 15 SKUs | No entity; **no dates** | Yes | Step 3 | **Accepted with a limit**: prices undated; no costs to sell |
| `trial_balance_2025-09-30.csv` | Trial balance, 33 accounts; debits = credits 6,546,018 | No entity | Yes | Tie-out, Step 6 | **Accepted with a limit**: company user-asserted. **No reserve account in it** |
| `inventory_listing_2025-09-30_final.csv` | **An employee shift rota** (E08–E10, weeks 1–4: days / nights / off). Not a stock listing despite its name | None | n/a | No step uses it | **Rejected.** If a revised listing exists, upload it instead |

**Still missing:** (1) **reserve account detail** for the period (required for the roll-forward — the TB shows no reserve account, so I read the balance as nil; please confirm); (2) **costs to sell** for the NRV test; (3) prior write-offs and below-cost sales (to derive rates); (4) forecast and approval limits. I would wait here; proceeding on the accepted files as instructed.

**Tie-out:** listing 683,100 = TB 1200 Inventory 683,100. **Difference 0.**

## Exception list (usage window: trailing 12 months; history, not forecast)

| SKU | Qty | Value | Last sale | Days | Bucket | Units sold 12m | Months of supply | Recent price vs cost | Rationale |
|---|---:|---:|---|---:|---|---:|---:|---|---|
| **LK-09** Lock set legacy | 847 | **39,792** | 2024-06-03 | 484 | >365 | **0** | ∞ | **28.20 vs 46.98** | No movement 16 months **and** price below cost |
| **PN-55** Panel 55mm (discontinued) | 501 | **26,528** | 2024-02-19 | 589 | >365 | **0** | ∞ | **31.80 vs 52.95** | Discontinued, no movement 19 months, price below cost |
| TR-07 Trim seasonal | 337 | 19,896 | 2024-11-28 | 306 | 181–365 | 266 (Oct–Nov 2024 only) | 15.2 | 85.55 vs 59.04 | **Seasonal — excluded from the no-move list** per your answer; season is Oct–Nov, now starting. Watch: if Oct–Nov 2025 sales do not come, re-assess |
| HG-22 Hinge soft-close | 1,294 | 53,056 | 2025-07-14 | 78 | 0–90 | 910 | 17.1 | 59.45 vs 41.00 | Steady ~90 a month, then **zero in Aug and Sep 2025**. Watch, not reserved |
| FX-02 Fixing kit pro | 2,653 | 92,849 | 2025-08-30 | 31 | 0–90 | 849 | 37.5 | 50.75 vs 35.00 | **Zero in Sep 2025**; 37.5 months of supply |
| SB-20 Steel bracket | 2,985 | 59,691 | 2025-09-27 | 3 | 0–90 | 504 | **71.1** | 29.00 vs 20.00 | Excess against history |
| SB-35 Steel bracket heavy | 2,018 | 46,424 | 2025-09-22 | 8 | 0–90 | 588 | 41.2 | 33.35 vs 23.01 | Excess against history |
| FX-01 Fixing kit | 2,280 | 72,952 | 2025-09-25 | 5 | 0–90 | 840 | 32.6 | 46.40 vs 32.00 | Excess against history |

By bucket (last-sale proxy): 0–90 days **596,884** (12 SKUs); 91–180 **0**; 181–365 **19,896** (TR-07, seasonal); over 365 **66,320** (LK-09, PN-55).

No-move is not obsolescence on its own: TR-07 was taken out as seasonal; no other special category was named.

## NRV test (cost vs recent selling price; costs to sell not supplied)

Two SKUs have a recent selling price below cost: **LK-09 (847 × (46.98 − 28.20) = 15,906.60)** and **PN-55 (501 × (52.95 − 31.80) = 10,596.20)** — **26,502.80 before costs to sell**, so a **minimum** write-down. Every other SKU's price exceeds its cost. The prices are undated, and neither SKU has sold in 12 months, so "recent" is unevidenced.

## Proposed reserve (proposal — the rates are yours to approve)

No rates can be **derived** from history: the files hold no write-offs and no below-cost sales. So I propose, and **wait for your yes**:

| Population | Method | Proposed | Amount |
|---|---|---|---:|
| LK-09, PN-55 (>365 days, below cost) | Specific identification, **once, on the more severe basis** | Option A — to recent price (NRV floor) | **26,502.80** |
| | | Option B — full reserve, if no sale is expected (discontinued, 16–19 months without a sale) | **66,320.00** |
| TR-07 (seasonal) | Excluded | — | 0 |
| Excess against history (SB-20, SB-35, FX-01, FX-02; 271,916 in value) and the HG-22 / FX-02 sales stop | **No rate proposed** — no evidence of loss; prices are 45–50% above cost. Needs a forecast or your rate | — | not sized |
| Everything else (0–90 days, priced above cost) | No reserve | 0% | 0 |

**Proposed reserve: 26,502.80 (A) to 66,320.00 (B)** — LK-09 and PN-55 counted once, not again in an ageing bucket.

Proposed entry (not posted): **DR Inventory Obsolescence Expense / CR Inventory Reserve** — 26,502.80 or 66,320.00. No write-off entry is proposed: the stock is still held.

## Roll-forward

Beginning reserve **0** (no reserve account in the TB — unconfirmed) + additions (as approved above) − write-offs 0 = ending reserve. **Not tied to a reserve account** — none exists; please confirm or upload the account detail.

## Not done, and why

Rate derivation and reserve back-test (no write-off or below-cost sale history). Full NRV (no costs to sell). Forecast comparison (no forecast — history used, labelled). Physical condition: **`[manual]`, not assessed** — owner: warehouse / operations; you report none known. Workpaper `Inventory_Reserve_2025-09_Northbrook Trading Ltd.xlsx` offered; not created without your yes.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, 30 Sep 2025, USD — **user-asserted**. Source: **upload** (Mosofin not used, your choice). Listing, movement, prices, TB: accepted with limits. `inventory_listing_2025-09-30_final.csv`: **rejected** (shift rota). Ageing basis: **last sale date proxy** |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 0 on uploads · 1 buckets yours; rates **proposed, not derived** · 2 done (12-month window; TR-07 excluded as seasonal) · 3 done to recent price; costs to sell **not done** · 4 proposed A / B; back-test **not done** · 5 proposal only · 6 roll-forward from nil, **not tied** (no reserve account) · 7 tables here; xlsx offered · 8 not offered |
| Not done | Reserve account detail; costs to sell; write-off history; forecast; approval limits; condition |

Nothing was posted, sent or changed. **Data sources:** upload — `inventory_listing_2025-09-30.csv`, `inventory_movement_12m.csv`, `selling_prices.csv`, `trial_balance_2025-09-30.csv`.
