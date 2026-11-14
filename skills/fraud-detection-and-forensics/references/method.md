<!-- fraud-detection-and-forensics · method.md · read for: Stages 3–6 — the risk assessment, the analytical tests, and the report. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 1 — Clarify the engagement type and boundaries
- Step 0 — Fetch the evidence (grounding) — Mosofin addition
- Step 2 — Apply the fraud triangle / risk framework
- Step 3 — Fraud risk assessment (if proactive)
- Step 4 — Analytical detection (red flags)
- Step 5 — Investigate flagged items (framework)
- Step 6 — Quantify losses (forensic measurement)
- Step 7 — Report and remediate
- Step 8 — Output
- Step 9 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Never drop a task because no tool covers it.** Evidence preservation, interviews and legal process are
legitimately `[manual]` and stay in the workflow with owners named.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 1 — Clarify the engagement type and boundaries

**Determine what's being asked** — **[manual]**, and **before Step 0**:

- **Fraud risk assessment**: proactively identify where the entity is vulnerable
- **Analytical detection**: screen data for red flags — **no specific allegation**
- **Investigation support**: **a specific concern or allegation exists**

**For investigation support, immediately flag that qualified forensic investigators and legal counsel
should lead, evidence must be preserved (chain of custody), and the analysis is to inform — not to accuse.
Maintain objectivity throughout.**

**Mosofin addition:** where the objective is **investigation support**, **say clearly that a Mosofin read is
analysis and not preserved evidence**, and that records should be preserved by qualified people **before or
alongside** any querying. Querying does not alter records — Mosofin is read-only — but it also does not
preserve them.

## Step 0 — Fetch the evidence (grounding) — Mosofin addition

**Runs after Step 1**, deliberately.

**Batch independent reads into one message** — the vendor master, the employee list, the disbursement
population and the journal entries do not depend on each other. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`search_vendors`* + *`get_vendor`* — **names, addresses, contact details, created dates** — usually
  **[auto]**
- *`search_employees`* + *`get_employee`* — **names, addresses, contact details, active status** — usually
  **[auto]**
- *`search_bills`* / *`search_purchases`* / *`search_expenses`* — **the disbursement population** — usually
  **[auto]**
- *`search_payments`* / *`search_checks`* — payments made — usually **[auto]**
- *`search_journal_entries`* — **manual entries, the financial-statement-fraud surface** — usually
  **[auto]**
- *`search_credit_memos`* / *`search_refund_receipts`* — **voids, refunds and write-offs** — usually
  **[auto]**
- *`get_general_ledger`* — **the full transaction population, which is what Benford's needs** — usually
  **[auto]**
- *`get_profit_and_loss`* and *`get_balance_sheet`* by period — **trends, ratios and reserve movements** —
  usually **[auto]**
- *`search_customers`* — for skimming and lapping context — usually **[auto]**
- *`get_company_info`* — legal name, currency, year-end — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat — **the pre-agreed approver**, per Gate 2 — then re-invoke the
  same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap. **In this skill, record
  which tests could therefore not run** — a test not run is not a test passed.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data. **Fraud analytics over fixture data produces
fictional anomalies about real-sounding names.** Stop and say so.

## Step 2 — Apply the fraud triangle / risk framework

**Fraud typically involves three elements — the fraud triangle:**

- **Pressure / incentive** — financial need, targets, personal circumstances
- **Opportunity** — weak controls, override ability, access
- **Rationalization** — justification

**Plus consider capability. Use this to assess where fraud risk concentrates and to structure analysis —
not to profile individuals.**

**[manual]**, and the last clause is the operative one. **The workspace can tell you where opportunity
exists — it cannot tell you anything about pressure or rationalization, and it must not be used to guess.**
Financial pressure on a named individual is not a legitimate inference from accounting data.

**Categorize fraud types being considered:**

- **Asset misappropriation** — theft, skimming, fraudulent disbursements, payroll schemes, expense fraud —
  **most common**
- **Financial statement fraud** — manipulating results: revenue, reserves, and so on — **highest impact**
- **Corruption** — bribery, kickbacks, conflicts of interest

*Mosofin note on coverage*: **asset misappropriation and financial statement fraud are substantially
testable here**; **corruption largely is not.** Kickbacks and conflicts of interest leave little trace in a
general ledger — they show up in relationships, pricing and communications the workspace cannot see. **Say
so** rather than reporting a clean result across all three categories.

## Step 3 — Fraud risk assessment (if proactive)

