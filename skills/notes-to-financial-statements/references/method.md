<!-- notes-to-financial-statements · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding) — Mosofin addition
- Step 1 — Build the disclosure checklist
- Step 2 — Draft accounting policy notes
- Step 3 — Draft account-detail notes
- Step 4 — Draft commitments and contingencies
- Step 5 — Draft related party disclosures
- Step 6 — Draft subsequent events note
- Step 7 — Completeness review
- Step 8 — Consistency and cross-references
- Step 9 — Output
- Step 10 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Never drop a task because no tool covers it.** Policies, contingencies and legal positions are legitimately
`[manual]`.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding) — Mosofin addition

**Batch independent reads into one message** — the statements, the roll-forward populations, the
concentration data and the post-period activity do not depend on each other. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`get_balance_sheet`* and *`get_profit_and_loss`*, **current and comparative** — **the tie-out targets** —
  usually **[auto]**
- *`get_trial_balance`* at both period ends — usually **[auto]**
- *`search_accounts`* — **the chart, for scoping which notes apply** — usually **[auto]**
- *`get_general_ledger`* on **allowance, PP&E, intangible, goodwill, debt, equity and reserve accounts** —
  **the roll-forward populations** — usually **[auto]**
- *`get_profit_and_loss`* **by class / customer / product** — **revenue disaggregation and concentration** —
  usually **[auto]**
- *`search_customers`* / *`search_vendors`* — **concentration, and related-party name matching** — usually
  **[auto]**
- *`search_employees`* — **related-party name matching** — usually **[auto]**
- **Everything posted after the reporting date up to the issuance date** — *`search_journal_entries`*,
  *`get_general_ledger`* — **the subsequent events candidate population** — usually **[auto]**
- *`get_aged_receivables`* / *`get_aged_payables`* — usually **[auto]**
- *`get_company_info`* — **legal name, currencies, year-end** — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that note to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — **notes are published with the statements**, and a
fixture-derived roll-forward would be audited.

## Step 1 — Build the disclosure checklist

**Tailor a checklist to the entity. Common note categories** — with the Mosofin scoping verdict, since
**which notes apply is largely readable from the chart**:

**1. Nature of operations and basis of presentation** — **[gated]**
- **Description of the business** — **[manual]**
- **Basis of accounting** (GAAP / IFRS, going concern) — **[manual]**
- **Consolidation principles** — **[gated]**; Gate 1 lists the entities
- **Functional and presentation currency** — **[auto]** from the profile
- **Use of estimates** — **[manual]**

**2. Summary of significant accounting policies** — **[manual]** throughout, **[auto]** to scope which apply
- **Revenue recognition** (per `revenue-recognition-asc606`)
- **Cash and cash equivalents** (definition)
- **Accounts receivable and allowance**
- **Inventory** — costing method, per `inventory-costing-fifo-lifo-wavg`
- **Property, plant & equipment** — capitalization, depreciation methods, useful lives
- **Intangible assets and goodwill**
- **Leases** (per `lease-accounting-asc842-ifrs16`)
- **Impairment policies**
- **Income taxes**
- **Foreign currency**
- **Financial instruments**
- **Stock-based compensation**
- **Fair value measurement**
- **Recently adopted and recently issued accounting standards**

**3. Account-level detail notes** — one per material line item — **[gated]**, and **this is where the
workspace does most of the drafting**:
- **Cash and restricted cash** — **[gated]**; restricted status is `[manual]`
- **Receivables and allowance roll-forward** — **[auto]**
- **Inventory by category** — **[auto]** where the chart separates categories
- **Prepaid and other current assets** — **[auto]**
- **Property, plant & equipment** — cost, accumulated depreciation, additions, disposals — **[auto]**; see
  `fixed-asset-register-and-depreciation`
- **Intangibles and goodwill**, with impairment testing results — **[gated]**; balances `[auto]`, the test
  `[manual]`, per the goodwill impairment test
- **Leases** — ROU assets, lease liabilities, maturity analysis, weighted-average term and discount rate —
  **[gated]**; balances `[auto]`, the schedule `[manual]`
- **Accrued liabilities detail** — **[auto]**
- **Debt** — terms, maturities, covenants, interest rates — **[gated]**, per `debt-and-covenant-tracking`
- **Income taxes** — current / deferred, effective rate reconciliation, deferred tax components, NOLs,
  uncertain positions — **[gated]**, per the tax provision work and
  the deferred tax roll-forward
- **Equity** — share classes, rights, dividends, stock-based comp — **[gated]**; **share data is `[manual]`
  from the cap table**
