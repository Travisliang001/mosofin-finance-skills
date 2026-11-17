# Transfer pricing analysis — Northbrook group (Northbrook Trading Ltd, USA / Northbrook UK Ltd, England) — 2025

Mosofin is not connected, so this run is manual: every step is `[manual]` and every figure comes from your uploads. **This is analysis for a qualified transfer pricing specialist to review, not tax advice.** No method is selected, no price is concluded to be arm's length, nothing is adjusted or filed.

## Read-back

Preparing **2025** transfer pricing analysis for **Northbrook Trading Ltd** (USA, USD, parent) and **Northbrook UK Ltd** (England, GBP, 80% owned), as described in `group_structure.md`. Two transaction types: **goods** (UK → US, cost plus 8%) and a **management fee** (UK → US). Functional description and comparables as you supplied them. Data source: **upload only**. Figures to 30 September 2025.

| Intake question | Treatment |
|---|---|
| B — group, year, entities | Answered: two entities, 2025. The 20% minority holder of the UK company is outside the group. |
| C — documentation requirements | One **sample rule** supplied: local file where intercompany transactions exceed 250,000 a year (currency not stated). No deadlines or jurisdiction source. |
| D — functions, assets, risks | Answered in `transfer_pricing_inputs.md` (UK = contract manufacturer to US specification, little inventory, no market risk; US owns designs). Corroborated below — it does not fully hold. |
| E — agreements | Goods: agreement dated 1 Jan 2022 (not uploaded — terms as you summarised). Management fee: **no written agreement**. |
| F — comparables / prior documentation | Comparables: user's database extract, 5 contract manufacturers, IQR mark-up on total cost **5.5%–9.5%**, **2024 data**. Prior documentation: not supplied. |
| Group IP | Not asked in the inputs: does the UK company use the group's designs or brand for its own third-party sales, and does it pay for them? |

## Upload validation (shown before any work)

| File | What it actually is | Entity / period | Usable? | Step that uses it | Verdict |
|---|---|---|---|---|---|
| `group_structure.md` | Group structure, ownership, currencies, 2024 consolidation facts | Group, at 2025 | Yes | Steps 1, 7 | **Accepted** |
| `transfer_pricing_inputs.md` | Functional summary, pricing terms, comparable range, sample doc rule | 2025 (comparables 2024) | Yes — a summary, not the agreement or the database study | Steps 2, 3–6, 7, 8 | **Accepted with a limit**: user-supplied, not evidenced; agreement itself not uploaded |
| `intercompany_ledger_northbrook_trading.csv` | US intercompany ledger, 3 entries, **Jul–Sep 2025**, total **38,000 USD** | Northbrook Trading, Q3 2025 | Yes | Steps 1, 8 | **Accepted with a limit**: one quarter only |
| `intercompany_ledger_northbrook_uk.csv` | UK intercompany ledger, 4 entries, **Jul–Sep 2025**, total **33,220 GBP** | Northbrook UK, Q3 2025 | Yes | Steps 1, 8 | **Accepted with a limit**: one quarter only |
| `trial_balance_northbrook_uk_2025-09-30.csv` | UK TB, 10 accounts, Dr = Cr 653,520; revenue 412,000, COGS 251,000, opex 126,000 (GBP, YTD) | Northbrook UK, 30 Sep 2025 | Yes — no split of IC vs third-party revenue | Steps 2b, 4, 6, 6b | **Accepted with a limit**: entity-level only, so PLIs are proxies |
| `transfer_pricing_inputs_final.csv` | **Not TP inputs.** A staff shift rota (E08–E10, weeks 1–4) | n/a | No | None | **Rejected** on content. |

**Still missing:** intercompany ledgers for **Jan–Jun 2025** (and Q4 when available) — required for the annual inventory and the 250,000 test; the goods agreement itself; the UK revenue split (intercompany vs third party) and the cost base of intercompany goods (to test cost plus 8%); the US trial balance; the comparable study itself; documentation deadlines. I would wait for your answer here; proceeding on the accepted files.

## Step 1 — Transaction inventory (Q3 2025)

| Ref | Date | Type | Direction | US side (USD) | UK side (GBP) | Both sides? | Agreement? |
|---|---|---|---|---:|---:|---|---|
| IC-071 | 10 Jul | Management fee | UK → US | 12,000 | 9,450 | Yes | **No written agreement** |
| IC-082 | 12 Aug | Goods | UK → US | 18,500 | 14,570 | Yes | Yes (1 Jan 2022, not seen) |
| IC-093 | 18 Sep | Goods | UK → US | 7,500 | 5,900 | Yes | Yes |
| **IC-097** | **29 Sep** | Goods | UK → US | **—** | **3,300** | **UK only** | Yes |
| **Total** | | | | **38,000** | **33,220** | | |

