<!-- model-auditor-financial-model-review · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the source (grounding) — Mosofin addition
- Step 1 — Freeze the review scope
- Step 2 — Source tie-out
- Step 3 — Formula integrity review
- Step 4 — Statement and schedule checks
- Step 5 — Scenario and sensitivity review
- Step 6 — Deliver issue log and pass / hold call
- Step 7 — Output (Mosofin addition)
- Step 8 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Never drop a task because no tool covers it.** The formula, statement and scenario reviews are `[manual]`
spreadsheet work and remain in the workflow in full.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the source (grounding) — Mosofin addition

**Runs as part of Step 2**, not before Step 1 — **freeze the scope first**, so you know which periods and
which entity to pull.

**Batch independent reads into one message** — the statements, the trial balances and the balances do not
depend on each other. **Pull every historical period the model contains in one go.**

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical batch, per in-scope entity:

- *`get_profit_and_loss`* **for each historical period in the model** — usually **[auto]**
- *`get_balance_sheet`* **at each historical period end, including the opening balance sheet** — usually
  **[auto]**
- *`get_trial_balance`* at the same dates — **for line-level mapping** — usually **[auto]**
- *`get_cash_flow_statement`* where available — **opening and ending cash** — usually **[auto]**
- *`get_general_ledger`* on **debt, equity and any line the model treats specially** — usually **[auto]**
- *`search_accounts`* — **the chart, for mapping model lines to accounts** — usually **[auto]**
- *`get_company_info`* — legal name, **currency, year-end** — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → **that tie-out target becomes OPEN**, and record why.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — **tying a model to fixtures produces a clean
tie-out that means nothing**, and this model is going to a lender, an investor or a board.

## Step 1 — Freeze the review scope

Before reviewing, document — **[manual]**:

- **Model file name and version**
- **Review date**
- **Intended use**
- **Tabs or sections in scope**
- **Source files provided**
- **Materiality threshold**
- **Whether the review is formula integrity only or full source tie-out**

**If the model will be changed during review, keep an issue log so every fix is traceable.**

**Mosofin additions to the frozen scope**: **the workspace and entity the tie-out runs against, by
`display_name`**; **the as-at date of every source read**; and **the model's own source vintage** if known.
**A review is a point-in-time statement about a specific file against specific books** — record both ends.

## Step 2 — Source tie-out

**Tie key historical and opening balances to source** — **and this is the `[auto]` step**:

- **Historical P&L lines to financial statements, TB, or accounting export** — **[auto]**
- **Balance sheet opening and historical periods to source** — **[auto]**
- **Cash flow opening and ending cash to source** — **[auto]**
- **Debt balances to debt schedules** — **[gated]**: **the balance is `[auto]`; the schedule is `[manual]`**
  — see `debt-and-covenant-tracking`
- **Share count and equity items to cap table or board-approved records** — **[manual]**, always. **The cap
  table is not on this surface** — consistent with `equity-compensation-accounting` and
  `financial-statement-builder`
- **Tax, working capital, capex, and payroll assumptions to source support where provided** —
  **[gated]**: **the historical actuals underlying each are `[auto]`**, which lets you test whether the
  assumption is consistent with history; **the support for the forward assumption is `[manual]`**

**Flag every figure as:**

- **TIED**: agrees to source
- **IMMATERIAL DIFF**: difference below threshold
- **OPEN**: source missing or not yet reconciled
- **FAIL**: material mismatch

**Mosofin notes on the four flags, because the mix changes:**

- **TIED becomes the common outcome and it is now evidenced** — record **the tool, the parameters and the
  as-at date** beside each tied figure, so the tie-out is reproducible rather than asserted.
- **OPEN should be rare** for anything the books hold. **Where it persists, it is because a read was
  unavailable or the item is genuinely external** — the cap table, a debt schedule, an assumption memo.
  **Say which.**
- **FAIL needs the mapping checked first.** A model line aggregating three accounts will not equal one
  account. **Confirm the mapping before recording a material mismatch** — a false FAIL is worse than a
  missed one, because it destroys trust in the rest of the review.
