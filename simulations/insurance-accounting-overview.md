# Insurance close map — Harbour Mutual, September 2025

This run is manual: no Mosofin connection is present. Everything below comes from the file you uploaded. No reserve has been estimated. Nothing has been posted, sent or changed.

## (a) Read-back

Mapping the close for **Harbour Mutual**, a **carrier**, for **September 2025**, in **USD**, from **the close schedules summary you uploaded**. **Regulated**; reserves from **the actuary's quarterly report dated 30 September 2025**, as quoted. **One 30% quota share treaty.** Company, period and currency are as you stated them.

Taken from the file, for you to confirm: the business model (carrier), that it is regulated, the treaty, and the actuary's IBNR. Not answered anywhere: **the regulatory regime** (regulatory items listed as not assessed), **the actuary's name and valuation cadence beyond "quarterly"**, **the treaty's terms beyond 30%** (what business it covers, ceding commission), and **investment holdings and custodian**.

What I received:
- `insurer_close_schedules_2025-09.md` — a one-page summary: business model, written premium, unearned premium (opening, policy system, ledger), paid claims, case reserves, IBNR (actuary and ledger), reinsurance recoverable with ageing, commissions and opening deferred acquisition costs.
- `insurer_close_schedules_2025-09_final.csv` — three rows, columns employee / week_1..week_4, values nights / days / off.

## (b) Validation of the upload (before any work)

| File | What it actually is | Right company and period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `insurer_close_schedules_2025-09.md` | A summary of September close figures for an insurance carrier, quoting the policy system and the actuary | Harbour Mutual, September 2025; currency not stated (USD from intake) | Yes; each figure identifiable | Steps 0b, 1–4, 6 | **Accepted with a limit**: it is a summary in place of the policy data, the claims data and the actuary's report (all required for a carrier). Every figure is **user-supplied, not evidenced**; no claim-level, policy-level or accident-year data, so no recomputation, no development analysis |
| `insurer_close_schedules_2025-09_final.csv` | A four-week staff shift roster for employees E08–E10 | No company, date or amount | Not for this skill | No step uses it | **Rejected**. The name suggests final close schedules; the content is a rota. Set aside. If final schedules exist, please upload them |

**Still missing:** premium and policy data for the period (required for a carrier), claims data and the actuary's reserve report itself (required), the reinsurance treaty (recommended), prior close schedules (recommended; only opening UPR and DAC given), the custodian statement for investments. I would stop here and wait for your answer.

*You replied: go ahead with the accepted file.*

## (c) Findings

**1. Business model.** Stated as a carrier, and the figures carry a carrier's signature: unearned premium reserve, case reserves, IBNR (claims incurred but not yet reported), reinsurance recoverable, deferred acquisition costs. No client money accounts appear, so the client money reconciliation does not apply. Consistent.

**2. Unearned premium reserve (UPR): the ledger is 70,000 short of the policy system.**

| | Policy system | Ledger |
|---|---:|---:|
| Opening UPR | 2,100,000 | 2,100,000 |
| Add written premium, September | 900,000 | 900,000 |
| Less premium earned (balancing figure) | (750,000) | (820,000) |
| **Closing UPR** | **2,250,000** | **2,180,000** |
| **Difference** | | **70,000 (ledger under)** |

With the ledger's UPR 70,000 too low, earned premium for September is overstated by 70,000. The policy system is the source for UPR; I have not recomputed it (that needs policy inception and expiry dates). The half-of-annual-premium reasonableness test cannot run on one month of written premium.

**3. IBNR: the ledger is 60,000 below the actuary.** Actuary's quarterly report at 30 September 2025: 760,000; ledger 700,000. The actuary's figure is the one to book; this skill does not estimate IBNR, and neither balance is evidence that reserves are adequate. Case reserves of 1,300,000 come from the claims system; their ledger balance was not given, so not tied. Gross loss reserves per the source systems: 1,300,000 + 760,000 = **2,060,000**.

**4. Reinsurance (30% quota share): gross and ceded both shown.**

| Item | Gross | Ceded at 30% | Net |
|---|---:|---:|---:|
| Paid claims, September | 410,000 | 123,000 | 287,000 |
| Case reserves + IBNR (actuary) | 2,060,000 | 618,000 | 1,442,000 |
| Written premium, September | 900,000 | 270,000 | 630,000 |

