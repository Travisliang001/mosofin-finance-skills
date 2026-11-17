# Production cost report — Northbrook Trading Ltd — September 2025

Mosofin is not connected, so this run is manual: every step is `[manual]` and every figure comes from your uploads. Connecting Mosofin would let costs added and the work in progress (WIP) accounts be read from the books ([docs.mosofin.com](https://docs.mosofin.com)).

## Read-back (Stage 1)

Process costing for **Northbrook Trading Ltd** (user-asserted) for **September 2025**, as at 30 Sep 2025, currency **USD** (user-asserted; no file states a currency), across **Mixing → Filling** (the order in the production report), from **your uploads**. Method **weighted average** (blends opening WIP cost with this month's cost). Materials added **at the start** — applied to both departments, since your answer did not distinguish them (assumption). Normal spoilage: **none**. Department tag in the books (C): not answered; the production report labels rows by department, which is all an upload run needs. Transfer basis between departments: not answered; assumed **at cost** (no internal margin). Who counted the units, and on what date: **not stated**. Go-ahead assumed.

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Needed for | Verdict |
|---|---|---|---|---|---|
| `production_report_2025-09.csv` | Production report, 2 departments: opening WIP units and % complete, units started, completed, closing WIP units and %, materials added, conversion added, opening WIP cost | No entity, currency or date in the file; name says 2025-09 | Yes, but opening WIP cost is **one figure per department, not split** into materials / conversion (and transferred-in for Filling) | Steps 1–5 (units **and** costs added) | **Accepted with a limit**: company, period and currency user-asserted; costs added are a summary inside the production report, not a cost listing, so they are user-supplied, not evidenced; opening WIP split missing |
| `production_report_2025-09_final.csv` | **An employee shift rota** (E08–E10, weeks 1–4: days / nights / off). Not a production report despite its name | None | n/a | No step uses it | **Rejected.** If a final production report exists, please upload it in its place |

**Still missing:**
- **WIP account detail for September** (required for the ledger reconciliation, Step 6) — not supplied; the reconciliation to the books is not run.
- **Costs added by department as a ledger listing** — only the summary in the production report.
- **Opening WIP cost split** by cost element for each department (materials / conversion; plus transferred-in for Filling). Without it, the weighted-average cost per equivalent unit by element cannot be fixed; results below are shown as a range.
- Who supplied the unit counts and completion percentages, and the date of the count.

*I would wait here for your answer; proceeding with the accepted file as instructed.*

## Findings

**1. Units tie in both departments (Step 2).** No spoilage or loss, consistent with normal spoilage of none.

| | Mixing | Filling |
|---|---:|---:|
| Opening WIP + started | 2,000 + 18,000 = **20,000** | 1,000 + 17,000 = **18,000** |
| Completed + closing WIP | 17,000 + 3,000 = **20,000** | 16,500 + 1,500 = **18,000** |
| Difference | 0 | 0 |

Filling's 17,000 started equals Mixing's 17,000 completed and transferred out: the flow Mixing → Filling holds in the units.

**2. Equivalent units, weighted average (Step 3).** Materials at the start mean closing WIP is 100% complete for materials whatever its conversion stage.

| | Mixing | Filling |
|---|---:|---:|
| Transferred-in (100%) | — | 16,500 + 1,500 = 18,000 |
| Materials | 17,000 + 3,000 × 100% = **20,000** | 16,500 + 1,500 × 100% = **18,000** |
| Conversion | 17,000 + 3,000 × 40% = **18,200** | 16,500 + 1,500 × 30% = **16,950** |

**3. Cost per equivalent unit (Step 4) — fixed for costs added, a range for the total.**

Costs added this month, numerator / denominator: Mixing materials 126,000 / 20,000 = **6.3000**; conversion 68,000 / 18,200 = **3.7363**. Filling materials 33,000 / 18,000 = **1.8333**; conversion 52,800 / 16,950 = **3.1150**.

Weighted average also needs opening WIP cost in each element's numerator. Mixing's 14,500 and Filling's 9,900 arrive as single totals, so the per-element rate depends on a split I do not have and will not invent. Mixing, at the two extremes:

| Opening 14,500 assigned to | Materials / EU | Conversion / EU | Transferred out (17,000) | Closing WIP | Total |
|---|---:|---:|---:|---:|---:|
| All materials | 140,500 / 20,000 = 7.0250 | 68,000 / 18,200 = 3.7363 | 182,941.48 | 25,558.52 | 208,500.00 |
| All conversion | 126,000 / 20,000 = 6.3000 | 82,500 / 18,200 = 4.5330 | 184,160.44 | 24,339.56 | 208,500.00 |

**4. Costs assigned (Step 5).** Mixing: total to account for **208,500** (14,500 + 126,000 + 68,000). Transferred to Filling **182,941 – 184,160**; closing WIP **24,340 – 25,559** — a swing of 1,219 driven only by the missing split.

Filling: total to account for = 9,900 opening + transferred-in (182,941 – 184,160) + 33,000 + 52,800 = **278,641 – 279,860**. Across the four split combinations, completed to finished goods is **258,420 – 260,099** (16,500 units, **15.66 – 15.76 per unit**) and closing WIP **19,660 – 20,323**. With the split, both become single figures.

**5. Internal roll-forward ties (Step 6, internal half).** In every combination, transferred out + closing WIP = total to account for (Mixing 208,500.00; Filling equal to its total), so the arithmetic is sound. **The ledger half was not run**: no WIP account detail was uploaded, so opening WIP, costs added, transfers and closing WIP are not agreed to the books. This model reconciles to itself only.

**6. Proposed entries (Step 7) — proposals only, nothing posted.** Amounts final once the split arrives; real account names need your chart of accounts.

```
DR WIP – Filling          182,941 – 184,160     CR WIP – Mixing         (transfer at cost)
DR Finished goods         258,420 – 260,099     CR WIP – Filling        (16,500 units completed)
```

**7. Reasonability (output checks).** No prior-period unit cost was supplied, so no period comparison. Method stated: weighted average throughout; no method change can be detected from one period.

## What was not done, and why

- **Ledger reconciliation (Step 6, to the books)** — no WIP account detail; upload September WIP account activity per department.
- **Single cost per EU and single assigned amounts** — opening WIP cost not split by element; supply the split.
- **Costs added agreed to postings** — costs came as a summary in the production report; upload the departmental cost listing.
- **DM vs conversion classification check** — no account-level cost data.
- **Count source and date** — not stated; every unit count and percentage below is "user-supplied, source and date unknown".
- **Excel workpaper** — not created; I would ask first (`Process_Costing_2025-09_Northbrook Trading Ltd.xlsx`).

## Coverage sheet (manual run)

**Environment:** Northbrook Trading Ltd, September 2025, USD — all user-asserted. Data source: upload (gateway absent). Files: `production_report_2025-09.csv` accepted with a limit (company/period user-asserted; opening WIP unsplit; costs a summary); `production_report_2025-09_final.csv` rejected (shift rota).

**Capability map:** Not applicable: no connection. Every task is `[manual]`.

| Step | Status | Note |
|---|---|---|
| 0 Fetch evidence | Done with a limit | One usable file; WIP account detail missing |
| 1 Map flow | Done with a limit | Mixing → Filling from the report; not compared to posted transfers (no ledger) |
| 2 Physical units | Done | Both tie; source and count date unknown |
| 3 Equivalent units | Done | Weighted average; materials at start |
| 4 Cost per EU | Done with a limit | Costs-added rates fixed; totals a range (opening unsplit) |
| 5 Assign costs | Done with a limit | Ranges |
| 6 Reconcile | Internal done; **ledger not done** | No WIP account detail |
| 7 Postings | Proposed, not posted | Account names placeholders |
| 8 Save preferences | Not done | Offered only after results are approved |

**Data sources:** user upload — `production_report_2025-09.csv` (units, completion %, costs added, opening WIP cost). Nothing was posted, sent or changed anywhere.
