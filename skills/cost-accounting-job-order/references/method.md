<!-- cost-accounting-job-order · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding)
- Step 0b — The untagged-posting test (Mosofin addition)
- Step 1 — Define job cost structure
- Step 2 — Establish overhead pools and rates
- Step 3 — Accumulate actual costs by job
- Step 4 — Apply overhead
- Step 5 — WIP schedule and rollforward
- Step 6 — Under / over applied overhead treatment
- Step 7 — Reporting and controls
- Step 8 — Evolve the skill (Mosofin-specific, final step)
- Outputs
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with
plain-language wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool
added.

**Never drop a task because no tool covers it.** A `[manual]` task is a task with a *named gap*, not an
absence.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding)

Pull the `[auto]` / `[gated]` reads. **Batch independent reads into one message** — the job dimensions,
the cost ledger, the time activities and the overhead accounts do not depend on each other. Never
serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`search_classes`* / *`search_departments`* / *`search_customers`* — **the job codes** — usually
  **[auto]**
- *`get_profit_and_loss`* filtered by job dimension — **cost and revenue per job** — usually **[auto]**
- *`get_general_ledger`* on the cost and overhead accounts — **all direct-cost postings, with and
  without a job tag** — usually **[auto]**
- *`search_bills`* / *`search_purchases`* — materials, subcontractors and other direct costs by job —
  usually **[auto]**
- *`search_time_activities`* — **labour hours by job** — usually **[auto]**
- *`search_purchase_orders`* — committed but unincurred job cost — usually **[auto]**
- *`search_accounts`* — the WIP, applied-overhead and variance accounts, and the overhead pool accounts
  — usually **[auto]**
- *`get_balance_sheet`* / *`get_trial_balance`* — the WIP balance carried — usually **[auto]**
- *`search_budgets`* — budgeted overhead and base, for a predetermined rate — usually **[auto]**
- *`search_invoices`* — job billings, for margin reporting — usually **[auto]**
- *`search_employees`* — the labour population — usually **[auto]**
- *`get_company_info`* — currency and calendar — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — a job margin computed on it would drive real
pricing and bidding decisions.

## Step 0b — The untagged-posting test (Mosofin addition)

**Run this before Step 1.** It is the original's first quality check, promoted to a step because
everything downstream depends on it.

**[auto]**: read every posting to the direct-cost accounts over the period (*`get_general_ledger`*,
*`search_bills`*, *`search_purchases`*, *`search_time_activities`*) and **split them by whether they
carry a job tag.**

Report:

- **Total direct cost posted**
- **Total carrying a job tag** — the population this skill can work with
- **Total with no job tag** — and **this figure is the size of the error in every job margin**, because
  those costs belong to jobs and are sitting in none of them
- **The untagged postings themselves**, by account and vendor, so they can be corrected

**If the untagged proportion is material, say so before presenting any job margin.** A job costing
report built on 80% of the costs is not 80% right — the missing 20% is concentrated on whichever jobs
happened to be posted carelessly, so individual job margins may be wildly wrong even though the total
is only slightly off.

If no job dimension is in use at all, **stop here and say the books cannot support job costing yet**.
Recommending the tagging change is the single highest-value output available in that case.

## Step 1 — Define job cost structure

Define cost buckets — **[gated]**: the accounts exist and are readable, mapping them to buckets is a
decision:

- **Direct materials**
- **Direct labor**
- **Subcontractors**
- **Equipment**
- **Applied overhead**
- **Other direct costs** (travel, permits, freight)

**Define job dimensions (job, phase, cost code, location) to support reporting.** **[auto]** to see which
of these already exist as dimensions (*`search_classes`*, *`search_departments`*), and worth reporting:
most workspaces have a job level but no **phase** or **cost code** level, which is why cost overruns get
noticed at the job level rather than where they happened.

## Step 2 — Establish overhead pools and rates

**1. Choose overhead pool(s)**: factory overhead, field overhead, indirect labor, occupancy,
depreciation. **[gated]** — the accounts are **[auto]**, the selection is **[manual]**. **List the pool's
contents account by account** so the second quality check can actually be performed.

**2. Select allocation base:**

