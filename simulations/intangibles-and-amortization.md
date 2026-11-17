# Intangibles and amortisation — Northbrook Trading Ltd — as at 30 September 2025

Mosofin is not connected, so this run is manual: every step is `[manual]` and every figure comes from your uploads. Connecting Mosofin would read the intangible accounts and their movements directly ([docs.mosofin.com](https://docs.mosofin.com)).

## Read-back

Reviewing intangibles for **Northbrook Trading Ltd** (user-asserted) **as at 30 September 2025** (period: September 2025), in **USD** (user-asserted), under **US GAAP** (you, and confirmed by `accounting_policies.md`: "US GAAP. Private company."), from **your uploads**. **No intangibles register exists** (you), so only totals and movements can be reconciled; asset-level amortisation is not checked.

Not answered, and the skill's default applied:
- **E — useful life / indefinite status and method per class: not supplied.** The policies file gives lives for fixed assets (3–10 years) but **none for intangibles**. Default: report the charge in the books against the balances and **compute no new amortisation**. I do not pick a life.
- **F — capitalisation policy for internal development and stage dates: not supplied.** No development spend appears in the files. Default: capitalise nothing.

From `acquisition_terms_and_valuation.md` (facts inside a file; used once you confirm them here): Northbrook acquired **100% of Harlow Fabrication Ltd on 1 July 2025**; identified intangibles at fair value **customer relationships 260,000** and **trade name 90,000** (valuation report dated 20 Aug 2025). Please confirm.

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Needed for | Verdict |
|---|---|---|---|---|---|
| `trial_balance_2025-09-30.csv` | Trial balance, 33 accounts; debits 6,546,018 = credits 6,546,018 (foots) | No entity or currency named; date from file name only | Yes — balances only, **no ledger detail** | Steps 0b, 1, 10 (tie-out), 11 | **Accepted with a limit**: company and period user-asserted; balances only, so additions, disposals and the charge's pattern cannot be read |
| `acquisition_terms_and_valuation.md` | Summary of the Harlow deal terms and a table quoted from the valuation report | Northbrook Trading Ltd; acquisition 1 Jul 2025; US GAAP — matches intake | A **summary**, not the valuation report or the purchase agreement | Steps 1, 2, 5, 10, 11 | **Accepted with a limit**: every figure from it is **user-supplied, not evidenced**; lives, the trade name's renewal basis and valuation method are not in it |
| `accounting_policies.md` | Company accounting policies (framework, revenue, inventory, fixed assets, receivables) | No entity named; US GAAP, private company | Yes, but **no intangibles policy** and no development capitalisation policy | Intake C; Step 2 (shows the gap) | **Accepted with a limit**: confirms US GAAP; supplies no intangible life or method |
| `acquisition_terms_and_valuation_final.csv` | **An employee shift rota** (E08–E10, weeks 1–4: days / nights / off). Not acquisition or valuation data despite its name | None | n/a | No step uses it | **Rejected.** If a final valuation or a revised purchase price allocation exists, upload that instead |

**Still missing:** (1) **ledger detail** for any intangible, goodwill and accumulated amortisation accounts (required); (2) **useful life or indefinite status and method** for customer relationships and the trade name (required to compute any charge); (3) the **valuation report itself** and the purchase agreement; (4) whether the acquisition has been recorded anywhere — Northbrook's books, Harlow's books (push-down) or only a consolidation workpaper; (5) whether Northbrook, as a private company, has elected the **private-company alternatives** for goodwill and customer-related intangibles. I would wait here; proceeding on the accepted files as instructed.

## Step 0b — Is amortisation being charged at all?

| What the trial balance shows | Amount |
|---|---:|
| Intangible asset accounts (any class) | **none** |
| Accumulated amortisation | **none** |
| Amortisation expense | **none** (6600 Depreciation 37,800 is fixed assets) |
| Goodwill | **none** |
| Investment in Harlow Fabrication Ltd | **none** (the only investment is 1600 Investment in Northbrook UK Ltd, 104,800) |
| Earnout liability | **none** |

**Finding 1 — the acquired intangibles are not in the trial balance at all.** Customer relationships **260,000** and trade name **90,000** (total **350,000**) were acquired on 1 July 2025 and have **no cost, no accumulated amortisation and no charge** three months later. This is the GL → register gap at its worst: an intangible with no account will never be amortised. Nor is there any trace of the deal itself — no investment in Harlow (cost 1,400,000 cash + 180,000 earnout fair value = **1,580,000**), no earnout liability of 180,000. Either the acquisition is recorded only in a consolidation workpaper not supplied, or it has not been recorded. Please tell me which.

**Finding 2 — no amortisation can be computed, because no life has been set.** Customer relationships are finite-lived; amortisation runs from the acquisition date, so **three months (July–September) are due by 30 September** and **one month in September**, at 260,000 ÷ (life in months) per month. The trade name is finite **or** indefinite depending on whether renewal is expected — that is your call, with renewal evidence. **I have not chosen a life and I propose no charge** until you give one per class.

**Finding 3 — if the trade name is indefinite-lived, an annual impairment test is mandatory** (qualitative first under US GAAP) and none is evidenced. Please confirm the test date you will use.

## Purchase price check (from the summary; user-supplied, not evidenced)

| | Amount |
|---|---:|
| Consideration: cash 1,400,000 + earnout at fair value 180,000 | 1,580,000 |
| Net assets at fair value: 205,000 + 195,000 + 410,000 + 260,000 + 90,000 − 240,000 − 90,000 | 830,000 |
| **Implied goodwill** | **750,000** |

- Deferred tax ties: uplifts −5,000 + 15,000 + 90,000 + 260,000 + 90,000 = 450,000 × 20% = **90,000**, as stated.
- **Goodwill of 750,000 is not amortised here** — route it to the goodwill impairment test (Step 1). As a private company Northbrook may have elected the US GAAP private-company alternative to amortise goodwill, and to subsume customer-related intangibles that cannot be sold separately into goodwill; that election would change both the 260,000 and the 750,000. **Not assumed — please confirm.**
- Deal costs **46,000** are expensed under US GAAP, not capitalised. 6400 Professional Fees totals only **36,500**, less than 46,000, so at least **9,500** of deal costs sits somewhere other than professional fees (or was capitalised) — cannot be traced without ledger detail.
- The 15,000 inventory step-up and 90,000 fixed-asset uplift belong to inventory and `fixed-asset-register-and-depreciation`, not here.

## Roll-forward by class (30 September 2025)

| Class | Opening cost | Additions | Closing cost | Accum. amortisation | NBV | Per GL | Difference |
|---|---:|---:|---:|---:|---:|---:|---:|
| Customer relationships | 0 | 260,000 (1 Jul) | 260,000 | **not computed — no life** | — | 0 | **260,000 not in GL** |
| Trade name | 0 | 90,000 (1 Jul) | 90,000 | **not computed — life / indefinite not set** | — | 0 | **90,000 not in GL** |
| **Total** | 0 | 350,000 | 350,000 | — | — | 0 | **350,000** |

Opening cost assumed nil: no intangible account appears and no prior register exists. Register → GL: no register, so no phantom list. GL → register: no intangible account in the GL. The disposals half-entry check, the implied-life check and the capitalisation scan both ways have **nothing to run on** (no balances, no ledger detail, no development spend).

## Proposed entries (proposals only — not posted)

- **No amortisation entry proposed** until lives are set. Its form, once they are: DR Amortisation Expense / CR Accumulated Amortisation – Customer relationships (and – Trade name if finite), for 1 July–30 September.
- **No entry proposed to record the acquisition** — where it belongs (Northbrook's books as an investment, push-down to Harlow, or consolidation only) is a decision for you and `business-combinations-asc805`.

## Disclosure inputs

Cost by class: customer relationships 260,000, trade name 90,000 (user-supplied). Accumulated amortisation, period expense, weighted average remaining life and the **5-year amortisation forecast: not produced — no lives**. Indefinite-lived candidate: the trade name, pending your decision. Impairment charges: none evidenced; none concluded.

## Not done, and why

Amortisation for the period and the proposed charge (no lives — skill never picks one). Accumulated amortisation, NBV, 5-year forecast and weighted average remaining life (same). Implied-life check (no charge in the books). Capitalisation of internal development and the two-way scan (no policy, no stage dates, no development spend or ledger detail). Disposal half-entry check (no ledger detail). Impairment: indicators only and **never concluded**; none readable. Excel workpaper `Intangibles_Register_2025-09.xlsx` offered; not created without your yes.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, as at 30 Sep 2025, USD, US GAAP — **user-asserted**. Source: **upload** (Mosofin not used, your choice). TB: accepted with limit (balances only). Acquisition summary: accepted with limit (user-supplied, not evidenced). Policies: accepted with limit (no intangible policy). `acquisition_terms_and_valuation_final.csv`: **rejected** (shift rota) |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 0b done — **no intangible, amortisation or goodwill account exists** · 1 done (customer relationships, trade name; goodwill 750,000 routed out) · 2 **not done** (no lives) · 3 **not done** (no method) · 4 / 4b **not done** (no development data) · 5 **not done** · 6 form only, no amount · 7 indicators only; trade name annual test flagged · 8 not applicable (no lives yet) · 9 not done (no ledger detail) · 10 done with limit — 350,000 not in GL · 11 cost by class only · 12 tables here; xlsx offered · 13 not offered |
| Not done | Tie to GL detail and movements (needs intangible / goodwill ledger detail); amortisation and forecast (needs lives per class); deal-cost trace (needs professional fees detail); private-company elections (needs your confirmation) |

Nothing was posted, sent or changed. **Data sources:** upload — `trial_balance_2025-09-30.csv`, `acquisition_terms_and_valuation.md`, `accounting_policies.md`.
