<!-- personal-tax-return-prep · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the business-sourced figures (grounding) — Mosofin addition
- Step 1 — Establish the framework
- Step 2 — Gather and categorize income
- Step 3 — Apply income-specific deductions and adjustments
- Step 4 — Apply personal deductions / reliefs / allowances
- Step 5 — Compute taxable income
- Step 6 — Compute the tax
- Step 7 — Apply tax credits
- Step 8 — Compute balance due / refund and obligations
- Step 9 — Document checklist and organization
- Step 10 — Output
- Step 11 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Never drop a task because no tool covers it.** Most of this skill is `[manual]` by design — it concerns a
person, not a company.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the business-sourced figures (grounding) — Mosofin addition

**Only where the taxpayer has an interest in a connected entity**, and **only the figures the return
needs.**

**Batch independent reads into one message.** The server is **stateless**: pass `data_source_id` on **every**
call.

Typical batch, per in-scope entity:

- *`get_profit_and_loss`* **for the business's year** — **net profit, the starting point for
  self-employment or partnership income** — usually **[auto]**
- *`get_general_ledger`* on **the owner's capital, drawings or director's loan account** — **drawings and
  the balance** — usually **[auto]**
- *`get_general_ledger`* on **distributions or dividends declared and paid** — usually **[auto]**
- *`get_balance_sheet`* — **the owner's capital position** — usually **[auto]**
- *`search_payments`* — **payments to the owner**, by date — usually **[auto]**
- *`get_profit_and_loss`* filtered to **owner salary** where the owner is on payroll — usually **[auto]**;
  see the payroll tax filings for the withholding side
- *`get_company_info`* — legal name, **fiscal year end**, country — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that figure to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — **these figures go on a tax return with a
signature on it.**

## Step 1 — Establish the framework

**Confirm** — **[manual]**:

- **Jurisdiction(s) and tax year**
- **Residency / domicile status** — **determines what income is taxable and where** — **critical for
  cross-border**
- **Filing status and household composition** — affects rates, allowances and credits in many jurisdictions
- **The current rules / rates / brackets / allowances for the year** — **confirm; never assume**

**Mosofin note on the tax year**: **the business's fiscal year end may not match the personal tax year.**
**[auto]** to read the business year end, **[manual]** to determine which business period's profit falls
into which personal tax year — **a jurisdiction-specific basis-period question**, and one that has changed
in some jurisdictions recently. **Ask; do not assume the two align.**

## Step 2 — Gather and categorize income

**Organize all income by type, since types are often taxed differently** — each with its verdict:

**Employment income**: **salary, wages, bonuses, benefits-in-kind / fringe benefits, equity compensation.
From employer statements.** — **[gated]**: **`[auto]` for salary from a connected business where the
taxpayer is on its payroll**; **`[manual]` for any other employer**, and **`[manual]` for benefits-in-kind**
even from the connected business, since their taxable value is a computation, not a ledger figure.

**Self-employment / business income**: **net profit from sole-trader or freelance activity — revenue less
allowable business expenses. May need a separate computation** — `tax-return-prep-corporate` concepts apply
to the business, but **personal returns report the net.** — **[gated]**, ⭐ **and the strongest contribution
here**: **where the business is connected, the accounting net profit is `[auto]`.** **The tax adjustments
to it are `[manual]`.**

**Investment income**: **interest, dividends — often taxed at special rates — distributions.** —
**[gated]**: **distributions from a connected business are `[auto]`**; **third-party investment income is
`[manual]`.**

**Capital gains**: **gains and losses on disposals of assets — often taxed at distinct rates, with annual
exemptions and special holding-period rules.** — **[manual]**; there is no personal asset register here.

**Rental / property income**: **rental receipts less allowable expenses; depreciation or capital allowances
where permitted.** — **[gated]**: **`[auto]` where a property business is a connected entity**; otherwise
`[manual]`.

**Pension / retirement income**: **pensions, annuities, retirement account distributions.** — **[manual]**.

**Other income**: **royalties, trusts, foreign income, miscellaneous.** — **[manual]**.

**For each, capture the gross amount, any tax withheld, and the supporting document.**

**Mosofin addition — the owner's account.** **[auto]** where connected: **drawings, the loan or capital
account balance, and its movement.** **This is not itself an income category**, but in many jurisdictions it
matters:

- **Drawings may be taxable, capital, or a loan** depending on the entity type and the jurisdiction —
  **`[manual]` to determine, `[auto]` to quantify**
