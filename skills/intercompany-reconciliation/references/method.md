<!-- intercompany-reconciliation · method.md · read for: Stages 3–6 — the reconciliation itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding) — Mosofin addition
- Step 1 — Build the entity matrix
- Step 2 — Match transaction by transaction (where possible)
- Step 3 — Reconcile balances by entity pair
- Step 4 — Identify common mismatch causes
- Step 5 — Currency handling
- Step 6 — Settlement proposal
- Step 7 — Elimination entries
- Step 8 — Output
- Step 9 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Never drop a task because no tool covers it.** The rates and the agreement are legitimately `[manual]`.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding) — Mosofin addition

**This is the step where the parallel read matters most in the entire pack.**

**Batch every entity's reads into one message.** Each entity's ledger is independent of every other's —
**there is no reason to read them in sequence, and reading them together means every side is as at the same
instant.** For a six-entity group that is one round trip instead of six, and **it removes version skew as a
source of phantom mismatch.**

**Read per entity, not per pair.** For N entities you need **N reads**, not N(N−1)/2 — the pairs are formed
from the data afterwards.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, **per in-scope entity, all in one message**:

- *`get_company_info`* — **legal name and functional currency** — usually **[auto]**
- *`search_accounts`* — **the intercompany accounts**: IC receivable, IC payable, IC loan, IC revenue, IC
  expense — usually **[auto]**
- *`get_general_ledger`* on those accounts — **the IC ledger at transaction level, with references and
  dates** — usually **[auto]**
- *`get_balance_sheet`* / *`get_trial_balance`* — **the IC balances** — usually **[auto]**
- *`search_invoices`* / *`search_bills`* filtered to group counterparties — **the documents behind the
  entries, with their numbers** — usually **[auto]**
- *`search_customers`* / *`search_vendors`* — **how this entity names the other group members** — usually
  **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`. **Expect this often here** —
  it means a call omitted the entity.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap, **naming the entity, and
  marking every pair involving it accordingly.**
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag** **per entity**. `mock: true` on one side means **that pair is not reconciled** —
matching fixture data against real data produces a mismatch list that is entirely fictional.

## Step 1 — Build the entity matrix

**For each pair of entities (A, B), create:**

- **Entity A's IC Receivable from B** (and IC Payable to B)
- **Entity B's IC Payable to A** (and IC Receivable from A)

**These should mirror in equal-and-opposite amounts (after currency conversion).**

**For N entities, there are N(N−1)/2 pairs. Build the full matrix.**

**[auto]** to build, with the Mosofin addition that makes it honest:

**Mark each cell of the matrix with its reconcilability**, from Gate 1 and Gate 2:

| Both sides connected and readable | **Reconcilable** — proceed |
| One side `permission`-gated | **`[gated]`** — ask, then proceed |
| One side not connected, or `disabled` | **NOT RECONCILABLE** — report as such, name the missing side |
| One side returned `mock: true` | **NOT RECONCILABLE** — report as such |

**The matrix with these markings is itself a deliverable**, and it should appear before any numbers. **A
group where four of ten pairs cannot be reconciled has a reporting problem that matters more than the six
that can.**

## Step 2 — Match transaction by transaction (where possible)

**For each entity's IC ledger, attempt to match each line to a corresponding line in the counterparty's
ledger** — **[auto]**, and this is the core operation:

- **Match by reference number first** — invoice #, contract ID, transaction ID
- **If no reference, match by date + amount + counterparty**
- **If no match, mark as unmatched**

**Matching success patterns:**

- **1:1 match** — single line on each side, equal amounts → **matched**
- **1:N match** — one line on side A matches several lines on side B that sum → **matched as group**
- **N:N match** — lump on both sides reconciling several transactions → **matched as group**
- **Unmatched on either side** → **mismatch**

**Mosofin notes on making this work in practice:**

- **Reference numbers are readable** — document numbers on invoices and bills, and often carried into the
  memo of the counterparty's entry. **Match on them first**, as the original says, because they survive
  rate and timing differences that amount-matching does not.
- **Allow a date window.** The counterparty posts on receipt, not on issue. **A window of several days —
  agreed with the user, and stated — is normal**; a window wide enough to catch anything is not matching.
- **Report the match basis per line.** "Matched on reference" and "matched on amount and date alone" are
  different levels of confidence, and the second deserves a flag.
- **Never force a match.** Where the amounts differ, **record it as a matched pair with a difference**, not
  as a match. The difference is the finding.

## Step 3 — Reconcile balances by entity pair

**For each pair, compute** — **[gated]**: balances `[auto]`, conversion needs `[manual]` rates:

```
Entity A's IC Receivable from B (in A's functional currency, converted to group currency)
Entity B's IC Payable to A    (in B's functional currency, converted to group currency)

