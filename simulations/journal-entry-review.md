# Journal entry review — Northbrook Trading Ltd, September 2025 (upload path)

Mosofin is not connected, so this run is manual: every step works from your uploads and is marked `[manual]`. (Connecting Mosofin would automate the reads — docs.mosofin.com.) Nothing was corrected, reversed, reclassified or posted. **A flag is a question about an entry, not a conclusion about a person.**

## (a) Read-back

Reviewing the **journal entries of Northbrook Trading Ltd** (company name user-asserted; no file names it) for **September 2025, as at 30 September 2025**, in **USD**, from the files you uploaded. **Journal approval threshold: 10,000. August books closed on 12 September 2025.**

Not answered at intake, and what I did:

| Question | Default applied |
|---|---|
| Materiality threshold | **Not defaulted** (the skill never defaults one). The magnitude test uses only your 10,000 approval threshold. |
| Approval / workflow log | Not supplied → the four approval-based indicators are **NOT RUN** |
| Risk-sensitive accounts | Read by account type from the chart: revenue (4000), reserves (1150), equity (3000, 3100), clearing (1050, 2150), intercompany (2300) |
| Expected posting patterns / prior periods | Not supplied → **no baseline**; "unusual" is judged within this month only |
| Known risk areas; topside entries; who may see the output | Not answered. Topside entries are assumed **not** in this population. The output names users — restrict it until you say who may see it. |
| September close date | Not given → the "after close cutoff" test for September cannot run |

## (b) Validation of the upload — shown before any work

| File | What it actually is | Company / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `journal_entries_2025-09.csv` | Journal entry lines: number, effective date, posted-on date, user, account, debit, credit, memo. 14 lines, 7 entries | Effective dates 31 Aug–30 Sep 2025, posted 20 Sep–4 Oct. No entity or currency column | Yes: every entry balances; total debits = credits = 83,799. No source (manual/system), approver or timestamp column | Yes — Steps 1–7 | **Accepted with a limit**: approval, time-of-day and source tests cannot run; one entry is dated in August |
| `chart_of_accounts.csv` | Chart of accounts: number, name, type. 29 accounts | No entity name | Yes; all 9 accounts used in the journals are in it | Yes — account-type criteria (Step 2) | **Accepted** |
| `journal_entries_2025-09_final.csv` | **Not a journal listing.** A staff shift rota: employee, week_1…week_4 with "nights/days/off" for E08–E10 | No company, dates, accounts or amounts | No | No step uses it | **Rejected** on content, despite the name. If a later journal export exists, please upload that. Not used. |

Still missing: the approval log (recommended; four tests depend on it); prior-period journals (baseline, reversal tracing); October journals (to trace reversals of the September accruals); a materiality level; where topside entries live.

*I would stop here and wait for your answer. Assumed answer: "go ahead with the accepted files".*

## (c) Findings

**Screen complete: all 7 entries (14 lines, 83,799) screened; 7 carry at least one criterion; 3 are high priority.** All 7 are treated as manual (no source field). Not mock data.

### Patterns first

- **One entry is 60% of the month's journal value.** JE-0904 (50,000) of 83,799, posted by a user who posted nothing else.
- **Users:** s.patel posted 6 of 7 entries (33,799); a.reyes posted 1 (50,000), directly to revenue. A user name is not a person — shared or delegated logins break that link.
- **Accrued Liabilities (2100) is the credit side of 3 of 7 entries** (12,400 + 3,800 + 9,999 = 26,199). Whether this recurs each month-end cannot be said without prior periods.
- **Weekend postings: 3 of 7** — JE-0904 (Sun 28 Sep), JE-0905 (Sat 20 Sep), JE-0907 (Sat 4 Oct).
- **Two entries exceed the 10,000 approval threshold** (JE-0904 50,000; JE-0903 12,400) and **one sits 1 below it** (JE-0907 9,999).
- Reserves-versus-earnings and target-seeking tests: not run — one period only, no P&L supplied.

### Scoring weights (stated so the score can be read)

2 points each: hits revenue directly; posted to a closed prior period; amount just below the approval threshold; poster outside the month's usual poster. 1 point each: weekend posting; round amount; blank or generic memo; above approval threshold with approval not evidenced; unusual account pairing or memo/account mismatch; back-dated beyond a normal close window; posted after period end (routine close timing, lowest weight).

### Flagged entries, sorted by score

