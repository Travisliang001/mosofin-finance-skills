# Property accounting — Northbrook Trading Ltd, 2025 (US GAAP)

Mosofin is not connected, so this run is manual: every step is `[manual]`, from your uploads. (Connecting Mosofin would read each property's postings directly — docs.mosofin.com.) **Every entry below is a proposal; nothing has been posted.** No valuation is supplied by this skill.

## 1. Read-back

Accounting for **three properties** of **Northbrook Trading Ltd** (user-asserted), **USD**, from the schedule you uploaded. Your intake gave **September 2025 (as at 30 Sep 2025)**; the schedule states **"Period: 2025"** with full-year rent and costs. I show the full-year 2025 figures the schedule gives and the 30 Sep 2025 position alongside — **please confirm which period you want**.

| Intake | Answer used |
|---|---|
| B — framework | **US GAAP**, found in the schedule; confirm in this read-back. **No IAS 40 investment-property category applies** |
| C — use of each property | From the schedule: Unit 7 rented out; Mill House occupied by the company; Plot 12 under development |
| D — measurement model | Not applicable under US GAAP (cost only). No valuations supplied or needed for the face of the accounts |
| E — land / building split | Given in the schedule (300k/900k; 200k/600k); **basis of the split not supplied** |
| F — lease terms | Unit 7 summary terms in the schedule; no lease document |

## 2. Validation of the upload — shown before any work

| File | What it actually is | Company / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `property_schedule.md` | Property schedule: 3 properties with use, cost, land/building split, in-service date, 2025 rent billed and costs; Unit 7 lease summary; Plot 12 capitalised interest; 40-year building life | No company named; "2025" (full year), not 30 Sep 2025 | Partly: a **summary**, not the ledger; no accumulated depreciation, carrying amounts or deferred-rent balance; lease terms are a summary, not the lease | Yes — Steps 1–7 | **Accepted with a limit**: company user-asserted; period differs from intake (asked above); every figure **user-supplied, not evidenced** |
| `property_schedule_final.csv` | **Not a property schedule.** A staff shift rota: E08–E10, week_1…week_4, "nights / days / off" | No company, properties or amounts | No | No step uses it | **Rejected** on content despite its name. Not used |

**Still missing (required by the checklist):** **ledger detail** for the property, accumulated depreciation, deferred rent, interest and rental income accounts (without it no contradiction test can run on the books); the **Unit 7 lease** itself; for Plot 12, the **borrowing terms** and the dates work paused and resumed. Recommended: the basis of the land/building split.

*I would stop here and wait for your answer. Assumed answer: "go ahead with the accepted files".*

## 3. Findings

### Classification (US GAAP) — evidence and stated use agree

| Property | Stated use | Evidence in the schedule | Classification | Note |
|---|---|---|---|---|
| Unit 7, Dock Road | Rented to a tenant | 108,000 rent billed in 2025 | **PP&E at cost, depreciated** (rental property) | Third-party rent → not owner-occupied; under US GAAP not "investment property" — **no fair value model** |
| Mill House | Occupied by the company | No rent; 34,000 costs | **Owner-occupied PP&E**, cost model | — |
| Plot 12 | Under development | Capitalised interest, no depreciation | **Construction in progress** (land) | Not depreciated; see interest below |

### 1. Unit 7 — rent is not straight-lined (both frameworks require it)

Lease 1 Jan 2024 – 31 Dec 2028, 60 months: 8,000/month in year 1 rising 500 a year, first two months rent-free. Total contractual rent **524,000**, so straight-line income is **8,733.33 a month, 104,800 a year**.

| | 2024 | 2025 | 9 months to 30 Sep 2025 |
|---|---:|---:|---:|
| Contractual rent | 80,000 | 102,000 | 76,500 |
| Straight-line income | 104,800 | 104,800 | 78,600 |
| Deferred rent receivable, closing | **24,800** | **27,600** | **26,900** |

The schedule reports "rent billed" with no deferred rent balance, which is the signature of rent recognised as billed. **Proposed entry (2025, if 2024 was adjusted):** Dr Deferred rent receivable 2,800 / Cr Rental income 2,800. If nothing was ever straight-lined, the 24,800 relating to 2024 is a prior-period error — assess with `restatement-and-prior-period-adjustment` before booking it in 2025. Confirm against the ledger first.

**Billed figure disagrees with the lease:** 2025 is lease year 2, so contractual rent is 12 × 8,500 = **102,000**, but the schedule shows **108,000** (= 12 × 9,000, the year-3 rate) — **6,000 over**. Either the tenant was over-billed or the schedule is wrong. Check the invoices.

### 2. Plot 12 — interest capitalised after work paused

18,000 of interest was capitalised in 2025, **including 6,000 after work paused in June**. Capitalisation stops when activities to get the asset ready are substantially suspended (ASC 835-20), not only at readiness. **Proposed entry:** Dr Interest expense 6,000 / Cr Construction in progress (Plot 12) 6,000, unless the pause was a brief interruption inherent in the work — your judgment, with the dates. Remaining capitalised interest 12,000 needs the borrowing rate and qualifying spend to verify, and must not exceed interest incurred.
**Impairment indicator:** a development whose work has stopped is an indicator for Plot 12. Recoverable amount is not on this surface; **not concluded**.

### 3. Depreciation — land excluded (Test 0a)

| Property | Building | Life | Annual | Accumulated at 30 Sep 2025 | at 31 Dec 2025 |
|---|---:|---:|---:|---:|---:|
| Unit 7 (from 1 Apr 2021) | 900,000 | 40 y | 22,500 | 101,250 | 106,875 |
| Mill House (from 1 Jan 2018) | 600,000 | 40 y | 15,000 | 116,250 | 120,000 |

Land 300,000 + 200,000 + Plot 12 is **not depreciated**. Explicit and implicit land-depreciation tests can be run only against the ledger — expected balances above are the comparison to make. Unit 7 was in service from April 2021 but the lease only from 2024: what it did in 2021–23 is unknown (vacant? change of use?).

### Not found in the schedule
No sale, held-for-sale property or sale-leaseback. Fair value disclosure is not required for US GAAP PP&E. Pledges over property, capital commitments (Plot 12) and restoration obligations are **not in any upload — ask**.

## 4. What was not done, and why

| Item | Status | Needed |
|---|---|---|
| Contradiction tests on the books (0a–0d), register-to-GL both ways | **Not done** | Ledger detail for property accounts |
| Straight-line entry posted / confirmed against ledger | Proposed only | Ledger, lease document |
| Plot 12 interest rate and ceiling check | Not done | Loan agreement, interest incurred |
| Land/building allocation basis | Used as given | Basis (relative fair values) |
| Impairment test (Plot 12) | Indicator only | Recoverable amount |
| Pledges, commitments, restoration provisions | Not done | Mortgage deeds, contracts |
| Posting anything | **Not done — read-only** | A person |

## 5. Coverage and provenance (manual run)

- **A — Environment:** Northbrook Trading Ltd, standalone entity (assumed; confirm), USD, US GAAP (from schedule) — user-asserted; source **upload**; period 2025 per schedule vs 30 Sep 2025 per intake. Files: schedule *accepted with a limit*; `property_schedule_final.csv` *rejected (shift rota)*.
- **B — Capability map:** not applicable — no connection; every task is `[manual]`.
- **C — Steps:** Step 0 tests — on schedule only, not ledger; Step 1 classification — done (your stated use, consistent with evidence); Step 2 — interest finding; Step 3 — depreciation recomputed; Step 4 straight-line — computed; Steps 5 sales — none; Step 6 — indicator only; Step 7 — gaps listed.
- **E — Unknowns:** 6,000 over-billing; Plot 12 pause dates; whether 2024 straight-line was ever booked; Unit 7 use 2021–23.
- **F — Parameters:** US GAAP cost model; 40-year building life (yours); land split as supplied; straight-line over 60 months from 1 Jan 2024.

Would you like this as `Real_Estate_2025_Northbrook_Trading_Ltd.xlsx`? Only on your yes.
