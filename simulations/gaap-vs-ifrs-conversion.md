# US GAAP to IFRS conversion — Northbrook Trading Ltd — 30 September 2025

Mosofin is not connected, so this run is manual: every figure comes from your uploads and every step is `[manual]`. (Connecting Mosofin would scope the conversion straight from your chart of accounts: [docs.mosofin.com](https://docs.mosofin.com).) Every adjustment below is a **proposal**; nothing is posted.

## Read-back

Converting **Northbrook Trading Ltd** from **US GAAP to IFRS** at **30 September 2025** (nine months), in **USD**, for **group reporting, ongoing each year**, from **your uploads** and **the policies you uploaded**: revenue on delivery, inventory at **weighted average cost**, fixed assets straight-line 3–10 years, receivables allowance by ageing. **No materiality supplied**, so every difference found is quantified. Shall I go ahead?

**Open intake points (unanswered, no default in the skill):** whether the group is adopting IFRS **for the first time** (if so IFRS 1 applies and a **transition date** is needed); the **tax rate** for deferred tax; and the IFRS standards in force at 30 September 2025, which you or your technical reviewer confirm — what follows describes them for review, not as settled.

## Validation of the uploads (shown before any work — I would wait for your answer here)

| File | What it actually is | Company / period | Usable? | Step that uses it | Verdict |
|---|---|---|---|---|---|
| `trial_balance_2025-09-30.csv` | Trial balance, 33 accounts, balance sheet and nine-month P&L | No entity or currency named; 30 Sep 2025 per name | Debits = credits = 6,546,018; nine-month profit 597,741 | Steps 1, 4, 6 | **Accepted with a limit:** company and currency user-asserted |
| `accounting_policies.md` | Policy summary, framework US GAAP, private company | Northbrook (implied), current | Readable; no lease or tax policy stated | Steps 2, 3 | **Accepted with a limit:** silent on leases, income tax, impairment and contingencies |
| `lease_terms.md` | Lease schedule: warehouse (5 years from 1 Jan 2024, 9,000 a month in advance, +3% each January, 3-year renewal at market) and printer (12 months from 1 Mar 2025, 180 a month); IBR 6.0% with source | Company's leases | A **summary of key terms**, not the agreements | Step 4 leases | **Accepted with a limit:** figures user-supplied, not evidenced by the lease agreements |
| `trial_balance_september.csv` | A trial balance — but **of a different period**: retained earnings 763,715 (the opening 2024 balance), term loan 280,000, accumulated depreciation 260,800, nine-month profit 485,722 | **30 September 2024**, not 2025 — the content says so, the name does not | Balances (5,363,915 each side) | None for a 30 Sep 2025 conversion | **Rejected:** wrong period. It could serve as an IFRS comparative only if you say so; upload it as such and I will use it for that |

**Still missing:** (1) whether this is first-time adoption, and the transition date; (2) the applicable income-tax rate (no tax accounts exist in the TB); (3) the lease agreements; (4) the legal letter on contingencies from Greyfriars Legal LLP; (5) the fixed-asset register (components, any impairment indicators); (6) the receivables ageing and loss rates.

*Proceeding as if you answered "go ahead with the accepted files".*

## Step 1 — Scoping: all ten areas

| Area | Live here? | Evidence | Policy supplied? | Result |
|---|---|---|---|---|
| Inventory | Yes | Inventory 683,100 | Weighted average, LCNRV | No method change (IFRS permits weighted average; no LIFO). Write-down reversal difference: no write-down on record |
| PP&E | Yes | Cost 420,000, acc. dep. 311,200 (net 108,800) | Straight-line 3–10 yrs | Cost model can continue; component review needs the register; revaluation is **your election**, not made here |
| Impairment | Low | No impairment charge; net long-lived assets 108,800 | No | No indicator in the TB; reversal rules differ, nothing to reverse |
| Development costs | Not evident | No R&D account; software 28,000 | No | Absence is a signal, not proof: confirm no development spend is in payroll or software |
| **Leases** | **Yes — finding** | **Rent 81,000 (9 × 9,000) and no right-of-use asset or lease liability** | Lease terms supplied | **Quantified below** |
| Financial instruments | Yes | Receivables 798,360, allowance 9,000 (1.13%); term loan 220,000; investment in subsidiary 104,800 at cost | Ageing allowance | Both frameworks use expected losses; difference not quantifiable without loss rates. Loan at amortised cost; no fees known |
| Revenue | Always | Revenue on delivery | Yes | Converged in principle; no application difference identified for point-of-delivery sales |
| Provisions / contingencies | Possible | Accrued liabilities 28,800; a lawyer named for contingencies | No | Recognition thresholds differ; needs the legal letter |
| Income taxes | **Gap** | **No current or deferred tax account at all** | No | Deferred tax on every adjustment cannot be quantified without a rate |
| Other (capitalised interest, pensions, share-based pay) | No | None in the TB | — | Ruled out on the TB |

No contradiction with the stated framework (no revaluation surplus, no LIFO reserve, no impairment reversal).

## Step 4 — Leases (the one quantified area)

**First, a finding against the source framework itself.** ASC 842 also requires operating leases on the balance sheet, so the warehouse lease should already carry a right-of-use asset and liability under US GAAP. In addition, the lease escalates 3% each January, so 2025 rent is **9,270 a month**, but the ledger shows **9,000 a month** (81,000 vs 83,430): **2,430 unrecorded**. Both are corrections to the US GAAP books, not conversion differences.

**Assumptions (yours to confirm):** renewal option **not** reasonably certain, so excluded; discount 6.0% applied monthly as 0.5%; payments in advance; full retrospective measurement from 1 January 2024. Printer lease: 12 months, so both frameworks allow a **short-term exemption** — that is your election; not decided, immaterial (1,260 in 2025).

| Warehouse lease | Amount |
|---|---|
| Contractual payments, 60 months | 573,386.64 |
| Liability and right-of-use asset at 1 Jan 2024 (PV at 6%) | 495,030.73 |
| Liability at 30 Sep 2025 | 347,450.60 |
| IFRS 16 right-of-use asset at 30 Sep 2025 (straight-line, 8,250.51 a month) | 321,769.97 |
| ASC 842 right-of-use asset at 30 Sep 2025 (straight-line cost 9,556.44 a month) | 338,195.28 |
| 2025 YTD cost — ASC 842 single straight-line cost | 86,008.00 |
| 2025 YTD cost — IFRS 16 depreciation 74,254.61 + interest 16,892.62 | 91,147.23 |

The framework difference is the **expense pattern**: IFRS 16 front-loads cost (depreciation plus interest) where ASC 842 straight-lines it. Classification: **timing / measurement**.

## Step 6 — Reconciliation (pre-tax; deferred tax not yet computed)

| | Nine-month profit | Equity at 30 Sep 2025 |
|---|---|---|
| As booked (TB) | 597,741.00 | 2,158,895.00 |
| A. US GAAP correction — warehouse lease under ASC 842 and the 3% escalation | (5,008.00) | (11,685.32) |
| **US GAAP, corrected** | **592,733.00** | **2,147,209.68** |
| B. US GAAP → IFRS 16 expense pattern (opening equity effect at 1 Jan 2025: (11,286.07)) | (5,139.24) | (16,425.30) |
| **IFRS, pre-tax** | **587,593.76** | **2,130,784.38** |

Equity as booked = share capital 250,000 + retained earnings 1,378,654 − dividends/adjustments 67,500 + profit 597,741.

**Deferred tax: not dropped, but blocked.** Each adjustment creates a temporary difference (right-of-use asset 321,769.97 vs liability 347,450.60 under IFRS). The TB has no tax accounts and no rate was supplied, so the tax effect is **not quantified**; give the rate and its source and I will gross it up.

**Proposed entries (IFRS, at 30 Sep 2025, not posted):** DR Right-of-use asset 495,030.73; CR Accumulated depreciation — ROU 173,260.76; CR Lease liability 347,450.60; DR Retained earnings (opening, 2024 effect: IFRS cost 125,963.40 less rent booked 108,000) 17,963.40; DR Depreciation 74,254.61 and DR Interest 16,892.62 for 2025; CR Rent 81,000.00; CR Accrued rent (escalation) 2,430.00. Debits = credits = 604,141.36; total equity effect (28,110.63) = A + B above. Final split between opening equity and 2025 profit to be confirmed once the transition date is known.

## Step 5 — First-time adoption

Not decided. If the group is a first-time adopter, IFRS 1 offers lessee exemptions (e.g. measuring the asset equal to the liability at transition) that would change line B. **Your election, with technical input.**

## Step 7 — Presentation and policies

Presentation only, no number: IFRS statement of financial position ordering and terminology; *Dividends and Adjustments* to be split into dividends and any other equity movement; interest paid classification in cash flows; lease liability split current / non-current. Policies to rewrite: leases (new), income tax (new), impairment, provisions. IFRS disclosures are more extensive and remain to be drafted.

## Not done, and why

Deferred tax (no rate); first-time-adoption elections (not answered); allowance, contingencies and PP&E components (no ageing, legal letter or register); comparative period (the September 2024 TB was rejected as the wrong period for this request). I would ask before creating `GAAP_IFRS_Conversion_2025_Northbrook Trading Ltd.xlsx`. Nothing was posted or changed.

## Coverage sheet (manual run)

| Section | Entry |
|---|---|
| Environment | Northbrook Trading Ltd, 30 Sep 2025, USD, US GAAP → IFRS — user-asserted; source: upload (Mosofin not used, by choice) |
| Files | TB Sep 2025 accepted with limit; policies accepted with limit; lease terms accepted with limit (summary); `trial_balance_september.csv` rejected (30 Sep 2024) |
| Capability map | Not applicable: no connection. Every task is `[manual]`. |
| Steps | 1 scoping done (10 areas); 2–3 done; 4 leases quantified, others not quantifiable; 5 not decided; 6 reconciliation done pre-tax; 7 listed |
| Not done | Deferred tax; IFRS 1 elections; ECL, provisions, components; comparative |

**Data sources:** uploads — `trial_balance_2025-09-30.csv`, `accounting_policies.md`, `lease_terms.md` (user-supplied lease terms and IBR, 6.0%, lender quote 12 Dec 2023).
