<!-- healthcare-revenue-cycle-accounting · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding) — Mosofin addition
- Step 1 — Map revenue cycle flows
- Step 2 — Estimate net patient service revenue
- Step 3 — Reconcile AR and cash
- Step 4 — Reserves and key estimates
- Step 5 — Close controls
- Step 6 — Output (Mosofin addition)
- Step 7 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Never drop a task because no tool covers it.** The payer contracts and the denial detail are legitimately
`[manual]`.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding) — Mosofin addition

**Batch independent reads into one message** — the accounts, the revenue history, the AR and the cash do
not depend on each other. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

**Request aggregates, not patient detail**, wherever the tool allows it.

Typical opening batch, per in-scope entity:

- *`search_accounts`* — **gross revenue, contractual allowance and other contra revenue, AR, bad debt,
  charity care and cash accounts** — usually **[auto]**
- *`get_profit_and_loss`* **by period, and by class / department / location** — **gross charges, contra
  revenue and net revenue — the realization series** — usually **[auto]**
- *`get_general_ledger`* on the **contra revenue, bad debt and write-off accounts** — **adjustment volumes
  over time** — usually **[auto]**
- *`get_balance_sheet`* / *`get_trial_balance`* — **GL AR and the reserve balances** — usually **[auto]**
- *`get_aged_receivables`* — **the GL aging**, by customer or payer where set up — usually **[auto]**
- *`search_deposits`* / *`search_payments`* — **cash received, and unapplied amounts** — usually **[auto]**
- *`search_customers`* — **payers, where they are set up as customers.** **Read the payer-level structure,
  not patient records** — usually **[auto]**
- *`search_credit_memos`* — adjustments raised as credits — usually **[auto]**
- *`get_company_info`* — legal name, currency, year-end — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — **net revenue and the reserves are the largest
estimates in a healthcare income statement**, and a fixture-based realization rate would drive both.

## Step 1 — Map revenue cycle flows

**Define how transactions flow:**

> **Charge capture → claim submission → payer adjudication → remittance posting → patient responsibility →
> collections.**

**[gated]**: the flow itself is `[manual]` — it describes the entity's process — but **where each stage
lands in the GL is `[auto]`**, and mapping the two together is the useful output.

**Mosofin addition — map each stage to its accounting evidence, and mark where the GL simply cannot see:**

| Stage | Lands in the GL as | Verdict |
|---|---|---|
| **Charge capture** | gross charges, **if the entity records them** | **[gated]** — some providers post net only |
| **Claim submission** | nothing | **[manual]** — billing system only |
| **Payer adjudication** | nothing until posted | **[manual]** — where denials happen, and the GL never sees the reason |
| **Remittance posting** | cash and contractual adjustments | **[auto]** |
| **Patient responsibility** | patient AR | **[gated]** — visible in total, rarely split from payer AR |
| **Collections** | cash, and write-offs | **[auto]** |

**Two of the six stages are invisible to the ledger, and they are the two where value is lost.** Saying so
plainly is more useful than a flow diagram that implies full coverage.

## Step 2 — Estimate net patient service revenue

- **Gross charges are rarely collectible.**
- **Estimate contractual allowances based on payer contracts and historical realization.**
- **Separate:**
  - **Contractual adjustments (contra revenue)**
  - **Bad debt (expense) vs. charity care (policy-based presentation)**

**[gated]**, and this is the skill's most valuable `[auto]` contribution:

**Compute historical realization directly.** **[auto]** where gross charges are recorded: **net revenue ÷
gross charges, by period, by payer class where the dimension supports it.** Present it as a series, not a
single number — **realization drifts as payer mix and contract terms change**, and the trend is what tells
you whether the current estimate is still right.

**Then test the estimate against it.** An assumed realization of 42% against a computed history of 37% over
eight quarters is a finding, not a rounding difference. **Report the comparison; the estimate stays the
user's.**

**Where gross charges are not recorded in the GL** — some providers post net revenue only — **say that
realization cannot be computed from the ledger** and must come from the billing system. Do not derive a
realization rate from net figures alone.

**On the three-way separation, which is where healthcare accounting is most often wrong:**

- **Contractual adjustment** — the difference between the list price and the contracted rate. **Contra
  revenue. It was never going to be collected and was never really revenue.**
