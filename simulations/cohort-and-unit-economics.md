# Cohorts and unit economics — Northbrook Trading Ltd — as at 30 September 2025

Mosofin is not connected, so this run is manual: every step is `[manual]` and every figure comes from your uploads. Connecting Mosofin would read first-invoice dates and customer revenue straight from your books ([docs.mosofin.com](https://docs.mosofin.com)).

## Read-back

Analysing **monthly cohorts** for **Northbrook Trading Ltd** (user-asserted), a **transactional** business, over the **12 months October 2024 – September 2025**, in **USD** (user-asserted), from **your uploads**. A customer is **lost after 90 days with no invoice** (your rule). CAC is **paid-only on account 6200 (marketing)** as you named it — not fully loaded.

Unanswered, and how this run treats them:
- **When a customer counts as acquired (D)**: not answered. The skill proposes **first invoice** and waits for your yes. Assumed for the arithmetic below, but see Finding 1 — it decides the result, so both readings are shown.
- **Channel data, cost-to-serve, discount rate (F)**: not supplied → **blended CAC, one company-wide gross margin, undiscounted LTV**, stated as such.

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Needed for | Verdict |
|---|---|---|---|---|---|
| `customer_payment_history_12m.csv` | Invoice-level list: customer, invoice, invoice date, **paid date**, amount, days to pay. 60 invoices, 12 customers, **2,801,789**; invoice dates **10 Oct 2024 – 10 Jul 2025**; every row is paid | No entity or currency named | Customer, date and amount present. **No invoice dated Aug or Sep 2025**; no credits or refunds | Steps 1–6 (cohorts, retention, revenue per customer) | **Accepted with a limit**: company user-asserted; appears to be **paid invoices only**, so open invoices (Aug–Sep) are likely missing; covers only 67% of P&L revenue (below) |
| `monthly_profit_and_loss_36m.csv` | Monthly P&L by line, Oct 2022 – Sep 2025 (36 months). Every month's net income recomputes exactly | No entity or currency; lines are named, not numbered | Yes | Step 5 (spend), Step 6 (gross margin), coverage tie | **Accepted with a limit**: company user-asserted; the **`marketing` column is taken to be account 6200** — please confirm |
| `customer_list.csv` | Customer master: 12 customers, terms (all 30 days), credit limit, AP contact email | No entity named | Same 12 names as the invoice list. **No start date, plan, channel or geography** | Step 0 (customer population check) only | **Accepted with a limit**: confirms the population; supports no segment view. Contact emails not used |
| `customer_payment_history_12m_final.csv` | **An employee shift rota** (E08–E10, weeks 1–4, days / nights / off). Not customer data despite its name | None | n/a | No step uses it | **Rejected.** If a later customer invoice list exists (with Aug–Sep 2025 and open invoices), upload that instead |

**Still missing, and needed before any conclusion:** (1) the **full invoice list back to each customer's first-ever invoice** — paid *and* unpaid — including Aug–Sep 2025; (2) credits / refunds by customer; (3) your **acquisition definition (D)**. I would wait for your answer here; proceeding on the accepted files as instructed.

## Findings

**1. The 12 customers are almost certainly not new — the history is cut off, not the acquisitions.** All 12 first appear in **October (6) and November (6) 2024**, the first two months of the file, and **none appears after**. The P&L shows the business already billing **282,000 in October 2022** and **4,451,200 in the 12 months to September 2024**. So "first invoice in this file" is the window edge, not acquisition. The earliest cohort available is October 2024, and it is **left-censored** (its start is unobserved).

| Reading | Cohorts | New customers Dec 2024 – Sep 2025 | CAC |
|---|---|---|---|
| A. First invoice in the file = acquisition | Oct-24: 6; Nov-24: 6 | 0 | Oct–Nov 2024 spend 29,508 / 12 = **2,459** |
| B. Customers predate the window (what the P&L suggests) | None observable | 0 | **Not computable** — no acquisitions in 12 months; 216,382 of 6200 spend acquired nobody in this file |

Reading A's CAC, payback (≈0.3 months) and LTV/CAC (≥38×) are **artefacts and are not reported as results.** No health verdict is given until the true first-invoice dates are supplied.

**2. The customer file does not reconcile to revenue.** Invoices in the file are **2,801,789** against P&L revenue of **4,203,800** for Oct 2024 – Jul 2025 (**66.6%**), and **0 of 932,500** for Aug–Sep 2025. Month by month the file covers 42%–90%. Either there are more customers than the 12, or the file omits invoices. Retention built on it is not the whole book.

**3. Under your 90-day rule, six customers read as lost — but this is not safe to conclude.** The October-2024 group (Harlow Fabrication, Castleton Foods, Marlow & Finch, Tideswell Hotels, Calder Print, Elmfield Schools) last invoiced **10 June 2025**, **112 days** before 30 September → lost under the rule (logo retention **50%**). The November group last invoiced 10 July (82 days) → active. Because the file has **no invoices at all after July** while the P&L shows 477,100 and 455,400 of revenue in August and September, the six "losses" may be **unpaid August invoices missing from a payment history**. Show me the open invoices before treating them as churn.

**4. Revenue retention shows strong expansion.** Every customer bills **every two months**, and each invoice is a fixed step up on the first: cohort revenue at invoice ages 0 / 2 / 4 / 6 / 8 months is **100% / 120% / 140% / 160% / 180%** for both groups (Oct-24: 246,156 → 443,081; Nov-24: 154,100 → 277,377). Note the two-month cycle: a naive monthly "active" test would show false churn in every other month; your 90-day window avoids that. Logo retention is 100% for both groups through age 10; the only drop is Finding 3. Ages beyond 8 months have not been reached by both groups.

**5. Gross margin stepped down.** COGS was exactly 58% of revenue (margin **42%**) every month from Oct 2022 to Jun 2025, then **60% (margin 40%)** from Jul 2025. Window margin 41.4%. Any LTV should use 40% going forward, company-wide — which **cannot reveal negative-contribution customers**.

**6. Account 6200 behaves like a percentage of revenue, not acquisition spend.** Marketing is exactly **4.0% of revenue in 35 of 36 months**, then **29,146 (6.4%) in September 2025** — about **10,930** above the 4% line. A spend line that tracks revenue to the dollar looks like commission or an allocation, which would make it a poor CAC base. Please confirm what 6200 holds and what the September step is.

**7. Segments.** By size from the file: Harlow Fabrication alone is **868,549 (31%)**; the top two (with Pennine Retail, 392,250) are **45%**; the smallest, Foxhall Garden Centres, is 14,011. **Not analysable:** channel, plan and geography (not in any file). Noted only: days-to-pay rises by 3 days on every successive invoice for every customer (Harlow 76 → 100 days on 30-day terms) — a collections question for `ar-aging-and-collections`, not a retention one.

## Metrics, with their status

| Metric | Value | Status |
|---|---|---|
| Logo retention (90-day rule) | 100% to age 10; Oct-24 group 0% at age 11 | **Provisional** — Finding 3 |
| Revenue retention (bi-monthly ages) | 120 / 140 / 160 / 180% | Done, on the file's 67% of revenue |
| Customer lifetime | ≥ 11 months observed (lower bound); 1/churn not meaningful on one data point | Bounded below only |
| CAC (paid-only, 6200, blended) | Not computable (Reading B) / 2,459 (Reading A, not relied on) | **Not run as a result** |
| LTV on margin, payback, LTV/CAC | — | **Not run**: depend on CAC and on true lifetime |

## Not done, and why

Full cohort triangle by true acquisition month — needs full invoice history. CAC, payback, LTV/CAC — need acquisitions in the window and confirmation of what 6200 contains. Credit/refund netting — no credits supplied. Channel, plan, geography segments — no data. Discounted LTV — no rate. Fully-loaded CAC — not asked for (you named 6200 only). Excel workbook `Cohort_Unit_Economics_Northbrook Trading Ltd_2025-09.xlsx` offered, not created without your yes.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, as at 30 Sep 2025, USD — **user-asserted**. Source: **upload** (Mosofin not used, your choice). Invoice list, P&L, customer list: accepted with limits above. `customer_payment_history_12m_final.csv`: **rejected** (shift rota). Earliest cohort: Oct 2024, left-censored |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 0 done · 1 done with a limit (acquisition definition unconfirmed) · 2 done with a limit (67% of revenue; no Aug–Sep) · 3 done with a limit · 4 lower bound only · 5 **not done** · 6 **not done** · 7 **not done** · 8 **no verdict** · 9 size only · 10 tables in chat · 11 not offered |
| Not done | Tie of customer revenue to P&L (fails: 66.6%); Aug–Sep invoices; credits; true first-invoice dates |

Nothing was posted, sent or changed. **Data sources:** upload — `customer_payment_history_12m.csv`, `monthly_profit_and_loss_36m.csv`, `customer_list.csv`.
