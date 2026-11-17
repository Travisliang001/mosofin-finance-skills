# Payroll tax filings — Northbrook Trading Ltd, Q3 2025 (upload path)

Mosofin is not connected, so this run is manual: every figure comes from the files you uploaded, and every step is `[manual]`. Connecting Mosofin would read the liability accounts and the deposits automatically ([docs.mosofin.com](https://docs.mosofin.com)). **This is a computation for a qualified tax professional to review, not tax advice.** Nothing was deposited, filed or signed.

## Read-back

Preparing **Q3 2025 payroll tax** figures for **Northbrook Trading Ltd** (user-asserted) as employer of record, **USD**, from **the files you uploaded**. From your rate card (*sample rate card v1, tax year 2025*, fictitious — please confirm):
- Income tax withheld **12% of gross**; employee social security **7.65%**; employer social security **7.65%**. No wage-base ceiling or pre-tax rule is stated.
- Deposit schedule for 2025: **monthly, due the 15th of the following month**.
- Returns **quarterly**, filed by the company — **no payroll provider**.

Unanswered: **F (periodic or year-end)** — default applied: periodic Q3 figures only. **Jurisdiction(s)** not named; treated as one. **Other employer taxes** (e.g. unemployment) are not on the rate card; please confirm there are none.

## Validation of the upload (shown before any work)

| File | What it actually is | Company / period | Usable? | Used by | Verdict |
|---|---|---|---|---|---|
| `payroll_register_2025-09.csv` | Payroll register, 12 employees: gross, income tax, social security, 401(k), net; every row foots | No company or dates; September from the name | Yes, totals: gross **70,599**, income tax **8,472**, employee SS **5,401** | Steps 3, 5 | **Accepted with a limit**: company user-asserted; **September only — July and August registers missing for Q3** |
| `payroll_gl_detail_2025-09.csv` | GL detail on 6000, 2150, 2160, 2170, 1000, 12–30 Sep 2025; balances (142,576 each side) | Sep 2025 | Yes, but activity only, no opening balances | Steps 1, 4 | **Accepted with a limit**: September only; no 2160 balance at 1 Jul or 30 Sep |
| `payroll_tax_rules_SAMPLE.md` | Rate card, deposit schedule, return frequency and a list of Q3 deposits | Tax year 2025 | Yes, as user-supplied values with a source | Steps 1–4, statutory values sheet | **Accepted with a limit**: a summary; the deposit list is not deposit confirmations, so deposits are user-supplied, not evidenced |
| `payroll_register_2025-09_final.csv` | **Not a payroll register.** A shift rota for E08–E10, week_1–week_4 ("nights / days / off") | No amounts, no dates | No | No step | **Rejected** on content despite the name. Upload the final register if one exists |

**Still missing:** July and August 2025 registers (required for the Q3 return); deposit confirmations for July and August (required for the reconciliation); the 2160 balance at 30 Jun and 30 Sep (recommended); any wage-base ceilings (required if any apply); prior Q2 filing (recommended).

*Here I would stop and wait for your answer. Assumed answer: "go ahead with the accepted files".*

## Findings

**1. September amount due: 19,274 — agrees to the GL accrual.**

| Tax | Base (gross, per rate card) | Rate | Employee | Employer | Total |
|---|---:|---:|---:|---:|---:|
| Income tax withheld | 70,599 | 12% | 8,472 | — | 8,472 |
| Social security | 70,599 | 7.65% + 7.65% | 5,401 | 5,401 | 10,802 |
| **Total due for September** | | | **13,873** | **5,401** | **19,274** |

12% × 70,599 = 8,471.88 and 7.65% × 70,599 = 5,400.82, both agreeing to the register to rounding. The GL credits 2160 with **19,274**: computed amount due = liability accrued. No ceiling applied (none supplied).

**2. September deposit: 19,274, due 15 Oct 2025, not yet paid** (rate card: "September not yet paid"). Not late at 30 Sep. If unpaid after 15 Oct, it is late and penalties start; the penalty is not computed.

**3. The August deposit does not agree between your two sources: 31,900 on the rate card, 13,874 in the GL.** Both are dated 15 Sep. Difference **18,026**. One of them is wrong: either the GL under-records the payment or the rate card's list is wrong. **Deposit confirmation needed before the Q3 return.**

**4. July and August deposits of 31,900 each look high against September's 19,274.** At the same 27.3% combined rate, 31,900 implies gross of about 116,850 a month against 70,599 in September. If July and August payrolls were like September's, **each was over-deposited by 12,626 (25,252 for the two)** — an over-deposit is not harmless: it ties up cash and needs a credit on the return or a refund claim. If headcount was higher in July and August, it is fine. **Not concluded: the July and August registers are needed.**

**5. Timeliness, per the rate card's dates:** July deposit 14 Aug against a 15 Aug due date — **on time, 1 day early**. August deposit 15 Sep against 15 Sep — **on time, on the due date**. Amounts not verified (finding 3).

**6. Obligations against accounts.** One account, **2160 Payroll Tax Payable**, holds income tax, employee and employer social security together, so the deposit reconciliation cannot be split by tax from the ledger. No account exists for any other employer tax; if an unemployment or similar tax applies, **it may not be accrued at all**.

## Q3 deposit reconciliation (what can be done)

| Month | Liability | Deposited (rate card) | Deposited (GL) | Balance |
|---|---:|---:|---:|---|
| July | not supplied | 31,900 on 14 Aug | not supplied | Not computable |
| August | not supplied | 31,900 on 15 Sep | 13,874 on 15 Sep | **Sources disagree by 18,026** |
| September | 19,274 | — | — | **19,274 due 15 Oct** |
| **Q3** | 19,274 + July + August | 63,800 | — | Not computable |

The evidence stops at the files: neither source proves the authority received the money.

## Q3 return figures — partial

September only: wages 70,599; income tax 8,472; social security 10,802; total 19,274. **The Q3 return cannot be prepared** without July and August. If July and August liabilities equal their deposits, Q3 tax would be 31,900 + 31,900 + 19,274 = 83,074 — shown as a scenario only, not a figure for filing.

## Statutory values used

| Value | Amount / rule | Source | Year |
|---|---|---|---|
| Income tax withholding | 12% of gross | sample rate card v1 | 2025 |
| Employee / employer social security | 7.65% / 7.65% | sample rate card v1 | 2025 |
| Deposit schedule | Monthly, by the 15th of the following month | sample rate card v1 | 2025 |
| Return frequency | Quarterly | sample rate card v1 | 2025 |
| Wage-base ceilings | **None supplied** | — | — |

## Not done, and why

- Q3 return and July/August reconciliation: no July and August registers or deposit confirmations.
- Year-end wage statements: not in scope (periodic default).
- Penalties: not computed, per the skill.
- Excel workpaper `Payroll_Tax_Filings_Q3-2025_Northbrook Trading Ltd.xlsx`: not created. Would you like it?

## Coverage sheet (manual run)

**Environment:** Northbrook Trading Ltd, Q3 2025, USD — user-asserted. Data source: upload (Mosofin gateway absent). Register, GL and rate card accepted with limits; rota rejected. No provider.
**Capability map:** Not applicable: no connection. Every task is `[manual]`.

| Step | Status |
|---|---|
| 1 Obligations | Done with a limit: from the rate card; other employer taxes unconfirmed |
| 2 Deposit schedule | Done: monthly, 15th, user-supplied |
| 3 Amounts due | Done for September only |
| 4 Deposits vs liabilities | Done with a limit: August sources disagree; July/August liabilities missing |
| 5 Periodic return | Not done: two of three months missing |
| 6 Year-end | Not in scope |
| 7–8 Package and output | Tables in chat |

**Data sources:** upload — payroll_register_2025-09.csv, payroll_gl_detail_2025-09.csv, payroll_tax_rules_SAMPLE.md.
