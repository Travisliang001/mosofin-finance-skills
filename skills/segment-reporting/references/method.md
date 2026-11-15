<!-- segment-reporting · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

## Contents

- How to read the verdicts
- Inputs
- Workflow
- Step 1 — Identify operating segments (the management approach)
- Step 2 — Aggregate segments (if criteria met)
- Step 3 — Determine reportable segments (quantitative thresholds)
- Step 4 — Determine the measure of segment profit/loss
- Step 5 — Assemble segment data
- Step 6 — Reconciliations
- Step 7 — Entity-wide disclosures
- Step 8 — Comparatives and consistency
- Step 9 — Output
- Output Quality Standards
- Seed to evolved: what happens on the first real run
- Anti-patterns


## How to read the verdicts

- **`[auto]`** — Mosofin can do this from live reads, unattended.
- **`[gated]`** — the gateway asks first. Explain, get consent, re-invoke with `approved=true` (**reads only — never for a write**) and the `data_source_id`.
- **`[manual]`** — not on this surface, or not a machine's judgment. **The step stays. The user performs it.**

**Everything here is a proposal.** The gateway is read-only. Mosofin posts nothing and discloses nothing.

---

## Inputs

All eight preserved.

| Input | Format | Required | Mosofin source | Verdict |
|---|---|---|---|---|
| **Internal management reporting structure** | How the CODM views the business | **Required** | **Not in the books.** The dimension list is a candidate, not an answer. | `[manual]` |
| **Segment-level financial data** | Revenue, profit measure, assets per segment | **Required** | **`[auto]` if segments are a dimension; `[manual]` if not** | Depends on the binary |
| **Consolidated financials** | For reconciliation | **Required** | Live read | `[auto]` |
| **Reporting framework** | US GAAP / IFRS | **Required** | Not in the books | `[manual]` |
| **Reporting period** | Date range with comparatives | **Required** | Live read, both periods | `[auto]` |
| Intersegment transactions | Sales between segments | Recommended | **`[auto]` where segments are dimensions and the transactions are coded**; the *pricing basis* is a policy | `[auto]` in part |
| Geographic and product/service data | For entity-wide disclosures | Recommended | **Depends on what the customer and item records carry** — see Step 7 | `[auto]` in part |
| **Major customer data** | Customers ≥ 10% of revenue | Recommended | **`[auto]`, exact** — see Step 7 | `[auto]` |

---

## Workflow

### Step 1 — Identify operating segments (the management approach)

**`[manual]` at its root.** All three criteria preserved.

An operating segment is a component of the entity that:

1. **Engages in business activities earning revenue and incurring expenses**, including intersegment
2. **Whose operating results are regularly reviewed by the chief operating decision maker (CODM)** to make resource-allocation and performance decisions
3. **For which discrete financial information is available**

> **The CODM is whoever allocates resources and assesses performance — the CEO, a management committee, and so on. Identify who the CODM is and what reports they review. Segments follow how management actually runs the business, not an arbitrary structure.**

**List the operating segments as the CODM sees them.**

**What the workspace contributes, precisely** `[auto]`:

- **The dimension list**, with revenue and cost coded to each — a **candidate** structure to test the CODM question against
- **Whether discrete financial information is actually available** for each candidate, which is criterion 3 and is directly checkable: **a dimension that carries revenue but no cost has no discrete profit information**, and cannot be an operating segment on its own
- **Whether each candidate has genuine activity** — a dimension with three transactions in it is a coding artefact, not a component of the business

That third criterion is worth dwelling on, because it is the one place the ledger speaks directly to the standard. **Criterion 3 — discrete financial information available — is a data question, and the data is right there.** Criteria 1 and 2 are questions about the business and its management, and they are not.

---

### Step 2 — Aggregate segments (if criteria met)

**`[manual]`.** All criteria preserved.

Two or more operating segments **may** be aggregated into one if:

- Aggregation is **consistent with the core principle** — useful information about the business
- The segments have **similar economic characteristics**
- They are similar in: **nature of products or services, production processes, customer types, distribution methods, and regulatory environment** where applicable

> **Aggregation is optional and must meet ALL criteria. Document the judgment.**

