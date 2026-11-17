<!-- xbrl-tagging-checklist · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

## Contents

- How to read the verdicts
- Inputs
- Workflow
- Step 1 — Build the tag map
- Step 2 — Extensions governance
- Step 3 — Dimensional tagging
- Step 4 — Calculation and consistency checks
- Step 4b — Derive the expected calculation relationships *(Mosofin addition)*
- Step 5 — Validation workflow
- Outputs
- Output Quality Standards
- Seed to evolved: what happens on the first real run
- Anti-patterns


## How to read the verdicts

- **`[auto]`** — Mosofin can do this from live reads, unattended.
- **`[gated]`** — the gateway asks first. Explain, get consent, re-invoke with `approved=true` (**reads only — never for a write**) and the `data_source_id`.
- **`[manual]`** — not on this surface, or not a machine's judgment. **The step stays. The user performs it.**

**Everything here is a reference and a checklist.** The gateway is read-only. **Mosofin selects no element, creates no extension, tags nothing, runs no validation and files nothing.**

---

## Inputs

All four preserved.

| Input | Format | Required | Mosofin source | Verdict |
|---|---|---|---|---|
| **Filing draft** | Financials + notes + MD&A sections tagged | **Required** | **Not readable by Mosofin.** | `[manual]` |
| **Taxonomy version** | US GAAP taxonomy year/version | **Required** | **Not on this surface** — an external published artefact | `[manual]` |
| Prior filing tags | Previous tag map, if any | Recommended | Not in the books; **persist it** | `[manual]` |
| Validation tool output | EDGAR / validator errors and warnings | Recommended | **Mosofin does not run validation** | `[manual]` |

**Note that none of the four inputs is a ledger read.** That is the honest position, and it is why the contribution sits in Step 4 rather than in the inputs.

---

## Workflow

### Step 1 — Build the tag map

**`[manual]`.** Element selection requires the taxonomy and the document.

> **For each statement line and footnote table: select the most specific standard tag.**

**"Most specific" is the operative instruction.** A generic element where a specific one exists degrades comparability — which is the entire purpose of XBRL — without producing any validation error. **It is a quality failure that passes validation**, per the second near-substitute.

**Confirm**, all three preserved:

| Property | Note | Verdict |
|---|---|---|
| **Balance type** (debit/credit) | Determines sign handling — see Step 4 | `[manual]` from the taxonomy; **`[auto]` for the ledger's own natural balance**, which is a useful cross-check |
| **Period type** (instant/duration) | **Balance sheet items are instants; income and cash flow items are durations.** Mismatching them is a structural error. | `[manual]` from the taxonomy; **`[auto]` for which the underlying account is**, which is unambiguous in a ledger |
| **Data type** (monetary, shares, percent) | Shares and percentages are not monetary and must not be tagged as such | `[manual]`; **`[auto]` for monetary versus non-monetary in the accounts** |

**The `[auto]` contributions here are corroborations, not selections.** **A ledger knows unambiguously whether a figure is a balance or a flow, and what its natural sign is** — so where a chosen tag's period type or balance type contradicts the underlying account, that is a detectable inconsistency. It does not tell you which tag to choose; it tells you when the one chosen does not fit the thing being tagged.

---

### Step 2 — Extensions governance

**`[manual]`, entirely — and it is the substantive quality issue in XBRL.**

> **Use an extension only when:**
> - **No appropriate standard tag exists**
> - **The concept is genuinely company-specific**

**If using extensions**, all three rules preserved:

- **Anchor extensions to the closest standard element**
- **Maintain consistent naming conventions**
- **Minimise extension proliferation**

**Why this matters more than it appears to.** XBRL exists so that filings can be **compared by machines across companies.** **Every extension is a concept only this company uses**, and a filing heavy with extensions is one a consumer cannot compare to anything — **which defeats the purpose while passing every validation check.**

**Extensions are also the easy way out.** Where a standard element nearly fits but not exactly, creating an extension is faster than deciding whether the standard element is appropriate. **The governance exists to resist that**, and it is a review discipline rather than a technical control.

**Anchoring is the mitigation** — it tells a consumer which standard concept the extension most resembles, restoring some comparability. **An unanchored extension is opaque.**

**Mosofin contributes nothing to this step**, and should not pretend otherwise. **The one adjacent observation worth making**: where the accounts contain a genuinely unusual caption that has required an extension before, **that is a stable fact worth persisting** — see the lifecycle section — so the same decision is not re-litigated quarterly.

---

### Step 3 — Dimensional tagging

`[manual]` to tag; **`[auto]` for three of the five dimensions and for the reconciliation.**

> **Apply dimensions for:**

| Dimension | Mosofin | Verdict |
|---|---|---|
| **Segments** | **`[auto]` where segments are a dimension in the book** — the same binary as `segment-reporting` | Conditional |
| **Product lines** | **`[auto]` where item or class detail exists** | Conditional |
| **Geography** | **`[auto]` where customer or transaction country is recorded** — and **the attribution basis matters**, per `segment-reporting` | Conditional |
| **Debt tranches** | `[auto]` where tranches are separate accounts; **`[manual]` where one account holds several** | Conditional |
| **Share classes** | **`[manual]` — no cap table on this surface** | `[manual]` |