**Assess vulnerability by scheme type** — **[gated]**:

- **Map where each scheme could occur given the entity's processes** — **[manual]**; processes are not in
  the ledger
- **Evaluate the controls mitigating each** — the subject of a SOX controls review — **[manual]**
- **Identify gaps** — especially **segregation of duties, override ability, vendor / payroll master
  controls** — **[gated]**
- **Rate residual fraud risk by area** — **[manual]** judgment

**[auto]** contribution — **the master-data controls are partly testable.** Who can create a vendor is a
control question, but **how many vendors were created, when, and how quickly they were first paid** is
readable, and a vendor created and paid the same day is a control observation grounded in fact rather than
assertion.

## Step 4 — Analytical detection (red flags)

**Apply data analysis to surface anomalies.** **This step is where the Mosofin workspace contributes most —
nearly every test below is a query rather than a project.** Each one is marked with its verdict, and the
ones that **cannot** run here are marked plainly rather than quietly softened.

**Every result in this step is an indicator. None of them is a finding about a person.**

### Disbursement / vendor schemes

- **Duplicate payments** (per `duplicate-invoice-detection`) — **[auto]**. That skill's ten rules apply in
  full; nine of them run as queries.
- **Vendors matching employee addresses / bank accounts / phone** (fictitious vendor) — **[gated], and
  partially**. **Address and phone comparison between the vendor and employee masters is `[auto]`** and is a
  genuinely strong test. **Bank account comparison is `[manual]` — bank details are not exposed on this
  surface**, and it is the single most probative element of this test. Report the address and phone results;
  **name the bank-account comparison as not run.**
- **Vendors with sequential or unusual invoice numbering** — **[auto]**. A vendor whose invoice numbers to
  you run 1, 2, 3 is a vendor whose only customer is you.
- **Payments just under authorization thresholds** — **[auto]**, given the threshold. **Distribution of
  payment amounts clustered immediately below a limit** is one of the clearest quantitative red flags
  available, and it is a single query. **Ask for the threshold** — it is `[manual]` and the test is
  meaningless without it.
- **Round-dollar payments** — **[auto]**.
- **Vendors with a PO box only, no validation** — **[gated]**. The address is `[auto]`; **whether it was
  validated is `[manual]`.**
- **Sudden new vendors with high volume** — **[auto]**, and strong: **vendor creation date against
  cumulative spend in the following weeks.**

### Payroll schemes

**Coverage here is materially weaker, because payroll register detail is not on this surface. Say so.**

- **Ghost employees** — no taxes, no benefits, duplicate bank accounts / addresses — **[gated], partially**.
  **Duplicate addresses across employees are `[auto]`**; **the tax, benefit and bank-account elements are
  `[manual]`**, and they are the decisive ones.
- **Duplicate direct-deposit accounts across employees** — **[manual]**. **Bank details are not available
  here.** Report as not run.
- **Terminated employees still paid** — **[gated]**. Employee active status and payment dates are readable;
  **whether a payment after termination is a final settlement or a ghost is judgment**, and final
  settlements are entirely normal.
- **Excessive overtime / adjustments by one approver** — **[manual]**. Needs payroll register detail and
  approver identity.

### Skimming / cash

- **Revenue / cash trends inconsistent with activity** — **[auto]**. Revenue against deposits, by period and
  by location or class.
- **Unusual voids, refunds, write-offs** — **[auto]**, and one of the better tests available here:
  **credit memos, refunds and bad-debt write-offs concentrated by user, by customer, or at period boundaries.**
- **Lapping indicators in AR** (per `cash-application`) — **[gated]**. **Payment application patterns are
  readable — receipts consistently applied to older invoices while newer ones age — but confirming lapping
  needs the bank detail and the remittances**, which are not here.

### Financial statement manipulation

- **Journal entry red flags** (per `journal-entry-review`) — **[auto]**. **Manual entries at period end,
  round amounts, entries to unusual accounts, entries by unexpected users, reversals shortly after.** This is
  one of the strongest surfaces the workspace offers.
- **Reserves / accruals moving with earnings targets** — **[auto]**, and genuinely revealing: **plot reserve
  and accrual movements against pre-reserve profit across periods.** A reserve that reliably moves in the
  direction that smooths the result is an indicator worth investigating.
- **Revenue spikes at period-end, reversals after** — **[auto]**. **Revenue by day across the period
  boundary, and credit notes in the following weeks against invoices from the last days of the period.**
