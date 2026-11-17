# Notes to the financial statements — Northbrook Trading Ltd, 30 September 2025 (upload path) — DRAFT

Mosofin is not used for this run (you chose upload only), so every note is `[manual]`, built from your files. Nothing was written anywhere. **DRAFT — items needing management or legal input are flagged in place; no contingency wording is drafted.**

## Read-back

Drafting the notes for **Northbrook Trading Ltd** (user-asserted) as at **30 September 2025** (nine months), a **private** company under **US GAAP**, in **USD**, from **your uploads**, to be issued on **20 March 2026**. Policies as in **`accounting_policies.md`**; legal review of contingencies by **Greyfriars Legal LLP**. Framework, private status, issue date and legal reviewer were read from your policies file — I am treating them as your intake answers; please confirm.

| Open point | What I applied |
|---|---|
| Issue date 20 March 2026 vs a 30 Sep 2025 period | An issue date six months after a quarter-end reads like the **FY2025 annual** accounts. Please confirm the period. Subsequent-events window taken as 1 Oct 2025 – 20 Mar 2026 |
| Significant judgments and estimates (D) | Not supplied → structure only, marked for confirmation |
| Related-party list (E) | Not supplied → candidates from the books only; nothing drafted on relationships |
| Lease and fixed-asset schedules (F) | Not supplied → those notes from balances only |

## Validation of the upload — shown before any work

| File | What it actually is | Company / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `trial_balance_2025-09-30.csv` | TB, 33 accounts, YTD P&L | No company/date in file | Foots: 6,546,018 | Yes — every detail note, tie-out | **Accepted with a limit: company and period user-asserted** |
| `trial_balance_2024-12-31.csv` | TB, 33 accounts, pre-closing (FY2024 P&L open) | No company/date in file | Foots: 6,433,544; RE 763,715 + FY2024 profit 614,939 = 1,378,654 = opening RE in the 2025 TB | Yes — comparatives, roll-forwards | **Accepted with a limit**: date from file name |
| `accounting_policies.md` | Policy list + framework, private status, issue date, legal reviewer | Northbrook implied; no date | Yes | Yes — Steps 2, 8 | **Accepted** (user-supplied) |
| `prior_year_notes_extract.md` | One-paragraph extract of the 2024 notes (notes 1, 4, 7, 9, 11) | 2024 accounts | Partly — figures disagree with the Dec 2024 TB (Finding 1) | Yes — comparatives, consistency | **Accepted with a limit**: an extract, not the issued notes |
| `term_loan_agreement_summary.md` | Summary of the Calder Bank loan terms and covenants | Northbrook implied | Yes | Yes — debt note | **Accepted with a limit**: a summary, not the agreement; every term labelled user-supplied |
| `trial_balance_september.csv` | A Northbrook TB, but **not at 30 September 2025**: term loan 280,000 (vs 220,000), retained earnings 763,715 (the Dec 2023 figure), YTD revenue 3,499,900 (vs 4,038,600) — consistent with **30 September 2024** | Wrong period for the name | Foots: 5,363,915 | Not as the current TB | **Rejected** as the September 2025 TB on content. If it is the 30 Sep 2024 TB and you want it as the nine-month comparative, say so and I will use it |

Still missing: **financial statements** for the period and comparative (required — I have TBs only); **debt maturity schedule** (the summary suffices for the arithmetic), **lease schedule** (required for the lease note), **fixed-asset register**; **full issued 2024 notes**; related-party list; post-period ledger activity for subsequent events.

*I would stop here and wait for your answer. Assumed answer: "go ahead with the accepted files".*

## Disclosure checklist (scoped from the TB)

| Note | Required? | Drafted? | Tied to data? | Needs input | Verdict |
|---|---|---|---|---|---|
| 1 Nature of business, basis (US GAAP, going concern) | Y | Structure | n/a | Business description | manual |
| 2 Significant policies: revenue, inventory, PP&E, receivables | Y | Yes, from your file | Partly tested (Finding 4) | Judgments/estimates; tax; leases | manual |
| 3 Receivables | Y | Yes | Ties | — | manual |
| 4 Inventory | Y | Yes | Ties | Categories | manual |
| 5 Property and equipment | Y | Yes | Ties to TB; **not** to prior-year note | Register | manual |
| 6 Leases (warehouse to 2028) | **Y** | **No** | **No ROU asset or lease liability in the TB** | Lease schedule | manual |
| 7 Term loan | Y | Yes | Ties | Agreement | manual |
| 8 Income taxes | Y | **No** | No tax accounts | Tax position | manual |
| 9 Equity | Y | Partly | Ties | Share data | manual |
| 10 Related parties | Y | Candidates only | Ties | RP list | manual |
| 11 Commitments and contingencies | Y | Lease commitment flagged; **contingency not drafted** | — | Greyfriars Legal LLP | manual |
| 12 Subsequent events | Y | No | No post-period data | Management | manual |
| Ruled out: goodwill/intangibles, stock comp, deferred revenue, FX hedging | N | — | No such balances | — | manual |

