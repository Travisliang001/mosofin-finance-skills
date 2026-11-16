# Currency translation — Northbrook UK Ltd into USD, 30 September 2025 (upload path)

Mosofin is not connected for this run (you chose upload only), so every step is `[manual]` and works from your files. Connecting Mosofin would automate the reads — docs.mosofin.com. Nothing was posted: the translation and every entry below are **proposals**. No rate came from me; every rate is yours, from your file.

## (a) Read-back

Translating **Northbrook UK Ltd** from **GBP** into **USD** (the group's reporting currency; parent **Northbrook Trading Ltd**) at **30 September 2025**, from your uploads, at the **rates in `fx_rates.csv`, sourced from your bank rate sheet**. Functional currency **GBP** (your intake answer; `group_structure.md` agrees). **No intercompany loans; no hyperinflation** (your answers). From `group_structure.md`, to confirm: UK is **80% owned since 1 March 2019**, no acquisitions or disposals in 2025 — this makes a **non-controlling interest** (the 20% owned by outsiders) part of the work.

Assumptions (not answered, no default stated): the intercompany receivable is a **trading balance expected to be settled** (not a loan, per your answer), so any FX on it belongs in earnings, not CTA; the simple average rate supplied is used, because no monthly P&L was uploaded to test seasonality.

## (b) Validation of the upload — shown before any work

| File | What it actually is | Company / currency / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `trial_balance_northbrook_uk_2025-09-30.csv` | Trial balance, 10 accounts | Entity only in the file name; no currency or date in the content | Foots: DR = CR = 603,520. P&L open (YTD): profit 35,000 GBP. Net assets 187,420 = share capital 100,000 + RE 52,420 + profit 35,000 | Yes — Steps 1–3b | **Accepted with a limit: entity, GBP and 30 Sep 2025 user-asserted** |
| `fx_rates.csv` | Rate table, 7 GBP/USD rates with type, date and source | Closing 30 Sep 2025 1.27; average 1 Jan–30 Sep 2025 1.255; historical (equity) 1 Mar 2019 1.31; four transaction-date rates | Yes, source and date on every row; **no approver**; **no opening rate at 31 Dec 2024**; the four transaction rates (10 Jul, 12 Aug, 18 Sep, 29 Sep) match no transaction in any file | Yes — Step 3, Step 6 rate control | **Accepted with a limit**: transaction rates set aside (nothing to apply them to); no approver recorded |
| `group_structure.md` | Group summary: parent USD, UK GBP, 80% owned since 1 Mar 2019, presentation USD | Matches intake | Yes; a summary, so ownership and dates are **user-supplied, not evidenced** | Yes — NCI split, historical-rate date (Step 1, "Both entity scenarios") | **Accepted with a limit**: facts used once you confirm them in the read-back |
| `trial_balance_northbrook_uk_2025-09-30_final.csv` | **Not a trial balance.** A staff shift rota: employee E08–E10, week_1…week_4, "nights/days/off" | No entity, accounts or amounts | No | No step | **Rejected** on content despite the name. Not used. |

**Still missing — required for the CTA proof:** the **prior-period translated balances and the opening CTA** (31 Dec 2024), and the **31 Dec 2024 closing rate**; **historical rates for retained earnings** (RE built up after 2019 at many rates). Also needed: the **parent's side of the intercompany balance** (Northbrook Trading's TB) and its **currency of denomination**; **who approved the rates**; a **monthly P&L** for the seasonality test.

*I would stop here and wait for your answer. Assumed answer: "go ahead with the accepted files".*

## (c) Translation (GBP → USD)

| Account | GBP | Rate | Rate type | USD |
|---|---:|---:|---|---:|
| 1000 Bank | 84,200 | 1.27 | closing (monetary) | 106,934.00 |
| 1100 Accounts receivable | 61,300 | 1.27 | closing (monetary) | 77,851.00 |
| 1300 Intercompany receivable – Northbrook Trading | 33,220 | 1.27 | closing (monetary) | 42,189.40 |
| 1200 Inventory | 47,800 | 1.27 | closing (nonmonetary; closing is right for translation) | 60,706.00 |
| 2000 Accounts payable | (39,100) | 1.27 | closing (monetary) | (49,657.00) |
| **Net assets** | **187,420** | | | **238,023.40** |
| 3000 Share capital | 100,000 | 1.31 | historical, 1 Mar 2019 | 131,000.00 |
| 3100 Retained earnings (opening) | 52,420 | **1.31 — approximation** | historical; true rates not supplied | 68,670.20 |
| 4000 Revenue | 412,000 | 1.255 | average | 517,060.00 |
| 5000 Cost of goods sold | (251,000) | 1.255 | average | (315,005.00) |
| 6000 Operating expenses | (126,000) | 1.255 | average | (158,130.00) |
| **Profit for the period** | **35,000** | | | **43,925.00** |
| **CTA (balancing figure)** | | | | **(5,571.80)** |

