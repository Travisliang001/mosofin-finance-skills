<!-- 1099-and-t4a-prep · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding)
- Step 1 — Build a reportable vendor list
- Step 2 — Classify payments to the correct form / box / line
- Step 3 — Validate required fields per vendor
- Step 4 — Reconcile payments
- Step 5 — Produce the filing list
- Step 6 — Backup withholding / under-deduction reconciliation
- Step 7 — Output
- Step 8 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Everything below is the professional procedure, unchanged in step count, order, or
substance. What has been added is the plain-language wording, the `[auto]` / `[gated]` /
`[manual]` verdict per task, and the tool that typically evidences it.

**Never drop a task because no tool covers it.** A `[manual]` task is a task with a *named
gap*, not an absence. Silently omitting it would imply a check that never happened.

The tool names shown in *italics* are the **typical** evidence tool. Resolve the real name
and its policy from your Gate 2 catalog for this workspace and this company file — the
italic name is a pointer, not a promise.

## Step 0 — Fetch the evidence (grounding)

Before Step 1, pull the reads the capability map marked `[auto]` or `[gated]`. **Batch
independent reads into one message** — a vendor list, a payment search, and a general
ledger read do not depend on each other, so they run in parallel. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries and
follow-ups.

Typical opening batch, per in-scope entity:

- *`search_vendors`* — the vendor master (who you paid) — usually **[auto]**
- *`get_vendor_expenses`* — total spend per vendor for the year — usually **[auto]**
- *`search_bills`*, *`search_bill_payments`*, *`search_purchases`* — the individual
  transactions behind those totals — usually **[auto]**
- *`get_general_ledger`* — the underlying account-by-account detail used for the tie-out —
  usually **[auto]**
- *`get_company_info`* — the payer's own details — usually **[auto]**

Handle the envelopes you get back:

- `approval_required` → ask the user in chat, then re-invoke the same tool with
  `approved=true` (**reads only — never for a write**).
