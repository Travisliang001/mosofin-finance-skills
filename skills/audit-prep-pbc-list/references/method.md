<!-- audit-prep-pbc-list · method.md · read for: Stages 3–6 — building and tracking the PBC list. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding)
- Step 1 — Scope the audit areas
- Step 2 — Build the PBC list by area
- Step 3 — Specify what makes each item audit-ready
- Step 4 — Assess readiness and gaps
- Step 5 — Build the tracker and timeline
- Step 6 — Prepare for judgmental areas
- Step 7 — Anticipate adjustments and prior-year items
- Step 8 — Output
- Step 9 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with
plain-language wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence
tool added.

**Never drop a PBC item because no tool covers it.** A `[manual]` item is an item with a *named
gap and a named owner*, not an absence. In this skill that rule is the whole point: an item
quietly dropped from a PBC list is an item the auditor will ask for anyway, on the day, when
there is no time to prepare it.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding)

Pull the `[auto]` / `[gated]` reads. **Batch independent reads into one message** — the trial
balance, the balance sheet, the P&L, the agings and the general ledger do not depend on each
other. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`get_trial_balance`* — the foundational schedule everything else ties to — usually **[auto]**
- *`get_balance_sheet`*, *`get_profit_and_loss`*, *`get_cash_flow`* — the statements being
  audited — usually **[auto]**
- *`get_general_ledger`* — transaction detail behind any balance — usually **[auto]**
- *`get_aged_receivables`* / *`get_aged_payables`* — the subledger agings — policies often
  differ between the two
- *`search_accounts`* — the chart of accounts, to map areas to real account names — usually
  **[auto]**
- *`search_journal_entries`* — manual entries, a standard audit focus — usually **[auto]**
- *`get_company_info`* — industry, year-end, base currency — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that PBC item to **[manual]** and assign an owner.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

**Check the `mock` flag on every result, and treat it as a hard stop for this skill.** Fixture
data can illustrate a tracker's layout, but a schedule built on it must never be handed to an
auditor. Mark any such schedule "illustrative — not audit evidence" on its face.

## Step 1 — Scope the audit areas

Work out what the audit will actually cover, so you prepare for that and not for a generic
checklist.

Map the financial statement areas the audit will cover, **scaled to the entity**. Standard
areas — **[auto]** to test which of these the entity actually has, by inspecting the chart of
accounts and trial balance (*`search_accounts`*, *`get_trial_balance`*):

- Cash and cash equivalents
- Accounts receivable and revenue
- Inventory
- Prepaid and other assets
- Property, plant & equipment
- Intangibles and goodwill
- Accounts payable and accrued liabilities
- Debt and financing
- Leases
- Equity
- Revenue (and recognition)
- Payroll and compensation
- Income taxes
- Related party transactions
- Commitments and contingencies
- Subsequent events

**Prioritize by materiality and risk** — large balances, complex or judgmental areas, and
high-risk areas get more support. **[auto]** for balance size (*`get_trial_balance`*);
**[gated]** for risk, which is a judgment informed by the balance but not determined by it.

Note the asymmetry the books cannot resolve: **leases, commitments and contingencies, and
related parties are often *low* in recorded balance and *high* in audit attention**, precisely
because the risk is that something is missing from the books. Never scope those out on size
alone.

## Step 2 — Build the PBC list by area

For each area, list the schedules and evidence auditors typically request. **Tailor the list to
the entity — don't request inventory support from a services firm.**

**Cash**: bank reconciliations for all accounts — **[gated]**, the ledger side is readable
(*`search_accounts`*, *`get_general_ledger`*) and the statement side is not; **bank statements**
— **[manual]**; **bank confirmations** — **[manual]** and auditor-initiated (see the edge case);
list of accounts — **[auto]**. See `bank-reconciliation`.

