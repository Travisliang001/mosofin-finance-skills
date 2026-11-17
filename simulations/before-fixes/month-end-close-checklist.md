# Month-end close — Northbrook Trading Ltd, September 2025 (upload path)

Mosofin is not used for this run (you chose upload only), so every task is `[manual]` and every "evidence" entry below comes from your files, not from the books. Nothing was posted, no task was marked complete, no books were locked. **DRAFT — close calendar, owners, materiality and reporting framework are not yet given.**

## Read-back

Close checklist for **Northbrook Trading Ltd** (user-asserted), period **September 2025**, as at **30 September 2025**, in **USD** (user-asserted), from your uploads.

| Not answered at intake | What I applied |
|---|---|
| Target close date / calendar | Not given. Laid out on the skill's standard Day 1–7 allocation (business days 1–9 Oct 2025); flexes once you give a target |
| Reporting framework | Not given; does not change the task list. Please confirm |
| Owners / team | Not given → every owner is **TBD**; the checklist is worth little until they are filled |
| Materiality threshold | **Not assumed** (the skill says never to). Step 4 split above/below threshold is blocked |
| Soft or hard close | Not given → treated as a **soft** monthly close (the skill's stated norm for month-ends) |
| Existing close template | None supplied → standard list, scoped to your chart |

## Validation of the upload — shown before any work

| File | What it actually is | Company / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `trial_balance_2025-09-30.csv` | Trial balance, 33 accounts, YTD P&L | No company/date in file | Foots: DR = CR = 6,546,018; every account in the chart | Yes — scoping, Day 5 review, Step 6 tie-out | **Accepted with a limit: company and period user-asserted** |
| `trial_balance_2025-08-31.csv` | Prior-month trial balance, same 33 accounts | No company/date in file | Foots: DR = CR = 6,106,903 | Yes — BS variance and continuity proxy | **Accepted with a limit**: date from the file name |
| `chart_of_accounts.csv` | Chart, 41 accounts with types | No company | Yes | Yes — Step 2 scoping | **Accepted** |
| `recurring_entries.csv` | Log of 5 recurring entries with "posted" yes/no for Jul–Sep 2025 | No company | Yes | Yes — Day 3 status | **Accepted with a limit**: self-reported status, not posting evidence |
| `bank_statement_2025-09.csv` | Bank statement, 1–30 Sep 2025, 15 lines; running balance recomputes, 967,387 → 992,439 | No account number; payroll lines read "NORTHBROOK TRADING" | Yes | Yes — Day 2 bank rec status | **Accepted with a limit**: account identity inferred from the payee text |
| `trial_balance_2025-09-30_v2.csv` | A 4-line TB for **another company**: account 1000 is "Bank — Harlow Fabrication Ltd"; total 306,000 vs 6,546,018 | Harlow Fabrication Ltd | Foots, wrong entity | No step | **Rejected** on content despite the September name. If a revised Northbrook TB exists, upload it |

Still missing: **close calendar / target date, owners, materiality, framework**; September **GL detail or journal listing** (status evidence for Day 3 and a true opening-balance continuity check); **bank outstanding-items list** (bank rec); whether **Northbrook UK** is consolidated by this team.

*I would stop here and wait for your answer. Assumed answer: "go ahead with the accepted files".*

## Step 2 — Scoping from the chart and the TB (with evidence)

| Task group | Applies? | Evidence |
|---|---|---|
| Inventory cutoff, count/roll-forward, write-downs | **Yes** | 1200 Inventory 683,100 |
| Depreciation / fixed assets | **Yes** | 1500 cost 420,000; 1510 accumulated depreciation 311,200 |
| Accruals, prepaid amortisation | **Yes** | 2100 accrued 28,800; 1300 prepaid 18,000 |
| Loan amortisation | **Yes** | 2500 term loan 220,000 |
| Intercompany reconciliation (Day 4) | **Yes** | 2300 payable to Northbrook UK 38,000; 1600 investment in Northbrook UK 104,800 |
| Consolidation, translation (Day 6) | **Out for this entity's close; confirm** | You named one company; a UK subsidiary exists, so the group close would need it |
| FX revaluation | **Confirm** | No foreign-currency account; the UK intercompany balance may be GBP-denominated |
| Deferred revenue release | **Removed** | 2400 Deferred Revenue is in the chart with no balance in either TB |
| Payroll clearing, payroll tax, sales tax | **Yes** | 2150 1,200; 2160 5,400; 2200 2,600 |
| Merchant processor rec | **Yes** | 1050 Stripe Clearing 6,420; two Stripe transfers on the bank statement |
| Nonprofit / fund steps, stock comp, leases, intangibles | **Removed** | No such accounts in the chart |

## Close calendar (owners TBD; status verifiable only from uploads)

| Day | Task (linked skill) | Status | Evidence from your files |
|---|---|---|---|
| −5–0 | Calendar sent; bank and vendor statements requested | Not known | Bank statement received |
| 1 | AR/AP/inventory/payroll cutoff; bank imported to 30 Sep | Not verifiable | Needs GL entry dates |
| 2 | Bank rec (`bank-reconciliation`) | **Open — difference** | GL 1000 **1,002,979** vs statement **992,439**: GL higher by **10,540**; at 31 Aug GL 904,810 vs statement opening 967,387 (−62,577). Needs outstanding items |
| 2 | Stripe rec (`merchant-and-payment-processor-rec`) | **Open** | 1050 unchanged at 6,420 although 40,149 of Stripe transfers landed in September |
| 2 | AR/AP ageing, cash application | Not verifiable | AR fell 33,070; AP fell 15,685 |
| 3 | Rent 9,000 | Log: posted | TB 6100 +9,000; bank "Halden Property Mgmt" 9,000 on 8 Sep |
| 3 | Depreciation 4,200 | Log: posted | 6600 +4,200 and 1510 +4,200 |
| 3 | Insurance release 1,500 | Log: posted | 6150 +1,500 — **but 1300 Prepaid did not move (18,000 both months)** |
| 3 | Loan interest 1,069 | Log: posted | 7000 +1,069; 2500 down 5,000 |
| 3 | Software subscription 3,500 | **Log: NOT posted** | **6300 rose 3,500 in September anyway** — status and evidence disagree |
| 3 | Accruals, bad-debt true-up | Not verifiable | 2100 +200; allowance 9,000 unchanged |
| 4 | Payroll clearing (`payroll-clearing-reconciliation`) | Open | 2150 1,200 and 2160 5,400 unchanged; net pay out 52,702 (2 × 26,351) vs payroll expense 76,000 |
| 4 | Intercompany, tax accounts, BS recs | Open | 38,000 intercompany and 2,600 sales tax unchanged |
| 5 | TB review, BS variance, fluctuations | **Done (analysis)** | Findings below |
| 6 | Consolidation | Out (confirm) | — |
| 7 | Statements, review, lock, distribute | Not started | — |

Critical path: bank rec → Stripe rec → TB review → statements. **Outside dependencies (nobody here can advance them):** bank outstanding items, vendor statements, Northbrook UK's confirmation of the 38,000.

## Findings

1. **Software subscription: log says not posted, TB says 3,500 was booked** (6300: 28,000 → 31,500 = nine months × 3,500). Either the log is stale or the charge went through another route (e.g. a bill) — confirm before the books lock, or September could carry it twice.
2. **Insurance release is posted (1,500) but prepaid never moves** — 1300 is 18,000 at both month-ends. The credit side of the release is going somewhere else.
3. **Bank does not agree to the GL:** GL higher by 10,540 at 30 Sep; −62,577 at 31 Aug. Unexplained bank items: **ACH debit "UNKNOWN ORIG 88213" 1,240** (24 Sep); **loan payment 6,900** vs 5,000 principal + 1,069 interest = 6,069 (831 unexplained).
4. **Static balances to reconcile**: Stripe 6,420, allowance 9,000, prepaid 18,000, corporate card 7,300, payroll clearing 1,200, payroll tax 5,400, sales tax 2,600, intercompany 38,000, petty cash 500 — all unchanged Aug → Sep.
5. **September P&L**: revenue 455,400, net income 52,923. Gross margin **40.0%** vs 41.5% YTD to August. Marketing **29,146 = 6.4% of revenue**. No income-tax account exists.
6. **Dividends 67,500** sit in 3200 YTD; no change in September.
7. **Tie-out (Step 6)**: TB balances — **true by construction**, not proof the month is closed. Continuity: **not run as a true check** — no September opening balances; the proxy is that retained earnings (1,378,654) and dividends (67,500) are identical in both TBs and every Aug → Sep movement is listed above. Books locked: unknown.

## Not done, and why

Owners, due times, materiality split (Steps 3–4: not given); status evidence for cutoff and Day 3 entries beyond the TB movement (no GL); bank, Stripe, payroll and intercompany recs (hand-offs; headline differences only); lessons-learned timing (no posting dates). No `.xlsx` created — I would ask whether you want `MonthEndClose_2025-09_Northbrook Trading Ltd.xlsx`.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, Sep 2025, USD — user-asserted. Source: upload. Sep and Aug TBs, bank statement, recurring log accepted with limits; chart accepted; `_v2` TB rejected (Harlow Fabrication Ltd). |
| Capability map | Not applicable: no connection. Every task is `[manual]`. |
| Steps | 1 task list done · 2 scoping done · 3 owners/deadlines **not done** (not given) · 4 materiality **not done**; risk areas done · 5 open items done · 6 tie-out partial (continuity proxy only) · 7 **not done** (no timing data) · 8 tables in chat, no file. |
| Not done | Per-account continuity (Sep GL with opening balances); posting evidence (journal listing); bank rec (outstanding items); materiality list (threshold). |

**Data sources:** user uploads — `trial_balance_2025-09-30.csv`, `trial_balance_2025-08-31.csv`, `chart_of_accounts.csv`, `recurring_entries.csv`, `bank_statement_2025-09.csv`.
