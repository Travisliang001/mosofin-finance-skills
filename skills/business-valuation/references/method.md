<!-- business-valuation · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding)
- Step 1 — Define purpose, standard of value, and valuation date
- Step 2 — Choose the approaches
- Step 3 — Discounted Cash Flow (DCF)
- Step 4 — Trading comparables
- Step 5 — Precedent transactions
- Step 6 — Triangulate and conclude on enterprise value
- Step 7 — Bridge to equity value
- Step 8 — Adjustments — control premium and DLOM
- Step 9 — Sensitivities
- Step 10 — Build a defensible report
- Step 11 — Output
- Step 12 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with
plain-language wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool
added.

**Never drop a task because no tool covers it.** In this skill every market input is `[manual]` by
the nature of the domain, and recording that honestly is what makes the valuation defensible.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding)

Pull the `[auto]` / `[gated]` reads. **Batch independent reads into one message** — the P&L, the
balance sheet, the cash flow statement and the ledger detail do not depend on each other. Never
serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

**Read everything as at the valuation date**, not today. That is the single most important
discipline in this step, and it is one the connected books support directly.

Typical opening batch, per in-scope entity:

- *`get_profit_and_loss`* over **several years**, annually and monthly — the earnings history,
  EBITDA, D&A and the effective tax rate — usually **[auto]**
- *`get_balance_sheet`* **at the valuation date and at each prior year-end** — the capital
  structure, net debt components, working capital and its movement — usually **[auto]**
- *`get_cash_flow`* over the same years — capex, D&A and actual cash generation, as a reality check
  on any forecast — usually **[auto]**
- *`search_accounts`* — to itemise debt-like and cash-like accounts for the bridge — usually
  **[auto]**
- *`get_general_ledger`* on the debt, cash and fixed-asset accounts — the detail behind net debt
  and capex — usually **[auto]**
- *`get_trial_balance`* — a complete account-level position at the valuation date — usually
  **[auto]**
- *`get_customer_sales`* — revenue concentration, which bears directly on risk and therefore on any
  company-specific risk premium — usually **[auto]**
- *`get_company_info`* — legal name, currency, year-end, industry — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — it cannot support a valuation conclusion,
which may be relied on in a transaction, a tax filing, or litigation.

## Step 1 — Define purpose, standard of value, and valuation date

Get this wrong and every subsequent number, however carefully computed, answers the wrong question.

**The purpose drives** — all **[manual]**:

