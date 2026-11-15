<!-- government-fund-accounting-gasb · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding) — Mosofin addition
- Step 0b — Establish the basis and the fund dimension (Mosofin addition)
- Step 1 — Identify the fund structure
- Step 2 — Apply the right measurement basis per fund
- Step 3 — Build the fund financial statements
- Step 4 — Fund balance classifications (governmental funds)
- Step 5 — Build government-wide statements (GASB)
- Step 6 — Special items requiring specific treatment
- Step 6b — Major fund determination (Mosofin addition, from the edge cases)
- Step 7 — Disclosures and supplementary information
- Step 8 — IPSAS / other public-sector frameworks
- Step 9 — Output
- Step 10 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Never drop a task because no tool covers it.** The actuarial work and the constraint determinations are
legitimately `[manual]`.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding) — Mosofin addition

**Batch independent reads into one message** — the dimension list, the trial balance, the accounts and the
profile do not depend on each other. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`search_classes`* / *`search_departments`* / *`search_locations`* — **the candidate fund dimension.
  Read this first; it determines whether the rest is possible** — usually **[auto]**
- *`search_accounts`* — the chart of accounts, including **capital asset, debt and net-position accounts** —
  usually **[auto]**
- *`get_trial_balance`* **by fund dimension** where the platform supports it — usually **[auto]**
- *`get_balance_sheet`* **by class / department** — usually **[auto]**
- *`get_profit_and_loss`* **by class / department** — **revenues and expenditures by fund** — usually
  **[auto]**
- *`get_general_ledger`* — **interfund transfers and the detail behind reconciling items** — usually
  **[auto]**
- *`search_journal_entries`* — allocations and closing entries between funds — usually **[auto]**
- *`get_company_info`* — legal name, **fiscal year end** — usually **[auto]**

**Record the `accounting_method` used on every call** and report it — it is part of the basis question.

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — **government financial statements are public
documents, frequently audited and filed with a state authority.** Fixture-based figures inside one are a
serious matter.

## Step 0b — Establish the basis and the fund dimension (Mosofin addition)

**Run before Step 1, and report the answer on the face of every statement.**

1. **Is there a fund dimension?** **[auto]** from the dimension lists. If not, **fund-level reporting cannot
   come from this ledger** — stop and say so rather than presenting everything as one General Fund.
2. **Which basis are the books on?** **[manual]**, asked at Gate 3, corroborated **[auto]**: **are capital
   assets and long-term debt on the balance sheet?** If yes, the books are on a full-accrual-style basis and
   **the governmental fund statements are a conversion**. If no, the books look like a governmental fund
   basis and **the government-wide statements are the build**.
3. **Which perspective is being asked for?** Fund, government-wide, or both. **Both requires the
   reconciliation in Step 5**, which is the real deliverable.

**Write the answer into the workpaper header.** Everything downstream is uninterpretable without it.

## Step 1 — Identify the fund structure

**Under GASB — illustrative; confirm current categorization — funds are grouped into three categories:**

**Governmental funds** (general government activities, **modified accrual basis**):
- **General Fund** — main operating fund
- **Special Revenue Funds** — revenue restricted / committed for specific purposes
- **Capital Projects Funds** — financial resources for capital outlays
- **Debt Service Funds** — resources for principal / interest payments
- **Permanent Funds** — resources where principal is restricted, earnings benefit the government or
  citizens

**Proprietary funds** (business-type activities, **full accrual basis**):
- **Enterprise Funds** — services charged to external users: utilities, parking
- **Internal Service Funds** — services to other government departments: fleet, IT

