# US sales tax review — Northbrook Trading Ltd, 2025 year to date

This run is manual: no Mosofin connection is present. Everything below comes from the files you uploaded. This is a computation for a qualified tax professional to review, not tax advice. Nothing has been registered, filed, remitted, posted or changed.

## (a) Read-back

Reviewing sales tax for **Northbrook Trading Ltd** (name as you stated it) for **2025 year to date, to 30 September 2025**, in **USD**, with sales by state from **the file you uploaded**. Registered in **two states** (Texas since 1 February 2019, California since 1 June 2020), as marked in that file. Thresholds from **"sample rate card v1, tax year 2025"**, which is marked as fictitious test data, not real tax law. Rates are applied by **your tax engine**; none were supplied. Physical presence, per the same card: Texas (warehouse) and California (two employees) only.

Intake questions the files do not answer, and the default applied:
- **What you sell and what is taxable or exempt** — not answered. Taxability is treated as recorded in the sales file, and I say so wherever it matters.
- **Exemption certificates and marketplaces** — not answered. No exempt sales are identified in the file, and marketplace sales are **not separated** from direct sales.
- **Rates** — none supplied. This blocks every rate check and every exposure amount.
- **Where inventory sits** (third-party warehouses, fulfilment networks) — not stated beyond the Texas warehouse. Please confirm; no ledger records this.

What I received:
- `sales_by_state_2025.csv` — 5 states; sales 3,508,000; 4,470 transactions; tax collected 196,200; registration flag and date per state.
- `sales_tax_thresholds_SAMPLE.md` — thresholds for Ohio and Georgia, a statement that Oregon has no state sales tax, physical presence facts, no rates.
- `sales_by_state_2025_final.csv` — 3 rows, columns employee / week_1..week_4, values nights / days / off.

## (b) Validation of the upload (before any work)

| File | What it actually is | Right company and period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `sales_by_state_2025.csv` | Sales summary by state with transaction count, tax collected and registration status | No company named in it. "2025" only in the file name; it does not say whether it runs to 30 September or covers a full year | Columns identifiable; totals foot (3,508,000 / 4,470 / 196,200). One row per state: no months, no customers, no items, and it does not say whether "state" is ship-to or billing | Steps 1, 1b, 4 | **Accepted with a limit**: no crossing date can be computed, no taxable/exempt split, no marketplace split, and the state analysis is **indicative** until the address field is confirmed. It also serves as the registration list |
| `sales_tax_thresholds_SAMPLE.md` | A threshold card with physical presence facts | Tax year 2025. Marked fictitious | Usable for Ohio and Georgia. No thresholds for Texas or California, no rates, no measurement period for Georgia | Steps 1, 1b | **Accepted with a limit**: threshold tests for Ohio and Georgia only; no rate check anywhere |
| `sales_by_state_2025_final.csv` | A four-week staff shift roster (E08–E10) | No company, period, state or amount | Not for this skill | No step uses it | **Rejected**. The name suggests a final sales-by-state file; the content is a rota. Set aside. If there is a final sales file, please upload it |

**Still missing:** rates, or a rate report from your tax engine (required for exposure and rate checks); monthly or transaction-level sales by ship-to state (needed for the date each threshold was crossed); returns filed, the sales tax payable ledger, the purchase ledger and the exemption certificate register (recommended). I would stop here and wait for your answer.

*You replied: go ahead with the accepted files.*

## (c) Findings

**Step 1 — sales against the thresholds supplied** (source: sample rate card v1, tax year 2025; address field unconfirmed)

| State | Physical presence (as supplied) | Sales | Sales threshold | Sales vs threshold | Transactions | Count threshold | Count vs threshold | Registered? | Tax collected |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|
| Texas | Yes, warehouse | 1,840,000 | not supplied | — | 2,210 | not supplied | — | Yes, 2019-02-01 | 115,000 |
| California | Yes, two employees | 1,120,000 | not supplied | — | 1,480 | not supplied | — | Yes, 2020-06-01 | 81,200 |
| Ohio | None stated | 310,000 | 100,000 | 310% | 402 | 200 | 201% | **No** | 0 |
| Georgia | None stated | 142,000 | 100,000 | 142% | 260 | 200 | 130% | **No** | 0 |
| Oregon | None stated | 96,000 | none: no state sales tax per the card | — | 118 | — | — | No | 0 |
| Total | | 3,508,000 | | | 4,470 | | | | 196,200 |

