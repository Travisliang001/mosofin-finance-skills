# Intercompany reconciliation — Northbrook group — September 2025 (as at 30 September 2025)

Mosofin is not connected, so this run is manual: every step is `[manual]` and every figure comes from your uploads. Connecting Mosofin would read both ledgers in one batch ([docs.mosofin.com](https://docs.mosofin.com)).

## Read-back (Stage 1)

Reconciling intercompany balances (amounts the group companies owe each other) at **30 September 2025** between **Northbrook Trading Ltd** (USA, functional currency USD, parent) and **Northbrook UK Ltd** (England, GBP, 80% owned since 1 Mar 2019). Intercompany accounts: **2300 in the US books, 1300 in the UK books**. Group presentation currency: **USD**. Rates come **from your table** (source: "bank rate sheet"). Lines are matched at **each line's transaction-date rate**; balances are compared at the **closing rate of 1.27**. The group has **no other members** (per `group_structure.md`), so there is one pair. Intercompany agreement (F): **not supplied**, so pricing, mark-up and payment-term causes are **not assessed**. Date window: none needed, because every match below is on reference. Go-ahead assumed.

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Needed for | Verdict |
|---|---|---|---|---|---|
| `intercompany_ledger_northbrook_uk.csv` | UK intercompany ledger: 4 lines, 10 Jul – 29 Sep 2025, GBP **33,220.00**, all "Goods shipped / Management fee to US" | No entity named in the file. GBP agrees to UK functional currency | Yes. No opening-balance row, no settlements | Steps 1–3, UK side | **Accepted with a limit**: company user-asserted; taken as the full content of account 1300, with nil opening balance |
| `intercompany_ledger_northbrook_trading.csv` | US intercompany ledger: 3 lines, 10 Jul – 18 Sep 2025, USD **−38,000.00** (credits, i.e. payable) | No entity named. USD agrees | Yes, same limit | Steps 1–3, US side | **Accepted with a limit**: company user-asserted; taken as the full content of account 2300, with nil opening balance |
| `fx_rates.csv` | GBP/USD rate table: closing 1.27 (30 Sep), average 1.255, historical equity rate 1.31, and transaction rates for 10 Jul, 12 Aug, 18 Sep and 29 Sep | Covers the period; source stated | Yes | Step 5 | **Accepted** (rates and source are user-supplied) |
| `group_structure.md` | Group structure: two members, ownership, functional currencies, presentation currency | Names both companies; matches intake | Yes | Step 1 matrix | **Accepted** |
| `intercompany_ledger_northbrook_trading_final.csv` | **An employee shift rota** (E08–E10, weeks 1–4: days / nights / off), not a ledger despite its name | None | n/a | No step uses it | **Rejected.** If you have a later US intercompany ledger, upload it instead |

**Still missing:** the intercompany agreement (recommended). Also needed for eliminations: what Northbrook Trading still holds of the goods bought from the UK, and at what mark-up.

## Pair matrix (Step 1)

| Pair | Both sides uploaded? | Reconcilable? |
|---|---|---|
| Northbrook Trading Ltd ↔ Northbrook UK Ltd | Yes (2300 and 1300) | **Reconcilable**: one pair, N = 2 |

## Transaction matching (Step 2): every line matched on reference except IC-097

| Ref | Date | UK (GBP) | Rate (transaction) | UK in USD | US (USD) | Difference (UK − US) | Basis | Status |
|---|---|---:|---:|---:|---:|---:|---|---|
| IC-071 | 10 Jul | 9,450.00 | 1.2698 | 11,999.61 | 12,000.00 | −0.39 | Reference | Matched with difference |
| IC-082 | 12 Aug | 14,570.00 | 1.27 | 18,503.90 | 18,500.00 | +3.90 | Reference | Matched with difference |
| IC-093 | 18 Sep | 5,900.00 | 1.27 | 7,493.00 | 7,500.00 | −7.00 | Reference | Matched with difference |
| **IC-097** | **29 Sep** | **3,300.00** | 1.27 | **4,191.00** | — | **+4,191.00** | — | **Unmatched: on UK side only** |

The small differences are recorded rather than forced to zero. The US amounts imply rates of 1.26984, 1.26973 and 1.27119 against the bank sheet's 1.2698 / 1.27 / 1.27. **Probable cause:** the US side booked at a slightly different rate from the one on the sheet. This is a probable cause, not a confirmed one.

## Balance reconciliation (Step 3)

| | Amount |
|---|---:|
| UK receivable from US (1300): GBP 33,220.00 × closing 1.27 | **USD 42,189.40** |
| US payable to UK (2300) | **USD 38,000.00** |
| **Difference** | **USD 4,189.40** |
| of which **timing**: IC-097, goods shipped by UK on 29 Sep and not yet booked by US | 4,191.00 |
| of which **FX, closing vs transaction rate**: IC-071 (9,450 × (1.27 − 1.2698)) | 1.89 |
| of which **rate used by US differs from the sheet** (probable): −0.39 + 3.90 − 7.00 | −3.49 |
| **True mismatch identified** | **0.00** |

**IC-097 (GBP 3,300 / USD 4,191.00) is a cut-off item.** UK shipped on 29 Sep; the US books show nothing by 30 Sep. Probable cause: goods in transit, or one side missed posting. The US side should book it on receipt. If it never appears in October, it is a missed posting. On reference matching alone the two sides agree at **GBP 29,920.00**.

## Ageing and settlement (Step 6): proposal only

Nothing has been settled in three months. IC-071 is **82 days** old, IC-082 **49**, IC-093 **12** and IC-097 **1**. Payment terms are unknown because no agreement was supplied. **Proposed:** Northbrook Trading pays Northbrook UK the agreed items **GBP 29,920.00** (IC-071, 082, 093) once the three small rate differences are accepted. IC-097 follows once the US side has booked it. Settlement currency and date are for your treasury policy; I have not assumed either. The disputed differences are not settled.

## Eliminations (Step 7): consolidation-level, PROPOSED, NOT POSTED

| # | Entry | DR | CR |
|---|---|---:|---:|
| E1 | Eliminate agreed balances: DR US IC payable (2300) | 38,000.00 | |
| | CR UK IC receivable (1300), items 071/082/093 at closing rate | | 37,998.40 |
| | CR Difference carried explicitly (FX, to CTA (the currency translation reserve) pending agreement) | | 1.60 |
| E2 | Only if IC-097 is confirmed in transit: DR Goods in transit (consolidation) | 4,191.00 | |
| | CR UK IC receivable (1300), IC-097 | | 4,191.00 |

Both entries balance. Revenue and expense eliminations also apply: UK intercompany revenue of GBP 33,220, which is USD 42,187.51 at transaction rates, against the US management fee of 12,000 and goods of 26,000. **Unrealised profit in US inventory** cannot be computed without the US holdings and the mark-up. The 80% ownership affects the non-controlling interest, not the size of these eliminations, which remove 100%.

## What was not done, and why

- **Causes that need the agreement** (mark-up, pricing, payment terms, tax treatment): not assessed. Agreement not supplied.
- **Unrealised profit in inventory**: needs US inventory holdings and the mark-up.
- **Opening balances / ties to trial balance**: no TB for either company. Both ledgers are taken as complete from July with nil openings.
- **Manual journals posted direct to IC accounts**: none seen in the listings, but the listings show no entry type, so this check is limited.
- **Workpaper**: shown here as tables. Say if you want `IC_Reconciliation_2025-09.xlsx`.
- **Posting**: nothing has been posted, settled, sent or changed in either company's books.

## Coverage and provenance (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd (USD) and Northbrook UK Ltd (GBP), at 30 Sep 2025, presentation USD. Companies are **user-asserted**. Data source: **upload**. Files: both ledgers accepted with limit (company user-asserted, nil opening assumed); rates and group structure accepted; `intercompany_ledger_northbrook_trading_final.csv` **rejected** (shift rota) |
| Capability map | Not applicable: no connection. Every task is `[manual]`, per pair: Trading ↔ UK. |
| Steps | 0 n/a (upload); 1 done; 2 done, all on reference; 3 done, split timing / FX / rate; 4 done, causes probable; agreement-based causes not assessed; 5 done at user rates; 6 proposed; 7 proposed, inventory profit **not done**; 8 tables in chat |
| Not done | TB tie, opening balances, unrealised profit, agreement-based causes. These need both trial balances, the US inventory listing and the IC agreement |
| Parameters | Transaction rates per line, closing rate 1.27 for balances; matching on reference; no date window or amount tolerance used |

**Data sources:** UK and US intercompany ledgers, rate table and group structure, all supplied by you; no ledger read through any connection.
