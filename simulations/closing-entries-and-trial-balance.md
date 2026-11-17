# Closing entries and trial balance — Northbrook Trading Ltd — FY ended 31 December 2024

Mosofin is not connected, so this run is manual: every step is `[manual]` and every figure comes from your uploads. Connecting Mosofin would read the trial balance, account types and the new-year auto-close test directly ([docs.mosofin.com](https://docs.mosofin.com)).

## Read-back

Closing the books of **Northbrook Trading Ltd** (user-asserted) for the **year ended 31 December 2024**, in **USD** (user-asserted; no file names a company or currency). Data source: **upload only**.

Intake questions your answers did not cover, and how this run treats them:

| Question | Treatment |
|---|---|
| Entity type | **Not answered; the skill never defaults it.** The chart shows *Share Capital* and *Retained Earnings* and the name ends "Ltd", which points to a **corporation (private limited company)**. Proposed, not assumed: please confirm. It changes nothing in the figures below because no dividend account exists, but it decides the Step 5 dividend variant. |
| Does your accounting system auto-close the year? | **Not answered and not testable** (no trial balance at 1 January 2025 was supplied). Conservative reading: **status unknown — the entries below must not be posted until this is confirmed.** |
| Is the audit complete? | Not answered. Treated as a **preliminary close**; re-run the tie-outs if audit adjustments follow. |
| Reporting framework | Not answered. No OCI accounts exist in the chart, so it changes no figure here. |
| Dividends declared in 2024 | No dividend or distribution account in the chart or trial balance. Taken as **nil**; please confirm none were declared and booked elsewhere. |
| Closing method | No *Income Summary* account in the chart → **two-step close** proposed. |

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Needed for | Verdict |
|---|---|---|---|---|---|
| `trial_balance_2024-12-31.csv` | Account-level trial balance, 29 accounts, debit/credit columns. Debits **6,459,050** = credits **6,459,050** | No entity or currency named; date in file name only | Yes — foots, account numbers match the chart | Steps 1, 2, 4, 5, 7, 8 (the pre-closing TB) | **Accepted with a limit**: company, currency and date user-asserted; whether it is the **final** TB after all adjustments is your confirmation, not evidence |
| `chart_of_accounts.csv` | Chart of accounts, 36 accounts with **type** | No entity named | Yes — every TB account is in it with a type; names agree | Step 2 (temporary / permanent split on type) | **Accepted with a limit**: company user-asserted |
| `trial_balance_september.csv` | A trial balance at **September**, no year stated: revenue 3,499,900 and RE 789,221 (same opening RE as December) — an **interim year-to-date TB, nine months**, not a year-end TB | No entity, no year; covers a period ending in September, not 31 Dec 2024 | Foots (5,389,421 both sides) | **No step uses it**: the closing works from the year-end pre-closing TB | **Rejected** — wrong period for a closing run. Set aside, not read into the work. If you meant to send the TB at **1 January 2025** (for the auto-close test) or the **prior-year balance sheet at 31 Dec 2023** (for opening RE), upload that instead |

**Still missing (please send with your answers):** (1) **trial balance at 1 January 2025** — required for the auto-close test (Step 0b); (2) **P&L for FY2024** — for the net-income cross-check (Step 4); (3) **balance sheet at 31 December 2023** — to evidence opening retained earnings; (4) list of year-end adjusting entries posted. I would wait for your answer here; proceeding on the accepted files as instructed.

## Step 0b — closed-state test

**Not run: no 1 January 2025 trial balance.** The December TB still carries all P&L balances and RE at 789,221, which is consistent with "not closed" at 31 Dec, but cannot show whether your system rolls the year automatically when FY2025 is opened. **Finding: state unknown.** If your system auto-closes, posting Entries 1–2 below on top would understate/overstate RE by the full year's result (633,096).

## Step 1 — Pre-closing TB

- Debits **6,459,050** = credits **6,459,050**. Balances. 29 accounts, all in the chart.
- **Adjusting entries — a gap to confirm:** a corporation with pre-tax profit of **633,096** shows **no income tax expense and no income-tax-payable account** anywhere in the chart. Either the **tax provision has not been posted** or tax is booked somewhere unexpected. Do not close until this is resolved (see `corporate-tax-provision-asc740`); closing now would roll a pre-tax figure into RE. Depreciation (50,400) is present; whether accruals, prepaid amortization and the allowance review were posted is `[manual]` — your confirmation.
- Reconciliations tied out, variances reviewed, management approval: `[manual]`, not evidenced.

## Step 2 — Classification (on type, not name)

- **Temporary (close):** 4000 Sales Revenue (Income); 5000 COGS (Cost of Goods Sold); 6000, 6100, 6200, 6300, 6400, 6500, 6600, 7000 (Expense).
- **Permanent (carry forward):** 1000–1510 assets, 2000–2500 liabilities, 3000 Share Capital, 3100 Retained Earnings.
- **Type / name exceptions:** none that would mis-close. Noted only: 1150 Allowance for Doubtful Accounts and 1510 Accumulated Depreciation are typed as assets with credit balances — correct contra-assets, permanent.
- Chart accounts with **no TB line** (taken as zero, nothing to close): 1160 Employee Advances; 6150 Insurance; 6160 Repairs and Maintenance; 6700 Office Supplies; 6800 Travel and Meals; 6900 Postage and Delivery; 6950 Cash Over and Short. Please confirm they are zero rather than omitted from the export.

## Step 4 — Closing totals

| Line | USD |
|---|---:|
| Revenue (A): 4000 Sales Revenue | 4,597,600 |
| Other income / gains (B) | 0 |
| Cost of revenue (C): 5000 | 2,666,608 |
| Operating expenses (D): 6000 842,400; 6100 108,000; 6200 183,904; 6300 42,000; 6400 30,000; 6500 18,392; 6600 50,400 | 1,275,096 |
| Other expenses (E): 7000 Interest Expense | 22,800 |
| Income tax expense (F) | **0 — see Step 1 gap** |
| **Net income (pre-tax as booked)** | **633,096** |
| Dividends (G) | 0 |

P&L cross-check: **not done — no P&L uploaded.**

## Step 5 — Proposed closing entries (two-step; proposals only, FY2024, nothing posted)

**Entry 1 — close revenue:** DR 4000 Sales Revenue 4,597,600 / CR 3100 Retained Earnings 4,597,600. *Memo: Close revenue to RE — FY2024.*

**Entry 2 — close expenses:** DR 3100 Retained Earnings 3,964,504 / CR 5000 Cost of Goods Sold 2,666,608; CR 6000 Payroll Expense 842,400; CR 6100 Rent 108,000; CR 6200 Marketing 183,904; CR 6300 Software 42,000; CR 6400 Professional Fees 30,000; CR 6500 Bank Fees 18,392; CR 6600 Depreciation 50,400; CR 7000 Interest Expense 22,800. *Memo: Close expenses to RE — FY2024.*

**Entry 3 — dividends:** none (no dividend account). **OCI (Step 6):** none in the chart.

**Do not post until** (a) the auto-close status is confirmed and (b) the tax provision gap is resolved — if a provision is booked, Entry 2 gains a CR to income tax expense and net income falls by that amount.

## Steps 7–8 — Post-closing TB and tie-outs (constructed, not verified against a live system)

- Post-closing TB: 20 permanent accounts; debits **2,494,546** = credits **2,494,546**. All revenue and expense accounts at zero.
- Only temporary accounts moved; every asset, liability and Share Capital balance unchanged.
- **Retained earnings roll:** opening 789,221 + net income 633,096 − dividends 0 ± OCI 0 = **closing RE 1,422,317**.
- Limit: opening RE 789,221 is **taken from the TB**, not evidenced against a 31 Dec 2023 balance sheet; the tie to the closing balance-sheet equity section is **not done** (no balance sheet uploaded).

## Step 9 — Lock and roll

**Not done and not doable by this skill.** Locking FY2024 is a human action in your accounting system — **owner to be named by you** (typically the controller). The FY2025 opening balances should equal the post-closing TB above; verify after posting.

## Not done, and why

- Auto-close test (Step 0b) — needs the 1 Jan 2025 TB.
- Net income vs P&L — needs the FY2024 P&L.
- Opening RE continuity and closing equity tie — needs balance sheets at 31 Dec 2023 and 31 Dec 2024.
- Confirmation that all adjusting entries posted, in particular the **income tax provision** — needs your adjusting-entry list.
- Excel workpaper `Closing_Entries_TB_FY2024_Northbrook Trading Ltd.xlsx` — offered; not created without your yes. Tables above stand in.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, FY ended 31 Dec 2024, USD — **user-asserted**. Data source: **upload**. TB 31-12-2024 and chart: accepted with limits (company/period user-asserted). September TB: **rejected** (interim, wrong period). |
| Capability map | Not applicable: no connection. Every task is `[manual]`. |
| Steps | 0b not done · 1 done with a limit (balance proved; adjustments not evidenced; tax provision missing) · 2 done · 3 done (two-step, no Income Summary) · 4 done, P&L cross-check not done · 5 done (proposals) · 6 done (no OCI) · 7 done (constructed) · 8 done with a limit (opening RE and BS tie not evidenced) · 9 **not done** (manual, owner to name) · 11 not offered (results not yet approved) |
| Not done | 1 Jan 2025 TB; FY2024 P&L; 31 Dec 2023 and 2024 balance sheets; adjusting-entry list; period lock |

Nothing was posted, locked or changed. **Data sources:** upload — `trial_balance_2024-12-31.csv`, `chart_of_accounts.csv`.