**Step 1b — the exposure join**

1. **Ohio: over both thresholds supplied, not registered, no tax collected.** Sales of 310,000 are 3.1 times the 100,000 sales threshold and 402 transactions are twice the 200 count threshold. Either test alone is passed. This is a state for your tax professional to review for economic nexus. Untaxed sales in the file: 310,000.
2. **Georgia: over both thresholds supplied, not registered, no tax collected.** Sales of 142,000 are 42,000 over the 100,000 threshold and 260 transactions are 60 over the 200 count threshold. Also a state to review. Untaxed sales in the file: 142,000.
3. **Oregon: no action indicated.** The card says Oregon has no state sales tax, so there is no threshold to test and nothing to collect on 96,000 of sales. Nothing here should be read as exposure.
4. **Texas and California: registered and collecting**, with physical presence. Consistent on the face of it.
5. **No state is approaching a threshold**; the two tested states are already well over.

Sales in states to review where no tax was collected: 310,000 + 142,000 = **452,000**, which is 12.9% of total sales.

I am not concluding that nexus exists in Ohio or Georgia. That is a determination for a qualified professional, on current law, and the thresholds used here are sample figures.

**Trigger date — not computable.** The file has one total per state. The month each threshold was crossed needs sales and counts by month. With these figures the crossings were certainly before 30 September 2025, and for Ohio probably early in the year (at an even run rate over nine months, 100,000 of sales by about the end of March and 200 transactions by about mid-May; that is an illustration, not a finding). If the thresholds also look at the prior calendar year, 2024 sales by state are needed too.

**Indicative exposure — not quantified.** No rates were supplied and I do not supply one. Once your tax engine's combined rates for Ohio and Georgia are provided, the indicative figure is taxable sales since the crossing date times that rate, still subject to the taxability of what you sell.

**Step 2 — registration.** For Ohio and Georgia, raise the sequencing question with a specialist **before** registering: registering first can limit what a voluntary disclosure agreement can achieve on the back period. The customers cannot now be charged, so any back tax would come out of margin.

**Step 4 — effective rate collected** (tax collected over total sales; taxability as recorded)

| State | Sales | Tax collected | Effective rate |
|---|---:|---:|---:|
| Texas | 1,840,000 | 115,000 | 6.25% |
| California | 1,120,000 | 81,200 | 7.25% |

Both sit on what looks like a single flat rate. With no expected combined rates supplied I cannot say whether they are right. A flat state-level rate can mean local or district rates are not being charged, or that some sales are exempt; that is a question for your tax engine report, not a finding.

**Steps 3, 5–9.** Not performed; see below.

## (d) What was not done, and why

- **Nexus conclusions** — never made by this skill; Ohio and Georgia are named for review.
- **Crossing dates** — no monthly or transaction-level data.
- **Exposure in dollars** — no rates supplied; this skill never supplies one.
- **Texas and California threshold tests** — no thresholds supplied (both have stated physical presence).
- **Taxability matrix (Step 3)** — no item list; no determinations supplied.
- **Exemption certificate gap analysis (Step 5)** — no register, and exempt sales are not shown in the file.
- **Use tax (Step 6)** — no purchase ledger.
- **Return figures and reconciliation, including the collected-not-remitted test (Steps 7–8)** — no returns and no sales tax payable ledger. I cannot say whether the 196,200 collected has been remitted.
- **Marketplace split (Step 9)** — not separated in the file; if you sell through a marketplace, direct sales may be lower than shown, though marketplace volume may still count toward the thresholds.
- **Period and address field** — the sales file does not say whether it ends 30 September 2025 or which address it uses. Please confirm both.
- **Inventory location outside Texas** — please confirm; stored inventory generally creates physical presence.
- **Excel workbook** (`Sales_Tax_Multistate_2025-YTD_Northbrook Trading Ltd.xlsx`) — not created; say if you want it.
- **Registering, filing, remitting, posting** — never done by this skill.

**Parameters used (to be re-confirmed next time, none carried forward):** thresholds Ohio and Georgia 100,000 of sales or 200 transactions, and Oregon no state sales tax, all from "sample rate card v1, tax year 2025" (fictitious sample); rates: none; period: 2025 year to date as stated at intake; states in scope: the five in the file.
