<!-- bank-fee-and-interest-analysis · method.md · read for: Stages 3–6 — the analysis itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding)
- Step 1 — Build a fee taxonomy
- Step 2 — Classify each statement line
- Step 3 — Tie to GL and detect coding issues
- Step 4 — Trend and variance analysis
- Step 5 — Optimization playbook
- Step 6 — Accounting entries
- Step 7 — Evolve the skill (Mosofin-specific, final step)
- Outputs
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with
plain-language wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence
tool added.

**Never drop a task because no tool covers it.** A `[manual]` task is a task with a *named gap*,
not an absence — and in this skill the largest gap is the statement itself.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding)

Pull the `[auto]` / `[gated]` reads. **Batch independent reads into one message** — the fee
account ledger, the interest ledger, the deposit list and the payment list do not depend on each
other. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`search_accounts`* — to locate the bank fee, interest income, interest expense, merchant fee
  and cash accounts — usually **[auto]**
- *`get_general_ledger`* on each of those accounts, across the whole period — the fee population
  as recorded — usually **[auto]**
- *`get_profit_and_loss`* with a monthly breakdown — the trend at summary level — usually
  **[auto]**
- *`search_purchases`* — fees often posted as expenses or card charges rather than journal
  entries — usually **[auto]**
- *`search_deposits`* / *`get_deposit`* — deposit counts, and the netting check — usually
  **[auto]**
- *`search_transfers`* — movements between own accounts, a wire-fee driver — usually **[auto]**
- *`search_bill_payments`* — outbound payment counts by method — usually **[auto]**
- *`search_payments`* / *`search_sales_receipts`* — inbound receipt counts, the merchant-fee
  driver — usually **[auto]**
- *`search_payment_methods`* — how methods are labelled in this workspace — usually **[auto]**
- *`get_balance_sheet`* — average cash balances, which drive both interest earned and the
  earnings credit — usually **[auto]**
- *`get_company_info`* — base currency and calendar — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — it can demonstrate the analysis but
must not support a renegotiation position or a posted entry.

## Step 1 — Build a fee taxonomy

Sort the charges into categories, because "bank fees: $4,200" tells you nothing actionable while
"wire fees: $1,900 across 63 wires" tells you what to do.

Buckets:

- **Account maintenance** — the standing monthly charge for having the account
- **Treasury management services** — positive pay, sweeps, reporting, fraud controls
- **Transaction fees (ACH, wires, checks)** — per-item charges for moving money
- **Cash handling** — counting and depositing physical notes and coin
- **Merchant services (discount, per-item, chargebacks)** — the cost of taking card payments:
  the **discount rate** (a percentage of each sale), a **per-item** charge, and **chargebacks**
  (a customer's card issuer reversing a payment)
- **FX and international** — currency conversion margins and cross-border charges
- **Lending-related fees** — commitment, arrangement, unused-line and covenant-monitoring fees
- **Interest earned / paid**

**[auto]** to populate from the books wherever the fee was posted; **[manual]** for any bucket
the books do not distinguish. Map each bucket to the actual account names in this chart of
accounts (*`search_accounts`*, **[auto]**), and **name any bucket that has no posted fees at
all** — for a business using that product, a zero is more likely to mean netted-and-uncoded than
free.

## Step 2 — Classify each statement line

For each line item capture — **[manual]** where the source is the statement, **[auto]** where the
source is a posted ledger entry:

- **Date**
- **Amount**
- **Descriptor** — the bank's own wording, which is what makes categorisation possible. In the
  books this survives only if whoever posted it kept the memo; where the memo is generic
  ("bank charge"), say the classification was inferred
- **Category / subcategory** — from Step 1
- **Driver (fixed vs volume)** — does this charge exist regardless of activity, or does it scale
  with the number of transactions? This distinction drives everything in Steps 4 and 5: fixed
  fees are removed by consolidating or renegotiating, volume fees by changing behaviour

## Step 3 — Tie to GL and detect coding issues

- **Match statement fees / credits to GL postings** — **[gated]**: the GL side is **[auto]**
  (*`get_general_ledger`*), the statement side **[manual]**. With both, this is a genuine
  two-sided tie-out. With only the GL, say clearly that you tied the books to themselves and the
  match rate is not meaningful
- **Identify missing postings (need JEs)** — **[manual]-dependent**, and **this is the step that
  needs the statement most**. A fee that was never posted cannot be found in the ledger. Without
  the statement, report this check as **not performed** rather than as finding nothing
- **Identify miscodings** (wrong expense account, wrong dimensions) — **[auto]** and a real
  strength here: scan for bank-fee-shaped transactions sitting in other accounts, and for fees
  posted without the class or department the entity normally uses
  (*`get_general_ledger`*, *`search_classes`*, *`search_departments`*)
- **Detect netted fees embedded in deposits** — **[gated]**, and inferable without the statement:
  compare each deposit's total against the receipts it comprises (*`get_deposit`*,
  *`search_payments`*, *`search_sales_receipts`*). Where the deposit is smaller, a fee was almost
  certainly deducted at source. **Netted fees are the most commonly missed bank cost**, because
  they never appear as an expense at all — the revenue simply arrives smaller

