<!-- payroll-tax-filings · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding) — Mosofin addition
- Step 1 — Identify the filing obligations
- Step 2 — Determine deposit / remittance schedule
- Step 3 — Compute the amounts due
- Step 4 — Reconcile deposits to liabilities
- Step 5 — Prepare periodic returns
- Step 6 — Year-end filings and wage statements
- Step 7 — Organize remittance and filing package
- Step 8 — Output
- Step 9 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Never drop a task because no tool covers it.** Almost every input here is legitimately `[manual]`, and
that is the correct result for a skill whose subject is statutory values.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding) — Mosofin addition

**Batch independent reads into one message** — the accounts, the balances, the payments and the journals do
not depend on each other. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`search_accounts`* — **every payroll tax liability account** — usually **[auto]**
- *`get_balance_sheet`* / *`get_trial_balance`* — **the liability balances, at each period end in scope** —
  usually **[auto]**
- *`get_general_ledger`* on **each liability account** — **accruals and remittances, with dates** — usually
  **[auto]**. **The central read**
- *`search_payments`* / *`search_checks`* — **deposits made, by payee and date** — usually **[auto]**.
  **The other half of Step 4**
- *`search_vendors`* — **the tax authorities as payees**, to map payments to obligations — usually
  **[auto]**
- *`get_profit_and_loss`* — wages and employer cost expense, for context — usually **[auto]**
- *`get_company_info`* — **legal name — the employer of record** — country, fiscal calendar — usually
  **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — **these figures go on a statutory filing**, and a
fixture-based deposit reconciliation would conclude that liabilities were settled when they were not.

## Step 1 — Identify the filing obligations

**For the jurisdiction(s), confirm what's required — do not assume; confirm current** — **[manual]**:

- **Withholding remittances**: **employee income tax withheld, remitted on a schedule** — frequency often
  depends on size
- **Social / payroll contribution remittances**: **employee + employer contributions**
- **Periodic returns**: **reports of wages and taxes for the period**, often quarterly
- **Year-end filings**: **annual reconciliations and employee wage statements**
- **Other employer taxes**: **unemployment, levies, training taxes** — jurisdiction-specific

**Map each obligation, its frequency, the form or mechanism, and the deadline.**

**[auto]** contribution — **the liability accounts are a partial map of the obligations.** Reading them
shows which taxes this entity actually accrues, which is a useful cross-check against the obligation list.
**Two mismatches are worth raising:**

- **A liability account with no obligation on the list** — an obligation nobody mapped, or a dormant one
- **An obligation on the list with no liability account** — **it may not be being accrued at all**, which
  is a more serious gap than a mapping error

**The account list is not the obligation list.** An entity can have an obligation it has never accrued.

## Step 2 — Determine deposit / remittance schedule

**Remittance frequency** — per-payroll, monthly, quarterly — **is usually assigned based on the employer's
size or history (confirm the rule).** For each obligation — **[manual]**:

- **Determine the required deposit schedule**
- **List due dates for the period**
- **Flag the consequences of late deposits** — **penalties scale with lateness** — **flag rather than
  computing punitive amounts without confirming rules**

**This step is entirely `[manual]`, and the edge case about schedule changes makes it dangerous to
shortcut.** **An employer's frequency can change year to year based on prior-period volume**, and **using
last year's schedule causes late deposits on the correct amounts** — a penalty for a timing failure, not a
computational one.

**[auto]** contribution once the schedule is supplied: **the historical payment pattern shows what the
entity has actually been doing.** **A pattern inconsistent with the stated schedule is worth raising** —
either the schedule changed and nobody updated the practice, or the practice was never right.

## Step 3 — Compute the amounts due

From the payroll registers, for each tax or contribution — **[gated]**, and **every rate is `[manual]`**:

- **Determine the correct taxable wage base** — gross, or gross less pre-tax deductions, **subject to caps**
  — see `payroll-reconciliation` Step 5. **`[manual]`; not derivable from the GL**
- **Apply the current rate** — **confirm; never hardcode** — **[manual]**
- **Respect annual wage-base ceilings** — contributions that stop at a cap — **[manual]**, and **per
  employee**
- **Sum employee and employer portions correctly** — **[auto]** arithmetic once the components exist
- **Arrive at the amount due for each obligation and period**

**Three things about this step in a Mosofin run:**

**The base and the rate are both `[manual]`, so the computation is too.** **What the workspace supplies is
the check, not the computation** — see Step 4.

