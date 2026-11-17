<!-- debt-and-covenant-tracking · method.md · read for: Stages 3–6 — the debt schedule, the covenants and the compliance report. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding)
- Step 0b — Debt-like item sweep (Mosofin addition)
- Step 1 — Build the debt schedule (facility inventory)
- Step 2 — Build amortization schedules
- Step 3 — Catalog the covenants
- Step 4 — Precise covenant definitions (the make-or-break detail)
- Step 5 — Compute the covenant ratios
- Step 6 — Project covenants forward
- Step 7 — Manage the maturity profile
- Step 8 — Compliance reporting
- Step 9 — Breach handling (if applicable)
- Step 10 — Output
- Step 11 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Never drop a task because no tool covers it.** A `[manual]` task is a task with a *named gap*, not an
absence — and in this skill the largest gap, the agreement, is also the most important document.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding)

Pull the `[auto]` / `[gated]` reads. **Batch independent reads into one message** — the debt accounts,
the P&L, the balance sheet and the cash accounts do not depend on each other. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`search_accounts`* — **every debt, lease liability, interest and cash account** — usually **[auto]**
- *`get_balance_sheet`* / *`get_trial_balance`* — **debt balances and cash at the testing date** —
  usually **[auto]**
- *`get_general_ledger`* on the debt accounts — **draws, repayments and interest, movement by movement**
  — usually **[auto]**
- *`get_profit_and_loss`* over the **trailing twelve months** — **book EBITDA components and interest
  charged** — usually **[auto]**
- *`search_bill_payments`* / *`search_purchases`* / *`search_transfers`* — **payments to lenders**, which
  evidence actual debt service — usually **[auto]**
- *`search_vendors`* / *`get-vendor`* — lenders as counterparties — usually **[auto]**
- *`get_cash_flow`* — cash generation, for coverage ratios — usually **[auto]**
- *`search_journal_entries`* — interest accruals and debt reclassifications — usually **[auto]**
- *`get_company_info`* — legal name, currency, period end — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — **a covenant position is certified to a lender by
an officer**, and a compliance conclusion drawn from fixtures would be a false certification.

## Step 0b — Debt-like item sweep (Mosofin addition)

**Run before Step 1.** The facility inventory is built from agreements the user knows about; this tests
it against the balance sheet.

**[auto]**: scan the accounts and balances for items that a covenant definition of "Debt" may capture even
though they are not loan agreements (*`search_accounts`*, *`get_balance_sheet`*,
*`get_general_ledger`*):

- **Finance and operating lease liabilities** — see the ASC 842 / IFRS 16 edge case; whether they count is
  definition-dependent, and getting it wrong moves the leverage ratio materially
- **Shareholder or director loans**
- **Deferred or contingent consideration** from an acquisition
- **Invoice discounting or factoring balances**
- **Overdrafts** — a negative cash balance is borrowing
- **Any interest-bearing payable**

**Report each against the facility inventory** and ask whether the agreement's definition of Debt includes
it. Where the sweep finds nothing beyond the listed facilities, **say it was run and found nothing** —
that is what makes the inventory's completeness defensible.

## Step 1 — Build the debt schedule (facility inventory)

For each facility:

- **Type** (term loan, revolver, mortgage, bond, lease debt, etc.) — **[manual]**
- **Lender / facility name** — **[gated]**; lenders often appear as vendors
- **Principal amount, current balance, undrawn capacity** — **balance [auto]**; **principal and undrawn
  capacity [manual]**, since the limit is not in the books
- **Interest rate** (fixed / floating; base + margin; rate reset dates) — **[manual]**
- **Maturity date** — **[manual]**
- **Amortization** (bullet, scheduled, balloon) — **[manual]**
- **Security / collateral** — **[manual]**
- **Currency** — **[gated]**
- **Key terms** (mandatory prepayments, prepayment penalties, change-of-control) — **[manual]**
- **Fees** (commitment, agency, unused) — **[gated]**; fees paid are visible in the ledger

**This inventory is the single source of truth — everything else builds from it.**