- `entity_required` → you did not pass a company file and more than one is live. Ask by
  `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error itself; do not guess a name.
- Dead connection → surface the `reconnect_url` to the user.

Check the **`mock` flag** on every result. `mock: true` means fixture/demo data — it can
illustrate the shape of the output but **cannot support a filing assertion**. If any figure
in a return rests on mock data, say so at the top of the deliverable and do not present the
return as filing-ready.

## Step 1 — Build a reportable vendor list

Work out which of the people and businesses you paid actually have to be reported.

For each vendor in the master — **[auto]** via *`search_vendors`* / *`get-vendor`*:

- **Was the vendor paid during the year? Sum total payments.** — **[auto]** via
  *`get_vendor_expenses`*, cross-checked against *`search_bill_payments`* and
  *`search_purchases`*. "Paid" means cash actually left, not just a bill recorded.
- **Was the vendor a reportable entity type for this jurisdiction?** — **[gated/manual]**:
  the *type* of business (sole trader, partnership, corporation) is a field on the vendor
  record where the books capture it, but it is frequently blank or wrong, and the
  jurisdiction's rule is the user's to supply. Examples of what different regimes cover:
  - **US 1099-NEC**: payments to non-corporation persons/entities for **services** in the
    course of a trade or business ("non-employee compensation" — money paid to someone who
    works for you but is not an employee)
  - **US 1099-MISC**: rents, royalties, prizes, certain medical payments, attorney
    payments, etc. — each in a specific numbered box
  - **US 1099-K**: payment-card and third-party-network transactions. Typically issued **by
    the payment processor**, not by you — see the edge case below before you report any of
    these yourself
  - **Canada T4A**: fees, commissions, scholarships and similar amounts paid to people who
    are not employees
  - **Canada T5018**: subcontractors in construction
  - **UK CIS**: subcontractors under the **Construction Industry Scheme** (a UK regime where
    the main contractor deducts tax at source from subcontractor payments and reports it
    monthly)
  - **(Other jurisdictions)**: per the user's stated requirements

- **Pull the vendor's tax form on file** — **[manual]** in almost every workspace. The
  signed certification is a *document*, not ledger data. Where the platform exposes an
  attachments catalogue (*`search_attachables`* / *`get_attachable`*), you may be able to
  see **that a file exists and what it is called** — that is metadata, not the form's
  contents, and is evidence of filing, not of validity. State the distinction. What is
  needed per regime:
  - **US**: W-9 (for US persons), W-8 series (for non-US persons) — the form on which a
    vendor certifies their name, tax ID and entity type
  - **Canada**: the T4A information-request equivalent
  - **UK CIS**: the CIS registration / verification record (which also sets the deduction
    rate)

Then filter:

- **Exclude payments to corporations if the jurisdiction excludes them.** — **[gated]**.
  US 1099-NEC generally excludes C-corporations and S-corporations, **but does include
  attorneys regardless of entity type** — confirm this with the user rather than applying
  it silently.
- **Include only payments in scope of the form.** — **[auto]** where the ledger's account
  coding is reliable (*`get_general_ledger`*, *`search_accounts`*). E.g. 1099-NEC covers
  services; rent belongs on 1099-MISC instead.
- **Apply the payment threshold the user provided.** — **[auto]** arithmetic on
  **[manual]** input. Use the figure from Gate 3 and state it in the output; never a
  remembered one.

## Step 2 — Classify payments to the correct form / box / line

Each form has numbered boxes, and each kind of payment belongs in a specific one. Putting a
right amount in a wrong box is still a wrong return.

For each reportable vendor, classify each payment to the correct reporting category —
**[auto]** where the ledger account or item coding maps cleanly (*`get_general_ledger`*,
*`search_purchases`*, *`search_bills`*, *`search_accounts`*), **[gated]** where the mapping
needs the user's judgment:

**US 1099-NEC**:
- Box 1: Non-employee compensation

**US 1099-MISC**:
- Box 1: Rents
- Box 2: Royalties
- Box 3: Other income
- Box 6: Medical and health care payments
- Box 7: Direct sales of $5,000+
- Box 10: Gross proceeds paid to an attorney (money routed *through* a lawyer, e.g. a
  settlement, reported even though it is not the lawyer's own fee income)
- Box 14: Excess golden parachute (an outsized payout triggered by a change of ownership)
- (Other boxes per the form's current-year specification — **user provides**)

**Canada T4A**:
- Box 020: Self-employed commissions
- Box 048: Fees for services
- Other boxes per CRA specification — **user provides**

**UK CIS**:
- Per the CIS monthly return

**If a vendor has multiple payment types, allocate each to its proper box / line. Sum per
box.** — **[gated]**: the split is arithmetic, but which payment is which type is a
judgment call the user confirms.

## Step 3 — Validate required fields per vendor

Check that you actually hold everything the form asks for, for every vendor you are about
to report. A missing tax ID is the single most common reason a filing gets rejected.

For each reportable vendor, confirm:

- **Legal name matches the tax form** — **[auto/manual]**: the name on the vendor record is
  *`get-vendor`* / *`search_vendors`* (**[auto]**); the name on the signed form is
  **[manual]**. Compare them and flag mismatches. The legal name is often not the trading
  name you know them by.
- **Tax ID on file and format-valid for the jurisdiction** — **[auto/gated]** where the
  books hold a tax-identifier field, otherwise **[manual]**. The identifier goes by
  different names: **TIN** (US taxpayer identification number), **SIN** (Canadian social
  insurance number), **BN** (Canadian business number), **UTR** (UK unique taxpayer
  reference). Check the format matches what the jurisdiction expects.
- **Address complete** — **[auto]** via *`get-vendor`*.
- **Entity type captured** — **[auto]** where recorded, **[manual]** where blank.
- **Tax form signed and dated** — **[manual]**.
- **Form is current (not expired per the jurisdiction's rules)** — **[manual]**.

**Flag missing or invalid items.** A vendor without a valid tax ID may trigger **backup
withholding** in the US (you are required to hold back a slice of future payments and remit
it to the tax authority) or non-reporting consequences elsewhere. Do not quietly proceed
with a blank.

## Step 4 — Reconcile payments

Prove your totals. The number you report has to agree with the books, or someone will
eventually ask why it doesn't.

For each vendor, sum payments by:

- **Payment date in the reporting year** — **[auto]** via *`search_bill_payments`*,
  *`search_purchases`*, *`search_deposits`*. Note: some jurisdictions require these returns
  on a **cash basis** (count it when the money moved) even when the books are kept on an
  **accrual basis** (count it when the obligation arose). Where the platform lets you set an
  accounting method on a report, set it deliberately and say which you used.
- **Payment method** (cash, cheque, ACH, wire) — **[auto]** where the transaction type is
  recorded. Typically all are in scope; **card payments may be excluded** if the processor
  reports them separately.
- **Currency** — **[auto]** to detect, **[gated]** to convert. Convert to the reporting
  currency at the payment-date rate or the annual average, per the jurisdiction's rule
  (from Gate 3). State which rule and which rates you used.

Compare totals to:

- **The general ledger by vendor** — **[auto]** via *`get_general_ledger`* /
  *`get_vendor_expenses`*. This is the tie-out: the proof that the filing list and the books
  tell the same story.
- **The vendor's own statement, if available** — **[manual]**: an external document the
  workspace cannot see.
- **Prior year's filings, as a sanity check** — **[manual]** unless the user supplies last
  year's filed list. A vendor who jumped from $2k to $200k, or vanished entirely, is worth a
  second look.

## Step 5 — Produce the filing list

For each reportable vendor:

- Vendor identifier
- Legal name
- Tax ID
- Address
- Entity type
- Each form / box with its total amount
- Validation status (are all required fields present?)
- Filing format (paper / e-file)

For the entity (the **payer** — you, the business doing the filing) — **[auto]** via
*`get_company_info`*:

- Payer name, address, TIN
- Total forms by type
- Total amounts by type

In a multi-entity run, produce this block **once per entity**, each labelled with its
datasource and `display_name`. Each connected company file is usually a separate filer with
its own returns.

## Step 6 — Backup withholding / under-deduction reconciliation

Some regimes make you hold back part of a payment and send it to the tax authority yourself.
This step checks you held back the right amount.

Some jurisdictions require:

- **Withholding on payments to vendors who didn't certify** (US backup withholding)
- **Deductions under specific schemes** — UK CIS has three statuses: **standard** rate,
  **higher** rate (for unverified subcontractors), and **gross** status (no deduction at all)
- **Treaty-rate withholding for non-resident vendors** — a reduced rate available under a
  tax treaty between two countries

Reconcile — **[auto]** for the ledger half where a withholding liability account exists
(*`get_general_ledger`*, *`search_accounts`*), **[manual]** for the rest, since what
*should* have been withheld depends on each vendor's certified status:

- Total withheld during the year
- Total that should have been withheld per current vendor status
- Variance → either **over-withheld** (the vendor is owed a refund) or **under-withheld**
  (the business may owe the difference)

If the workspace holds no withholding account, say that explicitly rather than reporting
zero — "no withholding account was found in the connected books" and "nothing was withheld"
are different statements.

## Step 7 — Output

Deliver an `.xlsx` workpaper. Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**Sheet 1: Filing Summary**
- Reporting year, jurisdiction
- Forms in scope
- Vendor count and amount totals by form
- Validation pass / fail count
- Filing channel and due dates (user-supplied)
- **Added:** workspace name; each in-scope company file by `display_name`; each excluded
  company file and why; whether any figure rests on `mock` data

**Sheet 2: Reportable Vendor List**

| Vendor | Legal Name | Tax ID | Entity Type | Address | Form | Box / Line | Amount | Validation Status | Notes |

**Sheet 3: Excluded Vendors**

Vendors paid during the year but not reportable, with the exclusion reason (corporation /
under threshold / non-reportable category).

**Sheet 4: Validation Exceptions**

| Vendor | Missing Field(s) | Action Required |

**Sheet 5: Per-Form Detail**

One tab per form type with full filing-ready rows.

**Sheet 6: Payment Reconciliation**

| Vendor | GL Total | Filing Total | Variance | Reason |

**Sheet 7: Withholding Reconciliation** (if applicable)

| Vendor | Required Withholding | Actual Withholding | Variance | Action |

**Sheet 8: Coverage — NEW, Mosofin-specific**

The auditable record of what was actually verified versus assumed. One row per task in
Steps 1–6:

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used | Policy (enabled / permission / disabled) | `mock` | Gap — what could not be verified and what the user must supply |

In a multi-entity run this sheet is **per entity**, because a tool enabled for one company
file may be disabled for its sibling — the same task can be `[auto]` for one location and
`[manual]` for another.

**File naming:** `[Jurisdiction]_[FormType]_[Year]_FilingPrep.xlsx`

In a multi-entity run, include the entity: `[Jurisdiction]_[FormType]_[Year]_[EntityDisplayName]_FilingPrep.xlsx`,
plus one combined file named for the set. Every file states, on its summary sheet, exactly
which datasource and which `display_name` it covers.

**Grounding:** every figure in the deliverable must trace to a tool result in this
conversation or to something the user supplied by hand and that is labelled as such. Do not
tag individual figures with citations; end the answer with a single **Data sources** line
grouping the calls by datasource. Where the fetched data does not cover part of the
question, **name the tool that would have covered it** instead of estimating.

## Step 8 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** The first run discovered the workspace and
interviewed you. That does not need to happen again.

After the user has **seen the results** and approved them, ask — explicitly, at that point,
not earlier — whether to save this as their own customized version. A general "yes, go
ahead" from the start of the conversation does not count.

On an explicit yes, persist the **decisions**:

- The Gate 3 answers: reporting jurisdiction, form types in scope, thresholds applied and
  where they came from, currency-conversion rule, filing channel, entity-type overrides for
  specific vendors, the standing list of vendors always excluded and why
- Any generated assets: the vendor-classification mapping (which ledger account feeds which
  box), the workpaper template, folder and file-naming conventions
- The replay recipe: the exact sequence of reads that produced this year's return

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the
preference and asset files; set `datasources=` to match the recipe; no `.html`, `.css`, or
`.svg` files. Or write them as preference files alongside the installed skill, per the
user's setup.

**Key every preference and asset by datasource + entity `display_name`.** Write
"quickbooks / Northbrook Contracting — threshold $600, jurisdiction US, forms 1099-NEC +
1099-MISC" — not "threshold $600". The moment a second company file connects, an unlabelled
preference is ambiguous, and applying one location's vendor classification to another is
silently wrong. Record the chosen **scenario** (single vs multi, and which set) as a
preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status
belong to the workspace, not to the user's decisions. They change between runs and are
re-discovered by Gates 1–2 every time. **Decisions are the user's; state is the
workspace's.**

On later runs, match the stored entity names against Gate 1's live list. An entity that
appears in preferences but is no longer connected is **flagged to the user** — never
silently dropped, and never quietly applied to a different entity.

---

## Both entity scenarios

**Single-entity.** The workflow above, exactly as written, against one `data_source_id`.
One filer, one set of returns, one workpaper.

**Multi-entity.** Steps 0–7 run **once per entity**, each call targeting exactly one
`data_source_id`, and every pull, finding, and output carrying that entity's
`display_name`. Then one cross-entity step:

- **A side-by-side comparison**, not a consolidation. Information returns are filed per
  filer — each company file is normally its own payer with its own TIN, and merging their
  vendor totals into one return would be a filing error, not a summary. The exception is
  where several entities genuinely file under **one** tax ID (see the edge case below), in
  which case the aggregation is correct and must be stated explicitly.
- The comparison sheet shows, per vendor across entities: who was paid by more than one
  entity, whether the same vendor was classified consistently, and whether a vendor sits
  below the threshold at each entity individually but above it in aggregate — which matters
  only if the entities file jointly.

Capability is checked **per entity** at Gate 2. The coverage sheet shows each task's
verdict for each company file separately.
