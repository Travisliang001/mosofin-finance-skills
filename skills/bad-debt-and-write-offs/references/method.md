<!-- bad-debt-and-write-offs · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding)
- Step 1 — Choose the methodology
- Step 2 — Identify specific write-off candidates
- Step 3 — Compute the allowance
- Step 4 — Compute the adjustment
- Step 5 — Construct the JEs (hand off to journal-entry-builder)
- Step 6 — Output
- Step 7 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with
plain-language wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence
tool added.

**Never drop a task because no tool covers it.** A `[manual]` task is a task with a *named gap*,
not an absence.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding)

Pull the `[auto]` / `[gated]` reads. **Batch independent reads into one message** — the current
aging, the prior-period agings, the allowance account movement and the customer master do not
depend on each other. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`get_aged_receivables`* at the **period end** — the current aging — usually **[auto]**
- *`get_aged_receivables`* at **several past dates** — the historical agings that become the
  denominators of the loss rates — usually **[auto]** where a past `report_date` is accepted
- *`search_accounts`* — to locate the allowance, bad-debt expense and recovery accounts —
  usually **[auto]**
- *`get_general_ledger`* on those accounts over several years — the write-offs and recoveries
  that become the numerators — usually **[auto]**
- *`get_trial_balance`* / *`get_balance_sheet`* — the existing allowance balance — usually
  **[auto]**
- *`get_customer_balance`* — balances by customer — usually **[auto]**
- *`search_customers`* / *`get_customer`* — the customer master — usually **[auto]**
- *`search_credit_memos`* — credits that may already explain an unpaid balance — usually
  **[auto]**
- *`search_payments`* — receipts after a past write-off, i.e. recoveries — usually **[auto]**
- *`search_journal_entries`* — prior allowance true-ups and write-off entries — usually **[auto]**
- *`get_company_info`* — industry, year-end, base currency — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — it can demonstrate the calculation but
**cannot support a booked allowance or a write-off against a named customer**. Writing off a real
customer's balance on fixture evidence removes a real asset.

## Step 1 — Choose the methodology

Apply the user's stated framework. **The skill builds whichever framework is specified. It does
not pick.**

**Aged-receivable percentage method** (simple, common under many local GAAPs) — **[auto]** once
the loss rates exist:

- Assign a **loss rate** to each aging bucket based on historical experience — the proportion of
  balances in that band that historically ended up unpaid
- **Total allowance = Σ (bucket balance × bucket loss rate)**
- Example *structure*: Current 0.5%, 1-30 days 1%, 31-60 5%, 61-90 15%, 91-120 30%, 120+ 50%
- **Loss rates come from the user's historical data, not assumed.** The figures above are an
  illustration of the shape — rates rising with age — and must never be used as the entity's
  rates. **[auto]** to derive the real ones: for each past period, take the balance in a bucket
  (*`get_aged_receivables`* at that date) and the portion of it subsequently written off
  (*`get_general_ledger`* on the allowance and bad-debt accounts). Show the derivation, the
  periods used, and the resulting rate per bucket

**Specific identification method** — **[gated]**:

- Review each customer's open balance — **[auto]** (*`get_customer_balance`*,
  *`get_aged_receivables`*)
- Reserve fully or partially based on collectibility signals — **[manual]**, since the signals
  (insolvency, dispute, credit deterioration) are not in the ledger
- Often combined with aged-receivable for the rest

**CECL (US GAAP — ASC 326)** — **[gated]**. *Current expected credit loss*: you estimate losses
over the whole life of the receivable up front, rather than waiting for evidence of a problem:

- Forward-looking expected credit loss
- **Historical loss + current conditions + reasonable forecast** — the first is **[auto]**, the
  second **[gated]**, the third **[manual]**
- Various sub-methods: **vintage analysis** (tracking each period's originations through their
  life), **roll-rate analysis** (how much of each bucket rolls into the next), **probability of
  default × loss given default** (how likely a customer fails × how much you lose when they do)
- **Requires user-supplied historical data and forecast assumptions** — though in a connected
  workspace the historical half is usually derivable, so ask only for the forecast

**IFRS 9 ECL** — **[gated]**:

- **12-month or lifetime expected credit losses depending on staging** — *staging* being the
  three-way classification by how much credit risk has deteriorated since the receivable arose
- **Simplified approach for trade receivables: lifetime ECL based on a provision matrix** — a
  table of loss rates by aging bucket, which is the same structure as the aged-receivable method
  and is derivable the same way
- Same data requirements as CECL

## Step 2 — Identify specific write-off candidates

A balance is a write-off candidate when:

- **Customer is in bankruptcy / insolvency** — **[manual]**
- **Customer dissolved or unreachable** — **[manual]**
- **Past statute of limitations** — the legal deadline after which a debt can no longer be
  enforced. **[gated]**: the invoice date is **[auto]** (*`search_invoices`*,
  *`get_aged_receivables`*), the limitation period is a legal rule and **[manual]**
