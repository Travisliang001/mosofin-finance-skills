<!-- derivatives-and-hedging-asc815 · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding)
- Step 0b — Three checks the workspace can run (Mosofin addition)
- Step 1 — Inventory instruments and determine the accounting model
- Step 2 — Hedge designation and documentation
- Step 3 — Fair value measurement
- Step 4 — Effectiveness testing
- Step 5 — Journal entries
- Step 6 — Disclosures and controls
- Step 7 — Evolve the skill (Mosofin-specific, final step)
- Outputs
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Never drop a task because no tool covers it.** In this skill nearly everything is `[manual]` by the
nature of the subject, and recording that honestly is the correct outcome — not a shortfall.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding)

Pull the `[auto]` / `[gated]` reads. **Batch independent reads into one message** — the derivative
accounts, the OCI accounts, the settlements and the debt do not depend on each other. Never serialize
them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`search_accounts`* — **the derivative asset / liability, OCI and derivative gain / loss accounts** —
  usually **[auto]**
- *`get_balance_sheet`* / *`get_trial_balance`* — **recorded derivative positions and the OCI balance** —
  usually **[auto]**
- *`get_general_ledger`* on those accounts — **every movement, including the OCI reclassifications** —
  usually **[auto]**
- *`get_profit_and_loss`* — derivative gains and losses recognised — usually **[auto]**
- *`search_purchases`* / *`search_bill_payments`* / *`search_deposits`* / *`search_transfers`* — **cash
  settlements to and from counterparties** — usually **[auto]**
- *`search_vendors`* / *`get-vendor`* — counterparty banks — usually **[auto]**
- *`search_journal_entries`* — the mark-to-market and reclassification entries, which is how most of this
  is recorded — usually **[auto]**
- *`get_general_ledger`* on the debt accounts — **the hedged item, where it is interest-rate debt** —
  usually **[auto]**
- *`get_company_info`* — legal name, base currency, reporting dates — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — it cannot support a hedge designation, an
effectiveness conclusion, or a disclosure.

## Step 0b — Three checks the workspace can run (Mosofin addition)

Run these before Step 1. Each addresses a specific, common failure, and each is `[auto]`.

**1. Settlement completeness.** Scan cash movements to and from banks and financial counterparties
(*`search_purchases`*, *`search_deposits`*, *`search_transfers`*, *`search_vendors`*) and match them
against the instrument inventory. **A settlement with no corresponding instrument recorded suggests a
derivative accounting has not been told about** — which is how unrecorded positions persist. Report each
as a question.

**2. OCI reclassification.** Read the movement on the cash flow hedge OCI account (*`get_general_ledger`*).
For each amount parked there, ask **whether the hedged transaction has now occurred**. **Amounts stranded
in OCI after the hedged item has affected earnings are misstated** — the release should have happened, and
both OCI and earnings are wrong until it does. Where the hedged item is scheduled debt interest, the timing
is directly checkable against the interest actually charged.

**3. Documentation timing.** Compare **the date a derivative first appears in the accounts** against **the
designation date supplied**. **Hedge accounting requires contemporaneous documentation — it cannot be
applied retrospectively.** If the instrument existed before it was documented, hedge accounting is not
available for that gap, and every fair value movement in it belongs in profit and loss. Flag the gap in
days and the amount at stake.

Where any of these cannot be run because the relevant tool is unavailable, **record the check as not
performed** rather than reporting no exceptions.

## Step 1 — Inventory instruments and determine the accounting model

For each contract — **[manual]** for all three determinations:

- **Determine if it is a derivative.** The tests turn on the contract's terms: a value that changes with an
  underlying, little or no initial net investment, and settlement at a future date
- **Identify embedded derivatives in host contracts.** **This is the hardest completeness problem in the
  area** — the derivative is buried inside a contract that looks like something else entirely. Convertible
  loans, supply agreements with index-linked pricing, leases with unusual escalators, and contracts
  denominated in a third currency are the usual places
- **Determine if it qualifies for hedge accounting**

**[auto]** contribution only: the **recorded** instruments and the settlement sweep give a starting
inventory. **The absence of an instrument in the accounts is not evidence that none exists** — embedded
derivatives by definition are not separately recorded until someone identifies them.