The recoverable on paid claims, **123,000, agrees to 30% × 410,000**. **48,000 of it (39%) is over 90 days**: a credit exposure, not cash, and a sign that something is disputed or the reinsurer is slow. Counterparty and reason not supplied. The ceded share of reserves (618,000) and ceded premium (270,000) are arithmetic on the stated 30% only; whether the treaty covers all business, and its ceding commission, need the treaty. The policyholder is still owed the gross amount: reinsurance does not discharge it.

**5. Acquisition costs.** Commissions paid 135,000 = **15.0%** of September written premium. Opening deferred acquisition costs 310,000 are 14.8% of opening UPR, consistent with a 15% commission deferred over the earning pattern. Closing DAC and September amortisation were not supplied; they follow the premium earning pattern from the policy system, so I have not computed them.

**6. Investment income.** No figures supplied. Named source: the custodian statement.

**7. Effect of the two differences (proposals, before tax).**

| | Gross | Reinsurer's 30% share | Net |
|---|---:|---:|---:|
| UPR shortfall (earned premium overstated) | 70,000 | 21,000 | 49,000 |
| IBNR shortfall (claims understated) | 60,000 | 18,000 | 42,000 |
| **Result overstated by** | **130,000** | **39,000** | **91,000** |

The ceded column applies only if the quota share covers the business concerned; confirm against the treaty.

**8. Proposed entries — PROPOSALS, NOT POSTED** (generic account names; no chart supplied).
- Dr change in unearned premium (premium revenue) 70,000 / Cr unearned premium reserve 70,000.
- Dr claims incurred 60,000 / Cr IBNR reserve 60,000.
- If the treaty applies: Dr reinsurers' share of IBNR 18,000 / Cr ceded claims 18,000; and the matching ceded UPR adjustment of 21,000.

**9. Close checklist (carrier) — owners to confirm.**

| Task | Source | Owner | Status this month |
|---|---|---|---|
| Premium roll-forward and UPR | Policy system | Underwriting / finance | Done on summary; **70,000 difference** |
| Case reserves | Claims system | Claims | Ledger tie not possible |
| IBNR and LAE | Actuary (quarterly) | Actuary | **60,000 difference**; LAE not supplied |
| Loss reserve roll-forward and development triangles | Claims by accident year | Actuary / claims | Not done: no data |
| Reinsurance recoverables and ageing | Treaty, reinsurer statements | Reinsurance | Tied for paid claims; 48,000 over 90 days |
| Commissions and DAC | Policy system | Finance | Closing DAC not supplied |
| Investment income | Custodian | Treasury | Not supplied |
| Regulatory returns | Regime not stated | Compliance | Not assessed |

## (d) What was not done, and why

- **UPR, DAC and cession recomputation** — needs policy-level dates and the treaty.
- **Loss reserve roll-forward, development triangles, reserve adequacy** — needs claims by accident year and the actuary's report itself.
- **Ledger tie for case reserves, ceded balances, commissions payable** — ledger balances not supplied.
- **Regulatory items** — regime not stated.
- **Excel workpaper** (`Insurance_Close_Map_2025-09_Harbour Mutual.xlsx`) — not created; say if you want it.
- **Posting** — this skill never posts.

## Coverage (manual run)

| Section | Content |
|---|---|
| Environment | Harbour Mutual, carrier, September 2025, USD — user-asserted. Source: upload. Close schedules summary accepted with a limit (summary of policy, claims and actuarial data); `_final.csv` rejected (staff roster) |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 0b done; 1 done with a limit (UPR tie); 2 done with a limit (IBNR tie only); 3 done with a limit; 4 done with a limit; 5 not done; 6 checklist given, client money not applicable; 7 tables in chat; 8 not offered |
| Not done | Ledger ties beyond UPR and IBNR, prior-period roll-forwards: need a trial balance and last close's schedules |

**Data sources:** user-uploaded `insurer_close_schedules_2025-09.md` (all figures; policy system and actuary as quoted); intake answers (company, period, currency). No ledger read.
