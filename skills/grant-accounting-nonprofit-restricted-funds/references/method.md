<!-- grant-accounting-nonprofit-restricted-funds · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding) — Mosofin addition
- Step 1 — Classify funding
- Step 2 — Set up fund / grant tracking structure
- Step 3 — Recognize revenue and restrictions
- Step 4 — Track allowable costs and compliance
- Step 5 — Journal entries (examples)
- Step 6 — Output (Mosofin addition)
- Step 7 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Never drop a task because no tool covers it.** The agreements and the allowability rules are legitimately
`[manual]`.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding) — Mosofin addition

**Batch independent reads into one message** — the dimensions, the accounts, the spend and the receipts do
not depend on each other. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`search_classes`* / *`search_departments`* / *`search_locations`* — **the fund, program and grant
  dimensions** — usually **[auto]**
- *`search_accounts`* — the chart of accounts, including **net asset, contribution revenue and grants
  receivable accounts** — usually **[auto]**
- *`get_profit_and_loss`* **by class / program and by period** — **grant-tagged expenditure, the core
  data** — usually **[auto]**
- *`get_general_ledger`* — **expenditure detail by grant, and the release entries already posted** — usually
  **[auto]**
- *`get_balance_sheet`* **by class** — **restricted and unrestricted net assets, grants receivable, deferred
  amounts** — usually **[auto]**
- *`search_deposits`* / *`search_payments`* — **cash received by funder** — usually **[auto]**
- *`search_customers`* — **funders are often set up as customers** in a nonprofit ledger — usually
  **[auto]**
- *`search_invoices`* — where grant billings are raised as invoices — usually **[auto]**
- *`get_company_info`* — legal name, **fiscal year end** — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — **grant reports go to funders and to auditors, and
a Single Audit tests them.** Fixture-derived spend in a funder report is a serious matter.

## Step 1 — Classify funding

**Determine** — **[manual]**, all three, and **this step governs everything after it**:

- **Exchange transaction vs. contribution.** Did the funder receive commensurate value in return? **An
  exchange is revenue under the revenue standard** (`revenue-recognition-asc606`); **a contribution is
  not.** Government "grants" are frequently exchange transactions in substance.
- **Conditional vs. unconditional contribution.** **A condition exists where the agreement contains both a
  barrier the entity must overcome and a right of return or release if it does not.** **A conditional
  contribution is not recognised as revenue until the barrier is met** — it sits as a refundable advance if
  cash has been received.
- **With donor restrictions vs. without.** A restriction limits **how or when** the money may be used. **It
  does not prevent recognition** — this is the distinction most often muddled with conditionality.

**Say it plainly, because the confusion is universal: a condition delays *recognition*; a restriction
delays *release*.** A conditional grant produces no revenue yet. A restricted grant produces revenue now,
recorded in restricted net assets, released later.

**[auto]** contribution — a cross-check, not a determination: **cash received with no corresponding revenue,
or revenue with no receivable and no cash**, are both readable, and either can indicate a classification
that was never worked through. **Report the pattern; the classification is the user's.**

## Step 2 — Set up fund / grant tracking structure

- **Create fund / program dimensions** — **[gated]**: **Mosofin cannot create anything.** Read what exists
  and **propose** what is missing.
- **Define grant IDs and reporting categories** — **[manual]** to define, **[auto]** to check against what
  the ledger already carries
- **Establish coding rules for all grant-related activity** — **[manual]**

**Mosofin addition — assess the existing structure before proposing a new one.** **[auto]**:

- **Which dimensions exist, and are they used consistently?** A class used on 60% of transactions is not a
  tracking structure.
- **Do grants map one-to-one onto dimensions, or many-to-many?** **Several grants funding one program is
  the normal case**, and it means a class total is not a grant total. Where the mapping is many-to-many,
  say so — the entity may need a second dimension rather than a rethink of the first.
- **Are restricted and unrestricted net assets separated in the chart?** If not, **the restricted net asset
  rollforward cannot be produced from the ledger**, and that is a structural finding to report before
  anything else.

## Step 3 — Recognize revenue and restrictions

**At award / commitment (if unconditional):**

- **Record contribution receivable and revenue** — **restricted or unrestricted per terms**