## Step 2 — Hedge designation and documentation

**Before, or at, inception** — and the timing is the point — document — **[manual]**:

- **Risk being hedged**
- **Hedged item / transaction**
- **Hedging instrument**
- **Hedge type** (cash flow, fair value, net investment)
- **How effectiveness will be assessed**

**Hedge accounting is elective and conditional.** Without contemporaneous documentation it is simply not
available, however economically sound the hedge is — and the consequence is that all fair value movement
goes through profit and loss. **The documentation is not paperwork after the fact; it is the thing that
creates the accounting treatment.** Step 0b's third check exists for exactly this reason.

Briefly, the three hedge types, since the accounting differs:

- **Cash flow hedge** — hedging variability in future cash flows (e.g. floating-rate interest, a forecast
  purchase). Effective portion to **OCI**, released to earnings when the hedged item hits earnings
- **Fair value hedge** — hedging changes in the value of a recognised item (e.g. fixed-rate debt). Both
  the derivative **and the hedged item** are remeasured through earnings
- **Net investment hedge** — hedging the currency exposure of a foreign operation. Effective portion to
  **OCI**, alongside the translation difference it offsets — see `foreign-currency-translation-asc830`

## Step 3 — Fair value measurement

At each reporting date — **[manual]**:

- **Obtain the valuation and validate reasonableness.** The counterparty's mark is the usual source, and it
  is not independent — the counterparty is on the other side of the trade. Validating it, at least
  approximately, is part of the control
- **Separate the credit valuation adjustment (CVA / DVA) if applicable** — the adjustment for the risk that
  the counterparty (CVA) or the entity itself (DVA) fails to perform

**[auto]** contribution: the **previously recorded** carrying value, so the movement to be booked is the
difference between the new valuation and what is on the books — and that difference, not the valuation, is
the entry.

## Step 4 — Effectiveness testing

Perform **prospective and retrospective** assessments — **[manual]**, since both require valuations of the
instrument and of the hedged item:

- **Qualitative assessments if permitted** — available where the critical terms match closely, and much
  less work
- **Quantitative methods (dollar-offset, regression) as needed**

Two things worth stating: effectiveness must be assessed **at least each reporting period**, and **failing
it means dedesignation** — hedge accounting stops prospectively, and the amounts already in OCI follow
specific rules rather than simply reversing.

## Step 5 — Journal entries

**Baseline: derivatives are recognized at fair value.** `DR` is a debit, `CR` a credit. **Mosofin does not
post** — these are proposals.

**Change in FV without hedge accounting (trading):**
```
DR/CR Derivative Asset/Liability      XXX
    CR/DR Gain/Loss on Derivatives        XXX
```

**Cash flow hedge (effective portion to OCI):**
```
DR/CR Derivative Asset/Liability      XXX
    CR/DR OCI - Cash Flow Hedge           XXX
```

**Reclass from OCI when the hedged item impacts earnings.** — and this is the entry Step 0b's second check
looks for. Use the **real account names from the connected chart of accounts** (*`search_accounts`*,
**[auto]**).

Note that any **ineffective portion** of a cash flow hedge goes to earnings immediately, not to OCI — so a
single hedge can produce entries in both places in the same period.

## Step 6 — Disclosures and controls

Produce — **[gated]**: the recorded amounts and their location are **[auto]**, the notionals and maturities
are **[manual]**:

- **Notional and maturity tables**
- **Location of gains / losses in P&L / OCI** — **[auto]**, since the ledger shows exactly where each
  movement was posted
- **Credit risk disclosures**

**Controls** — **[manual]** to operate, with `[auto]` evidence where noted:

- **Contract completeness** — **[gated]** via the Step 0b settlement sweep, which is real evidence for this
  control
- **Review of valuations** — **[manual]**
- **Documentation timing** — **[gated]** via the Step 0b timing check
- **Effectiveness testing sign-off** — **[manual]**

## Step 7 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The instrument inventory's fixed terms**: type, counterparty, notional, start and maturity dates,
  underlying. These do not change period to period