- **Charity care** — care given to patients who qualify under the entity's financial assistance policy.
  **Never bad debt, and typically not revenue at all** — the entity decided not to pursue payment. **The
  eligibility determination is `[manual]`**, and the presentation follows the policy.
- **Bad debt** — amounts the entity **expected** to collect and did not. **An expense, or under the current
  revenue model frequently an implicit price concession reducing revenue instead.** **Which treatment
  applies is `[manual]`** and depends on whether collectability was assessed at the outset.

**Reclassifying between these three changes both revenue and expense**, and it is scrutinised — by auditors
and, for many providers, by regulators reviewing community benefit. **[auto]** support: **the amounts
posted to each account are readable and trendable**, so a shift between categories across periods is
detectable even when the reason is not.

## Step 3 — Reconcile AR and cash

- **Tie subledger AR to GL AR** — **[gated]**: **the GL side is `[auto]`, the subledger side is
  `[manual]`** unless a billing platform is connected. **This is the bridge, and it is the single most
  important control in the skill.**
- **Tie cash receipts to bank deposits** — **[auto]**: deposits and the cash account are both readable.
- **Track unapplied cash** — **[auto]**: unapplied receipts are readable, and **they are both a reconciling
  item and a revenue-cycle failure** — money received that has not been matched to a claim, ageing quietly.
  **Report the balance and its age.**

**Report the AR tie-out with the difference quantified**, even when it is zero, and **list the reconciling
items** — timing, unposted remits, adjustments recorded in one system and not the other. **"Ties" without a
number is an assertion.**

**[auto]** additions worth running:

- **AR days (days revenue outstanding)** on net revenue, trended. **The single most watched revenue cycle
  metric**, and computable from the GL.
- **AR aging distribution over time.** A lengthening tail signals denials or collection failure before the
  reserve does.

## Step 4 — Reserves and key estimates

- **Contractual allowance reserve** — **[gated]**: anchored on the Step 2 realization history
- **Denials reserve and recoveries** — **[manual]** on the drivers, **[auto]** on historical denial and
  recovery *amounts* where they are separately posted. **Denial reason codes and appeal success rates are
  the actual drivers, and they are in the billing system**
- **Bad debt reserve (expected credit losses) consistent with policy** — **[gated]**: **the aging and the
  historical write-off rate are `[auto]`**; the forward-looking element and the policy are `[manual]`.
  See `bad-debt-and-write-offs`

**Mosofin addition — test each reserve against outcomes.** **[auto]**: **compare each prior-period reserve
to what actually happened.** A contractual allowance reserve that is consistently released or topped up in
the following period is mis-set, and the pattern is readable across periods. **A reserve nobody has ever
back-tested is a reserve nobody has evidence for** — and this is the kind of estimate an auditor will ask
about first.

## Step 5 — Close controls

- **Cutoff testing for late charges and late remits** — **[gated]**: **postings dated near the period
  boundary and entries made after period end are `[auto]`**; whether the service occurred in the period is
  `[manual]`
- **Review payer mix changes** — **[gated]**: **revenue by payer or payer class across periods is `[auto]`**
  where the dimension exists. **Payer mix shifts move realization**, so this feeds directly back into
  Step 2's estimate
- **Trend analysis of adjustments and denials** — **[auto]** on amounts, **[manual]** on causes

**Mosofin addition — three close checks that run as queries:**

1. **Adjustment rate by period.** Contra revenue as a percentage of gross charges. **A step change means a
   contract changed, a payer changed behaviour, or something is posting incorrectly.**
2. **Write-off concentration.** Write-offs concentrated in a period, a payer or a user. **Report as a
   pattern, never as an allegation** — see `fraud-detection-and-forensics` for the discipline.
3. **Unapplied cash ageing.** Rising unapplied cash means remittances are not being matched, which
   overstates AR and understates cash applied.

## Step 6 — Output (Mosofin addition)

The original lists deliverables but does not specify a workpaper. Produce one.

Deliver an `.xlsx` workpaper. **Every sheet at aggregate level; no patient identifiers anywhere.**