**Fiduciary funds** (resources held in trust for others, **not the government's own**):
- **Pension and OPEB trust funds, investment trust funds, private-purpose trust funds, custodial funds**

**Identify which funds the entity uses and classify each.** **[gated]**: the dimension list is `[auto]` and
gives the candidate names; **assigning each to a category is `[manual]`** and drives the basis in Step 2.

**Mosofin check — a fund should be self-balancing.** **[auto]** where the platform supports a balance sheet
by dimension: **each fund's assets should equal its liabilities plus fund balance.** A dimension that does
not self-balance is being used as a cost tag, not a fund — which is a direct test of the class-is-not-a-fund
warning, and it is worth running before anything is built on the mapping.

## Step 2 — Apply the right measurement basis per fund

**Governmental funds — modified accrual basis, current financial resources measurement focus:**

- **Revenue recognized when measurable AND available** — collected within the period or soon enough after to
  pay current-period liabilities, **typically 60 days under GASB**
- **Expenditures recognized when the related liability is incurred** — with exceptions: **debt service,
  compensated absences, claims / judgments often when payable**
- **Capital assets and long-term debt NOT reported on governmental fund balance sheets**
- **Tracks current financial resources only**

**Proprietary and fiduciary funds — full accrual, economic resources measurement focus:**

- **Revenue when earned; expenses when incurred** — like commercial
- **Capital assets and long-term debt reported on the fund balance sheet**
- **Same basic structure as commercial accounting**

**The dual basis is foundational and confusing for those new to government — keep it clear.**

**[manual]** to apply, and **this is where the platform cannot help.** The **availability test is `[manual]`
judgment on `[auto]` data**: receipts after year-end are readable (*`get_general_ledger`* on the receivable
accounts into the following period), **so the 60-day collection can be measured** — but which revenues the
test applies to, and the period the government has adopted, are policy.

**Where the books are on full accrual, list the conversions required for each governmental fund**: remove
capital assets, remove long-term debt, apply availability, adjust expenditure recognition for the
exceptions. **Those conversions are the reconciling items in Step 5** — build them once and they serve both
purposes.

## Step 3 — Build the fund financial statements

**Governmental funds** — **[gated]**:
- **Balance Sheet** — **current resources only; no capital assets or long-term debt**
- **Statement of Revenues, Expenditures, and Changes in Fund Balances**
- **Budget-to-actual comparison** where required

**Proprietary funds** — **[gated]**:
- **Statement of Net Position**
- **Statement of Revenues, Expenses, and Changes in Net Position**
- **Statement of Cash Flows** — **with specific GASB categories: operating, noncapital financing, capital
  and related financing, investing — different from commercial categories**

**Fiduciary funds** — **[gated]**:
- **Statement of Fiduciary Net Position**
- **Statement of Changes in Fiduciary Net Position**

**The proprietary cash flow categories deserve emphasis**: **four categories, not the commercial three**,
and the split of financing into **noncapital** and **capital-and-related** has no commercial equivalent.
**A platform-generated cash flow statement will use commercial categories and must be rebuilt**, not
relabelled.

## Step 4 — Fund balance classifications (governmental funds)

**GASB requires governmental fund balance to be classified by spending constraint** — **[manual]**, in full:

- **Nonspendable** — not in spendable form, e.g. inventory, prepaids, **or legally required to be maintained
  intact**
- **Restricted** — **externally imposed** restrictions: creditors, grantors, laws / regulations,
  constitutional provisions
- **Committed** — constraints imposed by the **highest level of decision-making authority**, e.g. the
  governing body
- **Assigned** — **intent** for a specific purpose, **less binding than committed**
- **Unassigned** — **the residual**; **can be negative only in the General Fund typically**

**For each fund, classify fund balance into these categories and disclose.**

**This is `[manual]` and it cannot be otherwise.** **The classification depends on the source and strength of
the constraint** — a grant agreement, a statute, a council resolution, a management designation. **None of
that is in an accounting system.** The ledger gives you the *amount* of fund balance; **the constraint
hierarchy comes from documents.**

**[auto]** support that is genuinely useful: **the nonspendable amounts are largely readable** — inventory
and prepaid balances by fund are on the balance sheet, and they are nonspendable by definition of form.
Start there, and the remainder is the constrained population to be classified from documents.

## Step 5 — Build government-wide statements (GASB)

**In addition to fund statements, GASB requires government-wide statements on a full accrual basis:**

**Statement of Net Position** (full accrual, government-wide):
- **All assets — including capital — and liabilities — including long-term debt and net pension / OPEB
  liability**
- **Net position categories: net investment in capital assets / restricted / unrestricted**

**Statement of Activities**:
- **By function / program, showing program revenues and net (expense) revenue**
- **General revenues separately**
- **Change in net position**

**The dual-perspective model (fund + government-wide) requires reconciliations:**

- **Total governmental fund balances → governmental activities net position** — adjustments: **add capital
  assets net of depreciation, deduct long-term debt, accrual differences**
- **Net change in fund balances → change in net position**

**[gated]**, and **this reconciliation is the heart of the deliverable.** **[auto]** contribution: **the
reconciling items are readable where they exist on the books** — capital assets net of depreciation, the
long-term debt balance, accrued interest, deferred items. **Where they are not on the books, they are
`[manual]` from registers held outside**, and that is the common case for a government keeping fund-basis
books.

**Report the reconciliation with every item quantified and sourced.** A bridge with an unexplained residual
is the government-sector equivalent of a plug, and it will be the first thing an auditor asks about.

## Step 6 — Special items requiring specific treatment

**Capital assets** (government-wide only) — **[gated]**:
- **Reported at historical cost; depreciated except for land and infrastructure under the modified
  approach**
- **Infrastructure — roads, bridges — modified approach allowed for assets the government commits to
  preserve at a condition level**

*Mosofin note*: **the capital asset register is not on this surface** — see
`fixed-asset-register-and-depreciation`, where the same gap and the same two-directional reconciliation
apply. **The modified approach also requires condition assessments**, which are engineering records, not
accounting ones.

**Long-term debt** (government-wide only) — **[gated]**:
- **General obligation bonds, revenue bonds — reported with appropriate disclosure**
- **Interest accrued**

*Mosofin note*: **balances readable if on the books; the bond amortization schedules are `[manual]`** — see
`debt-and-covenant-tracking`.

**Pensions and OPEB** (GASB 68 / 75 and successors) — **[manual]**, always:
- **Net pension liability / net OPEB liability on the government-wide statement**
- **Pension / OPEB expense, deferred inflows / outflows of resources**
- **Requires actuarial valuation — flag for actuary involvement**

**This is frequently the largest line on the government-wide statement, and none of it is derivable from an
accounting system.** Never estimate it.

**Grants** — **[gated]**:
- **Government-mandated and voluntary nonexchange transactions — specific recognition rules: eligibility
  met, time requirements**
- **Don't recognize before eligibility requirements are satisfied**

*Mosofin note*: **grant receipts and the associated spending are `[auto]`**, which supports the eligibility
analysis — **but the grant agreement's conditions are `[manual]`.**

**Interfund activity** — **[auto]** where funds are a dimension:
- **Interfund transfers, interfund loans, reimbursements — distinct from external transactions**
- **Eliminated in government-wide as appropriate**

**This is one of the strongest `[auto]` contributions in the skill.** **Transfers between fund dimensions are
readable and should net to zero across the government** (*`get_general_ledger`*, *`search_journal_entries`*).
**A non-zero net is an unmatched interfund entry**, and it will misstate both funds and the elimination.
The same reasoning as `consolidation-and-eliminations`.

**Budgetary comparison** — **[gated]**:
- **Required for the general fund and major special revenue funds**
- **Show original budget, final budget, actual, variances**
- **Differences between budgetary and GAAP basis often exist — disclose**

*Mosofin note*: **actuals are `[auto]`; the budget may be readable** where the platform holds it; **the
budgetary basis and the original-versus-final distinction are `[manual]`** — amendments are legislative
acts, not ledger entries.

## Step 6b — Major fund determination (Mosofin addition, from the edge cases)

**The original raises this as an edge case; it is arithmetic, so run it as a step.** **[auto]** given
fund-level totals:

**Governmental and enterprise funds are presented individually if "major", otherwise aggregated.** The
determination is a **size threshold test** against total assets, liabilities, revenues and
expenditures / expenses — **both within the fund category and across the government** — plus any fund
management elects to present as major.

**Compute it and show the working**, per fund, per element. **It must be redetermined annually**, and it is
exactly the kind of test that gets carried forward unchanged from last year. **[manual]** only for the
election to present an additional fund as major.

## Step 7 — Disclosures and supplementary information

- **Notes** — extensive: **capital assets, long-term liabilities, pensions / OPEB, risk, debt service** —
  **[gated]**
- **Required Supplementary Information (RSI)**: **pension / OPEB schedules, budgetary comparison if not in
  basic statements, infrastructure if the modified approach is used** — **[manual]**
- **Combining statements for non-major funds** — **[auto]** where the fund dimension supports it
- **For US state / local: the Annual Comprehensive Financial Report (ACFR, formerly CAFR)** is the full
  document including **statements, notes, RSI, statistical section**

**The statistical section is a ten-year presentation** and is almost entirely outside a current-period
ledger read. Name it as a separate exercise.

## Step 8 — IPSAS / other public-sector frameworks

**If under IPSAS** — used by many central governments and international organizations — **or another
framework** — **[manual]**:

- **IPSAS is largely accrual-based** (with a **cash-basis IPSAS** option), **aligned conceptually with IFRS
  but with public-sector specifics — non-exchange revenue, social benefits**
- **Apply the framework's specific standards; structure is broadly similar to government-wide accrual**

**Confirm the specific framework and its current standards.**

*Mosofin note*: **an IPSAS accrual entity maps far more comfortably onto a commercial ledger than a GASB
entity does**, because it does not require the dual basis. **The structural problem at the top of this file
is largely a GASB problem.** Say so when the framework is IPSAS — the capability map improves considerably.

## Step 9 — Output

Deliver an `.xlsx` workpaper:

**Sheet 1: Fund Structure** — **each fund: category, type, basis, purpose.** Add three Mosofin columns:
**the dimension it maps to**, **whether it self-balances**, and **whether it is major**.

**Sheet 2: Governmental Fund Statements** — **balance sheet and statement of revenues / expenditures /
changes in fund balances; modified accrual.** **State whether this is the book basis or a conversion.**

**Sheet 3: Proprietary Fund Statements** — net position, revenues / expenses / changes, **cash flows in the
four GASB categories**.

**Sheet 4: Fiduciary Fund Statements**

**Sheet 5: Fund Balance Classifications** — per governmental fund:
**nonspendable / restricted / committed / assigned / unassigned**, **each with the constraint document that
supports it**.

**Sheet 6: Government-Wide Statements** — Statement of Net Position and Statement of Activities, full
accrual.

**Sheet 7: Reconciliations** — **fund to government-wide**, every item quantified and sourced, **with no
unexplained residual**.

**Sheet 8: Capital Assets, Long-Term Debt, Pensions / OPEB** — detail and roll-forwards, **each marked
`[auto]` from the books or `[manual]` from a register held outside**.

**Sheet 9: Budgetary Comparison** — original, final, actual, variance, **with the budgetary-to-GAAP
differences shown**.

**Sheet 10: Disclosures & RSI**

**Sheet 11: Interfund Activity — NEW, Mosofin-specific** — every interfund transfer by pair, **with the net
across the government, which must be zero**, and any unmatched items listed.

**Sheet 12: Basis and Coverage — NEW, Mosofin-specific**

| Task | Fund / entity (`display_name`) | Verdict (auto / gated / manual) | Tool used / external source | Accounting method | As-at date | `mock` | Gap |

**Head it with the Step 0b answer**: whether a fund dimension exists, which basis the books are on, and
which statements are therefore conversions.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming:** `Government_FS_[FY]_[EntityName].xlsx`

`[EntityName]` is the government's name; every file states which datasource and `display_name` it covers.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where the data does not
cover something — the actuarial liability, the constraints, the capital asset register — **name the source
required** instead of estimating.

## Step 10 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The fund structure**: every fund, its category, its type, its purpose — **and the dimension value it
  maps to.** The single most valuable asset here
- **Which basis the books are kept on**, and therefore **which statements are conversions**
- **The conversion list per governmental fund** — what must be removed or adjusted, and from where
- **The fund balance classification decisions** and **the constraint document supporting each** — by
  document reference, not by amount
- **The availability period** adopted for modified accrual revenue recognition
- **The reconciliation template** — the standing reconciling items between fund and government-wide
- **The major fund determination method**, and the note that **it must be recomputed annually**
- **The framework** — GASB or IPSAS — and the standards confirmed as current, **with the date confirmed**
- **The component unit list** and whether each is blended or discretely presented
- **The actuary and the valuation cadence** for pensions and OPEB. **Not the liability**
- The replay recipe: the exact sequence of reads that produced the fund-level trial balances

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist fund balances, net position, pension liabilities or any statement figure.** Government
financial statements are public documents built from live data. And **never persist anything identifying an
individual beneficiary** of a fiduciary or pension fund.

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / City of
Northbrook — GASB, books on fund basis, funds mapped to Class, General/Water Enterprise/Debt Service,
60-day availability, capital assets tracked outside" — not "GASB, fund basis". **Fund structures are
entity-specific by definition**, and applying one government's fund map to another produces statements for
funds that do not exist. Record the chosen **scenario** as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's.**

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped. **Where funds are separate company files, a
missing one is a missing fund**, and the statements would not cover the reporting entity.

---

## Both entity scenarios

**Single company file.** All funds in one file, distinguished by a dimension. Steps 0–9 run once, with every
figure tagged by fund. **The self-balancing test in Step 1 matters most here** — it is what tells you the
dimension is really being used as a fund.

**Multiple company files.** Common in the public sector, and it takes two distinct shapes:

- **One file per fund.** Legitimate, and it makes each fund genuinely self-balancing. Steps 0–9 run **once
  per file**, each call targeting exactly one `data_source_id`. **The government-wide statements are then a
  consolidation across files**, and **interfund activity is intercompany activity** — read both sides and
  prove it nets to zero. See `consolidation-and-eliminations`.
- **Component units.** **Legally separate entities for which the primary government is financially
  accountable.** Ask, per connected file, whether it is **part of the primary government**, a **blended**
  component unit, or a **discretely presented** one — **the three are presented differently and the
  distinction is `[manual]`**, resting on the accountability relationship rather than anything in the books.
  **A discretely presented component unit is shown in a separate column, not merged.**

Further points:

- **Internal Service Funds are typically consolidated into governmental activities in the government-wide
  statements**, with eliminations. **They are proprietary funds at the fund level and governmental
  activities at the government-wide level** — one of the model's genuine oddities, and easy to get wrong in
  both directions.
- **Fiduciary funds are excluded from government-wide statements entirely**, because the resources are not
  the government's. **Do not consolidate them.** This is the most common structural error when funds live in
  separate files and someone consolidates everything connected.
- **Each file's basis may differ** — an enterprise fund file on full accrual, a general fund file on a
  fund basis. **Establish the basis per file**, not once.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict per company
file and per fund.
