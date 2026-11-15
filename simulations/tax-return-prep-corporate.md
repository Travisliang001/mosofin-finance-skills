# Corporate tax computation — Northbrook Trading Ltd — Sampleland, tax year 2024

Mosofin is not connected, so this run is manual: every step is `[manual]` and every figure comes from your uploads. **This is a computation for a qualified tax professional to review, not tax advice.** Nothing is filed, paid or posted.

## Read-back

Preparing the **2024 corporate tax computation** for **Northbrook Trading Ltd** (user-asserted), jurisdiction **'Sampleland'**, calendar year to 31 December 2024, USD, from **your uploaded trial balance**, fixed asset register, rate card and tax computation summary. Data source: **upload only**.

| Intake question | Treatment |
|---|---|
| C — rates and rules | The rate card says **'sample rate card v1, tax year 2025'** and is marked fictitious. **It is not stated for 2024.** Rates are never carried across years, so the tax figure below is shown **only on the assumption that the same card applies to 2024** — please confirm or supply the 2024 card. |
| D — disallowed categories | From the same card: fines 100%, client entertainment 50%, donations above 10,000 (same 2024 caveat). |
| E — pools, losses, credits | Losses: the card says nil brought forward **at 1 Jan 2025**; the computation summary says "no losses carried forward". Taken as nil for 2024, user-supplied. Opening tax written-down values at 1 Jan 2024: **not supplied**. Credits: none stated. |
| F — group / related party | **Not answered.** The TB shows *Investment in Northbrook UK Ltd* (104,800) and *Intercompany Payable — Northbrook UK* (38,000), so related-party dealings exist. Default: **treated as standalone, assumed**; transfer-pricing and group relief not considered. |

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Step that uses it | Verdict |
|---|---|---|---|---|---|
| `trial_balance_2024-12-31.csv` | Year-end TB, 33 accounts; Dr = Cr 6,433,544. P&L open: revenue 4,597,600, expenses 3,982,661, **pre-tax profit 614,939**; no tax expense or tax payable account | No entity named | Yes | Steps 1, 2, 2b, 5 | **Accepted with a limit**: company user-asserted; finality not evidenced (no signed accounts) |
| `fixed_asset_register.csv` | Register, 8 assets, cost **420,000** = TB 1500; in-service dates and book lives | No entity; mentions a July 2025 sale, so prepared in or after 2025 | Yes | Step 4 | **Accepted with a limit**: no disposals in 2024; no tax WDVs per asset |
| `tax_rates_and_rules_SAMPLE.md` | Rate card, Sampleland, **tax year 2025**, fictitious | Year **2025**, not 2024 | Yes | Steps 2, 4, 7, 9 | **Accepted with a limit**: wrong stated year; used only as an assumption, shown as such |
| `prior_year_tax_computation_summary.md` | Despite the name, a **2024** computation summary: taxable profit 305,000, tax 61,000, WDV at 31 Dec 2024 101,600 | Tax year 2024 — the year being prepared | Yes, a summary | Prior-year attributes (losses nil); a cross-check | **Accepted with a limit**: summary, not the return; it is not a *prior*-year document (see finding 1) |
| `trial_balance_september.csv` | TB at **September** with no year: RE 763,715 (same opening RE as Dec 2024), revenue 3,499,900 — a **nine-month interim TB for 2024** | Wrong period | Foots (5,363,915) | None — the computation starts from the year-end TB | **Rejected** — interim, not the year's final accounts. Set aside. |

**Still missing:** the **2023 return** (opening tax WDVs per asset or pool, any 2023 add-backs to reverse); the **2024 rate card**; the signed 2024 accounts (Step 1b finality); tax instalments paid in 2024; ledger detail of Marketing and Professional Fees (Step 2b). I would wait for your answer here; proceeding on the accepted files.

## Computation (book-to-tax), on the 2025 card assumed for 2024