**[auto]** cross-check worth running: the **actual interest charged divided by the average balance** gives
the **effective rate borne**. Compare it to the stated rate. A material difference usually means fees are
being charged as interest, a margin has ratcheted, or the facility is not what the inventory says it is.

## Step 2 — Build amortization schedules

For each facility, period-by-period — **[gated]**: the forward schedule needs the terms, but **every
historic line is `[auto]`**:

- **Opening balance**
- **Scheduled principal payments** (per the amortization schedule)
- **Voluntary / mandatory prepayments**
- **New draws** (revolvers)
- **Interest accrual** (balance × rate × time)
- **Interest paid**
- **Closing balance**

**Build through the maturity date. For floating-rate debt, use the current rate — and run sensitivities at
higher and lower rates.**

**[auto]** and important: build the **historic** side from **ledger movements, not net balance changes**
(*`get_general_ledger`*). A revolver that was drawn and repaid within a period shows no net movement while
carrying real interest cost and real covenant impact. **Then compare actual against scheduled** — a
divergence means a prepayment, a missed payment, or a schedule that is out of date, and all three matter.

## Step 3 — Catalog the covenants

**For each agreement, list every covenant verbatim (or with precise reference).** **[manual]** throughout
— covenants live in the document.

**Financial covenants** — quantitative tests:

- **Leverage ratio**: Net Debt / EBITDA (typically capped at a maximum)
- **Interest coverage**: EBITDA / Interest (typically with a minimum)
- **Fixed charge coverage**: (EBITDA + something) / (Interest + Principal + something) (minimum)
- **Debt service coverage**: Cash flow / Debt service (minimum)
- **Minimum liquidity / Minimum cash**: (minimum)
- **Maximum capex**, **Minimum tangible net worth**, etc.

**Affirmative covenants** — **things the borrower must do**: deliver financials, maintain insurance, comply
with laws, and so on.

**Negative covenants** — **things the borrower must NOT do**: incur additional debt above a cap, pay
dividends above a basket, dispose of assets above a cap, change the business, undertake M&A above a
threshold.

**Events of default** — **what triggers default**: covenant breach, payment default, **cross-default to
other debt**, material adverse change, insolvency.

Note that the negative covenants and the affirmative deliverables are as capable of causing a default as
the financial ratios, and they get far less attention. **[auto]** can contribute to two of them: dividends
and distributions paid are readable against a basket, and new debt incurred is visible from the Step 0b
sweep.

## Step 4 — Precise covenant definitions (the make-or-break detail)

**Loan-agreement definitions of covenant components are critical and rarely match GAAP exactly.**
**[manual]**, all of it, and **blocking** — see the banner. For each covenant:

- **The exact numerator and denominator per the agreement**
- **"EBITDA" is almost never just book EBITDA** — typically defined with addbacks: one-time costs, stock
  comp, M&A costs, "permitted adjustments", often with caps on how much can be added back
- **"Debt" may exclude certain items** (leases, accruals) **or include items not on the balance sheet**
  (guarantees)
- **"Cash" may exclude certain restricted balances**
- **The testing period** (TTM / quarterly / annual)
- **The testing date** (period-end / month-end)

**A covenant computed against book numbers without the agreement's specific definitions will be wrong.
Always work from the agreement.**

**Mosofin's role here is to present the book starting point transparently** — each component as the ledger
reports it, clearly labelled — **so the definitional adjustments can be applied on top and each one
shown.** A covenant build that displays "book EBITDA → each addback → covenant EBITDA" is auditable; one
that shows only the final figure is not.

## Step 5 — Compute the covenant ratios

For each test date — **[gated]**: **[auto]** arithmetic on **[manual]** definitions:

- **Build each ratio's numerator and denominator per the precise definitions**
- **Compute the ratio**
- **Compare to the limit**
- **Compute headroom** — the cushion: e.g. if leverage must be ≤ 4.0× and actual is 3.2×, headroom is
  0.8 turns; **or, more usefully, the EBITDA reduction that would trigger a breach**
- **Determine compliance status**: in compliance / approaching the limit / breached

**Show the build — numerator components, denominator components, ratio, limit, headroom — auditable.**

