# Government fund statements — Millbrook Township, year to 30 June 2025

This run is manual: no Mosofin connection is present. Everything below comes from the files you uploaded. Nothing has been posted, sent or changed.

## (a) Read-back

Preparing statements for **Millbrook Township** for the **year to 30 June 2025** under **GASB**, in **USD**, from **the trial balance by fund and the notes you uploaded**. Books on **modified accrual for the governmental funds and full accrual for the Water fund**; **three funds** (General, Road, Water) tagged as **classes**. Constraints as listed in your notes; capital assets, debt and the net pension liability as **quoted in your notes**, not from the registers or the actuarial report. Company, period and currency are as you stated them.

Taken from `township_notes.md`, for you to confirm: the framework, the basis, the fund tagging, the constraints, the capital asset and debt totals and the pension figure. Not answered anywhere: **fiduciary funds** (none shown; I assume none, please confirm), **component units** (none assumed), **the availability period** (60 days is the usual GASB period; please confirm yours), and whether **any of the net pension liability belongs to the Water fund**.

What I received:
- `township_trial_balance_by_fund.csv` — 10 rows, columns fund / fund_type / account / amount; balance sheet accounts only for General, Road and Water.
- `township_notes.md` — framework, basis, constraints, and summary figures for capital assets, debt and pension.
- `township_trial_balance_by_fund_final.csv` — three rows, columns employee / week_1..week_4, values nights / days / off.

## (b) Validation of the upload (before any work)

| File | What it actually is | Right company and period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `township_trial_balance_by_fund.csv` | A trial balance by fund: balance sheet accounts for three funds | **Names no government, period or currency** | Columns clear; every fund self-balances (below). **No revenue or expenditure accounts** | Steps 1–6b | **Accepted with a limit**: company and period user-asserted. Balance sheet only, so no operating statement, no Statement of Activities, no revenue/expense test for major funds |
| `township_notes.md` | Management notes: framework, basis, constraints, summary capital asset / debt / pension figures | Millbrook Township; pension report dated 15 Aug 2025 (after year-end, as expected) | Yes | Steps 0b, 4, 5, 6 | **Accepted with a limit**: a summary in place of the capital asset and debt registers and the actuarial report. Those figures are **user-supplied, not evidenced**; no roll-forwards, no deferred outflows / inflows for pensions |
| `township_trial_balance_by_fund_final.csv` | A four-week staff shift roster for employees E08–E10 | No government, date or amount | Not for this skill | No step uses it | **Rejected**. The name suggests a final trial balance by fund; the content is a rota. Set aside. If a final trial balance exists, please upload it |

**Still missing:** the capital asset and long-term debt **registers** (required for government-wide; totals only received), the **actuarial report** (required; one figure quoted), revenue and expenditure accounts by fund (needed for the operating statements), the budget by fund (recommended), and property tax collections in the 60 days after 30 June 2025 (needed for the availability test). I would stop here and wait for your answer.

*You replied: go ahead with the accepted files.*

## (c) Findings

**1. Basis and fund dimension (Step 0b).** A fund dimension exists (classes). Books: modified accrual for General and Road, full accrual for Water, so **the governmental fund statements are book basis and the government-wide statements are the build.** This is consistent with the trial balance: no capital assets or long-term debt in General or Road; both in Water.

**2. Fund structure and self-balancing.**

| Fund | Category | Type | Basis | Assets | Liabilities | Fund balance / net position | Balances? |
|---|---|---|---|---:|---:|---:|---|
| General | Governmental | General Fund | Modified accrual | 960,000 | 95,000 | 865,000 | Yes (0) |
| Road | Governmental | Special Revenue | Modified accrual | 310,000 | 0 | 310,000 | Yes (0) |
| Water | Proprietary | Enterprise | Full accrual | 2,590,000 | 1,500,000 | 1,090,000 | Yes (0) |

Every fund self-balances, so the class is being used as a fund, not a cost tag.

**3. Fund balance classification (governmental funds), each with its constraint.**

