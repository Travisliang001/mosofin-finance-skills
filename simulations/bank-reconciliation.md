# Bank reconciliation — Northbrook Trading Ltd, September 2025 (upload path)

The Mosofin tools are not present, so this run is manual: it works only from the files you uploaded. Nothing was posted, marked cleared or signed off.

## (a) Read-back

Reconciling **one cash account of Northbrook Trading Ltd** (the account is not named in your answers or in the files; no account number is shown anywhere) for **1–30 September 2025**, in **USD**, against **the bank statement you uploaded**, with the books read from **the cash ledger you uploaded**.

Intake questions left unanswered, and the default applied:

| Question | Status | Default applied |
|---|---|---|
| B — which account | Not answered; files carry no account name or masked identifier | Treated as a single operating account. Please confirm the name and masked identifier. |
| E — last reconciled | Not answered, no prior report | **The bridge starts unqualified**: opening outstanding items are unknown. I recommend establishing a baseline. |
| F — materiality | Not answered | I am **proposing** USD 100 as the level below which an item needs no named owner. This is my proposal, not your policy. The bridge is tied to the cent regardless. |
| Cutoff policy | Not supplied | Method defaults: match window same day ± 3 business days; deposits in transit escalate after 10 business days, outstanding cheques after 90 days. |

## (b) Validation of the upload — shown before any work

| File | What it actually is | Company / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `bank_statement_2025-09.csv` | A bank statement: date, description, amount, running balance. 16 rows (opening line + 15 transactions) | 1–30 Sep 2025. No company or account name in a header; the payroll lines read "PAYROLL NORTHBROOK TRADING". Currency not stated; USD taken from intake | Yes. Running balance recomputed line by line and it foots: opening 1,246,642 → ending **1,219,776** | Yes — Steps 1–4 (statement side) | **Accepted with a limit**: account identity and currency rest on your intake answer, not on the file |
| `cash_account_ledger_2025-09.csv` | GL activity for a cash account: date, description, amount. 16 rows (opening + 15 entries) | 1–30 Sep 2025; opening 1,246,642 agrees with the statement opening. No entity name in the file | Yes, with gaps: no reference or counterparty column, and no separately stated ending balance (no trial balance). Ending balance derived by summing: **1,230,316** | Yes — Steps 1–5 (book side) | **Accepted with a limit**: book ending balance is a sum of the ledger, not agreed to a trial balance; reference matching (method 3) is only possible where the cheque number sits in the description |
| `bank_statement_2025-09_final.csv` | **Not a bank statement.** Its content is a staff shift rota: columns employee, week_1…week_4; rows E08–E10 with "nights / days / off" | No company, no dates, no amounts | No — nothing in it this skill can use | No — no step uses a rota | **Rejected.** The file name suggests a final statement but the content is a rota. If a later "final" statement exists, please upload it; otherwise I use `bank_statement_2025-09.csv`. Set aside and not read into the work. |

Still missing: the account name and masked identifier (required, typed in chat); a trial balance to confirm the GL ending balance (required form of the ending balance); a chart of accounts (needed to name real accounts in proposed entries); the prior reconciliation and cutoff policy (recommended).

*I would stop here and wait for your answer. Assumed answer: "go ahead with the accepted files".*

## (c) Findings

**Bank statement supplied: yes.** No figure rests on mock data. Both sides: same account (as confirmed by you), USD, as at 30 September 2025.

### Reconciliation summary — two ladders

| Bank side | USD | | Book side | USD |
|---|---:|---|---|---:|
| Statement ending balance 30 Sep | 1,219,776.00 | | GL cash ending balance 30 Sep | 1,230,316.00 |
| + Deposit in transit (Tideswell Hotels, booked 30 Sep) | 12,400.00 | | − Monthly service fee not recorded (30 Sep) | (50.00) |
| − Outstanding cheque 2291 (Orchard Packaging, booked 29 Sep) | (3,150.00) | | − ACH debit ORIG 88213 not recorded (24 Sep) — **unidentified** | (1,240.00) |
| **Adjusted bank balance** | **1,229,026.00** | | **Adjusted book balance** | **1,229,026.00** |

Raw difference between statement and books: 1,230,316 − 1,219,776 = **10,540.00**, fully explained: 12,400 − 3,150 + 50 + 1,240 = 10,540. The ladders meet to the cent **only if** the 1,240 debit is a genuine charge to be booked. If it proves to be unauthorised or a bank error, it moves to the bank ladder as a bank error (+1,240) and the two ladders meet at 1,230,266.00 instead. Either way no unexplained residue remains, but **I do not call the account reconciled while that item is unidentified.**

