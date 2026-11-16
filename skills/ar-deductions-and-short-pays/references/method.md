<!-- ar-deductions-and-short-pays · method.md · read for: Stages 3–6 — the analysis itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding)
- Step 1 — Build the deduction log
- Step 2 — Age and size the log
- Step 3 — Find duplicates and repeats
- Step 4 — Decide each deduction against its evidence
- Step 5 — Propose the resolution
- Step 6 — Accounting entries
- Step 7 — Evolve the skill (Mosofin-specific, final step)
- Outputs
- Both entity scenarios

Each step carries an `[auto]` / `[gated]` / `[manual]` verdict and the typical evidence tool.
**Never drop a task because no tool covers it.** A `[manual]` task is a task with a *named gap*.
Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding)

Pull the reads in **one batch**: they do not depend on each other. The server is **stateless**:
pass `data_source_id` on **every** call, including retries.

- *`search_invoices`* — the invoices behind each deduction, with original amount and balance —
  usually **[auto]**
- *`search_payments`* — the short payments: date, amount, the invoices applied, the memo —
  usually **[auto]**
- *`search_credit_memos`* — credits already issued, so nothing is credited twice — **[auto]**
- *`get_aged_receivables`* — the receivables total the log must sit inside — **[auto]**
- *`search_customers`* — terms and contacts — **[auto]**
- **Backup** — proofs of delivery, carrier reports, agreements, contracts: **[manual]** on every
  path. Ask for them by deduction.

## Step 1 — Build the deduction log

One row per deduction: customer, the customer's reference, the invoice, invoice amount, amount
paid, **amount deducted**, payment date, reason code as given, and status.

- From a deduction log or deduction account, take the rows as they are and tie the total to the
  account.
- From open balances only, a partly paid invoice is a **candidate**: the remittance or payment
  memo says whether the customer deducted or simply paid late. Do not call it a deduction without
  that.
- Map each customer reason to one of: **damage**, **shortage**, **pricing**, **promotion**,
  **freight**, **returns**, **unexplained**. Keep the customer's own words next to the mapped
  reason.

## Step 2 — Age and size the log

Age each deduction from its **payment date** (when the customer took it), not the invoice date.
Show the total and count by reason and by age band (0–30, 31–60, 61–90, over 90). Anything past
the dispute window (Stage 1, F; default 90 days) is **at risk**: say so per item.

Tie the log's total to the deduction account or the deducted part of receivables. A difference
is a finding: deductions that were written off without a record, or a log that is out of date.

## Step 3 — Find duplicates and repeats

Before deciding anything:

- **The same invoice deducted twice**, by the same customer, for the same reason. Usually one
  claim taken on two payments. The second is invalid whatever the first's outcome.
- **A deduction already credited**: a credit memo issued for the same invoice and amount. The
  deduction is a second recovery of the same thing.
- **Repeat claimants**: one customer, the same reason, many times. Not invalid by itself; worth
  reporting as a pattern for the sales or operations owner.

## Step 4 — Decide each deduction against its evidence

| Reason | Valid when the evidence shows | Invalid when the evidence shows |
|---|---|---|
| Damage | A carrier exception or damage report at delivery, or agreed returned goods | A clean signed delivery note and no report |
| Shortage | Delivery note signed short, or received quantity below invoiced | Delivery note signed for the full quantity |
| Pricing | The agreed price is below the invoiced price | The invoice used the agreed price |
| Promotion | A promotion agreement covering this order, at this rate, not yet credited | No agreement, outside its dates, or already credited |
| Freight | Terms put freight on the seller (delivered / prepaid) | Terms put freight on the customer (e.g. FOB origin, freight billed per contract) |
| Unexplained | — | — : always **needs backup**; ask the customer for the reason |

Every decision cites its evidence document. **No evidence either way is "needs backup"**, with
the document named that would decide it.

Apply the write-off policy **after** the decision: a valid item is credited, not written off; an
invalid or unsupported item **within the limit** may be proposed for write-off (cheaper than the
dispute), naming who approves under the policy.

## Step 5 — Propose the resolution

| Decision | Proposal |
|---|---|
| Valid | Credit memo for the deducted amount, against the invoice, for approval |
| Invalid | Dispute draft to the customer: the invoice, the amount, why it is not valid, the evidence attached, and the request to pay |
| Duplicate | Dispute draft, citing the first deduction |
| Needs backup | Request to the customer or the internal owner for the named document |
| Within write-off limit | Write-off proposal, naming the approver under the policy |

The drafts are drafts: the skill sends nothing.

## Step 6 — Accounting entries

`DR` is a debit, `CR` a credit; every entry balances. **Mosofin does not post** — these are
proposals.

```
Valid deduction (credit memo)
DR Sales returns and allowances (or the promotion / freight account)   XXX
    CR Accounts receivable                                                  XXX

Write-off within policy
DR Bad debt expense (or deductions written off)                         XXX
    CR Accounts receivable                                                  XXX
```

Use the **real account names** from the chart of accounts (*`search_accounts`*, **[auto]**).
Promotions are usually a reduction of revenue, not an expense: say which account you chose.

## Step 7 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them,
ask — explicitly, at that point, not earlier — whether to save this as their own customised
version. A general "yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- the map from customer reason codes to the reasons above
- the write-off limit and approver, and the dispute window
- customer-specific rules (agreed promotion rates, freight terms, portal locations)
- the accounts used for each kind of credit
- the replay recipe: the reads that produced this log

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference
files; set `datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write
preference files alongside the installed skill.

**Key every preference by datasource + entity `display_name`.** **Never persist state**:
connections, company files, tool policies and `mock` status are re-discovered by Gates 1–2 every
run. Never persist customer bank details.

---

## Outputs

- **Deduction log.** Every deduction with its age, reason (mapped and as given), evidence,
  decision, and proposal; totals by reason, age band and decision.
- **Duplicates and repeats.**
- **Proposed credit memos and write-offs**, with approver.
- **Dispute and backup-request drafts**, one per customer.
- **Proposed entries**, marked as proposals.

**Coverage sheet — Mosofin-specific.** One row per task in Steps 1–5:

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used | Policy | `mock` | Gap — what could not be verified and what the user must supply |

The row for **"decide against evidence"** reads `manual` on every path, with the backup supplied
listed. Ask whether the user wants the log as an Excel (`.xlsx`) file, and create it only on a
yes: `AR_Deductions_[YYYY-MM-DD].xlsx`, and per entity in a multi-entity run. If they decline,
give the same sheets as tables in the chat.

**Grounding:** every figure traces to a tool result in this conversation or to labelled
user-supplied evidence. End with a single **Data sources** line grouping calls by datasource.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`.

**Multi-entity.** Steps 0–6 run **once per entity**, each call targeting exactly one
`data_source_id`, every deduction carrying that entity's `display_name`. A customer of two
entities has two logs: a deduction on one entity's invoice is never offset against the other's
balance. Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's
verdict per company file.
