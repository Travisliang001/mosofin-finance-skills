# Chart of accounts restructure — Northbrook Trading Ltd, as at 30 September 2025 (upload path)

Mosofin is not connected, so this run is manual and uses only your uploads (connecting Mosofin would read every account's transaction count and last activity: docs.mosofin.com). **Nothing was created, renamed, merged or deactivated**; the chart and the mapping are proposals for a person to make in your system.

## (a) Read-back

**Restructuring** the existing chart of **Northbrook Trading Ltd**, to stay in **the same accounting system**, under **US GAAP**, for a **distribution** business reporting by **department**. The chart must serve the **lender's covenant reporting**, which needs **one-time professional fees shown separately**. Currency USD.

| Intake question | Status | Treatment |
|---|---|---|
| B — new or restructure | Restructure (your request file) | Old-to-new map below |
| C — target system | "The same accounting system", not named | Account types kept in the file's own taxonomy; the import file needs the system named |
| D — framework | US GAAP | Used |
| E — industry, dimensions | Distribution; department | Department values not supplied: proposed, to confirm |
| F — reports | Lender covenant reporting | One-time fees split; EBITDA lines tagged |
| Tax jurisdictions | Not supplied | **No tax accounts added**; gaps listed |

## (b) Validation of the upload — shown before any work

| File | What it actually is | Company / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `chart_of_accounts.csv` | Chart of accounts: number, name, type; **36 accounts**; no duplicate numbers or names | Undated; no company named | Yes, but **no active/inactive column**, and 1160 is listed out of order (after 6950) | Yes — Steps 1–2 and the migration map | **Accepted with a limit**: company user-asserted; inactive status unknown |
| `trial_balance_2025-09-30.csv` | Trial balance, 29 accounts, debits = credits; P&L accounts are Jan–Sep 2025 year-to-date | 30 Sep 2025; no company or currency | Balances only: **no transaction counts or last-activity dates**; 9 months, not the 12+ the checklist recommends | Yes — Step 0b usage (proxy only) | **Accepted with a limit**: usage can be inferred, not measured |
| `chart_of_accounts_request.md` | Your restructure brief: target system, framework, industry, dimension, reporting need | Undated | Yes | Yes — intake C–F | **Accepted** |
| `chart_of_accounts_final.csv` | **Not a chart of accounts.** A staff shift rota: E08–E10, week_1–week_4, "nights/days/off" | No company, dates or accounts | No | No | **Rejected** on content; I use `chart_of_accounts.csv` |

Still missing: ledger activity per account (transaction count, last date) for 12+ months — recommended, and required before any account is retired; the system name and its import template; department list; tax jurisdictions; active status per account.

*I would stop here and wait. Assumed answer: "go ahead with the accepted files".*

## (c) Findings

### 1. Usage analysis — 9-month window, Jan–Sep 2025, from balances only

29 of 36 accounts carry a balance. **Seven accounts have no balance at 30 Sep 2025:**

| Account | Type | YTD net posting | Classification | Recommendation |
|---|---|---:|---|---|
| 6150 Insurance | Expense | 0 | No net activity in 9 months | **Investigate, do not retire**: Prepaid Expenses holds 18,000 with no expense released, so insurance may be stuck in prepaids |
| 6160 Repairs and Maintenance | Expense | 0 | No net activity | Retire candidate, once the ledger confirms zero transactions |
| 6700 Office Supplies | Expense | 0 | No net activity | Retire candidate; or merge with 6900 into one "Office and Postage" |
| 6800 Travel and Meals | Expense | 0 | No net activity | Keep if travel is expected (sales team); confirm with ledger |
| 6900 Postage and Delivery | Expense | 0 | No net activity | Merge candidate (above); outbound freight belongs in 5100 for a distributor |
| 6950 Cash Over and Short | Expense | 0 | No net activity | Retire candidate (petty cash is 500) |
| 1160 Employee Advances | Asset | balance 0 | **Not classifiable from a balance**: a nil balance does not mean unused | Keep pending ledger evidence |

A nil P&L balance over nine months is strong but not conclusive (postings could net to zero). **No account goes on the retire list until transaction counts confirm it.**

### 2. Structure

4-digit numbering fits a 36-account chart; conventional ranges already in use. **Two misplacements:** 7000 Interest Expense is typed "Expense" inside the operating range, which puts it above EBITDA in a number-ordered P&L; 1150 Allowance and 1510 Accumulated Depreciation are contra accounts (they reduce the asset beside them) and need a credit normal balance. No account name encodes a department, so no dimension consolidation is needed.

### 3. Proposed additions (US GAAP, distribution, covenant reporting)

| New # | Name | Type | Why |
|---|---|---|---|
| 6410 | Professional Fees — One-time | Expense | **Lender covenant**: one-time fees shown apart from 6400 (rename 6400 "Professional Fees — Recurring") so they can be added back to covenant EBITDA |
| 6050 | Bad Debt Expense | Expense | Always required; 1150 allowance exists with no expense account |
| 8200 | Foreign Exchange Gain/Loss | Other Expense | Always required; intercompany with Northbrook UK |
| 8100 | Interest Expense (from 7000) | Other Expense | Below EBITDA for covenant reporting |
| 2450 | Current Portion of Long-Term Debt | Other Current Liability | Term loan 220,000 must be split current/non-current |
| 2170 | Benefits / Retirement Withholdings Payable | Other Current Liability | Payroll liabilities separated by type beside 2150 and 2160 |
| 4900 / 4910 | Sales Returns and Allowances; Sales Discounts | Income (contra) | Distribution: returns and early-pay discounts |
| 5100 / 5200 | Freight-in; Inventory Adjustments and Shrinkage | Cost of Goods Sold | Distribution: landed cost and stock losses |

**Not added:** income tax expense and payable (9000s) and any jurisdiction-specific sales-tax accounts — **no jurisdiction was supplied**; the company has share capital and no tax accounts, so please confirm its tax status. Department values (e.g. Operations, Sales, Warehouse, Finance, Admin) are suggestions only.

### 4. Migration map (every old account)

| Old | Action | New | Migration entry? |
|---|---|---|---|
| 1000, 1010, 1050, 1100, 1200, 1300, 1500, 2000, 2050, 2100, 2160, 2200, 2300, 3000, 3100, 4000, 5000, 6000, 6100, 6200, 6300, 6500, 6600 | Keep | same | No |
| 1150, 1510 | Keep; set as contra (credit normal balance) | same | No |
| 2150 Payroll Clearing | Keep; describe as clearing only (should sit at nil; holds 1,200 credit — investigate) | same | No |
| 2500 Term Loan | Keep (non-current); current portion to 2450 | 2500 + 2450 | Yes — reclassify the portion due within 12 months (needs loan schedule) |
| 6400 Professional Fees | Rename "— Recurring"; split one-time items to 6410 | 6400 + 6410 | Yes, for 2025 one-time fees, if you want YTD restated |
| 7000 Interest Expense | Renumber/retype | 8100 | Yes — move YTD 17,100 if renumbered mid-year |
| 6150, 1160, 6800 | Keep pending investigation | same | No |
| 6160, 6950 | Retire candidate (after ledger check) | — | No (nil balance) |
| 6700, 6900 | Merge candidate | 6700 Office and Postage | No (nil balance) |

## (d) What was not done, and why

| Step | Status | Gap |
|---|---|---|
| 0b Usage | done with a limit | Balances only; transaction counts and last dates need a ledger export |
| 1–2 Structure, accounts | proposed | Active status unknown |
| 3 Industry | proposed | Distribution confirmed by you; block kept minimal |
| 4 Tax accounts | **not done** | No jurisdiction supplied |
| 5 Multi-entity | partial | Northbrook UK counterparty exists; its chart not supplied |
| 6 Import file | not created | System not named; would you like `Northbrook Trading Ltd_COA_2025-09-30.xlsx`? Only on a yes |
| 7 Save preferences | not offered yet | After your review |

**Coverage (manual run).** Environment: Northbrook Trading Ltd, USD, user-asserted; data source upload; verdicts as in (b). Capability map: not applicable, no connection; every task `[manual]`. Window: Jan–Sep 2025 YTD balances. Not done: transaction-level usage, inactive-account check, dimension and tax-code review — each needs a ledger and system export.

**Data sources:** user uploads only — `chart_of_accounts.csv`, `trial_balance_2025-09-30.csv`, `chart_of_accounts_request.md`.