**Release from restriction occurs when purpose / time restrictions are met.**

**[gated]**, and **this is where the workspace does its most valuable work.** Once the purpose and the award
are known:

- **Purpose restriction** → **release equals qualifying expenditure incurred**, capped at the award.
  **Qualifying expenditure is `[auto]`** by grant dimension and account. **So the release amount is
  computed from the ledger**, with the underlying transactions as its support — rather than estimated or
  carried forward from last month's spreadsheet.
- **Time restriction** → **release occurs when the period arrives.** **[auto]** on dates.
- **Both** → **released when the later of the two is satisfied.** Compute both and take the later.

**Report the release with its working**: the grant, the qualifying spend in the period, the cumulative
spend, the award, and the resulting release. **A release entry without that working is the single least
supported number in most nonprofit ledgers**, and here it need not be.

**Two `[auto]` checks worth running alongside:**

1. **Cumulative release must never exceed the award.** A running total that has passed the award means
   earlier releases were overstated.
2. **Restricted net assets should equal awards recognised less cumulative releases**, by grant. A difference
   means an entry was missed or double-posted.

## Step 4 — Track allowable costs and compliance

- **Track spend vs. budget by grant category** — **[gated]**: **spend is `[auto]`**, the budget is `[manual]`
  unless the platform holds it
- **Flag unallowable costs** — **[gated]**: **the allowability rules are `[manual]`**, but once stated,
  **testing the ledger against them is `[auto]`** — a rule excluding entertainment, alcohol, lobbying or
  fundraising costs becomes an account-and-description query
- **Maintain supporting documentation for audits** — **[manual]** to hold, **[auto]** to index: every
  transaction's date, vendor, amount and account is readable, which produces the **transaction listing an
  auditor asks for first**

**Mosofin additions — four compliance checks that run as queries:**

1. **Overspend.** Cumulative spend against the award, by grant and by budget category. **Report both the
   overall position and the category positions** — a grant within budget overall can breach a category cap.
2. **Spend outside the grant period.** Transactions dated before the start or after the end date. **A
   common and expensive finding**, and a pure date test.
3. **Untagged spend in grant-funded programs.** Expenditure in a program that a grant funds, carrying no
   grant dimension. Either a coding error or **cost the funder was never billed for.**
4. **Spend with no grant activity for a period.** A live grant with no expenditure for several months —
   either the work stalled, or the costs are going somewhere untagged. **Both matter before a funder
   report.**

## Step 5 — Journal entries (examples)

`DR` is a debit, `CR` a credit. **Mosofin does not post** — these are proposals:

**Record restricted contribution (simplified):**
```
DR Grants Receivable                 XXX
    CR Contribution Revenue - With Donor Restrictions   XXX
```

**Release restriction when spent / earned:**
```
DR Net Assets Released from Restriction    XXX
    CR Net Assets With Donor Restrictions      XXX
```

**(Account names vary by presentation.)**

**Note on the release entry**, since presentation genuinely varies: **the release is a transfer between net
asset classes — restricted net assets decrease and unrestricted net assets increase — and it is presented on
the statement of activities as a reciprocal pair of lines that net to zero in total.** **Confirm the
direction and the account names against this entity's actual presentation** (*`search_accounts`*,
**[auto]**) before proposing the entry, and use the account names the chart actually contains.

## Step 6 — Output (Mosofin addition)

The original lists deliverables but does not specify a workpaper. Produce one.

Deliver an `.xlsx` workpaper:

**Sheet 1: Grant Register** — **terms, restrictions, reporting.** Per grant: funder, award, period,
conditional or unconditional, purpose and time restrictions, reporting deadlines, **and the dimension it
maps to**. Plus the header block: workspace name; the entity by `display_name`; each excluded company file
and why; whether any figure rests on `mock` data.

**Sheet 2: Classification** — per grant: exchange or contribution, conditional or unconditional, restricted
or unrestricted, **with the agreement clause relied on**. **[manual]** throughout, and the source matters.

**Sheet 3: Spend vs. Budget** — by grant and by budget category, period and cumulative, **with variance and
percentage of award spent**.

**Sheet 4: Release from Restriction** — per grant: qualifying spend this period, cumulative, award,
computed release, **with the transaction support behind it**.

