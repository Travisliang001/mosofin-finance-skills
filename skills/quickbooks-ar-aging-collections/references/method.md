<!-- quickbooks-ar-aging-collections · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

## Contents

- How to read the verdicts
- Resolve the request
- Automatic input plan
- Two inputs the original concedes that it does not have to
- Pull and reconcile
- 1. Confirm company context
- 2. Pull the two core reports
- 3. Normalize the invoice table
- 4. Reconcile
- A near-substitute is not a substitute
- Request only material missing inputs
- Analyze and prioritize
- Two checks to run before anyone is chased
- Recommended action bands
- Draft correspondence
- Deliverables
- Completion checks
- Seed to evolved: what happens on the first real run
- Anti-patterns


## How to read the verdicts

- **`[auto]`** — Mosofin can do this from live reads, unattended.
- **`[gated]`** — the gateway asks first. Expect `approval_required`; explain, get consent, re-invoke with `approved=true` (**reads only — never for a write**) and the `data_source_id`.
- **`[manual]`** — not available from this surface. The step remains; the user supplies it.

Every verdict below is a **default written before the gateway was consulted.** Where Gate 2 disagrees, **Gate 2 wins** for this workspace, on this run, and the coverage sheet records the difference.

**Nothing here is sent, posted or changed.** Every draft is a proposal for a human to review and send themselves.

---

## Resolve the request

Four items, preserved:

1. **Scope** — all customers, one exact customer, or a requested overdue segment. `[manual]` to state, `[auto]` to apply.
2. **As-of date** — use the user's date; otherwise use today's and **state which you used**. `[auto]`
3. **Deliverable** — aging summary, invoice detail, collection plan, metrics, drafts, or a full workpaper. `[manual]`
4. **Special policy** — use only policy the user supplied; otherwise apply conservative, professional defaults. `[manual]`, and see Gate 3 — check the profile before asking.

**Do not ask the user to export QuickBooks data unless the connector is unavailable or a required read fails.** This instruction is preserved and strengthened: the whole point of a connected workspace is that the export request is the fallback, not the opening move.

---

## Automatic input plan

The original's thirteen-row table is preserved in full, with the Mosofin path and a verdict added to each row. The "if QuickBooks cannot provide it" column is retained because it is the fallback that makes the skill robust.

| Input | Source | Retrieval rule | Verdict | If unavailable |
|---|---|---|---|---|
| **Connected workspace** | `list_workspaces` | **Gate 0. Before everything.** | `[auto]` + user confirmation | Cannot proceed |
| **Connected company** | `get_agent_datasources`, then the company-information tool | Confirm `display_name` before any analysis | `[auto]` | Ask the user to connect or select the correct company file |
| As-of date | User request or current date | Pass as `YYYY-MM-DD` to **both** aging calls | `[auto]` | Ask only if the requested date is ambiguous |
| **Complete open-invoice detail** | A/R Aging Detail | Call with `as_of_date` and `transaction_type: "invoice"` | `[auto]` (verify at Gate 2) | Ask for an A/R Aging Detail export with customer, invoice number, invoice date, due date, open balance |
| **Independent A/R totals** | A/R Aging Summary | Pull **unfiltered** for the same date; filters only for explicit follow-up views | `[auto]` | Compute totals from detail, **disclose that no independent tie-out was available**, and ask for the summary export if reconciliation is required |
| Credits, payments, other reconciling rows | A/R Aging Detail | If invoice-only detail does not reconcile, call again **without** `transaction_type` and identify non-invoice rows | `[auto]` | Ask for unapplied credits/payments or a full detail export |
| Invoice fields / line-item drill-down | Get invoices | Enrich **selected** invoices by ID or document number only | `[auto]` | Continue with aging-report fields and label the omitted ones |
| Customer identity or email for a selected draft | Customer search | Resolve **one** selected customer when needed; do not enumerate all customers this way | `[auto]` | Ask for the intended recipient; email is not required for a draft |
| Payment terms | Due dates in A/R detail; optionally sales settings or invoice enrichment | Use the **due date** for aging; retrieve terms only when a requested draft depends on them | `[auto]` for due dates | Ask for the applicable terms; **do not infer them** |
| Functional currency | Report output where present | **Preserve the currency QuickBooks returns** | `[auto]` | Ask before presenting unlabeled consolidated totals |
| Exact credit sales for DSO | Not guaranteed by the aging tools — **but see the recovery note below** | Use a user-supplied figure for exact DSO | `[manual]`, possibly `[auto]` — check | Ask for credit sales and period; offer a clearly labelled approximation only if the user accepts it |
| Dispute status, credit hold, strategic tier | **Not accounting fields.** Not on this surface. | **Never assume.** | `[manual]` | Ask only for the flags the requested prioritisation actually needs |
| Payment-behaviour history | Not a report field — **but see the recovery note below** | | `[manual]` as stated; **partly `[auto]` in fact** | Ask for a history or tier list, or omit the factor and disclose it |
| Brand voice, late-fee rules, escalation policy | Not an accounting field | Use supplied policy | `[manual]` — **and persist it**, see the lifecycle section | Ask, or use a neutral reminder with no fees, threats, suspension or legal claims |

