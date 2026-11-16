# US GAAP → IFRS conversion — Northbrook Trading Ltd, nine months to 30 September 2025 (upload path)

Mosofin is not connected for this run (you chose upload only), so every step is `[manual]` and works from your files. Connecting Mosofin would automate the reads — docs.mosofin.com. Nothing was posted: every adjustment below is a **proposal**. Standards are described as I understand them; please confirm the versions in force at your reporting date.

## (a) Read-back

Converting **Northbrook Trading Ltd** (user-asserted) from **US GAAP to IFRS**, as at **30 September 2025** (nine months YTD), **USD**, for **group reporting, ongoing** — so this is **not first-time adoption** of IFRS by the entity itself; IFRS 1 does not apply (Step 5 skipped). From `accounting_policies.md` (to confirm): private company; revenue on delivery; inventory at **weighted average**, lower of cost and NRV; fixed assets straight line 3–10 years; receivables allowance from ageing; accounts issued 20 March 2026.

**Materiality: not supplied** — the skill never supplies one, so **every difference found is listed and quantified where the data allows**. **Tax rate: not supplied** — deferred tax is shown as a temporary difference × rate, rate to be confirmed; it is not dropped.

## (b) Validation of the upload — shown before any work

| File | What it actually is | Company / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `trial_balance_2025-09-30.csv` | Trial balance, 29 accounts | No company or date in the file | Foots: DR = CR = 6,589,681. YTD P&L open; profit **605,615** | Yes — source figures, scoping (Steps 1, 6) | **Accepted with a limit: company and period user-asserted** |
| `accounting_policies.md` | Policy summary, 7 lines | Northbrook not named; undated | A summary, not the policy manual: figures and choices user-supplied, not evidenced. No lease, tax, provisions or impairment policy | Yes — source treatments (Step 2) | **Accepted with a limit** |
| `lease_terms.md` | Lease schedule: warehouse (from 1 Jan 2024, 5 years, 9,000/month in advance, +3% each January, one 3-year renewal at market) and printer (12 months from 1 Mar 2025, 180/month); discount rate 6.0% IBR (lender quote 12 Dec 2023) | Undated; no company | Yes; key terms, not the agreements | Yes — the lease adjustment (Step 4) | **Accepted with a limit**: summary of terms, not the contracts |
| `trial_balance_september.csv` | A trial balance — but **not at 30 Sep 2025**. Retained earnings 789,221 vs 1,422,317 (a full year's profit, 633,096, lower); accumulated depreciation 260,800 = 311,200 − 12 × 4,200; term loan 280,000 = 220,000 + 12 × 5,000. It is the **September 2024** TB | Names no year; content is a year earlier than the intake period | Foots, but wrong period | No step in a non-first-time conversion needs it | **Rejected**: wrong period (appears to be 30 Sep 2024). If you want a comparative, confirm and I will use it as such |

**Still missing:** the **tax rate** and current tax position (no tax accounts exist at all); a **materiality** level; the **receivables ageing** and allowance workings; **legal letter / contingency list** (Greyfriars); fixed-asset register (componentisation); policy elections — **short-term lease exemption** and **revaluation model** — which I will not decide for you.

*I would stop here and wait for your answer. Assumed answer: "go ahead with the accepted files".*

## (c) Scoping — all ten areas

| Area | Live here? | Evidence | Result |
|---|---|---|---|
| **Leases** | **Yes — material** | **Rent 81,000 YTD and no right-of-use asset or lease liability** in the TB, against a 5-year warehouse lease | Quantified below. This is also a **US GAAP gap**: ASC 842 already puts operating leases on a private company's balance sheet |
| Inventory | Yes (683,100) | Weighted average, lower of cost and NRV — permitted under IAS 2; no LIFO | No measurement difference; write-down reversals allowed under IFRS (none evidenced) |
| PP&E | Yes (cost 420,000, NBV 108,800) | Straight line 3–10 years | Componentisation required under IFRS — needs the register; revaluation optional, **your election**. Not quantified |
| Impairment | Low | No impairment charges; small NBV | IAS 36 one-step model; no indicator in the files |
| Development costs | No | No R&D account; software 31,500 looks like subscriptions | Ruled out (absence is a signal, not proof) |
| Financial instruments | Yes (AR 798,360, allowance 9,000) | Ageing-based allowance; unchanged at 9,000 | CECL vs IFRS 9: both expected-loss; a provision matrix can satisfy both. Needs ageing. Not quantified |
| Revenue | Yes | Recognised on delivery | ASC 606 / IFRS 15 converged; no difference expected |
| Provisions / contingencies | Yes (accruals 28,800; legal review by Greyfriars) | "Probable" means likely under ASC 450, more likely than not under IAS 37; range measured at the low end vs midpoint | Needs the contingency list. Not quantified |
| Income taxes | **Yes — by absence** | **No current or deferred tax account at all**, on 605,615 of profit | Raised as a finding under both frameworks; deferred tax on every adjustment needs the rate |
| Other (capitalised interest, pensions, share-based payment) | No | No such accounts | Ruled out |

## (d) Lease adjustment — warehouse (IFRS 16, single lessee model)

Contractual payments 9,000 a month in 2024, **9,270 in 2025** (+3%), 9,548.10, 9,834.54, 10,129.58; renewal **excluded** (at market rent; not shown to be reasonably certain — your judgment). Discount 6.0% a year (0.4868% a month, effective), payments in advance.

- Lease liability at 1 Jan 2024: **496,909.00** = right-of-use asset (no direct costs, no incentives). Depreciation 8,281.82 a month over 60 months.
- At **30 Sep 2025**: right-of-use asset **322,990.85**; lease liability **348,306.96** (payments due in the next 12 months 113,742.90 — the current portion is their present value).
- Nine months 2025 under IFRS: depreciation **74,536.35** + interest **16,492.18** = **91,028.53**, against rent of **81,000** in the books.

**Two things the books show that the terms do not explain:** rent of 81,000 = 9 × 9,000, but the 3% escalation makes 2025 rent **9,270** (83,430 for nine months) — **2,430 not booked**, an error under either framework; please confirm whether it was waived. And under correctly applied ASC 842 the straight-line cost would be 9,556.44 a month (86,008 YTD), so of the 10,028.53 below, **5,008.00 is a US GAAP correction** and **5,020.53 is the true framework difference** (front-loaded IFRS cost vs straight line).

**Printer (180 a month, 12 months):** qualifies for the short-term lease exemption under both frameworks. If you elect it, no adjustment; if not, a small asset and liability for the 5 remaining payments (900). **Your election.**

## (e) Reconciliations (pre-tax; tax rate needed)

| Net income, nine months to 30 Sep 2025 | USD |
|---|---:|
| US GAAP net income per TB (no tax provision recorded) | 605,615.00 |
| Reverse rent expense — warehouse | +81,000.00 |
| Right-of-use depreciation | (74,536.35) |
| Lease interest | (16,492.18) |
| **IFRS net income before deferred tax on adjustments** | **595,586.47** |
| Deferred tax on the adjustment: 10,028.53 × rate | **rate needed** |

| Equity at 30 Sep 2025 | USD |
|---|---:|
| US GAAP equity per TB (250,000 + 1,422,317 + 605,615) | 2,277,932.00 |
| Right-of-use asset | +322,990.85 |
| Lease liability | (348,306.96) |
| **IFRS equity before deferred tax** | **2,252,615.89** |
| Deferred tax asset: 25,316.11 × rate | **rate needed** |
| Of which at 1 Jan 2025 (opening retained earnings) | (17,717.58) |

If the 2,430 escalation is owed, add a 2,430 liability and expense (both frameworks).

**Presentation differences (no number, still work):** IFRS ordering if adopted by the group (non-current first is common), "trade and other receivables / payables", right-of-use asset and lease liability as separate lines, lease cash split between financing (principal) and interest in the cash flow statement, wider IFRS disclosures still to draft.

## (f) Not done, and why

Deferred tax amounts (no rate); componentisation, ECL, provisions (no register, ageing or legal list); restated statements (hand-off to `financial-statement-builder`); rewritten policies (`notes-to-financial-statements`); IFRS 1 (not first-time adoption). Open items for technical accounting and audit: the missing tax provision; the ASC 842 gap; the renewal option. No `.xlsx` created — I would ask whether you want `GAAP_IFRS_Conversion_2025_Northbrook Trading Ltd.xlsx`.

## (g) Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, 30 Sep 2025, USD, US GAAP → IFRS — user-asserted. Source: upload. TB, policies, lease terms accepted with limits; `trial_balance_september.csv` rejected (September 2024). |
| Capability map | Not applicable: no connection. Every task is `[manual]`. |
| Steps | 1 scoping done (10 areas) · 2 differences identified · 3 classified (leases: recognition and measurement; others measurement/presentation) · 4 leases quantified, others **not done** (schedules) · 5 n/a · 6 reconciliations done pre-tax · 7 **not done** (hand-offs) · 8 tables in chat · 9 not offered. |
| Not done | Deferred tax (rate); ECL (ageing); provisions (legal list); componentisation (register); source figures not tied to issued statements (none uploaded). |

**Data sources:** user uploads — `trial_balance_2025-09-30.csv`, `accounting_policies.md`, `lease_terms.md`.
