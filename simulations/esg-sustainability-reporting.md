# ESG reporting design — Northbrook Trading Ltd — 2025

Mosofin is not connected, so this run is manual: every step is `[manual]` and every figure comes from your uploads. Connecting Mosofin would read spend by vendor and category directly ([docs.mosofin.com](https://docs.mosofin.com)). Nothing is published or submitted; this is a design and a first calculation for you to review. **Not assurance-ready by my say-so** — the list at the end is what an assurer would ask for.

## Read-back

Designing ESG reporting for **Northbrook Trading Ltd** (user-asserted), **USD**, period **2025** (your intake gives September 2025 as the as-at date; see the period question below). From `esg_scope_and_factors.md` (facts that arrived inside a file; used once you confirm them here): purpose **customer requests**; boundary **operational control, two sites** (Texas warehouse, California office); **no framework yet**; emission factors **you supplied** — electricity 0.40 kg CO₂e/kWh, diesel 2.70 kg CO₂e/litre, "sample factor set 2025"; **no assurance planned; nothing published before**. Go-ahead assumed.

**Assumption, stated because it is not answered:** the activity file says "2025" with no dates, while the P&L runs **January – September 2025**. I have treated the activity data as **January – September 2025** so that intensities use matching periods. If it is a full-year figure or an estimate, the intensities below change; the totals do not.

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Needed for | Verdict |
|---|---|---|---|---|---|
| `esg_activity_data_2025.csv` | Activity data, 5 rows: electricity Texas 412,000 kWh (utility bills) and California 38,000 kWh (landlord statement); diesel 9,600 litres (fuel card); headcount 12 (payroll); business flights **blank** ("not collected — spend only", no owner) | No entity; "2025", **no period dates** | Yes for four rows; flights row empty | Steps 1–3 | **Accepted with a limit**: company user-asserted; period assumed Jan – Sep 2025; **flights not reportable** |
| `esg_scope_and_factors.md` | Scope note: purpose, boundary, framework, two emission factors with source, assurance and publication history | No entity named | Yes. Factors give a source and year but **no version**, and are marked sample/fictitious | Steps 1, 2 (factors) | **Accepted with a limit**: factors **user-supplied**, not checked against any database by me |
| `profit_and_loss_2025_ytd.csv` | Monthly P&L, Jan – Sep 2025, 9 months, revenue 4,038,600 | No entity or currency | Yes; summary lines only, **no utilities, fuel, travel or freight lines** | Intensity denominator; Scope 3 spend mapping; reconciliation test | **Accepted with a limit**: company and currency user-asserted |
| `esg_activity_data_2025_final.csv` | **An employee shift rota** (E08–E10, weeks 1–4). Not activity data, despite its name | None | n/a | No step uses it | **Rejected.** If a later activity file exists, upload it instead |

**Still missing:** the **period the activity data covers**; the **factor version** and whether electricity should be **location-based or market-based**; a **separate grid factor for each site** (Texas and California grids differ — one factor for both is a known error); **flight distances** or at least travel spend with an owner; a **spend breakdown** by supplier/category (utilities, fuel, travel, freight are not separate P&L lines). Would wait here; proceeding on the accepted files.

## Scope and boundary (Step 1)

| Item | Decision |
|---|---|
| Organisational boundary | **Operational control**, 100% of the two sites (Texas warehouse, California office). Both appear to be leased (rent 9,000 a month in the P&L); operational control of a leased site keeps it in scope |
| Operational boundary | Scope 1: diesel (forklifts, van). Scope 2: purchased electricity, two sites. Scope 3: **not yet in scope** — business travel and purchased goods named below as gaps |
| Period / frequency | Calendar 2025, annual; matches the fiscal year in the P&L |
| Difference from financial boundary | None identified — single company; please confirm no other entity or site |

## First calculation — measured activity × your factors

| Metric | Site | Activity | Factor (source as given) | tCO₂e | Basis |
|---|---|---:|---|---:|---|
| Scope 2 electricity | Texas warehouse | 412,000 kWh | 0.40 kg/kWh, "sample factor set 2025" | 164.80 | Calculated from metered/billed kWh |
| Scope 2 electricity | California office | 38,000 kWh | same factor — **site-specific factor needed** | 15.20 | Calculated; landlord statement |
| **Scope 2 total** | | 450,000 kWh | | **180.00** | Location- or market-based **not stated** |
| Scope 1 diesel | Texas warehouse | 9,600 litres | 2.70 kg/litre | **25.92** | Calculated from fuel-card litres |
| **Scope 1 + 2** | | | | **205.92** | |
| Scope 3 business travel | All | — | — | **not reported** | No distance, no owner, no travel line in the P&L |
| Scope 3 purchased goods | All | — | — | **not reported** | No spend factor supplied; COGS 2,370,856 Jan – Sep is the candidate spend, an estimate tier only |

Intensities (on the Jan – Sep assumption): **51.0 tCO₂e per USD million of revenue** (205.92 ÷ 4.0386); **17.2 tCO₂e per employee** (205.92 ÷ 12). Electricity is **87%** of the Scope 1 + 2 total. Nothing published before, so no year-on-year comparison and no restatement issue.

## Metric catalogue (Step 2)

| Metric | Unit | Owner | Source system | Calculation | Tier | Controls |
|---|---|---|---|---|---|---|
| Electricity, Texas | kWh | Facilities manager | Utility bills | Sum of billed kWh × site grid factor | Measured | Bills reconciled to months; meter reads checked |
| Electricity, California | kWh | Office manager | Landlord statement | Allocated kWh × site grid factor | Allocated (landlord) | Ask for allocation basis |
| Diesel | litres | Facilities manager | Fuel card | Litres × diesel factor | Measured | Card totals tied to fuel spend |
| Headcount | employees | HR | Payroll | Period-end count; define FTE vs heads | Measured | Tie to payroll register |
| Business flights | km | **No owner** | **Not collected** | Distance × class factor | — | Assign owner; collect from travel bookings |
| Purchased goods (Scope 3 cat. 1) | tCO₂e (estimate) | Finance | Ledger by supplier | Spend × spend factor (currency and year stated) | **Estimate from spend** | Reconcile spend to P&L |
| Water, waste, DEI, safety, governance | m³ / t / various | To assign | Not collected | — | — | Catalogued, not yet produced |

**Not reportable this year as it stands:** business flights — **no owner and no source**, so it cannot be reported, and no spend figure exists to estimate it.

## Pipeline and controls (Step 3)

Each figure: source document retained per month; factor, version and year recorded against it; second-person review before release; catalogue versioned. **Reconciliation test:** Jan – Sep operating spend in the P&L is **3,378,085** (COGS, payroll, rent, marketing, software, professional fees, bank fees); **none** of it is used yet, because utilities, fuel and travel are not separate lines — map those accounts first so energy and fuel spend can be tied to the kWh and litres. **Spend is not consumption:** no figure above is derived from spend.

## What an assurer would ask for (not claiming readiness)

Utility bills and the landlord's allocation basis; fuel-card statements; the factor database with version; site-specific grid factors; the period definition; evidence of review; a statement of what is excluded (Scope 3) and why.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, 2025, USD — **user-asserted**; operational control, two sites. Data source: **upload**. Activity data, scope note, P&L accepted with limits; `esg_activity_data_2025_final.csv` **rejected** (shift rota) |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps 1–2 | Done; Scope 3 catalogued, not computed |
| Step 3 | Designed; reconciliation test **not passed** — spend not mapped |
| Step 4 | Done as tables; no trend (first year) |
| Not done | Flights, Scope 3, water, waste, social metrics, site-specific factors, period confirmation |

Nothing was published or submitted. **Data sources:** upload — `esg_activity_data_2025.csv`, `esg_scope_and_factors.md`, `profit_and_loss_2025_ytd.csv`.