**`[auto]` for one piece of evidence on "similar economic characteristics"**, which is otherwise the vaguest of the criteria: **compare the candidate segments' actual margins and growth rates over the available history.** Segments described as economically similar whose gross margins are 22% and 61% are a judgment that will be challenged, and the figures are one query.

**It is evidence, not a test.** Economic similarity is a forward-looking, qualitative assessment about long-term characteristics, and two segments with currently different margins can still be similar in the relevant sense. But a large, persistent divergence is exactly what an auditor or regulator asks about, and it is better raised internally.

**Aggregation is scrutinised** because it reduces disclosure. Document the judgment properly.

---

### Step 3 — Determine reportable segments (quantitative thresholds)

**`[auto]` given segment data — and this is arithmetic that is regularly got wrong by hand.**

An operating segment, or an aggregated group, is **reportable** if it meets **any ONE** of:

**1. Revenue test** — its reported revenue (**external + intersegment**) ≥ **10% of combined revenue of all operating segments**

Note the two easy errors, both `[auto]` to avoid: **intersegment revenue is included** in the numerator, and **the denominator is combined segment revenue, not consolidated revenue.** Those differ by exactly the intersegment eliminations.

**2. Profit/loss test** — the **absolute value** of its reported profit or loss ≥ **10% of the greater of:**
   - (a) **combined profit of all profitable segments**, or
   - (b) **combined loss of all loss-making segments**, absolute values

**This is the test people compute wrongly**, and it is worth spelling out. The denominator is not net profit. It is the **greater of two separate sums** — profitable segments added together, loss-making segments added together as absolute values — and whichever is larger. In a group where one segment is heavily loss-making, the denominator can be the loss side, and the threshold is then quite different from what a naive "10% of profit" calculation gives.

**`[auto]` computes it correctly every time.** That is a small thing that is genuinely useful.

**3. Asset test** — its assets ≥ **10% of combined assets of all operating segments**

Requires assets by segment, which is `[auto]` only where the balance sheet is dimensioned — **which it frequently is not, even where the P&L is.** Many books code revenue and cost to a class but not balances. Check; do not assume.

**Then the coverage test, which is the one people skip:**

> **75% coverage test**: reportable segments must account for **≥ 75% of total external (consolidated) revenue.** If not, **add more segments — even if below 10% — until 75% is reached.**

`[auto]`, and it is a genuine second-order step: it runs **after** the 10% tests and can force additional segments into the disclosure. **Note the denominator changes**: the 10% tests use combined segment revenue; the coverage test uses **external consolidated revenue.** Mixing them is another routine error.

> **Segments below the thresholds and not added are combined into "All Other Segments."**

**Document each segment's test results.** `[auto]` — Sheet 2 shows every segment against every test, including the ones that failed, because showing only the reportable ones hides the judgment.

---

### Step 4 — Determine the measure of segment profit/loss

**`[manual]`, and it is a question about the CODM's reports, not about GAAP.**

> **The measure reported is whatever the CODM uses — not necessarily a GAAP measure.**

Common measures, all four preserved: **segment operating income; segment EBITDA or adjusted EBITDA; segment contribution margin; gross profit.**

> **The key principle: report the measure the CODM actually uses. If the CODM uses adjusted EBITDA, report adjusted EBITDA — and reconcile it to consolidated income before tax.**

**This is counter-intuitive and it is the point of the management approach.** The instinct is to report a proper GAAP measure per segment. **The standard asks for the opposite**: report what management actually looks at, however non-standard, and bridge it to GAAP in the reconciliation. A GAAP measure the CODM never sees is not the segment measure.

`[auto]` for the arithmetic once the measure is defined; `[manual]` for the definition. And per the 10-Q and 10-K preparation: **a non-GAAP segment measure carries consistency obligations** — defined the same way period to period, or the change disclosed.

---

### Step 5 — Assemble segment data

**`[auto]` for the amounts where segments are dimensions. `[manual]` for the filter, which is the subtle part.**

> **For each reportable segment, gather what the CODM reviews — only items the CODM sees need to be disclosed.**

All eleven items preserved:

| Item | Verdict |
|---|---|
| **External revenue** | `[auto]` |
| **Intersegment revenue** | `[auto]` where coded |
| **Interest revenue and interest expense** (if reviewed) | `[auto]` |
| **Depreciation and amortisation** | `[auto]` |
| **The segment profit/loss measure** | `[auto]` once defined |
| **Material non-cash items** | `[auto]` in part; `[manual]` for materiality |
| **Income tax** (if reviewed at segment level) | `[auto]` where dimensioned — **often not** |
| **Segment assets** (if reviewed) | `[auto]` **only where the balance sheet is dimensioned** |
| **Segment liabilities** (IFRS 8, where provided to the CODM) | Same |
| **Capital expenditures** — additions to long-lived assets | `[auto]` |
| **Investment in equity-method investees** (if applicable) | `[auto]` where dimensioned |

#### The "only what the CODM sees" rule

**`[manual]`, and it runs against instinct.**

Several items above are qualified — *if reviewed*, *if provided to the CODM*. That qualification is doing real work: **an item the CODM does not review is not disclosed, even where the data exists.**

A connected ledger makes it trivially easy to produce all eleven items for every segment. **Producing them all is wrong.** It represents the CODM as reviewing information they do not see, which misdescribes the management approach the disclosure is supposed to convey — and it commits the entity to producing the same items every period thereafter.

**So: compute what the data supports, then filter to what the CODM reviews, and record which items were excluded and why.** The Gate 3 interview asks this question for exactly this reason.

---

### Step 6 — Reconciliations

`[auto]` where segments are dimensions — **with a caution that matters.**

Required reconciliations, all four preserved:

- **Total segment revenue → consolidated revenue** (eliminating intersegment)
- **Total segment profit/loss → consolidated income before tax** (and adjustments)
- **Total segment assets → consolidated assets**
- **Other material items → consolidated equivalents**

Reconciling items typically include, all three preserved:

- **Intersegment eliminations**
- **Unallocated corporate / HQ costs**
- **Differences between the segment measure and GAAP** — adjustments excluded from adjusted EBITDA, for instance

#### The reconciliation ties by construction, and that is a warning

**Where segments are dimensions of the same ledger, the segment P&Ls are slices of the consolidated P&L. They sum to it automatically.** A reconciliation that comes out clean has demonstrated that the slices add up — which double entry guarantees.

This is the same trap as `financial-statement-builder`'s balancing balance sheet and the receivables ageing's detail-to-summary tie. **Internal consistency is a floor, not a result.**

**What the reconciliation is actually for is the reconciling items** — the unallocated corporate costs, the measure differences, the eliminations. Those are the informative content, and they do not appear automatically. Present them individually and explained, not as a single balancing figure.

#### The check that does mean something: uncoded transactions

**`[auto]`, and it is the most useful thing in this step.**

**Read for transactions with no dimension assigned.** Where segments are ledger dimensions, any transaction that was not coded falls out of every segment and appears in the reconciliation as an unexplained residual — or, worse, gets absorbed into "unallocated corporate" where nobody questions it.

| Finding | Meaning |
|---|---|
| **Nothing uncoded** | The dimension is complete; the segment slices genuinely cover the business. |
| **A small, consistent uncoded amount** | Probably genuine corporate items. Confirm they belong in unallocated. |
| **A large or growing uncoded amount** | **A coding discipline problem**, and it silently understates whichever segments the transactions belonged to — which can change the 10% test results. |
| **Uncoded revenue specifically** | Worse than uncoded cost, because it flows straight into the 75% coverage test and the revenue threshold. |

**This is the segment equivalent of the completeness checks elsewhere in the pack**, and it is one query.

---

### Step 7 — Entity-wide disclosures

**Required regardless of segment structure — including for single-segment entities.** All three areas preserved, and the verdicts differ sharply.

**Products and services** — external revenue by product or service group, **unless impracticable.**

`[auto]` **where items or item categories are on the invoice lines.** Many books carry item detail; some carry only account-level revenue. **Where revenue is coded only to accounts, the product split is whatever the chart happens to encode** — which may or may not be a sensible product grouping. Check before claiming it.

**Geographic information:**

- **Revenue from external customers attributed to the entity's country of domicile and to all foreign countries** — in total, and by individual country where material
- **Long-lived assets located in the country of domicile and in foreign countries** — by country where material

**Revenue by geography**: `[auto]` **where the customer or transaction record carries a country** — and **the attribution basis matters.** The standard says *attributed to*, and the entity must choose and disclose a basis: customer location, or where the goods or services were delivered. **These differ**, and the ledger may only support one of them. This is the same billing-versus-shipping distinction that governs the sales tax work. **State which field was used.**

