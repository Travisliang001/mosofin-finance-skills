<!-- benefits-and-401k-accounting · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding)
- Step 1 — Categorize the benefits
- Step 2 — Defined contribution plans
- Step 3 — Compensated absences (PTO / vacation)
- Step 4 — Short-term benefits (health, insurance, etc.)
- Step 5 — Defined benefit plans (structure; actuary required)
- Step 6 — Vesting and forfeitures
- Step 7 — Reconciliation and disclosure
- Step 8 — Output
- Step 9 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with
plain-language wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence
tool added.

**Never drop a task because no tool covers it.** A `[manual]` task is a task with a *named gap*,
not an absence — and in this skill the actuarial gap is a feature of the domain, not a shortcoming
of the workspace.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding)

Pull the `[auto]` / `[gated]` reads. **Batch independent reads into one message** — the benefit
expense ledger, the liability accounts, the remittance payments and the employee list do not
depend on each other. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`search_accounts`* — to locate the retirement payable, PTO accrual, benefit expense and
  insurance accounts — usually **[auto]**
- *`get_general_ledger`* on each of those accounts — cost and liability movement, the raw material
  for every roll-forward — usually **[auto]**
- *`get_trial_balance`* / *`get_balance_sheet`* — the liability balances carried — usually
  **[auto]**
- *`get_profit_and_loss`* with a monthly breakdown — benefit cost trend — usually **[auto]**
- *`search_bill_payments`* / *`search_purchases`* — **remittances to the plan provider and the
  insurer**, which is how you test whether withheld money actually left — usually **[auto]**
- *`search_bills`* — insurer and provider invoices — usually **[auto]**
- *`search_vendors`* / *`get-vendor`* — the plan administrator and insurer as vendors — usually
  **[auto]**
- *`search_employees`* / *`get_employee`* — the employee population — usually **[auto]**
- *`search_journal_entries`* — prior accruals and true-ups — usually **[auto]**
- *`get_company_info`* — year-end and base currency — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — it cannot support a booked accrual, a
disclosure figure, or a statement that contributions were remitted on time.

## Step 1 — Categorize the benefits

Benefits fall into categories with different accounting. Getting the category wrong changes
everything downstream, so do this first.

- **Defined contribution (DC) retirement plans** (e.g. 401(k)-type, where the employer contributes
  a defined amount): **simple — expense the employer contribution as earned.** The employer's
  promise ends once the money is paid in; what it grows into is the employee's risk.
- **Defined benefit (DB) plans / pensions** (employer promises a defined future benefit):
  **complex — actuarial accounting (ASC 715 / IAS 19).** Here the employer carries the risk, so
  the obligation must be estimated over decades.
- **Other post-employment benefits (OPEB)** (e.g. retiree health): **also actuarial.**
- **Short-term benefits** (health insurance, current-period benefits): **expense as incurred /
  earned.**
- **Compensated absences (PTO / vacation)**: **accrue as earned if they vest or carry over.**

**Identify which categories apply.** **[gated]**: the chart of accounts and the vendor list give
strong hints (*`search_accounts`*, *`search_vendors`* — a pension administrator or insurer
appearing as a vendor is direct evidence), but the definitive list comes from the user. **A
benefit with no account and no vendor is exactly the one most likely to be unaccrued** — ask
rather than concluding it does not exist.

## Step 2 — Defined contribution plans

The employer's obligation is limited to the contribution. Account simply:

```
DR  Retirement Benefit Expense (employer contribution/match)   $X
    CR  Retirement Contribution Payable                            $X
(then CR Cash when remitted)
```

- **Recognize the employer match / contribution as expense in the period the employee earns it** —
  not when it is paid. **[gated]**: the posted expense is **[auto]**
  (*`get_general_ledger`*), the amount *earned* depends on the plan formula and payroll, which is
  **[manual]** without a payroll connection
- **Employee contributions are withholdings** (they reduce net pay) — handled in
  `payroll-journal-entry-builder`, **not employer expense**. **[auto]** to check for the error:
  if the benefit expense account contains the employee's own money, expense is overstated. This
  is a common and material misposting, and it is directly testable
- **Track unremitted contributions as a liability; remit timely (often a regulatory deadline —
  flag).** **[auto]**, and the strongest compliance contribution in this skill: take the payable
  account's balance and its movement (*`get_general_ledger`*), match it against remittances to the
  plan administrator (*`search_bill_payments`*, *`search_purchases`*), and **report both the
  unremitted balance and how long it has been outstanding**. Withheld employee money held too long
  is a regulatory breach, not merely a late payment
- **Account for any vesting of the employer match** — forfeitures of unvested match reduce expense
  or cost. **[manual]** for the vesting status; see Step 6

## Step 3 — Compensated absences (PTO / vacation)

Accrue a liability for paid time off employees have earned but not yet taken, if the benefit:

- **Vests or accumulates** (carries over), **AND**
- **Is probable and estimable**

```
PTO liability = accrued hours × pay rate (× any payout factor)
DR  PTO/Vacation Expense        $increase in liability
    CR  Accrued PTO Liability       $increase
```

