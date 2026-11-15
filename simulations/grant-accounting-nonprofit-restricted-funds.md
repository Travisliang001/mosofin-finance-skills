# Grant accounting — Riverside Community Trust, year to 30 June 2025

This run is manual: no Mosofin connection is present. Everything below comes from the files you uploaded. Nothing has been posted, sent or changed.

## (a) Read-back

Tracking **three grants** (G1 City food grant, G2 Harlow Foundation, G3 State seniors grant) at **Riverside Community Trust** for the **year to 30 June 2025**, under **ASC 958**, in **USD**, tagged by **class** (Youth, Seniors, Food bank), from **the grant summary and the trial balance you uploaded**. **One is conditional** (G1). Indirect costs at **10% of direct costs where the award allows**. Company, period and currency are as you stated them.

Taken from the files, for you to confirm: which grants are conditional, the purpose restrictions, budgets, the indirect rate and the report dates. Not answered anywhere: **whether any grant is an exchange transaction rather than a contribution** (G1 and G3 are government grants), **the clause relied on for each classification** (no award letters), **the composition of the 95,000 opening restricted net assets**, and **which awards allow indirect costs** (I take G3 as not allowing them, since its indirect budget is 0).

What I received:
- `grant_awards_and_spending.md` — one table, three grants: award, period, condition, restriction, budget and spend by category, report date; indirect rate note.
- `nonprofit_trial_balance_and_gifts.md` — Riverside's account balances for the year, a table of gifts with restriction and spend, and the shared-cost split.
- `grant_awards_and_spending_final.csv` — three rows, columns employee / week_1..week_4, values nights / days / off.

## (b) Validation of the upload (before any work)

| File | What it actually is | Right company and period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `grant_awards_and_spending.md` | A grant register summary: terms, budgets and spend by category | **Names no organisation or currency**; grant periods cover the year | Yes; spend is by category totals only, not transactions | Steps 1–4 | **Accepted with a limit**: company user-asserted. A summary in place of the award letters, so every term is **user-supplied, not evidenced**, and no clause can be cited. Spend is in totals, so the date and allowable-cost tests run only on what the summary states |
| `nonprofit_trial_balance_and_gifts.md` | Account balances, a gifts table and the shared-cost allocation | Riverside Community Trust, year to 30 June 2025 | Partly: **the balances do not balance** (debits 1,037,000, credits 915,000, difference 122,000) | Step 3 (contributions, restricted net assets roll-forward) | **Accepted with a limit**: the 122,000 gap means a liability or income line is missing; the roll-forward cannot be tied to a balanced ledger |
| `grant_awards_and_spending_final.csv` | A four-week staff shift roster for employees E08–E10 | No organisation, date or amount | Not for this skill | No step uses it | **Rejected**. The name suggests the final grant awards and spending; the content is a rota. Set aside. If a final version exists, please upload it |

**Still missing:** the award letters (required; a summary received), spending and receipts **by transaction** for each grant (required; category totals received), allowable cost rules (recommended), receipts by funder, and the opening restricted net assets by grant. I would stop here and wait for your answer.

*You replied: go ahead with the accepted files.*

## (c) Findings

**1. Classification (yours to confirm; no clause available).**

| Grant | Contribution or exchange | Conditional? | Restriction | Status at 30 June 2025 |
|---|---|---|---|---|
| G1 City food grant 150,000 | Contribution assumed; government grant, test for exchange | **Yes**: barrier 5,000 meals; **5,400 served, so the condition is met** | Purpose: food bank; time: Jul 2024–Jun 2025 | Recognise 150,000, with donor restrictions |
| G2 Harlow Foundation 200,000 | Contribution | No | Purpose: youth programme | Recognise 200,000, with donor restrictions |
| G3 State seniors grant 60,000 | Contribution assumed; government grant, test for exchange | No | Purpose: seniors | **Not in the contributions recorded** (see 4) |

A condition delays recognition; a restriction delays release. G1 moved from conditional to recognised when the 5,000th meal was served.

**2. Spend against budget and award** (indirect at 10% of actual direct cost where allowed).

| Grant | Staff (budget / actual) | Supplies (budget / actual) | Direct | Indirect | Total charged | Award | Remaining | % spent |
|---|---|---|---:|---:|---:|---:|---:|---:|
| G1 | 90,000 / 88,000 | 45,000 / 32,000 | 120,000 | 12,000 | 132,000 | 150,000 | 18,000 | 88% |
| G2 | 140,000 / 121,000 | 40,000 / 39,000 | 160,000 | 16,000 | 176,000 | 200,000 | 24,000 | 88% |
| G3 | 50,000 / 49,000 | 10,000 / **11,300 in period** | 60,300 | 0 | 60,300 | 60,000 | **(300)** | 100.5% |

**3. Compliance exceptions.**

