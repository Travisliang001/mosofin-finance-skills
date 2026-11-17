# Inventory to GL reconciliation — Northbrook Trading Ltd — 30 September 2025

Mosofin is not connected, so this run is manual: every step is `[manual]` and every figure comes from your uploads. Connecting Mosofin would read the item quantities, GL balances and the cut-off population directly ([docs.mosofin.com](https://docs.mosofin.com)).

## Read-back

Reconciling inventory for **Northbrook Trading Ltd** (user-asserted) **at 30 September 2025**, **USD** (user-asserted), from **your uploads**.

Not answered, and no default is stated, so the more conservative reading is taken (it decides no conclusion; both answers shown where it matters):
- **Is the stock listing a separate system from the GL?** Unknown. If it is the same platform, the GL-to-listing agreement below is **nil by construction** and proves nothing about the stock; if separate, it is a real agreement.
- **When was the last physical count?** No count was supplied and no date given. Treated as **no recent count on file** — please tell me the date.
- Locations, in-transit / consignment, reserve policy, variance accounts: not supplied.

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Needed for | Verdict |
|---|---|---|---|---|---|
| `trial_balance_2025-09-30.csv` | Trial balance, 33 accounts; debits = credits 6,546,018. One inventory account: 1200 Inventory **683,100** | No entity or currency; date from file name | Yes | Steps 1, 3 | **Accepted with a limit**: company and period user-asserted; balances only, no inventory ledger detail |
| `inventory_listing_2025-09-30.csv` | Stock listing (subledger extract): 15 SKUs, qty, unit cost, value, last sale date; extended value **683,100**; no location | No entity; date from file name | Yes; `unit_cost` rounded to whole dollars (value used) | Steps 1, 3, ledger checks | **Accepted with a limit**: company user-asserted; no locations |
| `inventory_movement_12m.csv` | Units sold by SKU by month, Oct 2024–Sep 2025, 180 rows | No entity | Units only — no receipts, no values, no dates within the month | Ledger checks (no-movement items) | **Accepted with a limit**: cannot support cut-off or a quantity roll-forward |
| `inventory_listing_2025-09-30_final.csv` | **An employee shift rota** (E08–E10, weeks 1–4: days / nights / off). Not a stock listing despite its name | None | n/a | No step uses it | **Rejected.** If a revised listing or a **count sheet** exists, upload it instead |

**Still missing:** (1) **physical count results** and the count date (required — the only leg that tests existence); (2) whether the listing is a separate system (required); (3) transactions around 30 Sep and anything posted after it (cut-off); (4) reserve account detail and reserve policy; (5) in-transit / consignment and title terms. I would wait here; proceeding on the accepted files as instructed.

## Header

| | |
|---|---|
| Subledger a separate system? | **Not confirmed** |
| Last physical count | **None supplied — headline finding** |
| Count cadence | Not known |

## Reconciliation

| GL account | GL balance | Listing (Σ value) | Difference | Reason | Action |
|---|---:|---:|---:|---|---|
| 1200 Inventory | 683,100 | 683,100 | **0** | If one system: **nil by construction**. If separate: agrees | Confirm which |

Reconciling items (Step 3): none identified — no in-transit, cut-off, FX or standard-cost variance data supplied. Leg 2 (listing to count) and leg 3 (transitive) **not performed: no count**. So this is **not a completed reconciliation**: the GL and the listing agree with each other, and nothing here shows the 683,100 of stock exists.

## Findings

1. **No physical count on file.** GL 683,100 = listing 683,100, but without a count this is agreement between records, not evidence of stock. Recommend a full count (or a cycle-count programme) and send me the results; shrinkage cannot be stated without one.
2. **One inventory account (1200) covers all stock** — no raw materials / WIP / finished goods / in-transit split, no reserve contra. Category-level reconciliation is impossible (structural limitation). No consignment-in account appears; whether third-party stock is in the listing is unknown.
3. **No inventory reserve account in the TB**, so the carrying value is full cost while the listing holds long-unsold stock — routed to `inventory-obsolescence-and-reserve`, not written down here:

| SKU | Last sale | Days to 30 Sep | Units sold, 12 months | Value |
|---|---|---:|---:|---:|
| PN-55 Panel 55mm (discontinued) | 2024-02-19 | 589 | 0 | 26,528 |
| LK-09 Lock set legacy | 2024-06-03 | 484 | 0 | 39,792 |
| TR-07 Trim seasonal | 2024-11-28 | 306 | 266 (Oct–Nov 2024) | 19,896 |

   **86,216** in total (12.6% of 683,100), 66,320 of it unsold for over a year.
4. **Negative quantities: none** (all 15 SKUs positive).

## Proposed entries (proposals only — not posted)

**None.** Shrinkage, overage and cut-off entries follow a count and a boundary population; neither was supplied. Any write-down belongs to the reserve assessment.

## Not done, and why

Listing-to-count comparison, variance classification and investigation, shrinkage and its trend (no count; shrinkage is not stated without one). Cut-off testing, both dated near the boundary and posted after it (no transaction detail). Reserve roll-forward (no reserve account or detail). In-transit and consignment (no title terms). Workpaper `Inventory_Recon_2025-09.xlsx` offered; not created without your yes.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, 30 Sep 2025, USD — **user-asserted**. Source: **upload** (Mosofin not used, your choice). TB, listing, movement: accepted with limits. `inventory_listing_2025-09-30_final.csv`: **rejected** (shift rota) |
| Capability map | Not applicable: no connection. Every task is `[manual]`. Physical count: `[manual]`, owner warehouse / operations, last performed **unknown** |
| Steps | 0 on uploads · 0b systems **not confirmed**; count **none supplied** · 1 done; single account reported · 2 leg 1 only · 3 done: difference 0 (nil by construction if one system) · 4 **not done** (no count) · 5 none identified (no data) · 6 **not done** · 7 **not done** · 8 none proposed · 9 tables here; xlsx offered · 10 not offered |
| Not done | Count results; system question; cut-off population; reserve detail; title terms for in-transit / consignment |

Nothing was posted, sent or changed. **Data sources:** upload — `trial_balance_2025-09-30.csv`, `inventory_listing_2025-09-30.csv`, `inventory_movement_12m.csv`.