**A/R / Revenue**: A/R aging (per `ar-aging-and-collections`) — **[auto]** where the aging tool
allows; revenue by month / customer — **[auto]** (*`get_profit_and_loss`* with a monthly
breakdown, *`get_customer_sales`*); **subledger-to-GL reconciliation** — **[auto]**, comparing
the aging total to the A/R control account, which is one of the highest-value schedules this
skill can produce unaided; sample invoices with support — invoice **[auto]**
(*`search_invoices`*, *`read_invoice`*), contract and delivery evidence **[manual]**; credit memo
detail — **[auto]** (*`search_credit_memos`*); **allowance calculation** — **[manual]**, an
estimate that lives in a schedule not the ledger; confirmations support — **[manual]**; revenue
recognition memos — **[manual]**, authored.

**Inventory**: inventory listing by location — **[gated]** (*`search_items`* gives the item
master; per-location quantities usually need an inventory system); costing support
— **[manual]**; **physical count records** — **[manual]**,
and never inferable; reconciliation to GL (per `inventory-to-gl-reconciliation`) — **[gated]**,
GL side **[auto]**; obsolescence reserve calculation — **[manual]**.

**PP&E**: fixed asset register (per `fixed-asset-register-and-depreciation`) — **[gated]**: the
GL accounts and movements are **[auto]** (*`get_general_ledger`*), but a true asset-by-asset
register with lives and methods usually lives outside the books; additions with invoices —
additions **[auto]**, invoices **[manual]**; disposals — **[auto]** to identify the movement;
depreciation schedule — **[manual]**; roll-forward — **[auto]** from GL movement.

**A/P / Accruals**: A/P aging — **[auto]** where the aging tool allows; subledger-to-GL
reconciliation — **[auto]**; accrual support and calculations (per `accruals-and-deferrals`) —
**[gated]**, the booked entries are **[auto]** (*`search_journal_entries`*) and the calculations
behind them are **[manual]**; **search for unrecorded liabilities** support — **[auto]** and
genuinely well-suited to this workspace: list bills and payments recorded *after* period end for
services *before* it (*`search_bills`*, *`search_bill_payments`*), which is exactly the auditor's
own procedure; vendor statements — **[manual]**.

**Debt**: **debt agreements** — **[manual]**; amortization schedules — **[manual]**; covenant
compliance (per `debt-and-covenant-tracking`) — **[gated]**, the ratios' inputs are **[auto]**
and the covenant definitions are **[manual]**; interest expense recalculation support —
**[gated]**, interest posted is **[auto]** (*`get_general_ledger`*), the rate and terms
**[manual]**; confirmations support — **[manual]**.

**Equity**: equity roll-forward — **[auto]** from the equity
accounts' GL movement; stock / option records —
**[manual]**; **board minutes for equity transactions** — **[manual]**.

**Tax**: tax provision — **[manual]**; returns —
**[manual]**; deferred tax support — **[manual]**. The tax accounts' balances and movements are
**[auto]**, which is the starting point but not the provision.

**General**: **trial balance** — **[auto]**; **general ledger** — **[auto]**; board / committee
minutes — **[manual]**; significant contracts — **[manual]**; **related party listing** —
**[manual]** (see the edge case: the books do not flag related parties, and this is a common
audit finding); management representation support — **[manual]**; subsequent events memo —
**[gated]**, the post-period transactions are **[auto]** and the memo is authored.

## Step 3 — Specify what makes each item audit-ready

Handing over something incomplete costs more than handing over nothing, because it generates
questions and rework.

For each PBC item, define the standard:

- **Ties to the GL / financial statements** — every schedule reconciles to the audited number.
  **[auto]** to test, wherever the schedule was produced from the books: compute the difference
  against the control account and show it
- **Supported** — underlying documents available: invoices, contracts, confirmations.
  Mostly **[manual]**
- **Roll-forward / reconciliation included** where relevant — opening, movements, closing.
  **[auto]** from GL movement for balance-sheet accounts