- **Increase the liability as employees earn PTO; decrease as they take it (or are paid out)** —
  **[auto]** for the liability account's movement (*`get_general_ledger`*), **[manual]** for the
  underlying hours
- **Use current pay rates; consider whether unused PTO is paid out on termination** — if
  "use it or lose it" with no payout and no carryover, often **no accrual** is required. This is a
  policy question, **[manual]**, and it decides whether the whole step applies
- **Reassess the balance each period** — **[auto]** to flag a warning sign: a PTO liability that
  never moves is not being reassessed, and one that only ever rises suggests time earned is being
  accrued but time taken is not being released

The hours × rate calculation itself is **[manual]** in an accounting-only workspace. Say so
plainly rather than deriving an accrual from headcount.

## Step 4 — Short-term benefits (health, insurance, etc.)

- **Expense employer-paid premiums / costs in the period of coverage** — **[auto]** for the posted
  cost (*`get_general_ledger`*, *`search_bills`*), **[gated]** to confirm the period of coverage,
  which usually appears on the insurer's invoice rather than in a structured field
- **Accrue for incurred-but-unpaid amounts at period-end** — e.g. a **self-insured** plan's
  **incurred-but-not-reported (IBNR)** claims: medical costs employees have already run up that
  nobody has billed yet. **[manual]** — this is an estimate, sometimes actuarial. **[auto]** to
  detect the risk: invoices arriving after period end for pre-period coverage
  (*`search_bills`* over the subsequent window)
- **Employee contributions to premiums are withholdings** (in `payroll-journal-entry-builder`) —
  same testable misposting as in Step 2

## Step 5 — Defined benefit plans (structure; actuary required)

DB accounting (ASC 715 / IAS 19) requires an **actuarial valuation** — a specialist's calculation
of what the promise will cost, using assumptions about lifespans, salary growth, and discount
rates. The skill structures the components; **the obligation and cost come from an actuary**.

**Key components** — **[manual]**, every one:

- **Projected / Defined Benefit Obligation (PBO / DBO)**: the present value of promised benefits
  — what the future promise is worth in today's money (actuarial)
- **Plan assets**: the fair value of assets set aside to fund the obligation
- **Funded status**: plan assets − obligation. A net asset or liability on the balance sheet —
  positive means the plan is overfunded, negative means underfunded
- **Net periodic benefit cost**: service cost + interest cost − expected return on assets +/−
  amortization of prior service cost and actuarial gains/losses (US GAAP); under IAS 19, service
  cost + net interest on the net liability, with **remeasurements** to **OCI** (other
  comprehensive income — gains and losses recorded in equity rather than through profit)

**Treatment of gains / losses**:

- **IAS 19**: remeasurements (actuarial gains / losses, return on assets versus interest) → **OCI,
  not reclassified** — they never pass back through profit
- **US GAAP**: actuarial gains / losses may be **deferred and amortized** (the **corridor** method
  or another); **service cost in operating**, other components elsewhere

Record the net benefit cost (operating portion and OCI portion) and the balance-sheet funded
status. **This requires the actuarial report — flag that an actuary must provide the obligation,
asset values, and assumptions. Do not fabricate actuarial figures.**

**[auto]** only for what the ledger already carries: the pension liability or asset balance as
posted, the movement on it, and contributions actually paid into the plan
(*`get_general_ledger`*, *`search_bill_payments`*). These **tie to** the actuary's numbers; they
do not replace them. If no actuarial report is available, **produce the structure with the cells
empty and named**, and list every empty cell in Sheet 8. An empty schedule that says what it needs
is a useful deliverable; a filled one built on estimates is not.

## Step 6 — Vesting and forfeitures

For employer contributions / benefits subject to **vesting** — the point at which the employee's
entitlement becomes unconditional:

- **Recognize cost considering vesting where appropriate** — **[manual]**
- **Forfeitures of unvested employer contributions** (when employees leave before vesting)
  **reduce employer cost or are used to offset future contributions per the plan** — **[manual]**
  for the forfeiture amount; **[auto]** to spot the trigger, since leavers show up as employees
  becoming inactive (*`search_employees`* with active status) and as a fall in payroll activity

## Step 7 — Reconciliation and disclosure

- **Reconcile benefit liability roll-forwards** (DC payable, PTO accrual, DB funded status) —
  **[auto]** for the ledger side of each (*`get_general_ledger`*, *`get_trial_balance`*):
  opening + cost accrued − payments = closing
- **Confirm contributions remitted tie to amounts withheld + the employer portion** (coordinate
  with `payroll-reconciliation`) — **[gated]**: remittances out are **[auto]**
  (*`search_bill_payments`*), amounts withheld are **[manual]** without a payroll connection. Where
  both exist, this is a genuine two-sided check and should be performed
- **Disclosure figures for `notes-to-financial-statements`**:
  - **DC**: cost recognized — **[auto]** where the expense account is clean
  - **DB**: obligation and asset roll-forwards, funded status, assumptions, net periodic cost
    components, expected future contributions / benefit payments — **[manual]**, from the actuary
  - **PTO**: accounting policy and liability — policy **[manual]**, liability **[auto]**