- **Labor hours** (common in services / field work) — **[auto]** where time is tracked
- **Labor dollars** — **[gated]**: hours **[auto]**, rates **[manual]**
- **Machine hours** (manufacturing) — **[manual]**
- **Direct cost %** (sometimes used in construction but **less precise**) — **[auto]**

**3. Determine overhead rate:**

```
Predetermined rate = Budgeted overhead / Budgeted base
```

**[gated]**: budgets held in the system are **[auto]** (*`search_budgets`*), otherwise **[manual]**.
**[auto]** and worth offering alongside: the **actual** overhead-to-base ratio for the last complete
year, computed from the ledger. That is not the predetermined rate — the whole point of a predetermined
rate is that it is set in advance — but it is the best available sanity check on whether the budgeted
rate is realistic.

**Document assumptions and frequency (annual rate, quarterly refresh, or rolling 12 months).**

## Step 3 — Accumulate actual costs by job

- **Attribute direct materials issues to the job, in the cost sheet** — **[gated]**: purchases coded to a job are **[auto]**; a true
  *issue* from stock needs an inventory system
- **Attribute direct labor to the job, in the cost sheet (including burden if applicable)** — **[gated]**: hours **[auto]**, rates
  and burden **[manual]**
- **Attribute subcontractor invoices to the job, in the cost sheet** — **[auto]** (*`search_bills`* with the job dimension)
- **Ensure mapping from source systems (payroll, procurement, inventory) is consistent** — **[gated]**:
  where those systems are connected, the mapping is checkable; where they are not, it is **[manual]**

Mosofin **reads** these postings; it does not make them. Where a cost is missing from a job, the fix
happens in the source system.

## Step 4 — Apply overhead

For each job period:

```
Applied overhead = Overhead rate × actual base for the job
```

**[auto]** once the rate is set and the base is measurable.

**Track:**

- **Applied overhead by job** — **[auto]**
- **Actual overhead incurred in the pool** — **[auto]** (*`get_general_ledger`* on the pool accounts)
- **Under / over applied overhead** — **[auto]**, the difference between the two

Having both sides readable is what makes Step 6 a measurement rather than an estimate.

## Step 5 — WIP schedule and rollforward

Build a WIP rollforward **per job** — **[auto]** where the WIP account carries the job dimension:

```
Beginning WIP
+ Current period costs (DM, DL, OH, subs)
- Costs relieved to COGS (upon shipment/completion/recognition)
= Ending WIP
```

**If percent-of-completion is used, coordinate with percentage-of-completion accounting for revenue
recognition and cost-to-complete.**

Two `[auto]` checks worth running here:

- **The sum of per-job WIP must equal the WIP account balance** (*`get_trial_balance`*). A difference
  means costs are in WIP without a job tag — the Step 0b problem, surfacing on the balance sheet.
- **WIP by job age**, which feeds the WIP aging in Step 7.

## Step 6 — Under / over applied overhead treatment

At period end — **[auto]** to compute, **[manual]** to choose the treatment:

- **Under-applied overhead**: actual > applied (debit variance) — you charged jobs less overhead than
  you actually incurred
- **Over-applied overhead**: applied > actual (credit variance)

Typical close entry (simplified). `DR` is a debit, `CR` a credit. **Mosofin does not post** — these are
proposals:

```
If under-applied:
DR Cost of Goods Sold (or variance acct)    XXX
    CR Applied Overhead                        XXX

If over-applied:
DR Applied Overhead                          XXX
    CR Cost of Goods Sold (or variance acct)    XXX
```

**Policy choices** — **[manual]**:

- **Close all to COGS** (common for immaterial amounts)
- **Prorate to WIP / FG / COGS** (for material manufacturing environments)

**[auto]** to inform the choice: compute the variance as a percentage of total overhead. A variance that
is a few percent supports closing to COGS; one that is large distorts inventory values and argues for
proration — and it also suggests the rate itself needs revisiting, which is the fourth quality check.

## Step 7 — Reporting and controls

Outputs to produce:

- **Job cost report** (cost by bucket, by phase) — **[auto]** where the dimensions exist
- **Job margin and variance vs estimate** — **[gated]**: actual cost and billings are **[auto]**;
  **the estimate is [manual]**, and without it there is a margin but no variance