**Caps are per employee and cannot be aggregated.** The same limit as `payroll-reconciliation`: **no group
figure recovers a per-employee ceiling.**

**And the amount due is not the liability balance.** **The balance is what was accrued; the amount due is
what the rules require.** **Where they differ, the accrual was wrong** — and that is a finding worth having
before the filing, not after.

## Step 4 — Reconcile deposits to liabilities

For each obligation — **[gated]**, and **this is the step the workspace substantially performs**:

```
Liability incurred (from registers/GL)
− Deposits/remittances already made
= Balance still due (or overpaid)
```

**Both terms are `[auto]`**: **the liability from the GL**, **the deposits from the payment records** by
payee and date.

**Confirm:**

- **Deposits were made on time and in the right amounts** — **[gated]**: **the dates and amounts are
  `[auto]`; the due dates are `[manual]`.** **Given them, timeliness is exact** — "deposited on the 24th
  against a due date of the 22nd" rather than "appears late"
- **The GL liability balance matches the amount that should still be owed** — **[auto]** against the
  computed amount
- **No under- or over-deposits — both cause problems** — **[auto]**

**This draws on `payroll-reconciliation`.**

**Two Mosofin emphases:**

**An over-deposit is not a safe error.** It ties up cash, and **recovering it usually requires an
adjustment on a subsequent filing or a refund claim** rather than simply stopping. Report it as an item
requiring action, not as a comfort.

**A payment that left the company is not a deposit that arrived.** **With a third-party provider, Step 4 can
reconcile perfectly while nothing has been remitted.** **The `[auto]` evidence stops at the company's bank
account.** **Say where it stops.**

## Step 5 — Prepare periodic returns

For each periodic — e.g. quarterly — return — **[gated]**:

- **Total wages (and taxable wages per each tax's base)** — **gross `[auto]`, taxable `[manual]`**
- **Total tax withheld / contributed** — **[auto]** from the GL, **subject to the accrual being right**
- **Deposits made** — **[auto]**
- **Balance due or overpayment** — **[auto]**
- **Headcount / other required data points** — **[gated]**; headcount `[auto]`, the required definition
  `[manual]`

**Ensure the return figures tie to the registers and GL for the period.**

**[auto]** for the GL leg of that tie; **the register leg needs the register.** **State which legs were
tied.**

## Step 6 — Year-end filings and wage statements

At year-end — **[gated]**:

- **Employee wage statements**: **each employee's annual gross, taxable wages (per base), and amounts
  withheld** — **[manual]** from the register; **personal data**
- **Annual reconciliation / return**: **total wages and taxes for the year, reconciled to the sum of
  periodic returns and to the GL** — **[gated]**; **the GL leg `[auto]`**
- **Three-way tie**: **sum of wage statements = sum of periodic returns = GL annual wages / taxes. All
  three must agree before statements are issued.**

**Resolve any differences before distributing statements** — **employees use them for their own returns;
errors cascade.**

**The three-way tie is the most consequential check in this skill**, and **the workspace supplies one leg
of it exactly and immediately.** **[auto]**: the GL annual wages and taxes are available the moment the year
closes, **which means two of the three legs can be compared as soon as the registers are — before the
returns are even assembled.**

**And the deadline is real.** **A wage statement issued and later corrected means amended filings, amended
employee tax returns, and in many jurisdictions a penalty per statement.** **Resolve first, issue second.**

## Step 7 — Organize remittance and filing package

Produce a clear package — **[gated]**:

- **Each filing with its figures, due date, and supporting reconciliation**
- **Remittance schedule with amounts and dates**
- **Reconciliations tying everything to the registers and GL**
- **Flagged items needing confirmation or professional review**

**Mosofin addition to the package**: **every statutory value used, with its source and its year**, in one
place. **A filing package whose rates cannot be traced to a source is one nobody can review**, and the
original's own standard requires that nothing be hardcoded — **which only means something if the sourcing is
visible.**

## Step 8 — Output

Deliver an `.xlsx` workpaper:

**Sheet 1: Filing Obligations Calendar**

| Obligation | Frequency | Form/Mechanism | Period | Due Date | Status |

Add **Source** and **Year confirmed** columns — **every one of frequency, form and due date is `[manual]`**.
Plus the header block: workspace name; the entity by `display_name` **as employer of record**; excluded
company files; **whether a provider files and remits**; whether any figure rests on `mock` data.

**Sheet 2: Amounts Due Computation**

| Tax/Contribution | Taxable Base | Rate (current) | Cap Applied | Employee | Employer | Total Due |

**Every rate and cap carries its source and year.**

**Sheet 3: Deposit Reconciliation** — **liability vs. deposits made vs. balance due, with timeliness
flags.** **Both sides `[auto]`; the due dates supplied.** **Over-deposits flagged as requiring action.**

**Sheet 4: Periodic Return Figures** — **return-ready figures, tied to registers and GL**, **stating which
legs were tied**.

**Sheet 5: Year-End Reconciliation** — **wage statements ↔ periodic returns ↔ GL three-way tie**, with
**the GL leg marked `[auto]`** and differences listed.

**Sheet 6: Wage Statement Data** — **per-employee annual figures.** **The only per-employee sheet in this
skill**, and it exists because the statements require it.

**Sheet 7: Open Items / Professional Review** — **rates, schedules, forms, and deadlines flagged for
current-source confirmation and professional sign-off.**

**Sheet 8: Statutory Values Used — NEW, Mosofin-specific**

| Value | Amount / rule | Jurisdiction | Source | Year | Confirmed by | Date |

**Every rate, ceiling, threshold, frequency and deadline used anywhere in the workpaper.** **Nothing appears
in a computation that is not on this sheet.**

**Sheet 9: Coverage — NEW, Mosofin-specific**

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used / external source | As-at date | `mock` | Gap |

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming:** `Payroll_Tax_Filings_[Period]_[EntityName].xlsx`

Every file states which datasource and `display_name` it covers, and the jurisdiction.

**Grounding:** every ledger figure traces to a tool result in this conversation; **every statutory value
traces to Sheet 8.** End with a single **Data sources** line. Where confirmation of actual deposit was not
obtained, **say so** rather than reporting the liability as settled.

## Step 9 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The obligation map** — which taxes, which jurisdictions, which forms, which mechanism. **The most
  valuable stored asset here**, and it changes only when the business does
- **The account-to-authority map** — which liability account corresponds to which obligation and which
  payee. **This is what makes the deposit reconciliation automatic each period**
- **The registration and account numbers**, **by reference**
- **The filing calendar structure** — which obligations fall when, relative to period ends
- **The provider arrangement** — who files, who remits, and **who obtains proof of deposit**
- **The rate and schedule *sources*** — which authority publication, checked when, by whom. **Never the
  rates themselves**
- **The taxable base rules** per tax, **with the statutory year they applied to**
- **Known multi-jurisdiction complexity** and the specialist engaged
- The replay recipe: the exact sequence of reads that produced the liabilities and the deposits

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist rates, ceilings, thresholds, deposit frequencies or deadlines.** **They change annually, and
a stored rate reused silently produces an underpayment with penalties** — which is precisely the failure
this skill exists to prevent. **Persist the source; re-confirm the value.**

**And never persist any employee's wage or withholding data.** Wage statement figures are personal data
about identifiable people.

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / Northbrook
Trading Ltd — employer of record, PAYE and NI to HMRC, liability accounts 2210/2211/2212, paid to payee
'HMRC Cumbernauld', monthly cadence, rates confirmed annually each April from the authority's published
rates" — not "monthly cadence, rates each April". **Obligations attach to the legal employer**, and applying
one entity's obligation map to another files the wrong return under the wrong registration. Record the
chosen **scenario** (single vs multi) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's.**

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** One employer, one set of registrations, one filing set.

**Multi-entity.** **Each entity is a separate employer**, and this is a legal fact rather than a reporting
convention:

- **Filings are never consolidated.** **Each entity files under its own registration**, on its own schedule,
  for its own employees. **A group total is meaningless to a tax authority.**
- **Deposit schedules are assigned per employer**, based on that employer's own size and history. **Two
  group entities can be on different frequencies.**
- **Wage-base ceilings apply per employer per employee.** An employee moving between group entities mid-year
  **may restart a cap in the new entity**, depending on jurisdiction — see `payroll-reconciliation`. **This
  affects the amount due and is easily missed.**
- **Run the deposit reconciliation per entity.** A payment by one entity covering another's liability is an
  **intercompany balance**, not a deposit for that entity — see `intercompany-reconciliation` — **and the
  entity whose liability it was still has an unsettled obligation on its own account.**
- **Registration gaps are per entity.** An entity employing people in a jurisdiction where it is not
  registered **has an obligation it cannot currently meet** — see the edge case; flag it immediately.
- **A shared provider does not merge the obligations.** It files separately for each employer, and **proof
  of deposit is needed per employer.**

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict per company
file.
