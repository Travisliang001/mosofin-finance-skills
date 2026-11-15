<!-- nonprofit-fund-accounting · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding) — Mosofin addition
- Step 0b — Establish the two structural questions (Mosofin addition)
- Step 1 — Establish net asset classification
- Step 2 — Recognize contributions and grants
- Step 3 — Track and release restrictions
- Step 4 — Endowment accounting
- Step 5 — In-kind contributions
- Step 6 — Functional expense allocation
- Step 7 — Build the NFP financial statements
- Step 8 — Disclosures
- Step 9 — Output
- Step 10 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Never drop a task because no tool covers it.** Donor stipulations and allocation bases are legitimately
`[manual]`.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding) — Mosofin addition

**Batch independent reads into one message** — the accounts, the dimensions, the balances and the expense
data do not depend on each other. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`search_accounts`* — **the chart: net asset accounts by class, contribution revenue, expense accounts —
  the natural axis** — usually **[auto]**
- *`search_classes`* / *`search_departments`* / *`search_locations`* — **the candidate functional
  dimension** — usually **[auto]**
- *`get_profit_and_loss`* **by class / department** — **the functional matrix, if function is tracked** —
  usually **[auto]**
- *`get_balance_sheet`* / *`get_trial_balance`* **by class** — **net assets by restriction class** — usually
  **[auto]**
- *`get_general_ledger`* on **net asset and release accounts** — **the roll-forward and any release
  entries** — usually **[auto]**
- *`search_customers`* — **donors and funders, where set up as customers** — usually **[auto]**
- *`search_deposits`* / *`search_payments`* — contributions received — usually **[auto]**
- *`get_aged_receivables`* — **pledges receivable** — usually **[auto]**
- *`get_company_info`* — legal name, **fiscal year end** — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — **NFP statements go to funders, regulators and the
public**, and the program percentage in particular is read closely.

## Step 0b — Establish the two structural questions (Mosofin addition)

**Run before Step 1**, and put both answers in the workpaper header.

1. **Does the chart separate net asset classes?** **[auto]**. If not, **the classification, the roll-forward
   and the composition disclosure cannot come from the ledger.**
2. **Is function tracked, and is it function or programs?** **[auto]** to list the dimension values,
   **[manual]** to interpret them. **Values like *Program*, *Management & General*, *Fundraising* are
   functional. Values like *Youth Services*, *Food Bank*, *Foundation A* are programs or funders.**
3. **Is a second dimension available?** Many platforms offer both class and department or location. **An
   entity tracking programs on class and function on department can produce both** — and that combination
   is worth identifying, because it satisfies this skill and
   `grant-accounting-nonprofit-restricted-funds` simultaneously.

**Report what is possible before building it**, so the deliverable is not promised and then reduced.

## Step 1 — Establish net asset classification

**Net assets in NFPs are classified by donor restriction** — **[gated]**: balances `[auto]` where the chart
separates them; **the classification of any new item is `[manual]`**:

**Without donor restrictions**:
- **Resources free from donor-imposed restrictions**
- **Board-designated amounts** — board-imposed, not donor-imposed — **sit within this class**

**With donor restrictions**:
- **Restricted by donor as to purpose** — e.g. for a specific program
- **Restricted by donor as to time** — e.g. for use after a certain date
- **Held in perpetuity** — e.g. a permanent endowment where **the corpus must be maintained**, with
  earnings potentially restricted or unrestricted per the donor's intent

**The pre-ASU 2016-14 three-class model — unrestricted / temporarily / permanently restricted — was
simplified to two classes (without / with donor restrictions); within the "with" class, disaggregate by
nature / purpose / time / perpetuity in disclosures.**

**Mosofin note on board-designated funds**: **they are without donor restrictions, and the ledger cannot
tell you which amounts are board-designated** — they frequently sit in the same account as genuinely
unrestricted funds, or in a designated account that looks restricted. **The distinction is `[manual]`, from
board minutes**, and it matters because **the board can undesignate and a donor cannot.**

## Step 2 — Recognize contributions and grants

**Unconditional contributions**: **recognized as revenue when promised or received, at fair value, in the
appropriate net asset class** — **[gated]**.