- **Revenue disaggregation and contract balances** — **[auto]** by class, customer or product
- **Segment information** (per `segment-reporting`) — **[gated]**

**4. Commitments and contingencies** — **[manual]**
- **Operating commitments** — purchase obligations, capital commitments
- **Guarantees**
- **Litigation and claims**
- **Environmental and regulatory matters**

**5. Related party transactions** — **[gated]**
- **Nature of relationships** — **[manual]**
- **Transactions and balances** — **[auto]** once the parties are identified
- **Terms** — whether at arm's length — **[manual]**

**6. Financial instruments and risk** — **[gated]**
- **Fair value hierarchy** (Level 1/2/3) — **[manual]**; no fair values here
- **Credit risk, liquidity risk, market risk** (IFRS 7 / ASC 825) — **[gated]**; **concentration and ageing
  are `[auto]`**
- **Hedging activities** — **[manual]**, per hedge accounting

**7. Subsequent events** — **[gated]**
- **Recognized (Type 1) and non-recognized (Type 2) events through the issuance date**

**8. Other** — **[gated]**
- **Earnings per share computation** — **[manual]**; needs the share register
- **Pension / post-employment benefits** — **[manual]**; actuarial
- **Business combinations** — **[gated]**
- **Discontinued operations** — **[manual]**
- **Going concern** (if substantial doubt) — **[manual]**

**Mosofin scoping addition**: **read the chart and the balance sheet to determine which notes are live.**
No inventory, no inventory note. No goodwill, no goodwill note. No debt, no debt note. **Report the notes
ruled out with their evidence**, so a required disclosure is never dropped silently — the same technique as
a GAAP to IFRS conversion and an IPO readiness review.

## Step 2 — Draft accounting policy notes

**For each significant policy, draft a clear statement of the method the entity uses. Pull the actual policy
from the entity's data — do not assume.**

**Example structure (revenue)**: *"The Company recognizes revenue when control of goods or services
transfers to the customer, in an amount reflecting the consideration the Company expects to receive.
[Describe the entity's specific performance obligations, timing of recognition, and significant
judgments.]"*

**The draft uses the entity's actual policies. Where a policy isn't clear from the inputs, flag for the user
to confirm rather than inventing one.**

**Mosofin refinement of "pull from the entity's data":** **the data shows the results of a policy, not the
policy.** What is available:

| Policy | What the data shows | Verdict |
|---|---|---|
| **Inventory costing** | the platform's method setting, where exposed | **[gated]** — see `inventory-costing-fifo-lifo-wavg`; **the platform's method may not be the reported one** |
| **Depreciation** | the charge and the implied rate | **[gated]** — **an implied life is a question, not a policy** |
| **Revenue timing** | when revenue was recognised relative to invoicing | **[gated]** |
| **Capitalization threshold** | the pattern of what was capitalised | **[gated]** — see `fixed-asset-register-and-depreciation` |
| **Everything else** | nothing | **[manual]** |

**Draft the policy from what the user confirms, and where you have inferred something from the pattern, say
so and ask.** *"Depreciation appears to be charged straight-line at rates implying 5-year lives on
equipment — please confirm the stated policy"* is useful. **Asserting it as the policy is not.**

## Step 3 — Draft account-detail notes

**For each material account, draft the disclosure with the supporting numbers** — **[auto]** for most:

- **Roll-forwards** — e.g. **allowance, PP&E, goodwill, debt** — **[auto]**: opening, movements, closing,
  from the account histories
- **Maturity analyses** — **debt, leases** — **[gated]**; needs the schedules
- **Component breakdowns** — **inventory by type, deferred tax by source** — **[gated]**; `[auto]` where the
  chart separates them
- **Comparatives** — **[auto]**, **and checked against what was filed**

**Pull every number from the supporting schedules. Cross-reference to the primary statements — note totals
must tie to the BS/IS face.**

**That last sentence is the workspace's strongest contribution to this skill.** **[auto]**: **the note
figures and the statement figures come from the same reads**, so **the tie is provable rather than
transcribed.** **Report each note's tie with its difference, including zero**, and **record the tool call
behind each figure** — which makes Sheet 2's supporting-data reference reproducible.

**And check the comparative against the filed prior year**, not only against the ledger — see
`financial-statement-builder`. **A note comparative that does not match last year's published note is a
visible inconsistency**, and it is common where audit adjustments were never posted.

## Step 4 — Draft commitments and contingencies

- **Commitments**: **quantify purchase obligations, capital commitments, lease commitments (maturity
  table)** — **[gated]**: **lease commitments are `[auto]` where recognised**; purchase obligations are
  contractual and `[manual]`