- **Cost of further collection exceeds the amount** — **[gated]**: balance **[auto]**, the
  threshold a policy
- **Legal counsel advised cessation** — **[manual]**
- **Specific dispute resolved against the entity** — **[manual]**

**None of these is "the invoice is old."** Age is what puts a balance in the *allowance*; a
write-off needs one of the reasons above. Never propose a write-off on aging alone.

For each candidate:

- **Customer ID, balance, age** — **[auto]**
- **Reason for write-off** — **[manual]**, from the list above
- **Approval evidence** (per the entity's write-off authority matrix) — **[manual]**, and
  mandatory: an unapproved write-off is a control failure and a classic fraud route, since it
  removes a real receivable from the books
- **Tax treatment in the entity's jurisdiction** — **[manual]**. Most jurisdictions allow a
  deduction once specific criteria are met, **but rules vary — flag for the user**

First check whether an outstanding **credit memo** already explains the balance
(*`search_credit_memos`*, **[auto]**). A balance that should have been credited is not a bad
debt; writing it off as one records a loss that never happened and hides a billing error.

## Step 3 — Compute the allowance

If using the **aged-receivable method** — **[auto]**:

| Aging bucket | Balance | Loss rate (entity historical) | Provision |
|---|---|---|---|

**Sum = required allowance balance at period end.**

Record, next to each rate, **where it came from**: the periods used, the derivation, and whether
it was derived from the books or supplied. A rate without a source is the thing the quality
standards forbid.

If using **CECL / ECL** — **[gated]**:

- **Build the provision matrix from historical data** — **[auto]** where past agings are readable
- **Apply adjustments for current conditions** — **[gated]**; some conditions are observable in
  the books (a customer's payment pattern deteriorating, concentration rising) and worth
  surfacing
- **Apply the forward-looking adjustment** (**the user must supply the economic outlook**) —
  **[manual]**
- **Document all assumptions** — every adjustment, its size, and its rationale

## Step 4 — Compute the adjustment

The allowance is a *balance*, not an expense. What hits the P&L is only the movement.

```
Required allowance at period end     = $X
Existing allowance in GL              = $Y
Adjustment needed                     = $X − $Y
  Positive = increase allowance (book bad-debt expense)
  Negative = release allowance (reduce bad-debt expense)
```

**[auto]** for both figures: `$X` from Step 3, `$Y` from the allowance account
(*`get_trial_balance`*, *`get_general_ledger`*). State the existing allowance's account name and
balance date explicitly — a true-up against the wrong opening figure is the most common error in
this whole calculation.

## Step 5 — Construct the JEs (hand off to journal-entry-builder)

`DR` is a debit, `CR` a credit; every entry balances. **Mosofin does not post** — these are
proposals.

**Allowance adjustment**:
```
DR  Bad Debt Expense                          $adjustment (if increase)
    CR  Allowance for Doubtful Accounts          $adjustment
Memo: Period-end allowance true-up — [period]
```

If the adjustment is a **release**:
```
DR  Allowance for Doubtful Accounts           $adjustment
    CR  Bad Debt Expense                         $adjustment
Memo: Allowance release — [period] — [reason]
```

**Specific write-off** (after the allowance has been set up):
```
DR  Allowance for Doubtful Accounts           $balance written off
    CR  Accounts Receivable                      $balance written off
Memo: Write-off — [Customer] — [reason] — approval [reference]
```

**Direct write-off** (if the entity doesn't maintain an allowance — allowed only in some
jurisdictions / for cash-basis taxpayers):
```
DR  Bad Debt Expense                          $balance
    CR  Accounts Receivable                      $balance
```

**Tax recoverability on written-off receivables**:

Some jurisdictions allow recovery of the **output tax** (VAT / GST / sales tax) that was remitted
on the original invoice if the receivable becomes uncollectible — you paid tax on money you never
received — **but with formal procedures**. If the user's jurisdiction permits and they have
followed the procedure:
```
DR  Tax Payable / Input Tax Adjustment        $tax portion
    CR  Bad Debt Expense                         $tax portion
```
**Flag this — never auto-claim without user confirmation.** **[manual]**, always. The tax codes
and amounts on the original invoice are **[auto]** (*`read_invoice`*, *`search_tax_codes`*),
which helps size it — the entitlement is not.

**Recovery** (cash received after write-off): reverse the write-off or book directly:
```
DR  Cash                                      $recovered
    CR  Bad Debt Expense (or Recovery of Bad Debt Income)  $recovered
```
**[auto]** to detect: payments received from a customer whose balance was previously written off
(*`search_payments`* against the write-off history in *`search_journal_entries`*).

Use the **real account names from the connected chart of accounts** (*`search_accounts`*,
**[auto]**) rather than the generic labels above, and say which you chose.

## Step 6 — Output

Deliver an `.xlsx` workpaper. Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**Sheet 1: Allowance Calculation**

| Aging Bucket | AR Balance | Loss Rate | Provision |

- Total required allowance
- Existing allowance
- Adjustment needed

Add a header block: workspace name; each in-scope company file by `display_name`; each excluded
one and why; whether any figure rests on `mock` data.

**Sheet 2: Specific Write-Offs**

| Customer | Balance | Currency | Reason | Approval | Tax Recovery? | JE Reference |

**Sheet 3: Methodology Documentation**

- Framework chosen
- **Loss-rate source and date** — and, per bucket, whether it was **derived from the books**
  (with the periods used) or **supplied by the user**
- Forward-looking adjustments (if CECL/ECL)
- Assumptions and sensitivity (if material)

**Sheet 4: Roll-Forward**

| Opening Allowance | Add: Provision | Less: Write-Offs | Plus: Recoveries | Closing Allowance |

**Sheet 5: GL Posting**

All proposed JEs for the allowance and the write-offs, marked clearly as **proposals**.

**Sheet 6: Coverage — NEW, Mosofin-specific**

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used | Policy (enabled / permission / disabled) | `mock` | Gap — what could not be verified and what the user must supply |

Rows for customer-specific risk, forward-looking indicators, approval evidence and tax
entitlement will read `manual` with their gaps named. That is the correct, expected result.

In a multi-entity run this sheet is **per entity**.

**File naming:** `BadDebt_Allowance_[YYYY-MM].xlsx`

In a multi-entity run: `BadDebt_Allowance_[YYYY-MM]_[EntityDisplayName].xlsx`, plus one combined
file. Every file states which datasource and `display_name` it covers.

**Grounding:** every figure traces to a tool result in this conversation or to labelled
user-supplied evidence. End with a single **Data sources** line grouping calls by datasource.
Where the data does not cover something, **name the tool that would have covered it** instead of
estimating.

## Step 7 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them,
ask — explicitly, at that point, not earlier — whether to save this as their own customized
version. A general "yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The reporting framework** and the methodology chosen within it, including any sub-method
  (vintage, roll-rate, PD × LGD, provision matrix)
- **The derivation recipe for loss rates** — which periods, which accounts, which buckets. Note
  the distinction: persist *how the rates are derived*, **not the rates themselves**. Rates are
  re-derived each period from current history; a frozen rate defeats the point of having history
- The account mapping: allowance, bad-debt expense, recovery, and tax adjustment accounts, by
  their real names
- **The write-off authority matrix** — who approves what, up to what value
- The tax jurisdiction's position on output-tax recovery, and the procedure that must be followed
- Customer categories carrying a standing rate override (e.g. government or institutional
  customers — see the edge case) with the reason
- The forward-looking adjustment's source, if CECL/ECL — whose forecast, published where
- The replay recipe: the exact sequence of reads that produced this period's calculation

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference
files; set `datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write
preference files alongside the installed skill.

**Do not persist customer balances, customer names with risk assessments, or write-off case
details.** A stored note that a named customer is a credit risk is both a snapshot and a
sensitive assertion about a real business; it belongs in the accounting system, not a skill
bundle.

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks /
Northbrook Trading — IFRS 9 simplified, provision matrix derived from trailing 3 years, allowance
account: Provision for Doubtful Debts" — not "IFRS 9 simplified". Entities have genuinely
different loss experience, and an unlabelled matrix applied to the wrong company file misstates
a real balance. Record the chosen **scenario** (single vs multi, and which set) as a preference
too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to
the workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is
the workspace's.**

On later runs, match stored entity names against Gate 1's live list. An entity in preferences
that is no longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One allowance, one
roll-forward, one workpaper.

**Multi-entity.** Steps 0–6 run **once per entity**, each call targeting exactly one
`data_source_id`, every loss rate, allowance and write-off carrying that entity's
`display_name`. Then one cross-entity step:

- **A roll-up of allowances and a comparison of loss rates by entity.** Allowances aggregate
  meaningfully. **Loss rates do not** — pooling them produces a rate that describes no entity.
  Report rates per entity, and comment on the differences rather than averaging them away.
- **Derive rates per entity, from that entity's own history.** Where one entity is too new or too
  small to have credible history, say so and use a sibling's rate **explicitly and labelled**,
  rather than silently.
- **A shared customer failing affects every entity that bills them** — this is the cross-entity
  finding worth surfacing. One customer's insolvency may be immaterial at each entity alone and
  material to the group.
- **Intercompany receivables are excluded** from the allowance — see the edge case and
  `intercompany-reconciliation`.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict per
company file.