**Conditional contributions** — **a barrier the recipient must overcome AND a right of return or release**:
**NOT recognized until the conditions are substantially met. Track them as conditional and only recognize
when conditions are met.** **[manual]**, always — **the barrier is in the agreement.**

**Distinguishing contributions from exchange transactions:**

- **A contribution is non-reciprocal** — the donor doesn't receive commensurate value
- **An exchange is reciprocal** — e.g. a grant where the grantor gets specific deliverables of value to
  themselves — **recognized under revenue recognition principles** (`revenue-recognition-asc606`)
- **Many "grants" are partly or wholly contributions; assess carefully**

**Net asset class at receipt:**

- **Unrestricted (without donor restrictions) if the donor imposed no restriction**
- **With donor restrictions if the donor restricted it**

**[auto]** cross-check, not a determination: **cash received with no corresponding revenue, or revenue with
no receivable and no cash**, both indicate a classification that was never worked through. **Report the
pattern; the classification is the user's** — the same treatment as in
`grant-accounting-nonprofit-restricted-funds`.

## Step 3 — Track and release restrictions

**When a donor-imposed restriction is satisfied — purpose accomplished or time elapsed:**

- **Reclassify net assets from "with donor restrictions" to "without donor restrictions"**
- **Shown on the statement of activities as "Net assets released from restrictions"** — **an increase in the
  without-donor-restrictions column and a decrease in the with-donor-restrictions column (zero in total)**

**Track each restriction and when it's released. A common error is recognizing the restricted contribution
and the expense without making the release entry, leaving the released amount stranded in the restricted
class.**

**Mosofin contribution — that common error is detectable.** **[auto]**:

- **Qualifying expenditure occurred** — spend against the restricted purpose, readable by dimension
- **No release entry posted** — the release accounts show no corresponding movement
- **Restricted net assets grew** while the purpose was being satisfied

**Together those three are the signature of the missing release**, and it is one of the most common NFP
errors. **Report it with the qualifying spend that should have triggered the release.**

**And the release is computable**, exactly as in the grant skill: **purpose restrictions release as
qualifying costs are incurred, capped at the restricted amount; time restrictions release on the date.**
**Report the release with its working** — the qualifying spend, the cumulative, the restricted balance.

## Step 4 — Endowment accounting

For **donor-restricted endowments** — **[manual]** throughout, with `[auto]` balances:

- **The original gift (corpus) is held in perpetuity**
- **Earnings — interest, dividends, gains / losses — per the donor's stipulation**: **if unrestricted by
  donor, classified as without donor restrictions; if restricted (e.g. for a particular program), with
  donor restrictions until used**
- **"Underwater" endowments** — fair value below original gift: **the deficiency is reflected in net assets
  with donor restrictions with required disclosure** — **[manual]**: **there are no fair values on this
  surface**
- **Spending rate / appropriation per the organization's policy and applicable laws** — **[manual]**

**Board-designated endowments are within "without donor restrictions"** — the board can undesignate.

**[auto]** contribution is limited: **investment income and the endowment account balances are readable**;
**the corpus / earnings split and every donor stipulation are not.** **Underwater status requires a fair
value and therefore cannot be determined here** — name the source required.

## Step 5 — In-kind contributions

**Contributed goods and services recognized at fair value when** — **[manual]**:

- **For contributed services**: **they would typically be purchased if not donated AND require specialized
  skills provided by qualified individuals** — otherwise **not recognized**
- **For contributed nonfinancial assets** — goods, use of facilities: **recognized; ASU 2020-07 added
  disclosure requirements about utilization and valuation**

**Record contribution revenue and the corresponding expense or asset.**

**[auto]** only where already recorded: **an in-kind revenue account with matching expense** is readable.
**In-kind contributions that were never recorded are invisible** — and **the recognition test and the
valuation are both `[manual]`.**

## Step 6 — Functional expense allocation

**NFPs report expenses by both natural classification** — salaries, rent, supplies — **and functional
classification** — **program services, management & general, fundraising**. **The Statement of Functional
Expenses, a required disclosure for all NFPs, presents the matrix.**

**Allocate expenses to functions:**