Expressing headroom **as the fall in EBITDA that would cause a breach** is worth doing every time. "0.8
turns of headroom" means little to most readers; "profits could fall by £1.4m before we breach" is
immediately actionable.

## Step 6 — Project covenants forward

Beyond current compliance, project covenants forward using the forecast (`rolling-forecast` or a
three-statement model) — **[gated]**: the forecast is **[manual]**, the projection arithmetic
is **[auto]**:

- **Quarter-by-quarter projection of each ratio**
- **The most binding constraint and when it might bind**
- **Sensitivity to EBITDA, debt, and rate changes**
- **Identify the earliest projected breach (if any) and the headroom trajectory**

**Forward-looking covenant analysis prevents surprises.** The trajectory matters more than the point: a
comfortable ratio narrowing steadily every quarter is a more urgent finding than a tight one that is
stable.

**[auto]** contribution: the **scheduled amortization is known**, so the debt side of every future
quarter's ratio is largely determined already. Only the earnings side is uncertain — which means the
question "how far can EBITDA fall before we breach, in each future quarter?" is answerable now.

## Step 7 — Manage the maturity profile

- **Maturity schedule by year** (the **"maturity wall"**) — **[gated]**: balances **[auto]**, maturities
  **[manual]**
- **Refinancing risk**: large maturities approaching, market conditions
- **Refinancing timeline** — **most refinance well before maturity to avoid distress**
- **Concentration with single lenders / instruments** — **[gated]**: concentration by balance is
  computable once facilities are mapped to lenders

## Step 8 — Compliance reporting

**Most agreements require periodic compliance certificates:**

- **The required format and frequency** (often quarterly) — **[manual]**
- **The computation, signed by an officer** — **[manual]** to sign; Mosofin certifies nothing
- **Other required deliverables** (financials, projections) — **[manual]**
- **Track delivery deadlines** — **[gated]**: once the calendar is stored, upcoming deadlines are
  trackable

**A missed deadline is itself a default** in many agreements — see the edge case. The calendar is not
administrative housekeeping; it is a covenant.

## Step 9 — Breach handling (if applicable)

If a covenant is breached or projected to breach:

- **Immediate**: **notify management and likely counsel; covenant breaches can trigger acceleration and
  cross-defaults**
- **Engage the lender**: **waivers and amendments are often negotiable, especially before a missed
  payment**
- **Document**: the breach, the cause, remediation, the waiver or amendment
- **Accounting effect**: **a breach can reclassify long-term debt to current**
  (`financial-statement-builder`); **may affect going concern**, a matter for the notes

**Breach is a serious event — flag for legal and governance involvement.**

Two Mosofin-specific cautions here, both about restraint:

- **Do not declare a breach from book figures.** Given the definitional gap, a book-based ratio can show a
  breach that does not exist under the agreement — and raising a false breach with a lender has
  consequences of its own.
- **The reclassification to current is material and detectable in its absence.** Where a breach is
  confirmed, check whether the debt is still shown as long-term (*`get_balance_sheet`*, **[auto]**) — if
  it is, the balance sheet is misstated, and it is the kind of misstatement auditors look for.

## Step 10 — Output

Deliver an `.xlsx` workbook.

**Sheet 1: Facility Inventory** — each facility with key terms. **Mark each field as read or supplied**,
and include the **effective rate borne** alongside the stated rate. Add a header block: workspace name;
each in-scope company file by `display_name`; each excluded one and why; **the covenant testing
perimeter**; whether any figure rests on `mock` data.

**Sheet 2: Amortization Schedules** — per facility, period-by-period. **Historic lines from ledger
movements, forward lines from the terms**, with actual-versus-scheduled variance shown.

**Sheet 3: Covenant Register** — each covenant verbatim with key definitions referenced. **Flag every
covenant whose definitions have not been supplied** — those are the ones not computed.

**Sheet 4: Covenant Compliance — Current Period** — each ratio: **book components → definitional
adjustments → covenant components → ratio → limit → headroom → status**. Headroom expressed **both as a
ratio cushion and as the EBITDA fall that would breach**.