- **Contingencies**: **for litigation and claims, describe the matter, the entity's position, and the
  accounting treatment** — **accrued if probable and estimable; disclosed if reasonably possible; nothing if
  remote** — per **ASC 450 / IAS 37**. **[manual]**, entirely

**Legal review needed: contingency language has legal implications. Draft from management's input but flag
that legal counsel must review wording — Claude drafts, doesn't opine on legal outcomes.**

**This is a hard boundary and it is worth restating in Mosofin terms.** **[auto]** contribution is limited to
one thing: **whether a provision has been recorded**, and its movement. **That is a fact about the accounts.**
**Whether a matter is probable, reasonably possible or remote, and what it might cost, are legal and
management judgments that must be supplied.** **Never characterise an outcome and never estimate an
unestimated loss**.

## Step 5 — Draft related party disclosures

- **Identify relationships** — parent, subsidiaries, associates, key management, entities under common
  control — **[gated]**
- **Disclose transaction types, amounts, and outstanding balances** — **[auto]** once parties are identified
- **State terms** — arm's length or not — **[manual]**
- **Key management compensation** — required under IFRS; varies under US GAAP — **[manual]**

**Mosofin contribution — the identification step is partly automatable.** **[auto]**:

- **Vendors and customers whose names match other connected group entities** — **intercompany transactions**,
  and see `intercompany-reconciliation`
- **Vendors and customers whose names match employees or known directors** — **a match to investigate**,
  never a conclusion. See `fraud-detection-and-forensics` for the discipline
- **Once a party is identified, its transactions and balances are exact** — the disclosure's quantitative
  half writes itself

**The relationships themselves are `[manual]`.** A director's other company will not match on name, and a
family relationship is invisible entirely. **Ask for the related party list; use name matching to test it,
not to build it.**

## Step 6 — Draft subsequent events note

**For events between the reporting date and issuance** — **[gated]**:

- **Recognized (Type 1)**: **conditions existed at the reporting date → already adjusted in the statements;
  disclose if significant**
- **Non-recognized (Type 2)**: **conditions arose after → disclose nature and estimated financial effect**,
  or state that an estimate can't be made

**Common subsequent events: debt issuances / refinancing, acquisitions, major customer loss, litigation
developments, asset impairments, dividends declared, equity raises.**

**Mosofin contribution — the candidate population.** **[auto]**: **read everything posted between the
reporting date and the issuance date.** Surface:

- **Large or unusual transactions** by value
- **New debt, repayments or refinancing** — movements on debt accounts
- **Equity movements** — raises, distributions, dividends declared
- **Acquisitions** — new goodwill, investment or intangible balances
- **Material write-offs or impairments**
- **A significant customer with no activity** where there previously was

**This is a candidate list, not a subsequent events note.** **Materiality and the Type 1 / Type 2
classification are `[manual]`**, and **events that leave no ledger trace — a lawsuit filed, a contract lost,
a regulatory change — are invisible here.** **Ask about those explicitly.**

**But the note that most often misses something is this one**, and a systematic list of what actually hit the
books beats recollection.

## Step 7 — Completeness review

**Run the disclosure checklist against the drafted notes. For each item** — **[gated]**:

- **Required for this entity?** (Y/N based on framework + activities) — **[gated]**: **activities are
  `[auto]` to scope; the framework requirement is `[manual]`**
- **Drafted?** (Y/N) — **[auto]**
- **Tied to supporting data?** (Y/N) — **[auto]**
- **Needs management / legal input?** — flag — **[manual]**

**Flag gaps. Public entities have far more disclosure requirements than private; IFRS and US GAAP differ in
specifics.**

**Mosofin addition to the checklist — a fifth column: Verdict.** `[auto]` / `[gated]` / `[manual]`. **A note
marked Drafted-Yes and Verdict-manual is drafted from what someone told you**, and that is a different
assurance from one built on a tie-out. **The reviewer should see which is which.**

## Step 8 — Consistency and cross-references

- **Note numbers referenced on the face of the statements match the notes** — **[manual]**
- **Numbers in notes tie to the primary statements** — **[auto]**, and reported with differences
- **Comparatives consistent with prior year notes** (or explained) — **[gated]**; **check against the filed
  prior year**
- **Accounting policy notes consistent with how the numbers were actually prepared** — **[gated]**, ⭐ **and
  worth emphasising**: **a policy note saying one thing while the data shows another is a real
  inconsistency.** A stated FIFO policy against a platform running weighted average; a stated
  five-year life against an implied ten. **[auto]** to detect the divergence; **[manual]** to resolve which
  is right
