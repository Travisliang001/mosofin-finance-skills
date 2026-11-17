# Revenue recognition — Harlow Fabrication contract — Northbrook Trading Ltd — at 30 September 2025

Mosofin is not connected, so this run is manual: every step is `[manual]` and every figure comes from your uploads. Connecting Mosofin would automate the ledger reads ([docs.mosofin.com](https://docs.mosofin.com)).

## Read-back (Stage 1)

Analysing the **36-month software, implementation and support agreement** with **Harlow Fabrication Ltd** for **Northbrook Trading Ltd** (user-asserted), under **ASC 606**, position **at 30 September 2025**, currency **USD** (user-asserted; neither the contract nor the billing listing states a currency), from **the contract terms and invoice listing you uploaded**. Standalone selling prices **from the company price list, as quoted in the contract file** (a fact that arrived inside a file: used once you confirm it here). **No expedients; no modifications** (your answer). Go-ahead assumed.

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Needed for | Verdict |
|---|---|---|---|---|---|
| `contract_harlow_fabrication.md` | Key-terms summary of a supply and services agreement: three deliverables with prices, billing plan, SSPs | Seller named Northbrook Trading Ltd (matches); signed 1 Jul 2025, 36 months; no currency stated | Yes: price 150,000 foots (108k+24k+18k) | Steps 1–5 | **Accepted with a limit**: a summary, not the signed agreement. Termination, renewal, acceptance, hosting and title clauses are not in it, so control and distinctness judgments rest on user-supplied terms, not evidence |
| `harlow_contract_invoices_2025.csv` | Invoice and receipt listing for this contract, 4 invoices, 1 Jul – 30 Sep 2025 | No entity or currency named | Yes: billed 67,500, paid 65,000 | Step 6 balances | **Accepted with a limit**: company and currency user-asserted |
| `accounting_policies.md` | Summary of accounting policies (US GAAP, private company) | No entity, period or currency named | Yes | Inputs: policies / expedients; Step 0 context | **Accepted with a limit**: company user-asserted. It names no ASC 606 expedients, consistent with your "none" |
| `contract_harlow_fabrication_final.csv` | **An employee shift rota** (employee, week_1–week_4: days / nights / off for E08–E10). Not a contract and not billing data, despite the name | None | n/a | No step uses it | **Rejected.** If a final or amended version of the Harlow contract exists, please upload that instead; if not, nothing is missing |

**Still missing:** revenue and deferred revenue ledger detail for Harlow (recommended) — without it Step 0 and the "recognised vs should-have-been" comparison cannot run; a chart of accounts (needed for account coding; not invented below).

## Findings

**1. The policy note does not describe ASC 606 recognition.** `accounting_policies.md` says revenue is "recognised when goods are delivered". This contract is mostly services delivered over 36 months; a delivery-based policy, applied to it, points to recognition on billing or on go-live rather than over the term. Whether the books actually do this cannot be tested without the ledger (Step 0 not run) — it is the first question to answer.

**2. Contract (Step 1).** Parties approved (signed 1 Jul 2025), rights and payment terms identifiable, commercial substance and collectibility not contradicted: 2 of 3 invoices paid within terms; INV-20977 (2,500, 30 Sep) open. Collectibility is your judgment.

**3. Performance obligations (Step 2) — your judgment, both answers shown.**
- PO1 Hosted software licence, access for the term. Hosted with access for the term indicates the customer consumes it as provided (a service, over time). If you conclude it is a right-to-use licence the customer can take, it is point-in-time — schedule C below.
- PO2 Implementation (completed 31 Aug 2025). Distinct only if the customer could benefit from it with other resources **and** it is separately identifiable within the contract (not a significant customisation of the licence). Not concluded.
- PO3 Support, 36 months: a series of substantially similar services, over time.

**4. Transaction price (Step 3).** Fixed 150,000; no variable consideration, no right of return, no tax shown on the invoices. **Significant financing component flag:** 60,000 is paid on signing against services delivered across 36 months; the resulting contract liability is still about 23,300 a year later and only unwinds at month 36, so the timing gap exceeds one year and ASC 606's one-year expedient is not available. Whether it is significant, and the rate, are yours; not adjusted below.

**5. Allocation (Step 4) — relative SSP, sums to the transaction price.**

| PO | SSP (price list, per contract file) | % of SSP | Allocated | Contract-stated price | Difference |
|---|---:|---:|---:|---:|---:|
| Licence | 120,000 | 66.667% | 100,000.00 | 108,000 | −8,000 |
| Implementation | 30,000 | 16.667% | 25,000.00 | 24,000 | +1,000 |
| Support | 30,000 | 16.667% | 25,000.00 | 18,000 | +7,000 |
| **Total** | **180,000** | 100% | **150,000.00** | 150,000 | 0 |

The 30,000 discount (180,000 − 150,000) is spread pro rata; no evidence it belongs to one PO. The contract's own line prices are **not** the allocation. SSP source: price list, user-supplied, observation count unknown (no sales ledger).

**6. Recognition at 30 Sep 2025 (Step 5) — three months of 36 elapsed.**

| Scenario | Licence | Implementation | Support | Cumulative revenue | Billed | Contract balance |
|---|---:|---:|---:|---:|---:|---:|
| **A** Licence over time; implementation distinct, recognised by 31 Aug | 8,333.33 | 25,000.00 | 2,083.33 | **35,416.67** | 67,500 | **Contract liability 32,083.33** |
| **B** Licence over time; implementation not distinct, over the term with the licence | 8,333.33 | 2,083.33 | 2,083.33 | **12,500.00** | 67,500 | **Contract liability 55,000.00** |
| C Licence point in time at 1 Jul; implementation distinct | 100,000.00 | 25,000.00 | 2,083.33 | 127,083.33 | 67,500 | Contract asset 59,583.33 |

Monthly over-time amounts: licence 2,777.78, support 694.44, implementation if not distinct 694.44. The A–B gap at 30 Sep is **22,916.67** of revenue. Under either A or B, revenue recognised on invoice (67,500) would be overstated by **32,083.33 (A)** or **55,000.00 (B)**.

**7. Balances (Step 6).** Receivable 2,500 (INV-20977, unpaid at 30 Sep). Cash received 65,000. Contract liability as above; scenarios A and B produce no contract asset.

**8. Proposed entries for September 2025 (Step 7) — PROPOSED, NOT POSTED. Scenario A; account names are captions, not your codes.**

| Entry | DR | CR | Amount |
|---|---|---|---:|
| INV-20977 issued 30 Sep | Accounts receivable | Contract liability | 2,500.00 |
| September revenue, licence | Contract liability | Revenue — licence | 2,777.78 |
| September revenue, support | Contract liability | Revenue — support | 694.44 |

Under B, September revenue is 4,166.67 (2,777.78 + 694.44 + 694.44). Each entry balances. If the books already recognised revenue on the invoices, a catch-up is needed; its size depends on what the ledger shows.

**9. Modifications (Step 8): none, per your answer. Contract costs (Step 9): commission test not run, no expense data. Disclosure (Step 10): RPO at 30 Sep is the unsatisfied allocated price — 114,583.33 under A, 137,500.00 under B — and includes 82,500 not yet billed, so it is not the deferred revenue balance.**

## Decisions needed from you

1. Is implementation distinct (A) or not (B)? 2. Is the hosted licence a service over time (A/B) or a point-in-time licence (C)? 3. Is the upfront payment a significant financing component, and at what rate? 4. Please upload the Harlow revenue and deferred revenue ledger detail so the recognised-vs-should-have-been comparison can run.

## What was not done, and why

- **Step 0 (four standard-application tests)**: needs the revenue, deferred revenue, contract asset and tax ledger. Not uploaded.
- **Recognised to date vs should have been**: needs the ledger. Not uploaded; nothing anchored to the books.
- **Commission / contract-cost test**: no commission data.
- **Observable SSP (level 1)**: no sales ledger; the price list is user-supplied.
- **Account coding**: no chart of accounts; captions only.
- **Workpaper**: shown as tables; say if you want `RevRec_HarlowFabrication_[contract no.]_2025-09-30.xlsx`.
- **Posting**: nothing posted, sent or changed anywhere.

## Coverage and provenance (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, at 30 Sep 2025, USD — all **user-asserted**. Framework ASC 606, no expedients, no modifications (user). Data source: **upload**. Files: contract summary — accepted with limit (summary only); invoices — accepted with limit (company/currency user-asserted); policies — accepted with limit (company user-asserted); `contract_harlow_fabrication_final.csv` — **rejected** (shift rota) |
| Capability map | Not applicable: no connection. Every task is `[manual]`. |
| Steps | 0 **not done** (no ledger); 1 done with limit (summary); 2 done, judgment open; 3 done, SFC flagged not measured; 4 done; 5 done under three scenarios; 6 done with limit (billing only); 7 drafted, not posted; 8 n/a per user; 9 **not done**; 10 RPO computed, disaggregation not done; 11 tables only |
| Not done | Step 0 tests, recognised-vs-should-have-been, contract-balance roll-forward to GL, commission test — all need the revenue / deferred revenue ledger upload |
| Parameters | ASC 606; no expedients; SSP = price list (user-supplied, count unknown); measure of progress = time elapsed (licence, support); constraint n/a (no variable consideration) |
