<!-- ap-invoice-processing-and-3way-match · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding)
- Step 1 — Intake and hygiene
- Step 2 — Vendor and compliance checks
- Step 3 — Field validation
- Step 4 — Match logic
- Step 5 — Exception handling
- Step 6 — Posting
- Step 7 — Audit trail
- Step 8 — Evolve the skill (Mosofin-specific, final step)
- Outputs
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with
plain-language wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical
evidence tool added.

**Never drop a task because no tool covers it.** In this skill several controls are
inherently `[manual]` — approvals, bank-detail changes, physical receipts — and recording
them as gaps is the honest result. A control silently omitted reads as a control that passed.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding)

Pull the `[auto]` / `[gated]` reads. **Batch independent reads into one message** — bills,
purchase orders, vendors, terms and tax codes do not depend on each other. Never serialize
them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`search_bills`* — the bills in scope — usually **[auto]**
- *`get-bill`* — one bill's lines, amounts, tax, terms and PO reference — usually **[auto]**
- *`search_purchase_orders`* / *`get_purchase_order`* — the orders to match against — usually
  **[auto]**
- *`search_vendors`* / *`get-vendor`* — vendor status, terms, remit-to — usually **[auto]**
- *`search_terms`* / *`get_term`* — payment terms and due-date rules — usually **[auto]**
- *`search_accounts`*, *`search_classes`*, *`search_departments`* — the coding structure —
  usually **[auto]**
- *`search_tax_codes`* / *`search_tax_rates`* — tax codes in use — usually **[auto]**
- *`search_items`* — the products / services being ordered and billed — usually **[auto]**
- *`search_bill_payments`* — what has already been paid, for cycle-time KPIs — usually
  **[auto]**
- *`search_attachables`* — attachment metadata, evidence that a document exists — usually
  **[auto]**
