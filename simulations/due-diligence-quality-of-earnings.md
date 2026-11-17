# Quality of earnings (buy-side) — Northbrook Trading Ltd — twelve months to 30 September 2025

**Statement-level review only.** No trial balance or ledger was supplied, so this is a review of management's monthly statements and bridge, not of the transactions behind them. It is analysis for the deal team: **not an audit, and not a recommendation to buy.** Mosofin is not connected; every step is `[manual]` and every figure comes from the data room files you uploaded. Connecting Mosofin to the target's books would let the ledger behind each adjustment be read ([docs.mosofin.com](https://docs.mosofin.com)).

## Read-back

Buy-side quality of earnings on **Northbrook Trading Ltd** (target), **LTM to 30 September 2025**, plus the two prior years to September (FY23 Oct 2022 – Sep 2023, FY24 Oct 2023 – Sep 2024), **USD**, all user-asserted. **Earliest period the data supports: October 2022** — so the one-time test covers LTM and two prior years, not three. Management proposes **four adjustments**. Related parties as listed in `related_parties.md` (to be confirmed by you). Ledger depth: **statements only** (question D unanswered; the skill's default). Go-ahead assumed.

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Needed for | Verdict |
|---|---|---|---|---|---|
| `monthly_profit_and_loss_36m.csv` | Monthly P&L by line, Oct 2022 – Sep 2025, 36 months; every month foots to net income | No entity or currency | Yes | Steps 2–4, 3b | **Accepted with a limit**: company user-asserted; no customer or product split |
| `monthly_balance_sheet_36m.csv` | Monthly balance sheet, Oct 2022 – Sep 2025; balances every month; retained earnings move by exactly net income each month | No entity or currency | Yes | Steps 2, 5, 6, 7 | **Accepted with a limit**: company user-asserted; summary lines only |
| `management_adjusted_ebitda_bridge.csv` | Management's four proposed adjustments, net +57,300 | No entity or period stated | Yes | Steps 3, 3b | **Accepted with a limit**: management's assertions — each is tested below, none accepted on its face |
| `related_parties.md` | Short list of related parties: Northbrook UK Ltd (80% subsidiary), A. Reyes (CEO; owns Halden Property Management, the warehouse landlord), J. Marsh (director since June 2025), Investor A (20% shareholder) | Names Northbrook group | Yes | Step 3 (owner / related-party normalisations), Step 9 | **Accepted with a limit**: a summary, user-supplied; whose 80% and whose 20% is not stated |
| `monthly_profit_and_loss_36m_final.csv` | **An employee shift rota** (E08–E10, weeks 1–4). Not a P&L, despite its name | None | n/a | No step uses it | **Rejected.** If a later or final P&L exists, upload that instead |

**Still missing:** **trial balances and ledger** (required for depth: without them no adjustment can be traced to transactions); **payroll detail** showing the owner's 192,000; **revenue by customer and invoice listing** (concentration, cut-off); **debt schedule / loan terms**; **market rent benchmark**; **trade show invoice**; any **forecast**. **Perimeter:** Northbrook UK Ltd is listed as an 80% subsidiary, but the statements show no intercompany balance and no minority interest — they look like **Northbrook Trading Ltd alone**. Please confirm the deal perimeter: if the subsidiary is in the deal, consolidated figures are needed before normalising. Would wait here; proceeding on the accepted files.

## Base numbers (Step 2)

The balance sheet balances in all 36 months; retained earnings roll forward by exactly net income (no dividends, no tax); fixed assets fall by exactly the depreciation charge every month; debt falls 5,000 every month. **There is no income tax line and no tax liability in any month** — for a limited company this needs explaining (tax DD).

| | FY23 | FY24 | LTM Sep 25 |
|---|---:|---:|---:|
| Revenue | 3,857,500 | 4,451,200 | 5,136,300 |
| Gross margin | 42.0% | 42.0% | 41.4% |
| **Reported EBITDA** (net income + interest + depreciation) | 500,021 | 665,649 | **812,250** |
| EBITDA margin | 13.0% | 15.0% | 15.8% |

## Adjusted EBITDA bridge — LTM

| # | Adjustment | Management | Diligence view | Basis |
|---|---|---:|---:|---|
| | Reported EBITDA | 812,250 | 812,250 | |
| 1 | One-time legal fee, June 2025 | +14,000 | **+14,000** (subject to the invoice) | June professional fees 16,500 against a flat 2,500 every other month for 36 months: the excess is exactly 14,000 and **does not recur** in FY23 or FY24 |
| 2 | Owner salary above market | +60,000 | **0 — not evidenced** | Payroll is one aggregate line (885,600 LTM); the 192,000 paid and the 132,000 market rate are management's figures with no payroll record or benchmark. If both are evidenced: +60,000 |
| 3 | Trade show marketing "one-time" | +7,300 | **0 — rejected** | Trade shows are ordinary marketing and normally recur. The September spike does not match the claim: marketing is 4.0% of revenue in 35 of 36 months, September is 29,146 (6.4%), **10,930** above run-rate, not 7,300. Unexplained 3,630 |
| 4 | Related-party rent below market | −24,000 | **−24,000** | Landlord Halden Property Management is owned by the CEO (related-party file); rent 108,000 a year in every year; post-deal rent will be at market. Market rate (132,000 implied) to be benchmarked |
| | **Adjusted EBITDA** | **869,550** | **802,250** | 862,250 if item 2 is evidenced |

Management's adjustments total +57,300, **7.1% of reported EBITDA** — a normalisation, not a reconstruction.

**Recurring "one-time" test (Step 3b)**

| Add-back | LTM | FY24 | FY23 | Every year? |
|---|---:|---:|---:|---|
| Professional fees above 2,500/month | 14,000 | 0 | 0 | No |
| Marketing above 4.0% of revenue | 10,930 | 0 | 0 | No in the data — but a trade show is a recurring activity in substance |
| Owner salary | not separable | not separable | not separable | Untestable without payroll |
| Related-party rent | 108,000 | 108,000 | 108,000 | **Yes** — a recurring normalisation, correctly a deduction |

**Symmetry:** no one-time income items appear in any year (no other income, no asset-sale gains). Management's bridge does include one adverse item (rent), which is to its credit.

**Run-rate observation, not in the bridge:** COGS moved from **58% to 60% of revenue from July 2025** and stayed there. If 60% is the new level, LTM EBITDA overstates the run-rate by **74,258** (2% × LTM revenue 5,136,300 = 102,726, less 28,468 already borne in Jul – Sep). Ask management why: price, mix or input cost.

## Revenue quality (Step 4)

Strong growth (+15.4% FY24, +15.4% LTM) with clear seasonality: peak in June – July, trough in November – December. **Concentration, churn, recurring split and cut-off: not done** — no customer or invoice data.

## Working capital (Step 5) — trade NWC = AR + inventory + prepaid − AP − accrued

| Method (LTM Oct 2024 – Sep 2025) | Target level |
|---|---:|
| Average | **1,028,604** |
| Median | 1,049,963 |
| Peak-to-trough midpoint (829,410 Nov 24; 1,223,079 Jul 25) | 1,026,245 |
| 24-month average | 912,742 |

Spread between methods: up to **136,221** (median vs 24-month average) — that is what the negotiation is about. **I do not set the peg.** NWC at 30 Sep 2025: 1,151,896, 123,292 above the LTM average (seasonal). **Deterioration:** DSO 43.8 → 47.1 → 50.5 days and DIO 62.8 → 72.8 days (Sep 23 → Sep 25); DPO 35.4 → 32.0. Receivables and stock are building faster than sales — ask about AR ageing and slow-moving stock.

## Net debt (Step 6) and capex (Step 7)

Debt 220,000 − cash 1,237,236 = **net cash 1,017,236** at 30 Sep 2025. Debt-like items to negotiate: **accrued liabilities 38,000**; **unrecorded income tax** (none on the balance sheet); any lease liability (none recorded; the warehouse is rented from a related party). Interest of 1,900 every month on a balance falling from 280,000 to 220,000 is an effective ~9.2% — check the loan terms. Net debt definition to be agreed with `business-valuation`.

**No capex in 36 months.** Fixed assets net fell from 255,800 to 108,800 purely by depreciation (50,400 a year). **Capex is sustained far below depreciation: the business is being run for cash and the buyer inherits a catch-up.** Maintenance capex cannot be split without a fixed-asset register.

## Risks and open items (Steps 8–9)

1. Perimeter: the 80% subsidiary Northbrook UK Ltd is outside these figures (legal / structure). 2. **Tax: no tax charge or liability in three years** (tax DD). 3. Related-party rent with the CEO's company (needs market benchmark and a post-deal lease). 4. Margin step-down from July 2025. 5. Zero capex. 6. AR and inventory days rising. 7. Key person: A. Reyes is CEO, director and landlord; J. Marsh joined the board in June 2025 — June's legal fee may relate. Forecast assessment: **not done** — none supplied.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Target Northbrook Trading Ltd, LTM 30 Sep 2025, USD — **user-asserted**; buy-side. Data source: **upload** (data room). P&L, balance sheet, bridge, related parties accepted with limits; `monthly_profit_and_loss_36m_final.csv` **rejected** (shift rota). Earliest period: Oct 2022 |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps 1–3b | Done with a limit: statement level; two adjustments evidenced, one rejected, one unevidenced |
| Step 4 | Done with a limit: trend and seasonality only |
| Steps 5–7 | Done; capex split not done (no register) |
| Steps 8 | **Not done**: no forecast |
| Not done | Tie to ledger/TB, customer concentration, cut-off, payroll check, consolidation of the subsidiary |

Nothing was written to any system; output for the CFO only. **Data sources:** upload — `monthly_profit_and_loss_36m.csv`, `monthly_balance_sheet_36m.csv`, `management_adjusted_ebitda_bridge.csv`, `related_parties.md`.