**Sheet 5: Covenant Projection** — forward quarters; sensitivity; earliest projected breach; headroom
trajectory.

**Sheet 6: Maturity Profile** — by year, concentration, refinancing horizon.

**Sheet 7: Compliance Calendar** — required certificate and reporting dates, with the next ones due.

**Sheet 8: Breach / Waiver Log** — history of breaches, waivers and amendments.

**Sheet 9: Debt-Like Item Sweep — NEW, Mosofin-specific**

| Balance sheet item | Amount | On the facility inventory? | Captured by the agreement's Debt definition? | Effect on leverage if included |

**Sheet 10: Coverage — NEW, Mosofin-specific**

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used | Policy | `mock` | Gap — what could not be evidenced and who supplied it |

**Every covenant definition row reads `manual`.** A covenant computed without one should not appear at
all.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming:** `Debt_Covenant_[YYYY-MM]_[EntityName].xlsx`

`[EntityName]` is the company file's `display_name`, or the borrowing group's name where the covenant is
tested at group level. Every file states which datasource and `display_name` it covers, and the perimeter
tested.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where the data does not
cover something — every term, every definition — **name the source required** instead of estimating.

## Step 11 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

Covenants are tested quarterly, so this step pays back four times a year.

On an explicit yes, persist the **decisions**:

- **The facility inventory's fixed terms**: type, lender, principal, rate basis, maturity, amortization
  pattern, security. These do not change between tests
- **The covenant definitions**, component by component — **the single most valuable artefact in this
  skill.** They are buried in a long document, they are the thing that makes the ratio correct, and
  re-extracting them every quarter is both slow and error-prone
- **The covenant limits and the testing calendar** — dates, frequency, certificate format
- **The testing perimeter** — which entities form the borrowing group
- **The account map**: which accounts constitute Debt, Cash and each EBITDA component **under the
  agreement's definition**, so the build is reproducible
- **The cross-default map** — which facilities trigger which
- **Waivers and amendments in force**, with their expiry
- The replay recipe: the exact sequence of reads that produced the balances and book components

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Do not persist covenant ratios, headroom figures, balances, or any breach position.** A stored record
that the entity was close to breach is highly sensitive — it is exactly the information that damages a
refinancing negotiation if it circulates, and it is stale within a quarter. **Persist the definitions and
the terms; re-compute the position.**

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / Northbrook
Trading — facility A: leverage ≤ 3.5× tested quarterly on TTM covenant EBITDA (book EBITDA plus
restructuring capped at 10%); Debt excludes operating leases" — not "leverage ≤ 3.5×". **Different
facilities define the same-sounding ratio differently**, and an unlabelled definition applied to the wrong
facility produces a confident, wrong compliance conclusion. Record the chosen **scenario** (single vs
multi, and the borrowing perimeter) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's** — and every balance, ratio and headroom figure is state.

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — and here that flag matters: **if an entity has left the borrowing group
or been disposed of, the covenant perimeter has changed**, which is a substantive event, not a data
issue. Ask.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One facility set, one perimeter.

**Multi-entity.** Steps 0–10 read **once per entity**, each call targeting exactly one `data_source_id`,
every balance carrying its entity's `display_name`. Then:

- **The covenant perimeter is defined by the agreement, not by the workspace.** It may be the whole group,
  a sub-group ("the Restricted Group"), or one borrower. **Confirm it explicitly and state it on every
  output.** A ratio computed over the connected set rather than the defined perimeter is wrong even if
  every other input is right.
- **Consolidate the perimeter properly before computing.** Intercompany debt between entities inside the
  perimeter is usually excluded; intercompany debt to an entity outside it usually is not.
- **Entities outside the perimeter still matter for negative covenants** — restrictions on transferring
  assets or cash to unrestricted subsidiaries are common, and the transfers themselves are readable.
- **Guarantees cross entity lines.** An entity may guarantee another's debt without carrying it on its own
  balance sheet, and guarantees are frequently inside the covenant definition of Debt. They are
  `[manual]` — nothing in the ledger shows a guarantee.
- **Cross-default links facilities across entities.** One entity's breach can accelerate another's debt.
  Map it.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict per company
file.