- **Methodology documented** for estimates and judgments — **[manual]**
- **Reviewed** internally before handing to auditors — **[manual]**, and it needs a named
  reviewer who is not the preparer

**A schedule that doesn't tie to the GL will generate auditor questions and rework — the
tie-out is the point.**

**Mosofin addition to this standard: provenance.** Every `[auto]` schedule records the tool, the
parameters, the as-of timestamp, and the `mock` status that produced it. That is what lets
someone reproduce the number six months later when the auditor asks.

## Step 4 — Assess readiness and gaps

For each item:

- **Is it already prepared?** (e.g. monthly reconciliations from close —
  `month-end-close-checklist`, `balance-sheet-reconciliations`) — **[manual]** to confirm what
  exists outside the books
- **Does it tie out?** — **[auto]** for anything produced from the books
- **Is the support complete?** — **[manual]**
- **Who owns preparing it?** — **[manual]**, and mandatory for every `[manual]` item
- **What's the gap?** — the capability map from Gate 2 answers this directly for every schedule

**Identify the high-effort and high-risk items early.** The reliable signal: items that are
`[manual]`, judgmental, *and* material. Those three together are where audits slip.

## Step 5 — Build the tracker and timeline

- **Assign each item an owner and due date** (before fieldwork) — **[manual]**
- **Sequence so foundational items (TB, reconciliations) come first** — everything else ties to
  them, so a late trial balance delays every other schedule
- **Track status** (not started / in progress / ready / delivered / auditor questions)
- **Build in review time before items go to auditors** — the review in Step 3 needs calendar
  space, or it will not happen

Sequence backwards from the fieldwork start date confirmed at Gate 3.

## Step 6 — Prepare for judgmental areas

**Auditors focus on estimates and judgments** — the places where the number is an opinion rather
than a fact. Prepare robust memos for:

- **Revenue recognition conclusions**
- **Allowances and reserves** — credit losses (money you may not collect), inventory
  obsolescence (stock you may not sell), warranty (repairs you may owe)
- **Impairment assessments** — whether an asset is worth
  less than its carrying value
- **Valuation judgments**
- **Contingencies** — possible obligations depending on a
  future event, such as a lawsuit
- **Going concern** (if relevant) — whether the entity can continue operating for the
  foreseeable future

**These memos explain management's position and support; they reduce back-and-forth.**

All of these are **[manual]** to author. What the workspace *can* contribute is the underlying
data each memo rests on — the aging behind an allowance, the balances behind an impairment test,
the cash trend behind a going-concern assessment — **[auto]**. Supply that data with its
provenance, and let the human write the judgment.

## Step 7 — Anticipate adjustments and prior-year items

- **Review prior-year audit adjustments and management letter points — ensure they're addressed
  this year.** **[gated]**: prior audit adjustments are often visible as journal entries around
  the prior year-end (*`search_journal_entries`*, **[auto]**); the management letter itself is
  **[manual]**
- **Self-identify likely adjustments rather than waiting for auditors** — **[auto]** analytics
  help here: unusual journal entries, round-number postings, entries dated after period end,
  accounts that moved sharply
- **Prepare for the search for unrecorded liabilities and subsequent events review** —
  **[auto]**, per Step 2's A/P block: post-period bills and payments for pre-period services are
  directly readable, and this is one of the strongest automated contributions in the whole skill

## Step 8 — Output

Deliver an `.xlsx` audit-prep tracker.

**Sheet 1: PBC Tracker**

| Area | PBC Item | Description | Owner | Due Date | Status | Ties to GL? | Support Complete? | Notes |

Add columns: **Source (auto / gated / manual)**, **Tool used**, and **Entity (`display_name`)**.

**Sheet 2: Readiness Summary**

By area: % ready, key gaps, high-risk items. **Add:** % of items the workspace can produce
unaided versus those needing a human — the honest headline of an audit-readiness assessment.