### Two inputs the original concedes that it does not have to

This is the substantive analytical addition of the conversion, and both are worth having.

**Payment-behaviour history is largely derivable.** The original lists it as unavailable. But a *settled* invoice carries its invoice date, its due date and the date it was paid, and all three are readable. So:

- **Average days-to-pay per customer**, over whatever trailing history the connector will return — `[auto]`
- **The proportion of a customer's invoices paid after the due date** — `[auto]`
- **Whether that behaviour is deteriorating**: compare the last six months to the six before — `[auto]`

That is a genuine behavioural signal, computed from the ledger rather than asked for, and it is exactly the factor the original wanted for its priority ranking and then gave up on.

**Three honest caveats, which must travel with the figure.** It is a *lagging* measure built only from invoices that have already been paid — a customer who has stopped paying entirely will look fine, because their unpaid invoices are not in the sample. It reflects when cash was **applied** in the books, which may lag when it was received. And it says nothing about *why*; a customer who pays late because the invoices keep being wrong is a billing problem wearing a collections costume. Present it as observed behaviour, never as a character judgment about the customer.

**Credit sales for DSO may be separable.** The original says the exact denominator is not guaranteed, which is right, and then falls back to a total-income proxy. Before falling back, check: if the connector distinguishes **invoices** from **sales receipts** — credit sales from cash sales — then credit sales for the period is a live read and the DSO is exact rather than approximate. Check whether it does. If it does not, the original's proxy handling stands unchanged, including its label.

---

## Pull and reconcile

### 1. Confirm company context

`[auto]`. Call the company-information capability **after Gate 0 and Gate 1, not instead of them.** Show the connected company `display_name` in a short preface and in the final provenance table. If it is not the company the user intended, **stop** and ask them to switch — do not proceed and caveat afterwards.

### 2. Pull the two core reports

`[auto]`, for the **same as-of date**:

- **A/R Aging Detail** with `transaction_type: "invoice"` — the complete invoice-level population.
- **A/R Aging Summary**, with **no ranking or threshold filters** — an independent total by customer and native bucket.

Batch them together; they do not depend on each other.

> **Do not use Get Invoices as the core population.**
>
> This is preserved from the original with emphasis, because it is the trap most likely to produce a confidently wrong answer. That capability **defaults to a recent transaction window when a range is omitted**, and the invoices it therefore excludes are the oldest unpaid ones — which are the entire point of a collections run. An aging built on it will look complete, will reconcile against nothing, and will quietly omit the debts that matter most.

