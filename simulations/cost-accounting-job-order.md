# Job costing — Northbrook Trading Ltd — September 2025

Mosofin is not connected, so this run is manual: every step is `[manual]` and every figure comes from your uploads. Connecting Mosofin would read job-tagged postings, time and the overhead pool directly ([docs.mosofin.com](https://docs.mosofin.com)).

## Read-back

Costing jobs for **Northbrook Trading Ltd** (user-asserted) for **September 2025**, in **USD** (user-asserted), from **your uploads**. From `job_costing_policy.md` (facts that arrived inside a file; used once you confirm them here): jobs **tagged by project**; overhead pool **rent, depreciation and software**; overhead applied on **direct labour hours at a predetermined 28.00 an hour** (set January 2025 from the budget); labour costed at **46.00 an hour**; **J-301 contract price 60,000, J-302 31,000**; **J-298 invoiced 9,800 and closed in August**. Job status (open / closed) taken from the cost file. Revenue basis: the policy gives fixed contract prices, so this is read as **fixed fee** — please confirm.

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Needed for | Verdict |
|---|---|---|---|---|---|
| `job_costs_2025-09.csv` | Cost by job: 3 jobs (J-301, J-302 open; J-298 closed) and 2 **untagged** lines. Materials 30,700 tagged + 4,540 untagged (incl. 1,900 subcontractor); 306 labour hours | No entity; period from file name only; **no date, vendor or account on any line** | Yes, with limits | Steps 0b, 1, 3, 4, 5 | **Accepted with a limit**: company and period user-asserted; cut-off and vendor-level untagged report cannot be done |
| `job_costing_policy.md` | Costing policy: tag, pool, base, rates, contract prices, J-298 status | No entity or date beyond "January 2025" for the rate | A summary; the **budget behind 28.00 is not supplied** | Steps 1, 2, 4, 7 | **Accepted with a limit**: rates and prices **user-supplied, not evidenced** |
| `job_costs_2025-09_final.csv` | **An employee shift rota** (E08–E10, weeks 1–4: days / nights / off). Not job cost data despite its name | None | n/a | No step uses it | **Rejected.** If a revised job cost file exists, upload it instead |

**Still missing:** (1) **actual September overhead** in the pool (rent, depreciation, software) — needed for under/over-applied overhead; (2) **opening WIP by job** and the **WIP account balance** at 30 Sep — needed for the roll-forward and its reconciliation; (3) **J-298's cost to August** — to see the job's full cost against its 9,800 billing; (4) **estimates / cost-to-complete** for J-301 and J-302; (5) billings to date. I would wait here; proceeding on the accepted files as instructed.

## Step 0b — Untagged cost (reported before any margin)

| | Amount | Share |
|---|---:|---:|
| Direct cost tagged to a job (materials 30,700 + labour 306 h × 46.00 = 14,076) | 44,776 | 90.8% |
| **Untagged**: materials 2,640; subcontractor 1,900 | **4,540** | **9.2%** of total direct cost 49,316 (12.9% of posted materials and subcontract, 35,240) |

**This is material.** 4,540 of cost belongs to some job and sits in none, so **every job figure below is understated by an unknown share of it**. The file gives no vendor, date or account for the two lines, so I cannot say which jobs they belong to. Untagged cost is **not** spread across jobs. Please trace the two postings and re-tag them in your system.

## Job cost sheets — September (labour at 46.00, overhead at 28.00 per labour hour)

| Job | Customer | Status | Materials | Labour hours | Labour cost | Overhead applied | **Cost in September** | Contract price | Cost as % of price |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| J-301 | Ashby Engineering | open | 18,400 | 210 | 9,660 | 5,880 | **33,940** | 60,000 | 56.6% |
| J-302 | Tideswell Hotels | open | 9,200 | 96 | 4,416 | 2,688 | **16,304** | 31,000 | 52.6% |
| J-298 | Brecon Outdoor | **closed (Aug)** | 3,100 | — | — | — | **3,100** | invoiced 9,800 | see below |
| Untagged | — | — | 4,540 | — | — | — | **4,540** | — | — |
| **Total** | | | 35,240 | 306 | 14,076 | **8,568** | **57,884** | | |

Notes: labour is **hours (measured) × a rate you supplied**, not payroll cost. September cost only — opening WIP was not supplied, so these are not cumulative job costs. **No margin is reported for J-301 or J-302**: they are open, the contract price is not yet earned, and without an estimate of cost to complete the remaining 26,060 / 14,696 of price is headroom, not margin.

## Findings

1. **J-298 has 3,100 of materials posted in September after the job closed in August.** Either a late supplier invoice for work done before close (a cut-off item — the cost belongs to August and to cost of sales), or a mis-tag of cost that belongs to an open job. It must **not** sit in WIP for a closed job. J-298's margin against its 9,800 billing cannot be stated without its August cost; the September cost alone is **31.6% of the billing**.
2. **Untagged cost of 4,540 (9.2%)** — above; reported before any figure.
3. **Overhead applied 8,568** (306 h × 28.00: J-301 5,880; J-302 2,688). **Under/over-applied overhead not computed**: no September actuals for rent, depreciation or software were supplied. Pool listed account by account as per policy: rent, depreciation, software — no other account, and no one-off item visible, but the pool balances themselves are unseen.
4. **WIP roll-forward not reconciled**: September additions to WIP are J-301 33,940 and J-302 16,304 (50,244); opening WIP, relief to cost of sales and the WIP account balance were not supplied.

## Proposed entries (proposals only — not posted)

- Apply overhead to open jobs: DR WIP – J-301 5,880; DR WIP – J-302 2,688 / CR Applied Overhead 8,568.
- J-298: **no entry proposed** until you confirm whether the 3,100 is a late August cost (then to cost of sales, not WIP) or belongs to another job.
- Under/over-applied overhead: entry deferred until pool actuals arrive (policy for closing it to COGS or prorating also not stated).

## Not done, and why

Under/over-applied overhead and its treatment (no pool actuals; no policy). WIP roll-forward and reconciliation to the WIP account (no opening WIP or balance). Variance against estimate (no estimates). Cut-off tests and the vendor-level untagged report (no dates, vendors or accounts in the file). Phase / cost-code view (no such dimension). Actual-rate sanity check on 28.00 (no prior-year pool and hours). Excel workpaper `Job_Costing_2025-09_Northbrook Trading Ltd.xlsx` offered; not created without your yes.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, September 2025, USD — **user-asserted**. Source: **upload** (Mosofin not used, your choice). Job dimension: **project** (per policy). Job cost file and policy: accepted with limits. `job_costs_2025-09_final.csv`: **rejected** (shift rota) |
| Capability map | Not applicable: no connection. Every task is `[manual]`; labour rate and overhead rate **supplied**, hours **from the file** |
| Steps | 0b done (4,540 untagged, 9.2%) · 1 done (materials, labour, subcontract, applied overhead) · 2 done from policy, budget not evidenced · 3 done for September · 4 applied done; actual **not done** · 5 additions only, **not reconciled** · 6 **not done** · 7 job cost report done; margin and variance **not done**; WIP aging limited to J-298 · 8 not offered |
| Not done | Pool actuals; opening WIP and WIP balance; J-298 August cost; estimates; billings; dated, vendor-level cost detail |

Nothing was posted, sent or changed. **Data sources:** upload — `job_costs_2025-09.csv`, `job_costing_policy.md`.
