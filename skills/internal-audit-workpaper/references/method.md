<!-- internal-audit-workpaper · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding) — Mosofin addition
- Step 1 — Plan the audit
- Step 2 — Understand the area
- Step 3 — Build the audit program
- Step 4 — Execute fieldwork and document workpapers
- Step 5 — Develop findings
- Step 6 — Rate findings by risk
- Step 7 — Agree management responses
- Step 8 — Structure the report
- Step 9 — Follow-up
- Step 10 — Output
- Step 11 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Never drop a task because no tool covers it.** Observation, inquiry and confirmation are legitimately
`[manual]` fieldwork, and naming their owners is part of the program.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding) — Mosofin addition

**Run after Step 1 and Step 2 in the sequence below** — planning and understanding come first in an audit,
and pulling data before knowing what you are testing is how audits become fishing expeditions. **But
establish what data exists during planning**, because it shapes what procedures are possible.

**Batch independent reads into one message.** Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical reads, depending on the area under audit:

- *`search_accounts`* — the chart of accounts and the accounts relevant to the area — usually **[auto]**
- *`get_general_ledger`* — **the transaction population for the area and period** — usually **[auto]**
- *`search_bills`* / *`search_purchases`* / *`search_invoices`* — **document-level populations** — usually
  **[auto]**
- *`search_journal_entries`* — manual entries, always worth examining — usually **[auto]**
- *`search_vendors`* / *`search_customers`* / *`search_employees`* — master data — usually **[auto]**
- *`get_profit_and_loss`* / *`get_balance_sheet`* — analytical comparatives — usually **[auto]**
- *`get_company_info`* — legal name, currency, year-end — usually **[auto]**

**Record for every read: the tool, the parameters, the entity and the as-at date.** This is the workpaper's
Source and Work Performed sections, and it is what makes the procedure re-performable.

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → **document a scope limitation**, name the evidence unavailable, and state its
  effect on the conclusion.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — **an audit conclusion drawn from fixture data is
worthless and potentially misleading to governance.** Stop and say so.

## Step 1 — Plan the audit

**Define the engagement** — **[manual]** throughout:

- **Objectives**: what the audit will assess — e.g. *"evaluate the effectiveness and efficiency of the
  procurement process and compliance with policy"*
- **Scope**: what's included and excluded, **period covered, locations**
- **Criteria**: the standards to audit against — **policies, regulations, control frameworks, good
  practice**
- **Risk assessment**: the risks in the area that justify the audit focus
- **Approach**: the procedures and how evidence will be gathered

**Planning focuses the audit on the highest-risk, most valuable areas.**

**Mosofin addition to scope**: **state which entities are in scope by `display_name`, and record any
excluded entity as a scope limitation.** Also state, in the approach, **which procedure types the workspace
can perform and which require fieldwork** — that is the approach, made concrete.

## Step 2 — Understand the area

**Document how the area / process works** — **[gated]**:

- **Process flow, key activities, systems, roles** — **[manual]**
- **Controls in place** — **[manual]**
- **Key risks** — what could go wrong relative to the objectives — **[manual]**
- **Relevant policies and requirements** — **[manual]**

**Confirm understanding — e.g. via walkthrough — before testing.**

**[auto]** contribution: **the system's shape corroborates the described process.** Which accounts are used,
which document types exist, what volumes flow through, which users appear, whether the dimensions are
populated. **Where the ledger contradicts the described process, that is worth resolving before fieldwork
begins** — it usually means the process document is out of date, which is itself a finding.

**A walkthrough remains `[manual]`.** Reading the data is not watching the work.

## Step 3 — Build the audit program

**The audit program is the set of procedures to meet each objective.** For each objective:

- **The risks / controls / requirements to test** — **[manual]**
- **The specific procedures** — **inspect, observe, re-perform, analyze, inquire, confirm** — **[gated]**,
  and see the mapping at the top of this file
- **Sample approach where applicable** — **[gated]**, and see below
- **The evidence to obtain** — **[gated]**
- **Who performs it** — **[manual]**

**A good program links every procedure to an objective — no procedure without a purpose, no objective
without coverage.**

**Mosofin additions to the program table — three columns:**

1. **Procedure type**, from the six.
2. **Verdict** — `[auto]`, `[gated]` or `[manual]` — which follows largely from the type.
3. **Population and approach** — **full population or sample**, and for a sample, **the method, size and
   basis**.

**On the sample approach specifically:** for each `[auto]` procedure, **ask whether a sample is needed at
all.** Where the population is readable and the test is computable, **test all of it and say so.** Reserve
sampling for procedures where the evidence is outside the system or the volume genuinely prevents it. **A
program that samples 25 items from a population you could have tested entirely is weaker than it needed to
be.**