- **An overdrawn owner's or director's account can trigger a tax charge**, an interest benefit, or both —
  see the edge cases. **The balance and its movement are exactly readable**, and it is a figure owners
  routinely cannot state
- **Distributions taken as drawings and never formally declared** are a common and consequential
  informality. **The ledger shows what was taken; the paperwork determines what it was**

## Step 3 — Apply income-specific deductions and adjustments

- **Allowable expenses against self-employment and rental income** — **[gated]**: **the business's expenses
  are `[auto]`; which are allowable for tax is `[manual]`**
- **Capital losses offsetting capital gains, and carryforwards** — **[manual]**
- **Income-specific reliefs** — jurisdiction-specific — **[manual]**

**The first line is the important distinction**: **accounting expenses and tax-allowable expenses are not
the same set.** Entertainment, certain provisions, depreciation versus capital allowances — **all differ**,
and the difference is the business tax computation. **Reading the P&L gives you the starting figure, not the
answer.**

## Step 4 — Apply personal deductions / reliefs / allowances

**Jurisdiction-specific — confirm what applies and current amounts** — **[manual]**, all of it:

- **Personal allowance / standard deduction / tax-free threshold**
- **Itemized deductions** where applicable: **mortgage interest, charitable contributions, medical,
  state / local taxes**
- **Retirement / pension contribution relief**
- **Other statutory reliefs** — education, childcare

**Determine whether a standard or personal allowance, or itemizing, produces the better result where the
jurisdiction allows a choice.**

**Compute both where a choice exists** — the original's instruction, and it is arithmetic once the amounts
are supplied.

## Step 5 — Compute taxable income

```
Total income (all sources)
− Income-specific deductions
− Personal allowances / deductions / reliefs
= Taxable income
```

**Separate income into the right "baskets" if the jurisdiction taxes ordinary income, dividends, and capital
gains at different rates.**

**[auto]** arithmetic on **[manual]** inputs. **The bucketing is the part that goes wrong**: an owner-manager
taking part salary and part dividend has income in two baskets taxed at different rates, **and the
allowances may attach to one and not the other.** **Confirm the ordering rules for the jurisdiction** — they
are not intuitive and they change the answer.

## Step 6 — Compute the tax

**Apply the jurisdiction's rate structure for the year — confirm current brackets and rates** —
**[manual]** for every rate:

- **Progressive brackets applied to ordinary income**
- **Special rates for dividends / capital gains where applicable**
- **Surcharges / additional taxes for higher incomes**
- **Social / national insurance contributions if computed alongside income tax**

```
Tax on ordinary income (through brackets)
+ Tax on dividends/capital gains (at applicable rates)
+ Any surcharges / additional taxes
= Tax before credits
```

**Every rate on this list is `[manual]` and appears on the statutory values sheet** — the same discipline as
the payroll tax filings. **Nothing enters this computation that cannot be traced to a current source.**

## Step 7 — Apply tax credits

**Jurisdiction-specific — confirm eligibility and current amounts** — **[manual]** except where noted:

- **Family / child credits**
- **Foreign tax credits** — for foreign income taxed abroad
- **Earned-income / low-income credits**
- **Education, energy, or other statutory credits**
- **Withholding and estimated payments already made** — **[gated]**: **withholding on owner salary from a
  connected business is `[auto]`**; personal estimated payments are `[manual]`

```
Tax before credits
− Non-refundable credits (limited to tax due)
− Refundable credits / payments and withholding
= Balance due or refund
```

**The ordering matters** — **non-refundable credits are capped at the tax due and are wasted beyond it,
while refundable ones are not** — so **applying them in the wrong order changes the refund.** Confirm the
jurisdiction's ordering.

## Step 8 — Compute balance due / refund and obligations

- **Net tax payable or refund** — **[auto]** arithmetic
- **Estimated-payment requirements for the next year** — **[manual]**
- **Filing and payment deadlines for the jurisdiction** — **[manual]**
- **Penalties / interest exposure if underpaid** — **flag, don't compute punitive figures without confirming
  rules** — **[manual]**

## Step 9 — Document checklist and organization

**Produce a checklist mapping each figure to its source document, and flag missing documents** —
**[gated]**:

- **Each income item → supporting statement**
- **Each deduction → receipt / evidence**
- **Carryforwards from the prior year**
- **Items needing clarification**

**This makes the return reviewable and audit-ready.**

