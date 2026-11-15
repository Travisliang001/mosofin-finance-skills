<!-- pensions-and-postretirement-asc715 · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding) — Mosofin addition
- Step 0b — Compare what was recorded to what the actuary said (Mosofin addition)
- Step 1 — Identify plan type and components
- Step 2 — Rollforward obligations and plan assets
- Step 3 — Determine funded status
- Step 4 — Determine net periodic benefit cost
- Step 5 — Journal entries
- Step 6 — Disclosures
- Step 7 — Output (Mosofin addition)
- Step 8 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Never drop a task because no tool covers it.** Almost everything here is legitimately actuarial, and
saying so is the honest result.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding) — Mosofin addition

**Batch independent reads into one message** — the accounts, the balances, the contributions and the expense
do not depend on each other. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical batch, per in-scope entity:

- *`search_accounts`* — **the pension liability or asset, pension expense, compensation expense and the
  AOCI pension component** — usually **[auto]**
- *`get_balance_sheet`* / *`get_trial_balance`* at both period ends — **the recorded position** — usually
  **[auto]**
- *`get_general_ledger`* on **the pension liability and AOCI accounts** — **the movements, and the annual
  entry itself** — usually **[auto]**
- *`search_payments`* / *`search_checks`* — **employer contributions paid to the plan or trustee** — usually
  **[auto]**
- *`get_profit_and_loss`* — **pension expense recognised** — usually **[auto]**
- *`search_journal_entries`* — **the pension entry, which is almost always a manual annual journal** —
  usually **[auto]**
- *`search_employees`* — headcount, as context — usually **[auto]**
- *`get_company_info`* — legal name, currency, **year-end** — usually **[auto]**

**Pull several prior years.** **Pension entries are annual**, so a single year shows nothing about whether
the treatment has been consistent.

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — **the net pension liability is frequently one of
the largest figures on a sponsor's balance sheet**, and it is disclosed extensively.

## Step 0b — Compare what was recorded to what the actuary said (Mosofin addition)

**Run as soon as the report is available**, before building the entries — **because if last year's entry was
wrong, this year's roll-forward starts from the wrong place.**

**[gated]**: **the recorded side is `[auto]`; the report side is `[manual]`.** Three comparisons:

| Check | Recorded (`[auto]`) | Per report (`[manual]`) |
|---|---|---|
| **Balance sheet position** | the pension liability or asset | **the funded status** |
| **Income statement** | pension and compensation expense | **the net periodic benefit cost** |
| **Equity** | the AOCI pension component and its movement | **the remeasurement and amortisation** |

**All three should agree.** **Where they do not, the difference is either an entry that was never posted, a
prior-year error carried forward, or a report the entity never acted on** — and **all three are common**,
because a pension entry is made once a year by someone reading a long document.

**Also `[auto]`: was an entry posted at all this year?** **A sponsor with a defined benefit plan and no
pension journal in the period has not accounted for it** — the simplest and most consequential finding
available here.

## Step 1 — Identify plan type and components

**Key components typically include** — **[manual]**, all from the report:

- **Service cost**
- **Interest cost**
- **Expected return on plan assets (GAAP) / net interest (IFRS)**
- **Amortization of prior service cost**
- **Amortization of actuarial gains / losses** — corridor approach in some GAAP contexts
- **Settlements / curtailments** (if applicable)

**Note the third component names the framework difference explicitly**, and it matters: **ASC 715 uses an
expected return on plan assets, while IAS 19 uses net interest on the net liability at the discount rate.**
**The two produce different expense figures from identical facts**, and **which applies is the framework, not
a choice.** See `gaap-vs-ifrs-conversion`, where this appears as a conversion difference.

**[auto]** contribution: **whether the expense accounts separate these components** is readable, and **a
single "pension expense" line makes the disclosure in Step 6 impossible to produce from the ledger.** Worth
knowing before the disclosure is due.

## Step 2 — Rollforward obligations and plan assets

**From the actuarial report** — **[manual]** except where noted:

```
- Beginning PBO/APBO
+ Service cost
+ Interest cost
+/- Actuarial gains/losses
+ Plan amendments
- Benefits paid
= Ending PBO/APBO
```

**Plan assets rollforward:**

```
- Beginning fair value
+ Actual return
+ Employer contributions
- Benefits paid
= Ending fair value
```

**One line in each is not the actuary's.**

