# Deferred tax roll-forward — Northbrook Trading Ltd, 1 January to 30 September 2025

This run is manual: no Mosofin connection is present. Everything below comes from the files you uploaded. It is a computation for a qualified tax professional to review, not tax advice. Nothing has been posted, filed or changed.

## (a) Read-back

Rolling forward deferred tax for **Northbrook Trading Ltd** from **31 December 2024 to 30 September 2025**, jurisdiction **"Sampleland"**, in **USD**, from **the trial balance at 30 September 2025, the fixed asset register and the 2024 tax computation you uploaded**. Enacted rate **20%**, from **"sample rate card v1, tax year 2025"**, the rate for every reversal year as stated there. Losses brought forward **nil**, per the rate card and the 2024 computation. Company, period and currency are as you stated them.

Taken from the files, for you to confirm: the jurisdiction, the 20% enacted rate for reversal periods, tax depreciation at 25% straight line on cost, nil losses, and the opening deferred tax liability of 9,000. Not answered anywhere: **the tax basis at 30 September 2025 by asset** (only a 31 December 2024 total), **whether the bad debt allowance, accruals and prepayments are deductible when booked or when paid**, and **the tax treatment of the July 2025 van sale**.

What I received:
- `trial_balance_2025-09-30.csv` — 29 accounts; foots at 6,589,681; profit to date 605,615.
- `trial_balance_september.csv` — 29 accounts, same chart; foots at 5,389,421; profit to date 499,661.
- `fixed_asset_register.csv` — 8 assets, cost 420,000, in-service dates and useful lives; no depreciation or tax columns.
- `prior_year_tax_computation_summary.md` — 2024: taxable profit 305,000, tax 61,000, tax written-down value 150,000 on cost 420,000, deferred tax liability 9,000.
- `tax_rates_and_rules_SAMPLE.md` — the rate card: 20%, disallowed items, tax depreciation 25% straight line, nil losses.

## (b) Validation of the upload (before any work)