**Sheet 3: Judgmental Area Memos**

List of required memos and their status, with the supporting data available for each.

**Sheet 4: Prior-Year Follow-Ups**

Prior adjustments and management letter points, and how addressed.

**Sheet 5: Timeline**

Sequenced schedule to fieldwork.

**Sheet 6: Coverage — NEW, Mosofin-specific**

| PBC Item | Area | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used | Parameters | As-of timestamp | Policy (enabled / permission / disabled) | `mock` | Gap — what could not be produced and who owns it |

This sheet is the audit trail for the audit prep itself. In a multi-entity run it is **per
entity**: a tool enabled for one company file may be disabled for its sibling, so the same PBC
item can be `[auto]` for one component and `[manual]` for another.

Optionally a clean PBC list document for sharing with the team (Word, where the host can make one).

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming:** `Audit_Prep_PBC_[YYYY]_[EntityName].xlsx`

In a multi-entity run, `[EntityName]` is the company file's `display_name`, one per component
plus a group file. Every file states which datasource and `display_name` it covers.

**Grounding:** every figure traces to a tool result in this conversation or to labelled
user-supplied evidence. End with a single **Data sources** line grouping calls by datasource.
Where the data does not cover something, **name the tool that would have covered it** instead of
estimating.

## Step 9 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them,
ask — explicitly, at that point, not earlier — whether to save this as their own customized
version. A general "yes, go ahead" from earlier does not count.

Audit prep is annual, so this step matters more here than almost anywhere: **next year's prep
should start from this year's list, not from a blank page.**

On an explicit yes, persist the **decisions**:

- **The tailored area map** — which of the sixteen standard areas this entity actually has, and
  which were scoped out and why
- **The PBC list as tailored**, with each item's owner, its usual lead time, and where the
  `[manual]` evidence lives (which folder, which system, which person)
- The engagement type, the auditor's own PBC list if one governs, and the fieldwork cadence
- **Judgmental areas and their memo owners** — the areas that consume the most audit effort
- **Prior-year adjustments and management letter points**, so next year's Step 7 opens with them
  already listed
- Materiality as communicated, with the year it applied to
- The replay recipe: the exact sequence of reads that produced this year's schedules

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference
files; set `datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write
preference files alongside the installed skill.

**Do not persist the audited figures, the schedules themselves, or any client document.** They
are a snapshot of one year and belong in the audit file, which is a controlled record. Persist
the *list, the owners, and the decisions*.

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks /
Northbrook Trading — no inventory area; PP&E register held by the finance manager; leases
material" — not "no inventory area". Components of a group differ sharply in what they hold, and
an unlabelled area map applied to the wrong component scopes out a real balance. Record the
chosen **scenario** (single vs group, and which set) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to
the workspace and are re-discovered by Gates 1–2 every run — which matters especially across a
full year, since a tool enabled last audit may be disabled this one. **Decisions are the user's;
state is the workspace's.**

On later runs, match stored entity names against Gate 1's live list. An entity in preferences
that is no longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One PBC list, one readiness
summary, one timeline.

**Multi-entity / group audit.** Steps 0–8 run **once per entity**, each call targeting exactly
one `data_source_id`, every PBC item and readiness score carrying its component's
`display_name`. Then one cross-entity step:

- **A group PBC list on top of the component lists** — consolidation support, the elimination
  schedule, intercompany reconciliations, and the group's own judgmental memos.
- **Component readiness is not additive.** The group is ready when the *slowest* component is
  ready, not when the average is. Report the critical path, not a blended percentage.
- **Capability differs per component**, so the same PBC item can be `[auto]` at one entity and
  `[manual]` at another. The readiness summary must show this, because it is precisely where
  effort needs to go.
- **Intercompany balances must agree between components** before the group audit begins — a
  mismatch found in fieldwork is an expensive one. See `intercompany-reconciliation`.
