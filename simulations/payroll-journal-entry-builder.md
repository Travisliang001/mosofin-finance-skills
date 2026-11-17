# Payroll journal entries — Northbrook Trading Ltd, September 2025 (upload path)

Mosofin is not connected, so this run is manual: every figure comes from the files you uploaded, and every step is `[manual]`. Connecting Mosofin would read the chart, prior runs and liability balances automatically ([docs.mosofin.com](https://docs.mosofin.com)). **Every entry below is a proposal — PROPOSED, NOT POSTED.** Nothing was posted, paid or changed.

## Read-back

Payroll for **Northbrook Trading Ltd** (user-asserted), **September 2025**, as at 30 Sep 2025, **USD**. From your rate card (*sample rate card v1, tax year 2025*, fictitious): income tax withheld 12%, employee social security 7.65%, **employer social security 7.65%**; deposits monthly, due the 15th of the following month. Please confirm these as your rates.

Unanswered, and how each is handled:
- **Pay period and pay date(s):** not given. Required — **the period-end accrual (Step 6) is blocked** until you give them.
- **Clearing account:** not stated. Your chart has **2150 Payroll Clearing**, so the net pay credit below goes there; if you pay net pay straight from 1000, it credits 1000 instead. Please confirm.
- **Employer 401(k) match:** no file states one. Not defaulted; not booked.
- **Department allocation basis:** the register tags each person to a department, so direct assignment is shown, **pending your confirmation**. No department dimension was supplied.
- **Capitalised labour:** none flagged in the register; treated as none — please confirm.

## Validation of the upload (shown before any work)

| File | What it actually is | Company / period | Usable? | Used by | Verdict |
|---|---|---|---|---|---|
| `payroll_register_2025-09.csv` | Payroll register, 12 employees, 6 departments: gross, income tax, social security, 401(k), net. Every row foots (gross − deductions = net) | No company, currency or dates; month from the name and your intake | Yes. Gross **70,599**; net **53,902**. No employer-cost columns, no pay date | Steps 1–4, 7 | **Accepted with a limit**: company and period user-asserted; no pay dates; employer costs not in it |
| `chart_of_accounts.csv` | Chart of accounts, 41 accounts with types | Company not named | Yes | Steps 1–3, 5, 7 | **Accepted with a limit**: company user-asserted |
| `payroll_tax_rules_SAMPLE.md` | Rate card and deposit schedule, plus Q3 deposits made | Tax year 2025 | Yes, as user-supplied rates | Steps 3, 7 (employer cost, liabilities, run comparison) | **Accepted with a limit**: a summary, fictitious rates; figures user-supplied, not evidenced |
| `payroll_register_2025-09_final.csv` | **Not a payroll register.** A shift rota: E08–E10, week_1–week_4, "nights / days / off" | No amounts, no dates | No | No step | **Rejected** on content: the name says "final register", but it has no pay data. Upload the final register if one exists; otherwise the register above is used |

**Still missing:** pay period and pay date(s) (required: accrual); prior payroll runs or journals (recommended: run comparison); employer 401(k) match terms (required for full cost); the GL balances of 2150 / 2160 / 2170 and any accrual from August (recommended: reversal check).

*Here I would stop and wait for your answer. Assumed answer: "go ahead with the accepted files".*

## Findings

**1. Gross-to-net identity holds.** Gross 70,599 = income tax 8,472 + employee social security 5,401 + 401(k) 2,824 + net 53,902. It holds on every row as well, and the withholdings match the rate card (12% of 70,599 = 8,471.88; 7.65% = 5,400.82; 401(k) is 4% on every row).

**2. Employer social security, 5,401, is not in the register and has to be booked on top.** 7.65% × 70,599 = 5,400.82, matched to the employee share of 5,401. **Total payroll expense = 70,599 + 5,401 = 76,000.** It is additional expense, not a deduction — crediting it anywhere in the employee entry would balance and be wrong.

**3. Employer and employee liabilities share one account.** Income tax, employee social security and employer social security all go to **2160 Payroll Tax Payable** (19,274). Your chart has no separate accounts, so `payroll-reconciliation` and `payroll-tax-filings` cannot separate them from the ledger either. The split is kept in the memos below.

**4. Chart gaps — no accounts invented.** No separate payroll tax expense, employer match expense, net pay payable or accrued payroll account exists. Employer tax is debited to **6000 Payroll Expense**; an accrual, when computable, would use **2100 Accrued Liabilities**. Add accounts if you want these split.

**5. Run comparison: September's tax liability is 40% below the deposits for July and August.** The rate card shows deposits of **31,900** for July and for August. September's liability is **19,274**, which is **12,626 (39.6%) lower**. At the same 27.3% combined rate, 31,900 implies gross of about **116,850** a month, against 70,599 now. That is a headcount change, a missing pay run in this register, or a deposit error. **Please explain before posting.** No prior registers were supplied, so per-head and per-component comparison could not run.

**6. Personal data.** Admin and Management each have one employee, so a department total would disclose one person's pay. They are combined below. No individual pay appears in this output.

## Proposed entries — PROPOSED, NOT POSTED

**JE 1 — Gross pay and employee withholdings** (memo: "Sep 2025 payroll — gross to net")

| Account | Debit | Credit | Memo |
|---|---:|---:|---|
| 6000 Payroll Expense | 70,599 | | Gross wages |
| 2160 Payroll Tax Payable | | 8,472 | Income tax withheld |
| 2160 Payroll Tax Payable | | 5,401 | Employee social security |
| 2170 401(k) Payable | | 2,824 | Employee 401(k) deferrals |
| 2150 Payroll Clearing (or 1000 if paid direct) | | 53,902 | Net pay |
| **Total** | **70,599** | **70,599** | Balanced |

**JE 2 — Employer costs** (memo: "Sep 2025 payroll — employer social security")

| Account | Debit | Credit |
|---|---:|---:|
| 6000 Payroll Expense | 5,401 | |
| 2160 Payroll Tax Payable (employer share) | | 5,401 |

Employer 401(k) match: **not booked** — no terms supplied.

**JE 3 — Clearing:** when the bank pays net pay, DR 2150 / CR 1000, 53,902. Date pending the pay date.

**JE 4 — Period-end accrual: blocked.** Needs the pay period end and pay date. If any September work is paid in October, the accrual must include employer social security (7.65% on top).

**Department allocation (direct assignment from register — basis to confirm)**

| Department | Headcount | Gross | Employer SS | Total cost |
|---|---:|---:|---:|---:|
| Operations | 3 | 16,906 | 1,293 | 18,199 |
| Sales | 2 | 12,077 | 924 | 13,001 |
| Finance | 2 | 11,333 | 867 | 12,200 |
| Warehouse | 3 | 11,797 | 902 | 12,699 |
| Admin + Management | 2 | 18,486 | 1,415 | 19,901 |
| **Total** | **12** | **70,599** | **5,401** | **76,000** |

Employer SS rounded by department; the 1 rounding difference sits in the largest line. The allocation sums to the total.

**Liability summary** (feeds `payroll-tax-filings`)

| Payable | Amount | To whom / when |
|---|---:|---|
| 2160 Payroll Tax Payable | 19,274 | Tax authority; monthly deposit due **15 Oct 2025** (September not yet paid, per rate card) |
| 2170 401(k) Payable | 2,824 | Plan administrator; timing not supplied |
| 2150 Payroll Clearing (net pay) | 53,902 | Employees, on the pay date (not supplied) |

## Validation (Step 7)

| Check | Result |
|---|---|
| Each entry balances | Pass: JE 1 70,599 = 70,599; JE 2 5,401 = 5,401 |
| Gross = net + employee withholdings | Pass: 70,599 = 53,902 + 16,697 |
| Total expense = gross + employer costs | Pass: 76,000 = 70,599 + 5,401 (match excluded, not supplied) |
| Every account exists in the chart | Pass: 6000, 2150, 2160, 2170, 1000 all in the uploaded chart |
| Employer / employee liabilities distinct | **Fail — limitation**: both in 2160 |
| Liabilities match amounts to be remitted | Not done: no remittance records beyond the rate card |
| Allocation sums to total | Pass |
| Run-over-run comparison | **Flag**: 19,274 vs 31,900 deposits; no prior registers |
| Prior accrual reversed | Not done: no August accrual or GL supplied |

## Not done, and why

- Period-end accrual: no pay period or pay date.
- Employer 401(k) match: no plan terms.
- Per-head run comparison and prior-accrual reversal: no prior runs or GL detail.
- Excel workpaper `Payroll_JE_2025-09-30_Northbrook Trading Ltd.xlsx`: not created. Would you like it?

## Coverage sheet (manual run)

**Environment:** Northbrook Trading Ltd, September 2025, USD — user-asserted. Data source: upload (Mosofin gateway absent). Register, chart and rate card accepted with limits; rota rejected.
**Capability map:** Not applicable: no connection. Every task is `[manual]`.

| Step | Status |
|---|---|
| 1 Register components and mapping | Done: 4 components mapped; shared 2160 noted |
| 2 Gross / withholding entry | Done |
| 3 Employer cost entry | Done with a limit: social security only; match not supplied |
| 4 Department allocation | Done with a limit: direct assignment, basis to confirm |
| 5 Net pay funding | Done with a limit: clearing assumed from the chart |
| 6 Accrual | Not done: no pay dates |
| 7 Validation | Done with a limit: comparison and reversal checks not runnable |
| 8 Output | Tables in chat |

**Data sources:** upload — payroll_register_2025-09.csv, chart_of_accounts.csv, payroll_tax_rules_SAMPLE.md.
