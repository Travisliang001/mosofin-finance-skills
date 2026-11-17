# Credit and collections policy — Northbrook Trading Ltd — base at 30 September 2025

Mosofin is not connected, so this run is manual: every step is `[manual]` and every figure comes from your uploads. Connecting Mosofin would let the customer base, payment history, credits and write-offs be read from the books ([docs.mosofin.com](https://docs.mosofin.com)).

**This designs a policy. No terms, limits or holds were changed and no customer was contacted.**

## Read-back

Designing a credit and collections policy for **Northbrook Trading Ltd** (user-asserted), to fix **slow payment**, on the customer base at **30 September 2025**, currency **USD** (user-asserted), from your uploads. Standard terms **net 30** (your answer; the customer list agrees — all 12 customers on 30 days). Orders **can be held by the sales lead in the order system**. Not answered (F): **who approves credit exceptions, write-off limits, who owns each relationship** — drafted below as open questions, not invented. Go-ahead assumed.

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Needed for | Verdict |
|---|---|---|---|---|---|
| `ar_aging_detail_2025-09-30.csv` | Open-item receivables ageing at 30 Sep 2025, 14 lines, 12 customers, total **798,360** (incl. credit note CM-0312 −2,150) | As at 30 Sep 2025; no entity or currency | Yes; days overdue recomputed and agree | Steps 1, 3, 6 | **Accepted with a limit**: company user-asserted |
| `customer_list.csv` | Customer master: 12 customers, terms, credit limits, AP contact emails | No entity | Yes | Steps 1–2 (terms in use, limits) | **Accepted with a limit**: company user-asserted; contacts used for nothing — nothing is sent |
| `customer_payment_history_12m.csv` | Paid-invoice history, 60 invoices (5 per customer), Oct 2024 – Sep 2025, days-to-pay (recomputed: agree) | No entity | Yes; paid invoices only | Step 1 (behaviour), Step 6 | **Accepted with a limit**: company user-asserted; 5 invoices per customer is a thin sample |
| `approval_matrix_and_tolerances.md` | **A purchasing / AP document**: purchase-order approval limits (manager to 10,000, CEO above), three-way-match tolerances, AP exceptions | Northbrook implied | Readable, but it governs **purchases, not customer credit** | **No step uses it**: it does not answer who approves credit exceptions or write-offs | **Set aside, not used.** Please type the credit governance (question F) in the chat instead |
| `ar_aging_detail_2025-09-30_final.csv` | **An employee shift rota** (E08–E10, weeks 1–4). Not an ageing despite its name | None | n/a | No step uses it | **Rejected.** If a final ageing exists, please upload it in its place |

**Still missing:** credit notes and **write-offs** for the period (for disputes and bad debt %); **opening A/R** (for CEI); **credit sales** for the period (for a true DSO); your credit governance (F).

*I would wait here for your answer; proceeding with the accepted files as instructed.*

## Findings

**1. The base does not pay on net 30, and it is getting slower (Step 1).** Across 60 paid invoices: mean days-to-pay **45.3** (simple), **55.6** value-weighted. Every customer slowed with each invoice — the first-invoice average was **38.8 days**, the latest **51.8** (+3 days per invoice for 11 customers, **+6 for Harlow**). Net 30 is the written term; it is not what happens.

**2. Segment grid — real customers, mean days-to-pay, sample n = 5 each (Step 1).** Value = 12-month paid invoices; payment bands on net 30: prompt ≤ 35 days, late 36–50, slow > 50.

| Value \ Payment | Prompt (≤ 35) | Late (36–50) | Slow (> 50) |
|---|---|---|---|
| **High (> 300k)** | Castleton 31 (308,196) | Pennine 44 (392,250) | **Harlow 88 (868,549)** |
| **Mid (100–300k)** | Marlow & Finch 29; Brecon 28 | Ridgeway 47; Ashby 36; Calder 41 | Tideswell 62 |
| **Low (< 100k)** | Dunmore 30; Elmfield 33 | — | Foxhall 75 |
| **Count** | 5 | 4 | 3 |

Margin could not be measured (no customer-level cost) and is **left out as unmeasured**. Disputes: one credit in the data, Calder Print CM-0312 −2,150 = **1.9%** of Calder's 112,070 — a credit-memo proxy, which understates disputes settled without a credit.

**3. Concentration.** Harlow is **248,157 / 798,360 = 31.1%** of receivables and over its 200,000 limit by 48,157; Pennine 14.0%. One account drives the overdue problem: Harlow is 92% of the 90+ bucket.

**4. Buckets today, for sizing the cadence (Step 3).**

| Days past due | Value | % of A/R | Customers |
|---|---:|---:|---:|
| Not yet due (incl. CM −2,150) | 425,953 | 53.4% | 7 |
| 1–15 | 168,107 | 21.1% | 2 (Pennine, Ashby) |
| 16–30 | 32,020 | 4.0% | 1 (Calder) |
| 31–60 | 72,046 | 9.0% | 1 (Ridgeway) |
| 61–90 | 48,031 | 6.0% | 1 (Tideswell) |
| 90+ | 52,203 | 6.5% | 2 (Harlow 48,200; Foxhall 4,003) |

Twelve accounts: every step can be done by one person; no automation and **no credit committee** are needed — a committee for twelve accounts is theatre.

**5. Hold rule tested on the real base (Step 2).**

| Rule: hold if any item is more than … days past due | Customers held today | A/R affected |
|---|---:|---:|
| 30 | **4 of 12** (Harlow, Ridgeway, Tideswell, Foxhall) | 372,237 (46.6%) |
| 60 | 3 of 12 (Harlow, Tideswell, Foxhall) | 300,191 (37.6%) |
| 90 | 2 of 12 (Harlow, Foxhall) | 252,160 (31.6%) |

A 30-day hold would stop **a third of the book** today, including the largest customer. **Proposed:** hold at **60 days past due or over limit**, with a 15-day warning; phase to 45 days once the base pays inside 50. Your choice — the counts are the evidence.

**6. Governance design point.** Holds sit with the **sales lead**, who also owns the relationship. That puts the stop decision with the person most reluctant to use it. Recommend: credit (finance) decides the hold, sales executes it; overrides recorded with approver and reason. **Designed, not verified** — nothing in the files shows who does what.

## Policy outline (each step's verdict in a manual run is `[manual]`)

- **Credit rules (Step 2):** onboarding — credit application + references for any new limit; limits per `credit-limit-and-customer-risk`; triggers — first late payment, days-to-pay up 10+ days over 3 invoices, sudden order increase; holds as finding 5; exceptions approved by **[open: name and limit]**.
- **Cadence (Step 3):** day −5 reminder; days 1–15 statement and call; 16–30 second call, account flagged; 31–60 hold warning, finance manager call; 61–90 hold, senior escalation; 90+ final demand, consider agency or provision. Templates by bucket marked **`REVIEW REQUIRED - NOT SENT`**.
- **Disputes (Step 4):** codes from what happens — today only a damage/pricing-type credit (CM-0312); codes: damage, pricing, quantity, quality, other; evidence and 10-day SLA each; a short-pay pending investigation is not a credit, a credit is not a write-off.
- **Governance (Step 5):** credit owner, write-off limits, separation of credit / cash application / write-off — **[open questions for you]**.

## KPI baseline (Step 6)

| KPI | Baseline | Basis |
|---|---|---|
| % current A/R | **53.4%** | Not-yet-due 425,953 / 798,360 at 30 Sep 2025 |
| DSO | **≈ 80.9 days** (proxy) | 798,360 / (60 paid invoices 2,801,789 + open 800,510 = 3,602,299) × 365; **not true credit sales** — replace with the ledger figure |
| CEI | **Not computed** | Needs opening A/R and credit sales for the period |
| Bad debt % | **Not computed** | No write-off data |
| Dispute cycle time, promise-to-pay kept | Need a system that records them | — |

CEI measures the collections team; DSO measures working capital and moves with sales.

## Coverage sheet (manual run)

**Environment:** Northbrook Trading Ltd, 30 Sep 2025, USD — user-asserted. Data source: upload (gateway absent). Ageing, customer list, payment history accepted with limits; approval matrix set aside (AP document); `ar_aging_detail_2025-09-30_final.csv` rejected (shift rota). **Capability map:** Not applicable: no connection. Every task is `[manual]`.

| Step | Status | Gap |
|---|---|---|
| 1 Segment | Done; margin unmeasured | n = 5 per customer |
| 2 Credit rules | Drafted; hold rule tested | Approvers (F) |
| 3 Cadence | Sized and drafted | Bucket transition rates need prior ageings |
| 4 Disputes | Drafted from one credit | Credit and dispute history |
| 5 Governance | **Designed, not verified** | Roles, limits |
| 6 KPIs | 2 of 4 automated KPIs (DSO as proxy) | Opening A/R, credit sales, write-offs |
| 7 Save | Not done | Offered only after approval |

**Data sources:** user uploads — `ar_aging_detail_2025-09-30.csv`, `customer_list.csv`, `customer_payment_history_12m.csv`. Nothing was changed, held or sent.