Difference                    = $X
```

**The difference should be zero (or near-zero due to FX). Investigate non-zero differences.**

**Report the difference for every pair, including zero.** A pair reported as "agreed" without a number is an
assertion; **"agreed, difference 0.00 in group currency" is evidence.**

**And separate the difference into its components** — this is what Step 6 of the output sheet is for:
**timing, FX, and true mismatch**. Lumping them together makes every pair look equally broken when most are
just late.

## Step 4 — Identify common mismatch causes

**Common reasons for IC mismatches** — with the Mosofin verdict on whether the workspace can detect each:

| Cause | Resolution | Detectable? |
|-------|-----------|---|
| **Cut-off timing** (A invoiced, B hasn't booked yet) | **Time difference; will resolve next period** | **[auto]** — the entry appears on one side with a date near period end and on the other after |
| **One side missed posting** | **Post the missing entry** | **[auto]** — unmatched with no later appearance |
| **Different amounts due to FX rate differences** | **FX translation gain / loss flows to CTA / FX reserve** | **[gated]** — visible once both sides are converted |
| **Different amounts due to one side including / excluding tax** | **Determine the correct treatment per IC policy** | **[auto]** — the difference equals the tax on the document |
| **Different classification** (one side as loan, other as service fee) | **Align per agreement** | **[auto]** — the accounts differ across the pair |
| **One side posted gross, other net** (commissions, rebates) | **Align per agreement** | **[auto]** — a consistent proportional difference |
| **Mark-up applied by one side not recorded by other** | **Per IC pricing policy** | **[gated]** — visible as a consistent percentage; **the policy is `[manual]`** |
| **Withholding tax deducted by paying entity not booked by receiving entity** | **Both should reflect the WHT** | **[gated]** — the difference equals a plausible WHT rate |
| **Settled transactions not cleared from open IC accounts** | **Apply settlements** | **[auto]** — a payment exists with the invoice still open |
| **Manual journal posted to IC account without informing the counterparty** | **Coordinate** | **[auto]** — a journal entry with no counterparty document |

**Assign a probable cause to every mismatch**, as the original's quality standard requires — **and label it
as probable.** The pattern is readable; the reason a human did something is not.

**One `[auto]` check the causes table implies but does not state:** **a journal entry posted directly to an
IC account, with no document behind it**, is the single most common source of unexplained mismatch, and it
is readable (*`search_journal_entries`*). **List them separately** — they are usually where the answer is.

## Step 5 — Currency handling

**When entities have different functional currencies:**

- **Each entity records IC transactions in its own functional currency**
- **The transaction itself may be denominated in either currency**
- **Mismatches commonly arise from different rates used by each side**

**Translation for matching:**

- **Convert each entity's IC balance to the group reporting currency** using the **period-end rate** for
  balance sheet items or the **transaction-date rate** for P&L items
- **After conversion, mismatches should be only timing-related, not FX-related**

**If using different FX rates between sides causes a mismatch, the resolution is NOT to force a match by
adjusting one side's books.** Instead:

- **Booking entity uses spot rate at transaction date for the IC P&L**
- **Counterparty mirrors at the same rate (per IC agreement)** — **if not, the difference becomes an FX
  translation difference handled at consolidation, often through CTA**

**[manual]** on every rate. **[auto]** on the currencies themselves — each entity's functional currency comes
from its profile, so **which pairs are cross-currency is known before any rate is applied.**

**Mosofin emphasis, because read-only makes it structural:** **this skill cannot adjust anyone's books.** It
proposes. **That is exactly the discipline the original asks for here** — an FX difference is a real
economic effect to be carried to CTA, not an error to be papered over.

**Order matters**: **translate, then compare.** Comparing local-currency figures across a cross-currency
pair produces a difference that means nothing.

## Step 6 — Settlement proposal

**For pairs with open balances that should be settled** — per IC policy or group treasury practice —
**[auto]** arithmetic on a `[manual]` policy:

- **Net the receivables and payables to one settlement amount**
- **Identify the paying entity and receiving entity**
- **Identify the settlement currency**
- **Document the settlement entry on both sides**

**Net per pair, not gross** — the original's own quality standard. **[auto]**: netting across all accounts
in a pair is straightforward once matched.

**Mosofin addition — ageing.** **[auto]**: **how long each open IC balance has been outstanding** is
readable, and **a long-aged intercompany balance is a different problem from a large one.** Balances that
have sat for several periods point at the process breakdown the edge cases call out — and they should drive
the settlement priority.

**Do not propose settling a mismatch.** Settle the agreed balance; **the disputed difference is resolved
first**, or the settlement just moves the problem.

## Step 7 — Elimination entries

**For consolidation, eliminate** — **[gated]**:

- **IC receivable on A vs. IC payable on B** — both eliminate against each other — **[auto]** once matched
- **IC revenue on A vs. IC expense on B** — eliminate — **[auto]** once matched
- **IC profit in inventory** — if A sold inventory to B at a mark-up that B still holds: **eliminate the
  unrealized mark-up** — **[manual]**: **it needs to know what B still holds and at what mark-up**, and
  neither is an IC ledger figure
- **IC dividends** — eliminate — **[auto]** where identifiable

**Build the elimination JEs at the consolidation level. These typically don't post to either entity's
individual books — they're consolidation-only entries.** **Mosofin posts nothing anywhere**, which matches
this exactly.

**The full consolidation process is separate work: hand these entries to whoever owns it.**

**Eliminate the agreed amount, and carry the difference explicitly.** Eliminating A's figure against B's
different figure leaves a residual that lands somewhere in the consolidated result — **usually silently.**

## Step 8 — Output

Deliver an `.xlsx` workpaper:

**Sheet 1: Entity Pair Summary**

| Pair | Entity A IC Position | Entity B IC Position | Difference | Status |

Add the Mosofin column: **Reconcilable?** — with **not-reconcilable pairs listed first**, naming the missing
or unreadable side. Plus the header block: workspace name(s); every group member by `display_name` with its
functional currency; each excluded or missing entity; the group reporting currency; whether any entity
returned `mock` data.

**Sheet 2: Transaction-Level Matching**

| Pair | Entity A Line | Entity B Line | Match Type | Amount | Difference | Reason |

Add **Match Basis** — reference, or amount-and-date alone — and flag the weaker basis.

**Sheet 3: Mismatches**

| Pair | Unmatched On Side | Amount | Probable Cause | Recommended Action |

Add **Age** and, as a separate block, **journal entries posted direct to IC accounts with no document**.

**Sheet 4: Settlement Proposal**

| Pair | Net Amount | Paying Entity | Receiving Entity | Settlement Currency | Suggested Settlement Date |

**Sheet 5: Elimination Entries** — for consolidation use. **Pass-through to `journal-entry-builder` for
posting in the consolidation ledger.** Marked as **proposals**.

**Sheet 6: Currency Reconciliation** — **for each pair, show original currency amounts, FX rates applied,
and converted amounts. Quantify FX-related differences vs. timing differences vs. true mismatches.** **The
three-way split is the point of this sheet** — most differences are timing.

**Sheet 7: Pair Matrix — NEW, Mosofin-specific** — the full N(N−1)/2 matrix with each cell's reconcilability
and its verdict. **The map of what this run could and could not do.**

**Sheet 8: Coverage — NEW, Mosofin-specific**

| Task | Pair / entity (`display_name`) | Verdict (auto / gated / manual) | Tool used / external source | As-at date | `mock` | Gap |

Recorded **per pair**, since a pair is only as readable as its weaker side.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming:** `IC_Reconciliation_[YYYY-MM].xlsx`

Every file names the workspace(s), the group members covered, and the pairs not reconciled.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where the data does not
cover something — the rates, the agreement, the inventory holdings — **name the source required** instead of
estimating.

## Step 9 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The group structure**: which company files are group members, and which pairs are expected to trade.
  **A pair that has never had a transaction does not need reconciling every month**
- **The IC account map per entity**: which accounts are IC receivable, payable, loan, revenue, expense
- **The counterparty naming map** — **how each entity refers to each other entity**: as a customer, a
  vendor, a class, a memo convention. **The single most valuable stored asset here**, because it is the join
  and it is different in every group
- **The match rules**: reference field conventions, the agreed date window, the amount tolerance
- **The intercompany agreement terms**: pricing methodology, mark-up, payment terms, settlement cadence
- **The FX rate *source* and the rate-type policy** per statement line. **Not the rates**
- **The group reporting currency**
- **Known recurring causes** — expressed as rules: "Entity C posts monthly recharges in arrears, so a
  one-month timing difference is expected". **Not the amounts**
- **The settlement policy**: net per pair, cadence, settlement currency
- The replay recipe: the exact per-entity batch that produced both sides

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist balances, mismatch amounts, transaction lists or settlement figures.** All state, and all of
it moves every period — that is the entire point of re-reading both sides.

**Key every preference and asset by datasource + entity `display_name`, and every pair by both names.**
Write "quickbooks / Northbrook Holdings ↔ quickbooks / Northbrook Europe BV — IC accounts 1450/2450 and
1450/2450, counterparty as vendor 'NBH Ltd', 5-day window, monthly recharge in arrears" — not "5-day
window". **Pair conventions are specific to the pair**, and applying one pair's rules to another produces
matches that are not matches. Record the chosen **scenario** — which entities, which workspaces — as a
preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's.**

On later runs, match stored entity names against Gate 1's live list. **An entity in preferences that is no
longer connected turns every pair it belongs to into a not-reconcilable pair** — flag it prominently, and
never fall back to the single-sided view.

---

## Both entity scenarios

**Single-entity — not applicable, and say so.** Intercompany reconciliation requires two sides. With one
company file connected you can report **that entity's IC account balances, their ageing, and the
counterparties named in them** — which is genuinely useful as a starting point — but **it is not a
reconciliation** and must not be labelled as one.

**Multi-entity — the only real scenario.** Steps 0–8 as written, with these standing rules:

- **Read per entity in one batch; form pairs from the data.** N reads, not N(N−1)/2.
- **Every figure carries its entity's `display_name` and its currency.** A column of IC balances spanning
  three currencies without labels is the classic multi-entity error here.
- **A pair is only as readable as its weaker side.** Record verdicts per pair.
- **Sub-groups and chains**: where A sells to B who sells to C, **match A↔B and B↔C separately** — see the
  edge cases. Do not try to reconcile A to C directly; they have no direct balance.
- **Entities in different workspaces** need each workspace confirmed at Gate 0. **An unconfirmed workspace's
  entity is unreadable**, which makes its pairs unreconcilable.
- **Differing year-ends across the group** mean the period being reconciled may be a different point in each
  entity's cycle. **Read the same calendar period from each** and say so, rather than each entity's own
  period-end.
- **Not every pair needs reconciling every period.** Where the stored structure says a pair never trades,
  confirm the balance is nil and move on — **but confirm it, do not assume it.**

Capability is checked **per entity** at Gate 2 and **recorded per pair**; the coverage sheet and the pair
matrix together show exactly what this run could and could not do.
