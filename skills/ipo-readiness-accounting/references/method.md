<!-- ipo-readiness-accounting · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding) — Mosofin addition
- Step 0b — Measure what is usually asserted (Mosofin addition)
- Step 1 — Assess gaps vs public-company requirements
- Step 2 — Close acceleration plan
- Step 3 — Accounting policy memo library
- Step 4 — Equity and EPS readiness
- Step 5 — SOX / ICFR readiness
- Step 6 — Reporting and disclosure process
- Step 7 — Output (Mosofin addition)
- Step 8 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Never drop a task because no tool covers it.** The equity, control and memo workstreams are legitimately
`[manual]`, and naming their owners and durations is what a roadmap is for.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding) — Mosofin addition

**Batch independent reads into one message** — the historical statements, the journal population and the
account structure do not depend on each other. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`get_profit_and_loss`* and *`get_balance_sheet`* **for each of the last three to four years** — **the
  comparable-data check** — usually **[auto]**
- *`search_journal_entries`* **with posting dates**, over several periods — **the close-timing and
  manual-entry population** — usually **[auto]**
- *`get_general_ledger`* — **movement by posting date versus transaction date** — usually **[auto]**
- *`search_accounts`* — **the chart, and whether it has changed across the comparable years**; **suspense
  and uncategorized accounts** — usually **[auto]**
- *`get_trial_balance`* at each year end — usually **[auto]**
- *`get_company_info`* — **legal name, year-end, industry** — usually **[auto]**

**Pull several periods deliberately.** **A single close tells you nothing about cadence**; three or four
show the pattern, and the pattern is what a readiness assessment needs.

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — **a readiness assessment on fixtures measures a
fictional company**, and it would be relied on for a timetable and a budget.

## Step 0b — Measure what is usually asserted (Mosofin addition)

**Run before Step 1**, because these measurements are the evidence Step 1's gap assessment should rest on.
**[auto]** throughout.

**1. Close speed.** For each of the last several periods: **the distribution of posting dates relative to
period end.** Report **the working day by which 50%, 80% and 100% of the period's entries were posted**, and
**the date of the last adjusting entry.** Compare against the public-company requirement the user is
targeting.

**2. Manual entry profile.** **The proportion of period-end movement arriving by manual journal**, by count
and by value, and **how it trends.** Also **the largest manual entries** and which accounts they touch.
**Every one of these becomes an ICFR control** — the number is the size of the Step 5 workstream.

**3. Comparable-data depth.** **How many complete years the system holds** on a consistent chart and basis,
and **where any discontinuity falls** — a chart restructure, an entity change, a basis change. Compare
against the years that must be presented.

**4. Period integrity.** **Entries posted into periods that were already reported**, prior-period
adjustments, and **whether prior-year comparatives in the system still match what was previously
presented.** See `financial-statement-builder`, where the same check appears from the reporting side.

**5. Reconciliation hygiene.** **Suspense and uncategorized account balances, with ages**, and **accounts
with no movement that nonetheless carry a balance.**

**Present these five as measurements, with their method stated**, and let the gap assessment in Step 1 use
them. **A roadmap built on measured close timing is a different document from one built on an interview.**

## Step 1 — Assess gaps vs public-company requirements

**Workstreams** — each with its verdict:

- **Close speed and discipline** — monthly / quarterly cadence — **[gated]**: **measured in Step 0b**; the
  target and the process changes are `[manual]`
- **Audit readiness and PCAOB expectations** — **[gated]**: **period integrity and evidence availability are
  measurable**; the audit standard and the auditor's expectations are `[manual]`
- **ICFR / SOX program and evidence** — **[manual]**; see `sox-controls-design-and-testing`. **[auto]**
  input: the manual-entry profile sizes it
- **Accounting memos for complex areas** — **[gated]**: **which areas apply is partly readable** from the
  chart and the balances, exactly as in `gaap-vs-ifrs-conversion`; the memos themselves are `[manual]`
- **Disclosure readiness (S-1 / 10-Q / 10-K)** — **[manual]**
- **Equity accounting and EPS** — **[manual]**; the cap table is not here

**Report the gap per workstream with a size and a basis**, not a colour. "Close currently completes on day
23 against a day-8 target" is a gap; "close: amber" is not.

## Step 2 — Close acceleration plan