**Employer contributions are `[auto]`** — **payments to the plan or trustee, by payee and date.** **Compare
them to the report's figure.** **A difference means either a contribution the actuary did not know about —
common where a payment was made close to the measurement date — or a payment recorded as a contribution that
was something else.** **Either way it changes the closing plan asset value and therefore the funded
status.**

**Benefits paid are `[manual]`** — they leave the plan, not the employer, and **the ledger sees nothing.**

## Step 3 — Determine funded status

**Funded status = Fair value of plan assets − Benefit obligation.**

**Record as net pension asset / liability on balance sheet.**

**[manual]** on both terms — **plan assets need a fair value, the obligation needs the actuary** — **and
`[auto]` on the recorded result.** **The comparison is Step 0b's first check.**

**Note that the funded status goes on the balance sheet in full.** **Where the plan is in surplus there may
be a ceiling on the asset recognised** — an asset ceiling test under IAS 19, and specific conditions under
ASC 715. **`[manual]`, and easy to miss** where a plan has moved into surplus for the first time.

## Step 4 — Determine net periodic benefit cost

**Break into** — **[manual]**:

- **Amounts in earnings** — **service cost + other components per policy**
- **Amounts in OCI** — **remeasurements, actuarial changes, prior service cost adjustments**

**The split is the substance of modern pension accounting**, and it is worth stating why: **service cost is
an operating cost of employing people this year; the remeasurements are the consequence of assumptions
changing, which says nothing about this year's operations.** **Putting the second through profit would make
reported results move with bond yields.**

**[auto]** check: **the split as recorded.** **Where everything went through profit and nothing through
OCI** — or the reverse — **the entry does not follow the framework**, and that is visible without the
report.

**Note also the presentation requirement**: under both frameworks **service cost sits with other
compensation cost, while the remaining components are presented separately, outside operating profit** in
many presentations. **[auto]** to check whether the expense accounts allow it.

## Step 5 — Journal entries

**Typical approach — simplified; account names vary.** `DR` is a debit, `CR` a credit. **Mosofin does not
post** — these are proposals:

**Record net periodic benefit cost and liabilities:**
```
DR Compensation Expense (service cost)     XXX
DR Pension Expense (other components)      XXX
    CR Pension Liability / Accrued Benefit     XXX
```

**Record OCI components (from actuarial changes):**
```
DR/CR OCI - Pension (AOCI)             XXX
    CR/DR Pension Liability                XXX
```

**Record employer contributions:**
```
DR Pension Liability                   XXX
    CR Cash                                 XXX
```

Use the **real account names from the connected chart** (*`search_accounts`*, **[auto]**).

**Note the third entry may already be posted.** **[auto]**: contributions are cash transactions and are
usually recorded when paid. **Check before proposing it** — **proposing an entry that already exists would
double the liability reduction.**

**And note what the three entries do together**: **the liability moves to the funded status, the cost splits
between profit and OCI, and the cash reduces the liability.** **If the closing liability does not equal the
funded status after all three, something is wrong** — which is Step 0b's first check, run forward.

## Step 6 — Disclosures

**Prepare disclosure-ready tables** — **[gated]**:

- **Assumptions** — **[manual]**; from the report, **and disclosed with sensitivity in many frameworks**
- **Rollforwards** — **[manual]** except the contribution line
- **Components of cost** — **[gated]**; **`[auto]` where the accounts separate them**
- **Expected contributions** — **[manual]**; forward-looking
- **Benefit payment forecasts** — **[manual]**; actuarial projection

**Pension disclosure is among the most extensive in a set of accounts**, and **almost all of it is
actuarial.** **[auto]** contribution is limited to the recorded amounts and the contribution history — which
is worth supplying, because **the disclosed contribution figure should agree to the cash**, and it is a
check nobody runs.

## Step 7 — Output (Mosofin addition)

The original names deliverables but does not specify a workpaper. Produce one.

Deliver an `.xlsx` workpaper, plus the memo:

**Document: Period-End Pension Accounting Memo** — the plan, the framework, the report relied on with its
date and author, the components, the conclusion, and **the open items**.

**Sheet 1: Recorded vs. Actuarial — NEW, Mosofin-specific** — the three Step 0b comparisons, with
differences and explanations. **Lead with this sheet**; it frames everything else.

**Sheet 2: Obligation Roll-Forward** — the PBO/APBO lines, **each marked as from the report**.