> **Ensure dimensions reconcile to totals.**

**`[auto]` on the ledger side, and this is a real check.** Where the dimensions exist in the book, the dimensional breakdown sums to the total by construction — **so Mosofin can supply both the members and the total, and any failure to reconcile in the tagged data is a tagging error rather than an accounting one.**

**And the caveat from `segment-reporting` applies**: where the dimensional analysis is assembled outside the accounts, **it will not reconcile by construction**, and the reconciliation is a genuine test. **Say which situation applies**, because it changes what a difference means.

**Share classes are `[manual]`** for the reason that recurs throughout this pack — the equity compensation accounting, `statement-of-equity-changes`, `sec-10q-10k-prep`. **And the EPS check in Step 4 depends on the same absent data.**

---

### Step 4 — Calculation and consistency checks

**The step where Mosofin contributes.** All four checks preserved.

| Check | Verdict | What Mosofin supplies |
|---|---|---|
| **Confirm calculation relationships for roll-forwards and subtotals** | **`[auto]` for the expected relationships** — see Step 4b | The arithmetic the accounts actually embody |
| **Verify EPS and share counts align** | **`[manual]` — no cap table on this surface** | Nothing. Flag it. |
| **Validate sign conventions** (negatives versus credits) | **`[auto]` for the natural balance** of every underlying account | The sign each figure carries in the accounts |
| **Ensure the same concept is tagged consistently across sections** | `[manual]` — **requires reading the document** | The authoritative value, so a figure appearing in three places can be checked against one reference |

#### On sign conventions, which cause a disproportionate share of errors

**XBRL sign handling is a recurring source of error** because it combines two things that both invert: **the element's balance type** (debit or credit) and **the presentation sign** (whether a figure is shown in parentheses in the document).

**A credit-balance element tagged with a negated presentation, carrying a figure already shown as negative in the statements, can end up doubly inverted** — and the resulting instance may validate cleanly while reporting an expense as income.

**`[auto]` supplies the unambiguous half**: **what sign the figure carries in the ledger, and whether the account is naturally a debit or a credit.** That is the ground truth against which the tagged sign can be checked, and it removes the part of the problem that is a matter of fact rather than of presentation.

#### On consistency across sections

`[manual]` to check, **`[auto]` to make checkable.** The same figure commonly appears in the primary statements, in a note, and in MD&A. **Tagging them with different concepts, or with different values, is a defect** — and it is exactly what `sec-10q-10k-prep`'s final read-through looks for on the human-readable side.

**Mosofin supplies one authoritative value per figure**, so all three occurrences are checked against a single reference rather than against each other.

---

### Step 4b — Derive the expected calculation relationships *(Mosofin addition)*

**`[auto]`, and it is the contribution the original does not have.**

An XBRL **calculation linkbase** asserts arithmetic: that certain elements sum to a total, that a roll-forward's components sum to its closing balance. **Those relationships are structural facts about the accounts**, and the accounts know them.

`[auto]` can produce the expected set directly:

| Relationship | Source |
|---|---|
| **Subtotal compositions** | Which accounts roll into each statement subtotal — **the chart's own hierarchy** |
| **Roll-forwards** | Opening + movements = closing, for every account requiring one — fixed assets, equity components, allowances, provisions, debt |
| **Statement totals** | Assets = liabilities + equity; revenue less costs to net income; cash flow's three sections to the net movement |
| **Dimensional sums** | Members to total, where dimensions exist |

**Hand this to the tagger as a specification.** It is more reliable than reconstructing the relationships from the document, and **it is produced from the same source the figures came from** — so a calculation inconsistency in the instance points to a tagging error rather than an ambiguity about what should sum to what.

**Two caveats.** **The taxonomy's calculation relationships are its own** and may not match the entity's chart structure exactly — this is a specification of what the accounts do, not of what the taxonomy requires, and where they differ, the taxonomy governs the tagging. And **calculation linkbases do not cover everything**: dimensional aggregations and some note disclosures are outside their scope. **This is an input to Step 4, not a replacement for it.**

---

### Step 5 — Validation workflow

**`[manual]`, all three steps. Mosofin runs no validation.**

- **Run pre-validation in the tagging tool** — `[manual]`; a tool Mosofin does not have
- **Resolve EDGAR errors (must-fix) and assess warnings** — `[manual]`
- **Perform independent reviewer sign-off** — `[manual]`

**The distinction between errors and warnings is preserved and matters**: errors block; **warnings are assessed, not ignored.** A filing accepted with unexamined warnings has passed a machine check and skipped a judgment.

**And the reviewer sign-off is the control that catches what validation cannot** — per the second near-substitute, **a wrong element choice validates perfectly.** The reviewer is looking for the thing the machine is structurally unable to see, which makes the sign-off substantive rather than procedural.

**`[auto]` contributes one thing to the reviewer's work**: the reference schedule from Step 4, so the review compares tagged values to the accounts rather than to the document they were taken from.

---