- **Standard of value**:
  - **Fair market value**: the price between willing, informed, unrelated parties (typical for tax)
  - **Fair value** (financial reporting): a specific defined term under **ASC 820 / IFRS 13** —
    market participant assumptions
  - **Fair value** (statutory, e.g. dissenters' rights): **a different legal concept** that varies
    by jurisdiction — the same words, a different meaning
  - **Investment value**: value to a **specific** buyer (synergies, strategic fit)
- **Premise of value**: **going concern** vs. **orderly liquidation** vs. **forced liquidation** —
  is the business continuing, being wound down at leisure, or sold in a hurry?
- **Level of value**: **control vs. non-controlling**, **marketable vs. non-marketable** — which
  determines the discounts and premiums in Step 8

**Specify the valuation date** — the as-of date for the valuation. **Market data and forecasts are
anchored here.** **[auto]** to honour it on the company side: every read above takes it as the
as-of date.

## Step 2 — Choose the approaches

Three standard approaches; usually multiple are applied and triangulated:

- **Income approach (DCF)**: present value of future cash flows. **Theoretically most rigorous; most
  assumption-heavy.**
- **Market approach — Trading comps**: multiples derived from publicly-traded peer companies'
  market prices.
- **Market approach — Precedent transactions**: multiples derived from past M&A transactions of
  similar businesses (**these often include a control premium**).
- **Cost / asset approach**: rare for going concerns (more for holding companies, real estate,
  liquidation scenarios). **[auto]** contribution: where this approach is relevant, the balance
  sheet at the valuation date is directly readable — though the assets still need fair valuing.

**Most engagements weight two or three approaches; document the weighting rationale.** **[manual]**
to choose and weight.

## Step 3 — Discounted Cash Flow (DCF)

**Build the cash flow forecast** — typically 5–10 years (depending on business stability):

- Start from the forecast / `three-statement-financial-model` / `rolling-forecast` — **[manual]**
- Compute **unlevered free cash flow (FCFF)** — the cash the business generates before paying
  anyone who financed it:

```
EBIT × (1 − tax rate)
+ D&A
− Capex
− Δ Working capital
= FCFF
```

**[auto]** for every historical component of that formula — EBIT, D&A, capex and the movement in
working capital are all readable (*`get_profit_and_loss`*, *`get_cash_flow`*, *`get_balance_sheet`*
across periods). That gives a **historical FCFF series**, which is the most useful reality check
available on a forecast: a projection that departs sharply from the entity's own cash-generation
history needs a stated reason. Build it and show it alongside the forecast.

**Determine the discount rate — WACC** (for FCFF) — **[manual]** for every market input:

```
WACC = (E/V × Cost of Equity) + (D/V × Cost of Debt × (1 − tax rate))

Cost of Equity (typically CAPM) = Risk-free rate + Beta × Equity Risk Premium + adjustments
  (size premium, country/specific-company risk premium as appropriate)
```

Each input is its own decision:

- **Risk-free rate**: typically a long-term government bond yield matching the cash flow tenor —
  **confirm current** — **[manual]**
- **Equity risk premium**: from market data (current sourced) — **[manual]**
- **Beta**: from comparable companies, **unlevered then relevered** to the target's capital
  structure — **[manual]** for the peer betas; **[auto]** for the target's own capital structure
  used in the relevering
- **Size premium / specific-company premium**: from research data where used (US studies — confirm
  current) — **[manual]**. **[auto]** contribution: revenue concentration and customer churn from
  the books are legitimate evidence *for* a company-specific premium, and quantifying them is
  better than asserting a premium
- **Cost of debt**: the entity's marginal borrowing rate (or comparable) — **[gated]**: the
  **actual** rate borne is derivable from interest expense against average debt
  (*`get_profit_and_loss`*, *`get_balance_sheet`*, *`get_general_ledger`*), which is a strong
  cross-check on any assumed marginal rate
- **Capital structure weights**: **target (long-run) capital structure typically, not necessarily
  current** — **[auto]** for the current structure, **[manual]** for the target one

**All inputs are current-sourced; do not hardcode market data — confirm at the valuation date.**

**Terminal value** (the value beyond the explicit forecast period) — **most often the larger part
of DCF value** — **[manual]**:

- **Perpetuity growth (Gordon growth)**: `TV = FCF in year T+1 / (WACC − g)`, where **g is the
  long-term growth rate (should not exceed long-term economy growth)** — a g above economy growth
  implies the business eventually becomes the economy
- **Exit multiple**: `TV = year T metric (EBITDA typically) × exit multiple` (often from comps)

**Build with both methods; reconcile** — the implied perpetuity g from an exit multiple, and the
implied exit multiple from a perpetuity g. Where they imply wildly different things, one of them is
wrong.

**Compute enterprise value (DCF)**:

```
EV = PV of explicit-period FCFFs + PV of terminal value
```

**Discount each FCFF and the TV back to the valuation date at WACC.**

## Step 4 — Trading comparables

- **Select peers**: publicly-traded companies similar in industry, size, growth, profitability,
  geography, capital structure — **[manual]**
- **Compute multiples at the valuation date**: EV/Revenue, EV/EBITDA, EV/EBIT, P/E, P/B (the
  relevant ones for the industry). **Use LTM and forward (next-twelve-months) figures** — *LTM* is
  the last twelve months. **[manual]** for the peers' figures; **[auto]** for the **target's own**
  LTM metrics, which are exactly what the multiples get applied to
- **Adjust as needed** for differences (one-time items in peers, growth / margin differences) —
  **[manual]**
- **Apply ranges of multiples to the target's metrics**:
  - `EV = EBITDA × EV/EBITDA multiple`
  - **Pick a low / mid / high from the peer range with justification**
- **Display the comp set with multiples, statistics (mean / median / quartiles), and the chosen
  range**

## Step 5 — Precedent transactions

- **Select transactions**: completed M&A transactions of similar targets, **recent enough to be
  relevant** — **[manual]**
- **Compute deal multiples** based on disclosed deal terms — **[manual]**
- **Apply ranges similarly to trading comps**
- **Note**: precedent transactions typically include a **control premium**, so resulting values
  reflect a **control basis** — different from trading comps, which are minority-share-price-based.
  Mixing the two without adjusting for this is a common and material error

**Data availability and reliability vary; use only transactions with reliable data.**

## Step 6 — Triangulate and conclude on enterprise value

- Each approach yields an **EV range**
- **Compare the ranges; understand differences** — DCF assumption-driven; comps market-driven;
  precedents control-premium-driven
- **Weight or select a concluded EV range with rationale**
- **Avoid false precision — valuation conclusions are ranges, often with a "central" figure**

**[manual]** to weight and conclude. Where the three ranges barely overlap, that is itself the
finding and should be said plainly rather than averaged away.

## Step 7 — Bridge to equity value

**Enterprise value** is the value of the business's operations; **equity value** is what is left for
shareholders after the lenders are paid. This bridge is where a valuation most often goes quietly
wrong, and it is also the part a connected workspace supports best.

```
Enterprise value (EV)
− Total debt (and debt-like items per QofE definitions)
+ Cash (and cash equivalents, less restricted)
− Minority interest (if EV includes consolidated cash flows including NCI)
+ Equity-method investments (if not in EV)
= Equity value

Equity value / Diluted shares outstanding = Equity value per share
```

**[auto]** for the balance-sheet components, and **itemise them** rather than taking a summary line
(*`get_balance_sheet`*, *`search_accounts`*, *`get_general_ledger`*):

- **Total debt and debt-like items** — including finance leases, shareholder loans, deferred
  consideration and unfunded obligations, which frequently sit outside an account named "debt"
- **Cash — less restricted cash**, which is not available to shareholders and must be excluded
- **Minority interest** and **equity-method investments** as carried

**[manual]** for **diluted shares**: include in-the-money options and warrants (**treasury stock
method** or proceeds method), convertible securities, and RSUs. A cap table is not in the accounting
system, and share counts in the equity accounts are usually issued shares, not diluted ones — do
not substitute one for the other.

**Coordinate the net debt definition with `due-diligence-quality-of-earnings`** — a valuation and a
QofE that define net debt differently will not reconcile, and someone will notice.

## Step 8 — Adjustments — control premium and DLOM

- **Control premium**: applied when valuing a control interest on a basis derived from minority
  share data (trading comps). **Typically empirically observed** — **[manual]**
- **Discount for lack of marketability (DLOM)**: applied to private / restricted holdings — reflects
  **the cost of illiquidity**, that you cannot sell a private stake quickly. Various studies and
  methods — **[manual]**
- **Discount for lack of control / minority interest discount**: applied to non-controlling
  interests when valued from a controlling basis — **[manual]**

**These adjustments are significant and study-supported; document the basis. They are a major area
of valuation specialist judgment.** They are also, in percentage terms, often larger than the
differences between the three approaches — so an undocumented discount can dominate the whole
conclusion.

## Step 9 — Sensitivities

Show sensitivity to key drivers (`scenario-and-sensitivity-analysis`) — **[auto]** arithmetic once
the model exists:

- **WACC ±** (a small change in WACC swings DCF significantly)
- **Terminal growth or exit multiple ±**
- **Revenue growth ±**
- **Margin ±**

**A sensitivity table shows the range of outcomes and supports the conclusion.** For a
terminal-value-heavy DCF, the WACC × growth grid is the single most informative exhibit in the whole
workbook.

## Step 10 — Build a defensible report

A valuation report typically contains:

- **Purpose, standard of value, premise, level of value, valuation date**
- **Description of the subject company**
- **Industry and economic outlook**
- **Financial analysis**
- **Approaches considered (and why used or not)**
- **DCF detail** (forecast, WACC build, TV, discounting)
- **Comps detail** (peer selection, multiples, application)
- **Precedent transactions detail**
- **Adjustments** (control, DLOM)
- **Reconciliation and conclusion**
- **Sensitivities**
- **Limiting conditions and assumptions**

**For litigation, tax, or financial reporting use, professional standards (USPAP / SSVS / IVS) and a
qualified valuation specialist are typically required.** Say so explicitly in the report rather than
leaving it implied — and add a Mosofin-specific limiting condition stating which figures came from
the connected accounting records, as at what date, and that no market data was drawn from them.

## Step 11 — Output

Deliver an `.xlsx` valuation workbook and a report.

**Workbook (.xlsx):**

**Sheet 1: Valuation Summary** — each approach's EV range, the equity value bridge, per-share value,
weighted conclusion. Add a header block: workspace name; the entity by `display_name`; each excluded
company file and why; the **valuation date**; the currency; whether any figure rests on `mock` data.

**Sheet 2: DCF** — forecast FCFFs, WACC build, discounting, terminal value, PV of TV, EV. **Add the
historical FCFF series** alongside the forecast.

**Sheet 3: Trading Comps** — peer set, multiples table, statistics, applied range.

**Sheet 4: Precedent Transactions** — transaction list, multiples, statistics, applied range.

**Sheet 5: WACC Build** — **each input with its source and date**. This sheet is where the "no
hardcoded market data" standard is proved or fails; every row must name where the figure came from
and when.

**Sheet 6: Equity Value Bridge** — EV → equity value detailed walk, **itemised** rather than
summarised.

**Sheet 7: Adjustments** — control premium, DLOM, minority discount with supporting basis.

**Sheet 8: Sensitivities** — WACC × growth, multiples ranges, etc.

**Sheet 9: Open Items / Specialist** — items requiring valuation specialist sign-off; current market
data confirmation.

**Sheet 10: Coverage — NEW, Mosofin-specific**

| Input or task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used / external source | As-of date | Policy (enabled / permission / disabled) | `mock` | Gap — what could not be evidenced and who owns it |

Every market input reads `manual` with its external source and date, or is listed as outstanding.
An input with **no source and no date is a defect**, not an assumption.

**Report document**: a structured valuation report with the elements above (as a Word document where
the host can make one).

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming:** `Valuation_[Target]_[YYYY-MM-DD]`

Use the entity's `display_name` as `[Target]` where it is a connected company file, and the
**valuation date** as the date. Every file states which datasource and `display_name` it covers.

**Grounding:** every subject-company figure traces to a tool result in this conversation; every
market input traces to a named external source with its date. End with a single **Data sources**
line grouping calls by datasource. Where the data does not cover something — which for all market
data it will not — **name the source required** instead of estimating.

## Step 12 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them,
ask — explicitly, at that point, not earlier — whether to save this as their own customized version.
A general "yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The purpose, standard of value, premise and level of value** typically applied for this entity,
  and the specialist engaged for regulated uses
- **The peer set and the precedent transaction set** — the *identities* and the selection rationale,
  which are stable and expensive to rebuild
- **The WACC build structure** — which inputs are used, which sources they come from, and how beta
  is unlevered and relevered. **Not the values**
- **The net debt definition** — exactly which accounts are debt-like, which cash is restricted —
  agreed once with `due-diligence-quality-of-earnings` and reused
- **The normalising adjustments** applied to EBITDA and why
- **The approach weighting** and its rationale
- The replay recipe: the exact sequence of reads that produced the financial foundation

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files;
set `datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference
files alongside the installed skill.

**Never persist market data values, the concluded value, the forecast, or any share-count or cap
table detail.** Market values are stale the moment they are stored and re-using them is exactly the
"hardcoded market data" failure the standards forbid; a concluded value is a point-in-time opinion
that could mislead if reused; cap table data is confidential. **Persist the structure and the
sources, never the numbers.**

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks /
Northbrook Trading — FMV standard, going concern, control basis; peers: [set]; net debt includes
finance leases and shareholder loans" — not "peers: [set]". Entities in one group can be in
genuinely different industries with different peers, and an unlabelled peer set applied to the wrong
company produces a confidently wrong valuation. Record the chosen **scenario** (entity vs group, and
which set) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's** — and market data is neither: it is the world's, and must be re-sourced each time.

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that
is no longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One financial foundation, one
DCF, one bridge.

**Group.** Steps 0–11 run the financial foundation **once per entity**, each call targeting exactly
one `data_source_id`, every figure carrying its entity's `display_name`. Then consolidate
deliberately:

- **A group valuation is not the sum of entity valuations.** Eliminate intercompany revenue, cost
  and balances before computing group EBITDA or group net debt, or both are overstated. See
  `consolidation-and-eliminations`.
- **Net debt is a group concept.** Cash trapped in one entity and debt sitting in another do not
  simply net if the cash cannot be moved — restricted or non-distributable cash is not available to
  the group's shareholders. Itemise per entity, then state what genuinely nets.
- **Minority interests** in partly-owned entities are deducted in the bridge, and their measurement
  must be consistent with how the cash flows were consolidated.
- **Different entities may warrant different peer sets** if they operate in different industries —
  a sum-of-the-parts valuation is then the more honest approach, and should be labelled as such.
- **Capability is checked per entity** at Gate 2: a component with narrower permissions may have a
  `[manual]` foundation while its siblings are `[auto]`. The coverage sheet shows this per file.
