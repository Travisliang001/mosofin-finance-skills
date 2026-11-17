# Revenue recognition — Harlow Fabrication contract, Northbrook Trading Ltd

This run is manual: no Mosofin connection is present, so everything below comes from the files you uploaded. Nothing has been posted, sent or changed anywhere.

## (a) Read-back

Analysing the **36-month supply and services agreement with Harlow Fabrication Ltd** (signed 1 July 2025) for **Northbrook Trading Ltd** (company as you stated it; not confirmed against a connection), under **ASC 606**, position as at **30 September 2025**, in **USD**, from the files you uploaded. Standalone selling prices from **the company's price list as quoted in the contract summary**. No expedients elected; no modifications (both as you stated).

Intake questions the files do not answer:
- Invoices and payments on the contract to date: not supplied (required).
- Revenue and deferred revenue ledger detail for the customer: not supplied (recommended).
- Source evidence for the price list (observation counts of standalone sales): not supplied.

What I received:
- `contract_harlow_fabrication.md` — a key-terms summary: customer Harlow Fabrication Ltd, signed 1 July 2025, 36 months, three deliverables totalling 150,000, billing terms, price-list SSPs totalling 180,000.
- `accounting_policies.md` — seven policy lines: US GAAP, private company, "Revenue: recognised when goods are delivered".
- `contract_harlow_fabrication_final.csv` — three rows, columns employee / week_1..week_4 with values nights / days / off.

## (b) Validation of the upload (before any work)

| File | What it actually is | Right company and period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `contract_harlow_fabrication.md` | Contract key-terms summary | Customer and dates fit. The seller is not named in the file; currency is not stated (USD taken from intake) | Yes. Deliverable prices foot to 150,000; SSPs foot to 180,000. No renewal, termination, payment-days or signature evidence | Steps 1–6 | **Accepted with a limit**: Step 1 criteria on approval, termination and collectibility cannot be evidenced from it |
| `accounting_policies.md` | Accounting policy summary | No company or period named in it | Yes, short | Inputs (policies and expedients); context for Step 0 | **Accepted with a limit**: it names no expedients and has no policy for services or licences delivered over time |
| `contract_harlow_fabrication_final.csv` | A four-week staff shift roster (employees E08–E10) | No company, no period, no amounts | Not for this skill | No step uses it | **Rejected**. Despite its name it is not the contract or a billing listing. Please upload the invoice and payment listing for Harlow instead |

**Required inputs still missing:** invoices and payments on the contract to date (CSV/XLSX). Recommended and missing: revenue and deferred revenue ledger detail for Harlow.

Without the invoice listing, the output will **not** contain: actual billed and collected amounts, the receivable, a comparison of what was recognised with what should have been, or the Step 0 tests. I will not rebuild billing from the contract and call it actual. I would stop here and wait for your answer.

*You replied: go ahead with the accepted files.* Billing below is therefore **contractual billing per the contract terms**, labelled as such, not invoiced amounts.

## (c) Findings

All figures are contract-derived unless marked.

**Step 0 — do the books apply the standard?** Not run: no ledger. One point from the policy file to raise: the only revenue policy is "recognised when goods are delivered". This contract has no goods; it is hosted access, implementation and support. The policy does not cover it, and if revenue is in practice booked on invoice, September year-to-date revenue on this contract would be 65,000 against 35,416.67 below.

**Step 1 — contract.** Signed 1 July 2025, 36 months to 30 June 2028, fixed 150,000. Not evidenced: approval by both parties, termination and renewal clauses, collectibility. If Harlow can cancel without penalty, the term may be shorter than 36 months (edge case: cancellable contracts). Your call.

**Step 2 — performance obligations (your judgment; indicators only).**
1. Hosted software access for the term. "Hosted, access for the term" reads as a service the customer receives as time passes, not a licence delivered on day one.
2. Implementation, completed 31 August 2025. Capable of being distinct if a third party could do it; separately identifiable only if it does not significantly customise or integrate the hosted service. The skill's edge case notes that on hosted contracts it is often **not** distinct.
3. Support, 36 months. A series of substantially the same services; could arguably be combined with (1).

Question for you: is implementation distinct? I show both outcomes.

**Step 3 — transaction price.** 150,000 fixed. No variable amounts, no right of return (per contract). Two flags:
- **Billing does not add up to the price.** 60,000 on signing + 2,500 a month from August 2025 to June 2028 is 35 instalments = 87,500; total 147,500, which is **2,500 short of 150,000**. Either there is a 36th instalment after the term ends or the summary is wrong. Please confirm from the signed contract.
- **Possible significant financing component.** 60,000 (40% of the price) is paid on signing for services running three years. No expedient applies beyond one year. Whether it is significant, and the rate, are yours to decide; not adjusted here.