- **A fifth outcome exists here and deserves its own label: STALE.** **The figure ties to the model's source
  vintage but not to the books today.** That is neither a modelling error nor agreement — **it means the
  history moved**, and the fix is a refresh, not a formula. **Report it separately**; treating it as FAIL
  misattributes the cause.

**Tie every historical period, not a sample.** The cost is one batch of reads.

## Step 3 — Formula integrity review

**Inspect formulas for** — **[manual]** throughout; **this is spreadsheet inspection and the workspace has
no part in it**:

- **Broken links or external workbook dependencies**
- **Hardcoded constants inside formulas**
- **Formula inconsistencies across rows or periods**
- **Circular references**
- **References to hidden, deleted, or obsolete tabs**
- **Forecast formulas pointing to historical source tabs unexpectedly**
- **Manual overrides in calculated sections**
- **Sign convention inconsistencies**
- **Mixed units, currencies, or period cadences**

**Hardcoded constants inside formulas are acceptable only when they are deliberate, labeled, and immaterial
or standard constants. Otherwise, move them to assumptions.**

**One connection to Step 2 worth making**: **a hardcode in a historical column is frequently a figure
someone typed to make the model agree to a source.** **The tie-out finds the number; the formula review finds
how it got there.** Cross-reference the two — a hardcoded historical that ties, and a formula-driven
historical that does not, tell very different stories about the model's construction.

## Step 4 — Statement and schedule checks

**Check that** — **[manual]**, internal to the model:

- **Balance sheet balances in every period**
- **Cash flow ending cash links to balance sheet cash**
- **Retained earnings rolls forward**
- **Debt rolls forward and interest is calculated from debt assumptions**
- **Fixed assets roll from opening cost and accumulated depreciation through capex, depreciation, disposals,
  and closing balance**
- **Working capital movements reconcile to balance sheet changes**
- **Tax expense, cash taxes, and deferred taxes are internally consistent when modeled**
- **Valuation cash flows tie to operating model cash flows if a valuation tab is included**

**Any balance break, circular reference, or material source mismatch is normally a HOLD.**

**[auto]** contribution, and it is limited but real: **the opening positions these roll-forwards start
from are tie-out targets from Step 2.** **A roll-forward that is internally consistent but starts from a
wrong opening balance is wrong throughout** — and the internal check will not catch it. **Test the openings
against source; test the roll internally.** Both, separately.

## Step 5 — Scenario and sensitivity review

**Test that scenario controls work** — **[manual]**:

- **Base, downside, upside, or custom cases switch correctly**
- **Scenario-driven assumptions update outputs**
- **Sensitivity tables reference the intended variables and outputs**
- **Data tables or equivalent sensitivity tools recalculate correctly**
- **No scenario produces impossible outputs without warning**, such as negative working capital days unless
  intentional

**[auto]** context: **historical ranges are readable**, which gives a reasonableness frame for the scenarios.
**A downside case with margins better than any month in the last three years, or an upside assuming
collection days the entity has never achieved, is worth a comment** — not a formula error, but a
credibility one, and the reviewer is the last person who can raise it.

## Step 6 — Deliver issue log and pass / hold call

**Create an issue log with** — **[gated]**:

- **Issue ID**
- **Severity: Critical / High / Medium / Low**
- **Location**: tab, row, column, or named section
- **Description**
- **Impact**
- **Suggested fix**
- **Owner or next action**
- **Status: Open / Fixed / Accepted / Not applicable**

**Final call:**

- **PASS**: **no critical or high issues remain, key figures tie, and checks clear**
- **PASS WITH COMMENTS**: **only low or accepted medium issues remain**
- **HOLD**: **any critical / high issue remains, including balance breaks, circular references, broken
  links, material source mismatches, or unsupported key assumptions**

**Mosofin additions to the log**: **a Source column** — where a tie-out issue is logged, **name the tool, the
parameters and the as-at date**, so the issue is reproducible by whoever fixes it. And **treat STALE
separately from FAIL** in severity: **a stale historical is usually High and fixed by refreshing; a genuine
material mismatch may be Critical and means something is wrong in the model or the books.**

**The pass / hold call is the reviewer's.** The workspace supplies evidence for one input to it.

## Step 7 — Output (Mosofin addition)

The original specifies deliverables in prose; produce them as a package.