- **The hedge designations**: which instrument hedges which item, the hedge type, **the designation date**,
  and the documented risk. The designation date in particular, because the timing check depends on it
- **The effectiveness method** per relationship — qualitative or quantitative, and which quantitative
  method
- **The account map**: derivative asset / liability, the cash flow hedge OCI account, the derivative gain /
  loss account, and where the ineffective portion goes
- **The valuation source** and methodology — who provides the mark, and how it is validated. **Not the
  values**
- **Whether hedge accounting is applied at all**, per relationship
- **Dedesignation history**, with dates and reasons
- The replay recipe: the exact sequence of reads that produced the recorded positions and the three checks

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist valuations, mark-to-market positions, notionals with counterparty names, or effectiveness
results.** A derivative position discloses the entity's view on a rate or a currency, which is
commercially sensitive; a stored mark is stale within a day. **Persist the structure and the designations;
re-obtain the values.**

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / Northbrook
Trading — swap hedges facility A interest, cash flow hedge designated 2026-03-14, qualitative
effectiveness, OCI account: Cash Flow Hedge Reserve" — not "cash flow hedge, qualitative". **The
instrument and the hedged item must sit in the same entity for the designation to hold**, and an unlabelled
designation applied to the wrong company file asserts a hedge relationship that does not legally exist.
Record the chosen **scenario** (single vs multi, and which entity holds what) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's** — and every valuation, OCI balance and effectiveness result is state.

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Outputs

- **Hedge accounting memo per hedge relationship.** Risk, hedged item, instrument, type, designation date,
  effectiveness method — **with the designation date checked against when the instrument first appeared in
  the accounts**.
- **Period-end JE package.** Marked as **proposals**, showing the movement from the recorded carrying value
  to the new valuation, and splitting effective and ineffective portions.
- **Effectiveness test results.** With the method used and the period assessed.
- **Disclosure tables.** Notional and maturity, location of gains and losses in P&L and OCI, credit risk.
- **Exception log** — failed hedges and dedesignations, with dates and consequences.

**Workspace checks report — NEW, Mosofin-specific.**

| Check | Result | Detail | Action |

Covering the three Step 0b checks: **settlement completeness**, **OCI reclassification**, and
**documentation timing**. Each states whether it was run, and what it found — including nil results.

**Coverage sheet — NEW, Mosofin-specific.**

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used / external source | As-at date | Policy | `mock` | Gap — what could not be evidenced and who supplied it |

**Every valuation and every effectiveness result reads `manual` with its source.** That is the correct,
expected entry — an `[auto]` valuation here would be a defect.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.
Offer a Word document only where the host can make one; otherwise give the text in the chat.

**File naming — Mosofin addition** (the original left it unstated, and multi-entity output needs it):
`Derivatives_Hedging_[YYYY-MM]_[EntityName].xlsx`, where `[EntityName]` is the company file's
`display_name`. Every file states which datasource and `display_name` it covers.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where the data does not
cover something — every valuation, every rate — **name the source required** instead of estimating.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One instrument inventory, one set of
designations.

**Multi-entity.** Steps 0–6 run **once per entity**, each call targeting exactly one `data_source_id`,
every instrument carrying its entity's `display_name`. Then:

- **The instrument and the hedged item must sit in the same entity** for the designation to hold in that
  entity's own accounts. **A group treasury holding the swap while a subsidiary holds the debt is common
  and consequential**: the subsidiary has an unhedged exposure in its standalone accounts, and the hedge
  may only work at group level — if at all, and only with the right documentation.
- **Internal derivatives do not qualify.** A swap between two group entities nets to zero on consolidation
  and generally cannot be a hedging instrument for group reporting; only an external contract can. Where
  treasury faces the market externally and then mirrors internally, **the external leg is the hedging
  instrument**.
- **Net investment hedges are inherently a group matter** — they hedge the translation of a subsidiary, so
  the exposure exists only in the consolidated accounts. See `foreign-currency-translation-asc830` and
  `consolidation-and-eliminations`.
- **The settlement sweep runs per entity**, since cash moves in whichever entity has the bank account, and
  that may not be the entity carrying the instrument.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict per company
file.