- **Standardize reconciliations** — **[gated]**: **which accounts are unreconciled or carry ageing
  balances is `[auto]`**; the standard is `[manual]`
- **Automate recurring entries** — **[auto]** to identify: **entries that repeat every period with the same
  accounts and similar amounts** are the automation candidates, and they are readable with their frequency
  and value
- **Tighten cutoff policies** — **[auto]** to test: **transactions posted after period end but dated within
  it**, and the reverse
- **Improve subledger-to-GL tie-outs** — **[gated]**; see `inventory-to-gl-reconciliation` and
  `balance-sheet-reconciliations` for the same split
- **Build a close calendar and RACI** — **[manual]**, and **the primary deliverable of this step**

**Sequence by measured impact.** **The last adjusting entry's date from Step 0b tells you what is actually
holding the close open** — and it is frequently one or two accounts, not the whole process. **Automating
recurring entries that were never on the critical path saves nothing.**

## Step 3 — Accounting policy memo library

**Prioritize memos for** — **[manual]** to write, **[gated]** to scope:

- **Revenue recognition** — see `revenue-recognition-asc606`
- **Stock compensation** — see `equity-compensation-accounting`
- **Leases** — see `lease-accounting-asc842-ifrs16`
- **Business combinations** — see `business-combinations-asc805`
- **Income taxes** — see `corporate-tax-provision-asc740`
- **Debt and derivatives** — see `debt-and-covenant-tracking` and `derivatives-and-hedging-asc815`

**Mosofin addition — scope the library from the accounts.** **[auto]**: **read the chart and the balance
sheet to see which of these six areas are actually live for this entity.** No lease liability, no
acquisitions, no derivatives — then those memos are lower priority or unnecessary, and **saying so with
evidence saves real effort.** The same scoping technique as `gaap-vs-ifrs-conversion`, and it works here for
the same reason.

**Report the areas ruled out and why**, so nobody re-raises them later.

## Step 4 — Equity and EPS readiness

- **Validate cap table accuracy** — **[manual]**, always. **The cap table is not on this surface**
- **Identify complex equity instruments** — **[gated]**: **preferred stock, convertible notes and warrants
  leave balance-sheet traces**, so their *existence* is often readable; **their terms are not**, and the
  terms are what makes them complex
- **Ensure 409A history supportable** — **[manual]**; valuations
- **Build diluted EPS model** — **[manual]**; **weighted average shares and dilutive instruments both come
  from the cap table**

**This is the workstream the workspace helps least with, and it is frequently the one that delays the
timetable.** **Say so early.** Convertible instruments, down-round provisions and historical option pricing
routinely surface late and consume months. **[auto]** contribution is limited to flagging that instruments
exist — which is still worth doing, because an unflagged convertible note is a worse surprise.

## Step 5 — SOX / ICFR readiness

- **Identify key processes and controls** — **[manual]**; see `sox-controls-design-and-testing`
- **Document narratives and walkthroughs** — **[manual]**
- **Remediate segregation-of-duties issues** — **[gated]**: **some patterns are visible** — the same user
  creating and approving, or entering both sides of a process — **but the user data is limited and shared
  logins break the link.** **Surface patterns; do not conclude**
- **Implement evidence retention** — **[gated]**: **a Mosofin read is repeatable evidence and can be
  documented as such** — see `internal-audit-workpaper` — **but it is not a retained record.** Retention is
  a systems and policy matter

**Mosofin sizing input, and it is the useful one:** **the manual-entry count from Step 0b is the approximate
size of this workstream.** Each recurring manual entry becomes a control with a preparer, a reviewer,
evidence and a test. **A close with 200 manual journals a month has a materially larger ICFR programme than
one with 20**, and that difference drives both cost and timeline.

## Step 6 — Reporting and disclosure process

- **Implement tie-out discipline** — **[gated]**: **the cross-statement tie-outs are `[auto]`** — see
  `financial-statement-builder`, which specifies all seven
- **Draft disclosure checklists** — **[manual]**
- **Establish review / certification workflow** — **[manual]**, and note that **certification is a personal
  legal obligation of named officers**, which changes how the review process must be designed

## Step 7 — Output (Mosofin addition)

The original lists deliverables but does not specify a document. Produce one.

Deliver an `.xlsx` workpaper, and where a narrative roadmap is wanted, a document alongside it
(where the host can make one):

