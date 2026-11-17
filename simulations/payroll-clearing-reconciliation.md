# Payroll clearing reconciliation — Northbrook Trading Ltd, September 2025 (upload path)

Mosofin is not used for this run (you chose upload only), so every step is `[manual]` and works from your files. **Nothing was posted, remitted or written off: every entry below is a proposal.** Payroll data is personal: this workpaper works at account level and reports **counts and totals only** — no individual's pay or deductions appear below.

## Read-back

Reconciling the payroll control accounts of **Northbrook Trading Ltd** (user-asserted) for **September 2025**, as at **30 September 2025**, in **USD** (user-asserted), from **your uploads**: 2150 Payroll Clearing, 2160 Payroll Tax Payable, 2170 401(k) Payable (proposed from the GL detail — please confirm the list).

| Not answered at intake | What I applied |
|---|---|
| Remittance cadence per liability | **Not defaulted** (the skill never defaults it). The behaviour test and "expected balance" for 2160 and 2170 are **blocked** — I show what each reading would mean |
| Opening balances at 31 Aug 2025 | Not supplied → roll-forwards show **September movement only** |
| Materiality for write-offs | Not given; no write-off proposed |
| Benefit / 401(k) provider statement, prior reconciliation | Not supplied |

## Validation of the upload — shown before any work

| File | What it actually is | Company / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `payroll_gl_detail_2025-09.csv` | GL detail, 10 lines: September payroll journal (6000 / 2150 / 2160 / 2170) and three bank payments | No company named; dated 12–30 Sep 2025 | Foots: DR = CR = 142,576. **Movements only — no opening or closing balances** | Yes — Steps 1–5 | **Accepted with a limit**: company user-asserted; roll-forward lacks opening balances |
| `payroll_register_2025-09.csv` | Payroll register: 12 employees, gross, income tax, social security, 401(k), net pay | No company or pay dates in file | Every row foots (gross − deductions = net); totals below | Yes — Steps 2, 5 | **Accepted with a limit**: company and period user-asserted; one monthly total, not per pay run |
| `payroll_register_2025-09_final.csv` | **Not a register.** A shift rota (employees by week, day/night/off) — no pay amounts | No company, no period, no amounts | No financial content | No step | **Rejected** on content despite its name. Not read into the work |

Still missing: **opening balances (TB at 31 Aug and 30 Sep 2025)** for 2150, 2160, 2170 — required for the roll-forward and ageing; **remittance cadence** for payroll tax and 401(k) — required; **bank statement** (to prove money left, not just that it was recorded); **several prior months of GL** for the ageing and never-clearing test; 401(k) provider statement.

*I would stop here and wait for your answer. Assumed answer: "go ahead with the accepted files".*

## Register vs payroll journal (Step 2) — basis: register

| Component | Register (12 employees) | Payroll journal | Difference |
|---|---:|---:|---:|
| Gross pay | 70,599 | — | |
| Employer social security (76,000 − 70,599) | 5,401 (= employee share 5,401) | in 6000 76,000 | 0 |
| Net pay → 2150 | 53,902 | 53,902 | **0** |
| Income tax 8,472 + employee SS 5,401 + employer SS 5,401 → 2160 | 19,274 | 19,274 | **0** |
| 401(k) deferrals → 2170 | 2,824 | 2,824 | **0** |

The journal agrees with the register on every component.

## September roll-forward (movement only — openings missing)

| Account | Opening | + Accrued | − Remitted / paid | = Sep movement | Expected | Status |
|---|---|---:|---:|---:|---|---|
| 2150 Payroll Clearing | **not supplied** | 53,902 | 52,702 (2 runs × 26,351, 12 and 26 Sep) | **+1,200** | Nil after the cycle | **Investigating** |
| 2160 Payroll Tax Payable | **not supplied** | 19,274 | 13,874 ("August deposit", 15 Sep) | +5,400 | One month's withholdings if remitted monthly → 19,274 | Blocked (cadence) |
| 2170 401(k) Payable | **not supplied** | 2,824 | **0** | +2,824 | Depends on cadence | Blocked (cadence) |

Bank tie-out (Step 5) — **recorded disbursements only, not the bank statement**: net pay 26,351 on 12 Sep and 26,351 on 26 Sep; tax deposit 13,874 on 15 Sep. Total payroll cash out recorded in September: **66,576**.

## Findings

1. **Payroll clearing does not clear: 1,200 of September net pay was not disbursed.** Register net pay 53,902 vs two equal runs totalling 52,702. A clearing account should return to nil after the cycle. Possible causes, by the skill's list: unclaimed or returned pay, a held final payment, or a run that excluded part of the register. **It may be owed to an employee** — it must not be written off; if unclaimed it can become escheatable. Needs the run-level register and the bank statement. *(Referenced by amount only.)*
2. **Payroll tax: September's 19,274 is still outstanding at 30 September**, and the August deposit (13,874) was **5,400 less than September's accrual** (19,274 − 13,874 = 5,400). If August's withholdings were of similar size, a 5,400 residual may be surviving each remittance — the never-clearing pattern. Needs the 31 Aug balance and the August accrual to confirm.
3. **401(k) deferrals of 2,824 were withheld and not remitted in September.** Employee deferrals must reach the plan promptly; confirm the cadence and that the October remittance includes them.
4. **Register and journal agree on every component** (difference 0) — so the journal is right *as to the register*. Because openings are missing, the closing GL balances themselves are **not reconciled**.

## Proposed entries

None. The 1,200 is investigating, not a known error; tax and 401(k) are timing until the cadence says otherwise. Timing differences are documented, not adjusted.

## Not done, and why

Ageing and never-clearing residual over twelve periods (Step 0b — no prior months); GL vs expected closing (Step 3 — no openings); bank-statement tie (Step 5 — no statement); YTD reconciliation (Step 6 — no YTD data); escheatment determination (manual, and premature). No `.xlsx` created — I would ask whether you want `Payroll_Recs_2025-09.xlsx`.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, Sep 2025, USD — user-asserted. Source: upload. GL detail and register accepted with limits; `_final` register rejected (shift rota). |
| Capability map | Not applicable: no connection. Every task is `[manual]`. |
| Steps | 0b **not done** (no history) · 1 done (3 accounts proposed) · 2 done, register basis · 3 movement only, **closing not reconciled** · 4 done for clearing · 5 recorded disbursements only · 6 **not done** · 7 flagged (1,200; possible 5,400) · 8 none proposed · 9 tables in chat. |
| Not done | Roll-forward from opening (TB at 31 Aug); ageing (prior GL months); bank tie (statement); cadence-based expected balances (your cadences). |

**Data sources:** user uploads — `payroll_gl_detail_2025-09.csv`, `payroll_register_2025-09.csv`.
