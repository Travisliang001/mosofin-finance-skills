<!-- petty-cash-management · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding) — Mosofin addition
- Step 0b — Test the imprest invariant (Mosofin addition)
- Step 1 — Capture the float
- Step 2 — Parse vouchers
- Step 3 — Compute the reconciliation
- Step 4 — Code vouchers to GL accounts
- Step 5 — Replenishment
- Step 6 — Discrepancy handling
- Step 7 — Output
- Step 8 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Never drop a task because no tool covers it.** The count is `[manual]` by its nature and stays in the
workflow with an owner and a date.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding) — Mosofin addition

**Batch independent reads into one message.** The server is **stateless**: pass `data_source_id` on
**every** call.

Typical batch, per in-scope entity:

- *`search_accounts`* — **the petty cash account or accounts, and Cash Over/Short** — usually **[auto]**
- *`get_balance_sheet`* / *`get_trial_balance`* — **the petty cash balance** — usually **[auto]**
- *`get_general_ledger`* on **the petty cash account** — **the imprest invariant test** — usually **[auto]**
- *`get_general_ledger`* on **Cash Over/Short** — **the shortage trend** — usually **[auto]**
- *`search_payments`* / *`search_checks`* — **replenishments, with dates and amounts** — usually **[auto]**
- *`search_locations`* / *`search_classes`* — **where several floats exist** — usually **[auto]**
- *`get_company_info`* — legal name, currency — usually **[auto]**

**Pull at least twelve months.** **The value here is in the pattern** — replenishment frequency and shortage
trend — **not in this period's balance.**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — **and a float reconciled against a fixture balance
proves nothing about the cash in the tin.**

## Step 0b — Test the imprest invariant (Mosofin addition)

**Run before Step 1.** **[auto]**, and it takes one read.

**Under an imprest system the petty cash account balance is constant.** So:

| What the account shows | What it means |
|---|---|
| **A flat balance equal to the authorised float** | **The fund is being run correctly.** Proceed |
| **A balance that moves with each expense** | **Not an imprest system.** Expenses are being posted to the float directly, which means **the account is a cash account being spent down**, and replenishments are top-ups rather than expense recognitions |
| **A balance that differs from the authorised float** | **The float has been changed without authority**, or the authorised amount is not what was stated, or a difference was posted here rather than to Cash Over/Short |
| **No movement at all for a long period** | **A dormant float** — still holding cash somebody is accountable for, and **still needing a count** |

**Report the result before the reconciliation.** **If the fund is not run as an imprest float, the Step 3
formula does not describe it**, and the reconciliation needs a different shape — which is worth knowing
before computing anything.

## Step 1 — Capture the float

**Document the authorized float** — the constant amount that the petty cash fund should always reconcile to
when cash + vouchers are summed. **[gated]**: **the GL balance is `[auto]`; the authorisation is
`[manual]`.**

**Where they differ, resolve it first.** The rest of the reconciliation is measured against this number.

## Step 2 — Parse vouchers

For each voucher or receipt — **[manual]**, from the box:

- **Date**
- **Payee / vendor**
- **Description / business purpose**
- **Amount**
- **Currency** (if mixed)
- **Voucher number**
- **Approver** (if required by policy)
- **Receipt attached: Y/N**

**Normalize and check:**

- **Numeric amounts**
- **Date within the reconciliation period**
- **Each voucher has an approver if policy requires**
- **Receipt present per policy threshold** — use the entity's stated threshold; **if none provided, flag
  every receipt-less voucher**

**That last instruction is the right default and worth keeping**: **absent a stated threshold, every missing
receipt is flagged.** Assuming a threshold would silently pass items the policy might not.

## Step 3 — Compute the reconciliation

```
Authorized float                           = $X
Less: vouchers/receipts in the box         = ($Y)
Less: IOUs / temporary advances            = ($A)
Equals: expected cash on hand              = $X − $Y − $A
Actual cash counted                        = $Z

Difference (Z minus expected)
  = 0   → ties
  > 0   → cash over (less common; investigate)
  < 0   → cash short (most common; investigate)
```

**Output the formula and the result. Never silently absorb a difference.**

**[gated]**: **the float is `[auto]`; the vouchers, the IOUs and the count are `[manual]`.** **Three of the
four inputs come from the box and the tin**, which is the honest position — **this reconciliation is
performed by a person with the fund in front of them**, and the workspace supplies the anchor and the
context.

## Step 4 — Code vouchers to GL accounts

**Use `gl-coding-assistant` logic. Account numbers come from the user's COA only.** **[auto]** for the
chart — real accounts, and **the coding history is readable**, which makes the suggestions evidenced rather
than generic. See that skill.

## Step 5 — Replenishment

**When the custodian requests replenishment** — typically when cash drops below a threshold:

```
Replenishment amount = sum of approved vouchers in the period
```

**GL posting at replenishment** — hand off to `journal-entry-builder`. `DR` is a debit, `CR` a credit.
**Mosofin does not post** — this is a proposal:

```
DR  Expense accounts (per voucher coding)        $vouchers
DR  Input Tax Recoverable (if jurisdiction allows) $tax
    CR  Cash / Bank                                  $replenishment
```

**The petty cash on-hand balance in the GL stays constant at the float amount; only the bank moves.**

