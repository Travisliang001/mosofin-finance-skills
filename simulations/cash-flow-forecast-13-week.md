# 13-week cash flow forecast — Northbrook Trading Ltd, 1 Oct – 30 Dec 2025 (upload path)

Mosofin is not connected, so this run is manual and uses only your uploads (connecting Mosofin would read payment history and derive each customer's days-to-pay: docs.mosofin.com). **Direct method** (actual cash in and out). Nothing was paid, drawn or deferred; every lever is a proposal.

## (a) Read-back

Forecasting cash for **Northbrook Trading Ltd**, **13 weeks from Wed 1 Oct to Tue 30 Dec 2025**, in **USD**, opening from **your September bank statement**, with **your 30 Sep A/R aging, open bills, September payroll register and term-loan summary**, against a **minimum cash of 250,000** (your intake answer).

| Input | Status | Treatment |
|---|---|---|
| Horizon | Not answered | Default 13 weeks |
| Opening cash, accounts counted | One bank statement; no other accounts named; restricted cash not stated | 1,219,776 (statement, 30 Sep), assumed unrestricted |
| Minimum cash 250,000 | Given; covenant or management choice not stated. The loan summary has no liquidity covenant | Treated as a **management floor**, not a covenant |
| Collection timing | No payment history uploaded, so days-to-pay **cannot be derived** | **Assumed**: current invoices on due date; overdue ≤45 days in week 2; overdue >60 days excluded as at-risk |
| Bill payment plan | Not given | Each bill paid in its due-date week |
| Payroll pay dates | Not given; statement shows 12 and 26 Sep | Bi-weekly every second Friday from 10 Oct (6 runs) |
| Payroll tax remittance dates, employer taxes, other taxes, new sales, new purchases, facility | Not supplied | Not forecast; listed as gaps below |

## (b) Validation of the upload — shown before any work

| File | What it actually is | Company / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `bank_statement_2025-09.csv` | Bank statement, 15 transactions; running balance recomputes 1,246,642 → **1,219,776** | 1–30 Sep 2025; "PAYROLL NORTHBROOK TRADING" only; no account name or currency | Yes | Yes — Step 1 opening cash; Step 3 recurring rhythm (rent, payroll, loan) | **Accepted with a limit**: one account only; company/currency user-asserted |
| `ar_aging_detail_2025-09-30.csv` | Open A/R by invoice: 13 invoices + credit memo CM-0312; net **798,360** | As at 30 Sep 2025; no company/currency | Yes; "amount" taken as open balance | Yes — Step 2 | **Accepted with a limit**: no payment history, so timing is assumed |
| `open_bills_2025-09-30.csv` | Open A/P: 12 bills, **255,264**, all due 3–25 Oct | As at 30 Sep 2025 | Yes; contains a probable duplicate (below) | Yes — Step 3 | **Accepted with a limit** |
| `payroll_register_2025-09.csv` | One payroll run, 12 employees: gross 70,599, net **53,902**; each net = gross − withholdings | Sep 2025 (file name only; no pay date or period column) | Yes | Yes — Step 3 payroll | **Accepted with a limit**: pay date and frequency inferred from the statement; employer taxes absent |
| `term_loan_agreement_summary.md` | Summary of a term loan: Calder Bank, 5,000/month + interest at 5.7%, covenants | Undated summary | Yes, as a summary | Yes — Step 3 debt service; Step 5 covenants | **Accepted with a limit**: summary, not the agreement; figures user-supplied |
| `ar_aging_detail_2025-09-30_final.csv` | **Not an aging.** A staff shift rota: E08–E10, week_1–week_4, "nights/days/off" | No company, dates or amounts | No | No | **Rejected** on content; I use `ar_aging_detail_2025-09-30.csv` |

Still missing: payroll tax and 401(k) remittance dates and employer taxes (required for payroll); tax payment dates (sales tax, income tax); expected new sales and new purchases; any credit facility; whether other bank accounts exist; 12 months of cash history to check annual payments.

*I would stop here and wait. Assumed answer: "go ahead with the accepted files".*

## (c) Findings

### 13-week forecast (USD)

| Wk | Dates | Opening | Receipts | Disbursements | Net | Closing | Headroom over 250,000 |
|---|---|---:|---:|---:|---:|---:|---:|
| 1 | 1–7 Oct | 1,219,776 | 24,015 | 160,199 | (136,184) | **1,083,592** | 833,592 |
| 2 | 8–14 Oct | 1,083,592 | 558,036 | 83,745 | 474,291 | 1,557,883 | 1,307,883 |
| 3 | 15–21 Oct | 1,557,883 | 64,041 | 55,779 | 8,262 | 1,566,145 | 1,316,145 |
| 4 | 22–28 Oct | 1,566,145 | 52,034 | 89,462 | (37,428) | 1,528,717 | 1,278,717 |
| 5 | 29 Oct–4 Nov | 1,528,717 | 0 | 16,747 | (16,747) | 1,511,970 | 1,261,970 |
| 6 | 5–11 Nov | 1,511,970 | 0 | 62,902 | (62,902) | 1,449,068 | 1,199,068 |
| 7 | 12–18 Nov | 1,449,068 | 0 | 16,697 | (16,697) | 1,432,371 | 1,182,371 |
| 8 | 19–25 Nov | 1,432,371 | 0 | 60,802 | (60,802) | 1,371,569 | 1,121,569 |
| 9 | 26 Nov–2 Dec | 1,371,569 | 0 | 16,747 | (16,747) | 1,354,822 | 1,104,822 |
| 10 | 3–9 Dec | 1,354,822 | 0 | 62,902 | (62,902) | 1,291,920 | 1,041,920 |
| 11 | 10–16 Dec | 1,291,920 | 0 | 16,697 | (16,697) | 1,275,223 | 1,025,223 |
| 12 | 17–23 Dec | 1,275,223 | 0 | 60,802 | (60,802) | 1,214,421 | 964,421 |
| 13 | 24–30 Dec | 1,214,421 | 0 | 16,697 | (16,697) | **1,197,724** | 947,724 |
| | **Total** | | **698,126** | **720,178** | (22,052) | | |

Chain ties: each closing is the next opening. Receipts: A/R current at due date 428,103; A/R overdue ≤45 days in week 2 (Pennine 112,071, Ridgeway 72,046, Ashby 56,036, Calder 32,020 less credit CM-0312 2,150 = 29,870) 270,023. Disbursements: bills 248,784; payroll net 6 × 53,902 = 323,412; withholdings and 401(k) 6 × 16,697 = 100,182 (assumed remitted the week after each payroll); rent 3 × 9,000; term loan 3 × 6,900; bank fees 100.

### Liquidity

- **Lowest point: week 1, 1,083,592** (Kestrel 88,583 and Orchard 41,687 fall due before most collections). Headroom 833,592. **No week breaches the 250,000 floor.**
- **Even with zero collections**, cash ends week 13 at 499,598; the average weekly outflow of 55,398 would reach the floor after about **17.5 weeks**.
- After week 4 there are no receipts, because **no new sales were supplied**. The outflows after week 4 also exclude new purchases. Both understate activity; the shape after week 4 is not a trend.

### Flags

1. **Probable duplicate bill — 6,480.** Kestrel Supplies INV-4471 (5 Oct) and "Kestrel Supplies Inc." INV4471 (6 Oct): same vendor, same number apart from the hyphen, same amount. Forecast once; please confirm before paying. If both were paid, week 1 low falls to 1,077,112.
2. **At-risk receivables excluded — 100,234**: Harlow INV-20418 48,200 (95 days overdue), Tideswell 48,031 (67), Foxhall 4,003 (130). Upside if collected.
3. **Concentration**: Harlow is 248,157 (31% of A/R); INV-20977 199,957 is the largest single receipt (week 2). If it slips 2 weeks, the low point is unchanged.
4. **Payroll mismatch**: the register's net pay 53,902 exceeds each September payroll on the statement (52,310) by 1,592. I forecast the higher figure.
5. **Statutory remittances not seen**: withholdings 13,873 and 401(k) 2,824 per run, yet no tax or 401(k) remittance appears on the September statement; employer social-security share not supplied. Timing here is my assumption.
6. **Term loan**: forecast at September's 6,900 on the 22nd (5,000 principal + about 1,900 interest). The Q3 compliance certificate (leverage ≤ 2.50×, interest cover ≥ 4.0×) is due **14 Nov 2025**, inside the horizon; it cannot be tested from these files (no EBITDA, no card balance).
7. **Unknown ACH debit 1,240 (24 Sep)** on the statement: not forecast to recur; identify it.

### Sensitivities and levers

All A/R slips 2 weeks: the low moves to week 3 at 944,068, still 694,068 above the floor. Largest receipt fails: closing week 13 is 997,767. Levers if needed (proposals, never payroll or remittances): pay Kestrel 4502 on its due date not earlier; chase Pennine 112,071 and Ridgeway 72,046 now.

## (d) What was not done, and why

| Step | Status | Gap |
|---|---|---|
| 1 Grid, opening cash | done with a limit | One account; restriction unconfirmed |
| 2 Receipts | done with a limit | Days-to-pay assumed, not derived (needs invoice and payment history); no new sales |
| 3 Disbursements | done with a limit | Tax, employer payroll taxes, new purchases, capex not supplied; no prior-year cash to find annual items |
| 4–5 Chain, liquidity | done | Floor is a management figure |
| 6 Sensitivities | done | |
| 7 Forecast vs actual | not done | First run; no prior forecast |
| 8 Workbook | not created | Would you like `13Week_Cash_Forecast_2025-10-01.xlsx` with live formulas? Only on a yes |
| 9 Save preferences | not offered yet | After your review |

**Coverage (manual run).** Environment: Northbrook Trading Ltd, USD, user-asserted; data source upload; verdicts as in (b). Capability map: not applicable, no connection; every line `[manual]`. **Manual lines that could breach a floor:** payroll (amount from register, dates inferred), remittances (timing assumed), debt service (from one statement line and the summary), taxes (absent), facility (none supplied).

**Data sources:** user uploads only — `bank_statement_2025-09.csv`, `ar_aging_detail_2025-09-30.csv`, `open_bills_2025-09-30.csv`, `payroll_register_2025-09.csv`, `term_loan_agreement_summary.md`.
