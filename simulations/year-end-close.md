# Year-end close — Northbrook Trading Ltd, year ended 31 December 2024, USD (upload path)

Mosofin is not connected, so this run is manual and works only from the files you uploaded. Nothing was posted or locked; the closing entries below are **proposals**. No materiality was supplied by me, and no going-concern conclusion is drawn.

## Read-back

Running the year-end close for **Northbrook Trading Ltd** at **31 December 2024**, in **USD**, from **your uploaded trial balances, fixed asset register and a September journal listing**. Company, year-end and currency are user-asserted. **Framework (B) not given** — I do not infer it; framework-dependent items are shown conditionally. **One file describes a different year (see validation)**, so audit type (C), filings (D), events (E) and prior findings (F) are, for FY2024, unanswered: audit steps skipped, common filings listed as questions, events asked again, nothing carried forward and **no materiality**.

## Validation of the upload — shown before any work

| File | What it actually is | Company / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `trial_balance_2024-12-31.csv` | Year-end TB, 33 accounts, full-year P&L | 31 Dec 2024; no company/currency | Yes: debits 6,433,544 = credits | Yes: Steps 2, 5, lead schedules | **Accepted with a limit**: company user-asserted |
| `trial_balance_september.csv` | Interim TB, 33 accounts, 9-month P&L. **The file gives no year**; content shows **30 Sep 2024**: retained earnings 763,715 = the 2024 opening in the December TB, accumulated depreciation 12,600 (3 × 4,200) below December | 30 Sep 2024 (inferred) | Yes: debits 5,363,915 = credits | Yes: Q4 test in Step 1b | **Accepted with a limit**: year inferred from content; supports a Q4 check only, not a month-by-month one |
| `fixed_asset_register.csv` | Register of 8 assets: cost, in-service date, life | No as-at date; FA-008 labelled "sold Jul 2025" | Yes; cost total 420,000 = TB. No accumulated depreciation, method or salvage | Yes: fixed assets year-end block | **Accepted with a limit**: depreciation recomputed on an assumed method |
| `journal_entries_2025-09.csv` | 7 journals (16 lines), all balanced, dated 31 Aug – 30 Sep 2025 | **September 2025 — the year after this year-end** | Yes | Partly: new-year detail for the lock and opening tests (Steps 5b–5c), one month only | **Accepted with a limit**: covers one month of 2025, not the new year to date |
| `audit_inputs.md` | Audit and year-end facts: **"full audit of the year to 31 December 2025"**, fieldwork 9 Feb 2026, 2025 events, owners, filings, prior-year point | **Names FY2025, not FY2024** | Readable | Would answer C–F | **Rejected for this run**: it names a different year. Is the year-end you want **31 December 2025**? If so, I will correct the read-back and re-validate |

Still missing (required): **trial balance at 31 Dec 2023** (prior year end); **general ledger detail for 2024** and for 2025 to date. Recommended: depreciation method and salvage; lease schedule; the framework; materiality.

*I would stop here and wait. Assumed answer: "go ahead with the accepted files".*

## Findings — FY2024

**1. The year's arithmetic, and proposed closing entries (Step 5).** Net income 2024 = revenue 4,597,600 − costs 3,982,661 = **614,939**. Proposed: close revenue (Dr 4,597,600) and every expense account to retained earnings; dividends account is nil. **Retained earnings: 763,715 + 614,939 − 0 = 1,378,654** closing — the figure the 2025 opening must show (Step 5c). No 2025 opening TB was uploaded, so the opening test **did not run**.

**2. Twelve months closed? (Step 1b) — Q4 only.** December less September: depreciation 12,600 = 3 × 4,200; rent 27,000 = 3 × 9,000; software 10,500, insurance 4,500, repairs 1,500, professional fees 7,500 — each exactly three months of the run-rate. **Q4 recurring entries ran.** January–September cannot be tested month by month without the GL.