**Sheet 1: Readiness Roadmap with Timeline** — workstreams, phases, dependencies, target dates. **The
primary deliverable.** Plus the header block: workspace name; the **intended registrant** by `display_name`;
excluded company files; whether any figure rests on `mock` data; **and whether a reorganisation is
pending**.

**Sheet 2: Measured Baseline — NEW, Mosofin-specific** — the five Step 0b measurements, **with their method
and the periods measured**, and the target for each.

**Sheet 3: Gap Assessment by Workstream** — the six workstreams, **each gap stated with a size and a
basis**, and its verdict.

**Sheet 4: Workstream Deliverables and Owners** — every deliverable, its owner, its effort, its dependency.
**`[manual]` workstreams name a person or a role.**

**Sheet 5: Close Calendar + RACI** — the target close, day by day, with responsibilities.

**Sheet 6: Memo Library Index** — the six areas, **which are live for this entity with the evidence**,
priority, owner, status.

**Sheet 7: SOX Readiness Plan and Evidence Framework** — processes, controls, evidence, **sized against the
manual-entry profile**.

**Sheet 8: Coverage — NEW, Mosofin-specific**

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used / external source | As-at date | `mock` | Gap |

**The equity and control rows read `manual` with owners.** In a roadmap skill **that is the deliverable, not
a shortfall.**

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.
Offer a Word document only where the host can make one; otherwise give the text in the chat.

**File naming (Mosofin addition — the original specifies none):**
`IPO_Readiness_[YYYY-MM]_[EntityName].xlsx`

Every file states which datasource and `display_name` it covers.

**Grounding:** every measurement traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where the data does not
cover something — the cap table, audit status, the control environment — **name the source required**
instead of assessing it.

## Step 8 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The roadmap structure**: workstreams, phases, dependencies, target dates
- **The workstream owners** — by role wherever possible
- **The measurement definitions** — how close speed, manual-entry proportion and period integrity are
  measured here, **so each re-measurement is comparable.** **Not the measurements**
- **The target close calendar and RACI**
- **The memo library index** — which areas are live, which were ruled out and why, and their priority
- **The account map**: suspense and uncategorized accounts, the accounts holding the close open, the
  recurring-entry candidates
- **The intended registrant** and the group structure assumed
- **The years requiring audit** and their status at last check
- The replay recipe: the exact sequence of reads that produced the baseline measurements

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist financial figures, the measurements themselves, cap table data, valuations or any
IPO-timetable specifics.** **An intention to go public, and the timing of it, is material non-public
information** — it does not belong in a stored skill bundle. **Persist the method and the structure; never
the state or the plan's confidential specifics.**

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / Northbrook
Technologies — registrant, close measured on journal posting date vs period end, suspense 9990, live memo
areas: revenue, stock comp, leases" — not "close measured on posting date". **Measurement definitions depend
on this entity's chart**, and applying them elsewhere measures something different. Record the chosen
**scenario** (single vs multi, and the registrant) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's** — and **every readiness measurement is state by design**, since the purpose is to watch it
move.

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`, assessed as the registrant.

**Multi-entity.** Steps 0–7 run **once per entity**, each call targeting exactly one `data_source_id`, every
measurement carrying its entity's `display_name`. Then the points specific to an IPO:

- **Establish the registrant and the reporting entity.** **The financial statements in the filing are the
  registrant's, consolidated** — so **readiness is a group question, and the group's close is only as fast
  as its slowest subsidiary.** Measure close speed per entity; **the group close cannot beat the last one to
  report.**
- **A pre-IPO reorganisation changes the answer.** Assessing the current structure when a holding company is
  about to be inserted, or entities carved out, **wastes most of the work.** Ask before measuring.
- **Consolidation itself is a close workstream**, and frequently the slowest part. See
  `consolidation-and-eliminations` and `intercompany-reconciliation` — **intercompany mismatches that a
  private group tolerates for a quarter cannot survive a 40-day filing deadline.**
- **Every subsidiary needs the same discipline**, and **the weakest entity sets the ICFR programme's
  scope** — a small subsidiary with two people has segregation-of-duties problems the parent's controls do
  not cure.
- **Comparable-data depth must hold across the group**, not just at the parent. An entity acquired two years
  ago may not have the history the filing needs.
- **Policies must be uniform across entities** for consolidated reporting, and differences are a
  remediation item — see `gaap-vs-ifrs-conversion` where the same issue appears.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict per company
file.
