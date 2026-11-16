# Subsequent events review — Northbrook Trading Ltd — balance sheet date 30 September 2025

Mosofin is not connected, so this run is manual: every step is `[manual]` and every figure comes from your uploads. Nothing is classified, posted or concluded here; management concludes.

## Read-back

Reviewing subsequent events for **Northbrook Trading Ltd** (user-asserted), USD, US GAAP (ASC 855 — the framework is stated in `legal_matters.md`), from **30 September 2025** to an issue date of **20 March 2026**. Data source: **upload only**.

| Intake question | Treatment |
|---|---|
| C — issue date and definition | Date given (20 Mar 2026). **Definition not given** (issued vs available to be issued). Please confirm; it belongs in the disclosure. |
| D — estimates that matter most | Not answered. Default: **test every reserve and accrual account found** — allowance for doubtful accounts (1150), accrued liabilities (2100), the legal matters, and inventory (no reserve account exists). |
| E — management events by category | **Not answered.** Listed below as not answered, by category. |
| F — board minutes / legal updates since 30 Sep | Not supplied. **Not reviewed.** The legal matters schedule is dated 28 Sep 2025, before the period end. |

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Step that uses it | Verdict |
|---|---|---|---|---|---|
| `trial_balance_2025-09-30.csv` | TB, 33 accounts; Dr = Cr 6,546,018. AR 798,360, allowance 9,000, accrued liabilities 28,800 | No entity named; date from name | Yes | Period-end balances for the estimates | **Accepted with a limit**: company user-asserted |
| `ar_aging_detail_2025-09-30.csv` | AR aging by invoice, 14 lines, total **798,360** = TB 1100 | Aged at 30 Sep 2025 | Yes | Step 2b receivable patterns | **Accepted with a limit**: company user-asserted |
| `legal_matters.md` | Legal matters schedule, 3 matters, management's view and counsel's estimate | At 30 Sep 2025 | Yes — a summary, not counsel's letters | Step 2b settlement pattern; Step 3 | **Accepted with a limit**: summary prepared by GC; figures user-supplied, not evidenced; no post-period legal update |
| `post_period_ledger_2025-10.csv` | Post-period ledger detail, 4 entries, 6–20 Oct 2025 | October 2025 | Yes | Step 2 sweep | **Accepted with a limit**: covers **October 2025 only**; 1 Nov 2025 – 20 Mar 2026 is unswept |
| `post_period_ledger_2025-10_final.csv` | **Not a ledger.** A staff shift rota: employees E08–E10, weeks 1–4, "days/nights/off". No dates, accounts or amounts | n/a | No | None | **Rejected** — wrong document despite its name. If a "final" October ledger exists, upload that; otherwise upload ledger detail from 1 Nov 2025 to the issue date. |

**Still missing:** ledger detail from 1 November 2025 to 20 March 2026 (required — the window runs to issue); management's answers by category (required for non-recognised events); board minutes and legal updates since 30 Sep (recommended); the allowance computation and the make-up of accrued liabilities 28,800 (to see whether the bracket claim is accrued). I would wait for your answer here; proceeding on the accepted files.

## Completeness statement

*The transactional sweep covered every entry in the uploaded post-period ledger, 1–31 October 2025 (4 entries). Nothing after 31 October 2025 has been swept. Non-transactional events are covered only by the enquiries recorded below, none of which has been answered.* The window is **still open**.

## Ledger sweep detail (candidates, not classifications)

| # | Pattern | Counterparty | 30 Sep position | Post-period transaction | Date | Days after | Amount | Candidate type |
|---|---|---|---:|---|---|---:|---:|---|
| 1 | Litigation settled after period end; claim predates it | Customer claim, defective brackets | Probable, range 40,000–70,000; accrual not visible in TB | Settlement paid, coded 6400 Professional Fees | 14 Oct 2025 | 14 | **52,000** | Recognised (Type 1) candidate |
| 2 | Pre-period receivable written off | Foxhall Garden Centres (administration) | 4,003, 130 days overdue | Write-off against allowance 1150 | 9 Oct 2025 | 9 | **4,003** | Recognised candidate |
| 3 | Pre-period receivable paid after period end (favourable) | Pennine Retail Group | 112,071, 12 days overdue | Receipt in full | 6 Oct 2025 | 6 | **112,071** | Recognised candidate — evidence of collectibility |
| 4 | Credit note after period end | Returned PN-55 panels (customer not named) | Unknown — no invoice reference | Credit note, coded 1200 Inventory | 20 Oct 2025 | 20 | **8,200** | Candidate — needs the original invoice date |
| 5 | Material period-end balance, no activity since | Harlow Fabrication Ltd | **248,157** (48,200 at 95 days + 199,957 current) | None in October | — | — | 248,157 | Collectibility indicator (weaker) |