| Fund | Nonspendable | Restricted | Committed | Assigned | Unassigned | Total |
|---|---:|---:|---:|---:|---:|---:|
| General | 0 | 0 | 200,000 (board resolution, fire truck) | 50,000 (next year's budget) | **615,000** | 865,000 |
| Road | 0 | 310,000 (state law, road maintenance) | 0 | 0 | 0 | 310,000 |
| **Total** | 0 | 310,000 | 200,000 | 50,000 | 615,000 | 1,175,000 |

Nonspendable is zero because no inventory or prepaid balances appear. The resolution and the state law are cited in your notes, not uploaded; please give the resolution's reference and date.

**4. Property tax receivable — availability not tested.** General carries 140,000 of property tax receivable. Under modified accrual, only the part collected within the availability period (commonly 60 days) is revenue; the rest is a **deferred inflow of resources** (unavailable revenue). Post-year-end collections were not supplied. If none of it is available, the General Fund balance falls to 725,000 and unassigned to **475,000**. It is fully recognised on the government-wide statements either way.

**5. Government-wide: governmental activities, reconciliation from fund balances.**

| Item | Amount | Source |
|---|---:|---|
| Total governmental fund balances (865,000 + 310,000) | 1,175,000 | Trial balance |
| Add capital assets, net of depreciation | 3,100,000 | Notes (register not supplied) |
| Less general obligation debt | (900,000) | Notes (register not supplied) |
| Less net pension liability | (640,000) | Notes, actuarial report 15 Aug 2025 (report not supplied) |
| **Net position of governmental activities (partial)** | **2,735,000** | |

**Not in the bridge, and needed before it is final:** pension deferred outflows and inflows (actuarial report), accrued interest on the 900,000 of GO debt, compensated absences, and the add-back of any property tax deferred in finding 4. These are **missing items, not a residual**; the 2,735,000 is incomplete until they arrive.

Net position categories (assuming all GO debt financed capital assets and no proceeds are unspent): net investment in capital assets 3,100,000 − 900,000 = **2,200,000**; restricted (roads) **310,000**; unrestricted **225,000**.

**6. Business-type activities (Water).** Net position 1,090,000: net investment in capital assets 2,400,000 − 1,500,000 = **900,000**; unrestricted **190,000** (unless the revenue bond covenants require a reserve; not supplied). No pension liability appears in Water; if its staff are in the plan, part of the 640,000 belongs here. **Total primary government net position (partial): 3,825,000.**

**7. Major fund determination (computed this year; thresholds 10% of the category and 5% of governmental plus enterprise combined — please confirm against current GASB).**

| Fund | Assets / category | Assets / combined (3,860,000) | Liabilities / category | Liabilities / combined (1,595,000) | Major? |
|---|---:|---:|---:|---:|---|
| General | 75.6% | 24.9% | 100% | 6.0% | Always major |
| Road | 24.4% | 8.0% | 0% | 0% | **Major** (assets meet both tests) |
| Water | 100% | 67.1% | 100% | 94.0% | **Major** |

Revenues and expenditures were not supplied, so those two elements are not tested; the asset test alone already makes Road major.

**8. Interfund activity.** No interfund receivables, payables or transfers appear in the trial balance. Not tested further: transfer detail for the year was not supplied.

## (d) What was not done, and why

- **Statement of revenues, expenditures and changes in fund balances; Water's operating statement and GASB four-category cash flow statement; Statement of Activities; the net-change reconciliation** — no revenue or expense accounts in the trial balance.
- **Availability test** on the 140,000 property tax receivable — no post-year-end collections.
- **Pension deferred outflows / inflows, pension expense, split between governmental and Water** — actuarial report not supplied. Never estimated.
- **Capital asset and debt roll-forwards, accrued interest** — registers not supplied.
- **Budgetary comparison** for General and Road — no budget.
- **Fiduciary funds, component units** — none shown; assumed none, to confirm.
- **Current GASB standards** — not confirmed in this run (GASB 87 leases, 96 subscriptions); please confirm none apply.
- **Excel workpaper** (`Government_FS_FY2025_Millbrook Township.xlsx`) — not created; say if you want it.
- **Posting** — this skill never posts.

## Coverage (manual run)

| Section | Content |
|---|---|
| Environment | Millbrook Township, year to 30 June 2025, USD — user-asserted. Source: upload. Trial balance accepted with a limit (unnamed; balance sheet only); notes accepted with a limit (summary of registers and actuarial report); `_final.csv` rejected (staff roster) |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 0b done; 1 done (self-balancing proved); 2 done with a limit (availability not tested); 3 done with a limit (balance sheets only); 4 done; 5 done with a limit (partial bridge); 6 done with a limit (pension, debt, capital assets from notes); 6b done with a limit (assets and liabilities only); 7 not done; 8 not applicable (GASB); 9 tables in chat; 10 not offered |
| Not done | Revenue/expenditure statements, availability test, interfund transfer netting, budget comparison: each needs the uploads listed above |

**Data sources:** user-uploaded `township_trial_balance_by_fund.csv` (fund balances) and `township_notes.md` (basis, constraints, capital assets, debt, pension); intake answers (government, period, currency). No ledger read.