For a single-customer request, pass the exact customer name when known. If only a fuzzy name is supplied, **resolve it first and state the matched customer** — chasing the wrong Smith is a real failure mode with a real cost.

### 3. Normalize the invoice table

`[auto]`. One row per open invoice, with these columns where available:

| Company | As-of Date | Customer | Customer ID | Invoice # | Invoice ID | Invoice Date | Due Date | Days Past Due | Aging Bucket | Original Amount | Open Balance | Currency | Source |
|---|---|---|---|---|---|---|---:|---|---:|---:|---|---|---|

All of the original's normalisation rules are preserved:

- **`Days Past Due = As-of Date − Due Date`**, in calendar days.
- A negative or zero result is **Current**, unless QuickBooks' returned bucket requires a documented correction.
- **Preserve document numbers as text.** An invoice number is an identifier, not a quantity; a leading zero lost to numeric coercion is an invoice nobody can find.
- **Do not replace open balance with original invoice amount.** They differ whenever a partial payment has been made, and chasing the original amount on a part-paid invoice is the fastest way to lose a customer's trust in your bookkeeping.
- **Preserve customer and invoice IDs** where the tool returns them.
- **`Source = QuickBooks A/R Aging Detail`** on every imported row.
- **If a required field is absent, leave it blank and record the gap. Do not fabricate it.**

**One Mosofin addition to the Source column:** where a row or a field came from the user rather than the report, mark it. The original's completion checks already require QuickBooks-supplied, calculated, user-supplied and unavailable inputs to be distinguished; putting that distinction on the row itself is how it survives being copied into somebody's deck.

Calculated buckets, unless the user specifies otherwise:

- **Current**: days past due ≤ 0
- **1–30**: 1 through 30
- **31–60**: 31 through 60
- **61–90**: 61 through 90
- **91–120**: 91 through 120
- **Over 120**: 121 or more

**QuickBooks' summary may collapse everything past 90 days into `91+`. Derive the 91–120 and Over-120 split from the invoice due dates in the detail report.** `[auto]`. This split is not cosmetic: for most businesses the difference between four months overdue and eight months overdue is the difference between a collections problem and a provisioning question. See `bad-debt-and-write-offs`.

### 4. Reconcile

`[auto]`. All five of the original's checks, preserved in order:

1. **Sum invoice open balances** by customer and in total.
2. **Compare the total with A/R Aging Summary** for the identical date.
3. **Compare native bucket totals** where compatible — combine your calculated 91–120 and Over 120 before comparing to QuickBooks' `91+`.
4. **If invoice-only detail differs**, retrieve the full A/R Aging Detail **without** the transaction-type filter and identify credits, payments, journal entries and other reconciling rows.
5. **Report the variance and its explanation. Never silently force a tie.**

Tolerance: **0.01 in the report currency**, unless currency precision indicates otherwise.

### A near-substitute is not a substitute

The original already says the essential thing, and it is worth keeping its exact discipline:

> **Call the result a summary-to-detail reconciliation, not a general-ledger control-account reconciliation, unless a separate GL source was actually used.**

This is correct and it deserves spelling out, because it is the same trap that runs through the whole pack. Detail and Summary are **two reports generated by the same system from the same underlying records.** Tying them proves the reports agree with each other. It does **not** prove the receivables ledger agrees with the A/R control account in the general ledger, and it certainly does not prove that the customer agrees the debt is owed.

Three levels, and they are commonly confused:

| What you have | What it proves |
|---|---|
| Detail ties to Summary | The two reports are consistent. Rules out a filter or date mismatch. |
| Subledger ties to the GL control account | Nothing has been posted to A/R by journal that bypassed the customer ledger. **Requires a separate GL read.** `[auto]` — see below. |
| The customer confirms the balance | The debt exists as far as the debtor is concerned. **`[manual]`, and not obtainable from any accounting system.** |