### What the sweep says about each estimate

1. **Customer claim, defective brackets — 52,000.** The claim existed at 30 Sep (GC's view 28 Sep: probable, 40,000–70,000) and settled 14 days later at 52,000. On the evidence this is the classic recognised event: the settlement fixes the amount of a liability that existed at the balance sheet date. **Proposed (not posted):** Dr Legal / claims expense 52,000, Cr Accrued liabilities 52,000 at 30 Sep 2025, less any amount already in accrued liabilities (28,800 in total; make-up not supplied). Without the settlement, ASC 450 would accrue the low end of the range, 40,000, absent a best estimate. Two points to resolve: (a) any insurance recovery under the product-liability policy (10,000 deductible) is a separate receivable, recognised only if probable, never netted; (b) the October payment is coded to **6400 Professional Fees** — a claim settlement, not a fee.
2. **Allowance for doubtful accounts — 9,000.** Foxhall 4,003 written off 9 days after period end (in administration, 130 days overdue) — the condition very likely existed at 30 Sep; it is absorbed by the 9,000 allowance, so no adjustment unless the allowance was reserved for other balances. Items over 90 days total **52,203** (Harlow 48,200 + Foxhall 4,003) against a 9,000 allowance; Harlow has 248,157 outstanding and no receipt in October. Pennine's 112,071 receipt is favourable evidence and, if any of the allowance sat against Pennine, it was too high.
3. **Credit note 8,200, PN-55 panels.** If the panels were invoiced before 30 Sep, this is evidence the revenue was not earned or the goods were faulty at the date (Type 1); if invoiced after, it is a post-period event. The posting is also odd: a credit note normally credits AR and debits returns/revenue; this one is coded only to inventory 1200. Please give the invoice reference.
4. **Former employee claim** (reasonably possible, up to 25,000): no post-period activity seen; disclosure-only candidate under ASC 450, not a subsequent event on this evidence. **Supplier counterclaim** (remote): nothing.

## Subsequent events log

| Event | Event date | Posting date | Source | Category | Accounting impact | Disclosure |
|---|---|---|---|---|---|---|
| Bracket claim settled | 14 Oct 2025 | 14 Oct 2025 | Ledger sweep + legal schedule | *for preparer* | 52,000 to accrue at 30 Sep (less any existing accrual) | *for preparer* |
| Foxhall write-off | 9 Oct 2025 | 9 Oct 2025 | Ledger sweep | *for preparer* | 4,003, within allowance | *for preparer* |
| Pennine receipt | 6 Oct 2025 | 6 Oct 2025 | Ledger sweep | *for preparer* | Favourable; allowance review | — |
| PN-55 credit note | 20 Oct 2025 | 20 Oct 2025 | Ledger sweep | *for preparer* | 8,200, pending invoice date | *for preparer* |
| Harlow — no activity | — | — | Ledger sweep | *for preparer* | Collectibility of 248,157 | — |

Category is left blank on purpose: it turns on when each condition arose, which is a fact for management. Proximity (6–20 days) is evidence, not proof.

## Management enquiry — not answered

Litigation · customers · financing (incl. the term loan, 220,000) · ownership · assets (casualty) · acquisitions or disposals · regulatory · people · commitments · dividends declared after 30 Sep. Each is an open non-recognised-event enquiry; none can be inferred from the ledger. Legal disclosure wording is not drafted here.

## Not done, and why

- Sweep of 1 Nov 2025 – 20 Mar 2026 — no ledger; re-run immediately before issue.
- Board minutes and legal updates — not supplied.
- Classification, materiality and disclosure — management's judgment.
- Excel workpaper — would ask before creating `Subsequent_Events_2025-09-30_Northbrook_Trading_Ltd.xlsx`. Nothing posted.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, USD (user-asserted); BS date 30 Sep 2025; window end 20 Mar 2026, definition **not confirmed**; framework ASC 855. Data source: upload. 4 files accepted with limits, 1 rejected (staff rota). Sweep run once, over October 2025 only. |
| Capability map | Not applicable: no connection. Every task is `[manual]`. |
| Steps | 1 done (definition open); 2 — ledger sweep done for Oct only, cash review same, minutes / legal updates / management enquiry **not done**; 2b done; 3 not done (preparer); 4 quantified, not decided; 5 log drafted. |
| Unknowns carried forward | All five candidates unclassified; Nov–Mar unswept; every enquiry category open; accrued-liabilities make-up; credit-note invoice date. |
| Parameters | Window 30 Sep 2025 – 20 Mar 2026; accounts swept 1100, 1150, 1200, 2100, 6400 against the AR aging and legal schedule. |