## Step 4 — Trend and variance analysis

Provide:

- **MoM and YoY trends** — month on month and year on year — **[auto]**
  (*`get_general_ledger`*, *`get_profit_and_loss`* with a monthly breakdown). Year-on-year needs
  13+ months of data, which is why Gate 3 asks for it
- **Unit rates (fee per wire, per ACH, per deposit)** — **[auto]**, and the most useful output
  this skill produces from a connected workspace. The numerator is the posted fee; the
  denominator is the real transaction count from the books (*`search_transfers`*,
  *`search_bill_payments`*, *`search_deposits`*, *`search_payments`*). State the count and the
  period alongside every rate — a rate without its denominator cannot be checked or negotiated
  with
- **Outliers and one-time items** — **[auto]**: charges far outside the normal range, charges
  appearing once, and step-changes in a monthly fee. Separate one-time items out of the trend, or
  they distort every comparison

## Step 5 — Optimization playbook

Each of these is a **recommendation for a human to act on** — Mosofin changes nothing.

- **Replace wires with ACH where possible** — **[auto]** to size: count wires and multiply by the
  rate difference. Wires are typically many times the cost of an ACH payment, and a meaningful
  share are habit rather than necessity
- **Consolidate accounts** — **[auto]** to size: each account carries its own maintenance charge,
  so count the accounts (*`search_accounts`*) and identify low-activity ones
  (*`get_general_ledger`*)
- **Negotiate pricing and ECR** — the **earnings credit rate** is a notional interest rate banks
  apply to your average balance and use to offset fees, rather than paying you interest. A high
  balance may already be paying for services invisibly, which changes whether moving cash
  elsewhere is actually a saving. **[manual]** for the rate; **[auto]** for the average balance it
  applies to (*`get_balance_sheet`*)
- **Review the merchant pricing model** — interchange-plus versus flat-rate versus tiered pricing
  produce very different costs at different transaction mixes. **[manual]** unless a processor is
  connected; **[auto]** for the transaction mix that determines which model wins
- **Automate coding rules for recurring fees** — **[auto]** to identify: recurring, same-amount,
  same-descriptor charges are exactly what a rule should handle, and they are visible in the
  ledger

## Step 6 — Accounting entries

`DR` is a debit, `CR` a credit; every entry balances. **Mosofin does not post** — these are
proposals.

**Fees**
```
DR Bank Fees Expense                 XXX
    CR Cash                               XXX
```

**Interest earned**
```
DR Cash                               XXX
    CR Interest Income                     XXX
```

Use the **real account names from the connected chart of accounts** (*`search_accounts`*,
**[auto]**) rather than the generic labels above, and say which you chose. For a **netted** fee,
the entry is not the one above: the receipt must be grossed up and the fee recognised separately,
or the fee stays invisible and revenue stays understated — state that explicitly where netting
was detected.

## Step 7 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them,
ask — explicitly, at that point, not earlier — whether to save this as their own customized
version. A general "yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The account mapping** — which real accounts hold bank fees, merchant fees, interest income
  and interest expense, and which cash accounts belong to which bank