**And check coverage against the `[manual]` half.** If every procedure for an objective is `[auto]`, ask
whether the objective is really covered — **effectiveness, efficiency and authorisation are rarely
answerable from data alone.**

## Step 4 — Execute fieldwork and document workpapers

**Perform the procedures, documenting each in a workpaper that meets the standard:**

- **Purpose**: what the procedure tests — **linked to the objective**
- **Source**: where the evidence came from
- **Work performed**: exactly what was done — sample selected, tests run
- **Results**: what was found, with evidence
- **Conclusion**: does the result meet the criteria?

**Workpaper quality standard: a reviewer (or another auditor) should be able to re-perform from the
workpaper and reach the same conclusion. Every conclusion is supported by documented evidence;
cross-reference to source documents.**

**Use clear referencing (indexing) so workpapers tie to the program and the report.**

**Mosofin form for an `[auto]` procedure** — this is what satisfies the re-performance standard:

| Workpaper element | What to record |
|---|---|
| **Purpose** | The objective and the assertion tested |
| **Source** | **The datasource, the entity by `display_name`, and the tool called** |
| **Work performed** | **The exact tool name and every parameter passed**, the population size, and whether it was full or sampled |
| **Results** | The output, the exception count, and the exceptions themselves |
| **Conclusion** | The auditor's conclusion against the criteria |

Plus **the as-at date and the `mock` status** of every read. **A workpaper recording "reviewed the ledger"
is not re-performable; one recording the tool, the parameters and the date is.**

## Step 5 — Develop findings

**Where work identifies a gap — actual vs. criteria — develop a finding using the standard structure**, the
**5 C's**: **condition-criteria-cause-consequence-corrective action**:

- **Condition**: **what is** — the actual situation found — **[gated]**; the `[auto]` evidence supports it
- **Criteria**: **what should be** — the standard, policy or expectation — **[manual]**
- **Cause**: **why the gap exists** — the **root cause** — **[manual]**
- **Consequence / Effect**: **the impact or risk**, quantified where possible — **[gated]**; **quantification
  is often `[auto]`**
- **Recommendation**: **what should be done to address the cause** — **[manual]**

**A finding without a root cause leads to recommendations that don't fix the real problem. Push to the
underlying cause.**

**Note where the split falls, because it is the shape of the whole skill:** **the workspace can establish
the condition and quantify the consequence. It cannot supply the criteria, and it cannot find the cause.**
Cause is about people, incentives, systems and design — **it is found by asking, not by querying.** A
finding built entirely from data will stop at the symptom, which is precisely what the edge cases warn
against.

## Step 6 — Rate findings by risk

**Assign each finding a risk rating** — e.g. high / medium / low — **based on:**

- **Likelihood** of the risk materializing
- **Impact / magnitude** if it does — **financial, operational, compliance, reputational**

**Ratings prioritize management's attention and remediation. Be consistent in the rating criteria.**

**[manual]** to rate; **[gated]** support: **the financial magnitude is frequently computable** — the value
of transactions affected, the exposure, the error rate extrapolated across the population. **A rating
supported by a quantified exposure survives challenge; one supported by judgment alone often does not.**

**Repeat findings rate higher** — see the edge cases. **[gated]**: where the same test was run in a prior
engagement, **re-running it is straightforward**, and **whether the exception persisted is a fact.**

## Step 7 — Agree management responses

For each finding — **[manual]** throughout:

- **Obtain management's response** — agreement, action plan, owner, target date
- **Where management disagrees, document both positions objectively**
- **Distinguish "accept the risk"** — a management decision to be recorded — **from remediation**

**This step is entirely a conversation with people.** Nothing here is derivable, and an audit that skips it
produces recommendations nobody owns.

## Step 8 — Structure the report

**Build the internal audit report** — **[gated]**:

- **Executive summary**: overall conclusion or opinion, key findings, overall risk rating
- **Background and scope / objectives**
- **Findings**: each with **condition / criteria / cause / consequence / recommendation, risk rating, and
  management response**
- **Overall assessment**: the auditor's conclusion on the area
- **Appendices**: detailed support as needed

**Tone is objective, factual, and constructive — internal audit adds value by improving the organization,
not just criticizing.**

**Mosofin additions to the report**: **state the scope limitations**, including any entity that could not be
read and any evidence that was unavailable; **state where conclusions rest on ledger data alone**, and
therefore what they do and do not cover — particularly completeness.

## Step 9 — Follow-up

**Establish follow-up on agreed actions** — **[gated]**:

- **Track remediation status against target dates** — **[manual]**
- **Validate that completed actions actually addressed the finding (re-test)** — **[gated]**, and **this is
  where a stored test definition pays off**: **re-running the identical query is exact, cheap and
  comparable.** "The same test, re-run on the same basis, now returns 0 exceptions against 43" is far
  stronger evidence of remediation than a management assertion that it was fixed
- **Report overdue / unresolved items to governance** — **[manual]**