**Step 4 — allocation on relative standalone selling prices** (source: company price list, as quoted; observation count not supplied).

| PO | Contract price | SSP | % of SSP | Allocated price |
|---|---:|---:|---:|---:|
| Hosted software access | 108,000 | 120,000 | 66.67% | 100,000.00 |
| Implementation | 24,000 | 30,000 | 16.67% | 25,000.00 |
| Support | 18,000 | 30,000 | 16.67% | 25,000.00 |
| Total | 150,000 | 180,000 | 100% | 150,000.00 |

The 30,000 bundle discount (16.67%) is spread proportionally. The prices stated in the contract are **not** the allocation: software drops by 8,000, implementation rises by 1,000, support rises by 7,000.

**Step 5 — recognition schedule, case A: implementation distinct** (access and support over time, time elapsed, criterion 1; implementation satisfied by 31 August 2025).

| Period | Software access | Implementation | Support | Period revenue | Cumulative |
|---|---:|---:|---:|---:|---:|
| Jul 2025 | 2,777.78 | — | 694.44 | 3,472.22 | 3,472.22 |
| Aug 2025 | 2,777.78 | 25,000.00 | 694.44 | 28,472.22 | 31,944.44 |
| Sep 2025 | 2,777.78 | — | 694.44 | 3,472.22 | **35,416.67** |
| Oct 2025 – Jun 2028 (33 months) | 2,777.78 a month | — | 694.44 a month | 3,472.22 a month | 150,000.00 |

Implementation is shown in full at completion; if it was performed evenly over July and August it is 12,500 a month, with the same cumulative figure at 30 September.

**Case B: implementation not distinct** (one combined obligation, straight line): 150,000 / 36 = 4,166.67 a month; cumulative at 30 September 2025 **12,500.00**. The judgment moves 22,916.67 of revenue.

**Step 6 — contract balance at 30 September 2025** (contractual billing: 60,000 + 2,500 Aug + 2,500 Sep = 65,000).

| | Case A | Case B |
|---|---:|---:|
| Cumulative billing (contractual) | 65,000.00 | 65,000.00 |
| Cumulative revenue earned | 35,416.67 | 12,500.00 |
| **Contract liability (deferred revenue)** | **29,583.33** | **52,500.00** |
| Revenue overstated if recognised on invoice | 29,583.33 | 52,500.00 |
| Revenue if contract-stated prices were used instead of the allocation (case A) | 34,500.00 (916.67 too low) | n/a |

The receivable cannot be stated: no payment data.

**Step 7 — proposed entries, case A. PROPOSED — NOT POSTED** (sales tax ignored; none stated).

| Date | Debit | Credit | Amount |
|---|---|---|---:|
| 1 Jul 2025 | Accounts receivable | Contract liability | 60,000.00 |
| Aug and Sep 2025, each | Accounts receivable | Contract liability | 2,500.00 |
| Jul 2025 | Contract liability | Revenue | 3,472.22 |
| Aug 2025 | Contract liability | Revenue | 28,472.22 |
| Sep 2025 | Contract liability | Revenue | 3,472.22 |

**Steps 8–10.** Modifications: none, as you stated. Contract costs: was a sales commission paid on winning this three-year contract? With no expedient elected it would be capitalised and amortised; not answered. Remaining performance obligations at 30 September 2025: 150,000 − 35,416.67 = **114,583.33** (case A), which is not the deferred revenue balance because it includes amounts not yet billed.

## (d) What was not done, and why

- **Step 0 tests (0a–0d)** — no ledger, chart of accounts or invoice listing was uploaded.
- **Actual billing, receipts, the receivable, and recognised-versus-should-have-been** — the required invoice and payment listing is missing; the file with the matching name was a shift roster and was rejected.
- **The distinct conclusion, the over-time conclusion, the financing-component conclusion and rate** — these are your judgments; I set out indicators and both outcomes.
- **Observable SSP evidence** — the price list was taken as quoted; no standalone sales were available to count.
- **Collectibility, approval, termination and renewal terms** — not in the summary.
- **Contract costs schedule** — commission facts not supplied.
- **The 147,500 versus 150,000 billing difference** — flagged, not resolved.
- **Excel workpaper** — not created; say if you want it.
- **Posting** — this skill never posts. Every entry is a proposal for a person to review.

Parameters used: ASC 606; no expedients; SSPs 120,000 / 30,000 / 30,000 from the price list; time elapsed over 36 months from 1 July 2025; billing per contract terms.