**Sheet 1: Net Revenue Model** — **gross charges → contractual → net revenue**, by period and by payer
class. Plus the header block: workspace name; the entity by `display_name`; each excluded company file and
why; whether any figure rests on `mock` data; **and a statement that output is aggregate-level by design**.

**Sheet 2: Realization History — NEW, Mosofin-specific** — net revenue ÷ gross charges by period and payer
class, **with the assumption in use shown alongside the computed history**.

**Sheet 3: Revenue Cycle Map** — the six stages, where each lands in the GL, **and the two the GL cannot
see**.

**Sheet 4: AR Roll-Forward and Tie-Out** — opening AR, charges, adjustments, cash, write-offs, closing;
**GL versus subledger with the difference quantified and reconciling items listed**.

**Sheet 5: AR Aging and Metrics** — aging by payer class, **payer AR and patient AR separated**, AR days
trended.

**Sheet 6: Reserve Calculations** — contractual, denials, bad debt, **each with its basis** and **its
back-test against prior-period outcomes**.

**Sheet 7: Charity Care vs. Bad Debt** — amounts by category and period, with the policy basis, **and any
shift between categories highlighted**.

**Sheet 8: Cash and Unapplied** — receipts tied to deposits; **unapplied cash with ageing**.

**Sheet 9: Close Controls Checklist and Calendar** — cutoff, payer mix review, trend analysis, with owners
and dates.

**Sheet 10: Coverage — NEW, Mosofin-specific**

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used / external source | As-at date | `mock` | Gap |

**Every billing-system row reads `manual`.** That is the correct entry, and it is what makes the bridge
honest.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming (Mosofin addition — the original specifies none):**
`Healthcare_Revenue_Cycle_[YYYY-MM]_[EntityName].xlsx`

Every file states which datasource and `display_name` it covers.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where the data does not
cover something — the contracts, the denial reasons, the eligibility determinations — **name the source
required** instead of estimating.

## Step 7 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The account map**: gross revenue, each contra revenue account and what it represents, AR, bad debt,
  charity care, unapplied cash
- **The payer class mapping** — which customers or classes correspond to which payer class
- **Whether gross charges are recorded**, and therefore whether realization is computable here
- **The reserve methodology** for each of the three reserves, and **the back-test cadence**
- **The charity care policy basis** and its presentation treatment
- **The bad debt vs. price concession determination** and the reasoning
- **The realization basis** — which periods, which payer classes, how weighted. **Not the rates**
- **The close calendar and control owners**
- The replay recipe: the exact sequence of reads that produced the realization series and the AR tie-out

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist any patient identifier, patient balance, date of service, diagnosis or clinical detail.**
Not in any form, not for any reason. **This is absolute** — PHI does not belong in a skill bundle, and
nothing about convenience changes that. **Also never persist realization rates, reserve balances, AR
figures or write-off amounts** — all state, and all of it moves.

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / Northbrook
Family Health PC — gross charges recorded, contractual to 4910, charity care to 4930, payer classes on
Class, bad debt treated as price concession" — not "contractual to 4910". **Account maps and payer
structures are entity-specific**, and applying one practice's mapping to another misstates net revenue in
both. Record the chosen **scenario** (single vs multi) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's.**

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One provider, one AR, one realization
series.

**Multi-entity.** Common in healthcare, and the structures matter:

- **A professional corporation and a management services organisation.** The PC bills and collects; the MSO
  provides staff, premises and administration under a management agreement. **Revenue sits in one entity and
  most costs in the other**, so **neither entity's margin means anything alone.** Read both, and say which
  is which.
- **Multiple practice sites or specialties.** Steps 0–6 run **once per entity**, each call targeting exactly
  one `data_source_id`, every figure carrying its entity's `display_name`. **Realization differs by
  specialty and by site** — payer mix and contracts differ — so **never apply one entity's realization rate
  to another.**
- **A hospital and its employed physician group** have entirely different payer dynamics and reserve
  profiles. Same rule.
- **Intercompany management fees** move margin between entities without changing group results. See
  `consolidation-and-eliminations`; they are eliminated on consolidation and must not be read as third-party
  cost.
- **Payer contracts are usually negotiated at group level but perform differently per site.** The contract
  is one `[manual]` input; **the realization it actually delivers is per-entity and `[auto]`.**

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict per company
file.
