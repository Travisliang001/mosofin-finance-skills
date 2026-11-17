# Month-end close: Northbrook Trading Ltd, September 2025

Mosofin is not connected, so this run is manual: every task is `[manual]` and every status below
is what your uploads show, not a live read. (Connecting Mosofin would pre-populate task status from
the books: [docs.mosofin.com](https://docs.mosofin.com).) Nothing is posted, locked or marked
complete. Every entry below is a draft for you to review.

## Read-back (please confirm)

> Closing **September 2025** for **Northbrook Trading Ltd**, USD, from **your uploads**.
> **Assumptions, as nothing in the files answers them:** framework not stated; **hard close**
> (September is a calendar quarter end and retained earnings show a December year end; this is the
> more conservative reading — tell me if it is a soft close); no target close date, owners or
> materiality given, so owners are "to assign" and **no materiality is applied**. Go ahead?

## Validation of the upload (shown before any work)

| File | What it actually is | Company / period | Usable? | Step | Verdict |
|---|---|---|---|---|---|
| `trial_balance_2025-09-30.csv` | Trial balance, 33 accounts, YTD | No company named; 30 Sep 2025 | Foots: 6,546,018 each side | Scoping, tie-out, Day 5 review | **Accepted with a limit**: company user-asserted |
| `trial_balance_2025-08-31.csv` | Trial balance, 33 accounts, YTD | No company named; 31 Aug 2025 | Foots: 6,106,903 each side | Prior period: September's movement, continuity | **Accepted with a limit**: company user-asserted |
| `bank_statement_2025-09.csv` | Bank statement, 1–30 Sep 2025, 15 transactions | No bank or account named | Running balance recomputes: 970,887 + 25,052 = 995,939 | Day 2 bank reconciliation | **Accepted with a limit**: account user-asserted; no GL cash detail to match against |
| `recurring_entries.csv` | Recurring entry log, Jul–Sep posted flags | No company named | Readable | Day 3 status (Evidence column) | **Accepted with a limit**: a user-kept log, checked against the TB below |
| `chart_of_accounts.csv` | Chart of accounts, 41 accounts with types | Names Northbrook UK as intercompany | All 33 TB accounts appear in it | Step 2 scoping | **Accepted** |
| `trial_balance_2025-09-30_v2.csv` | 4-line balance listing; bank line **"Bank — Harlow Fabrication Ltd"** | **Harlow Fabrication Ltd**, not Northbrook | Foots (306,000) but not this company's | None | **Rejected**: a different company's trial balance. If Harlow is a group company in scope, tell me and I will add it as a separate entity |

**Still missing:** general ledger detail for September (cash account especially) to reconcile the
bank and test cutoff; Northbrook UK's September TB for the intercompany pair; close calendar, owners,
materiality. I would wait for your answer; this run continues on the five accepted files.

## Scoping (Sheet 8): what applies, with the evidence

| Task group | Applies? | Evidence |
|---|---|---|
| Inventory cutoff, count, write-downs | **Yes** | 1200 Inventory 683,100 |
| Fixed assets / depreciation | **Yes** | 1500 cost 420,000; 1510 −311,200 |
| Accruals and prepaids | **Yes** | 2100 28,800; 1300 18,000 |
| Payroll cutoff and clearing | **Yes** | 2150, 2160 balances; payroll on the bank |
| Sales tax reconciliation | **Yes** | 2200 2,600 |
| Merchant processor rec | **Yes** | 1050 Stripe Clearing 6,420; Stripe transfers on the bank |
| Intercompany and Day 6 consolidation | **Yes** | 1600 Investment in Northbrook UK Ltd 104,800; 2300 payable 38,000. Northbrook UK is not uploaded: its tasks stay with an owner, unverifiable |
| FX | **Likely** (at consolidation) | A UK subsidiary; its currency not given |
| Deferred revenue release | **No** | 2400 in chart, no balance |
| Leases, intangibles, stock comp | **No** | no accounts |

## Findings

**1. Software subscription not posted in September.** Your recurring log shows Software 3,500 "no"
for September, and the TB agrees: 6300 Software is 28,000 at both 31 Aug and 30 Sep. Draft entry, if
the service was received: **Dr 6300 Software 3,500 / Cr 2100 Accrued liabilities 3,500**.
Marketing moved 29,146 in September against ~18,000 a month: check whether the software charge was
coded to marketing instead.

**2. The other recurring entries are evidenced in the TB** (Evidence, not completeness): rent 9,000
(6100), depreciation 4,200 (6600 and 1510), insurance 1,500 (6150), interest 1,069 (7000), loan
principal 5,000 (2500: 225,000 → 220,000).

**3. Insurance released but prepaids unchanged.** 6150 rose 1,500, yet 1300 Prepaid stays at 18,000.
Either a new prepayment of exactly 1,500 was added or the release was credited elsewhere. Reconcile 1300.

**4. Bank does not tie to the GL.** GL cash 1,006,479 vs bank 995,939: **10,540 more in the books**.
At 31 August the bank was 66,077 *above* the GL (970,887 vs 904,810). GL cash moved +101,669 in
September; the bank moved +25,052. A swing from −66,077 to +10,540 needs the reconciling items listed.
Items on the bank to trace: **ACH debit "UNKNOWN ORIG 88213" 1,240**; **loan payment 6,900 vs 6,069
booked** (5,000 principal + 1,069 interest; 831 unexplained); wire fee 35 and service fee 50. Status:
**not reconciled** — I cannot verify a reconciliation from the ledger.

**5. Static balances to reconcile.** Unchanged from August to the dollar: Stripe Clearing 6,420,
Allowance 9,000, Corporate Card 7,300, Payroll Clearing 1,200, Payroll Tax 5,400, Sales Tax 2,600,
Intercompany 38,000, Investment 104,800. A clearing or tax account that never moves is either dormant
or not being reconciled.

**6. September movement.** Revenue 455,400; COGS 273,240 (gross margin 40.0%); net income 56,423.
AR −33,070, inventory −28,461, AP −15,685. No budget supplied, so no budget variance.

**7. Inter-period continuity: not run.** Both files are closing TBs; September's opening balances
need the GL. Retained earnings is 1,378,654 in both, as expected mid-year.

## Close calendar (Sheet 1, extract)

| Day | Task | Owner | Status | Evidence |
|---|---|---|---|---|
| 1 | AR / AP / inventory / payroll cutoff | to assign | not verifiable | needs GL |
| 2 | Bank reconciliation | to assign | **Open: 10,540 unreconciled** | bank 995,939 vs GL 1,006,479 |
| 2 | Stripe reconciliation | to assign | Open | 1050 static at 6,420 |
| 3 | Rent, depreciation, insurance, interest | to assign | Entries evidenced | TB movements above |
| 3 | Software subscription | to assign | **Not posted** | 6300 unchanged |
| 3 | Bad debt allowance true-up | to assign | Not evidenced | 1150 unchanged at 9,000 |
| 4 | Prepaids, accruals, payroll, sales tax recs | to assign | Open | static balances |
| 4 | Intercompany with Northbrook UK | to assign | **Blocked (external)** | UK TB not supplied |
| 5 | TB review, BS variance to August | done here | Done | movements above |
| 6 | Consolidation | to assign | Blocked by Day 4 | |
| 7 | Statements, review, lock, distribute | to assign | Not started | books lock is a person's |

**External dependencies (grouped):** Northbrook UK's TB; the bank's detail for the 1,240 debit and the
6,900 loan payment; the software supplier's invoice.

## Final tie-out (Sheet 6)

| Item | Result |
|---|---|
| TB balances | Yes, 6,546,018 — true by construction; it does not show the month is closed |
| BS accounts reconciled | **No**: bank open (10,540), eight static balances unreconciled |
| Inter-period continuity | **Not run**: needs September GL |
| Adjusting entries posted | Software 3,500 not posted |
| Books locked | Unknown (a system state) |

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, September 2025, USD: **user-asserted**. Data source **upload** (Mosofin not used). 5 files accepted (4 with limits), 1 rejected (Harlow TB). Hard close assumed |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 1 built; 2 scoped (above); 3 owners **not given**; 4 **no materiality** (not assumed), risk areas flagged; 5 open items listed; 6 done with a limit (no GL); 7 **not done** (no posting dates); 8 tables in chat |
| Not done | Cutoff and continuity (need GL); intercompany (need UK TB); budget variance (need budget) |

Data sources: your uploads, as validated above. Would you like `MonthEndClose_2025-09_Northbrook Trading Ltd.xlsx`?
