# Currency translation — Northbrook UK Ltd (GBP) into USD — 30 September 2025

Mosofin is not connected, so this run is manual: every figure comes from your uploads and every step is `[manual]`. (Connecting Mosofin would read each entity's trial balance in its own currency: [docs.mosofin.com](https://docs.mosofin.com).) Everything below is a **proposal**; nothing is posted.

## Read-back

Translating **Northbrook UK Ltd** from **GBP** into **USD** (the presentation currency of **Northbrook Trading Ltd**, the parent) at **30 September 2025**, from **your uploads**, at the **rates you supplied, sourced from "bank rate sheet"**. Functional currency **GBP**, as you stated. **No intercompany loans**; the intercompany balance is **trading** (to be settled). **No hyperinflation**. UK is **80% owned** since 1 March 2019, so the translation adjustment is split with the 20% non-controlling interest. Shall I go ahead?

Notes: the intake names Northbrook Trading Ltd; the trial balance is the UK subsidiary's. The group structure names the UK entity as in scope, so I accept it for that company. The ownership, the opening balances and the trading designation come from `group_structure.md` and count as answered once you confirm.

## Validation of the uploads (shown before any work — I would wait for your answer here)

| File | What it actually is | Company / currency / date | Usable? | Step that uses it | Verdict |
|---|---|---|---|---|---|
| `trial_balance_northbrook_uk_2025-09-30.csv` | Trial balance, 10 accounts, balance sheet and nine-month P&L | Entity and currency not named in the file (name only); taken as Northbrook UK Ltd, GBP, 30 Sep 2025 | Debits = credits = 603,520; net assets 187,420 = share capital 100,000 + retained earnings 52,420 + profit 35,000 | Steps 1, 3, 3b | **Accepted with a limit:** company, currency and date user-asserted |
| `fx_rates.csv` | Rate table: GBP/USD closing (30 Sep 2025, 31 Dec 2024), average (1 Jan–30 Sep 2025), historical (share capital, 1 Mar 2019), four transaction-date rates | GBP/USD, dated, each with a source | Source given for every rate; **no approver** for any | Steps 3, 3b | **Accepted with a limit:** rate approver missing. The four transaction-date rates are not used by any step here (no dividends or capital movements); set aside |
| `group_structure.md` | Group chart, ownership, investment at cost, and last year's translated balances | Northbrook group, 31 Dec 2024 and 2025 | Summary figures, not the prior-year translated TB | Steps 3 (opening retained earnings), 3b (opening CTA), 4 | **Accepted with a limit:** prior-period figures are a **summary**, user-supplied, not evidenced by last year's workpaper |
| `trial_balance_northbrook_uk_2025-09-30_final.csv` | **Not a trial balance.** A staff shift rota (E08–E10, days / nights / off) | No entity, currency or money | Nothing relevant | None | **Rejected:** the content is a rota, whatever the name says |

**Still missing:** (1) the **parent's side of the intercompany balance** (Northbrook Trading Ltd's payable to UK, with its currency of denomination) to test the pair before translation; (2) **who approved** each rate; (3) a **monthly P&L** for the UK entity, to test whether the simple average rate is safe; (4) recommended: last year's translated TB to evidence the 66,059 and 6,077 brought forward.

*Proceeding as if you answered "go ahead with the accepted files".*

## Step 1 — Functional currency

Your answer: GBP. The evidence available agrees: the books are kept in GBP, revenue, costs, bank and payables are all GBP-denominated as far as the TB shows, and the entity is not funded by a loan from the parent. Home currency (GBP) = functional currency (GBP): no remeasurement layer before translation. **One open point:** the denomination of the 33,220 intercompany receivable. If it is invoiced in USD, it is a foreign-currency monetary item in the UK books and must be remeasured to GBP first, with the difference in UK earnings.

## Step 3 — Translation (rates: closing 1.2700, average 1.2550, historical 1.3100)

| Account | GBP | Rate | USD |
|---|---|---|---|
| Bank | 84,200 | closing 1.27 | 106,934.00 |
| Accounts receivable | 61,300 | closing 1.27 | 77,851.00 |
| Intercompany receivable — Northbrook Trading | 33,220 | closing 1.27 | 42,189.40 |
| Inventory | 47,800 | closing 1.27 | 60,706.00 |
| Accounts payable | (39,100) | closing 1.27 | (49,657.00) |
| **Net assets** | **187,420** | | **238,023.40** |
| Share capital | 100,000 | historical 1.31 | 131,000.00 |
| Retained earnings b/f | 52,420 | as translated at 31 Dec 2024 | 66,059.00 |
| Sales revenue | 412,000 | average 1.255 | 517,060.00 |
| Cost of goods sold | (251,000) | average 1.255 | (315,005.00) |
| Operating expenses | (126,000) | average 1.255 | (158,130.00) |
| Profit for the nine months | 35,000 | | 43,925.00 |
| **CTA (balancing figure), closing** | | | **(2,960.60) debit** |

