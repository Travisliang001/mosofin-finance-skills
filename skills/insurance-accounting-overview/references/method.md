<!-- insurance-accounting-overview · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding) — Mosofin addition
- Step 0b — Settle the model and read the account signature (Mosofin addition)
- 1) Premium and unearned premium
- 2) Claims and loss reserves
- 3) Reinsurance
- 4) Acquisition costs and commissions
- 5) Investment income (if carrier)
- Step 6 — Close deliverables
- Step 7 — Output
- Step 8 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


The original's five-area workflow map, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict per item, and the typical evidence tool added.

**Never drop a task because no tool covers it.** The actuarial and policy-system items are legitimately
`[manual]`, and naming their owners is what a close map is for.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding) — Mosofin addition

**Batch independent reads into one message** — the accounts, the balances, the revenue and the bank
positions do not depend on each other. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`search_accounts`* — **premium receivable, unearned premium, loss and LAE reserves, reinsurance
  recoverable and payable, commissions payable and receivable, DAC, and any trust or fiduciary bank
  account** — usually **[auto]**. **The account list alone largely reveals the business model**, and is
  worth reading before the interview concludes
- *`get_balance_sheet`* / *`get_trial_balance`* — **all of the above as balances**, opening and closing —
  usually **[auto]**
- *`get_profit_and_loss`* by period — **commission and fee income, or premium and losses** — usually
  **[auto]**
- *`get_general_ledger`* on **the reserve, recoverable and trust accounts** — movements — usually **[auto]**
- *`search_accounts`* filtered to bank accounts — **to identify trust versus own-funds accounts** — usually
  **[auto]**
- *`get_aged_receivables`* / *`get_aged_payables`* — **premium receivable and insurer payable ageing** —
  usually **[auto]**
- *`search_invoices`* / *`search_bills`* — commission billings and insurer settlements — usually **[auto]**
- *`get_company_info`* — legal name, currency, **country** — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — **and a client money reconciliation performed on
fixture balances is worse than none**, because a shortfall is a reportable regulatory event and a false
clean result is a false assurance.

## Step 0b — Settle the model and read the account signature (Mosofin addition)

**Run before the workflow map.** **[auto]**, and it takes one read:

**The chart of accounts carries a signature.**

- **Loss reserves, IBNR, unearned premium, reinsurance recoverable** → **carrier**
- **Commission income, insurer payable, client money / trust bank** → **broker or MGA**
- **Both** → ask; it may be a group with mixed entities, or an MGA with delegated authority binding on
  behalf of carriers.

**Where the account signature contradicts the stated business model, raise it before proceeding** — it
usually means either the model was described loosely or the chart was inherited from a different business.

**Then state the profile plainly in the output**: which of the two capability columns applies, and therefore
which parts of the close map the workspace can evidence and which it cannot.

## 1) Premium and unearned premium

- **Gross written premium (GWP)** — **[gated]**. **Carrier**: `[manual]` from the policy system, with the
  GL holding a posted total. **Broker / MGA**: premium usually flows through as client money rather than
  revenue — **what is readable is the flow, not the entity's income.**
- **Unearned premium reserve (UPR) for coverage not yet provided** — **[gated]**. **The balance is
  `[auto]`; the calculation is `[manual]`**, because earning depends on policy inception and expiry dates
  held in the policy system. **A UPR cannot be recomputed from a ledger.**
- **Premium receivables and cash** — **[auto]**. Balances, ageing and receipts are all readable, and
  **premium receivable ageing is a real credit and collection control** — see `ar-aging-and-collections`.

**Mosofin check — the UPR reasonableness test.** **[gated]**: for a book of broadly annual policies written
evenly, **UPR should sit near half of annual written premium.** A ratio far from that is not an error, but
it is a question worth asking — and it can be computed from figures the ledger holds. **Present it as a
reasonableness indicator, never as a recomputation.**

## 2) Claims and loss reserves

- **Case reserves (claim-level estimates)** — **[manual]**. Set claim by claim in the claims system. **The
  GL holds the total; the ledger cannot see a single claim.**
- **IBNR (incurred but not reported)** — **[manual]**, always, and **actuarial by definition.** It is an
  estimate of claims that have happened and **that nobody has told the insurer about yet**. Nothing in an
  accounting system contains information about events not yet reported. **Never estimate it.**