### Matched list — 13 of 15 statement lines

All 13 matched by **method 1** (exact amount, same date); descriptions are also identical. Cheque 2287 additionally matches by reference (method 3).

Pennine Retail 41,200 (2 Sep) · Check 2287 −8,400 (3 Sep) · Stripe 18,842 (5 Sep) · Halden Property −9,000 (8 Sep) · Castleton Foods 36,100 (10 Sep) · Payroll −52,310 (12 Sep) · Wire Kestrel −64,200 (15 Sep) · Wire fee −35 (15 Sep) · Ridgeway 27,950 (17 Sep) · Stripe 21,307 (19 Sep) · Term loan −6,900 (22 Sep) · Payroll −52,310 (26 Sep) · Ashby Engineering 22,180 (29 Sep).

Book-side duplicate test: payroll −52,310 appears twice (12 and 26 Sep). Both clear the bank on the same dates, two weeks apart — a bi-weekly payroll, not a duplicate. No other repeated amount.

### Unmatched — bank side (on the statement, not in the books)

| Date | Statement line | USD | Classification | Owner / next action |
|---|---|---:|---|---|
| 30 Sep | MONTHLY SERVICE FEE | −50.00 | Bank fee | Bookkeeper: post the proposed entry below |
| 24 Sep | ACH DEBIT UNKNOWN ORIG 88213 | −1,240.00 | **Unknown — needs research.** No payee, nothing in the ledger at this amount | Controller: ask the bank for the originator of ID 88213 and check for an authorisation, within 5 business days. Unauthorised ACH debits have short return windows, so this is urgent. Do not book it to an expense account until identified. |

### Unmatched — book side (in the books, not on the statement)

| Date | Ledger line | USD | Classification | Note |
|---|---|---:|---|---|
| 30 Sep | Deposit — Tideswell Hotels | 12,400.00 | Deposit in transit (money banked that the bank has not yet credited) | Booked on the last day; confirm it appears on the October statement. Escalate if not credited within 10 business days (by 14 Oct). |
| 29 Sep | Check 2291 to Orchard Packaging | −3,150.00 | Outstanding cheque (issued, not yet cashed) | 1 day old at period end; normal timing. Escalate at 90 days. |

### Other observations

- The loan payment of 6,900 is booked as one cash line; this ledger cannot show whether it was split between principal and interest. Outside this skill's scope, noted for the loan schedule.
- The Stripe transfers (18,842 and 21,307) match the bank exactly; whether they are net of processor fees is a matter for the processor reconciliation, not this one.

### Proposed entries — proposals only, nothing posted

No chart of accounts was uploaded, so the account names below are **generic placeholders**, not your real account names. Supply the chart of accounts and I will restate them.

1. Record bank fee — evidenced by statement line 30 Sep "MONTHLY SERVICE FEE −50"
   DR Bank fees expense 50.00 / CR Cash (bank account) 50.00
2. **Held, not proposed for posting** — statement line 24 Sep "ACH DEBIT UNKNOWN ORIG 88213 −1,240". Once identified: if a valid charge, DR the relevant expense or payable 1,240.00 / CR Cash 1,240.00; if unauthorised, no entry — dispute with the bank and carry as a bank-side reconciling item.

After entry 1 only, the GL would read 1,230,266.00 and the single open item is the 1,240 debit.

### Sign-off

Preparer: ____________ Reviewer: ____________ (two different people; I fill in neither and cannot sign.)

## (d) What was not done, and why

| Task | Verdict | Gap |
|---|---|---|
| Statement ending balance (Step 1) | manual — from your upload | Account name / masked identifier and currency not in the file |
| GL ending balance (Step 1) | manual — summed from the ledger upload | No trial balance to agree it to |
| Bridge and matching (Steps 2–3) | done from uploads | Opening outstanding items unknown — no prior reconciliation; bridge starts unqualified |
| Classification (Step 4) | done | 1,240 ACH debit left as "unknown" — only the bank can identify the originator |
| Proposed entries (Step 5) | partial | Real account names need the chart of accounts; entry for the 1,240 held |
| Sign-off (Step 6) | manual | Needs two named people |
| `bank_statement_2025-09_final.csv` | rejected | A shift rota, not a statement; not used |
| Save preferences (Step 7) | not offered yet | Only after you have reviewed these results |

Would you like this workpaper as an Excel file (`Bank_Rec_[AccountName]_2025-09.xlsx`)? I will create it only if you say yes.

**Data sources:** user uploads only — `bank_statement_2025-09.csv` (statement side), `cash_account_ledger_2025-09.csv` (book side). No Mosofin connection was used.