Translated TB foots: debits = credits = 763,776.00. **That it balances proves nothing** — the CTA would absorb a wrong rate.

## Step 3b — Proof of the CTA, independently of the plug

| | USD |
|---|---|
| Opening CTA (31 Dec 2024, debit) | (6,077.00) |
| Opening net assets 152,420 × (1.2700 − 1.2530) | +2,591.14 |
| Profit 35,000 × (1.2700 − 1.2550) | +525.00 |
| Dividends / capital movements | 0 (none in 2025) |
| **Expected closing CTA** | **(2,960.86) debit** |
| Plugged CTA | (2,960.60) debit |
| **Difference** | **0.26** |

The 0.26 is explained: last year's net assets were carried at 190,982, but 152,420 × 1.2530 = 190,982.26, so the brought-forward CTA was rounded by 0.26. **The CTA is proved.** Movement in the period: **3,116.14 credit to OCI** (100% basis).

Split with the non-controlling interest (20%): closing CTA group share **(2,368.48)**, NCI **(592.12)**; period movement group **2,492.91**, NCI **623.23**. Net assets attributable to NCI at closing rate: 47,604.68.

Average-rate check: no monthly P&L was supplied, so seasonality could not be tested. The transaction-date rates in Jul–Sep (1.2698–1.2700) sit close to the closing rate and above the 1.2550 average; if UK earnings are weighted to later months, the simple average understates translated profit. Stated as a limit, not adjusted.

## Step 4 — Intercompany

Trading balance, expected to be settled → any FX difference on it goes to **earnings**, not CTA. UK side: 33,220 GBP = **42,189.40 USD** at closing. **The parent's side was not uploaded**, so the pre-translation match cannot be tested; the elimination must wait for it. Translate first, then eliminate.

Investment check: 104,800 USD = 80% × 100,000 GBP × 1.3100 = 80% × 131,000. Agrees.

## Step 5 — Proposed entries (consolidation, not posted)

```
DR  Cumulative translation adjustment (OCI, group)    2,368.48  closing balance, group share
DR  Non-controlling interest                            592.12  closing balance, NCI share
    CR  Translation balancing (consolidation worksheet)        2,960.60
```
Period movement to OCI: credit 3,116.14 (group 2,492.91, NCI 623.23). Account names to be taken from the group chart. No remeasurement entry is proposed unless the intercompany receivable proves to be USD-denominated.

## Step 6 — Controls

Rate source: "bank rate sheet" for every rate — **approver not recorded** (open). Completeness: all 10 accounts classified and translated. Classification (for remeasurement): monetary — bank, AR, intercompany receivable, AP; nonmonetary — inventory. CTA proof: run above, owner to be named.

## Not done, and why

Intercompany match and elimination (parent side not uploaded); seasonality test of the average rate (no monthly P&L); rate approvals (not supplied); tie-out to the consolidation (other entity not in this run). I would ask before creating `FX_Translation_2025-09_Northbrook UK Ltd.xlsx`. Nothing was posted or changed.

## Coverage sheet (manual run)

| Section | Entry |
|---|---|
| Environment | Northbrook UK Ltd, GBP functional, into USD for Northbrook Trading Ltd, 30 Sep 2025 — user-asserted; source: upload (Mosofin not used, by choice) |
| Files | UK TB accepted with limit; rates accepted with limit (no approver); group structure accepted with limit (summary); `_final.csv` rejected (shift rota) |
| Capability map | Not applicable: no connection. Every task is `[manual]`. |
| Steps | 1 done (functional GBP, IC denomination open); 2 not needed unless IC is USD; 3 done; 3b done, difference 0.26 explained; 4 done with limit; 5 proposals; 6 done with limit |
| Not done | Intercompany pair; monthly average-rate test; rate approval; consolidation tie-out |

**Data sources:** uploads — `trial_balance_northbrook_uk_2025-09-30.csv` (GBP), `fx_rates.csv` (bank rate sheet), `group_structure.md` (user-supplied prior-year figures).