**A re-test that uses a different method proves less than one that repeats the original.** **Store the test
definition** (Step 11) so the follow-up is genuinely a repeat.

## Step 10 — Output

Deliver the workpapers, report, and tracker:

**Workpaper package (`.xlsx`):**

**Sheet 1: Audit Plan** — objectives, scope, criteria, risk assessment, approach. Plus the Mosofin header:
workspace name; entities in scope by `display_name`; **excluded entities recorded as scope limitations**;
whether any read returned `mock` data.

**Sheet 2: Audit Program** — **each procedure linked to an objective, with method, sample, evidence,
performer.** Add **procedure type**, **verdict**, and **full population or sample with its basis**.

**Sheet 3: Workpapers Index** — **referenced workpapers with purpose, work performed, results,
conclusion.** For `[auto]` procedures, **work performed records the tool, the parameters, the entity and the
as-at date.**

**Sheet 4: Findings Register**

| Finding | Condition | Criteria | Cause | Consequence | Recommendation | Risk Rating | Mgmt Response | Owner | Target Date |

Add **Population tested** and **Exception rate**, and a **Repeat?** flag.

**Sheet 5: Follow-Up Tracker** — status of agreed actions, re-test results. **With the stored test
definition against each item**, so the re-test repeats the original.

**Sheet 6: Procedure Coverage — NEW, Mosofin-specific**

| Objective | Procedure | Type | Verdict | Population | Evidence source | Performer | Scope limitation? |

**Every `[manual]` row names a person.** This sheet is the honest statement of what the workspace did and
what the fieldwork must still cover — and it should show **at least some observe, inquire or confirm work
for any objective concerning effectiveness or authorisation.**

**Report document:**

**The structured internal audit report.**

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.
Offer the report as a Word document only where the host can make one; otherwise give it as text in the chat.

**File naming:** `Internal_Audit_[Area]_[YYYY]_[EntityName]`

`[EntityName]` is the company file's `display_name`, or the group name.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where the data does not
cover something — completeness, authorisation, effectiveness — **name the fieldwork required** instead of
concluding.

## Step 11 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The audit program for this area** — objectives, procedures, and the objective each links to. **The most
  valuable stored asset**, and it makes the next cycle a rerun rather than a rebuild
- **The test definitions** — for each `[auto]` procedure, **the exact tool, parameters and population
  definition.** This is what makes a follow-up re-test a genuine repeat
- **The criteria references** — which policy, which clause, which regulation. **By reference, not by
  content**
- **The risk rating scale** and its definitions, so ratings stay consistent across engagements
- **The account and dimension map** for the area
- **The audit universe entry** — the area, its risk assessment, its audit cycle
- **The `[manual]` fieldwork list** — which procedures need a person, and which role performs them
- **Known scope limitations** for this entity — evidence that is structurally unavailable
- The replay recipe: the exact sequence of reads that produced each population

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist findings, exceptions, populations, management responses or the names of individuals.**
Audit findings concern how identifiable people did their jobs. **A finding carried forward outside a formal
tracker, unrebutted and unclosed, becomes a permanent record nobody can answer** — the same reasoning as
`fraud-detection-and-forensics`. **Persist the program and the tests; never the results.**

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / Northbrook
Trading — procurement audit program v2, PO population from search_purchases, criteria: Procurement Policy
2025 §4, 3-tier rating scale" — not "procurement audit program v2". **Programs are built around a specific
entity's systems and accounts**, and applying one entity's program to another tests things that may not
exist there. Record the chosen **scenario** (single vs multi) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's.**

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged as a scope limitation** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One population per test, one conclusion.

**Multi-entity.** Steps 0–10 run **once per entity**, each call targeting exactly one `data_source_id`,
every population and finding carrying its entity's `display_name`. Then:

- **Ask whether this is one audit of a group process or several entity audits.** They produce different
  reports. A group process audit concludes on the process across entities; **an entity audit concludes on
  that entity**, and the two must not be blended.
- **The same test may not be possible in every entity.** Different tool policies, different chart
  structures, different dimension usage. **Record the verdict per entity**, and **an entity where a test
  could not run is a scope limitation for the group conclusion.**
- **Exception rates should be reported per entity as well as in total.** A group rate of 3% concealing one
  entity at 15% and four at 0% points straight at where the process has broken — **and that is usually the
  finding.**
- **Consistency across entities is itself an audit objective** in a group process audit: the same process
  operating differently in different entities is a control design issue.
- **Segregation of duties often breaks down in smaller entities** — see
  `fraud-detection-and-forensics`. A group conclusion driven by the largest entity's controls says nothing
  about a two-person subsidiary.
- **Do not aggregate populations across entities into one test.** Different charts, different currencies,
  different volumes. Run per entity, then summarise.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each procedure's verdict per
company file.