**3. Fixed assets: the register does not support the ledger.** Register cost 420,000 = TB. But straight-line from in-service month, no salvage (my assumption — please confirm the method): **2024 depreciation 58,431 vs 50,400 booked; accumulated at 31 Dec 2024 211,741 vs 273,400 in the TB (difference 61,659).** The ledger charges a **flat 4,200 every month**, although FA-008 (12,000, 5 years from May 2019) became fully depreciated in April 2024 and FA-005 runs out in January 2025 — the signature of a hard-coded recurring entry. Register-based monthly charge at Dec 2024: 4,803. FA-008 "sold Jul 2025" is still on the register: a 2025 disposal to record.

**4. Estimates — fresh look needed.** Allowance for doubtful accounts **9,000, unchanged** from September to December against AR of 602,143 (1.5%). No inventory reserve against inventory of 495,154. Both need a fresh look; the judgment is yours.

**5. Items the books show traces of — for you to answer.**
- **No income-tax expense or payable** on a pre-tax profit of 614,939: the tax provision workpaper cannot start.
- **Rent 108,000 with no right-of-use asset or lease liability**: under US GAAP (ASC 842) or IFRS 16 this is the unrecognised-lease signature. Framework needed.
- **Investment in Northbrook UK Ltd 104,800 and intercompany payable 38,000**: a subsidiary exists; are consolidated statements required?
- **Stripe clearing 6,420** identical in September and December: not clearing.

**6. Going-concern facts only (no conclusion).** Cash 804,366 (+6,420 clearing); current assets 1,917,083 vs current liabilities 274,829 excluding any current portion of the term loan (265,000; maturity not in the books); profitable year. Management assesses.

**7. Lock test (Step 5b) on the file supplied.** No entry in `journal_entries_2025-09.csv` is dated in 2024, so this file shows **no posting into the closed year** — one month of 2025 only, so this is not evidence the lock held. Observations in that month, for the 2025 close: **JE-0904 revenue adjustment 50,000 (Dr AR / Cr revenue), dated 28 Sep, the only entry by a.reyes**, memo "Revenue adjustment"; **JE-0905 3,800 dated 31 Aug, posted 22 Sep** into a closed month; **JE-0907 9,999 to marketing / accrued, no memo**.

**If the year-end is 31 December 2025 instead:** the year has not closed (figures to September 2025); `audit_inputs.md` would be accepted (full audit, fieldwork 9 Feb 2026, dividend 60,000, Harlow acquisition 1 Jul, restructuring Oct); `trial_balance_september.csv` would be **rejected as the wrong year** (it is September 2024); and finding 7's three entries become current-year review items.

## What was not done, and why

- Audit steps (PBC, lead schedules, confirmations, rep letter): audit type unanswered for FY2024 — skipped.
- Filings: not answered; to ask — corporate income tax return(s), 1099 information returns, payroll year-end forms, sales-tax annual reconciliation, any statutory accounts.
- Prior-year comparative test and Jan–Sep month checks: need the 2023 TB and the 2024 GL.
- Counts, confirmations, valuations, payroll register, deferred tax attributes, debt maturities: outside the files.
- No Excel file created; I would ask before making `YearEndClose_2024-12-31_Northbrook-Trading-Ltd.xlsx`.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, FY ended 31 Dec 2024, USD — user-asserted; entity basis (single TB); framework, audit type, materiality not given. Source: upload; four files accepted with limits, `audit_inputs.md` rejected (FY2025). Months verified: Q4 only. Lock date unknown |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 1 standard close: not run (no monthly data). 1b: Q4 done, Jan–Sep **not done**. 2 (15 blocks): audit prep skipped; tax provision blocked (no tax line); statutory returns listed as questions; payroll, impairment, consolidation, revenue, restatement **not done**; estimates done with a limit; fixed assets done (register ≠ ledger); leases flagged; going concern facts only; cash flow, disclosures, equity roll not done (no prior-year TB). 3–4 filings/audit: not done. 5 closing entries: drafted. 5b: done with a limit. 5c: **not done**. 6–7: chat only |
| Not done | Prior-year comparatives (needs 31 Dec 2023 TB); twelve-month check (needs GL); opening balance test (needs 1 Jan 2025 TB) |
| Unknowns carried forward | Framework; year in scope; depreciation difference 61,659; tax; leases; consolidation; allowance; Stripe clearing |
| Parameters | Depreciation recomputed straight-line from in-service month, no salvage (assumed); no materiality applied |