All 10 accounts classified; none defaulted to a rate. **The retained-earnings rate is an approximation**: I applied the only historical rate you gave (1.31, the acquisition date) to all 52,420 GBP of retained earnings. That is almost certainly wrong for profits earned in 2019–2024, and every cent of the error lands in CTA.

## (d) Findings

1. **CTA cannot yet be proved.** The independent proof needs opening net assets × (closing − opening rate); there is **no 31 Dec 2024 rate and no opening CTA**. The only part I can prove is this year's profit term: **35,000 × (1.27 − 1.255) = +525.00**. Rebuilding cumulative CTA from the historical rates (−4,000.00 on share capital, −2,096.80 on RE at 1.31, +525.00 on profit = −5,571.80) **agrees with the plug only because it uses the same rates**; it is not independent. Status: **plug −5,571.80, unproved**.
2. **Sensitivity to the RE rate:** if RE were wrongly carried at the closing rate, CTA would be −3,475.00 — a 2,096.80 swing that would still balance. This is exactly what the proof exists to catch.
3. **Non-controlling interest (20%).** CTA splits **group −4,457.44 / NCI −1,114.36**; profit splits group 35,140.00 / NCI 8,785.00; NCI's share of net assets is 47,604.68. Both equity lines are misstated if the split is skipped.
4. **Intercompany receivable GBP 33,220 (USD 42,189.40 at closing).** Your answer was "no intercompany loans", so I treat it as a trading balance expected to settle: FX on it goes to **earnings**, not CTA. The pre-translation agreement with the parent's payable **could not be checked** — the parent's TB was not uploaded. Its currency of denomination is unknown; if it is USD, the UK entity must **remeasure** it into GBP first, with the gain or loss in UK profit.
5. **Remeasurement (Step 2):** no other non-GBP balances or transactions are visible in the TB; the four transaction-date rates have nothing to attach to. Done with that limit.
6. **Rates control:** source and date present on every rate; **no approver**. The closing (1.27) and the September transaction rates (1.27) agree; the average 1.255 is below closing, so profit translates lower than it would at spot.

**Proposed entry (not posted), in the consolidation:** record CTA of **(5,571.80)** to OCI / accumulated other comprehensive income — group (4,457.44), NCI (1,114.36) — **held until the proof in Finding 1 can run.** No remeasurement entry proposed until the intercompany currency is known.

## (e) Not done, and why

CTA proof (opening rate, opening CTA, translated prior balances missing); RE historical rates (not supplied — approximation used and flagged); intercompany pre-translation match (parent TB missing); seasonality test (no monthly P&L); tie to consolidation (hand-off to `consolidation-and-eliminations`; translate first, then eliminate). No `.xlsx` created — I would ask whether you want `FX_Translation_2025-09_Northbrook Trading Ltd.xlsx`.

## (f) Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook UK Ltd (GBP) into USD for Northbrook Trading Ltd, 30 Sep 2025 — user-asserted. Source: upload. TB, rates, group structure accepted with limits; `_final` TB rejected (staff rota). |
| Capability map | Not applicable: no connection. Every task is `[manual]`. |
| Steps | 0 inputs read · 1 functional currency GBP, user-asserted (no P&L/vendor evidence to test the four factors) · 2 remeasurement done with limit · 3 translation done; RE rate approximated · 3b CTA proof **not done** (profit term only) · 4 intercompany **not done** pre-translation · 5 CTA entry proposed, held · 6 controls: rate source yes, approver **missing**, completeness 10/10 accounts · 6b tables in chat · 7 not offered. |
| Not done | CTA proof (upload Dec-2024 translated balances, opening CTA, Dec-2024 rate); RE rates; parent's intercompany side; rate approver. |

**Data sources:** user uploads — `trial_balance_northbrook_uk_2025-09-30.csv`, `fx_rates.csv`, `group_structure.md`.
