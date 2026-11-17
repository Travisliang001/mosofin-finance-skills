# Defined benefit pension (ASC 715) — Northbrook Trading Ltd, 30 September 2025 (upload path)

Mosofin is not connected, so this run is manual: every figure comes from the files you uploaded, and every step is `[manual]`. Connecting Mosofin would read the pension liability, OCI and contributions from your books ([docs.mosofin.com](https://docs.mosofin.com)). **Every entry below is a proposal; nothing was posted.** No actuarial figure or assumption was estimated: every one comes from the actuary's summary.

## Read-back

Accounting for the **staff pension plan** of **Northbrook Trading Ltd** (user-asserted) at **30 September 2025**, **USD**. From the uploaded summary (please confirm, as the answers to intake questions B–D): a **defined benefit plan** under **ASC 715**, measured at **30 September 2025**, report dated **20 October 2025** by **Marlow Actuaries**. The measurement date equals the reporting date.

Unanswered, defaults applied:
- **E — amendments, curtailments, settlements:** none stated. **Assumed none**, as the skill requires me to say.
- **F — prior-year roll-forwards:** not supplied. Opening position taken from the summary's opening figures and checked against the trial balance (see finding 1).

## Validation of the upload (shown before any work)

| File | What it actually is | Company / period | Usable? | Used by | Verdict |
|---|---|---|---|---|---|
| `actuarial_report_summary.md` | **Summary** of an actuarial valuation: PBO and plan assets opening/closing, cost components, contributions, benefits paid, discount rate; plus one line about the ledger | Plan sponsor not named; measured 30 Sep 2025 | Yes; both roll-forwards close | Steps 1–6 | **Accepted with a limit**: a summary, not the report; figures user-supplied, not evidenced; no assumptions beyond the 5.0% discount rate, no AOCI balance, no sensitivity or benefit forecast |
| `trial_balance_2025-09-30.csv` | Trial balance, 33 accounts, debits = credits = **6,546,018** | 30 Sep 2025; company not named | Yes | Step 0b (recorded position) | **Accepted with a limit**: company user-asserted; balances only, no ledger detail |
| `actuarial_report_summary_final.csv` | **Not an actuarial report.** A staff shift rota: E08–E10, week_1–week_4, "nights / days / off" | No amounts | No | No step | **Rejected** on content despite its name. Upload the full actuarial report if that is what was meant |

**Still missing:** the full actuarial report (required for disclosures: assumptions, sensitivity, expected contributions, benefit forecasts); prior-year roll-forwards and the opening AOCI balance (recommended); ledger detail showing where the 45,000 contributions were booked (recommended, so the contribution entry is not proposed twice).

*Here I would stop and wait for your answer. Assumed answer: "go ahead with the accepted files".*

## Findings

**1. No pension entry has been posted — and the trial balance carries no pension liability at all.** The summary says "no pension entry posted in the nine months", and the TB confirms it: there is **no pension liability, no pension expense and no AOCI account**. The summary's line "Ledger: pension liability 220,000" is **not supported by the TB**: the only 220,000 balance is **2500 Term Loan**. 220,000 does equal the opening funded status (960,000 − 1,180,000), so it is what the books *should* have carried at the start. **Either the opening liability was never recognised (a prior-period error) or it sits in an account not on this TB.** Please confirm which.

**2. Obligation and plan assets roll forward cleanly.**

| PBO | Amount | | Plan assets | Amount |
|---|---:|---|---|---:|
| Opening | 1,180,000 | | Opening fair value | 960,000 |
| + Service cost | 62,000 | | + Actual return | 41,000 |
| + Interest cost | 59,000 | | + Employer contributions | 45,000 |
| ± Actuarial loss | 0 | | − Benefits paid | (36,000) |
| − Benefits paid | (36,000) | | | |
| **Closing** | **1,265,000** | | **Closing** | **1,010,000** |

Both close to the report's figures with no difference.

**3. Funded status: 1,010,000 − 1,265,000 = 255,000 underfunded.** A **net pension liability of 255,000** should be on the balance sheet at 30 Sep. Recorded: **nil**. No asset ceiling issue (deficit).

**4. Net periodic benefit cost: 63,400 to earnings; 16,600 loss to OCI.**

| Component | Earnings | OCI |
|---|---:|---:|
| Service cost (compensation cost) | 62,000 | |
| Interest cost | 59,000 | |
| Expected return on assets (ASC 715) | (57,600) | |
| **Net periodic benefit cost** | **63,400** | |
| Asset loss: expected 57,600 − actual 41,000 | | **16,600** |
| Actuarial loss on obligation | | 0 |
| Amortisation of prior service cost / gains and losses | not given | not given |

Proof: liability movement 255,000 − 220,000 = **35,000** = 63,400 + 16,600 − 45,000. No amortisation figures are in the summary; if AOCI carries opening losses beyond the corridor, the actuary must supply the amortisation.

**5. Contributions of 45,000 per the report: where they were booked is unknown.** There is no pension account on the TB, so they were either charged to expense (e.g. 6000 Payroll Expense) or not paid by the company. Ledger detail is needed before the contribution entry is proposed.

**6. The chart cannot present the components.** There is no separate service-cost or other-components account, so the ASC 715 presentation (service cost with compensation, the rest outside operating income) and the components disclosure cannot be produced from the ledger.

## Proposed entries — PROPOSED, NOT POSTED (new accounts needed: no pension accounts exist)

| # | Entry | Debit | Credit | Status |
|---|---|---:|---:|---|
| 1 | DR Compensation expense — service cost / CR Net pension liability | 62,000 | 62,000 | Ready once accounts exist |
| 1 | DR Pension cost, other components (interest 59,000 − expected return 57,600) / CR Net pension liability | 1,400 | 1,400 | Ready |
| 2 | DR AOCI — pension / CR Net pension liability (asset loss) | 16,600 | 16,600 | Ready |
| 3 | DR Net pension liability / CR where the contributions were booked | 45,000 | 45,000 | **Pending**: confirm where the 45,000 sits, to avoid double counting |
| 4 | Recognise the opening liability: DR opening equity (retained earnings / AOCI split per prior roll-forwards) / CR Net pension liability | 220,000 | 220,000 | **Pending**: prior-period error; split needs prior-year roll-forwards |

After all four, the net pension liability is 220,000 + 63,400 + 16,600 − 45,000 = **255,000**, equal to the funded status.

## Recorded vs actuarial (Step 0b)

| Check | Recorded (TB) | Per report | Difference |
|---|---:|---:|---:|
| Balance sheet position | nil | (255,000) | 255,000 |
| Earnings cost | nil | 63,400 | 63,400 |
| OCI | nil | 16,600 | 16,600 |

## Not done, and why

- Disclosure tables beyond the roll-forwards and components: the summary gives only the discount rate (5.0%); no other assumptions, expected contributions or benefit forecasts.
- AOCI roll-forward and amortisation: no opening AOCI.
- Memo and Excel workpaper `Pension_Accounting_2025_Northbrook Trading Ltd.xlsx`: not created. Would you like them?

## Coverage sheet (manual run)

**Environment:** Northbrook Trading Ltd, 30 Sep 2025, USD — user-asserted. Data source: upload (Mosofin gateway absent). Actuarial summary and TB accepted with limits; rota rejected.
**Capability map:** Not applicable: no connection. Every task is `[manual]`.

| Step | Status |
|---|---|
| 0b Recorded vs actuarial | Done: nothing recorded |
| 1 Plan and components | Done: DB, ASC 715; amortisation not given |
| 2 Roll-forwards | Done: both close |
| 3 Funded status | Done: 255,000 deficit |
| 4 Cost split | Done: 63,400 earnings / 16,600 OCI |
| 5 Entries | Done with a limit: 3 and 4 pending |
| 6 Disclosures | Done with a limit: roll-forwards and components only |
| 7 Output | Tables in chat |

**Data sources:** upload — actuarial_report_summary.md (Marlow Actuaries, 20 Oct 2025), trial_balance_2025-09-30.csv.
