<!-- ar-cash-application-lockbox · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding)
- Step 1 — Normalize receipts
- Step 2 — Match hierarchy
- Step 3 — Exceptions
- Step 4 — Entries
- Step 5 — Tie to bank
- Step 6 — Evolve the skill (Mosofin-specific, final step)
- Outputs
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with
plain-language wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence
tool added.

**Never drop a task because no tool covers it.** A `[manual]` task is a task with a *named gap*,
not an absence.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding)

Pull the `[auto]` / `[gated]` reads. **Batch independent reads into one message** — open
invoices, recorded payments, deposits, credits and the customer master do not depend on each
other. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`search_invoices`* — invoices in the window, the population to match against — usually
  **[auto]**
- *`read_invoice`* — one invoice in full, including the customer's PO reference — usually
  **[auto]**
- *`get_aged_receivables`* — what is open and how old — usually **[auto]**
- *`search_payments`* / *`get_payment`* — customer receipts as recorded, and what they were
  applied to — usually **[auto]**
- *`search_deposits`* / *`get_deposit`* — how receipts were banked, including batches — usually
  **[auto]**
- *`search_sales_receipts`* — receipts taken at the point of sale, with no invoice behind them —
  usually **[auto]**
- *`search_credit_memos`* / *`search_refund_receipts`* — credits and refunds that explain a
  short-pay — usually **[auto]**
- *`search_customers`* / *`get_customer`* — the customer master, for payer identification —
  usually **[auto]**
- *`get_customer_balance`* — total owed per customer, for the tie-out — usually **[auto]**
- *`search_accounts`* — to locate the unapplied cash and bank accounts — usually **[auto]**
- *`get_general_ledger`* — movement on the unapplied cash and bank accounts — usually **[auto]**
- *`get_company_info`* — base currency and time zone — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — it can demonstrate the matching logic
but **must never drive a real cash application or a write-off**. Applying fixture cash to a real
invoice would show a customer as paid when they have not paid.

## Step 1 — Normalize receipts

Get every receipt into one consistent shape before matching anything.

**Capture payer, amount, date, references, and bank trace identifiers.**

- **Payer** — **[gated]**: the name on a recorded payment is the customer it was booked
  against (*`get_payment`*, **[auto]**); the name the *bank* shows is often different — a
  parent company, a factoring agent, a payment platform — and that is **[manual]** without the
  bank file. This mismatch is the single most common cause of unapplied cash, which is why the
  payer-alias map is worth storing.
- **Amount** and **date** — **[auto]** for recorded payments (*`search_payments`*,
  *`search_deposits`*). Use the entity's time zone when a receipt falls near midnight.
- **References** — **[auto]** where the payment carries a memo or document number; the invoice
  numbers a customer actually quoted usually live in the **remittance advice** (the note saying
  which invoices a payment covers), which is **[manual]**.
- **Bank trace identifiers** — the bank's own reference for a transfer — **[manual]** unless a
  banking datasource is connected. Record the field as blank rather than substituting an
  internal id; a trace number is what lets someone find the payment at the bank.

## Step 2 — Match hierarchy

Work down the list. Stop at the first level that gives an unambiguous answer, and record which
level produced the match — a level-1 match and a level-5 match carry very different confidence.

1. **Invoice number** — **[auto]** where a reference exists (*`search_invoices`*,
   *`read_invoice`*). The strongest match; take it whenever it is available.
2. **Exact amount to a single invoice** — **[auto]**. Strong, but check for two open invoices
   at the same amount before treating it as unambiguous.
3. **Exact amount to multiple invoices** — **[auto]**: a receipt equal to the sum of several
   open invoices. Genuinely useful, and also the level where false positives begin, because
   several combinations can add to the same total. Report the combination you chose and say
   whether another was possible.
4. **PO match** — **[auto]** where the customer's purchase-order number is recorded on the
   invoice (*`read_invoice`*). Common with larger customers who pay by PO rather than invoice
   number.
5. **Fuzzy match** — **[gated]**: near-name, near-amount, or date-proximity matching. Never
   auto-accept a fuzzy match. Present it with its reason and its confidence, and let a human
   decide.
6. **Manual research queue** — **[manual]**. Everything unresolved goes here, with what is
   known and what is missing. **This queue is an output, not a failure** — an honest research
   queue is more useful than a forced match.

Because Mosofin is read-only, every level produces a **proposal**. Nothing here applies cash.

## Step 3 — Exceptions

- **Short-pay** — the customer paid less than the invoice. **[auto]** to detect
  (*`read_invoice`* balance versus *`get_payment`* amount); **[gated/manual]** to resolve.
  **Create a deduction case or write off per policy** — using the threshold confirmed at
  Gate 3. First check whether a **credit memo** already explains the difference
  (*`search_credit_memos`*, **[auto]**), because a short-pay that matches an outstanding credit
  is not a deduction at all. Assign a **reason code** (see Step 6 — the code set is the user's
  and should be stored).
- **Overpay** — the customer paid more than the invoice. **[auto]** to detect. **Create a
  customer credit or apply to future invoices** — both are write actions, so both are
  proposals. Check for a duplicate payment before creating a credit; a customer paying twice
  looks identical to a customer overpaying once.
- **Unidentified** — you cannot tell who paid or for what. **Park in Unapplied Cash with aging
  and escalation.** **[auto]** to find what already sits in unapplied cash and how long it has
  been there (*`search_accounts`*, *`get_general_ledger`*). Unapplied cash that ages is a real
  problem: it overstates the receivable, understates the customer's payment record, and often
  hides a genuine dispute.

## Step 4 — Entries

`DR` is a debit, `CR` a credit; every entry balances. **Mosofin does not post** — these are
proposals.

**Receipt (direct)** — applying cash straight to the invoice:

```
DR Cash                              XXX
    CR Accounts Receivable               XXX
```

**Unapplied cash approach** — banking the money now, working out whose it is later:

```
DR Cash                              XXX
    CR Unapplied Cash                    XXX
```

Followed, once identified, by a reclassification from Unapplied Cash to Accounts Receivable.

Use the **real account names from the connected chart of accounts** (*`search_accounts`*,
**[auto]**) rather than the generic labels above, and say which you chose. Where the receipt is
already recorded and applied, this step becomes a **review** of how it was applied rather than a
proposal to apply it — say which of the two you did.

## Step 5 — Tie to bank

**Tie daily receipts to deposits; explain differences (timing, fees, batch splits).**

- **[auto]** for the books' side: recorded receipts (*`search_payments`*,
  *`search_sales_receipts`*) against recorded deposits (*`search_deposits`*,
  *`get_deposit`*), by day.
- **[manual]** for the bank's side, unless a banking datasource is connected. **This is the
  limit named at the top of this file.** A tie of recorded receipts to recorded deposits is a
  *book-to-book* check — genuinely useful for catching batching errors, and **not** a bank
  reconciliation. Do not call it one. For the real thing, see `bank-reconciliation`.

The three standard difference types, each of which is a legitimate explanation rather than an
error:

- **Timing** — money received on one day, banked on the next.
- **Fees** — the bank or card processor deducts its charge, so the deposit is smaller than the
  receipts. The receipt is gross; the deposit is net.
- **Batch splits** — one deposit covers many receipts, or one day's receipts are banked in
  several deposits. Match the batch, not the individual amounts.

State plainly which side of the tie-out you could evidence, and report an untied difference
rather than forcing agreement.

## Step 6 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them,
ask — explicitly, at that point, not earlier — whether to save this as their own customized
version. A general "yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The payer-alias map** — the bank or remittance name for each customer versus the name in
  the books. This is the highest-value thing to carry forward: it is pure accumulated
  knowledge, it never appears in the ledger, and it directly reduces unapplied cash on every
  future run
- **The deduction policy**: the write-off threshold, who approves above it, and the **reason
  code set** with what each code means
- Which customers habitually pay by PO rather than invoice number, and which send remittance
  advices and how
- The unapplied cash account and the bank accounts, by their real names
- The escalation rule for aged unapplied cash
- The replay recipe: the exact sequence of reads that produced this run

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference
files; set `datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write
preference files alongside the installed skill.

**Do not persist bank account numbers, bank trace identifiers, customer contact details, or
receipt-level data.** Those are transaction records and payment credentials, not decisions;
they belong in the accounting and banking systems that control them.

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks /
Northbrook Trading — write-off threshold $50, reason codes: SHIP / PRICE / QTY / DISC" — not
"threshold $50". Entities routinely run different thresholds and different code sets, and an
unlabelled threshold applied to the wrong company file writes off real money. Record the chosen
**scenario** (single vs multi, and which set) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to
the workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is
the workspace's.**

On later runs, match stored entity names against Gate 1's live list. An entity in preferences
that is no longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Outputs

- **Applied cash register.** Every receipt with the invoice(s) it was matched to, **the match
  level that produced it (1–6)**, and whether the match is *recorded* or *proposed*.
- **Unapplied cash aging.** What is sitting unapplied, by age, with the escalation status. Aged
  unapplied cash is the headline number here — it is money you have that your books say you are
  still owed.
- **Deduction case list with reason codes.** Every short-pay with its amount, reason code,
  whether an existing credit explains it, and whether it falls under or over the write-off
  threshold.
- **Daily tie-out to bank deposits.** Receipts to deposits by day, with timing, fee and
  batch-split differences explained — **stating clearly whether the bank side was evidenced or
  is a book-to-book tie only**.

**Coverage sheet — NEW, Mosofin-specific.**

One row per task in Steps 1–5:

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used | Policy (enabled / permission / disabled) | `mock` | Gap — what could not be verified and what the user must supply |

Rows for bank / lockbox intake, remittance advice, bank trace identifiers and the deduction
policy will typically read `manual` with their gaps named. That is the correct, expected result
— not a defect.

In a multi-entity run the sheet is **per entity**.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming — Mosofin addition** (the original left it unstated, and multi-entity output
needs it): `AR_CashApplication_[YYYY-MM-DD].xlsx`, and in a multi-entity run
`AR_CashApplication_[YYYY-MM-DD]_[EntityDisplayName].xlsx` plus one combined file. Every file
states which datasource and `display_name` it covers.

**Grounding:** every figure traces to a tool result in this conversation or to labelled
user-supplied evidence. End with a single **Data sources** line grouping calls by datasource.
Where the data does not cover something, **name the tool that would have covered it** instead of
estimating.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One register, one unapplied
cash aging, one tie-out.

**Multi-entity.** Steps 0–5 run **once per entity**, each call targeting exactly one
`data_source_id`, every receipt and match carrying that entity's `display_name`. Then one
cross-entity step:

- **A comparison of unapplied cash and deduction rates by entity** — a location with far more
  unapplied cash than its siblings usually has a remittance or payer-naming problem, not a
  customer problem.
- **Never match across entities.** A receipt banked by one entity applied to another's invoice
  is an intercompany transaction, not a cash application. Flag it and route it to
  `intercompany-reconciliation`.
- **A shared customer paying one lump sum covering several entities' invoices** is the genuine
  cross-entity case, and it is common where a group bills a customer from more than one
  company. Split it explicitly by entity, show the split, and never let one entity's books
  absorb the whole receipt.
- **A shared bank account across entities** makes the daily tie-out ambiguous by design. Say so
  rather than producing a per-entity tie-out the bank data cannot support.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict per
company file.