- **Loss adjustment expenses (LAE)** — **[manual]**. The cost of handling claims, split between allocated
  and unallocated; also actuarial.

**[auto]** contribution, and it is limited but real: **the reserve balances and their movements are
readable**, so **a reserve roll-forward can be built and tied to the ledger** — opening, incurred, paid,
released, closing. **Development analysis, though, needs claims by accident year**, which is claims-system
data. **Loss development triangles cannot be built here.** Say so; the original names them in its
description and they are firmly `[manual]`.

## 3) Reinsurance

- **Ceded premium and reinsurance payable** — **[gated]**. Balances `[auto]`; **the cession calculation is
  `[manual]`**, from the treaty.
- **Reinsurance recoverables and credit risk** — **[gated]**. **The recoverable balance is `[auto]`;
  the counterparty credit assessment is `[manual]`** — there are no credit ratings on this surface.

**Two points worth stating in the close map:**

**Reinsurance does not discharge the obligation.** The insurer still owes the policyholder in full; the
recoverable is a separate claim on the reinsurer. **Presenting losses net of reinsurance without showing
gross obscures the actual exposure**, and gross and ceded should both appear.

**A recoverable is a credit exposure that can run for years.** **[auto]** support: **the ageing of the
recoverable balance is readable**, and a long-outstanding recoverable is the readable signal that something
is disputed or the counterparty is slow.

## 4) Acquisition costs and commissions

- **Commissions payable** — **[auto]**. Balance, ageing and settlement are all readable.
- **Deferred acquisition costs (DAC) where applicable** — **[gated]**. **The balance is `[auto]`; the
  deferral and amortisation pattern is `[manual]`**, because it follows the premium earning pattern, which
  follows policy dates.

**For a broker or MGA this is the revenue line, and it is substantially `[auto]`**: commission and fee
income by period, by insurer, by class where the dimension supports it. **Two `[auto]` checks worth having
in the close map:**

1. **Commission earned against premium placed**, where both are recorded — a rate check that catches
   under-collected commission.
2. **Clawback and cancellation experience** — credit notes and reversals against original commission, which
   indicates whether commission is being recognised too early on cancellable business.

## 5) Investment income (if carrier)

- **Interest / dividends** — **[auto]** where received into the entity's accounts.
- **Realized / unrealized gains** — **[gated]**: **realized gains are `[auto]`** once transacted;
  **unrealized gains need market values, which are `[manual]`** — the same rule as a business valuation and
  `derivatives-and-hedging-asc815`.

**For a carrier, investment income is a material earnings driver** and the investment portfolio usually
sits in a custodian's records rather than the ledger. **Name the custodian statement as the source.**

## Step 6 — Close deliverables

The original's five, with verdicts:

- **Premium rollforward and UPR schedule** — **[gated]**; balances `[auto]`, earning `[manual]`
- **Loss reserve rollforward (case + IBNR) and development analysis** — **[gated]** for the roll-forward,
  **[manual]** for development analysis
- **Reinsurance recoverable schedules** — **[gated]**; balances and ageing `[auto]`, treaty terms `[manual]`
- **Commission / DAC schedules** — **[auto]** for commissions, **[gated]** for DAC
- **Key reconciliations to GL** — **[gated]** by construction: **the GL side is always `[auto]`, the
  subledger side is `[manual]`** unless a policy or claims system is connected. **These reconciliations are
  the point of the close**, and each one should be reported with its difference quantified and its
  reconciling items listed.

**Mosofin addition — the client money reconciliation, for a broker or MGA.** **[auto]**, and it belongs at
the top of the deliverables for any regulated intermediary:

```
Trust bank balance(s)
  compared to
Amounts due to insurers  +  Amounts due to clients  +  Unallocated receipts
  =  Surplus or (shortfall)
```

**A shortfall is a regulatory breach**, typically reportable, and it can arise quietly — own-funds
commission left in the trust account, a client refund paid from the wrong account, an unallocated receipt
never matched. **Report the calculation with its date and its components**, and **surface unallocated
receipts with their age**, because they are the usual cause.

## Step 7 — Output

The original's outputs, delivered as an `.xlsx` workpaper:

**Sheet 1: Close Checklist Tailored to the Business Model** — every task, **its data source, its owner, its
due date, and its verdict** (`[auto]` / `[gated]` / `[manual]`). **This is the primary deliverable.** Plus
the header block: workspace name; the entity by `display_name` **with its business model**; each excluded
company file and why; whether any figure rests on `mock` data.