- **WIP aging (old / inactive jobs)** — **[auto]**, and one of the most useful findings: a job with WIP
  and no activity for months is either finished-but-unrelieved or abandoned, and both are real problems
- **Cutoff tests (late invoices, unrecorded costs)** — **[auto]**: bills received after period end for
  work done before it (*`search_bills`* over the subsequent window), and open purchase orders on jobs
  with no matching cost

## Step 8 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The job-tagging convention** — which dimension is the job code, and whether phase and cost code
  exist. The thing that makes every future period automatic
- **The cost-bucket map**: which accounts belong to direct materials, direct labour, subcontractors,
  equipment and other direct costs
- **The overhead pool composition** — account by account, and the accounts deliberately excluded
- **The allocation base** and the rate-setting frequency
- **The under / over-applied treatment policy** and the materiality threshold that triggers proration
- **The WIP capitalisation and relief policy**
- **Labour rates or burden factors**, if the user supplies them and is content for them to persist —
  **not individual employees' pay**
- The replay recipe: the exact sequence of reads that produced costs and hours by job

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Do not persist job margins, customer names with job values, individual pay rates, or the overhead
rate's numeric value.** Job margins are commercially sensitive — they are the basis of pricing and
bidding — and individual pay is personal data. **Persist the method; re-derive the rate.**

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / Northwood
Fabrication — jobs tagged by Class, phases by Department; pool = accounts 6100–6180; base = labour hours;
rate reset annually" — not "base = labour hours". Overhead pools and rates are entity-specific, and an
unlabelled rate applied to another company file allocates costs that entity never incurred. Record the
chosen **scenario** (single vs multi, and which set) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's** — and the overhead rate, the WIP balance and the untagged-cost figure are all state.

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Outputs

- **Job cost ledger model.** Cost by bucket, by job, by phase where it exists — **with the untagged
  total shown alongside**, so the reader knows what the model does not cover.
- **Overhead rate and pool documentation.** The pool listed **account by account**, the base, the rate,
  its derivation and its effective period.
- **WIP rollforward by job.** Reconciled to the WIP account balance, with any difference explained.
- **Under / over applied overhead calculation and JE recommendation.** Marked as a **proposal**, with the
  variance as a percentage of total overhead and the treatment policy applied.
- **Job profitability dashboard definitions.** Including which measures are `[auto]` and which depend on
  supplied estimates or rates.

**Untagged-cost report — NEW, Mosofin-specific.**

| Account | Vendor / source | Amount | Date | Why it matters (which jobs may be understated) |

**Coverage sheet — NEW, Mosofin-specific.**

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used | Policy | `mock` | Gap — what could not be evidenced and who supplied it |

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming — Mosofin addition** (the original left it unstated, and multi-entity output needs it):
`Job_Costing_[YYYY-MM]_[EntityName].xlsx`, where `[EntityName]` is the company file's `display_name`.
Every file states which datasource and `display_name` it covers, and the job dimension used.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where the data does not
cover something, **name the tool that would have covered it** instead of estimating.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One pool, one rate, one WIP
schedule.

**Multi-entity.** Steps 0–7 run **once per entity**, each call targeting exactly one `data_source_id`,
every job carrying its entity's `display_name`. Then:

- **Overhead pools and rates are per entity.** Each entity incurs its own indirect costs and has its own
  base. **A rate derived from one entity's pool and applied to another's jobs allocates costs that
  entity never incurred** — it moves profit between legal entities, with tax consequences.
- **A job delivered across entities** — one entity supplying labour to another's job — creates an
  intercompany charge, and the margin on it is unrealised at group level. Flag the pair for
  `consolidation-and-eliminations`, and see percentage-of-completion accounting for the contract
  side.
- **Job codes are usually entity-local.** The same physical job may carry different codes at each
  entity; map them explicitly before combining.
- **The untagged-posting test runs per entity**, since tagging discipline commonly differs sharply
  between a well-run parent and a recently acquired subsidiary — and that comparison is itself a useful
  finding.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict per company
file.
