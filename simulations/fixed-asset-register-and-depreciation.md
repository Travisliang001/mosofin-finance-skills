# Fixed asset register and depreciation — Northbrook Trading Ltd, September 2025 (upload path)

Mosofin is not connected for this run (you chose upload only), so every step is `[manual]` and works from your files. Connecting Mosofin would automate the reads — docs.mosofin.com. Nothing was capitalized, depreciated, disposed of or posted: every entry below is a **proposal** for you to review and enter yourself.

## (a) Read-back

Reviewing the **fixed asset register, September depreciation and the GL tie-out** for **Northbrook Trading Ltd** (user-asserted; no file names the company), **September 2025, as at 30 September 2025**, in **USD** (user-asserted), single entity.

| Not answered at intake | What I did (the skill never defaults these) |
|---|---|
| Useful lives by class | Not defaulted: used the per-asset lives **in your register** (labelled register-supplied). No class policy given. |
| Method | Register gives life only. Computed **straight-line** as the only method the data supports; labelled an assumption. |
| Salvage values | None in the register. Computed at **zero salvage** (the conservative reading: highest charge). Labelled an assumption. |
| First/last-period convention | **Not defaulted** — shown under **full-month** and **half-month**; they differ only for assets placed in service mid-month. |
| Capitalization threshold | **Not given** → the threshold scan (Step 2b) **not run**. |
| Framework, tax jurisdiction, impairment indicators | Not given. No componentization, revaluation or tax depreciation attempted. |

## (b) Validation of the upload — shown before any work

| File | What it actually is | Company / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `fixed_asset_register.csv` | Asset register: 8 assets with id, description, in-service date, cost, useful life | No company or as-at date | Cost foots to **420,000** = GL 1500. No class, method, salvage, location or accumulated depreciation columns. FA-008 is described "sold Jul 2025" but still listed | Yes — Steps 1, 5, 9 | **Accepted with a limit**: company user-asserted; method, salvage and convention not stated |
| `general_ledger_2025-09.csv` | September GL extract, 29 lines: 15 bank-account lines (one side only, 1000) and 7 journals (14 lines) | Dates 31 Aug–30 Sep 2025; no company | Journals balance (DR = CR = 79,799). Bank lines carry no offset account, so what Kestrel 64,200 or Orchard Packaging 3,150 bought cannot be seen. No movement on 1500; 1510 credited 4,200 by JE-0901 | Yes — additions, disposals, depreciation posted (Steps 0, 2, 8, 9) | **Accepted with a limit**: bank-side lines only; also posts 1,500 to 6150 Insurance, which has no balance in the TB, so GL and TB are not from one consistent cut |
| `trial_balance_2025-09-30.csv` | Trial balance, 29 accounts | No company or date in the file | Foots (6,589,681). 1500 cost 420,000; 1510 accumulated depreciation 311,200; 6600 YTD 37,800 | Yes — GL balances for the tie-out (Step 9) | **Accepted with a limit: company and period user-asserted** |
| `fixed_asset_register_final.csv` | **Not a register.** A staff shift rota: employee E08–E10, week_1…week_4, "nights/days/off" | No company, assets or amounts | No | No step | **Rejected** on content despite the name. Not used. If a later register exists, upload it. |

Still missing: **capitalization threshold** (required for Step 2b); **convention** and **method/salvage policy** (required — shown under alternatives meanwhile); **accumulated depreciation by asset** or the prior register (to explain Finding 1); **July 2025 GL** (proceeds of the FA-008 sale); **full September GL with offset accounts** (additions and the repairs scan); date and owner of the last physical count.

*I would stop here and wait for your answer. Assumed answer: "go ahead with the accepted files".*

## (c) Findings

**Register, straight-line, zero salvage, as at 30 Sep 2025:**

| Asset | Description | In service | Cost | Life | Monthly | Accum. dep. (full-month) | NBV | Sep charge |
|---|---|---|---:|---:|---:|---:|---:|---:|
| FA-001 | Warehouse racking | 2021-03-01 | 96,000 | 10 | 800.00 | 44,000.00 | 52,000.00 | 800.00 |
| FA-002 | Forklift | 2021-06-15 | 54,000 | 7 | 642.86 | 33,428.57 | 20,571.43 | 642.86 |
| FA-003 | Delivery van | 2022-01-10 | 62,000 | 5 | 1,033.33 | 46,500.00 | 15,500.00 | 1,033.33 |
| FA-004 | Office fit-out | 2020-09-01 | 88,000 | 10 | 733.33 | 44,733.33 | 43,266.67 | 733.33 |
| FA-005 | Servers | 2020-01-20 | 36,000 | 5 | 600.00 | 36,000.00 | 0.00 | 0.00 (fully depreciated Dec 2024) |
| FA-006 | Packing line | 2023-04-01 | 58,000 | 8 | 604.17 | 18,125.00 | 39,875.00 | 604.17 |
| FA-007 | Laptops batch 1 | 2022-08-01 | 14,000 | 3 | 388.89 | 14,000.00 | 0.00 | 0.00 (fully depreciated Jul 2025) |
| FA-008 | Delivery van (sold Jul 2025) | 2019-05-01 | 12,000 | 5 | 200.00 | 12,000.00 | 0.00 | 0.00 |
| **Total** | | | **420,000** | | | **248,786.90** | **171,213.10** | **3,813.69** |

