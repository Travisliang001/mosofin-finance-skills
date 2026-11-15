# Digital assets — Northbrook Trading Ltd — 30 September 2025

Mosofin is not connected, so this run is manual: every step is `[manual]` and every figure comes from your uploads. Connecting Mosofin would let the cash legs to and from the exchange be read from the books and swept for completeness ([docs.mosofin.com](https://docs.mosofin.com)).

**No price was supplied by me, no tax treatment is given, and nothing was posted.** Every entry below is a proposal.

## Read-back

Accounting for **bitcoin (BTC) and USD Coin (USDC)** held by **Northbrook Trading Ltd** (user-asserted) at **30 September 2025**, currency **USD**, under **US GAAP** (your answer), from the exchange export you uploaded. Held as an **investment**, in **exchange custody**; disposals on **FIFO** (first in, first out). Prices: the **exchange's closing price on 30 Sep 2025**, as it appears inside the export (a fact that arrived inside a file; used once you confirm it here). Not confirmed, and not asserted from memory: **whether ASU 2023-08 (fair value through net income) is adopted and applies at 30 Sep 2025**, the **exchange's name** and whether it is the principal market, the **timestamp** of the closing price, and **USDC's redemption rights**. Go-ahead assumed.

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Needed for | Verdict |
|---|---|---|---|---|---|
| `exchange_export_2025.csv` | Exchange transaction export: 4 trades (BTC buy 1.5 for 63,000 on 10 Feb; buy 0.5 for 26,000 on 20 May; sell 0.4 for 22,800 on 4 Aug; USDC buy 50,000 for 50,000 on 1 Jun) plus two 30 Sep closing-price rows (BTC 58,000, USDC 1.00) | No entity or exchange named; USD; Feb–Sep 2025 | Yes; **no fees column**, **no balance-as-at statement**, price rows have a date but no time and an unnamed venue | Steps 1–4, 6 | **Accepted with a limit**: company user-asserted; holdings are **derived from trades, not evidenced by a custodian balance statement**, so existence is not proven; prices are user-supplied with no venue name or timestamp |
| `trial_balance_2025-09-30.csv` | Trial balance at 30 Sep 2025, 29 accounts; debits 6,589,681 = credits 6,589,681 | As at 30 Sep 2025; no entity named | Yes | Step 0 (what is recorded), Step 0b | **Accepted with a limit**: company user-asserted |
| `exchange_export_2025_final.csv` | **An employee shift rota** (E08–E10, weeks 1–4). Not an exchange export despite its name | None | n/a | No step uses it | **Rejected.** If a final exchange export exists, please upload it in its place |

**Still missing:** an **exchange balance statement at 30 Sep 2025** (existence); the **exchange's name** and a **timestamped price** from the principal market; **confirmation of the standard** in force for your year (ASU 2023-08 adoption); **USDC redemption terms**; **ledger detail** for the bank account (to find where the fiat legs were booked); any **fees**.

*I would wait here for your answer; proceeding with the accepted files as instructed.*

## Findings

**1. The holdings are not in the books (Step 0b, completeness).** The trial balance has **no digital asset account and no crypto gain or loss account**. Yet the export shows **139,000** paid to the exchange (63,000 + 26,000 + 50,000) and **22,800** received back — **net 116,200** of fiat that bought assets the ledger does not show. Question for you: where were these cash legs booked (an expense, a suspense account, or not at all)? The bank ledger detail would answer it. Cash to an exchange is a transfer, not proof of what was bought; the quantities come from the export.

**2. Holdings at 30 Sep 2025, derived from the export (Step 1, inventory).** BTC **1.6** (1.5 + 0.5 − 0.4); USDC **50,000**. Supplied, not read; as-at date 30 Sep 2025 by derivation only — no balance statement.

**3. Classification (Step 1).** BTC: fungible, on a public blockchain, not your own — appears to meet the ASU 2023-08 scope criteria, **subject to your confirming the standard applies at this date**. USDC: **not automatically cash**. If you hold a right to redeem at par with the issuer, it is a claim on the issuer and may fall outside ASU 2023-08's scope; its accounting follows that claim. Needs the redemption terms. At 1.00 it carries at **50,000** on either reading.

**4. FIFO cost and the August sale (Steps 2, 4).**

| Lot | Quantity | Cost | Per BTC |
|---|---:|---:|---:|
| 10 Feb 2025 | 1.5 | 63,000 | 42,000 |
| 20 May 2025 | 0.5 | 26,000 | 52,000 |
| Sold 4 Aug, FIFO from lot 1 | −0.4 | −16,800 | 42,000 |
| **Remaining** | **1.6** | **72,200** | (1.1 @ 42,000 + 0.5 @ 52,000) |

Proceeds 22,800 (57,000 per BTC) − FIFO cost 16,800 = **realised gain 6,000**. Fees: none in the export; if any were charged they change both cost and gain.

**5. Measurement at 30 Sep — shown under each answer, since the standard is unconfirmed (Steps 3, 6).**

| | ASU 2023-08 applies (fair value) | ASU 2023-08 does not apply (cost less impairment) |
|---|---:|---:|
| BTC carrying amount | 1.6 × 58,000 = **92,800** | 72,200 less any impairment |
| Unrealised gain in net income | **20,600** | none; impairment to the **lowest price during the period**, no reversal |
| Realised gain on sale | 6,000 | 6,000 (if lot 1 was never impaired) |
| USDC | 50,000 | 50,000 |

Under the cost model **impairment cannot be concluded**: only a closing price was supplied, and the rule needs a **price series** for the whole period. Fair value is Level 1 only if the exchange is the principal market and the quote is timestamped — neither is confirmed.

**6. Proposed entries — proposals only; account names are new, since your chart has none (Step 4).** On the fair-value answer; the fiat side is "Operating Bank Account" only if that is where the cash went (finding 1).

```
DR Digital assets – BTC        63,000 / 26,000   CR Bank (10 Feb / 20 May purchases)
DR Digital assets – USDC       50,000            CR Bank (1 Jun)          [classification to confirm]
DR Bank                        22,800            CR Digital assets – BTC 16,800; CR Gain on digital assets 6,000 (4 Aug)
DR Digital assets – BTC        20,600            CR Gain on remeasurement of digital assets (net income) 20,600 (30 Sep)
```

If the cash legs were already expensed or parked elsewhere, the purchase entries become reclassifications from that account instead.

**7. Custody (Step 5).** Exchange custody: you may hold a **claim against the exchange** rather than the asset itself, with counterparty risk. Disclose the custodian and the concentration (all holdings at one unnamed exchange).

**8. Disclosures (Step 7).** Description and purpose (investment); policy (framework and model, once confirmed); carrying amount 92,800 BTC + 50,000 USDC on the fair-value answer; activity: purchases 89,000 BTC and 50,000 USDC, sale proceeds 22,800, gains 6,000 realised and 20,600 unrealised; custody risk; under ASU 2023-08 a reconciliation by significant holding. Current requirements to be confirmed.

## Open items for a specialist or for you

Standard and ASU 2023-08 adoption confirmation (date it was confirmed: **not yet**) · USDC redemption rights · exchange name, principal market, timestamped prices · exchange balance statement · where the fiat legs were booked · **tax treatment: not addressed here — refer to a tax specialist**.

## Coverage sheet (manual run)

**Environment:** Northbrook Trading Ltd, 30 Sep 2025, USD — user-asserted. Data source: upload (gateway absent). Export and trial balance accepted with limits; `exchange_export_2025_final.csv` rejected (shift rota). **Capability map:** Not applicable: no connection. Every task is `[manual]`.

| Step | Status | Gap |
|---|---|---|
| 0 Evidence | Done with a limit | No bank detail |
| 0b Completeness | Done on the trial balance: **no crypto accounts found** | Bank ledger needed to trace 116,200 net |
| 1 Classify | Done with a limit | Standard and USDC terms unconfirmed |
| 2–4 Measure, FIFO, entries | Done; both models shown | Fees, price venue/time |
| 5 Custody | Done with a limit | Exchange unnamed |
| 6 Impairment | **Not done** (cost model) | Price series |
| 7 Disclosures | Drafted | Current requirements |
| 8 Output | Tables in chat | `Crypto_Accounting_2025-09_Northbrook Trading Ltd.xlsx` only on a yes |
| 9 Save | Not done | Offered only after approval |

**Data sources:** user uploads — `exchange_export_2025.csv` (trades and 30 Sep closing prices), `trial_balance_2025-09-30.csv`. No price was supplied from memory. Nothing was posted, sent or changed.