- **Direct identification where possible** — an expense incurred entirely for one function — **[auto]**
  where the dimension is tagged
- **Allocation based on a rational, documented basis** — e.g. **time studies for personnel, square footage
  for occupancy** — **[manual]**: **the basis is a study, not a ledger field**
- **Maintain consistency period-to-period** — **[auto]** to check: **the same allocation ratios applied
  across periods are verifiable**
- **Disclose the allocation methodology** — **[manual]**

**Common pitfalls: under-allocating to M&G or fundraising** — **the incentive to overstate program % is real
but improper** — **joint costs (multi-purpose activities) have specific allocation rules.**

**The Mosofin position on the matrix:**

- **Natural axis: `[auto]`.** The chart of accounts.
- **Directly-identified functional costs: `[auto]`** where the dimension carries function.
- **Shared costs requiring allocation: `[gated]`.** The pool is `[auto]`; **the basis is `[manual]`.**
- **The resulting program percentage is `[auto]` to compute** — and **it should be reported alongside prior
  periods**, because **a program percentage that moves without an explained change in operations or
  methodology is exactly what regulators and funders question.**

**Report the proportion of expense that was directly identified versus allocated.** **A matrix where 80% is
allocated on judgment is a different document from one where 80% is directly tagged**, and the reader
deserves to know which.

## Step 7 — Build the NFP financial statements

**Statement of Financial Position** — balance sheet equivalent — **[gated]**:
- **Assets, liabilities, and net assets**
- **Net assets split: without donor restrictions / with donor restrictions**
- **Disclose composition of net assets with donor restrictions** — purpose, time, perpetuity

**Statement of Activities** — income statement equivalent — **[gated]**:
- **Revenue and expenses by net asset class**
- **Shows changes in each net asset class**
- **Includes net assets released from restrictions line**
- **Total change in net assets**

**Statement of Functional Expenses** — **[gated]**:
- **Expenses by natural × functional classification**

**Statement of Cash Flows** — **[gated]**:
- **Indirect or direct method** (`cash-flow-statement-indirect-method`); **NFP-specific items** — e.g.
  **restricted gifts for long-lived assets in financing**

**Mosofin check across the statements**: **the release line must net to zero on the statement of
activities** — an increase in one column and an equal decrease in the other. **[auto]** to verify, and **a
non-zero total is a mechanical error** that occasionally survives into published statements.

**And the net asset roll-forward must tie**: **opening + change = closing, per class**, against the balance
sheet.

## Step 8 — Disclosures

For `notes-to-financial-statements`, NFP-specific:

- **Liquidity and availability of resources** — **a required NFP disclosure**: quantitative and qualitative
  information about how the organization manages liquidity — **[gated]**, **and partly computable**: cash,
  receivables and short-term investments **less amounts unavailable because donor-restricted**
- **Composition of net assets with donor restrictions** — nature / purpose / time / perpetuity —
  **[gated]**; needs the stipulations
- **Endowment composition, spending policy, underwater amounts** — **[manual]**
- **Functional expense allocation methodology** — **[manual]**
- **Contributions, including conditional promises to give** — **[manual]**
- **In-kind contributions — utilization, valuation** — **[manual]**
- **Related parties — board members, key staff** — **[gated]**: **vendor and customer names can be compared
  to a supplied board and staff list**; the list itself is `[manual]`

**The liquidity disclosure deserves the effort.** The original notes it should be **"meaningful (not
boilerplate)"** — and **the quantitative half is largely computable**, which makes a specific disclosure
cheaper than a generic one.

## Step 9 — Output

Deliver an `.xlsx` NFP workbook:

**Sheet 1: Statement of Financial Position** — with net asset class detail. Plus the header block: workspace
name; the entity by `display_name`; excluded company files; **whether the chart separates net asset
classes**; **whether function is tracked as a dimension**; whether any figure rests on `mock` data.

**Sheet 2: Statement of Activities** — by net asset class, with releases, **and the release line verified to
net to zero**.

**Sheet 3: Statement of Functional Expenses** — natural × functional matrix, **with the directly-identified
and allocated proportions shown**.

**Sheet 4: Statement of Cash Flows**

