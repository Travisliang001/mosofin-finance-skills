# Financial statements — Northbrook Trading Ltd, nine months to 30 September 2025 (upload path)

Mosofin is not connected for this run (you chose upload only), so every step is `[manual]` and works from your files. Connecting Mosofin would automate the reads — docs.mosofin.com. Nothing was posted: every reclassification below is a proposal. **DRAFT — reporting framework, rounding basis and current portion of debt not yet confirmed.**

## (a) Read-back

Building **Balance Sheet, Income Statement, Comprehensive Income, Cash Flows and Changes in Equity** for **Northbrook Trading Ltd** (user-asserted; no file names the company), **as at 30 September 2025**, in **USD** (user-asserted), single entity, separate (not consolidated), from your uploads.

| Not answered at intake | What I did (the skill never defaults these) |
|---|---|
| Reporting framework | **Not defaulted.** Laid out current-first (US GAAP convention). Under IFRS: non-current items first, "Trade and other receivables / payables". Every figure and total is identical under both. Please confirm. |
| Rounding basis | **Not defaulted.** Shown in whole USD exactly as in the TB, unrounded. |
| Current portion of the term loan | **Not defaulted.** Shown under both readings (Finding 3). |
| Income statement format | Single by-nature/by-account listing, multi-step (gross profit shown). No department or class data, so by-function would be a reallocation, not a read. |
| Prior-year issued financials, EPS share count, discontinued ops, OCI items | Not supplied → tie-out 6 **not run**; EPS not presented; no disposal group or OCI assumed. |

## (b) Validation of the upload — shown before any work

| File | What it actually is | Company / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `trial_balance_2025-09-30.csv` | Trial balance, 29 accounts, debit/credit | No company, date or currency in the file | Foots: DR = CR = 6,589,681. Every account is in the chart. P&L accounts hold YTD balances (mid-year, pre-closing) | Yes — current period, Steps 1–3 | **Accepted with a limit: company and period user-asserted** |
| `trial_balance_2024-12-31.csv` | Trial balance, 29 accounts | No company or date in the file; as-at 31 Dec 2024 taken from the file name only | Foots: DR = CR = 6,459,050. Pre-closing (FY2024 P&L still open). Its RE 789,221 + its profit 633,096 = 1,422,317 = the opening RE in the 2025 TB, so it is consistent with being the prior year-end | Yes — comparative, Step 4 | **Accepted with a limit**: date user-asserted; it is a 12-month year, so it cannot be the comparative for a 9-month income statement |
| `chart_of_accounts.csv` | Chart of accounts, 36 accounts with types | No company | Yes; covers all 29 TB accounts | Yes — mapping and type checks, Steps 1–2 | **Accepted** |
| `trial_balance_2025-09-30_v2.csv` | A 4-line trial balance for **another company**: account 1000 is "Bank — Harlow Fabrication Ltd"; 3000 is "Equity", not Share Capital; total 306,000 against 6,589,681 in the main TB; no P&L or retained earnings | Names Harlow Fabrication Ltd, not Northbrook | Foots, but wrong entity | No step | **Rejected** on content despite the "2025-09-30" name. Not used. If a revised Northbrook September TB exists, please upload it. |

Still missing, and what each is for: **prior-year issued financial statements** (tie-out 6 — the check for unposted audit adjustments); **TB for the nine months to 30 Sep 2024** (like-for-like income-statement comparative); **term-loan amortization schedule** (current portion); **reporting framework and rounding basis**; tax computation or confirmation that no tax applies.

*I would stop here and wait for your answer. Assumed answer: "go ahead with the accepted files".*

## (c) Statements (whole USD, unrounded)

**Balance Sheet** | 30 Sep 2025 | 31 Dec 2024
---|---:|---:
Cash and cash equivalents (1000, 1010) | 1,230,816 | 952,829
Stripe clearing (1050) — other current asset | 6,420 | 6,420
Accounts receivable, net of allowance 9,000 (1100, 1150) | 789,360 | 593,143
Inventory (1200) | 683,100 | 495,154
Prepaid expenses (1300) | 18,000 | 18,000
**Total current assets** | **2,727,696** | **2,065,546**
PP&E, net — cost 420,000 less accumulated depreciation (1500, 1510) | 108,800 | 146,600
**Total assets** | **2,836,496** | **2,212,146**
Accounts payable and corporate card (2000, 2050) | 262,564 | 200,629
Accrued liabilities and payroll (2100, 2150, 2160) | 35,400 | 33,600
Sales tax payable (2200) | 2,600 | 2,600
Intercompany payable — Northbrook UK (2300) | 38,000 | 38,000
**Total current liabilities (before loan split)** | **338,564** | **274,829**
Term loan (2500) — split pending, see Finding 3 | 220,000 | 265,000
**Total liabilities** | **558,564** | **539,829**
Share capital (3000) | 250,000 | 250,000
Retained earnings (3100 + current-period profit) | 2,027,932 | 1,422,317
**Total equity** | **2,277,932** | **1,672,317**
**Total liabilities and equity** | **2,836,496** | **2,212,146**

The 31 Dec 2024 column includes FY2024 profit 633,096 in retained earnings (that TB was pre-closing).