**The middle one is available and the original does not ask for it.** `[auto]`: read the A/R control account balance from the trial balance at the same date and compare it to the aging total. A difference means something was posted directly to A/R without a customer document — a journal entry, a misposted receipt, an opening balance adjustment — and that difference will never appear in a detail-to-summary tie because both reports come from the customer ledger. Run it. It is one extra read and it catches a category of error the original's reconciliation is structurally blind to.

The third one is what an audit confirmation is for, and it is not on this surface. See `internal-audit-workpaper`.

---

## Request only material missing inputs

`[manual]`. After the automatic pulls, ask **one consolidated question** for gaps that materially change the requested output. **Check the profile first** (Gate 3) — most of these should already be known.

Core aging does not require dispute flags, payment history, strategic tier, DSO or brand voice. Where the user did not ask for those dimensions, **omit them and disclose the limitation** rather than asking.

A compact request, adapted from the original:

> The workspace supplied the invoice aging and balances for [company display_name]. It does not hold dispute status, credit-hold status, strategic-customer tier, or your collection-language policy — those are not accounting fields. To include them in the priority queue and the drafts, please provide the relevant customer or invoice flags and any approved escalation or late-fee wording. For an exact DSO, also provide credit sales and the measurement period.

If a core read fails, **state the failed capability and request the smallest fallback export.** Accept CSV, XLSX or a pasted table. **Clearly label any mixed workspace/user-supplied dataset** — and label it at the row level, not only in a footnote.

---

## Analyze and prioritize

**Always calculate, where the data supports it** — all six preserved, all `[auto]`:

- Total A/R outstanding
- Current and overdue totals
- Overdue as a percentage of total A/R
- Total and percentage over 90 days
- **Weighted average days past due**, using open balance as the weight and **flooring current invoices at zero**
- **Top-five customer concentration**

**DSO** — calculate only when the denominator and period are explicit:

```
DSO = ending A/R / credit sales for the period x days in period
```

If total accrual-basis income is used instead of credit sales, **title the metric `Approximate DSO (total-income proxy)` and state the limitation beside it.** Preserved exactly. A DSO computed on a denominator that includes cash sales is understated, systematically, and by a margin that varies with the sales mix — which makes it useless for the one thing DSO is for, which is comparison over time. See the credit-sales recovery note above before falling back to the proxy.

**Ranking.** Rank overdue customers **primarily by age and open balance** — `[auto]`. Apply payment behaviour, disputes, credit holds or strategic importance **only when those inputs were actually supplied** (or, for behaviour, actually derived — see above, and carry the caveats with it).

> **Do not turn missing flags into negative findings.**

Preserved, and worth restating in Mosofin terms: an absent dispute flag means **nobody recorded a dispute in a system that does not have a field for disputes.** It does not mean there is no dispute. Ranking a customer higher because "no dispute is flagged" converts a gap in the data into an accusation about the customer, and that is exactly the sort of confident wrongness that a live-data tool makes easy.

### Two checks to run before anyone is chased

*(Mosofin additions. Both are `[auto]`, both take one read, and both prevent a specific and avoidable embarrassment.)*

**1. Unapplied credits and payments on account.** Step 4 of the reconciliation already surfaces these as reconciling rows. Use them here too: **a customer with an unapplied credit note or a payment on account sitting against an overdue invoice may not owe what the aging says they owe.** Chasing someone for money they have already paid — money that is sitting unallocated in your own books — is the fastest way to lose the argument and the relationship at once. Check before drafting, every time, and flag any customer where an unapplied item exists.

**2. Duplicate invoices.** Same customer, same amount, invoice dates close together. `[auto]` to detect, `[manual]` to confirm. Some are genuine — a monthly retainer looks exactly like this. Some are a billing error, and the customer is not paying the second one because they are right not to. Flag the pattern; do not conclude from it.

### Recommended action bands

Preserved in full. **These are starting points, not policy** — the client's policy governs, and where they have one, Gate 3 should already have it.