**Sheet 5: Net Assets Detail and Roll-Forward** — by restriction nature; **opening + activity + releases =
closing**, **tied to the balance sheet**.

**Sheet 6: Contribution & Grant Register** — unconditional vs. conditional; restrictions; releases tracked.

**Sheet 7: Endowment Schedule** — corpus, earnings, spending, underwater status.

**Sheet 8: Functional Allocation Methodology** — allocation basis and computations.

**Sheet 9: Disclosure Data** — liquidity, restrictions composition, in-kind, and the rest.

**Sheet 10: Missing Releases — NEW, Mosofin-specific** — qualifying spend with no corresponding release
entry, by restricted purpose, with the amounts that should have released.

**Sheet 11: Coverage — NEW, Mosofin-specific**

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used / external source | As-at date | `mock` | Gap |

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming:** `NFP_FS_[YYYY]_[EntityName].xlsx`

Every file states which datasource and `display_name` it covers.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where the data does not
cover something — stipulations, conditions, fair values, allocation bases — **name the source required**
instead of estimating.

## Step 10 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The account map**: net asset accounts by class, contribution revenue by restriction, release accounts,
  in-kind accounts
- **The dimension mapping** — **which dimension carries function, which carries programs or grants, and the
  values in each.** **The most valuable stored asset here**, and the thing that makes the functional matrix
  reproducible
- **The functional allocation methodology** — the basis for each shared cost pool, **and the cadence for
  refreshing the study**
- **The classification decisions** per recurring funder: contribution or exchange, conditional or
  unconditional, restricted or not — **with the clause relied on**
- **The release basis** per restricted purpose: which expenditure qualifies
- **The endowment terms by fund** — corpus, earnings treatment, spending policy — **by reference, not by
  amount**
- **The board-designated amounts and their authority** — by reference to the minutes
- **The liquidity disclosure basis** — what counts as available within one year
- The replay recipe: the exact sequence of reads that produced the matrix and the release calculation

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist individual donor names, gift amounts, donor contact details or giving history.** **Donor
information is confidential and frequently legally protected**, and a skill bundle is not where it belongs —
the same rule as `grant-accounting-nonprofit-restricted-funds`. **Institutional funder terms are decisions
and may be stored by reference; an individual's giving is not yours to carry.** **And never persist net
asset balances, release amounts or expense figures** — all state.

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / Northbrook
Community Trust — function on Department (Program / M&G / Fundraising), programs on Class, restricted net
assets 3200, releases 3900, occupancy allocated by square footage reviewed annually" — not "function on
Department". **Dimension mappings are entity-specific**, and applying one organisation's mapping to another
builds a functional matrix from the wrong axis. Record the chosen **scenario** (single vs multi) as a
preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's.**

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One chart, one set of dimensions, one
statement set.

**Multi-entity.** Steps 0–9 run **once per entity**, each call targeting exactly one `data_source_id`, every
balance carrying its entity's `display_name`. Then the points specific to the sector:

- **A restriction travels with the money.** **Transferring restricted funds to an affiliate does not release
  the restriction** — see `grant-accounting-nonprofit-restricted-funds`. **Never treat an intercompany
  transfer as a release.**
- **A trading subsidiary is usually a for-profit entity** whose results are consolidated and whose profits
  may be gift-aided or donated up. **Its accounts are not NFP accounts**, and it has no net asset classes.
  **Do not apply this skill's classification to it** — consolidate its result into the charity's
  unrestricted column.
- **A supporting foundation holding endowment** produces restricted balances in one file and the spending in
  another. **Read both**, and compute releases against the spend wherever it occurred.
- **Functional allocation is per entity**, and **shared costs across entities need an inter-entity
  allocation basis** before they can be split by function. That basis is `[manual]`.
- **Consolidated statements keep the net asset classes separate.** **Never net restricted against
  unrestricted across entities** — see `consolidation-and-eliminations`; the classes survive consolidation.
- **The program percentage is usually presented at group level**, and **it should be computed from
  consolidated figures with intercompany eliminated** — a management fee charged between group entities
  would otherwise inflate M&G in one and program in the other.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict per company
file.