- **Terminology consistent throughout** — **[manual]**

**That fourth check is the one the workspace uniquely enables.** **Policy notes are usually rolled forward
year to year and rarely tested against the accounts.** Testing them is cheap here.

## Step 9 — Output

Deliver the notes as a structured document plus a checklist:

**Document: Notes to Financial Statements** — **drafted notes in standard order, formatted for inclusion in
the financial statements**, **marked DRAFT**, with **items requiring management or legal input visibly
flagged in place**.

**Workpaper (`.xlsx`):**

**Sheet 1: Disclosure Checklist**

| Note | Topic | Required (Y/N) | Drafted (Y/N) | Tied to Data (Y/N) | Needs Input | Owner |

**Add the Verdict column.** Plus the header block: workspace name; the entity by `display_name`; excluded
company files; the framework; **public or private**; **the issuance date**; whether any figure rests on
`mock` data.

**Sheet 2: Supporting Data References** — **which schedule or source backs each note.** **In a Mosofin run
this is the tool, the parameters and the as-at date**, which makes it reproducible.

**Sheet 3: Tie-Out** — **note totals vs. primary statement line items**, **each with its difference,
including zero**.

**Sheet 4: Open Items** — **notes needing management confirmation or legal review.**

**Sheet 5: Subsequent Events Candidates — NEW, Mosofin-specific** — everything material posted between the
reporting date and issuance, **with the classification left blank for management**.

**Sheet 6: Policy Consistency — NEW, Mosofin-specific** — stated policies against what the data shows, with
any divergence flagged.

**Sheet 7: Coverage — NEW, Mosofin-specific**

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used / external source | As-at date | `mock` | Gap |

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.
Offer a Word document only where the host can make one; otherwise give the text in the chat.

**File naming:** `Notes_to_FS_[YYYY]_[EntityName]`

`[EntityName]` is the legal name from the profile, or the group name.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where a note rests on
management's or counsel's input, **say so** rather than presenting it as drafted from data.

## Step 10 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The disclosure checklist** tailored to this entity — **which notes apply and which were ruled out, with
  the evidence.** The most valuable stored asset here
- **The accounting policy statements**, as confirmed — **the wording, which changes rarely and is redrafted
  needlessly every year**
- **The note structure and numbering**
- **The tie-out map** — which note figure ties to which statement line, and which read produces it
- **The related party list** — **by relationship and role**, not by transaction
- **The framework, and whether reduced disclosures apply**
- **The segment basis**, cross-referenced to `segment-reporting`
- **The legal review path** and who performs it
- **Known recurring open items** — expressed as rules
- The replay recipe: the exact sequence of reads that produced the roll-forwards and the tie-outs

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist financial figures, roll-forwards, drafted note text, contingency descriptions or related
party transaction detail.** All state — **and litigation descriptions in particular are sensitive and
legally reviewed**, so a stored draft could be circulated in a form counsel never approved. **Persist the
checklist and the policy wording; redraft every figure.**

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / Northbrook
Group — IFRS, private with reduced disclosures, notes 1–19, no inventory note (no inventory), segment basis
by Class, related parties: parent and two directors' companies" — not "IFRS, notes 1–19". **The checklist is
entity-specific**, and applying one entity's to another omits notes that entity genuinely requires. Record
the chosen **scenario** (single vs multi, consolidated) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's.**

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`.

**Multi-entity.** **The notes accompany consolidated statements**, so:

- **Every account-detail note is consolidated**, with intercompany eliminated — see
  `consolidation-and-eliminations`. **A roll-forward built by summing entities overstates every movement by
  the intercompany amount.**
- **The related party note is where multi-entity matters most.** **Gate 1's list is the group structure**,
  and **transactions between group members are intercompany rather than related-party disclosures in the
  consolidated accounts** — they eliminate. **But in each entity's own statutory accounts they are related
  party transactions requiring disclosure.** **Ask which statements these notes accompany**; the answer
  changes the note completely.
- **A disconnected group member means the consolidated disclosures are incomplete.** Say so before drafting.
- **Concentration is measured at group level**, and **a customer immaterial to the group may be a
  concentration for one subsidiary's own accounts.**
- **Segment disclosure follows the reporting segments**, which may not map to legal entities — see
  `segment-reporting`. **Do not assume the connected file list is the segment structure.**
- **Currency**: the presentation currency governs the notes, and **balances by currency are a required risk
  disclosure** — see `foreign-currency-translation-asc830`.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each note's verdict per company
file.