**That sentence is the imprest invariant, stated by the original itself** — and **Step 0b tests whether it
holds in practice.**

**[auto]** context worth reporting alongside: **the replenishment history.** **How often the fund has been
topped up and by how much** tells you whether the float is correctly sized. **A float replenished every week
is too small for its purpose; one replenished twice a year may be larger than it needs to be** — and either
is a cheap observation to make while you are here.

## Step 6 — Discrepancy handling

**If actual cash ≠ expected** — **[manual]** on the policy, **[gated]** on the treatment:

- **Small shortages within policy tolerance** → **post to Cash Over/Short (expense) per policy**
- **Larger shortages** → **flag for investigation; do not auto-post**
- **Cash over** → **investigate first; do not record as income until cleared**

**Policy tolerance comes from the user — do not assume a threshold.**

**Mosofin addition — the trend matters more than the instance.** **[auto]**: **read the Cash Over/Short
account across periods, by location or custodian where the dimension supports it.**

- **A one-off shortage within tolerance is a rounding of life.**
- **A shortage in every period, always in the same direction, always just inside tolerance, is a pattern** —
  and it is the pattern that a tolerance-based policy is least able to see, because each instance passes.
- **Report the pattern with its figures and its period count.** **Never as an allegation** — see
  `fraud-detection-and-forensics`; a persistent shortage has innocent explanations too, including a float
  that is simply mis-stated. **The pattern is the finding; the cause is somebody else's to establish.**

## Step 7 — Output

Deliver an `.xlsx` workpaper:

**Sheet 1: Reconciliation Summary**
- **Custodian, period, authorized float**
- **Cash counted, vouchers total, IOUs total**
- **Expected cash, difference, status** — ties / over / short
- **Replenishment amount**

Plus the Mosofin header: workspace name; the entity by `display_name`; **the imprest invariant result**;
**the count date and who performed it**; whether any figure rests on `mock` data.

**Sheet 2: Voucher Detail**

| Voucher # | Date | Payee | Description | Amount | Currency | GL Account | Tax Code | Receipt? | Approver | Notes |

**Sheet 3: Exceptions**
- **Missing receipts** (above policy threshold)
- **Missing approvals**
- **Dates outside period**
- **Amount discrepancies**

**Sheet 4: GL Posting Inputs** — inputs for `journal-entry-builder`, marked as **proposals**.

**Sheet 5: Fund Health — NEW, Mosofin-specific** — the imprest invariant test, the replenishment history and
frequency, the Cash Over/Short trend by period, and whether the float is correctly sized.

**Sheet 6: Coverage — NEW, Mosofin-specific**

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used / external source | As-at date | `mock` | Gap |

**The count row reads `manual` with its owner and date**, even — especially — when it has not been done.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming:** `[CustodianOrLocation]_PettyCash_[YYYY-MM].xlsx`

**Grounding:** every ledger figure traces to a tool result in this conversation; **the count and the
vouchers trace to the person who performed and supplied them.** End with a single **Data sources** line.

## Step 8 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The float amounts** and **which account holds each**, by location or custodian
- **The account map**: petty cash accounts, Cash Over/Short, the bank account replenishments come from
- **The receipt threshold and the shortage tolerance**, with their authority
- **The replenishment policy** — trigger level and frequency
- **The approval requirement** — who may approve a voucher, and above what amount
- **The count cadence** and who performs it
- **The common coding** for recurring petty cash categories, cross-referenced to `gl-coding-assistant`
- **Whether the fund is genuinely run as an imprest float**, as established by Step 0b
- The replay recipe: the exact sequence of reads that produced the invariant test and the trend

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist counts, differences, voucher details, payee names or custodian names.** All state — **and
a recorded shortage attached to a named custodian, carried forward outside a formal process, is exactly the
kind of unrebutted mark this pack refuses to keep.** See `fraud-detection-and-forensics`.

**Key every preference and asset by datasource + entity `display_name`, and by float.** Write "quickbooks /
Northbrook Trading — two floats: Head Office 500 in account 1015, Warehouse 250 in account 1016, receipts
required above 20, tolerance 5, counted monthly" — not "float 500, tolerance 5". **Floats are per location
and per custodian**, and applying one float's tolerance to another either passes real shortages or flags
normal ones. Record the chosen **scenario** (single vs multi) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's.**

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id` — **and possibly several floats**, each
reconciled separately per the first edge case.

**Multi-entity.** Steps 0–7 run **once per entity**, each float carrying its entity's `display_name` and its
location. Then:

- **Each entity's floats are its own.** **A single group-level petty cash reconciliation is not meaningful**
  — the funds are physically separate, held by different people, in different places.
- **A float held at one entity's site but funded by another** is an intercompany balance until settled —
  see `intercompany-reconciliation`. **Ask; shared premises make this more common than it sounds.**
- **Run the Cash Over/Short trend per float, not per entity or group.** **The pattern is custodian-specific**,
  and aggregating destroys exactly the signal worth having.
- **Tolerances and thresholds may reasonably differ by location** — a site float in a high-cost city and a
  small back-office tin do not need the same policy. **Store them per float.**
- **Currency**: a float held in a currency other than the entity's functional currency is reconciled in its
  own currency, per the second edge case, **and translated only for reporting** — see
  `multicurrency-fx-revaluation`.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict per company
file and per float.