- *`get_company_info`* — base currency and calendar — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with
  `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — it can demonstrate the match logic
but **cannot clear a real invoice for payment**. A "matched" verdict on fixture data would
authorise a real payment against an imaginary order.

## Step 1 — Intake and hygiene

Catch the bad ones before they get anywhere near a payment.

- **Validate required invoice fields** — **[auto]** for bills already posted
  (*`get-bill`*: vendor, number, date, due date, amounts, tax, currency, line coding);
  **[manual]** for invoices not yet entered, since Mosofin cannot read an inbound PDF.
  List explicitly which fields were checked and which were absent.
- **Detect duplicates (vendor + invoice # + amount)** — **[auto]** over posted bills
  (*`search_bills`*). Also test near-duplicates: same vendor and amount with a slightly
  different invoice number, or the same invoice entered under two vendor records. See
  `duplicate-invoice-detection` for the fuller treatment.
- **Flag fraud red flags (bank change, urgency, mismatched remit)** — **[manual]**, and
  importantly so. A **bank change** request, artificial **urgency**, and a **remit-to** that
  does not match the vendor on file are the classic invoice-fraud signature, and none of the
  three is visible in a posted bill. Mosofin can compare the remit-to name on the bill
  against the vendor master (*`get-vendor`*, **[auto]**) — that one check is real — but it
  cannot see the email, the pressure, or the changed bank details. Say so rather than
  implying a fraud screen was performed.

## Step 2 — Vendor and compliance checks

Make sure the payee is one you have actually agreed to deal with.

- **Vendor active / approved** — **[auto]** (*`search_vendors`*, *`get-vendor`*: active
  status). *Approved*, in the sense of having passed onboarding, is usually **[manual]**
  unless the workspace encodes it — an active vendor record is not the same as an approved
  one.
- **Tax forms on file where applicable** — **[manual]**. A signed W-9 / W-8 / equivalent is a
  document, not ledger data. An attachment listing (*`search_attachables`*, **[auto]**) can
  show that *a* file exists with a given name; that is evidence of filing, not of validity or
  currency. See `vendor-onboarding-and-w9-tin`.
- **Bank detail change control** — **[manual]**, always. Mosofin is read-only and does not
  expose, verify, or change bank details. This is the highest-value control in the whole
  step and the one Mosofin cannot perform: state it as a gap with a named owner, never as a
  check that passed.

## Step 3 — Field validation

Check the invoice is internally correct before checking it against anything else.

- **Total math checks** — **[auto]** (*`get-bill`*): do the lines sum to the subtotal, does
  subtotal + tax equal the total, do quantity × unit price equal each line amount?
- **Tax checks** — **[auto]** (*`get-bill`*, *`search_tax_codes`*, *`search_tax_rates`*): is
  the tax code one the entity uses, does the computed tax match the rate, is tax charged on
  lines that should be exempt? Whether the tax is *recoverable* is a jurisdiction rule and is
  **[manual]**.
- **Terms and due date** — **[auto]** (*`get-bill`*, *`get_term`*, *`search_terms`*): do the
  terms on the bill match the vendor's agreed terms, and is the due date consistent with
  them? A due date that does not follow the terms is a common data-entry error and it changes
  every downstream payment decision.

## Step 4 — Match logic

The core of the skill: compare the bill to what was ordered, and where possible to what was
received.

**2-way match: PO vs invoice (price and quantity tolerances)** — **[auto]** where bills carry
a PO reference (*`get-bill`*, *`get_purchase_order`*). Compare, per line: item, quantity,
unit price, and extended amount. Apply the tolerances confirmed at Gate 3 — a **tolerance**
being the small variance you accept without investigating, expressed as a percentage and
usually with an absolute floor so that a 5% tolerance on a $4 line does not consume review
time.

Where the bill carries **no PO link**, match by vendor, date, amount, item and description,
and **record the match as inferred rather than linked**. An inferred match is a judgment, and
a wrong one either clears a bill that should not have been cleared or raises an exception
that does not exist.

**3-way match: PO vs receipt vs invoice (invoice qty ≤ received qty, with tolerances)** —
**[gated] or [manual]**, depending on whether receipt data exists anywhere in the workspace.
This is the structural gap named at the top: most accounting connectors have no goods-receipt
object. Where an inventory or warehouse platform is connected, pull receipts from it and the
match is real. Where none is, **say plainly that only a 2-way match was performed**, and do
not label the output a 3-way match. Treating an open PO as evidence of receipt is exactly the
error that lets a supplier bill for goods that never arrived.

## Step 5 — Exception handling

What to do when the three do not agree. Each exception is **[auto]** to *detect* and
**[gated] or [manual]** to *resolve*, because resolution requires a human decision Mosofin
cannot make or record.

- **Price variance**: buyer approval, or a corrected invoice. Detected automatically; the
  approval is **[manual]**.
- **Quantity variance**: confirm the receipt, or split the invoice. Confirmation is
  **[manual]** wherever receipts are.
- **Missing PO**: an after-the-fact PO, or manager approval. Detection is **[auto]** — a bill
  above the PO-required threshold with no PO reference; the remedy is **[manual]**.
- **Tax mismatch**: a corrected invoice, or a tax code fix. Detection is **[auto]**; the fix
  is a change to the books, which Mosofin proposes but never makes.

Build these into an **exception matrix**: exception type → tolerance → who resolves it → what
evidence closes it → target turnaround.

## Step 6 — Posting

`DR` is a debit, `CR` a credit; every entry balances. **Mosofin does not post** — this is a
proposal.

Typical posting:

```
DR Expense / Inventory / Asset        XXX
DR Recoverable VAT (if applicable)    XXX
    CR Accounts Payable                   XXX
```

*Recoverable VAT* is the sales tax you can reclaim from the authorities on what you buy — it
is not a cost, so it is split out rather than sitting in the expense.

Use the **real account and dimension names from the connected books** (*`search_accounts`*,
*`search_classes`*, *`search_departments`*, **[auto]**) rather than the generic labels above,
and say which you chose. Where the bill is already posted, this step becomes a **review** of
how it was coded rather than a proposal to code it — say which of the two you did.

## Step 7 — Audit trail

**Maintain evidence: invoice, PO, receipt, approvals, exception notes.**

- **Invoice and PO** — **[auto]** to reference by number and date; the underlying documents
  are **[manual]** unless attached.
- **Receipt** — **[manual]** in most workspaces, per Step 4.
- **Approvals** — **[manual]**, always. An attachment listing shows a file exists, not that
  anyone authorised anything.
- **Exception notes** — produced by this run, and only as durable as where the user stores
  them. **Mosofin retains nothing on the user's behalf**, so say where the trail will
  actually live; a chat transcript is not an audit trail.

## Step 8 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved
them, ask — explicitly, at that point, not earlier — whether to save this as their own
customized version. A general "yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The match tolerances** — price and quantity, percentage and absolute floor. Pure policy,
  never in the books, and re-asking them every cycle is what makes the process feel manual
- **The approval matrix** — limits by role
- The **PO-required threshold** — above what value a purchase must have an order
- The coding standard: which account, class and department each spend category maps to, by
  their real names
- Which vendors are exempt from matching (utilities, rent) and why
- Where receipts, approvals and tax forms actually live, so the next run asks the right person
- The exception matrix as tailored, and the KPI targets agreed
- The replay recipe: the exact sequence of reads that produced this run

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference
files; set `datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write
preference files alongside the installed skill.