- **Unusual changes in ratios / margins** — **[auto]**. Gross margin, days sales outstanding, expense
  ratios, period over period.

### Benford's Law

**The distribution of leading digits in naturally-occurring financial data follows a known pattern;
significant deviations can indicate fabricated numbers. Apply as a screen — a deviation is an indicator to
investigate, not proof.**

**[auto]** — the full transaction population is available via *`get_general_ledger`*, which is exactly what
this test needs. **Apply it within its limits** (see the edge cases): naturally-occurring, wide-ranging data,
adequate sample size. **Report the population tested, its size, and the deviation measured** — a Benford's
result without its population is not interpretable.

### Statistical / pattern analysis

**Outliers, unusual frequencies, timing clusters.** — **[auto]**. Weekend and holiday postings, entries
outside business hours where timestamps exist, unusual round numbers, repeated identical amounts.

**Prioritize the output.** A wide screen over a full ledger produces many hits. **Rank by strength of
indicator and by amount, state the false-positive expectation, and never present the list as a list of
suspects.**

## Step 5 — Investigate flagged items (framework)

**For items warranting investigation — with qualified professionals leading** — **[manual]** throughout,
and deliberately so:

- **Preserve evidence** — originals, metadata, chain of custody — **don't alter records**. *Mosofin note*:
  **Mosofin cannot alter records, and it also cannot preserve them.** Preservation is a separate act by
  qualified people.
- **Gather evidence from multiple sources to corroborate** — **[gated]**; the ledger is one source, and a
  single-source conclusion is not corroboration.
- **Follow the money** — fund tracing: **trace transactions through accounts to disposition** — **[gated]**.
  **Tracing within the ledger is `[auto]`; tracing beyond it — through bank accounts to a destination — is
  `[manual]`**, because bank statement detail is not on this surface. **Say where the trail leaves what you
  can see.**
- **Build the timeline of events** — **[gated]**; transaction dates are `[auto]`, the surrounding events are
  not.
- **Quantify the potential loss** — see Step 6.
- **Document objectively — facts and evidence, not conclusions about guilt.**

**Maintain confidentiality and avoid tipping off; involve legal counsel on interviews, rights, and
process.**

## Step 6 — Quantify losses (forensic measurement)

**Where a scheme is substantiated — by investigators** — quantify — **[gated]**:

- **Direct loss** — amounts misappropriated or misstated
- **Period and method**
- **Recovery potential** — insurance, restitution, assets
- **Use defensible methods documented for potential legal / insurance use**

**Note the precondition: "where a scheme is substantiated (by investigators)".** **Quantification comes
after substantiation, not instead of it.** Producing a loss figure from indicators alone converts a
screening result into an accusation with a number attached, which is precisely what this skill must not do.

**[auto]** contribution: once investigators have substantiated a scheme and identified the transactions,
**summing and periodizing them from the ledger is straightforward and reliable** — and the ledger trail
supports the documented method the original asks for.

## Step 7 — Report and remediate

- **Objective findings report**: **what the evidence shows, the analysis, the quantification — factual,
  supporting potential legal / HR / insurance processes**, drafted with or for counsel — **[manual]**
- **Control remediation**: **the control failures that allowed the scheme** (a SOX
  controls finding) **and fixes to prevent recurrence** — **[gated]**
- **Escalation to appropriate governance** — audit committee, board, legal — **[manual]**

**Mosofin addition on distribution.** **State on the report who it is for.** A document listing employees
and vendors against fraud indicators is sensitive to the people named in it, most of whom will have done
nothing wrong. **Confirm the authorized recipients before producing it** — that was the Gate 3 question —
and do not widen circulation to make a workpaper more useful.

## Step 8 — Output

Deliver an `.xlsx` analysis workpaper and, where appropriate, a findings framework:

**Sheet 1: Engagement Scope & Boundaries** — type, objectives, and **the objectivity / escalation /
legal-counsel notes**. Plus the Mosofin header block: workspace name; the entity by `display_name`; each
excluded company file and why; **whether any figure rests on `mock` data**; **the authorized recipients**;
and **the statement that these reads are analysis, not preserved evidence**.

**Sheet 2: Fraud Risk Assessment** — by scheme type: vulnerability, controls, residual risk.

**Sheet 3: Analytical Red Flags** — **tests run, anomalies surfaced, by area, prioritized.** Add two Mosofin
columns: **the verdict** (`[auto]` / `[gated]` / `[manual]`) and **the population tested with its size**.

