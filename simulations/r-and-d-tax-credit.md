# R&D tax credit workpaper — Northbrook Trading Ltd, Sampleland, tax year 2025

Mosofin is not connected, so this run is manual: every step is `[manual]`, from your uploads. (Connecting Mosofin would automate the cost reads — docs.mosofin.com.) **This is a computation for a qualified tax professional to review, not tax advice. Nothing has been filed, posted or changed.**

## 1. Read-back

Preparing the **2025 R&D claim** for **Northbrook Trading Ltd** (user-asserted), jurisdiction **Sampleland**, in **USD**, from your uploads. Your intake gave the jurisdiction and year only. The answers below were **found inside `rd_projects_and_time.md`** and are used only once you confirm them here:

| Intake | Answer as found in your file | Status |
|---|---|---|
| C — regime, rate, source, year | "Sampleland R&D credit", **12% of qualifying cost**, SME scheme; source "sample rate card v1, tax year 2025". File marks it **fictitious, for testing** | User-supplied; **please confirm**. No restriction rate for subcontractors and no cap is given |
| D — projects | P1 Self-aligning bracket; P2 Warehouse layout review; P3 ERP configuration, each with a one-line description | Descriptions only; **which ones you judge to qualify is not stated** |
| E — staff time split | E01 40%, E02 60% (P1); E08 20% (P2); E06 15% (P3), "of the year" | Split given; **basis (timesheets? estimates?) not stated** |
| F — size, grants, subcontractors | SME; no grants; profitable; one subcontracted testing lab on P1 | User-asserted; group/linked enterprises not stated |

## 2. Validation of the upload — shown before any work

| File | What it actually is | Company / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `rd_projects_and_time.md` | A **summary note**: regime and rate, three project descriptions, staff % per project, P1 materials 14,200 and subcontractor 8,000, no grants, SME | No company named; "tax year 2025" | Partly: one-line descriptions, no technical narrative, no cost listing behind 14,200 / 8,000, no time records | Yes — Steps 1–5 | **Accepted with a limit**: a summary, not source documents. Every figure from it is **user-supplied, not evidenced** |
| `payroll_register_2025-09.csv` | Payroll register: 12 employees, gross 70,599, net 53,902; every row foots (gross − deductions = net) | No company; **September 2025 only**; no currency column (USD user-asserted) | Partly: **one month, not the tax year**; employee withholdings only, **no employer costs** | Yes — staff cost pool, Step 4 | **Accepted with a limit**: supports September staff cost only; the annual staff cost and employer costs cannot be computed |
| `rd_projects_and_time_final.csv` | **Not a time allocation.** A staff shift rota: E08–E10, week_1…week_4, "nights / days / off" | No company, no project, no hours | No | No step uses it | **Rejected** on content despite its name. If you hold timesheets by project, upload those |

**Still missing (required):** the **full-year 2025 payroll** with employer costs; **time records** or the basis of the staff split; **technical narratives** per project; invoices or ledger listing for the P1 materials and the testing lab; the **subcontractor restriction rule** and any cap from your rate card. **Flag now, not later:** whether Sampleland requires **advance notification** or has a claim deadline — a missed notification can extinguish the claim.

*I would stop here and wait for your answer. Assumed answer: "go ahead with the accepted files".*

## 3. Findings

### Step 2 — qualifying activity: the tests, for your decision (not decided here)

| Project | Advance sought? | Technical uncertainty? | Systematic process? | What your description says | Qualifies? |
|---|---|---|---|---|---|
| P1 Self-aligning bracket | "new joint geometry" | "outcome uncertain at the start" | "three failed prototypes" | Describes all three tests | **Your decision** — narrative needed |
| P2 Warehouse layout review | Not described | Not described | Not described | "re-arranging racking **using known methods**" | **Your decision** — reads as routine, applying existing techniques |
| P3 ERP configuration | Not described | Not described | Not described | "**standard configuration** of bought software" | **Your decision** — reads as routine configuration |

**Over-claim risk:** P2 and P3, as you describe them, fall in the method's "usually does not qualify" list (known methods; routine configuration of software). Including them would claim routine work. I have not decided this; I show the result both ways and recommend specialist review. The P1 boundary (start / end of uncertainty) is also undetermined — no dates were supplied.

### Step 4 — cost by project and category (USD)