**Sheet 5: Restricted Net Assets Roll-Forward** — opening, contributions recognised, releases, closing, by
grant and in total, **reconciled to the net asset accounts in the ledger**.

**Sheet 6: Compliance Exceptions — NEW, Mosofin-specific**

| Grant | Exception | Detail | Amount | Evidence |

The four Step 4 checks — overspend, spend outside period, untagged spend, dormant grants — plus any
unallowable-cost hits against the stated rules.

**Sheet 7: JE Templates and Coding Rules** — the entries and the coding conventions, **using the account
names this chart actually contains**, marked as **proposals**.

**Sheet 8: Audit-Ready Evidence Checklist** — what a funder audit or Single Audit will ask for, what exists,
and who holds it.

**Sheet 9: Reporting Calendar** — deadlines by funder, with owners.

**Sheet 10: Coverage — NEW, Mosofin-specific**

| Task | Grant / entity (`display_name`) | Verdict (auto / gated / manual) | Tool used / external source | As-at date | `mock` | Gap |

Every agreement-derived row reads `manual`. That is the correct entry.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming (Mosofin addition — the original specifies none):**
`Grant_Accounting_[YYYY-MM]_[EntityName].xlsx`

Every file states which datasource and `display_name` it covers.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where the data does not
cover something — the agreements, the conditions, the allowability rules — **name the source required**
instead of estimating.

## Step 7 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The grant-to-dimension mapping** — which class, program or fund carries which grant. **The single most
  valuable stored asset**, and the thing that makes every later period a single run
- **The classification per grant**: exchange or contribution, conditional or unconditional, restricted or
  unrestricted — **with the clause relied on**. These do not change over a grant's life and re-deciding them
  is where inconsistency enters
- **The release basis per grant**: purpose, time, or both, and **which expenditure qualifies**
- **The allowable and unallowable cost rules** per funder, as testable rules
- **The budget categories** and their caps
- **The indirect cost rate basis** — negotiated or de minimis, and how applied. **Not the amounts**
- **The account map**: contribution revenue restricted and unrestricted, net assets by class, grants
  receivable, refundable advance
- **The reporting calendar** — deadlines and owners, by funder
- The replay recipe: the exact sequence of reads that produced grant spend and the release calculation

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist grant balances, spend figures, release amounts or net asset totals** — all state. And
**never persist individual donor names, donation amounts or donor contact details.** Donor information is
confidential, frequently legally protected, and belongs in the entity's own systems rather than in a skill
bundle. **Grant terms from an institutional funder are decisions; an individual's giving history is not
yours to carry.**

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / Northbrook
Community Trust — Foundation A grant on Class 'Youth Programs', unconditional, purpose-restricted, releases
on program salaries and direct costs, 12% de minimis indirect" — not "purpose-restricted". **Grant-to-class
mappings are entity-specific by construction**, and applying one organisation's mapping to another releases
restrictions against the wrong spend. Record the chosen **scenario** (single vs multi) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's.**

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. Grants distinguished by dimension within
one file.

**Multi-entity.** Steps 0–6 run **once per entity**, each call targeting exactly one `data_source_id`, every
grant and balance carrying its entity's `display_name`. Then the points specific to restricted funds:

- **A restriction travels with the money.** **Transferring restricted funds to an affiliate does not release
  the restriction** — it moves a restricted balance. **Never treat an intercompany transfer as a release.**
  This is the most consequential cross-entity error available here.
- **Fiscal sponsorship.** Where one entity holds funds on behalf of another's project, **whether that is the
  sponsor's revenue or an agency transaction depends on whether the sponsor has variance power** — the
  discretion to redirect the funds. **`[manual]`, from the sponsorship agreement**, and it decides whether
  the amount appears in the sponsor's revenue at all.
- **A supporting foundation holding endowment for an operating charity** produces restricted balances in one
  file and the spending in another. **Read both**, and reconcile the release against the spend wherever it
  occurred.
- **Grants awarded to the group but administered by one entity** need the spend gathered across files before
  release can be computed. **Compute release on total qualifying spend**, not on one entity's share.
- **Consolidated statements must not net restricted against unrestricted** across entities. See
  `consolidation-and-eliminations`; the net asset classes stay separate through consolidation.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict per company
file.
