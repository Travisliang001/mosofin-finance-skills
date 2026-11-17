# Statement of changes in equity — Northbrook Trading Ltd — nine months to 30 September 2025

Mosofin is not connected, so this run is manual: every step is `[manual]` and every figure comes from your uploads. Nothing was posted or changed anywhere.

## Read-back

Building the statement of changes in equity for **Northbrook Trading Ltd** (user-asserted), a **corporation** under **US GAAP**, for the period **1 January – 30 September 2025**, in **USD** (user-asserted). Treasury stock: **none** (your answer; the chart agrees — no treasury account). Data source: **upload only**. Standalone entity: the TB carries *Investment in Northbrook UK Ltd* (104,800) at cost, so this is the parent's own statement, not a consolidation; no NCI or CTA arises in it.

| Intake question | Treatment |
|---|---|
| B — comparative | **Not answered.** No default for the period. Shown below: FY2024 roll-forward (the only prior period the files evidence), marked provisional. For an interim statement the usual comparative is the nine months to 30 Sep 2024; please say which you want. |
| D — share counts | Answered by `cap_table.csv` (used once you confirm it): 1,000,000 common shares, 80,000 options. |
| E — unusual movements | **Not answered.** The 7,500 "Adjustment" below is listed as unexplained. |
| F — dividend dates / per share | Not answered. Default: **dividends in total only**. (The ledger date is 31 Mar 2025; 60,000 / 1,000,000 shares would be 0.06 a share — derived, not confirmed.) |
| Par value per share | Not asked by the skill, needed for the par/APIC split. Share Capital 250,000 / 1,000,000 shares implies 0.25 — please confirm par. |

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Step that uses it | Verdict |
|---|---|---|---|---|---|
| `trial_balance_2024-12-31.csv` | TB, 33 accounts; Dr = Cr **6,433,544**. **Pre-close**: P&L still open (NI 614,939), RE 763,715 | No entity or currency named | Yes | Opening balances, Test 0b, comparative | **Accepted with a limit**: company/currency user-asserted |
| `trial_balance_2025-09-30.csv` | TB, 33 accounts; Dr = Cr **6,546,018**. YTD P&L open (NI 594,241); RE 1,378,654; 3200 Dividends and Adjustments Dr 67,500 | No entity named | Yes | Closing balances, tie-outs | **Accepted with a limit**: company user-asserted |
| `equity_accounts_ledger_2025.csv` | Equity ledger detail, 4 rows (3100, 3000) for 2025 | 2025, no entity named | Yes, but codes entries to 3100 that the TB holds in 3200 | Step 0 source test, Step 3 | **Accepted with a limit**: covers 3000 and 3100 only; account coding disagrees with the TB (see finding 3) |
| `cap_table.csv` | Cap table: 2 common holders, option pool with 2025 grant terms | No date or entity | Yes | Step 4 share roll-forward; stock comp check | **Accepted with a limit**: user-supplied, not evidenced; no par value |
| `trial_balance_september.csv` | A September TB with **no year**. RE 763,715 = the **2024 opening** RE; Sales 3,499,900 vs 4,597,600 at Dec 2024; Term Loan 280,000 (> 265,000 at Dec 2024). This is the **interim TB at 30 Sep 2024**, not 30 Sep 2025 | Wrong period | Foots (5,363,915) | None for the current period | **Rejected** — wrong year. Set aside. If you want the nine-months-to-Sep-2024 comparative, confirm this is that TB and I will use it there. |

**Still missing:** an income statement for Jan–Sep 2025 (tie-out 3 is otherwise the TB against itself); ledger detail for 3200; the cash flow statement or bank detail for the dividend (tie-out 8); par value; the closing balance sheet as reported for 31 Dec 2023 (Test 0b at the 2024 boundary). I would wait for your answer here; proceeding on the accepted files.

## Step 0 — Source test of every equity movement

| Account | Date | Amount | Source | Recognised category? | Explanation |
|---|---|---|---|---|---|
| 3100 RE | 2025-01-01 | 1,378,654 Cr | Opening | — | Agrees to 31 Dec 2024 (Test 0b) |
| 3100 / 3200 | 2025-03-31 | 60,000 Dr | "Dividend declared and paid" | Yes — cash dividend | Declared and paid same day; no dividend payable |
| 3100 / 3200 | **2025-06-30** | **7,500 Dr** | **"Adjustment"** | **No** | **Unexplained, mid-period, direct to equity.** Not net income, not a dividend, not shown as a prior-period adjustment or adoption effect. |
| 3000 Share Capital | 2025-01-01 | 250,000 Cr | Opening | — | No movement in 2025 |

**Test 0b — opening equity vs last year's closing: passes.** Dec 2024 TB is pre-close: RE 763,715 + FY2024 NI 614,939 (revenue 4,597,600 − expenses 3,982,661) = **1,378,654**, which equals the 2025 opening RE in the ledger and the Sep 2025 TB. Total equity at 31 Dec 2024 = 250,000 + 1,378,654 = **1,628,654**, equal to assets − liabilities on the Dec 2024 TB. No prior-period break.

### Findings

