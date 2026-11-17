# Customer invoice (prepare mode) — Northbrook Trading Ltd — Harlow contract, September 2025

Mosofin is not connected, so this run is manual: every step is `[manual]` and every figure comes from your uploads. Connecting Mosofin would read the customer record, item list and invoice sequence directly ([docs.mosofin.com](https://docs.mosofin.com)).

**Mosofin cannot create an invoice.** What follows is a **draft for review**: it is not in your accounting system, has not been numbered there and has not been sent.

## Read-back

Preparing **one invoice**: the **September 2025 monthly instalment** under the **Harlow Fabrication Ltd** supply and services agreement. Seller **Northbrook Trading Ltd**, currency **USD**, period **September 2025** (all user-asserted; no file states a currency). **No sales tax on this contract** (your answer). Mode: **prepare**. Go-ahead assumed.

**Assumptions and open questions (not defaulted, per the skill):**
- **Invoice date** — not given. The skill never defaults it. Shown below as *to be confirmed*; the due date follows from it.
- **Jurisdiction** — not given and never inferred. The mandatory-field list below is the common set; please confirm your jurisdiction's own list and any statutory wording.
- **Invoice numbering scheme and next number** — no invoice listing was uploaded, so the next number cannot be read and is **not invented**: shown as `[next number]`.
- **Tax point** (date of supply) — not given; with no tax charged it does not move tax between periods, but record it if your jurisdiction requires it.

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Needed for | Verdict |
|---|---|---|---|---|---|
| `contract_harlow_fabrication.md` | **Summary of key terms** of the Harlow agreement (signed 1 Jul 2025, 36 months): deliverables, prices, billing schedule, standalone selling prices. Not the signed agreement | Seller Northbrook Trading Ltd — agrees to intake; no currency stated | Yes: billing schedule 60,000 on signing + 2,500 × 36 = 150,000; deliverables foot to 150,000 | Steps 1–4 (what to bill, line, JE) | **Accepted with a limit**: a summary, not the agreement — figures are user-supplied, not evidenced; currency user-asserted |
| `customer_list.csv` | Customer master, 12 customers: terms, credit limit, AP email | No entity or currency | Harlow found: **30 days**, credit limit 200,000, ap@harlow.example. **No address, no tax ID** | Steps 1, 5 (bill-to, terms) | **Accepted with a limit**: company user-asserted; bill-to address and tax ID missing |
| `chart_of_accounts.csv` | Chart of accounts, 36 accounts | No entity | Yes. **No deferred revenue / contract liability account** | Step 4 (JE accounts) | **Accepted with a limit**: company user-asserted; deferred-revenue account must be named by you |
| `contract_harlow_fabrication_final.csv` | **An employee shift rota** (E08–E10, weeks 1–4: days / nights / off). Not a contract, despite its name | None | n/a | No step uses it | **Rejected.** If a final or amended Harlow contract exists, upload that instead |

**Still missing (one message, so you can gather them together):**
- **Required:** invoice date; your jurisdiction; numbering scheme and the last invoice number issued (or an invoice listing — also needed for the gap and duplicate check); **Harlow's billing address** and, if your jurisdiction needs it for B2B, its tax ID; **Northbrook's legal address and tax registration**; **payment instructions from a trusted source** (I will not reproduce bank details from any old document).
- **Improves the result:** Harlow's PO number if they require one; the July and August invoices to Harlow (to confirm the 60,000 signing invoice and the 2,500 instalments were issued, and to compare price); the AR ageing (Harlow's current balance against the 200,000 credit limit).

Would wait here for your answer; proceeding on the accepted files.

## The draft invoice — DRAFT FOR REVIEW, not issued

| Field | Value | Source |
|---|---|---|
| Seller | Northbrook Trading Ltd — address and tax registration **[to be supplied]** | contract summary / missing |
| Bill to | Harlow Fabrication Ltd — address **[to be supplied]**, tax ID **[if required]**; AP contact ap@harlow.example | customer list |
| Invoice number | **[next number]** — proposed only, not reserved | missing |
| Invoice date / tax point | **[to be confirmed]** / **[to be confirmed]** | missing |
| Due date | invoice date + **30 days** | customer list |
| Currency | **USD** | user-asserted |
| Customer PO / reference | **[if Harlow requires one]**; reference: Supply and services agreement dated 1 July 2025 | contract summary |

| Line | Description | Qty | Unit price | Tax | Line total |
|---|---|---:|---:|---:|---:|
| 1 | Harlow agreement — monthly fee, instalment 3 of 36 (September 2025) | 1 | 2,500.00 | 0.00 (no sales tax, per you) | **2,500.00** |

**Subtotal 2,500.00 · Tax 0.00 · Total inclusive 2,500.00 · Amount due USD 2,500.00.** Arithmetic checked: 1 × 2,500.00 = 2,500.00; 2,500.00 + 0.00 = 2,500.00.

Line checks: description specific; qty and price > 0; no tax code applies; currency agrees to header; no SKU list supplied. Price **2,500 agrees to the contract billing schedule**; no prior Harlow invoice was supplied, so the comparison with what Harlow was last charged **was not run**.

Payment instructions: **[to be confirmed from a trusted source]**. Footer: statutory wording **[per your jurisdiction]**; if no tax is charged because the supply is exempt, out of scope or zero-rated, the invoice may need to say which.

## Proposed journal entry (proposal — Mosofin does not post)

This contract **bills ahead of revenue**, so the instalment is a **deferred-revenue** booking, not a straight sale:

```
DR  1100 Accounts Receivable                         2,500.00
    CR  [Deferred Revenue / Contract Liability]          2,500.00
Memo: Invoice [#] — Harlow Fabrication Ltd — Sep 2025 instalment
```

**Your chart has no deferred revenue or contract liability account.** I have not invented one: please name the account (or add one in your own system). Crediting 4000 Sales Revenue with each billing would misstate revenue.

Why deferred — indicative, for hand-off to `revenue-recognition-asc606` (figures from the contract summary, user-supplied):
- Transaction price 150,000 allocated on standalone selling prices (total 180,000): licence **100,000**, implementation **25,000**, support **25,000**.
- Hosted licence (access for the term) and support recognised over 36 months: 2,777.78 + 694.44 = **3,472.22 a month**. Implementation complete 31 Aug 2025: 25,000 recognised by then.
- At 30 Sep 2025: billed 60,000 + 3 × 2,500 = **67,500**; revenue to date 25,000 + 3 × 3,472.22 = **35,416.67**; **contract liability 32,083.33**.
- So September revenue (3,472.22) is a separate recognition entry, not this invoice. The signing invoice (60,000) and the July/August instalments should also have gone to deferred revenue — not verifiable without the ledger.

## What was not done, and why

- **Next invoice number, gap check, duplicate check** — not run: no invoice listing.
- **Price against customer history** — not run: no prior Harlow invoices.
- **Credit position** — not run: no AR ageing (contract total 150,000 is inside the 200,000 limit).
- **Tax ID validity** — cannot be checked here in any mode.
- **Jurisdiction field list, statutory phrases, e-invoicing** — `[manual]`, awaiting your jurisdiction.
- **Revenue recognition schedule** — outside this skill; indicative figures above for `revenue-recognition-asc606`.
- **PDF / .xlsx** — not produced; would confirm the file name first (`Invoices_2025-09-30_batch1.xlsx` for a workpaper).

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, September 2025, USD — **user-asserted**. Data source: **upload** (Mosofin not used, by the user's choice). Contract summary, customer list, chart of accounts: accepted with limits above. `contract_harlow_fabrication_final.csv`: **rejected** (shift rota). |
| Capability map | Not applicable: no connection. Every task is `[manual]`. |
| Step 0 Evidence | Done with a limit: uploads only |
| Step 1 Mandatory fields | Done with a limit: common set; seller/customer address, tax IDs, invoice date, number, jurisdiction wording **open** |
| Step 2 Line validation | Done: one line; history comparison **not done** (no prior invoices) |
| Step 3 Totals | Done: 2,500.00, tax 0.00 |
| Step 4 JE | Done with a limit: deferred-revenue account **not in chart**, to be named by you |
| Step 5 Document | Done as a draft for review; payment details withheld pending a trusted source |
| Step 6 Output | Done in chat; workpaper file not created |
| Step 7 Save preferences | Not done: asked only after you approve the results |
| Not done | Sequence gap/duplicate check (needs invoice listing); credit check (needs AR ageing); confirmation that prior instalments were billed and deferred (needs ledger) |

Nothing was created, numbered, posted or sent. **Data sources:** upload — `contract_harlow_fabrication.md`, `customer_list.csv`, `chart_of_accounts.csv`.