| Line | Amount | Source |
|---|---:|---|
| Pre-tax accounting profit | 614,939 | TB (4,597,600 − 3,982,661) |
| + Book depreciation added back | 50,400 | TB 6600 |
| + Fines / entertainment / donations | 0 | No such account in TB; see sweep |
| − Tax depreciation, 25% SL on cost 420,000 | (105,000) | Register + card; **ceiling per asset not testable** (see below) |
| **Adjusted taxable profit before losses** | **560,339** | |
| − Losses brought forward | 0 | User-supplied (nil) |
| **Taxable profit** | **560,339** | |
| Tax at 20% | **112,068** | Card (2025) — assumption |
| Credits | 0 | None stated |

**Tax depreciation ceiling.** 25% straight line exhausts an asset after four years. FA-004 (Sep 2020), FA-005 (Jan 2020) and FA-008 (May 2019) were in service more than four years by 2024; if their tax value is already nil, 2024 tax depreciation falls (full-year convention on the remaining assets: **71,000**, giving taxable profit 594,339 and tax 118,868). The opening WDV per asset is a tax attribute from the 2023 return; I have not derived it from the book register.

### Findings

1. **The uploaded "prior year" summary is a 2024 computation and does not agree with this one.** It shows 2024 taxable profit **305,000** and tax **61,000**; the TB gives pre-tax profit 614,939, so reaching 305,000 would need net deductions of 309,939 beyond the book profit — far more than any adjustment the card supports (depreciation swap at most 50,400 − 105,000 = −54,600). Either the summary is for a different year (2023) and mis-titled, or the 2024 figure was computed on different accounts. Please confirm which.
2. **No tax recorded in the 2024 books.** The TB has no income tax expense, tax payable or deferred tax account, yet the summary states a deferred tax liability of 9,000 at 31 Dec 2024 (20% × (146,600 − 101,600)). The book NBV 146,600 does agree to the TB (420,000 − 273,400). The provision appears unbooked: route to `corporate-tax-provision-asc740`.
3. **Rate card year mismatch:** card is for 2025; no 2024 rates were supplied.
4. **Related-party dealings with Northbrook UK Ltd** exist (investment 104,800; payable 38,000). Treated as standalone by assumption; any transfer-pricing adjustment is not considered.

## Step 2b — disallowable candidates sweep (TB-level only)

| Account | Amount | Suggested category | In computation? |
|---|---:|---|---|
| 6200 Marketing | 183,904 | May contain client entertainment (50% disallowed) and gifts | No — needs ledger detail |
| 6400 Professional Fees | 30,000 | Legal/professional: may include capital or disallowable elements | No — needs detail |
| 6500 Bank Fees | 18,392 | May include late-payment charges or penalties | No — needs detail |
| 7000 Interest Expense | 16,957 | Interest limitation — no rule on the card | No |

Candidates only; nothing is added back without the detail and your determination.

## Step 9 — payments

On the computation above, 112,068 due for 2024; instalments paid in 2024 not supplied, so the balance due and any missed instalment cannot be stated. Due dates not supplied.

## Not done, and why

- Opening tax WDVs, tax depreciation schedule by asset — need the 2023 return.
- Finality test (Step 1b) — no signed accounts.
- Disallowable determinations — need ledger detail of 6200, 6400, 6500.
- Return-to-provision — no provision booked.
- Excel workpaper — would ask before creating `Tax_Computation_2024_Northbrook_Trading_Ltd.xlsx`.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd (user-asserted), standalone (assumed), Sampleland, tax year 2024, USD. Starting point: Dec 2024 TB, finality unevidenced. Rates: sample card v1 for **2025**, fictitious, assumed for 2024. Files: 4 accepted with limits, 1 rejected (Sep 2024 interim TB). |
| Capability map | Not applicable: no connection. Every task is `[manual]`. |
| Steps | 1 done; 1b not done; 2 done (no listed categories in TB); 2b TB-level only; 3 nothing identified, reversals need 2023 computation; 4 done with limit (no ceiling); 5–7 done on assumed card; 8 none; 9 not done; 10 partial; 11 tables in chat. |
| Unknowns | 2024 rate card; 2023 WDVs; conflict with the 305,000 summary; unbooked provision; related-party pricing; instalments paid. |
| Parameters | 20% flat; 25% SL on cost; fines 100%, entertainment 50%, donations > 10,000 — from the 2025 card, to be re-confirmed for 2024. |
