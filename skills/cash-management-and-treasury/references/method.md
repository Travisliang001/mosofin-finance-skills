<!-- cash-management-and-treasury · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding)
- Step 1 — Map the current cash landscape
- Step 2 — Design the bank account structure
- Step 3 — Liquidity policy
- Step 4 — Short-term investment policy
- Step 5 — Payment / disbursement controls
- Step 6 — FX management
- Step 7 — Borrowing facility management
- Step 8 — Treasury KPIs and reporting
- Step 9 — Documentation and governance
- Step 10 — Output
- Step 11 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with
plain-language wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool
added.

**Never drop a task because no tool covers it.** In this skill the control layer is largely
`[manual]` by nature, and recording that honestly is the difference between a policy document and a
false assurance.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding)

Pull the `[auto]` / `[gated]` reads. **Batch independent reads into one message** — the account list,
the balances, the movement and the fee history do not depend on each other. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries — and in a
multi-entity treasury review you are reading several files in turn, so passing the right one matters.

Typical opening batch, per in-scope entity:

- *`search_accounts`* — **every cash, bank and investment account**, active and inactive — usually
  **[auto]**
- *`get_balance_sheet`* / *`get_trial_balance`* — **balances per account** — usually **[auto]**
- *`get_general_ledger`* on each cash account — **movement, and therefore dormancy** — usually
  **[auto]**
- *`get_cash_flow`* — inflow and outflow volumes and their shape — usually **[auto]**
- *`search_deposits`* / *`search_payments`* — inflow mechanics and volumes — usually **[auto]**
- *`search_bill_payments`* / *`search_purchases`* — outflow mechanics and volumes — usually **[auto]**
- *`search_transfers`* — **movements between the entity's own accounts**, which reveal the informal
  concentration structure already in use — usually **[auto]**
- *`search_payment_methods`* — how payments are actually made here — usually **[auto]**
- *`get_profit_and_loss`* — bank fees and interest earned, for the KPI set — usually **[auto]**
- *`get_company_info`* — legal name, currency, country — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — it cannot support a liquidity policy, a
counterparty limit, or a decision to close an account.

## Step 1 — Map the current cash landscape

**The map is the foundation — most entities have more accounts than they realize.** This is the step
the workspace supports best, so do it thoroughly before designing anything.

- **All bank accounts by entity, currency, bank, purpose, balance, and signatories** — **[gated]**:
  **account, currency, balance and entity are [auto]** (*`search_accounts`*, *`get_balance_sheet`*);
  **bank, purpose and signatories are [manual]**. Produce the automated columns and ask the user to
  complete the rest — a half-filled map with honest blanks beats a confident one that is guessed
- **Identify redundant accounts, single-use accounts, dormant balances** — **[auto]**, and the
  highest-value automated finding here. Read movement per account over the last twelve months
  (*`get_general_ledger`*): an account with no transactions, or with a handful of transfers in and
  out and nothing else, is a candidate for closure. Rank by balance held and activity level
- **Concentration of counterparty exposure (cash sitting at a few banks)** — **[gated]**: balances
  are **[auto]**, but grouping them by bank needs the `[manual]` account-to-bank map from above.
  **Do not present a concentration figure until accounts are mapped to banks**; grouping by account
  name is not counterparty analysis
- **Trapped cash** (regulatory or contractual restrictions on movement) — **[manual]**. Ask
  explicitly; a restricted account may look identical to an operating one in the chart of accounts

## Step 2 — Design the bank account structure

Principles:

- **Operating accounts** per entity for collections and disbursements
- **Concentration accounts** to pool cash within an entity, country, or currency
- **Investment accounts** for surplus to be invested
- **Restricted accounts** kept separate (escrows, regulatory)
- **Minimize the number of accounts to what's needed; close redundant ones** — **[auto]** to
  identify the candidates, from Step 1
- **Diversify counterparty risk where balances are material** — don't keep all cash at one bank if it
  exceeds your risk threshold