| JE | Date / posted | Posted by | Approved by | Accounts | Amount | Criteria met | Score | Memo | Status |
|---|---|---|---|---|---:|---|---:|---|---|
| JE-0904 | 28 Sep / 28 Sep (Sunday) | a.reyes | not available | DR 1100 Accounts Receivable / CR 4000 Sales Revenue | 50,000 | Revenue hit directly by manual entry (2); unusual poster (2); round 50,000 (1); generic memo "Revenue adjustment" (1); weekend (1); 5× the approval threshold, approval not evidenced (1); AR raised by journal rather than an invoice (1) | **9** | Revenue adjustment | **Needs explanation — high** |
| JE-0907 | 30 Sep / 4 Oct (Saturday) | s.patel | not available | DR 6200 Marketing / CR 2100 Accrued Liabilities | 9,999 | 1 below the 10,000 threshold (2); **blank memo** (1); weekend posting (1); posted after period end (1) | **5** | (blank) | **Needs explanation — high** |
| JE-0905 | 31 Aug / 20 Sep (Saturday) | s.patel | not available | DR 6400 Professional Fees / CR 2100 Accrued Liabilities | 3,800 | **Posted to August 8 days after August closed on 12 Sep** (2); back-dated 20 days (1); weekend (1) | **4** | Legal fee missed in August | **Needs explanation — high** |
| JE-0903 | 30 Sep / 3 Oct | s.patel | not available | DR 6000 Payroll Expense / CR 2100 Accrued Liabilities | 12,400 | Above 10,000, approval not evidenced (1); posted after period end (1) | 2 | Accrued wages | Likely routine; confirm approval |
| JE-0902 | 30 Sep / 2 Oct | s.patel | not available | DR 6100 Rent / CR 1300 Prepaid Expenses | 1,500 | Memo says insurance, expense account is Rent (1); after period end (1) | 2 | Prepaid insurance release | Possible misclassification |
| JE-0906 | 30 Sep / 1 Oct | s.patel | not available | DR 7000 Interest Expense / CR 2500 Term Loan | 1,900 | Interest credited to loan principal, not to an accrual or cash (1); after period end (1) | 2 | Loan interest | Possible misposting |
| JE-0901 | 30 Sep / 2 Oct | s.patel | not available | DR 6600 Depreciation / CR 1510 Accumulated Depreciation | 4,200 | After period end only (1) | 1 | Monthly depreciation | Routine close entry |

### Detailed review of the top three (questions to ask)

1. **JE-0904, 50,000.** What does "adjustment" correct — which customer, which invoice or contract? Why a journal rather than an invoice (the receivable will have no invoice behind it in the AR subledger)? Who approved it, given it is five times the threshold? Why was it posted on a Sunday two days before quarter-end by a user with no other entries? Support needed: contract or delivery evidence and revenue recognition basis. If no support is produced, escalate under the fraud-investigation rules — objectively, with no approval request routed to anyone in scope.
2. **JE-0907, 9,999.** What marketing cost is accrued, from which vendor, on what estimate? A blank memo on an amount one unit under the approval limit needs both the support and a check for a companion entry splitting a larger accrual. None is present in this month's file.
3. **JE-0905, 3,800.** August was closed on 12 September; this entry is dated 31 August and was posted on 20 September. Who reopened August, and were August reports already issued? If so the August figures have changed by 3,800 after issue. The memo is specific and the amount small, so this looks like an error correction posted to the wrong period — the usual treatment would be a September entry. Proposal only: a person decides.

### Control observations (measured)

- Blank memo: 1 of 7 entries (14%); generic memo ("adjustment"): 1 of 7 (14%). By value, 59,999 of 83,799 (72%) carries a blank or generic description.
- A closed period accepted a posting 8 days after close — the period lock is either absent or was lifted.
- Entries over the approval threshold: 2 (62,400). Whether they were approved **cannot be answered** from these files; that is itself the observation.
- Segregation of duties (post versus approve): not testable.
- JE-0902 and JE-0906 are low-value but suggest account coding is not being reviewed (no insurance expense account exists in the chart; interest is going to the loan balance, which would overstate the loan by 1,900 unless interest is contractually capitalised).

## (d) What was not done, and why

| Criterion / task | Why it could not run | What it would have shown | How to obtain it |
|---|---|---|---|
| Entries lacking approval | No approver or status field | Whether JE-0904 and JE-0903 were approved | Approval log from the ledger system |
| Self-approved entries | Same | Poster = approver | Same |
| One person posting and approving (SoD) | Same | Segregation failure | Same |
| Approval controls operating (Step 7) | Same | Control conclusion | Same |
| Outside business hours | No timestamp, dates only (weekend test did run) | Late-night postings | Audit trail export |
| Posted after the September close cutoff | September close date not given | Late entries to September | The close date |
| Baseline of normal volume, usual posters, dormant accounts | One month only | Whether a.reyes or these accounts are unusual historically | 6–12 months of journals |
| Reversals not re-posted | October not supplied | Whether the wage and marketing accruals reverse | October journals |
| Duplicates against other periods | One month only (none within September) | Repeat entries | Prior months |
| Manual vs system split | No source field | The manual proportion | Source column |
| Topside entries | Location unknown | Adjustments above the ledger | Consolidation workpapers |
| Supporting documents, business rationale, final resolution | Need a person | Legitimate / error / escalate | Preparer and reviewer |

Nothing is carried forward or stored from this list. Would you like the workpaper as `JE_Review_2025-09_Northbrook Trading Ltd.xlsx`? Only on your yes.

**Data sources:** user uploads only — `journal_entries_2025-09.csv`, `chart_of_accounts.csv`; threshold and August close date typed at intake. No Mosofin connection used.