**Sheet 4: Flagged Items for Investigation**

| Item | Red Flag(s) | Area/Scheme | Amount | Evidence Needed | Status |

**Every row is a question, not a conclusion.** Head the sheet accordingly.

**Sheet 5: Fund Tracing / Timeline** (if investigating) — transaction tracing and chronology, **with the
point marked where the trail leaves the ledger**.

**Sheet 6: Loss Quantification** (if substantiated) — methodology and amounts. **Present only where
investigators have substantiated a scheme.**

**Sheet 7: Control Failures & Remediation** — what allowed it; fixes.

**Sheet 8: Escalation & Professional Involvement** — items requiring CFE / legal / governance.

**Sheet 9: Tests Not Run — NEW, Mosofin-specific**

| Test | Why it could not run | What it would have shown | How to obtain it |

**This sheet is as important as Sheet 3.** Bank-account matching for fictitious vendors and ghost employees,
payroll register tests, corruption indicators, external verification — **all unavailable here.** **A test
not run must never be reported as a test passed**, and a clean Sheet 3 alongside an empty Sheet 9 would
misrepresent the coverage badly.

**Sheet 10: Coverage — NEW, Mosofin-specific**

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used / external source | Population and size | As-at date | Policy | `mock` | Gap |

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming:** `Forensic_Analysis_[Period]_[EntityName].xlsx`

Every file states which datasource and `display_name` it covers.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where the data does not
cover something — bank details, payroll registers, corruption indicators — **name the source required**
instead of estimating.

## Step 9 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

**This skill has the strictest persistence rule in the pack.**

On an explicit yes, persist **only** the **method**:

- **The tests in the standard screen** for this entity, and which ones can and cannot run here
- **The authorization threshold** used for the just-under-threshold test, with its effective date
- **The account map**: which accounts hold reserves, write-offs, refunds and manual-entry activity
- **The population definitions**: what "the disbursement population" means for this entity
- **The risk areas identified** as structurally vulnerable — by process, never by person
- **The escalation path and the authorized recipients** — roles, not names, wherever possible
- **The false-positive patterns already cleared** — expressed as a rule, not as a list of people: "vendors
  sharing an address with an employee where the relationship is a disclosed related party" is a rule;
  a name is not
- The replay recipe: the exact sequence of reads that produced each test's population

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist findings, flagged items, anomalies, suspicions, vendor or employee names, addresses, or
anything identifying a person.** Not in a skill bundle, not in a preference file, not in a note for next
time. **An indicator about an identifiable person, written down and carried forward, becomes an allegation
that nobody ever tested and nobody can rebut.** Some of the people on a red-flag list will have done nothing
wrong, and they will never know a file exists. **Persist the method; never the results.**

**Key every preference by datasource + entity `display_name`.** Write "quickbooks / Northbrook Trading —
authorization threshold 10,000 from 2025-04-01, reserves in 2400–2450, bank-match tests unavailable" — not
"threshold 10,000". Record the chosen **scenario** (single vs multi) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's** — and every anomaly, every flag and every list is state.

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One population per test.

**Multi-entity.** Steps 0–8 run **once per entity**, each call targeting exactly one `data_source_id`,
every flagged item carrying its entity's `display_name`. Then the cross-entity patterns, which are a real
category of scheme:

- **A vendor paid by more than one group company.** Legitimate for shared suppliers — and also the shape of
  a fictitious vendor billing twice. **Compare vendor masters across entities on name, address and phone**;
  the same anomaly in two entities is a stronger indicator than in one.
- **The same invoice paid by two entities.** A cross-entity duplicate, and one that no single entity's
  review will ever see. See `duplicate-invoice-detection`.
- **An individual appearing as an employee in one entity and a vendor in another** — invisible within either
  entity alone, readable across both.
- **Intercompany transfers as a disposal route.** Funds moved between group entities before leaving; a
  single-entity trace stops at the transfer. **Trace across entities**, and say where the trail leaves what
  you can read.
- **Weaker oversight in smaller subsidiaries.** Risk concentrates where segregation of duties is thinnest.
  **A group-level clean result driven by the parent's controls says nothing about a two-person subsidiary.**
- **Run each entity's tests separately and label every result with its entity.** A merged anomaly list
  across entities in different currencies and control environments is not interpretable.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each test's verdict per company
file — **and Sheet 9 records, per entity, which tests could not run at all.**