**Income Statement** | 9 months to 30 Sep 2025 | FY2024, 12 months (**not like-for-like**)
---|---:|---:
Revenue (4000) | 4,038,600 | 4,597,600
Cost of goods sold (5000) | (2,370,856) | (2,666,608)
**Gross profit** | **1,667,744** (41.3%) | **1,930,992** (42.0%)
Payroll (669,600 / 842,400), rent (81,000 / 108,000), marketing (172,474 / 183,904), software (31,500 / 42,000), professional fees (36,500 / 30,000), bank fees (16,155 / 18,392), depreciation (37,800 / 50,400) | (1,045,029) | (1,275,096)
**Operating profit** | **622,715** | **655,896**
Interest expense (7000) | (17,100) | (22,800)
**Profit before tax** | **605,615** | **633,096**
Income tax expense | **none recorded** — Finding 2 | none recorded
**Net income** | **605,615** | **633,096**

**Comprehensive income:** no OCI items and no AOCI account in the chart; total comprehensive income = net income 605,615.

**Cash flows (indirect, draft from balance-sheet movements; full procedure belongs to `cash-flow-statement-indirect-method`):** net income 605,615 + depreciation 37,800 − AR increase 196,217 − inventory increase 187,946 + AP increase 61,935 + accruals increase 1,800 = **operating 322,987**; investing 0 (no change in PP&E cost); financing: term-loan repayment **(45,000)**; net change **277,987**; cash 952,829 → **1,230,816**.

**Changes in equity:** share capital 250,000 unchanged; retained earnings 1,422,317 + net income 605,615 − dividends 0 = **2,027,932**.

## (d) Cross-statement tie-outs (on the statements built above, not a platform report)

| # | Tie-out | Result | Difference |
|---|---|---|---:|
| 1 | Assets = Liabilities + Equity | Pass, both dates (2,836,496; 2,212,146) | 0 |
| 2 | Net income IS = net income on cash flow | Pass (605,615) | 0 |
| 3 | Net income + OCI = net income in equity statement | Pass (605,615; OCI nil) | 0 |
| 4 | Closing cash on cash flow = BS cash | Pass (1,230,816; Stripe clearing 6,420 classed outside cash) | 0 |
| 5 | Closing RE in equity statement = BS RE | Pass (2,027,932) | 0 |
| 6 | Comparatives = prior year as issued | **NOT RUN** — no issued FY2024 financials uploaded | n/a |
| 7 | Currency consistent | Pass, USD on every statement (user-asserted) | n/a |

Mapping completeness: all 29 TB accounts land on exactly one line in each period; mapped totals equal the TB. No type mismatch: the two credit balances in asset types (1150 allowance, 1510 accumulated depreciation) are contra accounts and shown as deductions.

## (e) Findings

1. **The income-statement comparative is not like-for-like.** The current period is 9 months; the only prior TB is the 12-month year to 31 Dec 2024. Monthly run-rates: revenue 448,733 vs 383,133 (+17%), COGS +19%, marketing +25%, professional fees 4,056 vs 2,500 (+62%). Upload the TB at 30 Sep 2024 for a proper comparative.
2. **No income tax.** A Ltd company with 605,615 of profit this year and 633,096 last year carries no tax expense and no tax payable in either TB. Net income above is profit before any provision. Confirm the tax position or supply the provision.
3. **Current portion of the term loan is undetermined.** The loan fell 265,000 → 220,000 (45,000 in 9 months, about 5,000 a month). Shown under each reading: all non-current → current liabilities 338,564, current ratio 8.06; if 5,000 a month continues, 60,000 current / 160,000 non-current → current liabilities 398,564, ratio 6.84. Needs the amortization schedule. Interest stays at 1,900 a month in both years despite the lower principal — worth checking against the schedule.
4. **Balances that have not moved in nine months:** Stripe clearing 6,420, payroll clearing 1,200, payroll tax payable 5,400, sales tax payable 2,600, corporate card 7,300, intercompany 38,000, prepaid 18,000, allowance 9,000. Clearing and tax accounts normally turn over; prepaid unchanged with nothing in insurance expense (6150 has no balance); allowance unchanged while AR rose 33% (DSO about 54 days vs 48). Each may be stale — reclassification or adjustment proposals need the detail.
5. **Intercompany payable to Northbrook UK 38,000** is a related-party balance requiring disclosure; it should be agreed to the UK entity before issue.

## (f) Not done, and why

Tie-out 6 (no issued FY2024 statements); EPS (no share count, and not required unless listed); like-for-like comparative IS (no Sep-2024 TB); final framework layout, rounding and loan split (not confirmed); full cash-flow and equity procedures (hand-offs; drafts above only); trend explanations (movements computed, causes need you); no `.xlsx` created — I would ask whether you want `Financial_Statements_2025-09_Northbrook Trading Ltd.xlsx`.

## (g) Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, 30 Sep 2025, USD — user-asserted. Source: upload. Files: Sep-2025 TB accepted with limit; Dec-2024 TB accepted with limit (date from name; 12-month); chart accepted; `_v2` TB rejected (Harlow Fabrication Ltd). |
| Capability map | Not applicable: no connection. Every task is `[manual]`. |
| Steps | 1 TB validation done · 2 BS done with limit (framework, loan split) · 3 IS done with limit (no tax) · 4 comparatives done with limit (period mismatch) · 5 OCI done (nil) · 6 CF draft · 7 equity draft · 8 tie-outs 1–5, 7 done, 6 **not done** · 9 rounding **not done** (basis not given) · 10 quality checks done · 11 tables in chat, no file · 12 not offered (no approval yet). |
| Not done | Prior-year issued comparison (upload FY2024 issued statements); like-for-like IS (Sep-2024 TB); current portion of debt (loan schedule); tax provision (tax computation). |

Footer: Northbrook Trading Ltd · separate entity · USD · whole units, unrounded · source: user upload · no mock data.

**Data sources:** user uploads — `trial_balance_2025-09-30.csv`, `trial_balance_2024-12-31.csv`, `chart_of_accounts.csv`.