**Do not persist vendor bank details, tax identification numbers, or invoice images.** Bank
details are the top fraud target and tax IDs are personal data; both belong in the systems
that control them, not in a skill bundle.

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks /
Northbrook Trading — price tolerance 2% or $25, PO required above $1,000" — not "tolerance
2%". Entities routinely run different thresholds, and an unlabelled tolerance applied to the
wrong company file either floods the queue with exceptions or silently clears real ones.
Record the chosen **scenario** (single vs multi, and which set) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong
to the workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's;
state is the workspace's.**

On later runs, match stored entity names against Gate 1's live list. An entity in preferences
that is no longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Outputs

- **SOP with roles, SLAs, evidence.** A **standard operating procedure** — the written
  routine — naming who does each step, the **SLA** (the agreed turnaround time) for each, and
  what evidence closes it. Include, per step, whether it is `[auto]`, `[gated]` or `[manual]`
  in *this* workspace, so the SOP describes the process as it can actually run.
- **Match rules and tolerance table.** The tolerances from Gate 3, with their absolute floors
  and the PO-required threshold.
- **Exception matrix.** Exception type → tolerance → owner → closing evidence → turnaround.
- **Recommended entries and controls.** Proposed postings and coding, plus the control gaps
  found — with the bank-detail control and the approvals control named explicitly if they are
  `[manual]`.
- **KPIs (cycle time, first-pass match rate).** **Cycle time** — how long from bill date to
  payment — is **[auto]** (*`search_bills`* + *`search_bill_payments`*). **First-pass match
  rate** — the share of invoices that match with no exception — is **[auto]** for the bills
  this run examined, but only over the population you actually pulled: state the population
  and the date range, since a rate quoted without its denominator is not a measure.

**Coverage sheet — NEW, Mosofin-specific.**

One row per task in Steps 1–7:

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used | Policy (enabled / permission / disabled) | `mock` | Gap — what could not be verified and what the user must supply |

Rows for approvals, bank-detail control, tax forms on file, and (usually) goods receipts will
read `manual` with their gaps named. That is the correct, expected result — not a defect.

In a multi-entity run the sheet is **per entity**: a tool enabled for one company file may be
disabled for its sibling.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.
Offer the procedure as a Word document only where the host can make one; otherwise give it as text in the chat.

**File naming — Mosofin addition** (the original left it unstated, and multi-entity output
needs it): `AP_InvoiceProcessing_[YYYY-MM-DD].xlsx`, and in a multi-entity run
`AP_InvoiceProcessing_[YYYY-MM-DD]_[EntityDisplayName].xlsx` plus one combined file. Every
file states which datasource and `display_name` it covers.

**Grounding:** every figure traces to a tool result in this conversation or to labelled
user-supplied evidence. End with a single **Data sources** line grouping calls by datasource.
Where the data does not cover something, **name the tool that would have covered it** instead
of estimating.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One exception matrix, one
KPI set, one SOP.

**Multi-entity.** Steps 0–7 run **once per entity**, each call targeting exactly one
`data_source_id`, every matched bill and exception carrying that entity's `display_name`.
Then one cross-entity step:

- **A comparison of exception rates and first-pass match rates by entity.** This is where the
  real finding usually is: one location generating three times the exceptions of its siblings
  is a process problem, not an accounting one.
- **Never match across entities.** One entity's bill against another's purchase order is not
  a match — it is two errors cancelling. Where a shared purchasing function orders on behalf
  of several entities, say so explicitly and treat the allocation as an intercompany step.
- **Shared vendors** may warrant one tolerance policy across entities, or deliberately
  different ones. Show the tolerance actually applied per entity.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict
per company file.
