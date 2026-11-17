# Payroll reconciliation — Northbrook Trading Ltd, September 2025 (upload path)

Mosofin is not connected, so this run is manual: every figure comes from the files you uploaded, and every step is `[manual]`. Connecting Mosofin would read the GL side, the liability balances and the recorded payments automatically ([docs.mosofin.com](https://docs.mosofin.com)). Nothing was posted, remitted or amended; every correction below is a proposal.

## Read-back

Payroll reconciliation for **Northbrook Trading Ltd** (user-asserted), **September 2025**, as at 30 Sep 2025, **USD**. September is a **quarter end**, so Steps 4 and 5 (filings, taxable wage bases) apply. No payroll platform is connected: the register is supplied.

Unanswered, and how each is handled:
- **Remittance due dates** for each liability: not given. The skill never defaults a due date, so **no overdue flag can be raised**; the liabilities are listed with their amounts and the flag is blocked.
- **Taxable wage base rules** (pre-tax deductions, caps): not given. **Step 5 is NOT PERFORMED.**
- **Third-party provider:** nothing suggests one; the bank shows the company paying net pay itself. Treated as self-remitted — please confirm.
- **Opening liability balances / prior reconciliation:** not given. Roll-forwards start from an unknown opening balance.

## Validation of the upload (shown before any work)

| File | What it actually is | Company / period | Usable? | Used by | Verdict |
|---|---|---|---|---|---|
| `payroll_register_2025-09.csv` | Payroll register, 12 employees: gross, income tax, social security, 401(k), net. Every row foots | No company or dates; month from name and intake | Yes for totals: gross **70,599**, net **53,902**. No employer-cost or taxable-wage columns | Steps 1, 2, 3 | **Accepted with a limit**: company and period user-asserted; cannot support Step 5 |
| `payroll_gl_detail_2025-09.csv` | GL detail, 10 lines on 6000, 2150, 2160, 2170, 1000, dated 12–30 Sep 2025. Debits = credits = 142,576 | Sep 2025; company not named | Yes, but **activity only**: no opening or closing balances | Steps 1, 2, 3 | **Accepted with a limit**: roll-forwards have no opening anchor |
| `bank_statement_2025-09.csv` | Operating bank statement, 1–30 Sep 2025, 15 lines. Opening **967,387**, closing **992,439**; running balance foots | Sep 2025; company and account not named | Yes | Steps 2, 3 | **Accepted with a limit**: company user-asserted |
| `payroll_register_2025-09_final.csv` | **Not a payroll register.** A shift rota for E08–E10, week_1–week_4, "nights / days / off" | No amounts, no dates | No | No step | **Rejected** on content: the name says "final register" but it holds no pay data. Upload the final register if one exists |

**Still missing:** remittance due dates per liability (required for the overdue flag); taxable wage base rules (required for Step 5); Q3 filing figures (recommended, Step 4); opening balances of 2150 / 2160 / 2170 at 31 Aug (recommended, roll-forward); the tax authority's confirmation of the August deposit (see finding 2).

*Here I would stop and wait for your answer. Assumed answer: "go ahead with the accepted files".*

## Findings — ordered by consequence

**1. Net pay: the bank paid 52,702, the register says 53,902 — 1,200 short, sitting in Payroll Clearing.**

| | Amount |
|---|---:|
| Net pay per register | 53,902 |
| Credited to 2150 Payroll Clearing (30 Sep) | 53,902 |
| Bank: PAYROLL NORTHBROOK TRADING, 12 Sep | 26,351 |
| Bank: PAYROLL NORTHBROOK TRADING, 26 Sep | 26,351 |
| **Paid per bank** | **52,702** |
| **Unpaid / unexplained, left as a credit in 2150** | **1,200** |

Tied to the **bank statement**, not just to recorded disbursements. 1,200 is smaller than any one employee's net pay, so it is not a single missed payslip. Likely causes: a manual cheque not yet presented, a deduction left out of the register, or a register error. **Until it is explained, Payroll Clearing does not return to nil** and either employees are owed 1,200 or the register overstates net pay. Ref: PR-09-01.

**2. The August tax deposit, 13,874, is in the GL but not in the bank statement.** The GL debits 2160 and credits 1000 Operating Bank on 15 Sep, memo "August deposit". **No such debit appears on the operating account's statement for September.** Either it was paid from another account (please send that statement), or **it was not paid**. If unpaid, withheld tax is overdue, with penalties, interest and possibly **personal liability for directors**. The due date was not supplied, so the overdue flag cannot be dated. **Confirm with the authority.** Ref: PR-09-02.

**3. Register ties to the GL — but on the same postings basis.**

| Component | Register | GL | Difference |
|---|---:|---:|---:|
| Gross wages | 70,599 | 6000 (gross + employer SS) 76,000 | — |
| Employer social security (7.65%, not in register) | 5,401 (derived) | included in 76,000 | 0 |
| Income tax + employee SS + employer SS | 8,472 + 5,401 + 5,401 = 19,274 | 2160 credit 19,274 | 0 |
| 401(k) deferrals | 2,824 | 2170 credit 2,824 | 0 |
| Net pay | 53,902 | 2150 credit 53,902 | 0 |

No manual adjustments to payroll accounts appear in the detail. **Limit:** the register has no employer-cost column, so employer social security is inferred as 76,000 − 70,599 = 5,401 (7.65% of gross is 5,400.82). The tie confirms the journal was built from the register; it does not independently prove either.

**4. Liability movements in September (opening balances not supplied)**

| Liability | Opening | + Accrued | − Remitted | = Movement | Note |
|---|---:|---:|---:|---:|---|
| 2150 Payroll Clearing | not supplied | 53,902 | 52,702 | **1,200 credit** | Should be nil: finding 1 |
| 2160 Payroll Tax Payable | not supplied | 19,274 | 13,874 (GL only) | 5,400 credit | August deposit unverified: finding 2. September's 19,274 unpaid at 30 Sep |
| 2170 401(k) Payable | not supplied | 2,824 | 0 | 2,824 credit | **No remittance to the plan in September**; due date not given |

Negative balances: none in the movements; closing balances cannot be confirmed without openings. Employer and employee taxes share 2160, so they cannot be rolled forward separately.

**5. Unrelated bank item:** `ACH DEBIT UNKNOWN ORIG 88213`, 1,240 on 24 Sep, is not a payroll movement. Pass it to `bank-reconciliation`.

## Not performed, and why

- **Step 4 — filings:** no Q3 filing figures supplied. GL wages for September are 70,599 gross; July and August were not supplied, so no quarter total.
- **Step 5 — taxable wage bases: NOT PERFORMED.** The register has no taxable-wage columns and no wage base rules were given. It would show whether income tax and social security were charged on gross or on gross less the 401(k) deferrals, and any cap effects. A gross × rate check is not offered as a substitute.
- Overdue flags: no due dates.
- Excel workpaper `Payroll_Reconciliation_2025-09_Northbrook Trading Ltd.xlsx`: not created. Would you like it?

## Exceptions and corrections (proposals only)

| Ref | Item | Type | Amount | Correction | Status |
|---|---|---|---:|---|---|
| PR-09-02 | August deposit not on bank statement | Possible missed remittance | 13,874 | Evidence of payment, or pay and reverse the GL entry | Open: penalty exposure |
| PR-09-01 | Net pay unpaid / unexplained in clearing | Error or timing | 1,200 | Identify; pay, or correct the register / journal via `payroll-journal-entry-builder` | Open |
| — | 401(k) not remitted in September | Timing until due date known | 2,824 | Confirm the plan's due date | Open |

## Coverage sheet (manual run)

**Environment:** Northbrook Trading Ltd, September 2025, USD — user-asserted. Data source: upload (Mosofin gateway absent). Register, GL detail and bank statement accepted with limits; rota rejected. Sources: register supplied; GL supplied; bank **statement** supplied; filings not obtained.
**Capability map:** Not applicable: no connection. Every task is `[manual]`.

| Step | Status |
|---|---|
| 1 Register to GL | Done with a limit: ties; employer cost inferred; same-postings basis |
| 2 Net pay to bank | Done: 1,200 short against the bank statement |
| 3 Liabilities | Done with a limit: movements only, no opening balances, no due dates |
| 4 Filings | Not done: no filing figures |
| 5 Taxable wage bases | **NOT PERFORMED**: no wage base data or rules |
| 6 Exceptions | Done: 3 items, ordered by consequence |
| 7 Output | Tables in chat |

**Data sources:** upload — payroll_register_2025-09.csv, payroll_gl_detail_2025-09.csv, bank_statement_2025-09.csv.