**Long-lived assets by country**: **`[manual]`, usually.** A fixed asset register records what an asset cost and when it was acquired. **It rarely records where the asset physically is** — consistent with `fixed-asset-register-and-depreciation` and property accounting. Where the entity has one location, this is trivial; where it has several, it must be supplied.

**Major customers** — **`[auto]`, and exact.**

> **If revenue from a single external customer ≥ 10% of total revenue, disclose that fact, the amount, and the segment(s) reporting it. Not required to name the customer.**

**This is the strongest single automatic contribution in the skill**, and it is worth saying why:

- Revenue by customer, ranked, with percentages, is one query and it is exact
- It is a **required disclosure for every entity**, including single-segment ones
- It **moves** — a customer at 8% last year and 13% this year triggers a disclosure that did not exist before
- **In manual practice it is often assessed from memory**, and memory is bad at the 10% boundary

`[auto]` should also handle the two refinements the standard needs: **aggregate customers under common control** where the entity is aware of the relationship (which the ledger may not know — flag it, see the related party disclosures), and **identify which segments report the revenue**, which is `[auto]` where segments are dimensions.

**The customer need not be named**, and the default should be not to name them — the disclosure requirement is the fact and the amount.

---

### Step 8 — Comparatives and consistency

`[auto]` for the comparatives; `[manual]` for the judgment. All three preserved.

- **Present comparative periods.** `[auto]` — read both periods in the same batch.
- **If segments change (reorganisation), restate prior periods to the new structure**, or explain why impracticable. **`[auto]` where the prior period's transactions carry dimensions that can be re-mapped; `[manual]` where the old structure cannot be reconstructed** — and that is exactly what makes restatement impracticable, so the ledger answers the practicability question directly.
- **Maintain consistency in the profit measure across periods.** `[manual]` to decide; **`[auto]` to check** — compute the prior period on the current definition and compare to what was previously reported.

**On restating after a reorganisation** `[auto]`: whether prior-period transactions can be re-mapped to the new segments depends on whether the underlying detail survives. If the old dimension was deleted rather than renamed, the history may be unrecoverable. **Check before promising a restatement**, because "impracticable" is a real and available answer and it is better established in advance than discovered halfway.

---

### Step 9 — Output

An `.xlsx` workpaper. All six of the original's sheets, plus two additions.

**Sheet 1: Segment Identification**
- **CODM identification** — `[manual]`, named
- **Operating segments listed** as the CODM sees them
- **Aggregation analysis**, if any, with the margin and growth evidence beside it
- **Mosofin addition**: the ledger's dimension list beside the CODM's structure, **with any divergence shown.** Where they differ, that is a finding worth explaining, not a discrepancy to reconcile away.

**Sheet 2: Reportable Segment Tests**
| Segment | Revenue (ext + inter) | % of combined | Profit/Loss | % Test | Assets | % Test | Reportable? |

Plus the **75% coverage check** as a separate block, **with its own denominator labelled** — external consolidated revenue, not combined segment revenue.

**Every segment appears**, including those failing all three tests, because the judgment is only visible when the failures are shown.

**Sheet 3: Segment Financial Data**
| Item | Segment 1 | Segment 2 | ... | All Other | Total |

**Only items the CODM reviews.** Add a note listing the items that were computable and deliberately excluded, and why.

**Sheet 4: Reconciliations**
Revenue, profit/loss and asset reconciliations. **Reconciling items itemised and explained individually** — never one balancing figure. **With the "ties by construction" caution printed on the sheet.**

**Sheet 5: Entity-Wide Disclosures**
Products and services; geographic revenue and assets; major customers. **Attribution basis stated for the geographic split.**

**Sheet 6: Disclosure Draft**
Footnote-ready text for `notes-to-financial-statements`. Marked **DRAFT**.

**Sheet 7: Data Quality and Coverage** *(Mosofin addition)*
| Check | Finding | Amount | % of total | Action |
|---|---|---|---|---|

Uncoded transactions, by type and amount. Dimensions with revenue but no cost. Dimensions with negligible activity. Whether the balance sheet is dimensioned. Whether prior-period detail supports a restatement.

