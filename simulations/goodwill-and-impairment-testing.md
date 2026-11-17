# Goodwill impairment test — Northbrook Trading Ltd, Harlow reporting unit, 30 September 2025

This run is manual: no Mosofin connection is present. Everything below comes from the files you uploaded. Nothing has been posted, sent or changed.

## (a) Read-back

Testing goodwill for **Northbrook Trading Ltd** at **30 September 2025** under **US GAAP (ASC 350)**, across **one reporting unit, "Harlow"**, with goodwill of **750,000 allocated entirely to Harlow as you supplied**, from **the projections and the 10.5% post-tax rate you uploaded**, in **USD**. Company, period and currency are as you stated them; nothing confirms them against a connection.

Taken from the files, for you to confirm: the test date, the framework, the unit, the allocation, the projections, the rate and its basis, and the trigger (loss of a major customer in August 2025). Not answered anywhere: **the basis of the goodwill allocation** (it is all in one unit, so nothing is split; I record the basis as "single acquired business") and **your annual test date**. Because a trigger is reported, this is an **interim test** either way.

What I received:
- `acquisition_terms_and_valuation.md` — the Harlow acquisition summary at 1 July 2025: consideration, and a book-value / fair-value table.
- `impairment_inputs.md` — test inputs: goodwill 750,000, unit carrying amount 1,620,000, five years of free cash flow 2026–2030, terminal growth 2.5%, rate 10.5% post-tax, the trigger.
- `impairment_inputs_final.csv` — three rows, columns employee / week_1..week_4, values nights / days / off.

## (b) Validation of the upload (before any work)

| File | What it actually is | Right company and period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `impairment_inputs.md` | A one-page summary of test inputs: carrying amount, goodwill, projections, rate, trigger | Test date 30 Sep 2025, US GAAP, matches intake. **The entity is not named in the file** (only the unit "Harlow"); currency not stated | Yes. Every figure identifiable | Steps 1–4, 7, 9 | **Accepted with a limit**: company and currency user-asserted. It is a summary: the carrying amount is one figure, not a balance sheet of the unit; the rate memo is cited, not supplied. Every figure is user-supplied, not evidenced |
| `acquisition_terms_and_valuation.md` | The acquisition summary that created the goodwill (1 July 2025) | Northbrook Trading Ltd acquiring Harlow Fabrication Ltd; three months before the test date | Yes; foots | Step 0b / 1 only: traces the 750,000 of goodwill to its origin and identifies the intangibles in the unit | **Accepted with a limit**: used only to trace goodwill and list the unit's intangibles. Its values are at 1 July 2025, not the test date, and are not used as carrying amounts |
| `impairment_inputs_final.csv` | A four-week staff shift roster for employees E08–E10 | No company, date or amount | Not for this skill | No step uses it | **Rejected**. The name suggests final impairment inputs; the content is a rota. Set aside. If a final version of the inputs exists, please upload it |

**Still missing:** the carrying amounts **by asset** within the Harlow unit (required; one total received), the discount rate derivation memo (required; cited only), market data for a market approach (recommended), Harlow's actual results since acquisition (needed to compare the projection to history), and the undiscounted cash flows and carrying amount of the customer relationships asset group (needed for the long-lived asset test below). I would stop here and wait for your answer.

*You replied: go ahead with the accepted files.*

## (c) Findings

**1. Scope.** Goodwill exists (750,000), so the ASC 350 test applies. The acquisition summary shows two intangibles in the unit at 1 July 2025: **customer relationships 260,000** (finite-lived, amortised) and **trade name 90,000** (life not stated). Their carrying amounts at 30 September were not supplied.

**2. Goodwill traces to the acquisition.** Fair value of net assets at 1 July 2025: 205,000 + 195,000 + 410,000 + 260,000 + 90,000 − 240,000 − 90,000 = **830,000**. Consideration 1,400,000 + 180,000 = 1,580,000. Goodwill 1,580,000 − 830,000 = **750,000**, which agrees to the test inputs. Deferred tax 90,000 = 20% × uplifts of 450,000; it ties.

**3. Triggering event.** Loss of a major customer in August 2025, three months into ownership. This requires an **interim test now**, independent of the annual test date. The qualitative assessment (US GAAP "Step 0") is not a good fit with a known trigger, so I go straight to the quantitative test. Customer revenue by period was not supplied, so the size of the loss is not measured. The other six indicators (market value, business climate, cost overruns, market capitalisation, legal, restructuring) are **not assessed**: owner, Northbrook finance.

**4. Order of testing — the customer relationships asset must be tested first.** Under US GAAP, long-lived assets in the unit are tested under ASC 360 before goodwill, and the goodwill test then uses their post-impairment carrying amounts. A lost major customer is a direct trigger for the **customer relationships intangible (260,000 at acquisition)**: if that customer was part of the relationships valued, the asset may not be recoverable. That test needs the undiscounted cash flows of the relationships and their carrying amount at 30 September, neither supplied. **Not done.** Any impairment there reduces the unit's carrying amount of 1,620,000 before the goodwill comparison below. If the trade name is indefinite-lived, it also needs its own test before goodwill.

