# Recurring transactions — Northbrook Trading Ltd, schedule from October 2025

Mosofin is not connected, so this run is manual: every step is `[manual]` or `[auto: computed]` from your uploads; nothing is `[auto: read]`. (Connecting Mosofin would validate against the live chart and audit the runs from the ledger — docs.mosofin.com.)
**NOT POSTED — every occurrence below is Pending. No template has been created, nothing is scheduled. Validation status: NOT VALIDATED against a live chart (checked against your uploaded chart only).**

## 1. Read-back

Recurring-entry review and schedule for **Northbrook Trading Ltd** (user-asserted), **USD**, as at **30 September 2025**, from your uploads. This skill has no upload checklist of its own, so I built one from its Inputs table (below). Not answered at intake, and how I treat it:

| Input | Treatment |
|---|---|
| Transaction type per item (JE / bill) | Not stated → treated as **recurring JEs**; rent and software may in fact be vendor bills — please say |
| Cadence | Not stated → **monthly**, inferred from the Jul–Sep posting columns (inference, please confirm) |
| End date / count | Not stated → **finite 12-month horizon, Oct 2025 – Sep 2026, flagged for renewal review** (skill's rule for open-ended) |
| Holiday calendar, roll policy | **Not supplied and not defaulted.** Dates shown unrolled; weekend dates flagged |
| Escalation, stop conditions | Not supplied → **fixed amounts**; contracts not seen |
| GL accounts, counterparties, tax codes | Not in the file → **proposed mapping** from your chart, for your confirmation |

## 2. Validation of the upload — shown before any work

| File | What it actually is | Company / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `recurring_entries.csv` | A register of 5 recurring items: name, amount, day of month, and **posted yes/no** for Jul, Aug, Sep 2025 | No company or currency; covers Jul–Sep 2025 | Partly: no GL accounts, counterparties, start/end dates, cadence or tax; "posted" is a user flag, not ledger evidence | Yes — Steps 2, 3, 5b | **Accepted with a limit**: run audit is on your flags, not the ledger; accounts are proposed, not specified |
| `chart_of_accounts.csv` | Chart of accounts: 41 accounts, number, name, type | No company named | Yes; no active/inactive or no-post flag, no tax codes | Yes — Step 2b account check | **Accepted with a limit**: existence and type checked; active status and tax codes cannot be |
| `recurring_entries_final.csv` | **Not a recurring-entry list.** A staff shift rota: E08–E10, week_1…week_4, "nights / days / off" | No company, entries or amounts | No | No step uses it | **Rejected** on content despite its name. Not used |

**Still missing:** ledger detail (GL or JE listing) for Jul–Sep 2025 to confirm what actually posted; the contracts behind rent, software, insurance and the loan (end dates, escalation); the prepaid insurance balance and policy end; the loan schedule; the holiday calendar and roll policy; the vendor list.

*I would stop here and wait for your answer. Assumed answer: "go ahead with the accepted files".*

## 3. Findings

### Run audit (Step 5b) — on your posted flags

| Entry | Amount | Day | Jul | Aug | Sep | Result |
|---|---:|---:|:-:|:-:|:-:|---|
| Rent | 9,000 | 1 | yes | yes | yes | Ran each month |
| Depreciation | 4,200 | 30 | yes | yes | yes | Ran each month |
| Insurance release | 1,500 | 30 | yes | yes | yes | Ran each month |
| Loan interest | 1,069 | 30 | yes | yes | yes | Ran each month |
| **Software subscription** | **3,500** | 5 | yes | yes | **no** | **Did not run in September 2025** |

**The software subscription stopped in September.** Expected on 5 Sep; your register shows it not posted. Either the template was deactivated or ended, the vendor or account changed, or the subscription was cancelled. Until you confirm which, September expense is understated by up to **3,500**. If the service was received, a proposed accrual — **Dr 6300 Software 3,500 / Cr 2100 Accrued Liabilities 3,500**, reversing 1 Oct 2025 — is for your review; I have not assumed the service continued. Confirm against the ledger before loading anything, so the subscription is not booked twice.

### Account check (Step 2b, against the uploaded chart)

| Entry | Proposed debit | Proposed credit | Exists / type |
|---|---|---|---|
| Rent | 6100 Rent (Expense) | 2000 AP if billed, or 1000 Bank | Yes / correct |
| Depreciation | 6600 Depreciation (Expense) | 1510 Accumulated Depreciation | Yes / correct |
| Insurance release | 6150 Insurance (Expense) | 1300 Prepaid Expenses | Yes / correct |
| Loan interest | 7000 Interest Expense | 2100 Accrued Liabilities (or 1000 Bank if paid) | Yes / correct |
| Software | 6300 Software (Expense) | 2000 AP | Yes / correct |

All proposed accounts exist and are of the right type. Active status cannot be checked from the upload.

### Items to check before automating a year ahead

- **Insurance release 1,500/month** draws down 1300 Prepaid Expenses; it must stop when the prepaid is used up. Prepaid balance and policy end not supplied.
- **Loan interest fixed at 1,069** on a 2500 Term Loan: interest on an amortising loan normally falls each month; a fixed figure may be wrong — check against the loan schedule.
- **Depreciation fixed at 4,200**: changes with additions and disposals; take it from the asset register each month rather than automate a fixed figure.
- **Rent 9,000 fixed**: lease escalation unknown; the posting history is not the lease.
- **"Day 30"** is ambiguous for month-end entries: in 31-day months it posts on the 30th, not the last day. February 2026 **rolls to 28 Feb** (not skipped). Say whether you mean "last day of month".

### Occurrence schedule, 12 months (Step 3) — all **Pending**

| # | Month | Rent (day 1) | Software (day 5) | Depreciation, insurance, interest (day 30) | Weekend dates (no roll applied) |
|---|---|---|---|---|---|
| 1 | Oct 2025 | 1 Oct | 5 Oct | 30 Oct | 5 Oct Sun |
| 2 | Nov 2025 | 1 Nov | 5 Nov | 30 Nov | 1 Nov Sat; 30 Nov Sun |
| 3 | Dec 2025 | 1 Dec | 5 Dec | 30 Dec | — |
| 4 | Jan 2026 | 1 Jan | 5 Jan | 30 Jan | 1 Jan holiday? |
| 5 | Feb 2026 | 1 Feb | 5 Feb | **28 Feb (rolled)** | 1 Feb Sun; 28 Feb Sat |
| 6–12 | Mar–Sep 2026 | 1st | 5th | 30th | 1 Mar Sun; 5 Apr Sun; 30 May Sat; 5 Jul Sun; 1 Aug Sat; 30 Aug Sun |

Memos: "{entry} — {month} {year}", e.g. "Rent — October 2025"; unique per occurrence. Per occurrence: rent 9,000; software 3,500 (**held** until September is explained); depreciation 4,200; insurance 1,500; interest 1,069 = **19,269 a month**. 12-month total **231,228** = 12 × 19,269 (rent 108,000; software 42,000; depreciation 50,400; insurance 18,000; interest 12,828). No tax applied — no tax codes supplied. Accrual reversals: only if the September software accrual is adopted (1 Oct 2025).

## 4. What was not done, and why

| Item | Status | Needed |
|---|---|---|
| Creating any template; posting any occurrence | **Not done — read-only.** A person does this | — |
| Run audit against the ledger; duplicate check (2c); automation candidates (2d) | **Not done** | GL / JE listing, vendor list |
| Active-account and tax-code validation | Not done | Live chart or tax-code list |
| Roll to business days | Not applied | Holiday calendar and roll policy |
| Escalation, end dates, stop conditions | Fixed / 12-month horizon assumed | Contracts, loan and prepaid schedules |

## 5. Coverage and provenance (manual run)

- **A — Environment:** Northbrook Trading Ltd, USD, as at 30 Sep 2025 — user-asserted; source **upload**; **NOT VALIDATED**; **nothing posted**. Files: register *accepted with a limit*; chart *accepted with a limit*; `recurring_entries_final.csv` *rejected (shift rota)*.
- **B — Capability map:** not applicable — no connection; every task `[manual]` or `[auto: computed]`.
- **C — Steps:** 1 type — assumed JE; 2 validate — done, open-ended flagged; 2b — done against upload; 2c, 2d — **not done**; 3 occurrences — computed; 4 escalation — none supplied; 5 template — proposed mapping; 5b run audit — done on your flags (software missing Sep).
- **E — Unknowns:** software September; insurance prepaid end; loan interest basis; weekend rolls.
- **F — Parameters:** monthly; days 1 / 5 / 30 (30 → 28 in Feb); no roll; horizon 12 months to Sep 2026; fixed amounts; USD.

Would you like `Northbrook_Trading_Ltd_RecurringSchedule_2025-09-30.xlsx`? Only on your yes.