## Step 8 — Output

Deliver an `.xlsx` workpaper. Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**Sheet 1: Benefit Cost Summary**

Cost by benefit type and period; liabilities by type. Add a header block: workspace name; each
in-scope company file by `display_name`; each excluded one and why; whether any figure rests on
`mock` data.

**Sheet 2: Defined Contribution**

Contributions / match by period, vesting, payable roll-forward. **Add:** the unremitted balance
and its age, against the deadline confirmed at Gate 3.

**Sheet 3: Compensated Absences (PTO)**

Accrued hours × rate, liability roll-forward, by employee or group.

**Sheet 4: Short-Term Benefits**

Premiums / costs, accruals for incurred-but-unpaid.

**Sheet 5: Defined Benefit (if applicable)**

Funded status, net periodic cost components, OCI, roll-forwards — **populated from the actuarial
report**. Where no report exists, present the structure with cells explicitly marked "awaiting
actuarial valuation".

**Sheet 6: Journal Entries**

For each benefit type, marked clearly as **proposals**.

**Sheet 7: Disclosures**

Disclosure-ready figures by benefit type.

**Sheet 8: Open Items / Actuary Required**

DB / OPEB items needing actuarial input. **Add:** every other `[manual]` gap with its owner —
plan terms not supplied, PTO balances missing, IBNR estimate outstanding.

**Sheet 9: Coverage — NEW, Mosofin-specific**

| Task | Benefit type | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used | Policy (enabled / permission / disabled) | `mock` | Gap — what could not be verified and what the user must supply |

Every DB and OPEB row reads `manual` with the gap "actuarial valuation required". That is the
correct, expected entry.

In a multi-entity run this sheet is **per entity**.

**File naming:** `Benefits_Accounting_[YYYY]_[EntityName].xlsx`

In a multi-entity run, `[EntityName]` is the company file's `display_name`, one per entity plus a
combined view. Every file states which datasource and `display_name` it covers.

**Grounding:** every figure traces to a tool result in this conversation or to labelled
user-supplied evidence. End with a single **Data sources** line grouping calls by datasource.
Where the data does not cover something, **name the tool that would have covered it** — or state
that none exists, as with actuarial figures — instead of estimating.

## Step 9 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them,
ask — explicitly, at that point, not earlier — whether to save this as their own customized
version. A general "yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The benefit inventory** — which of the five categories this entity actually has
- **Plan terms**: contribution formula, employer match, eligibility, and the **vesting schedule** —
  the highest-value items to carry forward, since they are stable, never in the ledger, and
  otherwise re-asked every period
- **The PTO policy**: accrual rate, carryover, payout-on-termination, and therefore whether an
  accrual is required at all
- **The account mapping**: which real accounts hold each benefit's expense and liability
- **The remittance deadline** applicable to withheld contributions, and the plan administrator's
  identity as a vendor
- **The reporting framework** and, for DB, the elected treatment of actuarial gains and losses
- **The actuary's identity and reporting cadence**, so the next run knows who to chase and when
- Whether the health plan is insured or **self-insured**, and how IBNR is estimated
- The replay recipe: the exact sequence of reads that produced this period's schedules

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference
files; set `datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write
preference files alongside the installed skill.

**Do not persist employee names, individual PTO balances, pay rates, contribution amounts, or any
actuarial report contents.** These are personal data about identifiable people and, for health
benefits, may be special-category data. Persist the *policy and the plan design*, never the
per-employee record.

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks /
Northbrook Trading — 4% employer match, 3-year cliff vesting, PTO carries over and is paid out" —
not "4% match". Entities within one group frequently offer different benefits, and an unlabelled
plan term applied to the wrong company file accrues a cost that does not exist there. Record the
chosen **scenario** (single vs multi, and which set) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to
the workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is
the workspace's.**

On later runs, match stored entity names against Gate 1's live list. An entity in preferences
that is no longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One benefit schedule, one set
of liabilities, one disclosure pack.

**Multi-entity.** Steps 0–8 run **once per entity**, each call targeting exactly one
`data_source_id`, every cost, liability and accrual carrying that entity's `display_name`. Then
one cross-entity step:

- **A roll-up of benefit cost and liability by entity.** Costs aggregate meaningfully for group
  reporting, but **each entity bears its own** — never present a group total without the per-entity
  breakdown beneath it.
- **One plan, several participating employers** is the common structure and the subtle one. A
  single retirement plan may cover employees of three entities; the *plan* is one thing, the
  *accounting* is per employer. Allocate contributions to the entity that employs each person, and
  say how the allocation was made. If the plan is a genuine **multiemployer plan**, different
  accounting and disclosure apply entirely — see the edge case.
- **A DB plan spanning entities** cannot be split without the actuary's help. The funded status is
  measured at plan level; ask the actuary for the per-employer allocation rather than apportioning
  by headcount.
- **Employees transferring between entities** carry accrued PTO with them. The liability should
  move too; check that one entity released what the other took on, or the group's total PTO
  liability is wrong in both directions.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict per
company file.
