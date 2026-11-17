# Contingencies — Northbrook Trading Ltd — at 30 September 2025

Mosofin is not connected, so this run is manual: every step is `[manual]` and every figure comes from your uploads. Connecting Mosofin would read legal spend by firm and month, accruals and settlements directly ([docs.mosofin.com](https://docs.mosofin.com)).

## Read-back

Evaluating contingencies (possible losses not yet settled) for **Northbrook Trading Ltd** (user-asserted) at **30 September 2025**, in **USD** (user-asserted), under **US GAAP**, from **your uploads**. **Three matters** on your list, each assessed by **the general counsel** (two dated 28 Sep 2025, one undated). Counsel: **Greyfriars Legal LLP**. **No matter is privileged**, and insurance is a **product liability policy with a 10,000 deductible**. The framework, privilege status and insurance terms arrived inside `legal_matters.md`; used once you confirm them here.

Not answered and treated by default: counsel's letters, the insurance policy and last year's disclosure (F) — **listed as not supplied**.

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Needed for | Verdict |
|---|---|---|---|---|---|
| `legal_matters.md` | Matter list: 3 matters with type, counsel, management's likelihood, estimate, who gave it | "At 30 September 2025"; no entity named | Yes. A **summary** of counsel's view, not counsel's letters | Steps 1–4 (population, classification, measurement, disclosure) | **Accepted with a limit**: company user-asserted; probabilities and ranges are **user-supplied, not evidenced** by counsel letters |
| `general_ledger_2025-09.csv` | GL extract: 29 lines, 15 bank lines (cash side only) and 7 journals (JE-0901 to 0907, balanced) | No entity; Sep 2025 (one JE dated 31 Aug) | Yes, with limits: bank lines are one-sided, so the extract does not foot (259,778 / 276,104) by design; **no opening balance on 2100 Accrued Liabilities**; no dedicated litigation or warranty account | Step 0 (existing accruals, settlements), Step 0b (sweep) | **Accepted with a limit**: one month only; cannot show the accrual already carried |
| `vendor_master.csv` | Vendor master, 12 vendors, with **2025 paid totals** (950,780) | No entity; "paid_2025", end date not stated | Yes for identifying law firms and their annual spend; no monthly detail | Step 0b (sweep) | **Accepted with a limit**: annual totals only, so no fee trend by month |
| `legal_matters_final.csv` | **An employee shift rota** (E08–E10, weeks 1–4). Not a matter list despite its name | None | n/a | No step uses it | **Rejected.** If an updated matter list exists, upload it instead |

**Still missing:** (1) the **balance on 2100 Accrued Liabilities at 30 Sep and its make-up** (to know whether any amount is already provided for the brackets claim — required to propose only the movement); (2) **counsel's letters**; (3) the **insurance policy** and any notice of claim to the insurer; (4) **prior-year disclosure**; (5) the **date** of the remote assessment on the supplier counterclaim. I would wait here; proceeding on the accepted files as instructed.

## Completeness sweep (Step 0b) — run, on limited data

| Signal | Evidence | Matched to a listed matter? | Question for management / counsel |
|---|---|---|---|
| Law firm spend | Greyfriars Legal LLP, paid 27,400 in 2025 (the only law firm in the vendor master) | Yes — counsel on all three matters | None; fees do not indicate likelihood and are not used as such |
| Legal fee accrual | JE-0905, 31 Aug: 3,800 "Legal fee missed in August" to 6400 Professional Fees / 2100 | Firm and matter not named | Which firm and which matter does the 3,800 relate to? |
| Unidentified payment | CHECK 2287, 3 Sep, 8,400, no payee | Unknown | Who was CHECK 2287 paid to? (asked only to exclude a settlement) |
| Insurance recoveries | None received in the extract | — | Has the brackets claim been notified to the product liability insurer? |
| Warranty / rework cost | No warranty or rework account in the extract | — | Is defective-bracket rework being booked anywhere? |

Nothing found suggests an unlisted matter; the two open items are questions, not assertions. Limit: one month of GL and annual vendor totals — a monthly fee trend could not be tested.

## Contingency log and treatment

| Ref | Matter | Likelihood (management) | Estimate | Source, date | Treatment | Amount |
|---|---|---|---|---|---|---|
| M1 | Customer claim, defective brackets (litigation) | **Probable** | **40,000 – 70,000**, no best estimate given | General counsel, 28 Sep 2025 | **Accrue the minimum of the range** (US GAAP, no point better than another) **and disclose** the further reasonably possible loss | **Accrue 40,000**; disclose up to a further **30,000** |
| M2 | Former employee claim (employment) | **Reasonably possible** | Up to 25,000 | General counsel, 28 Sep 2025 | **Disclose, no accrual** | Disclose range 0 – 25,000 |
| M3 | Supplier counterclaim (litigation) | **Remote** | — | General counsel, **undated** | **No accrual, no disclosure** | — · assessment date needed |

If counsel can name a best estimate inside 40,000–70,000, that figure replaces the minimum.

## Proposed entry (proposal only — not posted)

M1, at 30 September 2025:

DR Legal and claims expense (account to confirm; no such account in the extract — 6400 Professional Fees is the nearest) **40,000** / CR Accrued Liabilities – litigation (2100 or a separate provision account) **40,000**. *Memo: Accrue minimum of probable range, customer claim re defective brackets, per general counsel 28 Sep 2025.*

**This is the gross amount, proposed as the movement only on the assumption that nothing is already provided.** The September GL shows no such accrual, but without the 2100 opening balance I cannot rule out an earlier one. Confirm before posting, to avoid re-accruing.

**Insurance — not netted.** Above the 10,000 deductible the policy may respond for up to 30,000 of the 40,000 accrued (60,000 at the top of the range). No recovery is recognised: no policy terms or insurer acknowledgement were supplied, and a recovery is recorded separately, only when realisation is assured. The gross 40,000 stays on the balance sheet.

## Draft disclosure (for legal review)

> *The Company is a defendant in a claim brought by a customer alleging defective brackets. Management, with counsel, considers a loss probable and has accrued 40,000, the low end of an estimated range of 40,000 to 70,000; it is reasonably possible that the loss could exceed the amount accrued by up to 30,000. The Company carries product liability insurance subject to a 10,000 deductible; no recovery has been recognised.*
>
> *A former employee has brought a claim against the Company. Management considers a loss reasonably possible but not probable, and estimates the possible loss at up to 25,000. No amount has been accrued.*

Nothing in this wording goes beyond the assessment supplied. You said no matter is privileged, so matters are described by type; counterparties are not named.

## Controls (Step 5)

Legal letters from Greyfriars at 30 Sep: **not supplied** — request them. Refresh of assessments: M3 undated, so overdue by default. Review and sign-off: **CFO and general counsel — please name who signs.**

## Not done, and why

Movement against the existing accrual (no 2100 balance); evidence of probabilities (no counsel letters); recovery assessment (no policy); comparison to prior disclosure (not supplied); monthly fee trend (annual vendor totals only). Excel workpaper `Contingencies_2025-09_Northbrook Trading Ltd.xlsx` and a Word disclosure offered; not created without your yes.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, 30 Sep 2025, USD, US GAAP — **user-asserted**. Source: **upload** (Mosofin not used, your choice). Matter list, GL extract, vendor master: accepted with limits. `legal_matters_final.csv`: **rejected** (shift rota) |
| Capability map | Not applicable: no connection. Every task is `[manual]`; every probability and estimate is **management's (general counsel)** |
| Steps | 0 done with a limit · 0b **run**, limited to one month and annual totals · 1 done · 2 done · 3 done, movement **not confirmed** · 4 drafted · 5 owners to name · 6 not offered |
| Not done | 2100 balance and detail; counsel letters; insurance terms; prior-year disclosure; M3 assessment date |

Nothing was posted, sent or changed. **Data sources:** upload — `legal_matters.md`, `general_ledger_2025-09.csv`, `vendor_master.csv`.
