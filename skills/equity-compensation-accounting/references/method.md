<!-- equity-compensation-accounting · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding)
- Step 0b — Reconcile what was recorded (Mosofin addition)
- Step 1 — Classify the award: equity-settled vs. cash-settled
- Step 2 — Determine grant-date fair value
- Step 3 — Analyze the vesting conditions
- Step 4 — Determine the expense recognition pattern
- Step 5 — Handle forfeitures
- Step 6 — Build the expense schedule and entries
- Step 7 — Handle exercises, settlements, and modifications
- Step 8 — Build the award roll-forward and disclosures
- Step 9 — Coordinate with related areas
- Step 10 — Output
- Step 11 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Never drop a task because no tool covers it.** In this skill the award data and the valuations are
legitimately `[manual]`, and recording that is the honest result.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding)

Pull the `[auto]` / `[gated]` reads. **Batch independent reads into one message** — the expense accounts,
the equity accounts, the cash receipts and the departments do not depend on each other. Never serialize
them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`search_accounts`* — **the SBC expense, APIC, common stock and any cash-settled liability accounts** —
  usually **[auto]**
- *`get_profit_and_loss`* by period **and by department / class** — **the expense recorded and its
  functional split** — usually **[auto]**
- *`get_general_ledger`* on the SBC and equity accounts — **every movement, which is where the manual
  journals live** — usually **[auto]**
- *`get_balance_sheet`* / *`get_trial_balance`* — **APIC and common stock balances**, and any cash-settled
  liability — usually **[auto]**
- *`search_journal_entries`* — **the SBC entries themselves**, since this is almost always posted by
  journal — usually **[auto]**
- *`search_deposits`* — **cash received on option exercises** — usually **[auto]**
- *`search_employees`* — the recipient population, where employees are set up — usually **[auto]**
- *`search_departments`* / *`search_classes`* — the functional lines for allocation — usually **[auto]**
- *`get_company_info`* — legal name, currency, year-end — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — SBC expense flows into published results, the tax
provision and the cash flow statement, so a fixture-based figure propagates widely.

## Step 0b — Reconcile what was recorded (Mosofin addition)

**Run before Step 1.** SBC is nearly always posted as a manual journal from a schedule maintained
elsewhere, which makes it unusually prone to drift.

**[auto]**, three comparisons:

1. **Expense recorded vs. expense per the schedule.** Read the SBC expense account for each period
   (*`get_general_ledger`*, *`get_profit_and_loss`*) and compare it to the schedule supplied. **A
   difference means the schedule is stale, an entry was missed, or an entry was posted twice** — and
   because nobody reconciles a non-cash expense, these persist for years.
2. **APIC movement vs. cumulative expense.** For equity-settled awards the credit goes to APIC, so
   **cumulative SBC expense should reconcile to the APIC movement**, adjusted for exercises and issuances.
   A gap points to a missing credit or a misposted entry.
3. **Exercise proceeds through cash.** Option exercises bring **cash in** (*`search_deposits`*,
   *`get_general_ledger`*). Compare cash received against exercises reported in the roll-forward:
   **cash with no exercise recorded, or an exercise with no cash, is a completeness finding.**

Where any comparison cannot be run, **record it as not performed** rather than reporting agreement.

## Step 1 — Classify the award: equity-settled vs. cash-settled

**[manual]** — the settlement terms are in the plan document:

- **Equity-settled** (settled in shares — most options, RSUs, RSAs): measured at **grant-date fair value,
  not remeasured afterward.** Expense recognized over the service period with a credit to equity (**APIC**).
- **Cash-settled** (settled in cash based on share value — e.g. SARs settled in cash, phantom stock):
  treated as a **liability**, **remeasured to fair value each period** until settlement, with expense
  adjusted accordingly.