**Sheet 8: Coverage and Provenance** *(Mosofin addition)*
The mandatory coverage sheet.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

File naming: `Segment_Reporting_[YYYY]_[EntityName].xlsx`

Entity `display_name` on every sheet. If any read returned `mock: true`, say so in the file name and on Sheet 1.

---

## Output Quality Standards

All eight preserved.

- **CODM identified and the management approach applied.** `[manual]` — **named on Sheet 1.**
- **Reportable segment tests documented — the 10% tests and the 75% coverage test.** `[auto]`, **with every segment shown including the failures, and each denominator labelled.**
- **Segment profit measure matches what the CODM uses.** `[manual]` — **not a GAAP measure substituted for convenience.**
- **All required reconciliations present and tying to consolidated.** `[auto]` — **with the reconciling items itemised, since the tie itself is guaranteed where segments are ledger slices.**
- **Entity-wide disclosures included — products, geography, major customers.** `[auto]` for major customers; **required even for a single segment.**
- **Comparatives consistent or restated with disclosure.** `[auto]` where the prior detail supports restatement.
- **File naming consistent.** `[auto]`
- **No segment structure imposed that doesn't match how management runs the business.** **`[manual]`, and it is the standard that governs the rest** — and the one a connected ledger most tempts you to break, because the dimensions are right there.

**Four Mosofin additions:**

- **The dimension structure is shown beside the CODM structure**, and divergence is explained rather than hidden.
- **Uncoded transactions are quantified**, because they distort the threshold tests.
- **Only items the CODM reviews are disclosed**, with the excluded ones recorded.
- **The geographic attribution basis is stated**, since customer location and delivery location differ.

---

## Seed to evolved: what happens on the first real run

**What must never be frozen into a seed:** the capability map — Gate 2 reads it fresh.

**What is worth persisting into the workspace-scoped skill:**

1. **The CODM and the segment structure they review**, with the reasoning. This is the expensive answer and it is stable between periods — a reorganisation changes it, and nothing else does.
2. **The mapping from ledger dimensions to segments**, which is what makes every subsequent run automatic.
3. **The profit measure and its exact definition**, since consistency across periods is a requirement.
4. **Which Step 5 items the CODM reviews**, so the disclosure scope stays stable.
5. **The aggregation judgment and its support.**
6. **Whether the balance sheet is dimensioned**, and the geographic attribution basis.
7. **Prior-period test results**, so a segment crossing or falling below a threshold is visible as a change rather than rediscovered.
8. **Customers near the 10% line**, so the disclosure is anticipated rather than triggered.
9. **Uncoded-transaction findings and their resolutions.**

Persist through `create_skill`, scoped to the workspace. **Client facts belong in a client-scoped skill, never back in the seed** — customer concentration data is commercially sensitive.

**The evolved version's annual job is short**: has the structure changed, which segments crossed a threshold, which customers crossed 10%, and is anything still uncoded.

---

## Anti-patterns

- **Building the segment note from the chart's dimensions.** They are a candidate structure; the CODM's reports are the answer.
- **Treating each legal entity as a segment.** Sometimes true, never by default.
- **Reading segments off account names.** "North Region Sales" is a coding convention.
- **Computing the profit test on net profit.** The denominator is the greater of combined profits or combined losses, absolute.
- **Using consolidated revenue as the denominator for the 10% revenue test.** It is combined segment revenue, including intersegment.
- **Skipping the 75% coverage test.** It runs after the 10% tests and can force more segments in.
- **Excluding intersegment revenue from the revenue test.** It is included.
- **Reporting a clean reconciliation as validation.** Ledger slices sum to the ledger. The reconciling items are the content.
- **Absorbing uncoded transactions into "unallocated corporate."** Quantify them; they distort the tests.
- **Disclosing every Step 5 item because the data exists.** Only what the CODM reviews.
- **Substituting a GAAP measure for the CODM's measure** because it looks more rigorous.
- **Skipping entity-wide disclosures because there is one segment.** They are required anyway.
- **Assessing the 10% customer test from memory.** It is one exact query and it moves.
- **Promising a restatement before checking the prior detail survives.**
- **Conflating reporting units with segments** for goodwill.
- **Saying "disclosed".** Mosofin drafts.