1. **7,500 posted directly to equity on 30 June 2025, described only as "Adjustment".** Retained earnings moves for four reasons; this is none of them on the evidence. If it is an expense or correction it belongs in the P&L (net income would fall to 586,741) or, if a prior-year error, on its own prior-period-adjustment line against opening RE. Shown in the statement as a named, unexplained line, not in "Other". Please explain it.
2. **Stock-based compensation appears unrecorded.** The cap table shows 20,000 options granted 1 Apr 2025, grant-date fair value 1.10, 4-year monthly vesting: total 22,000. Straight-line, Apr–Sep is 6/48 months → **2,750** of compensation expense and APIC by 30 September (graded attribution would give more). The TB has **no APIC account and no stock-comp expense**. The 60,000 options already outstanding at 1 Jan 2025 also have no APIC behind them — grant data needed to say whether earlier expense was ever recorded. Not booked by this run; a proposal for you to confirm.
3. **The equity ledger and the TB disagree on coding.** The ledger posts the dividend and the adjustment to **3100**, yet the Sep TB shows 3100 unchanged at 1,378,654 and the 67,500 (60,000 + 7,500) in **3200 Dividends and Adjustments**. Amounts agree; the account does not. Confirm which is the export of record; 3200 should close to RE at year end.
4. **Dividend leg of tie-out 8 is partial:** declared 60,000 = paid 60,000 (same day), no dividend payable account, so declared − increase in payable (0) = 60,000 paid. The cash-flow leg is not evidenced (no cash flow statement uploaded).

## Statement of changes in equity (USD)

| | Share capital | APIC | Retained earnings | Total |
|---|---:|---:|---:|---:|
| **Balance 1 Jan 2024** (pre-close RE per Dec 2024 TB) | 250,000 | — | 763,715 | 1,013,715 |
| Net income FY2024 | | | 614,939 | 614,939 |
| **Balance 31 Dec 2024** | 250,000 | — | 1,378,654 | 1,628,654 |
| Net income, 9 months to 30 Sep 2025 | | | 594,241 | 594,241 |
| Cash dividend declared and paid, 31 Mar 2025 | | | (60,000) | (60,000) |
| Unexplained direct entry "Adjustment", 30 Jun 2025 | | | (7,500) | (7,500) |
| Stock-based compensation | | **not recorded** (2,750 indicated) | | — |
| **Balance 30 Sep 2025** | **250,000** | **—** | **1,905,395** | **2,155,395** |

FY2024 comparative is provisional: no 2024 equity ledger detail and no 31 Dec 2023 balance sheet, so the 1 Jan 2024 boundary is untested and "RE 763,715" is the Dec 2024 pre-close balance, assumed to have had no direct postings in 2024. No OCI, preferred, treasury or NCI components exist.

## Share count roll-forward (from your cap table, user-supplied)

| | Common shares | Options outstanding |
|---|---:|---:|
| Opening 1 Jan 2025 | 1,000,000 | 60,000 |
| Issued / granted | 0 | 20,000 |
| Exercised / repurchased / forfeited | 0 | 0 |
| Closing 30 Sep 2025 | 1,000,000 | 80,000 |

Issued = outstanding (no treasury shares). Options are not shares outstanding. Par/APIC split not done: par value not supplied.

## Tie-outs

| # | Tie-out | Result | Guaranteed or independent |
|---|---|---|---|
| 1 | Opening + movements = closing, each column | Holds | Guaranteed (arithmetic) |
| 2 | Total equity = BS equity: assets 2,713,959 − liabilities 558,564 = 2,155,395 | Holds | Guaranteed (same accounts) |
| 3 | NI 594,241 = income statement | Holds only against the TB itself | Not independent: no P&L uploaded |
| 4 | OCI = statement of comprehensive income | n/a — no OCI | — |
| 5 | Closing RE = BS RE 1,905,395 (3100 + 3200 + YTD NI) | Holds | Guaranteed |
| 6 | Closing AOCI | n/a | — |
| 7 | Share counts to disclosure | **Not done** — no BS share note supplied | Independent |
| 8 | Dividends declared 60,000 − Δ payable 0 = paid 60,000 | Equity/payable legs hold; **cash-flow leg not evidenced** | Independent |

The only test with real content is Step 0, and it found two items (findings 1 and 2).

## Not done, and why

- Par/APIC split; per-share dividend — par and per-share not confirmed.
- Stock-comp correctness — needs the full grant history, vesting and forfeiture data; 2,750 is an indication, not an entry.
- Test 0b at the 1 Jan 2024 boundary — needs the 31 Dec 2023 balance sheet.
- Tie-outs 3, 7 and 8 (cash leg) as independent checks — need the P&L, share disclosure and cash flow.
- Excel workpaper — would ask before creating `Statement_of_Equity_2025-09_Northbrook_Trading_Ltd.xlsx`. Nothing posted.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, corporation, US GAAP, USD — all user-asserted; standalone; chart consistent with a corporation (share capital, RE; no APIC, treasury or OCI accounts). Data source: upload. Files: 4 accepted with limits, 1 rejected (Sep 2024 TB). |
| Capability map | Not applicable: no connection. Every task is `[manual]`. |
| Steps | 0 done (ledger covers 3000/3100 only); 1 done; 2 done; 3 done; 4 done from user cap table, par split not done; 5 done with 3, 7, 8 limited; 6 FY2024 provisional; 7 tables in chat, no file. |
| Unknowns carried forward | 7,500 direct "Adjustment"; unrecorded stock comp (2,750 indicated for 2025, prior grants unknown); 3100/3200 coding mismatch; comparative period choice. |
| Parameters | 3000 → Share capital; 3100 + 3200 + current-year P&L → Retained earnings; treasury none; periods 1 Jan 2024 – 30 Sep 2025. |