| File | What it actually is | Right company and period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `trial_balance_2025-09-30.csv` | A trial balance, year to date | **Names no company, date or currency** | Yes; foots | Steps 1, 3, 4: book basis | **Accepted with a limit**: company and period user-asserted |
| `trial_balance_september.csv` | A second trial balance on the same chart | No company, date or currency; **conflicts with the file above**: retained earnings 789,221 vs 1,422,317 (633,096 lower, about a year's profit), term loan 280,000 vs 220,000 | Foots, but cannot be the same date | No step can use two trial balances for one date | **Rejected**: on its content it is a different period, most likely September 2024. If this is in fact the 30 September 2025 balance, tell me and I will rerun (result shown under finding 4) |
| `fixed_asset_register.csv` | A fixed asset register | No company or date; cost 420,000 agrees to the trial balance | Yes, but no accumulated depreciation and no tax columns | Step 1: depreciation difference | **Accepted with a limit**: company user-asserted; book basis by asset must be recomputed; FA-008 is marked sold in July 2025 but still in cost |
| `prior_year_tax_computation_summary.md` | A summary of the 2024 tax computation | 2024, prior year; no company named | Yes | Step 3 opening balance; tax basis at 31 Dec 2024 | **Accepted with a limit**: a summary in place of the prior deferred tax workpapers and the return; figures user-supplied, not evidenced |
| `tax_rates_and_rules_SAMPLE.md` | Rate card, labelled sample rates for testing | Tax year 2025 | Yes; source quoted | Step 2 | **Accepted with a limit**: user-supplied rates, quoted with their source |

**Still missing:** the **tax basis schedule by asset at 30 September 2025**, including tax depreciation (required), the **prior deferred tax workpapers** (required; a summary received), and the tax treatment of the allowance, accruals and prepayments. I would stop here and wait for your answer.

*You replied: go ahead with the accepted files.*

## (c) Findings

**1. No deferred tax in the ledger at all.** The trial balance has no deferred tax liability, no income tax expense and no tax payable account, yet the 2024 computation reports a deferred tax liability of 9,000 at 31 December 2024. Either it was never booked or it sits in another account. **The roll-forward cannot tie to the balance sheet** and the year-to-date P&L carries no tax charge on profit of 605,615.

**2. Opening balance does not reproduce.** A 9,000 liability at 20% means a taxable difference of 45,000, i.e. book value of fixed assets 195,000 against tax value 150,000. The trial balance implies book value at 31 December 2024 of 420,000 − (311,200 − 37,800) = **146,600**, which against 150,000 gives a small **deductible** difference of 3,400 (an asset of 680), not a 9,000 liability. Gap in book value: **48,400**. The prior workpapers are needed.

**3. Inventory of temporary differences** (permanent items such as fines, entertainment and donations are excluded; they belong in the rate reconciliation).

| Item | Account | Book basis 30 Sep 2025 | Tax basis | Status |
|---|---|---:|---:|---|
| Fixed assets | 1500 / 1510 | 108,800 (420,000 − 311,200) | Not supplied by asset; see 4 | Taxable difference |
| Allowance for doubtful accounts | 1150 | 9,000 | Not supplied | **Possible missed difference** (deductible) |
| Accrued liabilities | 2100 | 28,800 | Not supplied | **Possible missed difference** (deductible if deducted when paid) |
| Prepaid expenses | 1300 | 18,000 | Not supplied | **Possible missed difference** (taxable if deducted when paid) |
| Losses carried forward | — | — | Nil per rate card | None |

No double counts and no inventory item without an account.

**4. Fixed asset difference — two readings of the tax basis, results under each (please choose).**

| | Reading A: 2024 WDV rolled forward | Reading B: rule applied asset by asset from the register |
|---|---:|---:|
| Tax value 31 Dec 2024 | 150,000 (your computation) | 63,292 |
| Tax depreciation Jan–Sep 2025 | 78,750 (25% × 420,000 × 9/12) | per asset, monthly |
| Tax value 30 Sep 2025 | 71,250 | 28,542 |
| Book value 30 Sep 2025 | 108,800 | 108,800 |
| Taxable temporary difference | 37,550 | 80,258 |
| **Deferred tax liability at 20%** | **7,510** | **16,052** |

The two disagree because the 25% straight-line rule, applied to the register's in-service dates, would have written most of the 420,000 off by 2024 (tax value about 63,000), not left 150,000. Reading A also depreciates assets that are already fully written off. Neither is reliable without the tax schedule. With the rejected September trial balance instead, book value is 159,200 and Reading A gives 17,590.

**5. Roll-forward (Reading A, illustrative).**

| Line | Amount |
|---|---:|
| Opening deferred tax liability (2024 computation) | 9,000 |
| Current period movement (credit to deferred tax expense) | (1,490) |
| Rate change | 0 (20% throughout) |
| Acquisitions / disposals | 0 recorded (see 6) |
| **Closing deferred tax liability** | **7,510** |
| Tie to balance sheet | **Not possible**: no deferred tax account (difference 7,510 against nil) |
| Tie to P&L deferred tax expense | **Not possible**: no tax expense account |

**6. Van sold in July 2025 (FA-008) not removed.** Cost 12,000 is still in the register and in account 1500. It was fully depreciated for book purposes, so book value is unchanged, but cost and accumulated depreciation are both overstated by 12,000, and any proceeds and gain are unrecorded. Its tax effect depends on a disposal rule the rate card does not give.

**7. Book depreciation check.** Recomputing from the register (straight line, monthly from the in-service month), the charge for January–September 2025 is about 37,000, close to the 37,800 booked; but accumulated depreciation at 30 September comes to about 248,800 against 311,200 in the trial balance, a gap of about 62,400 I cannot explain from the register.

**8. Valuation allowance evidence.** No deferred tax asset of substance arises. Objective evidence is positive: profit to date 605,615; 2024 taxable profit 305,000; no losses. No cumulative loss. The conclusion is yours.

**9. Proposed entries — PROPOSALS, NOT POSTED**, pending findings 1, 2 and 4 (generic names; no tax accounts exist in this chart): first record the opening liability once confirmed (Dr retained earnings or prior-year tax expense 9,000 / Cr deferred tax liability 9,000); then the movement on Reading A (Dr deferred tax liability 1,490 / Cr deferred tax expense 1,490).

## (d) What was not done, and why

- **Tax basis by asset, disposal treatment, deductibility of accruals and allowances** — not supplied; owner: tax preparer.
- **Ties to balance sheet and P&L, tie to the total provision, rate reconciliation** — no tax accounts in the ledger; see `corporate-tax-provision-asc740`.
- **Disclosures** — components only; no expiring losses or credits.
- **Excel workpaper** (`Deferred_Tax_Rollforward_2025_Northbrook Trading Ltd.xlsx`) — not created; say if you want it.
- **Posting and filing** — this skill never posts or files.

## Coverage (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, 30 Sep 2025, USD, Sampleland — user-asserted. Source: upload. TB 2025-09-30 accepted with a limit; TB "september" rejected (different period on content); register, 2024 summary, rate card accepted with limits |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 1 done with a limit (three possible missed differences); 2 done under two readings; 3 done with a limit (ties not possible); 4 done; 5 not done; 6 proposals; 7 partial; 8 tables in chat; 9 not offered |
| Not done | Balance sheet and P&L ties, prior-period workpaper agreement: need the tax accounts or the prior workpapers |

**Data sources:** user-uploaded `trial_balance_2025-09-30.csv`, `fixed_asset_register.csv`, `prior_year_tax_computation_summary.md`, `tax_rates_and_rules_SAMPLE.md` ("sample rate card v1, tax year 2025"); intake answers. No ledger read.