**Sheet 3: Plan Asset Roll-Forward** — **with the employer contribution line marked `[auto]` and compared
to the report's figure**.

**Sheet 4: Funded Status** — plan assets less obligation, against the recorded balance sheet position, **with
any asset ceiling noted**.

**Sheet 5: Net Periodic Benefit Cost** — the components, split between earnings and OCI, **against the
recorded split**.

**Sheet 6: AOCI Roll-Forward** — opening, remeasurement, amortisation, closing, **tied to the AOCI account**.

**Sheet 7: Journal Entries** — the three entries, marked as **proposals**, **with any already posted
identified**.

**Sheet 8: Disclosure Tables** — assumptions, rollforwards, components, expected contributions, benefit
payment forecasts.

**Sheet 9: Controls Checklist** — **the original's named deliverable**: actuarial report completeness,
mapping, review — **plus whether an entry was posted at all, and whether the measurement date matches the
reporting date**.

**Sheet 10: Coverage — NEW, Mosofin-specific**

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used / external source | As-at date | `mock` | Gap |

**Nearly every row reads `manual`, sourced to the actuarial report.** **That is the correct result for this
skill**, and the sheet exists so the few `[auto]` checks are not mistaken for broader coverage.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.
Offer a Word document only where the host can make one; otherwise give the text in the chat.

**File naming (Mosofin addition — the original specifies none):**
`Pension_Accounting_[YYYY]_[EntityName].xlsx`

Every file states which datasource and `display_name` it covers, **and the actuarial report relied on**.

**Grounding:** every recorded figure traces to a tool result in this conversation; **every actuarial figure
traces to the report, by page or table reference.** End with a single **Data sources** line. **No actuarial
figure is ever estimated.**

## Step 8 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The plan details** — type, sponsor, participants covered, whether open or closed to new entrants
- **The framework** — ASC 715 or IAS 19 — **and the expected-return versus net-interest treatment that
  follows**
- **The account map**: pension liability or asset, service cost, other components, AOCI pension component
- **The actuary and the valuation cadence**, and the measurement date convention
- **The amortisation policy** — corridor or immediate, and the basis
- **The presentation policy** — where service cost and the other components sit in the income statement
- **The contribution schedule** and who authorises it
- **The entity that sponsors the plan**, where a group is involved
- The replay recipe: the exact sequence of reads that produced the recorded position

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist actuarial figures, assumptions, obligations, plan asset values or funded status.** All state
— **and an assumption reused from a prior year is the specific failure this area is prone to**, since
discount rates move materially year to year and everything scales off them. **And never persist participant
data** — plan membership is personal data about identifiable people, including former employees.

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / Northbrook
Manufacturing Ltd — sponsor, IAS 19, closed DB plan, net interest basis, liability 2600, AOCI 3300,
actuary valuation each 31 December" — not "IAS 19, closed DB plan". **The sponsoring entity carries the
obligation**, and applying one entity's plan details to another puts a liability in the wrong company.
Record the chosen **scenario** (single vs multi, and the sponsor) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's.**

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** One sponsor, one plan, one set of entries.

**Multi-entity.** **Group plans are common, and the accounting is not obvious:**

- **Establish which entity is the accounting sponsor.** **The entity that carries the obligation is not
  always the one whose employees are in the plan.** **The sponsor recognises the funded status; the
  participating entities may recognise only their contributions.**
- **Multi-employer and group plans have specific treatments.** Where several entities participate in one
  plan and **the assets and obligations cannot be attributed to individual entities**, participants may
  account for it as a defined contribution plan in their own accounts while the sponsor accounts for the
  whole. **`[manual]`, from the plan documentation** — and getting it wrong misstates both sets of accounts.
- **Contributions may be paid by one entity for several.** **[auto]** to read; **the allocation is
  `[manual]`**, and **an unallocated payment creates an intercompany balance** — see
  `intercompany-reconciliation`.
- **The obligation stays with the sponsor on consolidation**, and **intra-group recharges of pension cost
  eliminate** — see `consolidation-and-eliminations`.
- **Currency**: a plan denominated in a currency other than the sponsor's functional currency introduces
  translation on a large, long-dated liability — see `foreign-currency-translation-asc830`.
- **Run the recorded-versus-actuarial check on the sponsor**, and **check the participating entities recorded
  only what they should have.**

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict per company
file.