**Sheet 2: Required Data Sources and Owners** — what must come from the policy system, the claims system,
the actuary, the reinsurers and the custodian, **with named owners and cadences**.

**Sheet 3: Schedule Templates and Tie-Out Approach** — the roll-forward shapes for premium, reserves,
recoverables and commissions, **each showing the GL anchor it must tie to**.

**Sheet 4: Risk List** — **data completeness, reserve adequacy, reinsurance credit risk**, plus any risk the
`[auto]` reads surfaced: ageing recoverables, unallocated client money, commission clawback exposure.

**Sheet 5: GL Reconciliations** — each schedule against its GL account, **with the difference quantified,
including zero**, and reconciling items listed.

**Sheet 6: Client Money Reconciliation — NEW, Mosofin-specific, for brokers and MGAs** — the calculation
above, with components, date, and unallocated receipts aged.

**Sheet 7: Coverage — NEW, Mosofin-specific**

| Task | Entity (`display_name`) | Business model | Verdict | Tool used / external source | As-at date | `mock` | Gap |

**Every actuarial and policy-system row reads `manual` with its owner.** In a close-map skill **that is not
a gap — it is the deliverable**, since the whole purpose is to say who supplies what and when.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming (Mosofin addition — the original specifies none):**
`Insurance_Close_Map_[YYYY-MM]_[EntityName].xlsx`

Every file states which datasource and `display_name` it covers, and the business model.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where the data does not
cover something — IBNR, development triangles, treaty terms — **name the source required** instead of
estimating.

## Step 8 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The business model** per entity, and the capability profile that follows
- **The account map**: premium receivable, UPR, loss and LAE reserves, reinsurance recoverable and payable,
  commissions, DAC, **and specifically which bank accounts are trust accounts and which are own funds**
- **The close calendar**: every task, its owner, its source system, its due date — **the primary asset this
  skill produces**
- **The regulatory regime** and what the client money reconciliation must demonstrate
- **The actuary and the valuation cadence**
- **The reinsurance programme structure** — which treaties, which counterparties, renewal dates.
  **Not the balances**
- **The commission rate basis** by insurer or class, and the clawback terms
- **The DAC deferral and amortisation policy**
- The replay recipe: the exact sequence of reads that produced the balances and the client money position

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist reserve balances, IBNR figures, client money positions, recoverable balances or premium
amounts** — all state, and the client money position in particular is a point-in-time regulatory figure that
must be recomputed rather than recalled. **And never persist policyholder or claimant names, policy numbers,
or any claim detail** — these identify individuals, and claim information is sensitive personal data.

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / Northbrook
Insurance Brokers Ltd — broker, regulated, trust accounts 1050 and 1051, own funds 1010, commission income
4100, actuary n/a" — not "broker, regulated". **Trust account identification is entity-specific and
safety-critical**: applying one entity's account map to another could classify own funds as client money or
the reverse, which corrupts the one regulatory control this skill offers. Record the chosen **scenario**
(single vs multi, and which entities are regulated) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's.**

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One business model, one close map.

**Multi-entity.** Common in insurance, and the structures are meaningful:

- **A broking entity and a separate MGA.** Different regulatory permissions, different revenue, **and often
  different client money obligations.** Steps 0–7 run **once per entity**, each call targeting exactly one
  `data_source_id`, every figure carrying its entity's `display_name` **and business model**.
- **A carrier and its service company.** The carrier holds the risk and the reserves; the service company
  employs the staff and charges a management fee. **Neither entity's result means anything alone**, and the
  fee is eliminated on consolidation — see `consolidation-and-eliminations`.
- **Regulated and unregulated entities side by side.** **Client money rules attach to the regulated entity**,
  and money must not be commingled. **Never run one client money reconciliation across a group** — it is
  performed per regulated entity, against that entity's own trust accounts.
- **Never net client money across entities.** A surplus in one does not cure a shortfall in another; they
  are separate obligations to separate people.
- **Intra-group reinsurance** — a captive reinsuring the group's own risks — **eliminates on consolidation
  but is real in each entity's own statements.** Read both sides.
- **The business model may differ per file**, so **the capability profile is per entity too.** Do not
  present a group close map that implies uniform coverage.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict per company
file **and per business model**.
