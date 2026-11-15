# Tax provision — Northbrook Trading Ltd — nine months to 30 September 2025

Mosofin is not connected, so this run is manual: every step is `[manual]` and every figure comes from your uploads. Connecting Mosofin would read pre-tax income, the deferred tax accounts and three years of results directly ([docs.mosofin.com](https://docs.mosofin.com)). **This is a computation for a qualified tax professional to review, not tax advice.**

## Read-back

Computing the **interim tax provision for the nine months to 30 September 2025** for **Northbrook Trading Ltd** (user-asserted), **USD** (user-asserted), **US GAAP**, from **your uploads**. Rates and rules from `tax_rates_and_rules_SAMPLE.md`, quoted back as **"sample rate card v1, tax year 2025"**, jurisdiction **Sampleland**: corporate tax **20%**, enacted future rate **20%**, tax depreciation **25% straight line on cost**, losses brought forward **nil**. The file itself says these are **sample rates, not real law** — used only once you confirm them here. Opening position from `prior_year_tax_computation_summary.md`.

Unanswered, and how this run treats them: permanent vs temporary classification and tax bases (D) — **candidates listed, not determined**, except the fixed-asset tax value supplied; uncertain positions and future-income support (F) — **not assessed**; annual forecast for the interim effective rate — **not supplied** (see Step 1).

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Needed for | Verdict |
|---|---|---|---|---|---|
| `trial_balance_2025-09-30.csv` | Account-level TB, 29 accounts; debits = credits **6,589,681**; RE **1,422,317**; nine months of P&L | No entity or currency; date in file name only | Yes. **No income tax expense, payable or deferred tax account** | Steps 1–5, 10 (pre-tax income, book side) | **Accepted with a limit**: company and date user-asserted |
| `tax_rates_and_rules_SAMPLE.md` | Rate card: 20%, disallowances, 25% SL tax depreciation, instalments, enacted future rate 20% | Sampleland, tax year 2025; source named | Yes; marked **fictitious sample** | Steps 2, 4, 5, 9 (every rate) | **Accepted with a limit**: rates **user-supplied with source and year**; confirm they apply |
| `prior_year_tax_computation_summary.md` | 2024 computation summary: taxable profit 305,000, tax 61,000, fixed assets tax WDV 150,000 at 31 Dec 2024, DTL 9,000 | 2024 year | A **summary**, not the return or last year's workpaper; no per-asset tax values, no DTL components | Step 5 (opening deferred tax), Step 4 (tax basis) | **Accepted with a limit**: figures user-supplied, not evidenced |
| `fixed_asset_register.csv` | 8 assets, cost total **420,000**, in-service dates, book lives; FA-008 "sold Jul 2025" | No entity | Cost agrees to TB 1500. No accumulated depreciation or tax value per asset | Step 3 (depreciation difference) | **Accepted with a limit**: cannot reproduce book accumulated depreciation (311,200) or the tax WDV (150,000) |
| `trial_balance_september.csv` | A **September** TB whose RE is **789,221** and revenue 3,499,900 — not the 2025 TB (RE 1,422,317, revenue 4,038,600). Same chart, earlier year: **September 2024** | No date in the file; content shows the **prior year** | Foots (5,389,421) | No step: the provision is for 2025 | **Rejected** — wrong year. If you meant three years of P&L for the valuation allowance evidence, upload the 2022–2024 P&Ls instead |

**Still missing:** (1) **per-asset tax written-down values** at 31 Dec 2024 (needed for 2025 tax depreciation); (2) **last year's provision workpaper** with the DTL by component; (3) **full-year 2025 forecast** (interim effective rate); (4) **pre-tax results for 2022–2024** (valuation allowance evidence); (5) tax **instalments paid** in 2025. I would wait here; proceeding on the accepted files as instructed.

## Step 1 — Pre-tax book income

**605,615** for the nine months (revenue 4,038,600 less expenses 3,432,985). **No tax charge is posted** — the TB has no tax account at all. Interim method (ASC 740-270): estimated annual effective rate × year-to-date income. No forecast was supplied; because no permanent difference, credit or allowance is identified, the estimated annual rate equals the statutory **20%** — an assumption to confirm with the forecast.

## Steps 2–3 — Differences

**Permanent — candidates only (prompts, not determinations):** no account in the TB is named for fines, entertainment or donations. 6200 Marketing (172,474) may include client entertainment (50% disallowed per the rate card) — please confirm. None applied.

**Temporary — book side read, tax side supplied or outstanding:**

| Item | Book (read) | Tax (supplied) | Status |
|---|---:|---:|---|
| Fixed assets, 31 Dec 2024 | NBV 146,600 (420,000 − 273,400, i.e. 311,200 less 9 months × 4,200) | WDV 150,000 | Deductible difference **3,400** → **DTA 680** |
| Depreciation, 9M 2025 | 37,800 | Not computable per asset (Finding 2) | Illustrated below |
| Allowance for doubtful accounts | 9,000 | Not supplied (rate card silent) | Not determined |
| Accrued liabilities / prepaid | 28,800 / 18,000 | Not supplied | Not determined |

## Findings

**1. The opening deferred tax does not reconcile.** The 2024 summary says **DTL 9,000** at 31 Dec 2024, which needs book NBV to exceed tax WDV by 45,000 (9,000 / 20%). The figures supplied give the opposite: tax WDV 150,000 **exceeds** book NBV 146,600 by 3,400 — a **DTA of 680**. The 9,680 gap must be explained (another component, or an error) before the deferred tax roll-forward can tie.

**2. 2025 tax depreciation cannot be computed reliably.** The rule is 25% of cost a year, but only the pooled WDV is given, and three assets (FA-004, FA-005, FA-008; cost 136,000) were in service by 2020 and are likely fully claimed. The register does not reproduce the 150,000 WDV under either a monthly or a full-year convention (it gives 48,000–63,300 of remaining value). **Illustration A** (25% × 420,000 × 9/12 = **78,750**, within the 150,000 WDV) is shown only to make the split visible.

**3. The books carry no tax at all.** No current tax payable, no tax expense and no deferred tax account in the 2025 TB, while the 2024 summary shows tax of 61,000 and a DTL of 9,000. Either they sit in accounts not in this TB, or **the 2024 tax and deferred tax were never booked** — a prior-period question for your accountant. No 2025 instalments are visible either (safe harbour 100% × 61,000 = **4 × 15,250**, per the rate card).

**4. FA-008 sold in July 2025 but still in cost.** TB cost 1500 is **420,000** = the register total *including* FA-008 (12,000). The disposal, proceeds and any gain or loss are not in the books, and the rate card gives no tax rule for disposals. Raise with the fixed-asset owner; it affects both bases.

## Steps 4–5, 9–10 — Provision (proposal; Illustration A for the split)

| | Amount |
|---|---:|
| Pre-tax income | 605,615 |
| + book depreciation − tax depreciation (37,800 − 78,750) | (40,950) |
| Taxable income (estimate) | 564,665 |
| **Current tax at 20%** | **112,933** |
| **Deferred tax** (40,950 × 20%, DTL originating) | **8,190** |
| **Total provision, 9M** | **121,123** — ETR **20.0%** |

ETR reconciliation: tax at statutory 20% × 605,615 = 121,123; permanent differences 0; credits 0; allowance 0; rate change 0; **Other 0** (threshold for break-out: 1% of pre-tax income, 6,056). The **total of 121,123 does not depend on Illustration A**; only the current/deferred split does.

Deferred roll-forward under the bases supplied: opening **DTA 680** + expense 8,190 → closing **DTL 7,510** (book NBV 108,800 vs tax WDV 71,250, difference 37,550 × 20%). Using the summary's opening DTL 9,000 instead, the deferred line would be a 1,490 benefit and the reconciliation would carry a **9,680 "Other"** — above threshold, so not presented.

Proposed entry, for review only: DR Income tax expense – current 112,933; DR Income tax expense – deferred 8,190 / CR Income tax payable 112,933; CR Deferred tax liability 8,190. Not posted.

## Steps 6–8

**Valuation allowance:** no DTA of substance on Illustration A; losses brought forward nil. Measured evidence available: 9M 2025 pre-tax **605,615** and 2024 taxable profit 305,000. Three-year cumulative pre-tax result **not measured** (2022–2024 P&Ls not supplied). No conclusion drawn. **Uncertain positions:** not assessed (none supplied). **Intraperiod allocation:** no OCI or equity items in the TB; all to continuing operations.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, 9M to 30 Sep 2025, USD, US GAAP, Sampleland — **user-asserted**. Source: **upload** (Mosofin not used, your choice). Rate: 20% current and enacted future, **"sample rate card v1, tax year 2025"**. `trial_balance_september.csv` **rejected** (September 2024) |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 1 done (AETR assumed 20%) · 2 candidates only · 3 book side done, tax side partial · 4 done on Illustration A · 5 done, opening **does not tie** · 6 evidence partial, no conclusion · 7 not assessed · 8 done · 9 done · 10 deferred roll-forward ties only on the bases supplied · 11 tables in chat; `Tax_Provision_2025_Northbrook Trading Ltd.xlsx` offered · 12 not offered |
| Not done | Per-asset tax values; last year's workpaper; forecast; 2022–2024 P&Ls; instalments paid; disposal of FA-008 |

Specialist flags: none (single jurisdiction; no foreign operations or Pillar Two indicators). Nothing was posted or filed. **Data sources:** upload — `trial_balance_2025-09-30.csv`, `tax_rates_and_rules_SAMPLE.md`, `prior_year_tax_computation_summary.md`, `fixed_asset_register.csv`.