## Draft detail notes (USD; all figures tie to the TBs, difference 0)

**Receivables** — trade receivables 798,360 (31 Dec 2024: 602,143), less allowance 9,000 (9,000) = **789,360** (593,143).
**Inventory** — weighted average cost, lower of cost and NRV *(per your policy)*: **683,100** (495,154).
**Property and equipment** — straight line over 3–10 years *(per your policy)*. Cost 420,000 at both dates, no additions or disposals; accumulated depreciation 273,400 + charge 37,800 = 311,200; **net 108,800** (146,600).
**Term loan (Calder Bank)** — drawn 1 Jan 2020 565,000; fixed 5.7%; 5,000 a month plus interest; matures 31 May 2029. Balance **220,000** (265,000). **Current 60,000; non-current 160,000.** Maturities: Oct–Dec 2025 15,000; 2026 60,000; 2027 60,000; 2028 60,000; Jan–May 2029 25,000 (= 220,000). Interest recomputes: 9 months 2025 10,473.75 vs TB 10,474; FY2024 16,957.50 vs 16,957. Covenants (leverage ≤ 2.50x, interest cover ≥ 4.0x, quarterly on trailing twelve months) — **compliance not computed**: needs the trailing-twelve-month P&L to 30 Sep 2025.
**Equity** — share capital 250,000; retained earnings 1,378,654 at 1 Jan 2025; **dividends and adjustments 67,500** in 2025.

## Findings

1. **The prior-year notes do not match the 31 Dec 2024 books.** Note 4 accumulated depreciation **197,800 vs TB 273,400** (difference 75,600 = 18 months at 4,200). Note 7 term loan **445,000 vs TB 265,000** (difference 180,000); 445,000 is the balance at Dec 2021 (565,000 − 24 × 5,000). Either the extract carries stale figures or unposted adjustments exist — the comparatives cannot go out until resolved.
2. **No lease on the balance sheet.** The 2024 notes disclose a warehouse lease to 2028 and rent runs 9,000 a month, but there is no right-of-use asset or lease liability. ASC 842 applies to private companies; it also feeds the loan's Total Debt covenant definition. Needs the lease schedule.
3. **Contingency candidate — not drafted:** the June 2025 professional fees include a **one-time 14,000 legal fee for a contract dispute** (loan summary). Whether there is anything to accrue or disclose is for Greyfriars Legal LLP; I have written no wording.
4. **Policy consistency:** allowance "based on ageing", yet it is **9,000 at both dates** while receivables rose 32.6% (602,143 → 798,360) — the policy does not appear to have been applied. Depreciation: 50,400 a year on 420,000 cost implies an average 8.3-year life — inside "3 to 10 years". Inventory costing and revenue timing cannot be tested from a TB.
5. **Related-party candidates:** Northbrook UK Ltd — investment 104,800, intercompany payable 38,000. The 2024 note shows a **48,000 management fee from Northbrook UK**; the 2025 TB has no account where such income could sit. Dividends 67,500 paid in 2025 (recipients unknown).
6. **No income tax** in either TB for a Ltd company with nine-month profit of 594,241 (FY2024: 614,939). The tax note cannot be drafted.
7. **Subsequent events:** no post-period data supplied; candidates through 20 March 2026 must come from management (refinancing, dividends, the contract dispute).

## Not done, and why

Statement face tie (no statements uploaded; TB used); lease note (no schedule); tax note (no tax data); covenant compliance (no trailing-twelve-month P&L); subsequent events list (no post-period data); EPS (private). No file created — I would ask whether you want `Notes_to_FS_2025_Northbrook Trading Ltd` as `.xlsx` (checklist) and Word (notes).

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, 30 Sep 2025, USD, US GAAP private — user-asserted. Source: upload. 2025 and 2024 TBs, policies, prior-year extract, loan summary accepted (with limits); `trial_balance_september.csv` rejected (30 Sep 2024 content). |
| Capability map | Not applicable: no connection. Every task is `[manual]`. |
| Steps | 1 checklist done · 2 policies drafted from your file · 3 detail notes done with limit (TB, not statements) · 4 lease commitment flagged, contingency **not drafted** · 5 candidates only · 6 **not done** · 7–8 done (findings 1, 4) · 9 tables in chat. |
| Not done | Comparative vs issued 2024 notes (full notes); lease note (schedule); covenants (TTM P&L); subsequent events (post-period ledger). |

**Data sources:** user uploads — `trial_balance_2025-09-30.csv`, `trial_balance_2024-12-31.csv`, `accounting_policies.md`, `prior_year_notes_extract.md`, `term_loan_agreement_summary.md`.