**This classification drives the entire accounting. Confirm settlement type.** **[auto]** cross-check: a
cash-settled award produces a **liability** on the balance sheet; an equity-settled one produces an equity
credit. **Where the accounts show a liability but the awards are described as equity-settled — or the
reverse — one of the two is wrong**, and it is worth resolving before anything else.

## Step 2 — Determine grant-date fair value

**[manual]** throughout:

- **RSUs / RSAs** (full-value awards): fair value ≈ **share price at grant**, less the present value of
  dividends not received during vesting, if applicable
- **Options / SARs**: fair value from an **option-pricing model** — **Black-Scholes-Merton** for simple
  awards; **lattice or Monte Carlo** for complex or market-condition awards. Inputs: **share price, strike,
  expected term, volatility, risk-free rate, dividend yield**
- **ESPP**: fair value reflects **the discount and any look-back feature**

**The skill applies the model and recognition; if the entity needs the fair value computed, note the inputs
required and flag valuation-specialist involvement for complex awards or hard-to-value private-company
shares.**

**Record the valuation's source and date against every grant.** For a private company these valuations are
periodic and dated, and using a stale one across a later grant is a real and common error.

## Step 3 — Analyze the vesting conditions

Vesting conditions determine recognition, and the three types behave very differently — **[manual]** to
classify:

- **Service condition** (time-based, e.g. vest over 4 years): **recognize expense over the service period
  if the employee stays.**
- **Performance condition** (non-market, e.g. revenue or EPS target): **recognize if and when the condition
  is probable; expense trued up based on probability of achievement. If not probable, no expense**
  (reversed if previously recognized).
- **Market condition** (e.g. share price target, TSR): **factored into grant-date fair value** via the
  valuation model. **Expense is recognized regardless of whether the market condition is met, as long as
  service is rendered — a key and counterintuitive rule.**

**Identify each award's condition type — it changes whether and how expense is recognized.**

The contrast between the last two is the single most misunderstood point in this area: **a missed
performance target reverses the expense; a missed share-price target does not.** The reasoning is that the
market condition was already priced into the grant-date value, so the cost was incurred whether or not the
shares performed.

## Step 4 — Determine the expense recognition pattern

Recognize the grant-date fair value over the **requisite service period** — **[auto]** arithmetic on
**[manual]** terms:

- **Graded vesting** (e.g. 25% per year): choose the **attribution method** —
  - **Accelerated / graded** — each tranche expensed over its own vesting period, so the expense is
    **front-loaded**. **Required under IFRS 2; an option under US GAAP**
  - **Straight-line** — total expense spread evenly over the full period. **Permitted under US GAAP for
    service-only awards**
- **Cliff vesting** (all at once at the end): **straight-line over the period to the cliff**

**Build the period-by-period expense for each award / tranche.** The attribution choice materially changes
each period's charge from identical facts, so **state which method was used** — and keep it consistent.

## Step 5 — Handle forfeitures

- **US GAAP**: a **policy choice** — **estimate expected forfeitures upfront** (and true up), **OR account
  for forfeitures as they actually occur**
- **IFRS 2**: forfeitures due to failure to meet a service or non-market performance condition are
  **reflected by truing up to actual** — essentially as-they-occur for those

**Apply the entity's policy.** If estimating, apply the forfeiture rate to reduce expense, **then true up to
actual forfeitures**. If as-they-occur, **reverse expense for unvested awards when forfeited**.

**Note: market conditions are NOT forfeiture events — expense stands even if the market condition isn't
met** (per Step 3).

**[auto]** contribution: employees becoming inactive (*`search_employees`*) is a leaver signal, and leavers
are what drive forfeitures. It is a prompt to check the cap table, not a substitute for it — an employee
may leave with vested awards intact.

## Step 6 — Build the expense schedule and entries

For each period. `DR` is a debit, `CR` a credit. **Mosofin does not post** — these are proposals:

```
DR  Stock-Based Compensation Expense        $period expense
    CR  Additional Paid-in Capital (equity-settled)   $expense
    (or CR  Liability for cash-settled awards)
```