**Mosofin addition to the checklist**: **business-sourced figures cite the tool call, the entity
`display_name` and the as-at date** — which is a stronger reference than "per the accounts", and it lets the
reviewer re-derive the figure. **Every other line cites a document the taxpayer holds.**

## Step 10 — Output

Deliver an `.xlsx` personal tax workpaper:

**Sheet 1: Tax Computation Summary** — **income → deductions → taxable income → tax → credits → balance due
or refund.** Plus the header: the **taxpayer**, the **tax year**, the **jurisdiction**, the entities in
scope by `display_name`, and **whether any figure rests on `mock` data**.

**Sheet 2: Income Detail** — **by type, gross, withholding, source document**, **with each line marked
business-sourced or supplied**.

**Sheet 3: Deductions & Reliefs** — **itemized with evidence references; standard-versus-itemized comparison
if applicable**.

**Sheet 4: Capital Gains** — **disposals, gains and losses, exemptions, carryforwards**. **`[manual]`
throughout.**

**Sheet 5: Credits & Payments** — **credits, withholding, estimated payments**.

**Sheet 6: Document Checklist** — **each figure → document; missing items flagged.**

**Sheet 7: Open Items / Confirmations** — **rates, allowances, and treatment calls flagged for current-source
confirmation and professional review.**

**Sheet 8: Business-Sourced Figures — NEW, Mosofin-specific** — every figure taken from a connected entity,
with the entity, the tool call, the as-at date, **and the tax adjustment still required**. **Keeps the
business boundary visible.**

**Sheet 9: Statutory Values Used — NEW, Mosofin-specific** — every rate, band, allowance, threshold and
deadline, with **source and year**. **Nothing appears in a computation that is not on this sheet.**

**Sheet 10: Coverage — NEW, Mosofin-specific**

| Task | Source (entity `display_name` or document) | Verdict | Tool used | As-at date | `mock` | Gap |

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming:** `Personal_Tax_[YYYY]_[Name].xlsx`

**Grounding:** every business figure traces to a tool result in this conversation; **every personal figure
to a document the taxpayer holds; every statutory value to Sheet 9.** End with a single **Data sources**
line. **Recommend qualified professional review before filing** — explicitly, in the output, not only here.

## Step 11 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed** — **and this skill is the one exception to the usual evolution
pattern.**

**Persist nothing about the taxpayer.** **No income, no deductions, no credits, no balances, no household
details, no residency conclusions, no prior-year figures, and no rates or allowances** — the last because
they change annually and a stale band produces a wrong return.

**If the user explicitly asks to save a customized version after seeing the results**, the only things worth
storing are **structural and entity-level, not personal**:

- **Which connected entities the taxpayer has an interest in, and in what capacity** — **and only with
  explicit consent**, since it records a person's business interests
- **The account map** for owner drawings, distributions and capital in those entities
- **The jurisdiction and the sources** from which rates are confirmed — **the sources, never the values**
- **The basis-period convention** where the business year and tax year differ
- The replay recipe for the business-sourced figures

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and any preference file; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files.

**When in doubt here, store nothing.** **A personal tax computation is among the most sensitive documents a
person has**, and the convenience of pre-filling next year does not justify holding it. **The taxpayer's
own records are the right place for their own data.**

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run.

---

## Both entity scenarios

**No connected business, or none the taxpayer has an interest in.** **The workflow runs entirely on supplied
documents.** **This is complete, not degraded** — say so and proceed. The coverage sheet will read `manual`
throughout, which is correct.

**One or more connected entities the taxpayer has an interest in.** Then:

- **Read only the entities the taxpayer has an interest in.** Others are out of scope for a personal
  return, and reading them compiles data about third parties.
- **Each entity supplies its own figures**, and **an owner with interests in several has several sets** —
  profit shares, distributions and drawings from each, each with its own year end.
- **Partnership or shared ownership means the taxpayer's share, not the whole.** **[manual]** to establish
  the share; **`[auto]` to compute it once known.** **Never report a whole-entity figure as the taxpayer's
  income.**
- **Where other owners exist, their positions are not the taxpayer's business.** Read the taxpayer's own
  capital and drawings accounts, not the others'.
- **Different entities may have different year ends**, and the basis-period question in Step 1 applies to
  each separately.
- **Intra-group arrangements** — a management company paying an owner from one entity while the profits sit
  in another — **need the whole picture**, and the taxpayer should say which entities are involved rather
  than the reader inferring it.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each figure's source.