- **The banking product list** — so a bucket that should have fees and doesn't is flagged next run
- **The fee schedule / contracted rates**, with the date they applied from — this is what turns
  "we paid $30 a wire" into "we paid $30 against a contracted $18"
- The **ECR** arrangement, if any
- **Baseline unit rates** from this run, so the next run compares against them rather than
  starting cold
- The classification rules used for descriptors, so categorisation is consistent period to period
- Which items were one-time, so they are excluded from future trends
- The replay recipe: the exact sequence of reads that produced this analysis

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference
files; set `datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write
preference files alongside the installed skill.

**Do not persist bank account numbers or banking credentials.** Account names and internal
references are fine; the numbers are not, and they are never needed for this analysis.

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks /
Northbrook Trading — wire fee contracted $18, merchant interchange-plus 0.35%, fees post to Bank
Charges" — not "wire fee $18". Entities frequently bank on different terms, and an unlabelled
contracted rate applied to the wrong company file produces a variance that does not exist. Record
the chosen **scenario** (single vs multi, and which set) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to
the workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is
the workspace's.**

On later runs, match stored entity names against Gate 1's live list. An entity in preferences
that is no longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Outputs

- **Categorized fee schedule.** Every posted fee by bucket, with its date, amount, descriptor,
  driver (fixed / volume), and whether its category was **read** from the descriptor or
  **inferred**.
- **Tie-out to GL (matched vs unmatched).** **State which sides were evidenced.** With a
  statement, a genuine two-sided match rate. Without one, say explicitly that only posted fees
  were examined and the "unmatched" column cannot be populated.
- **Root-cause list for mismatches.** Missing postings, miscodings, netted fees, timing, and
  duplicate charges — each with its evidence and its owner.
- **Cost reduction recommendations.** Each one **sized** — the annual saving, the count it rests
  on, and the assumption behind it. An unsized recommendation does not get acted on.
- **Proposed JEs (if needed).** Marked clearly as proposals, including any gross-up entry where
  netting was detected.

**Coverage sheet — NEW, Mosofin-specific.**

One row per task in Steps 1–5:

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used | Policy (enabled / permission / disabled) | `mock` | Gap — what could not be verified and what the user must supply |

The row for **"identify missing postings"** will read `manual` with the gap "bank statement not
supplied" unless it was. That row is the honest headline of this whole analysis and must not be
omitted.

In a multi-entity run the sheet is **per entity**.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming — Mosofin addition** (the original left it unstated, and multi-entity output needs
it): `Bank_Fee_Analysis_[YYYY-MM].xlsx`, and in a multi-entity run
`Bank_Fee_Analysis_[YYYY-MM]_[EntityDisplayName].xlsx` plus one combined file. Every file states
which datasource and `display_name` it covers.

**Grounding:** every figure traces to a tool result in this conversation or to labelled
user-supplied evidence. End with a single **Data sources** line grouping calls by datasource.
Where the data does not cover something, **name the tool that would have covered it** instead of
estimating.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One fee schedule, one set of
unit rates, one playbook.

**Multi-entity.** Steps 0–6 run **once per entity**, each call targeting exactly one
`data_source_id`, every fee and rate carrying that entity's `display_name`. Then one cross-entity
step — and here it is commercially significant rather than merely tidy:

- **Consolidated volumes are the negotiating lever.** Banks price on total relationship volume,
  so the group's combined wire, ACH and card counts are what earns a better rate — even though
  each entity is billed separately. Produce the group volume table explicitly; it is often the
  single most valuable output of a multi-entity run.
- **Compare unit rates across entities.** Entities on different terms with the same bank, or with
  different banks entirely, is common and usually unintentional. A wire costing $18 at one entity
  and $35 at another is an immediate, quantified action.
- **Account consolidation across entities is limited by legal separateness** — each legal entity
  generally needs its own accounts. Recommend consolidating *within* an entity, and
  *renegotiating* across the group; do not propose merging entities' bank accounts.
- **Fees are never pooled into one figure** without the entity label — each entity bears its own
  costs.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict per
company file.