- **1–30 days**: friendly reminder; confirm the invoice was received. `[auto]` to draft
- **31–60 days**: formal follow-up; request a payment date. `[auto]` to draft
- **61–90 days**: management review and direct contact. `[manual]` — a person makes the call
- **Over 90 days**: escalation review **under the user's approved policy**. `[manual]`
- **Disputed**: route to dispute resolution, **not to collection pressure**. `[manual]`
- **Bankruptcy or insolvency notice**: **stop ordinary dunning** and flag for professional review. `[manual]`

The last two are the ones that matter most and they are both `[manual]` by necessity: neither a dispute nor an insolvency is a field in the accounting system. **A skill reading the ledger alone will happily generate a dunning letter to a company in administration.** That is why the flags are asked for, and why their absence is disclosed rather than treated as an all-clear.

---

## Draft correspondence

`[auto]` to draft. **Never to send — there is no send path, and there must not be one in this skill.**

Group invoices **by customer** unless the user asks for invoice-level drafts. Include:

- invoice number
- due date
- open balance
- total due
- a neutral request for a payment status update

**Use only a payment method, contact, deadline, fee or escalation statement that the user supplied or that the QuickBooks data explicitly supports.** No invented bank details. No invented deadline. No fee that no policy authorises.

**Mark every draft `REVIEW REQUIRED - NOT SENT`.**

**Mosofin additions to the drafting rules:**

- If any read returned `mock: true`, **mark the draft as fixture-derived** as well. A reviewer checking the tone of a letter will not notice that the customer does not exist.
- If the customer has an **unapplied credit or payment on account**, the draft does not go out until that is resolved. Say so on the draft rather than adjusting the figure silently.
- Draft in the currency the report returned. Do not convert.
- The draft addresses one customer of one company file. **Never a combined letter across entities.**

---

## Deliverables

Return the **smallest deliverable that satisfies the request.** A full workpaper contains all six of the original's sections, plus one Mosofin addition.

1. **Run context and provenance** — company `display_name`, workspace name, as-of date, accounting basis, **capabilities called with their observed `effective_policy`**, automatic fields, user-supplied fields, missing fields, and the extraction timestamp.
2. **Aging Summary** — customer rows, calculated buckets, totals, concentration, and the recommended next action.
3. **Aging Detail** — the normalized invoice-level table.
4. **Collection Plan** — ranked customers, overdue amount, oldest age, reason for priority, blank owner/status columns, next action.
5. **Drafts** — review-only reminder text, every one marked `REVIEW REQUIRED - NOT SENT`.
6. **Exceptions and Reconciliation** — credits, non-invoice rows, missing due dates, currency issues, the summary-to-detail variance, **and the GL control-account comparison** if it was run.
7. **Coverage and Provenance** *(Mosofin addition)* — the mandatory coverage sheet, set out below. Section 1 above is its ancestor and is folded into it rather than duplicated.

If creating a spreadsheet, use the available spreadsheet skill and name it `QuickBooks_AR_Aging_Collections_YYYY-MM-DD.xlsx`.

Where more than one company file is in scope, the `display_name` goes in the file name **and** in a column on every sheet. Never one file with two companies' debtors interleaved.

---

## Completion checks

All eight of the original's checks are preserved. They are good, and several of them are doing the same job as the coverage sheet.

- The connected QuickBooks company and the as-of date are visible.
- Core invoice data came from **A/R Aging Detail**, not from a limited recent-invoice query.
- Summary and detail use the **same date** and are reconciled, or the variance is disclosed.
- **Every calculated field is reproducible from visible source fields.**
- QuickBooks-supplied, calculated, user-supplied and unavailable inputs are **distinguished**.
- Missing QuickBooks fields were requested **only when material** to the user's requested result.
- **No QuickBooks record was changed and no customer was contacted.**
- **Every reminder is clearly labelled as an unsent draft.**