For multi-entity groups, consider — all **[manual]** to design, and all requiring review:

- **Cash pooling**:
  - **Physical pooling** — actual cash moved daily into a master account
  - **Notional pooling** — balances offset for interest purposes **without moving cash**

  Subject to legal, tax, and regulatory constraints in each jurisdiction.
- **In-house bank** structure for larger groups — an entity providing banking services to affiliates

**These structures affect intercompany balances (`intercompany-reconciliation`) and have tax /
transfer-pricing implications — flag for tax and legal review.**

**[auto]** contribution worth making: *`search_transfers`* shows the movements already happening
between the entity's own accounts. That reveals the **informal concentration structure already in
operation**, which is usually undocumented and is the natural starting point for a formal one.

## Step 3 — Liquidity policy

Establish — **[manual]** to set, **[gated]** to inform:

- **Minimum cash balance** to maintain — a floor based on working capital needs, debt service, and
  stress scenarios. **[auto]** to compute the inputs: average monthly operating outflow gives the
  natural unit (see days of cash on hand in Step 8)
- **Operating cash buffer** above the floor for normal volatility. **[auto]** to measure that
  volatility — the actual variation in monthly net cash flow is readable, so the buffer can be sized
  from observed behaviour rather than a round number
- **Surplus threshold** above which excess goes to investments or debt paydown
- **Reserve for specific commitments** (taxes, debt maturities, distributions) — **[manual]** for the
  commitments themselves

**The 13-week forecast (`cash-flow-forecast-13-week`) tests the policy against expected cash
positions.** Design the floor here; prove it survives there.

## Step 4 — Short-term investment policy

For surplus cash — **[manual]** throughout; this is policy, not data:

- **Eligible instruments** (treasuries, commercial paper, money market funds, time deposits, repo) by
  credit quality and maturity
- **Maximum maturity and weighted-average maturity**
- **Concentration limits per issuer / counterparty**
- **Permitted currencies**
- **Approval process for investments**

**Policy goals (in typical order): safety (preservation of principal), liquidity (ability to meet
needs), yield (last priority).** That ordering is the whole of treasury investment policy in one
line, and it is the line most often inverted in practice when rates are attractive.

**[auto]** contribution: identify **what is currently held** — investment and deposit accounts and
their balances (*`search_accounts`*, *`get_balance_sheet`*) — so the policy is written against the
actual portfolio rather than a blank page.

## Step 5 — Payment / disbursement controls

**Every item in this step is `[manual]` in an accounting-only workspace.** Mosofin cannot see
approvals, access rights or signatories. Design the controls; do not report them as operating.

- **Approval thresholds**: tiered approvals by payment size
- **Dual control** for high-value or unusual payments
- **Payment runs**: scheduled vs. ad hoc; cutoff times — **[auto]** to observe the *actual* pattern
  (*`search_bill_payments`* by date), which often differs from the stated policy and is a finding in
  itself
- **Wire vs. ACH vs. check**: appropriate use per situation — **[auto]** to see the actual mix
  (*`search_payment_methods`*, *`search_bill_payments`*); wires used where ACH would do is both a
  cost and a risk finding
- **Fraud prevention**: **positive pay** (the bank checks each cheque against a list you sent),
  **account verification**, **callback procedures for new payee setup**, **segregation of duties
  between payment initiation and approval**
- **Bank account access controls**: who has online access, what permissions, **periodic review of
  access**

**Coordinate with `sox-controls-design-and-testing` for the control framework. Payment fraud (e.g.
business email compromise) is a major risk — controls matter.**

**[auto]** contribution, and a genuinely useful one: **detect new payees created shortly before a
large payment** (*`search_vendors`* against *`search_bill_payments`*). That pattern is the signature
of business email compromise, and while the books cannot show the callback that should have
happened, they can show the payment that warrants asking about it.

## Step 6 — FX management

If the entity has FX exposure — **[gated]**:

- **Identify exposures** — **transactional** (payables / receivables in foreign currency) and
  **translational** (foreign subsidiaries). **[auto]** in part: foreign-currency accounts, and
  invoices and bills in other currencies, are visible (*`search_accounts`*, *`search_invoices`*,
  *`search_bills`*), which sizes the transactional exposure
- **Policy on hedging**: what to hedge, instruments permitted (forwards, options), counterparties,
  tenors, accounting (**hedge accounting**) — **[manual]**
- **Approval and execution authority** — **[manual]**
- **Reporting on exposures and hedges** — **[gated]**

No accounting datasource supplies FX rates or hedge valuations; both are **[manual]**.

## Step 7 — Borrowing facility management

Coordinate with `debt-and-covenant-tracking` — **[manual]** for terms, **[auto]** for what has been
drawn and repaid:

- **Available facilities, drawn / undrawn, covenants, maturities** — the **drawn** balance and its
  movement are readable (*`get_general_ledger`* on the debt accounts); **the limit, the undrawn
  availability and the covenants are not**
- **Use of revolver for working capital management**
- **Cash sweep arrangements where they exist**

**Undrawn capacity is not available capacity** — a borrowing base or a covenant may restrict it. Never
present a facility limit as liquidity without the terms confirmed.

## Step 8 — Treasury KPIs and reporting

Establish treasury KPIs to monitor. Verdicts vary sharply, so mark each on the dashboard:

- **Cash balance and trend** — **[auto]**
- **Concentration by bank / counterparty** — **[gated]**: needs the account-to-bank map
- **Days of cash on hand** (cash ÷ daily operating outflow) — **[auto]**, and one of the most useful
  single numbers in treasury: both the numerator and the denominator are derivable
- **Investment portfolio yield, weighted-average maturity, credit quality** — **[manual]** except for
  the balances held
- **Idle / non-yielding cash %** — **[gated]**: balances are **[auto]**, which accounts earn interest
  is **[manual]** (though interest posted per account is a strong signal)
- **Forecast accuracy** (`cash-flow-forecast-13-week`) — **[auto]** once that forecast is running
- **FX exposure and hedge coverage** — **[gated]** for exposure, **[manual]** for hedges
- **Bank fees** — **[auto]** (see `bank-fee-and-interest-analysis`)

**Build a treasury dashboard (link to `kpi-dashboard-builder`).** Mark each KPI with its verdict, so
a reader knows which numbers are measured and which are reported by hand.

## Step 9 — Documentation and governance

- **Written treasury policy approved at the appropriate level** — **[manual]**
- **Authority matrix** — who can open / close accounts, sign payments, approve investments, execute
  FX — **[manual]**, and the single most important document this skill produces, because every
  control in Step 5 depends on it
- **Periodic review of bank relationships, fees, services** — **[gated]**; the fee side is **[auto]**
- **Treasury risk reporting to executive / board** — **[manual]**

## Step 10 — Output

Deliver an `.xlsx` workbook and a policy document.

**Sheet 1: Bank Account Map**

Entity, currency, bank, purpose, balance, signatories; redundancies / dormants flagged. **Mark each
column's source** — balance and currency from the books, bank and signatories from the user. Add a
header block: workspace name; each in-scope company file by `display_name`; each excluded one and
why; whether any figure rests on `mock` data.

**Sheet 2: Recommended Structure** — operating / concentration / investment / restricted accounts;
pooling structure if applicable, **with the tax and legal review flag on its face**.

**Sheet 3: Liquidity Policy** — minimum cash, buffer, surplus threshold, reserves, **with the
observed volatility the buffer was sized from**.

**Sheet 4: Investment Policy** — eligible instruments, limits, approval matrix.

**Sheet 5: Payment Controls** — approval thresholds, dual control, fraud prevention. **Headed:
designed, not tested.**

**Sheet 6: FX Exposure & Policy** — exposures, hedging policy.

**Sheet 7: Treasury KPIs** — dashboard data, **each KPI marked auto / gated / manual**.

