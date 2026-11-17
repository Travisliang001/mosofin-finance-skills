# Quarter-end close — Northbrook Trading Ltd, Q3 2025 (July–September) (upload path)

Mosofin is not connected, so this run is manual: every figure comes from the files you uploaded, and every step is `[manual]`. Connecting Mosofin would read all three months, the posting dates and the prior quarters automatically ([docs.mosofin.com](https://docs.mosofin.com)). Nothing was posted, signed or filed. The certificate figures below are a draft for a person to check and sign.

## Read-back

Running the **Q3 2025** close for **Northbrook Trading Ltd** (user-asserted), **1 July – 30 September 2025**, **USD**, **US GAAP**, calendar year (the audit covers the year to 31 Dec 2025, so this is not Q4 and `year-end-close` does not apply). From your audit inputs (please confirm): due this quarter, the **board pack** and the **lender compliance certificate** (due 45 days after quarter end: **14 Nov 2025**); **no interim review**, so the reviewer steps are skipped. Covenant definitions are taken from your term-loan summary. **Materiality: none given, and none supplied.** Events: acquisition of **Harlow Fabrication on 1 July**; restructuring approved in **October**. Segments: no dimension supplied, treated as none.

## Validation of the upload (shown before any work)

| File | What it actually is | Company / period | Usable? | Used by | Verdict |
|---|---|---|---|---|---|
| `trial_balance_2025-09-30.csv` | TB, 33 accounts, debits = credits = 6,546,018; term loan 220,000 | 30 Sep 2025 per name and content; company not named | Yes | Steps 2, 5, 6 | **Accepted with a limit**: company user-asserted |
| `trial_balance_2025-08-31.csv` | TB, 33 accounts, foots at 6,106,903 | 31 Aug 2025 | Yes, for September movements only | Steps 1, 5 | **Accepted with a limit**: the prior *month*, not the prior quarter end (30 Jun) or year end (31 Dec 2024) |
| `journal_entries_2025-09.csv` | 7 journals (16 lines) with entry and posting dates and users | Dated 31 Aug–30 Sep, posted 22 Sep–3 Oct 2025 | Yes; each journal balances | Steps 1, 5 (late postings, cut-off) | **Accepted with a limit**: a selection of journals, not the full GL for the quarter |
| `term_loan_agreement_summary.md` | Summary of term-loan terms and covenant definitions | Current | Yes | Step 2 covenants, Step 3 certificate | **Accepted with a limit**: a summary, not the agreement |
| `audit_inputs.md` | Engagement facts, owners, Q3 obligations, 2025 events | Year 2025 | Yes | Intake C, E, F; Step 2 | **Accepted with a limit**: user-supplied facts |
| `trial_balance_september.csv` | A TB, foots at 5,363,915, but **not September 2025**: term loan **280,000** (57 repayments of 5,000 from 565,000 → **30 Sep 2024**), retained earnings 763,715, dividends nil | Content points to 30 Sep **2024** | Not as named | No step | **Rejected** on content: it is not the September 2025 TB the name suggests. If it is the 30 Sep 2024 comparative, say so and it can support the prior-year variance |

**Still missing:** TB at **30 Jun 2025** (required: Q3 activity and the reopened-period test); TB at **31 Dec 2024** (required: year-to-date roll-forward and trailing-twelve-month covenants); full GL detail for Jul–Sep (required for cut-off and late postings); lease schedule (Total Debt includes leases); the TB extraction date (see finding 6).

*Here I would stop and wait for your answer. Assumed answer: "go ahead with the accepted files".*

## Findings — ordered by consequence

**1. Covenants: compliance cannot be certified on trailing twelve months yet, but a breach is implausible.** TTM needs Q4 2024, which is missing. Book components (labelled as inputs, definition source: loan summary):

| Component, YTD to 30 Sep 2025 | Amount | Source |
|---|---:|---|
| Net income (TB, no tax charged) | 594,241 | ledger |
| + Interest 7000 | 10,474 | ledger; agrees to the agreement's 5.7% on the amortising balance (10,473.75) |
| + Depreciation 6600 | 37,800 | ledger |
| + One-time legal fee, June (≤15,000 cap) | 14,000 | agreement / CFO |
| **Covenant EBITDA, 9 months** | **656,515** | |
| Total Debt: term loan 220,000 + card 7,300 + leases (none on TB) | **227,300** | ledger |

Leverage ≤ 2.50x needs TTM EBITDA ≥ 90,920; interest cover ≥ 4.0x needs ≥ 57,571 (using Q4 2024 interest of 3,919 per the agreement's schedule). **Both pass unless Q4 2024 covenant EBITDA was a loss of more than about 566,000.** Two caveats for the certificate: **no lease liability is on the TB although rent runs at 9,000 a month**, so Total Debt may be understated; and the August legal fee (JE-0905, 3,800) would exceed the 15,000 add-back cap by 2,800 if also treated as one-time. **Certificate due 14 Nov 2025; drafted, not signed.**

**2. No tax charge has been booked in 2025.** The TB has no income tax expense or payable. YTD pretax income is **594,241**. The interim provision needs the estimated annual effective tax rate (EAETR), which only management can set: owner, controller.

**3. Manual revenue journal JE-0904: 50,000**, DR receivables / CR revenue, "Revenue adjustment", 28 Sep, by a.reyes (not the controller), no invoice reference. Revenue posted by journal two days before quarter end is a cut-off question: support needed before the board pack.

**4. The Harlow Fabrication acquisition (1 July) is not in the books.** No investment, goodwill or new accounts appear on the 30 Sep TB. Either it is accounted for elsewhere or not at all: a material mid-quarter event needing purchase accounting and disclosure. Hand off to business-combination accounting.

**5. Balances unchanged for twelve months** (30 Sep 2024 file set aside, so shown here only from Aug vs Sep 2025 plus the account behaviour): allowance for doubtful accounts **9,000** on receivables of 831,430 then 798,360 (1.08% → 1.13%) — not moved with the book; prepaid expenses **18,000** unchanged although JE-0902 releases 3,000; payroll clearing 1,200 and payroll tax 5,400 unchanged. A balance that does not move is not being reviewed.

**6. The 30 Sep TB does not reflect all September journals.** JE-0902 credits prepaid 3,000, yet 1300 stays 18,000; JE-0903 accrues 8,400 wages, yet 6000 rose by exactly 76,000 (the payroll alone); 2100 rose by only 200 against 19,468 of September-dated credits. Depreciation (4,200) and interest (1,069) are in. **Please confirm when the TB was extracted**: entries posted 1–3 Oct may be missing.

**7. Late and unusual postings.**
- JE-0905, legal fee 3,800, **dated 31 Aug, posted 22 Sep** — posted into August after it closed; the August TB as reported may differ from today's.
- JE-0907, **9,999** to marketing / accrued liabilities, **no memo**, posted 3 Oct — just under 10,000; needs support.
- JE-0901, 0902, 0903, 0906 dated 30 Sep, posted 1–3 Oct: normal period-end accruals.

**8. Dividends and adjustments 67,500 vs the 60,000 dividend declared in March**: 7,500 unexplained.

**9. Subsequent events:** restructuring approved in October — from management, not the ledger; likely a non-recognised (Type 2) event to disclose if material. Ledger sweep after 30 Sep not possible: no post-quarter GL.

## Quarter-specific tasks (all eleven groups kept, with owners)

| Group | Status | Owner |
|---|---|---|
| Tax provision (EAETR) | Not booked; rate needed | Controller |
| Revenue / KPIs | YTD revenue 4,038,600; concentration needs customer detail | Controller |
| Covenants | Drafted above; TTM pending Q4 2024 | Controller, CFO signs |
| Re-forecast | Management's | CFO |
| Variance (QTD / prior year) | Blocked: no 30 Jun or prior-year TB | Controller |
| Subsequent events | Restructuring logged; sweep not possible | Controller |
| Going concern facts | Cash 1,002,979; debt 227,300 (maturity 31 May 2029); assessment is management's | CFO |
| Estimates | Allowance unchanged; restructuring may need a provision in Q4 | Controller |
| Stock compensation | None on TB; confirm none | Controller |
| Segments | None tracked | — |
| Disclosure controls | Prior-year point: bank recs not reviewed monthly — re-test | Controller |

## Not done, and why

- Q3 activity, YTD roll-forwards, reopened-period test: no 30 Jun 2025 or 31 Dec 2024 TB.
- Cash to bank statement (Step 6): no statements.
- Monthly close of July and August: only August's closing TB.
- Workbook `QuarterEndClose_2025-Q3_Northbrook Trading Ltd.xlsx`: not created. Would you like it?

## Coverage sheet (manual run)

**Environment:** Northbrook Trading Ltd, Q3 2025, USD, US GAAP — user-asserted; fiscal year end assumed 31 Dec from the audit scope. Data source: upload (Mosofin gateway absent). Five files accepted with limits; `trial_balance_september.csv` rejected (30 Sep 2024 content).
**Capability map:** Not applicable: no connection. Every task is `[manual]`.

| Step | Status |
|---|---|
| 1 Monthly close (all three months) | Done with a limit: September only; TB / journal mismatch |
| 2 Quarter tasks | Done with a limit: all 11 listed with owners |
| 3 Reports | Certificate drafted, board pack figures partial |
| 4 Reviewer | Not applicable: no interim review |
| 5 YTD roll-forward, reopened period | Not done: no 30 Jun / 31 Dec TBs |
| 6 Cumulative validation | Not done: bank leg and roll-forward inputs missing |
| 7 Output | Tables in chat |

**Data sources:** upload — trial_balance_2025-09-30.csv, trial_balance_2025-08-31.csv, journal_entries_2025-09.csv, term_loan_agreement_summary.md, audit_inputs.md.
