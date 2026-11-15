# Cash flow statement (indirect method) — Northbrook Trading Ltd, nine months to 30 September 2025 (upload path)

Mosofin is not connected, so this run is manual and uses only your uploads (connecting Mosofin would read the full ledger behind fixed assets, debt and equity: docs.mosofin.com). Nothing was posted; the statement is a draft for a person to review and issue.

## (a) Read-back

Building the statement of cash flows for **Northbrook Trading Ltd**, **1 January – 30 September 2025**, bridging **31 December 2024 → 30 September 2025**, under **US GAAP (ASC 230)**, indirect method, in **USD**. Cash is **1000 Operating Bank Account, 1010 Petty Cash and 1050 Stripe Clearing**, none restricted. **No acquisitions or disposals of a business** in the period (your answer).

| Intake question | Status | Treatment |
|---|---|---|
| B — period and comparative date | You gave "September 2025, as at 30 Sep". The comparative date was not stated | The uploads bridge 31 Dec 2024 → 30 Sep 2025 (year-to-date). A September-only statement would need a trial balance at 31 Aug 2025. **Please confirm year-to-date** |
| C — framework | US GAAP (intake and `accounting_policies.md` agree) | Interest paid in operating; dividends paid in financing |
| D — cash | 1000, 1010, 1050; none restricted | Used |
| E — acquisitions | None | No working-capital stripping |
| F — IFRS choices / method | Not applicable under US GAAP; method not stated | Indirect (default) |

## (b) Validation of the upload — shown before any work

| File | What it actually is | Company / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `trial_balance_2024-12-31.csv` | Pre-closing trial balance, 29 accounts; debits = credits; 2024 net income 633,096 | 31 Dec 2024 (file name; content consistent). No company or currency | Yes; same account list as 30 Sep 2025 | Yes — Step 1 opening cash, Step 2 opening balances | **Accepted with a limit**: company/currency user-asserted |
| `trial_balance_2025-09-30.csv` | Trial balance, 29 accounts, balances; retained earnings 1,422,317 = 789,221 + 2024 profit 633,096 | 30 Sep 2025; YTD net income 605,615 | Yes | Yes — Steps 1–4 | **Accepted with a limit**: company/currency user-asserted |
| `profit_and_loss_2025_ytd.csv` | Monthly P&L Jan–Sep 2025; net income 605,615, revenue 4,038,600 — **agrees to the 30 Sep TB** | Jan–Sep 2025 | Yes | Yes — Step 2 net income, depreciation, interest | **Accepted** |
| `general_ledger_2025-09.csv` | Ledger extract: September bank lines on 1000 (net −16,326; opening 1,246,642) and 7 journals | Sep 2025 only | Partly. No fixed-asset, debt or equity movements for Jan–Aug; journals do not all agree to the TB (below) | Yes — Steps 3–4, 7 | **Accepted with a limit**: investing and financing derived from TB changes, not read from movements |
| `accounting_policies.md` | Policy note: US GAAP, private company, straight-line depreciation | Undated | Yes | Yes — Step 4 classification | **Accepted** |
| `trial_balance_september.csv` | A trial balance — but **at 30 September 2024**, not 2025: term loan 280,000, YTD revenue 3,499,900 (= Jan–Sep 2024), retained earnings still 789,221 | Wrong period: one year earlier than your intake. No date in the file | Yes, but not for this bridge | No step of a 2025 YTD statement uses it; a 2024 comparative would also need a TB at 31 Dec 2023 | **Rejected**: different period from your intake. If it was meant as the comparative, please upload the 31 Dec 2023 trial balance too |

Still missing: ledger detail for 1500/1510 fixed assets and 2500 term loan for Jan–Aug (required for accuracy); comparative-period balances; the income-tax status of the company (no tax accounts exist).

*I would stop here and wait. Assumed answer: "go ahead with the accepted files".*

## (c) Findings

### Statement of cash flows — nine months to 30 September 2025 (USD)