## Outputs

All four of the original's outputs preserved, plus two additions.

**Tag Map Template**
Statement line or footnote table, selected element, balance type, period type, data type, dimension members, prior-period tag. **`[manual]` for the elements; `[auto]` for the underlying account reference and its natural balance and period type**, as the corroboration in Step 1.

**Extensions and Anchoring Log**
Each extension, why no standard element fitted, the anchor element, the naming convention applied. **`[manual]`, entirely** — and **persisted**, so the same extensions are used consistently period to period.

**Validation Checklist**
Pre-validation run, errors resolved, warnings assessed with conclusions, reviewer sign-off. **`[manual]`.** Every line has a name and a date.

**Reviewer Sign-Off Checklist**
`[manual]`. **With the Step 4 reference schedule attached**, so the review is against the accounts.

**Reference Schedule** *(Mosofin addition)*
| Statement line | Ledger value (current) | Ledger value (comparative) | Natural balance | Instant/duration | Source accounts |
|---|---|---|---|---|---|

**`[auto]`, and it is what this skill contributes.** One authoritative value per figure, both periods, with its sign and its type — the reference every tie-out in Step 4 runs against. **Marked as information produced by the entity**, per the third near-substitute, with the queries recorded.

**Expected Calculation Relationships** *(Mosofin addition)*
The Step 4b specification.

**Coverage and Provenance** *(Mosofin addition)*
The mandatory coverage sheet.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

File naming: `XBRL_Tagging_[YYYY-Q#]_[EntityName].xlsx`

Registrant `display_name` on every sheet, **and whether the figures are consolidated or component-level.** If any read returned `mock: true`, say so in the file name and at the head of the reference schedule.

---

## Output Quality Standards

*(A Mosofin addition — the original has no Output Quality Standards section.)*

- **The taxonomy version is stated**, and confirmed current for the filing year.
- **The reference basis is stated** — consolidated or component-level.
- **The most specific standard element is selected**, and a generic substitute is treated as a defect even though it validates.
- **Every extension is justified, anchored and named consistently**, and the extension count is compared to the prior filing.
- **Balance type, period type and data type are confirmed against the underlying account**, not only against the taxonomy.
- **Every tagged figure is tied to the reference schedule**, current and comparative.
- **Comparatives reflect any restatement**, not the originally-filed figure.
- **Sign conventions are checked against the ledger's natural balance.**
- **Dimensional members reconcile to totals**, with the basis stated.
- **The EPS and share-count check is marked as requiring the cap table**, never left blank.
- **Calculation relationships are specified from the accounts** and reconciled to the taxonomy's own.
- **Errors are resolved and warnings are assessed with a recorded conclusion**, not ignored.
- **The independent reviewer signs off**, and the review is against the accounts rather than the document.
- **The reference schedule is re-run immediately before filing.**
- **File naming consistent.**

---

## Seed to evolved: what happens on the first real run

**What must never be frozen into a seed:** the capability map — Gate 2 reads it fresh — **and the taxonomy version**, which changes annually.

**What is worth persisting into the workspace-scoped skill:**

1. **The tag map.** **By far the most valuable artefact here** — established once, reused every quarter, and the reason quarter two takes a fraction of quarter one. Persist it with the taxonomy version it was built against, so a taxonomy update prompts a review rather than a silent carry-forward.
2. **The account-to-statement-line mapping**, which is what lets the reference schedule build itself.
3. **The extensions log with justifications and anchors** — so the same concepts get the same extensions, and so proliferation is visible over time.
4. **Which dimensions are ledger-native and which are assembled outside**, since it changes what a reconciliation difference means.
5. **The expected calculation relationships**, refreshed when the chart changes.
6. **Warnings previously assessed and accepted, with the reasoning**, so the same warning is not re-assessed from scratch each quarter.
7. **Who reviews, and what they need.**

Persist through `create_skill`, scoped to the workspace. **Client facts belong in a client-scoped skill, never back in the seed.**

**The evolved version's quarterly job is short**: here is the reference schedule for this period, here is what changed in the chart, here are the calculation relationships, and here is the tag map from last quarter with the deltas flagged.

---

## Anti-patterns

- **Claiming to review the tagging.** Mosofin cannot read the document or the taxonomy.
- **Treating validation success as tagging correctness.** A wrong element validates perfectly.
- **Choosing a generic element where a specific one exists.** No error is raised and comparability is lost.
- **Creating an extension because it is quicker than deciding.**
- **Leaving an extension unanchored.**
- **Carrying a tag map across a taxonomy version** without reviewing for deprecations.
- **Tagging the originally-filed comparative** where the prior period was restated.
- **Reference figures at component level** against a consolidated filing.
- **Ignoring warnings.** They are assessed, not skipped.
- **Leaving the EPS check blank** rather than marking it as requiring the cap table.
- **Producing the reference schedule once** and filing weeks later. Re-run it.
- **Treating a Mosofin reference schedule as exempt from IPE requirements.**
- **Using an XBRL review as a second check on the financials.** That gate closed earlier.
- **Saying "tagged", "validated" or "filed".** The gateway reads.