| Grant | Exception | Detail | Amount |
|---|---|---|---:|
| G3 | **Spend outside the grant period** | 3,200 of supplies dated July 2025, after the grant ended 30 June 2025 (and after the year-end) | 3,200 |
| G3 | **Category cap breached** | Supplies in period 14,500 − 3,200 = 11,300 against a 10,000 budget | 1,300 |
| G3 | **Overspend of the award** | In-period spend 49,000 + 11,300 = 60,300 against 60,000 | 300 |
| G1 | **Unspent at end of grant period** | Period ended 30 June 2025 with 18,000 unused (30,000 before indirect). Check the award for a refund clause before the 31 Aug report | 18,000 |
| G1, G2 | **Indirect budget above the stated rate** | Indirect budgets 15,000 and 20,000 are 11.1% of the direct budgets (135,000; 180,000), i.e. 10% of the award, not 10% of direct cost. Charge the 12,000 and 16,000 computed on actual direct cost unless the award says otherwise | — |

The unallowable-cost test (for example, the 31,000 of fundraising event costs) could not run: no transaction-level spend and no allowability rules.

**4. G3 is not in the books.** Contributions received 640,000 = Harlow 200,000 + City 150,000 + general donations 290,000. The State seniors grant (60,000, unconditional) is not among them, yet 63,500 of spend is charged to it. Either the grant is unrecorded (a contribution receivable and restricted revenue of 60,000 are missing) or it sits inside "general donations", in which case 60,000 is wrongly shown as unrestricted. Please confirm.

**5. Release from restriction** (purpose restriction: release equals qualifying spend, capped at the award).

| Grant | Qualifying spend | Award | Release |
|---|---:|---:|---:|
| G1 | 120,000 direct (+12,000 indirect if the award allows) | 150,000 | **120,000** (132,000 with indirect) |
| G2 | 160,000 direct (+16,000 indirect if allowed) | 200,000 | **160,000** (176,000 with indirect) |
| G3 | 60,300 in period; 59,000 within category caps | 60,000 | **59,000 to 60,000**, once recorded, never more than the award |

Cumulative release is below the award for G1 and G2. G2 runs to December 2025; I have assumed the 160,000 is all in this year, though the award started in January 2024.

**6. Restricted net assets roll-forward** (as recorded, G3 excluded): opening 95,000 + G2 200,000 + G1 150,000 − releases 160,000 − 120,000 = **165,000**. If G3 is added (60,000 in, 59,000–60,000 out) the closing is 165,000–166,000. The opening 95,000 is not broken down by grant, so the roll-forward cannot be proved grant by grant.

**7. Trial balance does not balance by 122,000.** Debits (cash 412,000 + expenses 625,000) = 1,037,000; credits (net assets 275,000 + contributions 640,000) = 915,000. Closing net assets on these figures are 290,000 against cash of 412,000; a liability of 122,000 (payables, or a refundable advance) is probably missing.

**8. Shared costs.** Salaries 90,000 + rent 24,000 = 114,000, split Youth 45,600, Seniors 28,500, Food bank 17,100, Management 17,100, Fundraising 5,700. Whether any of this is already in the grants' "staff" spend is not stated.

**9. Proposed entries — PROPOSALS, NOT POSTED** (generic account names; no chart supplied).
- G3, if unrecorded: Dr contribution receivable 60,000 / Cr contribution revenue — with donor restrictions 60,000.
- Releases for the year: Dr net assets with donor restrictions 280,000 (G1 120,000; G2 160,000) / Cr net assets released from restriction 280,000; plus G3 59,000–60,000 once recorded.

**10. Reporting calendar.** G1 City: **31 Aug 2025**. G3 State: **30 Sep 2025** (exceptions in 3 to resolve first). G2 Harlow: **31 Jan 2026**. Owners not supplied.

## (d) What was not done, and why

- **Classification by clause, exchange test** — no award letters.
- **Transaction-level date and allowability tests, untagged spend, dormant-grant check** — category totals only.
- **Restricted net assets by grant, tie to a balanced ledger** — opening not split; trial balance out by 122,000.
- **Excel workpaper** (`Grant_Accounting_2025-06_Riverside Community Trust.xlsx`) — not created; say if you want it.
- **Posting** — this skill never posts.

## Coverage (manual run)

| Section | Content |
|---|---|
| Environment | Riverside Community Trust, year to 30 June 2025, USD — user-asserted. Source: upload. Grant summary accepted with a limit (unnamed; summary of letters); trial balance accepted with a limit (does not balance by 122,000); `_final.csv` rejected (staff roster) |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 1 done with a limit (no clauses); 2 done with a limit (class mapping one-to-one assumed); 3 done with a limit; 4 done with a limit (summary-level tests only); 5 proposals given; 6 tables in chat; 7 not offered |
| Not done | Tie to a ledger, receipts by funder, transaction listing for audit: need a ledger export by class |

**Data sources:** user-uploaded `grant_awards_and_spending.md` and `nonprofit_trial_balance_and_gifts.md`; intake answers (organisation, period, currency). No ledger read.