| Operating activities | |
|---|---:|
| Net income | 605,615 |
| Depreciation (6600; accumulated depreciation +37,800) | 37,800 |
| Increase in accounts receivable (602,143 → 798,360) | (196,217) |
| Increase in inventory (495,154 → 683,100) | (187,946) |
| Prepaid expenses, allowance, card payable, payroll/tax payables (unchanged) | 0 |
| Increase in accounts payable (193,329 → 255,264) | 61,935 |
| Increase in accrued liabilities (27,000 → 28,800) | 1,800 |
| **Net cash from operating activities** | **322,987** |
| **Investing activities** — capex and disposals (fixed-asset cost unchanged at 420,000) | **0** |
| Repayment of term loan (265,000 → 220,000; 9 × 5,000) | (45,000) |
| Intercompany payable — Northbrook UK (38,000, unchanged) | 0 |
| **Net cash used in financing activities** | **(45,000)** |
| Effect of exchange rate changes (no foreign-currency cash) | 0 |
| **Net increase in cash** | **277,987** |
| Cash at 31 Dec 2024 (952,329 + 500 + 6,420) | 959,249 |
| **Cash at 30 Sep 2025** (1,230,316 + 500 + 6,420) | **1,237,236** |

**Tie-out:** 322,987 − 45,000 + 0 + 0 = 277,987 = 1,237,236 − 959,249. **Ties exactly; no plug.** No transfers between the three cash accounts (1010 and 1050 unchanged). No dividends: retained earnings moved only by the 2024 profit close.

### Supplemental disclosures

- **Cash paid for interest: 17,100** (9 × 1,900), inferred from the 6,900 monthly loan payment (5,000 principal + 1,900 interest) and no interest payable account; only September's payment is in the ledger.
- **Cash paid for income taxes: nil.** There is no tax expense or tax payable in either TB. Please confirm whether the company is a pass-through or a tax provision is missing.
- **Non-cash investing and financing: none identified** (no leases, no debt-for-asset entries in the uploads).

### Flags from the September ledger — they do not change the tie-out but need explanation

1. **JE-0904, 28 Sep, DR A/R / CR Sales 50,000, memo "Revenue adjustment"**: a round manual revenue entry with no support; it is 25% of the YTD rise in receivables. Non-cash; if reversed, net income and the A/R movement both fall by 50,000.
2. **JE-0907, 30 Sep, DR Marketing / CR Accrued 9,999, no memo**: explains most of September's marketing spike (29,146 vs about 18,200 run-rate).
3. **JE-0906 accrues 1,900 loan interest** although the 22 Sep payment of 6,900 already included interest: a possible double count.
4. **JE-0902 releases 1,500 prepaid insurance to 6150 Insurance**, an account in neither trial balance, while prepaids stay 18,000. The extract does not agree to the TB.
5. September journals credit Accrued Liabilities 24,099, yet the account rose only 1,800 over nine months; the January–August movements are not in the uploads.
6. **JE-0905 is dated 31 Aug** ("Legal fee missed in August") inside a September extract.
7. **Capex nil is derived, not read**: unchanged cost could hide an addition and a disposal of equal cost. Ledger detail on 1500 would confirm it.

## (d) What was not done, and why

| Step | Status | Gap |
|---|---|---|
| 1 Change in cash | done | Restriction user-asserted |
| 2 Operating | done | Working-capital changes taken as wholly operating; no Jan–Aug ledger to test non-cash movements |
| 3 Investing | done with a limit | Derived from TB; needs 1500/1510 ledger |
| 4 Financing | done with a limit | Gross draws not visible; only net change and one month's repayment |
| 5 FX | done — nil | |
| 6 Tie-out | done, exact | Platform's own cash-flow report not available for the second tie-out |
| 7 Supplemental | done with a limit | Tax status unknown |
| 8 Direct method | not requested | |
| 9 Comparative period | **not done** | Needs balances at 31 Dec 2023 and 30 Sep 2024 |
| Workbook | not created | Would you like `Cash_Flow_Statement_2025-09_Northbrook Trading Ltd.xlsx`? Only on a yes |
| 10 Save preferences | not offered yet | After your review |

**Coverage (manual run).** Environment: Northbrook Trading Ltd, USD, user-asserted; data source upload; verdicts as in (b). Capability map: not applicable, no connection; every line `[manual]`. Not done: ledger roll-forwards for fixed assets and debt, the platform cash-flow cross-check, the comparative period.

**Data sources:** user uploads only — `trial_balance_2024-12-31.csv`, `trial_balance_2025-09-30.csv`, `profit_and_loss_2025_ytd.csv`, `general_ledger_2025-09.csv`, `accounting_policies.md`.