**Reconciliation.** The UK intercompany receivable (TB 1300) is 33,220 GBP = the four UK entries. The US side holds 38,000 USD. At the rate implied by the matched entries (38,000 / 29,920 = 1.2701), the UK balance is **42,191 USD**, so the **US side is short 4,191 USD — exactly IC-097 (3,300 GBP × 1.2701)**, shipped 29 Sep and not recorded by the US at 30 Sep: goods in transit or a cutoff error. Matched pairs imply GBP/USD 1.2698–1.2712.

## Step 2b — Does the characterisation hold? (questions, not conclusions)

| Assertion | What the UK numbers show (GBP, 9 months) |
|---|---|
| "Manufactures to Northbrook Trading's specification" | Revenue 412,000, but intercompany goods in Q3 are only 23,770 — about **6%** of 9-month revenue even if Q3 were repeated three times (~17%). **Most UK revenue appears to be third-party sales.** |
| "Holds little inventory" | Inventory **47,800** = ~**52 days** of COGS (47,800 / 251,000 × 273). |
| "Bears no market risk" | Third-party receivables **61,300** (~41 days of revenue) — credit and market risk on independent customers. |

If the UK sells mainly to independents, it is not a captive contract manufacturer, its entity-level margin mixes two businesses, and those third-party sales may be an **internal CUP** for the goods it sells to the US (same product to independents). Please supply the revenue split.

**Management fee direction.** A 12,000-a-quarter fee charged by the UK (described as the low-function manufacturer) **to** the US parent, with no agreement, needs a benefit test: what service does the UK render to the parent? Only one quarterly charge is visible (Q3); 48,000 a year if charged every quarter.

## Step 4 — Northbrook UK PLIs (entity-level proxy, 9 months to 30 Sep 2025, single year)

| PLI | Computation | Result |
|---|---|---:|
| Mark-up on total costs | 35,000 / 377,000 | **9.28%** |
| Operating margin | 35,000 / 412,000 | 8.50% |
| Berry ratio | 161,000 / 126,000 | 1.28 |
| Return on assets | 35,000 / 226,520 | 15.5% |

## Step 6 — Comparison to the supplied range (not a conclusion)

- Entity-level mark-up **9.28%** sits **inside** the supplied IQR **5.5%–9.5%**, near the top (0.22 points below the upper quartile).
- It is a **proxy**: it blends third-party sales and possibly the management-fee income. If the Q3 fee (9,450) sits in revenue, excluding just that quarter gives 6.78%.
- The **stated price** (cost + 8%) is inside the range; the **realised** mark-up on intercompany goods cannot be computed without the cost of the goods shipped.
- Comparables are 2024 data against 2025 results; single year; no working-capital adjustment (comparables' days not supplied).
- **Step 6b loss test:** UK profitable in 2025 YTD (35,000 GBP). Other years not supplied.

## Step 7 — Documentation tier (sample rule)

Q3 intercompany flows ≈ 42,191 USD both sides. Whether the year exceeds **250,000** cannot be determined from one quarter; the rule's currency is also not stated. If Q3 is typical the annual total would be ~170,000 USD — below the threshold — but that is an extrapolation, not a finding. No CbCR threshold supplied.

## Step 8 — Conduct vs contract

- Management fee: **flow with no agreement**.
- Goods: agreement says cost + 8%; conduct cannot be tested (no cost base per shipment).
- IC-097 recorded on one side only.
- Balance unsettled for the whole quarter; group structure calls it trading, not a loan — if it stays open, it becomes an interest-free financing question.

## Not done, and why

- Method selection, tested party, arm's-length conclusion, adjustment — specialist's.
- Annual inventory and the 250,000 test — Q1–Q2 ledgers missing.
- Realised goods mark-up, internal CUP test — need revenue split and goods cost base.
- Excel workpaper / Word report — would ask before creating `Transfer_Pricing_England_2025_Northbrook_UK_Ltd`.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd (USA) and Northbrook UK Ltd (England, 80%), user-asserted from the structure file; year 2025, Q3 flows; UK TB 9 months. Data source: upload. 5 files accepted (4 with limits), 1 rejected (staff rota). Flows read from both sides except IC-097 (UK only). |
| Capability map | Not applicable: no connection. Every task is `[manual]`. |
| Steps | 1 done for Q3; 2 user-supplied; 2b done; 3 not done (specialist); 4 done, proxy; 5 range user-supplied; 6 comparison done, no conclusion; 6b one year; 7 partial; 8 done; 9 tables in chat. |
| Unknowns | IC-097 cutoff; management-fee agreement and benefit; UK third-party sales vs characterisation; group IP use; Q1–Q2 flows; deadlines. |
| Parameters | PLI on UK entity totals, GBP; FX implied 1.2701 from matched pairs; IQR 5.5%–9.5% (2024, user extract); doc threshold 250,000 (sample). |