**Document: Review Memo** — scope, approach, findings, and the **pass / hold call with its reasoning**.

**Workpaper (`.xlsx`):**

**Sheet 1: Review Scope** — the frozen scope from Step 1, **plus the workspace, entity `display_name`,
source as-at dates, and the model's source vintage**.

**Sheet 2: Source Tie-Out** — every figure tied, **with TIED / IMMATERIAL DIFF / OPEN / FAIL / STALE**, the
model location, the source figure, the difference, **and the tool call behind it**.

**Sheet 3: Formula Integrity Exceptions** — the nine checks, with locations.

**Sheet 4: Statement and Schedule Checks** — the eight checks, per period, pass or fail.

**Sheet 5: Scenario and Sensitivity Tests** — the five tests, plus any historical-plausibility comments.

**Sheet 6: Issue Log** — the eight fields, with the Source column.

**Sheet 7: Coverage — NEW, Mosofin-specific**

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used / external source | As-at date | `mock` | Gap |

**Steps 3, 4 and 5 read `manual` throughout.** That is correct and expected — **this sheet exists so nobody
reads a complete tie-out as a complete model review.**

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.
Offer a Word document only where the host can make one; otherwise give the text in the chat.

**File naming (Mosofin addition — the original specifies none):**
`Model_Review_[ModelName]_[YYYY-MM-DD].xlsx`

**Grounding:** every source figure traces to a tool result in this conversation; every model figure traces to
its cell reference. End with a single **Data sources** line. Where a tie-out could not be performed, **it is
OPEN with its reason**, never assumed tied.

## Step 8 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The model-line-to-account mapping** — **the most valuable stored asset here**, because it is what
  prevents false FAILs and it is rebuilt painfully every review
- **The materiality basis** for the IMMATERIAL DIFF threshold, and how it is set for each intended use
- **The tie-out target list** — which figures are checked for this model type
- **The severity conventions** — what counts as Critical, High, Medium, Low here
- **The standard checklist** for Steps 3, 4 and 5, including any model-specific checks this team adds
- **The entity or group the model represents**, and whether it is consolidated
- **Known accepted issues** — expressed as rules: "the hardcoded tax rate in row 88 is a deliberate,
  labelled statutory constant" — **not as a list of unresolved findings**
- The replay recipe: the exact sequence of reads that produced the source figures

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist model contents, financial figures, tie-out results, issue logs or the pass / hold call.**
All state — **and a model under review is frequently confidential**, whether it supports a transaction, a
financing or a board decision. **Persist the mapping and the method; never the model or its findings.**

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / Northbrook
Group — consolidated model, Revenue maps to 4000–4090, materiality 50k for lender models, opening BS at
2025-12-31" — not "Revenue maps to 4000–4090". **Mappings are chart-specific and model-specific**, and
applying one to another produces false FAILs across the board. Record the chosen **scenario** (single vs
multi, consolidated) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's.**

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity model.** The tie-out runs against one `data_source_id`. Straightforward.

**Consolidated model.** **The model's historicals are consolidated figures**, so:

- **Tie out against consolidated source**, not the parent's books and **not a sum of the entities'.**
  **Intercompany must be eliminated first** — see `consolidation-and-eliminations` — or **every revenue and
  cost line will FAIL by the intercompany amount**, and the reviewer will report a model error that is
  actually a source-preparation error.
- **A disconnected group member means the source is incomplete**, so a full tie-out is not possible. **Those
  lines are OPEN, not TIED**, and the pass / hold call must reflect that.
- **Ask whether the model consolidates or works from consolidated inputs.** A model that performs its own
  consolidation has an additional set of Step 4 checks — **the eliminations themselves** — which are
  internal to the model and `[manual]`.
- **Currency**: **a group model in one currency built from entities in several** contains translation the
  books may perform differently. **Confirm the rate basis before flagging differences as FAILs** — see
  `foreign-currency-translation-asc830`.
- **Non-controlling interests and equity items** are a common source of consolidated tie-out differences and
  **depend on the cap table, which is `[manual]`.**

Capability is checked **per entity** at Gate 2; the coverage sheet shows each tie-out target's verdict per
company file.
