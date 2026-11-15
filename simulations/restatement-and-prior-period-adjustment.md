# Prior-period error assessment — Northbrook Trading Ltd, 2024 revenue cut-off

Mosofin is not connected, so this run is manual: every step is `[manual]`, from your uploads. (Connecting Mosofin would sweep the ledger for postings into closed periods automatically — docs.mosofin.com.) **PROPOSED — NOT POSTED — AUDITOR INVOLVEMENT REQUIRED.** Nothing is concluded on materiality or method here.

## 1. Read-back

Assessing an error in **revenue cut-off** at **Northbrook Trading Ltd** (user-asserted), **USD**, found in **the Q3 2025 close**, affecting **2024 (issued 18 March 2025)** and 2025, under **ASC 250**, a **private** company, against the auditors' benchmark **5% of pre-tax income**. These facts were **found in `issued_statements_2024_extract.md`** and are used once you confirm them here.

| Intake | Treatment |
|---|---|
| E — what was known at the time | **Not answered.** Both treatments are set out; neither is decided. (A cut-off mistake on known dispatch dates usually reads as an error, but that is your and your auditors' call) |
| Per-share amounts | Not needed if no EPS is reported (private); share counts not supplied |
| Tax rate | **Not supplied** — tax effects shown gross, not computed |

## 2. Validation of the upload — shown before any work

| File | What it actually is | Company / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `issued_statements_2024_extract.md` | A **summary extract** of the issued 2024 statements: revenue 4,731,300, net income 331,596, issue date 18 Mar 2025; the error description; framework, entity type, materiality basis | No company named; FY 2024 | Partly: no balance sheet, **no pre-tax income**, no tax charge | Yes — the issued baseline (Steps 0, 2, 3) | **Accepted with a limit**: a summary, not the issued statements; every figure **user-supplied, not evidenced** |
| `trial_balance_2024-12-31.csv` | Trial balance at 31 Dec 2024, 33 accounts, **foots (6,433,544 both sides)**; pre-closing (P&L accounts open); no tax accounts | No company; date of extraction unknown | Yes | Yes — Step 0 books-vs-issued comparison; balance-sheet lines | **Accepted with a limit**: the ledger's current view, not the issued figures |
| `journal_entries_2025-09.csv` | Journal entries for September 2025: 7 entries, with entry date, **posted-on date** and user | Sep 2025 (one entry dated August) | Yes | Yes — Step 0 sweep, Step 7 control evidence | **Accepted with a limit**: one month only, so the sweep for postings into 2024 after issue covers September only |
| `issued_statements_2024_extract_final.csv` | **Not financial statements.** A staff shift rota: E08–E10, week_1…week_4, "nights / days / off" | No company, periods or figures | No | No step uses it | **Rejected** on content despite its name. Not used |

**Still missing (required):** the **issued 2024 statements** themselves (with pre-tax income, tax and balance sheet); **ledger detail** for revenue, receivables, inventory and cost of sales Dec 2024–Jan 2025 and the invoice / dispatch records; the **tax rate**. Recommended: 2025 year-to-date benchmarks (for the Little r test); the term-loan covenant definitions.

*I would stop here and wait for your answer. Assumed answer: "go ahead with the accepted files".*

## 3. Findings

### Step 0 — do the books still agree with what was issued?

**No — the 2024 trial balance does not agree with the issued extract.** TB revenue **4,597,600** vs issued **4,731,300**: **133,700 lower**. TB pre-tax result (no tax accounts) **614,939** vs issued net income 331,596. The revenue gap is **not** the 86,000 cut-off error. Either the ledger has moved since issue (a correction never assessed), or the TB is a different version. **Unexplained — this is the first question for the ledger.**

Sweep of the September 2025 journal (postings into earlier periods and unusual items) — observations, not allegations:

| Entry | Dated | Posted | By | Detail | Group |
|---|---|---|---|---|---|
| JE-0901/02/03/06/07 | 30 Sep | 1–3 Oct | s.patel | Month-end close entries | Ordinary close cycle — excluded |
| **JE-0905** | **31 Aug** | **22 Sep** | s.patel | Legal fee 3,800 "missed in August", into a closed month | Posting into a prior (monthly) period — small |
| **JE-0904** | 28 Sep | 28 Sep | **a.reyes** | Dr AR / Cr Revenue **50,000**, "Revenue adjustment", round sum, no support named | Manual revenue entry by a senior user — ask for support; not a cut-off finding |
| **JE-0907** | 30 Sep | 3 Oct | s.patel | Marketing accrual **9,999**, **no memo** | Unsupported accrual — ask |

No September entry posts into 2024. The full 2025 ledger is needed to sweep for postings into 2024 after 18 March 2025.

### Step 1 — error or change in estimate: **for you to determine**

Revenue 86,000 (cost 49,900) for goods **dispatched 2 January 2025** was recognised on **30 December 2024**. If the dispatch date and the terms were known at the time, this is an **error** (retrospective); a change in estimate does not fit a cut-off on known dates, but the determination and its documented basis are yours and your auditors'.

### Step 2 — quantification (pre-tax; tax rate not supplied)

| Line | 2024 as issued | Error | 2024 corrected | 2025 effect (counterbalancing) |
|---|---:|---:|---:|---:|
| Revenue | 4,731,300 | **(86,000)** overstated | **4,645,300** | +86,000 belongs in 2025 |
| Cost of goods sold | n/s | (49,900) overstated | — | +49,900 belongs in 2025 |
| **Pre-tax income** | n/s | **(36,100) overstated** | — | +36,100 understated in 2025 |
| A/R at 31 Dec 2024 | — | 86,000 overstated | — | Self-corrects on collection |
| Inventory at 31 Dec 2024 | — | 49,900 understated | — | Self-corrects on dispatch |

- **Rollover:** 2024 income overstated **36,100** pre-tax; 2025 income understated **36,100** unless corrected.
- **Iron curtain:** at 31 Dec 2024, retained earnings overstated **36,100** pre-tax (A/R +86,000, inventory −49,900); at 30 Sep 2025 the balance-sheet error has **reversed to nil** (goods dispatched, invoice in A/R from 2024).
- Tax effect: 36,100 × your rate — not computed.

### Step 3 — materiality indicators (Conclusion column blank: management / auditors)

| Benchmark | Figure | Error | Ratio |
|---|---:|---:|---:|
| Revenue 2024 (issued) | 4,731,300 | 86,000 | 1.8% |
| Net income 2024 (issued, after tax) | 331,596 | 36,100 pre-tax | 10.9% |
| Auditors' threshold, 5% of pre-tax income | **pre-tax income not supplied** | 36,100 | — |
| Equity per TB incl. 2024 result (pre-tax) | 1,628,654 | 36,100 | 2.2% |

The auditors' benchmark cannot be applied: pre-tax income is not in the extract. As an indicator only: pre-tax income is at least net income 331,596, and the error would fall below 5% only if pre-tax income exceeded **722,000** (36,100 / 5%), i.e. an effective tax rate above about 54%. Qualitative: no loss-to-profit swing (331,596 profit either way); a **term loan of 265,000** exists, so covenant effects need the definitions; trend and compensation effects not assessable; no indication of fraud in the error itself.

### Step 4 — correction method: the paths, not the choice

| Path | What it means here |
|---|---|
| **Restatement of 2024 comparatives** (Big R or Little r) | Restate 2024 revenue to 4,645,300 and COGS down 49,900; 2025 recognises the 86,000 sale. Proposed 2025 entry, **not posted**: Dr 3100 Retained Earnings 36,100 (less tax) / Dr 5000 COGS 49,900 / Cr 4000 Sales Revenue 86,000, plus tax |
| **Out-of-period, no restatement** | 2024 left as issued; the error has already reversed on the balance sheet, so 2025 income stays understated by 36,100; disclosure considered |

Little r test: needs 2025 benchmarks (not supplied). Aggregation: assess with the unexplained 133,700 revenue gap once explained.

## 4. What was not done, and why

| Item | Status | Needed |
|---|---|---|
| Error vs estimate; materiality conclusion; method choice | **Not done — yours and your auditors'** | — |
| Applying the 5% pre-tax benchmark | Blocked | Pre-tax income 2024 |
| Tax effect; amended return | Not computed | Tax rate, return position |
| Sweep of all 2025 postings into 2024; 133,700 gap | Not done | Full 2025 ledger; issued statements |
| Covenants; Little r test | Not done | Loan agreement; 2025 benchmarks |
| Root cause, control assessment, governance | **Not done** | People; auditor |
| Posting, restating, re-issuing | **Not done — read-only** | A person, with the auditor |

## 5. Coverage and provenance (manual run)

- **A — Environment:** Northbrook Trading Ltd, entity level, ASC 250, private, USD — user-asserted; source **upload**; **issued figures from `issued_statements_2024_extract.md` (summary), not the ledger**. Files: extract, TB, September JEs *accepted with a limit*; `issued_statements_2024_extract_final.csv` *rejected (shift rota)*.
- **B — Capability map:** not applicable — no connection; every task is `[manual]`.
- **C — Steps:** Step 0 — done with a limit (September only; TB disagrees with issued); **Step 1 — human, not done**; Step 2 — done pre-tax; **Step 3 — indicators only, conclusion blank**; Step 4 — both paths modelled; Step 5 — entry proposed; Steps 6–7 — not done.
- **E — Unknowns:** 133,700 revenue gap; JE-0904 support; JE-0907 support; tax rate; pre-tax income.
- **F — Parameters:** auditors' 5% of pre-tax income (supplied, not applied); rollover and iron curtain both shown; issued baseline dated 18 Mar 2025.

Would you like this as `Restatement_2024_Northbrook_Trading_Ltd.xlsx`? Only on your yes.