**Sheet 8: Counterparty Risk** — concentrations by bank. **Only populated once accounts are mapped
to banks**; otherwise state that the mapping is outstanding.

**Sheet 9: Coverage — NEW, Mosofin-specific**

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used | Policy (enabled / permission / disabled) | `mock` | Gap — what could not be evidenced and who owns it |

Every row in Step 5, and the bank-identity and signatory columns of Step 1, read `manual`. That is
the correct, expected result.

**Document: Treasury Policy** (as a Word document where the host can make one)

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming:** `Treasury_[YYYY]_[EntityName]`

In a multi-entity run, `[EntityName]` is the company file's `display_name` for per-entity outputs,
plus a group file for the structure and policy. Every file states which datasources and
`display_name`s it covers.

**Grounding:** every figure traces to a tool result in this conversation or to labelled
user-supplied evidence. End with a single **Data sources** line grouping calls by datasource. Where
the data does not cover something, **name the tool that would have covered it — or state that none
exists**, as with signatories — instead of estimating.

## Step 11 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask
— explicitly, at that point, not earlier — whether to save this as their own customized version. A
general "yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The account-to-bank-and-purpose map** — which account is at which bank, for what, at which
  entity. The highest-value artefact here: it is pure `[manual]` knowledge, it unlocks the
  counterparty concentration KPI, and it is otherwise rebuilt from scratch every review
- **The liquidity policy thresholds**: minimum, buffer, surplus, reserves — and the basis each was
  set on
- **The investment policy**: eligible instruments, limits, maximum maturity, concentration caps
- **The authority matrix**: who may open accounts, sign payments, approve investments, execute FX
- **Counterparty limits per bank**, and the risk-appetite basis behind them
- **Which accounts are restricted or trapped**, and why
- **The FX hedging policy** and the exposures it covers
- The replay recipe: the exact sequence of reads that produced the landscape map

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files;
set `datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference
files alongside the installed skill.

**Never persist bank account numbers, online banking credentials, signatory names with their
authority levels, or cash balances.** Account numbers and signatory lists are precisely what a
payment fraudster needs, and balances are sensitive and stale immediately. Persist **account
*names*, the bank each sits with, and the policy** — never the credentials or the amounts.

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks /
Northbrook Trading — Operating account at Bank A, floor $250k, counterparty cap $500k per bank" —
not "floor $250k". Entities have different banks, different floors and different restrictions, and
an unlabelled counterparty cap applied to the wrong company file either blocks a legitimate balance
or permits an excessive one. Record the chosen **scenario** (single vs multi, whether cash can move,
and which set) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's** — and a cash balance is state.

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is
no longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** Steps 1, 3, 4, 5, 6, 8 and 9 apply in full; Step 2's pooling structures largely do
not. One landscape map, one policy.

**Multi-entity.** The landscape map runs **once per entity**, each call targeting exactly one
`data_source_id`, every account and balance carrying that entity's `display_name`. Then the design
work is genuinely group-level:

- **Ask first whether cash can actually move.** Currency controls, minority shareholders, loan
  covenants and joint-venture agreements all block transfers. **A pooling design proposed where cash
  is trapped is worse than none** — it produces a group liquidity figure nobody can rely on.
- **Group cash is only spendable cash.** Report total group cash **and** the subset that can actually
  be moved to where it is needed. These are frequently very different numbers, and only the second
  one is liquidity.
- **Pooling creates intercompany positions.** Physical pooling moves real money and creates real
  intercompany loans requiring arm's-length interest; notional pooling does not move money but may
  still create cross-guarantees. Both need tax and legal review before design, not after and `intercompany-reconciliation`.
- **Counterparty concentration is a group exposure.** Three entities each holding a comfortable
  balance at the same bank may exceed the group's risk appetite in aggregate. Aggregate by bank
  across entities, not within them.
- **An entity with no connected file still holds cash.** Name it as a gap in the map rather than
  producing a group total that silently excludes it.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict per
company file.