| Project | Category | Gross cost | Apportionment / basis | Restriction | Qualifying amount | Source |
|---|---|---:|---|---|---:|---|
| P1 | Materials (prototypes) | 14,200 | 100%, direct | None stated | 14,200 | User-supplied, not evidenced |
| P1 | Subcontractor testing lab | 8,000 | 100%, direct | **Unknown — rule not supplied** | blocked | User-supplied, not evidenced |
| P1 | Staff E01 (Sep only) | 7,246 | 40%, basis not stated | — | 2,898.40 | Payroll register |
| P1 | Staff E02 (Sep only) | 4,830 | 60%, basis not stated | — | 2,898.00 | Payroll register |
| P2 | Staff E08 (Sep only) | 3,994 | 20% | — | 798.80 | Payroll register |
| P3 | Staff E06 (Sep only) | 6,874 | 15% | — | 1,031.10 | Payroll register |

Staff figures are **September 2025 gross pay only**, with no employer costs. The split was stated as a share **of the year**; applying it to one month gives a September figure, not the annual claim. I have **not annualised** it — the full-year payroll is needed. The 401(k) column is the employee's deferral, already inside gross; no employer contribution is shown.

### Step 5 — benefit at the supplied 12% (credit mechanism)

| Scenario | Qualifying cost | Credit at 12% |
|---|---:|---:|
| **A. P1 only, evidenced-so-far basis**: materials only | 14,200.00 | **1,704.00** |
| B. P1 materials + testing lab at 100% (if no restriction applies) | 22,200.00 | 2,664.00 |
| C. B + P1 September staff | 27,996.40 | 3,359.57 |
| D. C + P2 and P3 September staff (if you judge them qualifying) | 29,826.30 | 3,579.16 |

None of these is the claim: the annual staff cost is missing in every scenario. The P2 + P3 difference (1,829.90 of cost, **219.59** of credit) is what including routine work would add on September figures alone. Interaction with the return: the company is profitable, so a credit would ordinarily reduce corporation tax payable; whether Sampleland's credit is payable in cash, or can be carried forward, is not on the rate card — hand to `tax-return-prep-corporate` and `corporate-tax-provision-asc740`.

### Completeness, grants, capital vs revenue

- **Grants:** you state none; no ledger was supplied to sweep grant receipts or deferred grant income, so this is user-asserted, not checked.
- **Cost population:** no vendor ledger supplied, so cloud, software and other candidate R&D spend could not be swept. Only the three projects you named are in view.
- **Capitalised development:** not checked; no balance sheet supplied.
- **Thin records:** no contemporaneous time records, no narratives, no invoices — reconstruction risk is high.

## 4. What was not done, and why

| Item | Status | Needed |
|---|---|---|
| Qualifying-activity decision; P1 boundary | **Not done — your judgment** | Technical narratives, start/end dates |
| Annual staff cost; employer costs | **Blocked** | Full-year 2025 payroll with employer costs |
| Staff apportionment basis | Split used as given; basis unknown | Timesheets or structured estimates |
| Subcontractor restriction; caps | **Blocked** | The rule from your rate card |
| Completeness and grant sweep; capitalised costs | Not done | Ledger / vendor listing / balance sheet |
| SME status with linked enterprises; notification deadline | Not checked | Group structure; Sampleland procedure |
| Filing; specialist review | **Not done** | A qualified tax professional |

## 5. Coverage and provenance (manual run)

- **A — Environment:** Northbrook Trading Ltd, Sampleland, tax year 2025, USD — user-asserted; source **upload**; schedules assembled 15 Nov 2026 from a September 2025 payroll and a summary note (a **reconstruction**, not contemporaneous). Files: note *accepted with a limit*; payroll *accepted with a limit (one month)*; `rd_projects_and_time_final.csv` *rejected (shift rota)*.
- **B — Capability map:** not applicable — no connection; every task is `[manual]`.
- **C — Steps:** Step 1 regime — user-supplied, unconfirmed; **Step 2 — entirely human, not done**; Step 3 boundary — not done; Step 4 — done with a limit (September staff, subcontractor blocked); Step 5 — scenario arithmetic only; Step 6 documentation — index of what is missing; Step 7 — this pack.
- **D — Not done:** listed in section 4.
- **E — Unknowns:** P1–P3 qualification; subcontractor rule; annual payroll; grant sweep; notification deadline.
- **F — Parameters:** rate 12% from "sample rate card v1, tax year 2025" (user file, fictitious); staff % as supplied; no annualisation; no vendor filters (no ledger).

Would you like the workbook as `R&D_Claim_2025_Northbrook_Trading_Ltd.xlsx`? Only on your yes.