**Four Mosofin additions:**

- The **workspace** was confirmed at Gate 0, by name, with an explicit yes — not merely the company file.
- **Capabilities were read from `get_datasource_tools` this run**, not assumed from this document or from the bundled reference.
- The **basis constraint was re-derived**, not asserted.
- **Fixture data, if any, is labelled** in the file name, on the provenance sheet, and on every draft.

---

## Seed to evolved: what happens on the first real run

This file is a **seed**. Every verdict in it is a prediction made without seeing the workspace.

**What must never be frozen into a seed:** a snapshot of which tools existed and what they could do. The original froze exactly one such fact — the accrual-basis-only constraint — and that single sentence is the clearest illustration in the whole pack of why the rule exists. It was probably true. It is stated as though permanent. And a reader following it would never discover it had changed, because the file tells them the answer instead of telling them to look. **Gate 2 looks, every run.**

**What is worth persisting after the first run, and this skill has more of it than any other in the pack:**

1. **The escalation policy and approved reminder wording.** Asked for on every run in the original. Obtained once, used forever. This alone justifies the lifecycle.
2. **Late-fee rules**, if any exist.
3. **The customer tier list** — strategic accounts, and who is never to be chased without a call first.
4. **Standing dispute and credit-hold flags**, with the caveat that they go stale and need refreshing rather than trusting indefinitely.
5. **The credit-sales denominator**: whether it turned out to be separable from cash sales, and if not, that the proxy is in use and why.
6. **The bucket convention**, if the client uses something other than the default six.
7. **The GL control-account comparison result** — whether the subledger has historically agreed with the control account, and what the recurring difference is if there is one.
8. **The derived days-to-pay baseline per customer**, so that next month's run can report *change* rather than level. A customer whose average days-to-pay went from 34 to 61 is a better finding than one who is simply slow.
9. **Whether a basis parameter existed** at Gate 2, so the next run knows whether the constraint is still real.
10. **Any observed policy that differed from this file's defaults.**

Persist through `create_skill`, scoped to the workspace it came from. **Client-specific facts belong in a client-scoped skill and never back in the seed** — and for this skill that is emphatic, because the facts in question are *customer names, tiers and dispute histories*. A seed that travels to the next engagement carrying the last client's debtor list would be a serious breach, not merely untidy.

**The evolved version asks almost nothing and reports change rather than level.** That is the target: run one produces an aging; run twelve produces "these four customers are deteriorating and here is the evidence," with no questions asked at all.

---

## Anti-patterns

- **Using Get Invoices as the core population.** It defaults to a recent window and drops the oldest unpaid invoices — the ones the whole exercise is about.
- **Calling a detail-to-summary tie a control-account reconciliation.** Two reports from the same records. Read the GL control account too; it is one extra call.
- **Asserting the basis constraint instead of checking it.** The original's one frozen capability, and the reason Gate 2 exists.
- **Treating the bundled reference as authority on tool names.** It orients; `get_datasource_tools` decides.
- **Assuming QuickBooks is directly installed.** It is a datasource behind the gateway, reached with a `data_source_id`.
- **Confirming the company but not the workspace.** Gate 0 comes first, always.
- **Turning a missing flag into a negative finding.** No recorded dispute is not the same as no dispute.
- **Chasing a customer who has an unapplied credit** sitting in your own books.
- **Replacing open balance with the original invoice amount** on a part-paid invoice.
- **Losing a leading zero** on a document number by treating it as a quantity.
- **Presenting a total-income DSO as DSO.** Label it, or get the real denominator.
- **Merging two entities' debtors into one exposure figure** without saying so.
- **Drafting a threat the client's policy does not authorise** — fees, suspension, legal escalation, or any promise about what will happen next.
- **Handing over a fixture-derived draft letter.** The reviewer will check the tone, not the existence of the recipient.
- **Offering to send it.** There is no send path. Say that plainly and finish the analysis.