**Allocate the expense to the right functional lines (R&D, S&M, G&A, COGS) based on where the recipients
work.** **[gated]**: the departments exist and the current split is readable, but **mapping each recipient
to a function is `[manual]`** — the cap table names people, the ledger names departments, and nothing joins
them automatically.

**For cash-settled awards, remeasure the liability each period to fair value and adjust expense.** That
remeasurement needs a current valuation every period, not just at grant — a materially larger ongoing
burden, and worth flagging when the classification is confirmed.

Use the **real account names from the connected chart of accounts** (*`search_accounts`*, **[auto]**).

## Step 7 — Handle exercises, settlements, and modifications

**Option exercise** (equity-settled):
```
DR  Cash (exercise proceeds)
DR  APIC (the previously-recognized comp in APIC)
    CR  Common Stock (par)
    CR  APIC (excess)
```
**[gated]**: **the cash leg is `[auto]`** — this is the Step 0b completeness check — the rest is
`[manual]`.

**RSU vesting / settlement**: shares issued; **the accumulated APIC moves to common stock / APIC.** No cash
arrives, which is why RSU vesting is easy to miss entirely in the accounts.

**Modifications** (repricing, extending, accelerating): **compare the fair value immediately before and
after the modification; recognize incremental fair value as additional expense. Modifications are complex —
flag for careful treatment.** Two valuations are needed, both `[manual]`, both at the modification date.

**Cancellations / settlements**: **accelerate remaining expense** (cancellation) **or per the settlement
terms.**

## Step 8 — Build the award roll-forward and disclosures

Roll-forward of the award population — **[manual]**, from the cap table:

```
Outstanding (opening)  +  Granted  −  Exercised/Settled  −  Forfeited  −  Expired  =  Outstanding (closing)
                                                                                       of which Vested / Exercisable
```

**With weighted-average exercise prices and remaining contractual terms.**

Disclosure figures (for `notes-to-financial-statements`):

- **Total comp expense for the period** (and by award type) — **[auto]** where the accounts separate them
- **Unrecognized compensation cost and the weighted-average period to recognize it** — **[gated]**;
  computable from the schedule
- **Valuation assumptions** (volatility, expected term, risk-free rate, dividend yield) — **[manual]**
- **The award roll-forward** — **[manual]**
- **Intrinsic value / fair value of exercises and vests** — **[manual]**

## Step 9 — Coordinate with related areas

This step matters more than it looks: **SBC touches four other skills, and they must agree.**

- **The APIC build feeds `statement-of-equity-changes`** — **[auto]** for the movement
- **The book-tax difference** — the timing and amount of the tax deduction versus book expense — **feeds
  the tax provision work**. The deduction is frequently based on **intrinsic value at exercise or
  vest**, not grant-date fair value, so the two diverge substantially
- **The non-cash expense add-back feeds `cash-flow-statement-indirect-method`**
- **Payroll tax on equity comp** (where applicable) **feeds payroll skills** — vesting and exercise are
  taxable events with real cash consequences, even though the expense itself is non-cash

One cross-reference worth stating explicitly: in a quality-of-earnings review, **SBC should not be
added back to adjusted EBITDA** — it is a real, recurring economic cost. The same figure is a legitimate
add-back in the cash flow statement and an illegitimate one in a QofE bridge, which confuses people
regularly.

## Step 10 — Output

Deliver an `.xlsx` workpaper.

**Sheet 1: Expense Summary** — total SBC expense by period and functional line; unrecognized cost
remaining. Add a header block: workspace name; the entity by `display_name`; each excluded company file and
why; **which entity issues the shares**; whether any figure rests on `mock` data.

**Sheet 2: Award-by-Award Expense Schedule** — each grant / tranche, fair value, vesting, attribution,
period expense. **With the valuation source and date per grant.**

**Sheet 3: Vesting Condition Analysis** — service / performance / market classification and treatment per
award.

