# Credit review — Harlow Fabrication Ltd — customer of Northbrook Trading Ltd — 30 September 2025

Mosofin is not connected, so this run is manual: every step is `[manual]` and every figure comes from your uploads. Connecting Mosofin would let the full trading history, credit notes, write-offs and vendor records be read from the books ([docs.mosofin.com](https://docs.mosofin.com)).

**This is a recommendation for the credit function. No limit was set, no hold placed and no terms changed. No sanctions screening was done.**

## Read-back

Reviewing the credit limit for **Harlow Fabrication Ltd** (legal entity as named), a customer of **Northbrook Trading Ltd** (user-asserted), as at **30 Sep 2025**, currency **USD** (user-asserted), from your uploads. From `credit_request_and_policy.md` (facts that arrived inside a file; used once you confirm them here): requested **net 45**, about **40,000 a month**, current limit **200,000**; the customer's **own accounts to Dec 2024**, supplied by the customer (no auditor named); **no bureau report, no trade references, no credit insurance**; policy tier ceilings **50,000 / 150,000 / 300,000**, concentration cap **25% of receivables**, limits above **150,000** need the **finance director**. Assumption: the three ceilings map to tiers **C / B / A**; tier D gets no open credit. Go-ahead assumed.

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Needed for | Verdict |
|---|---|---|---|---|---|
| `customer_payment_history_12m.csv` | Paid-invoice history, 60 invoices for 12 customers (5 each), Oct 2024 – Sep 2025, with paid date and days-to-pay (recomputed: all 60 agree) | No entity or currency | Yes; paid invoices only — no credit notes, write-offs or open items | Step 2b (days-to-pay, trend, volume) | **Accepted with a limit**: company user-asserted; 12 months only, so peak exposure before Oct 2024 is unknown |
| `ar_aging_detail_2025-09-30.csv` | Open-item receivables ageing, whole ledger, 14 lines, 12 customers, total **798,360** (incl. one credit note −2,150) | As at 30 Sep 2025; no entity or currency | Yes; days overdue recomputed and agree | Step 2b (exposure), concentration | **Accepted with a limit**: company user-asserted |
| `credit_request_and_policy.md` | Credit request, the customer's summary accounts, and Northbrook's credit policy | Harlow / Northbrook | Yes | Steps 2, 4, 5 | **Accepted with a limit**: the accounts are a typed summary, not the statements — every Step 2 ratio is user-supplied, not evidenced; Dec 2024 figures are 9 months old and unaudited as far as shown |
| `customer_payment_history_12m_final.csv` | **An employee shift rota** (E08–E10, weeks 1–4). Not a payment history despite its name | None | n/a | No step uses it | **Rejected.** If a final payment history exists, please upload it in its place |

**Still missing (recommended, not blocking):** bureau report, trade references, the full customer statements, write-off history, the vendor list (to test whether Harlow is also a supplier), the terms on Harlow's customer record.

*I would wait here for your answer; proceeding with the accepted files as instructed.*

## Findings

**1. Exposure already exceeds the current limit.** Open items 30 Sep: INV-20418 **48,200, 95 days overdue** + INV-20977 199,957 not yet due = **248,157** against a **200,000** limit — **48,157 over**. Peak exposure in the 12 months seen: **471,498** (12–17 Sep 2025, three invoices open at once).

**2. Days-to-pay is long and getting worse (Step 2b, sample 5 paid invoices).** 76, 82, 88, 94, 100 days from invoice — mean and median **88**, rising **6 days per invoice**. Invoices are issued on **net 30** (every due date is invoice + 30), so Harlow pays **46 to 70 days late**, and the latest is the worst. Five invoices is a thin sample, but the trend is perfectly one-directional.

**3. The request understates actual trading.** Requested ~40,000 a month; invoiced in the last 12 months **1,116,706** (5 paid + 2 open) = **93,059 a month**. Invoice size rose every time: 124,078 → 148,894 → 173,710 → 198,526 → 223,341. A sustained rise in ordering together with slowing payment is a Step 7 distress trigger.

**4. Concentration breaches policy.** Harlow is **248,157 / 798,360 = 31.1%** of receivables (31.0% of gross 800,510), above the **25%** cap. Next largest: Pennine Retail Group 14.0%.

**5. Customer's own accounts (Step 2, user-supplied summary, Dec 2024).** Current ratio 1.9m / 1.7m = **1.12**; debt to equity 1.4m / 0.6m = **2.33** (debt, not total liabilities, so leverage may be higher); net margin 110,000 / 6.2m = **1.8%**; working capital **200,000**. Thin margin, high leverage, barely adequate liquidity; 9 months old.

**6. Tier: C — watchlist, bordering D (Step 4).** Rests on **both** your payment experience (findings 1–3) and the customer's summary accounts (finding 5); no bureau or references. Long relationship and every invoice eventually paid keep it out of D; the overdue 48,200, worsening lateness and leverage keep it out of B.

**7. Recommended limit and terms (Steps 5–6).**

| Method | Basis | Result |
|---|---|---:|
| 1 — % of working capital | 5–10% × 200,000 | 10,000 – 20,000 |
| 2 — Multiple of monthly volume | 1.5–2.0× request 40,000 / × history 93,059 | 60,000 – 80,000 / 139,588 – 186,118 |
| 4 — Tier ceiling | Tier C (assumed mapping) | 50,000 |

**Recommendation: reduce the limit from 200,000 to 50,000 (tier C ceiling); decline net 45; keep net 30.** This is **198,157 below current exposure**, so it needs a plan, not just a number: hold new shipments until INV-20418 (48,200) is paid and the balance is inside the limit; stop condition — any item over 30 days overdue triggers a hold; ask for a parent or personal guarantee and current (2025) accounts before any increase. If your tier mapping differs, the direction holds: even the 150,000 ceiling is below exposure. Any limit above 150,000, including the existing 200,000, needs the finance director.

**8. Monitoring triggers across the whole ledger (Step 7).** First-delay / slowing trend: **every customer's days-to-pay rose with each invoice** (+3 days each; Harlow +6). Overdue now: **Foxhall Garden Centres 4,003, 130 days** (mean days-to-pay 75), **Tideswell Hotels 48,031, 67 days** (mean 62), **Ridgeway Logistics 72,046, 41 days**. Calder Print has an unapplied credit note **−2,150** (possible dispute). Review cadence: Harlow quarterly (watchlist).

## Not done, and why

Bureau and trade-reference summaries (none supplied) · write-off history (not supplied) · customer-is-also-vendor test (no vendor list) · terms on record vs applied (record not supplied; applied terms are net 30) · industry benchmarks · qualitative factors (management, industry, events) · **sanctions screening — not available in this skill** · Excel workpaper (would ask first: `Credit_Review_Harlow Fabrication Ltd_2025-09-30.xlsx`).

## Coverage sheet (manual run)

**Environment:** Northbrook Trading Ltd, 30 Sep 2025, USD — user-asserted. Data source: upload (gateway absent). Three files accepted with limits; `customer_payment_history_12m_final.csv` rejected (shift rota). **Capability map:** Not applicable: no connection. Every task is `[manual]`.

| Input or task | Status | Source / sample size | Gap |
|---|---|---|---|
| Step 1 customer info | Done with a limit | Request file | Registration, ownership, industry |
| Step 2 ratios | Done with a limit | Customer summary, user-supplied | Full statements, audit status |
| Step 2b payment experience | Done | History, n = 5 paid; ageing, 2 open | Pre-Oct 2024 history |
| Step 3 qualitative | Not done | — | Not supplied |
| Step 4 tier | Done | Both evidence types | No bureau |
| Step 5–6 limit, terms | Proposed | Policy file | FD approval |
| Step 7 triggers | Done, whole ledger | 60 invoices, 14 open items | — |
| Step 9 save | Not done | — | Offered only after approval |

**Data sources:** user uploads — `customer_payment_history_12m.csv`, `ar_aging_detail_2025-09-30.csv`, `credit_request_and_policy.md`. Nothing was set, held, sent or changed.