Half-month convention: accumulated depreciation 247,948.81 (FA-002 and FA-003 half a month less); September charge unchanged at 3,813.69.

1. **Depreciation is still posted at 4,200 a month after FA-007 became fully depreciated.** The recurring JE-0901 (4,200) matched the register Jan–Jul 2025 (4,202.58 a month) but FA-007's 388.89 stopped at end-July. September should be **3,813.69**: **overcharged 386.31 in September** and again in August. YTD recorded 37,800 vs register **37,045.44** (full-month) or **37,345.44** (half-month) → **overcharged 754.56 or 454.56**. Implied life from the recorded charge: 50,400 / 420,000 = 8.3 years.
2. **The July 2025 sale of FA-008 is not recorded.** The register marks the van sold but keeps it, and register cost including it (420,000) equals GL 1500 exactly, so its **cost of 12,000 and accumulated depreciation of 12,000 are still on the books**. NBV is nil, so the whole proceeds are a gain; proceeds are not in the files (July GL needed) and the chart has no gain/loss-on-disposal account.
3. **GL accumulated depreciation does not tie to the register.** GL 1510 = **311,200**; register (zero salvage, full-month) = **248,786.90**; **difference 62,413.10** (62,413 + 838 = 63,251.19 on half-month). GL NBV 108,800 vs register NBV 171,213.10. Possible causes: depreciation on assets removed from the register, wrong lives, or salvage — needs accumulated depreciation by asset. No adjustment is proposed until it is explained.
4. **Fully depreciated assets still carried:** FA-005 Servers (36,000, nil NBV since Dec 2024) and FA-007 Laptops (14,000, nil since Jul 2025). Confirm whether in use — replacement and impairment-review candidates, not conclusions.
5. **No additions or disposals in September:** no debits or credits to 1500 in the GL extract; GL → register direction finds no unrecorded asset this month. Register → GL: no phantom except FA-008 (Finding 2). Land and CIP: no such accounts.
6. **Physical count:** no evidence it has ever been performed. Owner and date to be set — that absence is the finding.

**Roll-forward, 1 Sep → 30 Sep 2025 (GL):** cost 420,000 + 0 − 0 = 420,000; accumulated depreciation 307,000 + 4,200 − 0 = 311,200; NBV 108,800.

**Proposed entries (not posted):**

| # | Entry | Amount | Condition |
|---|---|---:|---|
| P1 | DR 1510 Accumulated Depreciation / CR 1500 Fixed Assets – Cost — remove FA-008 | 12,000 | Confirm sale date |
| P2 | DR cash or receivable where the proceeds sit / CR gain on disposal (new account needed) | proceeds | July GL and sale document |
| P3 | DR 1510 / CR 6600 Depreciation — reverse YTD overcharge | 754.56 (full-month) or 454.56 (half-month) | Convention and salvage confirmed; Finding 3 explained first |
| P4 | Change recurring JE-0901 to 3,813.69 from October | — | Same as P3 |

## (d) Not done, and why

Threshold scan both ways (no threshold; GL lacks expense-side detail; 6160 Repairs has no balance); capitalized-cost build-up (no invoices); impairment test (no cash flows; candidates only); tax-book depreciation (no jurisdiction); physical count (physical act). No `.xlsx` created — I would ask whether you want `FA_Register_and_Depreciation_2025-09.xlsx`.

## (e) Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, 30 Sep 2025, USD — user-asserted. Source: upload. Register, GL, TB accepted with limits; `fixed_asset_register_final.csv` rejected (staff rota). |
| Capability map | Not applicable: no connection. Every task is `[manual]`. |
| Steps | 1 classes done with limit (no class policy; lives from register) · 2 capitalization **not done** (no invoices, threshold) · 2b threshold scan **not done** · 3 method assumed SL · 4 convention shown both ways · 5 depreciation done with limit · 6 depreciation JE proposed (P3, P4) · 7 no additions · 8 disposal FA-008 proposed (P1, P2) · 9 roll-forward done; tie-out **fails by 62,413.10** · 10 impairment candidates only · 11 count **not done**, owner unassigned · 12 tables in chat · 13 not offered. |
| Not done | AD tie by asset (upload AD by asset or prior register); disposal proceeds (July GL); threshold scan (threshold + full GL); count (owner, date). |

**Data sources:** user uploads — `fixed_asset_register.csv`, `general_ledger_2025-09.csv`, `trial_balance_2025-09-30.csv`.