**Sheet 4: Forfeiture Treatment** — policy, rate (if estimated), true-ups.

**Sheet 5: Award Roll-Forward** — population movement with weighted averages.

**Sheet 6: Journal Entries** — period expense, exercises, settlements, modifications, marked as
**proposals**.

**Sheet 7: Disclosures** — assumptions, unrecognized cost, roll-forward — disclosure-ready.

**Sheet 8: Open Items / Specialist Review** — complex valuations and modifications flagged.

**Sheet 9: Recorded vs. Schedule — NEW, Mosofin-specific**

| Check | Per schedule | Per ledger | Difference | Explanation |

Covering the three Step 0b comparisons: period expense, cumulative expense against APIC movement, and
exercise proceeds against cash received.

**Sheet 10: Coverage — NEW, Mosofin-specific**

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used / external source | As-at date | Policy | `mock` | Gap |

Every fair value and every award-population row reads `manual` with its source. That is the correct entry.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming:** `Equity_Comp_[YYYY]_[EntityName].xlsx`

`[EntityName]` is the company file's `display_name`. Every file states which datasource and `display_name`
it covers.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where the data does not
cover something — the award population, every fair value — **name the source required** instead of
estimating.

## Step 11 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The plan terms**: award types in issue, standard vesting patterns, whether awards are equity- or
  cash-settled
- **The attribution method** and the **forfeiture policy** — both are elections that must stay consistent,
  and inconsistency is itself a finding
- **The framework** and the elections made within it
- **The account map**: SBC expense, APIC, common stock, cash-settled liability
- **The functional allocation basis** — how recipients map to departments, which is the join the systems
  do not make
- **The valuation source and cadence** — who values the shares and how often. **Not the values**
- **The recipient-to-entity map** in a group, so the expense lands in the right books
- The replay recipe: the exact sequence of reads that produced the recorded expense and the reconciliation

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist individual grants, recipient names, share counts, strike prices, fair values or the cap
table.** Individual equity holdings are personal financial data about identifiable people, and the cap
table is among the most confidential documents a company has. **Persist the plan design and the policies;
never the awards.**

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / Northbrook
Holdings (issuer) — equity-settled RSUs and options, straight-line attribution, forfeitures as they occur,
SBC to Share Scheme Costs, recharged to subsidiaries" — not "straight-line attribution". **In a group the
issuer and the employer differ**, and an unlabelled policy applied to the wrong company file puts the
expense in the wrong entity's results. Record the chosen **scenario** (single vs multi, and which entity
issues) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's** — and the award population, the fair values and the unrecognised cost are all state.

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One plan, one expense, one APIC
movement.

**Multi-entity.** Steps 0–10 run **once per entity**, each call targeting exactly one `data_source_id`,
every award and expense carrying its entity's `display_name`. Then the structural point:

- **The issuer and the employer are usually different entities.** Awards are over the parent's shares;
  the recipients work for subsidiaries. **The expense belongs to the entity that receives the services** —
  the employer — while **the equity credit belongs to the issuer**. In each subsidiary's own accounts the
  credit is typically a capital contribution from the parent rather than APIC.
- **Many groups recharge the cost** from the employer to the parent, or vice versa, under an agreement.
  **Whether a recharge exists changes both entities' results**, and it is `[manual]` — the arrangement is
  a contract, not a ledger field. Ask.
- **On consolidation the group sees one expense and one equity credit**, whatever the internal routing —
  so a group-level SBC figure should reconcile to the plan's total expense regardless of how it was pushed
  down. That is a useful check.
- **Recipient-to-entity mapping is the join nobody automates.** The cap table lists people; the ledger
  lists entities and departments. Store the mapping at Step 11 — it is the thing that makes the next
  period fast.
- **Payroll tax on vesting arises where the employee is employed and taxed**, which may be a third
  jurisdiction again.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict per company
file.