**5. Fair value of the Harlow unit (income approach, your inputs).** Free cash flows discounted at 10.5%, 2026 treated as one full year after the test date (end-of-year convention):

| Year | Free cash flow | Discount factor | Present value |
|---|---:|---:|---:|
| 2026 | 150,000 | 0.904977 | 135,747 |
| 2027 | 165,000 | 0.818984 | 135,132 |
| 2028 | 180,000 | 0.741162 | 133,409 |
| 2029 | 190,000 | 0.670735 | 127,440 |
| 2030 | 200,000 | 0.607000 | 121,400 |
| Terminal value: 200,000 × 1.025 ÷ (10.5% − 2.5%) = 2,562,500 | | 0.607000 | 1,555,437 |
| **Fair value of the unit** | | | **2,208,565** |

The terminal value is **70%** of the fair value. Basis check: a **post-tax** rate applied to free cash flows (post-tax) is consistent for a US GAAP fair value. Timing: cash flows for October–December 2025 were not supplied; if the forecast years end 31 December, discounting from 30 September adds a quarter to every period and the value is **2,009,961**. Please confirm the forecast year-end.

**6. The comparison (ASC 350, post ASU 2017-04).**

| | Amount |
|---|---:|
| Carrying amount of Harlow including goodwill | 1,620,000 |
| Fair value from your projections and rate | 2,208,565 |
| Fair value minus carrying amount (headroom) | **588,565 (36% of carrying)** |
| Impairment by the formula: carrying − fair value, capped at goodwill 750,000 | **0** |

On these inputs the arithmetic shows no shortfall. **This is the comparison, not a conclusion**: the carrying amount still has to come down by any ASC 360 impairment of the customer relationships (finding 4), and the projections have not been compared to actual results.

**7. Sensitivity** (fair value; impairment in brackets, capped at 750,000):

| Rate \ terminal growth | 1.5% | 2.0% | 2.5% | 3.0% |
|---|---:|---:|---:|---:|
| 10.5% | 2,022,250 (0) | 2,109,927 (0) | 2,208,565 (0) | 2,320,354 (0) |
| 11.5% | 1,814,018 (0) | 1,882,123 (0) | 1,957,795 (0) | 2,042,369 (0) |
| 12.5% | 1,643,821 (0) | 1,697,873 (0) | 1,757,330 (0) | 1,823,045 (0) |

Breakeven: the rate would have to rise to **13.3%**, or terminal growth fall to **−1.8%**, or every cash flow fall by **26.6%**, before fair value equals 1,620,000.

**8. The projection after a customer loss.** The forecast grows every year from 150,000 to 200,000 (+33% over four years) immediately after losing a major customer. Harlow's actual cash flows were not supplied, so I cannot compare; I record this as an observation for whoever prepared the forecast, not a judgment.

**9. Proposed entry.** None: the formula gives zero impairment on the inputs supplied. Had there been a shortfall it would be: debit impairment loss (operating P&L), credit goodwill. **US GAAP: goodwill impairment is never reversed.**

**10. Disclosure data available:** unit Harlow; goodwill 750,000; method income approach; rate 10.5% post-tax; terminal growth 2.5%; five-year horizon; headroom 588,565; sensitivity as above; trigger: loss of a major customer, August 2025.

## (d) What was not done, and why

- **ASC 360 test of customer relationships (and trade name if indefinite-lived)** — no undiscounted cash flows or carrying amounts by asset. Owner: Northbrook finance / valuation specialist. It must precede the goodwill test.
- **Projection compared to history** — no actual results for Harlow. Needs a P&L by month since 1 July 2025.
- **Discount rate derivation** — the memo is cited, not uploaded; 10.5% is user-supplied. Owner: valuation specialist.
- **Market approach** — no market data.
- **Goodwill allocation basis** — single unit, so not tested; confirm nothing else carries this goodwill.
- **Fair value itself** — computed only on your inputs; a material test should be reviewed by a valuation specialist.
- **Excel workpaper** (`Impairment_Test_2025-09_Northbrook Trading Ltd.xlsx`) — not created; say if you want it.
- **Posting** — this skill never posts.

## Coverage (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, 30 Sep 2025, USD — user-asserted. Source: upload. `impairment_inputs.md` accepted with a limit (summary; company user-asserted); `acquisition_terms_and_valuation.md` accepted with a limit (goodwill trace only); `impairment_inputs_final.csv` rejected (staff roster) |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 0 not applicable; 0b done with a limit (from upload, not balance sheet); 1 done; 2 done with a limit (one indicator supplied, six not assessed, no trend data); 3 not used (trigger present); 4 done with a limit; 5 not applicable (US GAAP); 6 **not done** (inputs missing); 7 done on your inputs, with sensitivity; 8 not applicable; 9 no entry; 10 data listed; 11 tables in chat; 12 not offered |
| Not done | Tie to a balance sheet, segment and customer trend, prior impairment history: each needs the ledger or a trial balance and P&L by period |

**Data sources:** user-uploaded `impairment_inputs.md` (all test inputs) and `acquisition_terms_and_valuation.md` (goodwill trace); intake answers (company, period, currency). No ledger read.
