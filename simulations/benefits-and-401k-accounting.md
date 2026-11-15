# Employee benefits and 401(k) — Northbrook Trading Ltd, September 2025 (upload path)

Mosofin is not connected, so this run is manual: every figure comes from the files you uploaded. Connecting Mosofin would read the benefit accounts and the remittances to the plan automatically ([docs.mosofin.com](https://docs.mosofin.com)). Nothing was posted or remitted. Every entry below is a proposal.

## Read-back

Benefits for **Northbrook Trading Ltd** (user-asserted), **September 2025**, in **USD**, under **US GAAP**. **No defined benefit plan** (as you said), so no actuarial work is needed. From your plan terms document, confirmed here for the read-back:
- **401(k):** employees contribute 4% of gross, matched 100% on the first 4%; the match vests 33% a year over three years.
- **Remittance:** employee contributions are due **within 7 business days of each pay date**.
- **Paid time off (PTO):** 15 days a year, accrued monthly, up to 5 days carried forward, **paid out on leaving**. So PTO must be accrued.

Unanswered: **question C, the other benefits.** No health, insurance or other benefit is named in any file. I treat none as in scope, but **a benefit with no account is the one most likely to be unaccrued**, so please confirm.

## Validation of the upload (shown before any work)

| File | What it actually is | Company / period | Usable? | Used by | Verdict |
|---|---|---|---|---|---|
| `payroll_register_2025-09.csv` | Payroll register, 12 employees (E01–E12): gross, income tax, social security, 401(k), net. Every row recomputes (gross − deductions = net) | No company or currency; month from the file name and your intake | Yes. Gross **70,599**; 401(k) withheld **2,824**; net **53,902** | Steps 2, 6, 7 | **Accepted with a limit**: company and period user-asserted; monthly totals, not per pay run |
| `payroll_gl_detail_2025-09.csv` | GL extract, 5 lines on 6000 Payroll Expense, 2150 Payroll Clearing, 2160 Payroll Tax Payable | Dated 12–30 Sep 2025 | Partly. **The extract does not balance**: debits to expense 76,000, credits 60,502 (55,102 net pay + 5,400 tax). No 401(k) payable or match account appears | Steps 2, 7 | **Accepted with a limit**: an extract of three accounts, not the full entry |
| `benefit_plan_terms.md` | Plan **summary** (not the plan document), with a PTO table for 4 employees | As at 30 Sep 2025 | Yes, as user-supplied terms | Steps 1–3, 6 | **Accepted with a limit**: a summary; PTO balances for only 4 of 12 employees |
| `payroll_register_2025-09_final.csv` | **Not a payroll register.** A staff shift rota: E08–E10, week_1…week_4, "nights / days / off" | No amounts or dates | No | No step | **Rejected** on content. The name suggests a final register. Upload it if one exists; otherwise the register above is used. |

**Still missing:** PTO balances for **E02, E03, E05, E07, E08, E09, E10, E11** (required for their accrual); the **401(k) remittance records** to the plan administrator for September (required for the remittance test); the GL balances of the 401(k) payable and accrued PTO accounts (needed for the roll-forward and the adjustment); the full September payroll entry; whether any employee has left (needed for forfeitures).

*Here I would stop and wait for your answer. Assumed answer: "go ahead with the accepted files".*

## Findings

**1. The employer 401(k) match, 2,824, has not been recorded.** Every employee contributes exactly 4% of gross (2,824 in total), so the match is 100% of that: **2,824** for September. Payroll expense of 76,000 is gross 70,599 plus employer social security 5,401, to the dollar. Nothing in it, or anywhere in the extract, is a match. Under US GAAP the match is expensed as employees earn it, in September, whatever its vesting. Vesting only matters when someone leaves, and forfeited match then reduces cost.

**2. Employee 401(k) withholdings, 2,824: no liability, no evidence of remittance.** The register withholds 2,824 from employees, and no 401(k) payable appears in the GL extract. **Remittance cannot be confirmed: no payments to the plan were supplied.** Against the 7-business-day deadline:

| Pay run | Pay date | Due by | Employee 401(k) (half of 2,824) | Status at 30 Sep |
|---|---|---|---:|---|
| Run 1 | 12 Sep | **23 Sep** | 1,412 | **Past due if unremitted**, 5 business days late |
| Run 2 | 26 Sep | 7 Oct | 1,412 | Not yet due |

The split assumes equal runs: both net-pay runs are exactly 26,951. Late remittance of withheld employee money is a compliance breach, not just a late payment. Please send the remittance record.

**3. Employee money in employer expense: test passed.** Payroll expense 76,000 = gross 70,599 + employer FICA 5,401. Gross includes the employees' own 401(k), as it should, and no withholding is counted twice. Employee social security of 5,401 equals 7.65% of gross, and so does the employer share.

**4. The payroll extract does not tie to the register. Two problems.**
- **Net pay over-credited by 1,200.** 2150 Payroll Clearing was credited 55,102 for net pay, but the register's net is 53,902, and that was paid (two runs of 26,951). That leaves the **1,200 credit sitting in Payroll Clearing**.
- **Withholdings largely missing.** The register implies credits of income tax 8,472 + employee social security 5,401 + employer social security 5,401 + 401(k) 2,824 = **22,098**. The extract shows only 5,400 to 2160, described as "taxes withheld *and* employer share, unpaid". That is one share of social security, not all of it. The extract is 15,498 short of balancing: 76,000 − 60,502.

Either the rest sits in accounts not exported, or it was never recorded. Please send the full entry before anything is corrected. This belongs in `payroll-reconciliation` / `payroll-journal-entry-builder`.

**5. PTO liability: 19,166.40 for the four employees with balances. Eight employees not computed.**

| Employee | Hours unused | Hourly rate (plan terms) | Liability |
|---|---:|---:|---:|
| E01 | 64 | 45.00 | 2,880.00 |
| E04 | 88 | 39.80 | 3,502.40 |
| E06 | 40 | 42.70 | 1,708.00 |
| E12 | 120 | 92.30 | 11,076.00 |
| **Total, 4 of 12** | | | **19,166.40** |

The supplied rates are about 7.65% above the hourly pay the register implies (e.g. E01 7,246 / 173.3 h ≈ 41.80 against 45.00). They appear to include employer payroll tax. That is a reasonable basis, since a payout carries the tax, but please confirm. The existing accrued PTO balance was not supplied, so the adjustment cannot be computed. The figure above is the required balance for these four only.

## Proposed entries (proposals only; nothing posted)

| # | Entry | Amount | Status |
|---|---|---:|---|
| 1 | DR 401(k) match expense / CR 401(k) contributions payable | 2,824.00 | Ready. Account names not in the files: use your own |
| 2 | DR PTO expense / CR Accrued PTO liability | 19,166.40 **less the existing balance** | Not final: existing balance and 8 employees missing |
| — | Payroll Clearing 1,200 and the withholding credits | — | **Investigating**: needs the full payroll entry |

## Not done, and why

- Remittance test and 401(k) payable roll-forward: no remittance records or payable balance.
- PTO for 8 employees and the PTO roll-forward: no balances; no GL balance.
- Forfeitures: no leaver data. Short-term benefits (health, insurance): none identified, so please confirm.
- Defined benefit: none, as you said.
- Disclosure figures: DC cost for September is **2,824** once entry 1 is accepted; PTO policy as above.
- Excel workpaper `Benefits_Accounting_2025_Northbrook Trading Ltd.xlsx`: not created. Would you like it?

## Coverage sheet (manual run)

**Environment:** Northbrook Trading Ltd, September 2025, USD, US GAAP, all user-asserted. Data source: upload, because the Mosofin gateway is absent. Register, GL extract and plan summary accepted with limits; rota rejected.
**Capability map:** Not applicable: no connection. Every task is `[manual]`.

| Step | Status |
|---|---|
| 1 Categorise | Done: DC 401(k), PTO; no DB; other benefits unconfirmed |
| 2 Defined contribution | Done with a limit: match computed; **remittance not verified** |
| 3 PTO | Done with a limit: 4 of 12 employees |
| 4 Short-term benefits | Not done: none identified |
| 5 Defined benefit | Not applicable: no plan |
| 6 Vesting / forfeitures | Not done: no leaver data |
| 7 Reconciliation | Done with a limit: register vs GL extract; 1,200 and 15,498 gaps open |
| 8 Output | Tables in chat |

**Data sources:** upload — payroll_register_2025-09.csv, payroll_gl_detail_2025-09.csv, benefit_plan_terms.md.
