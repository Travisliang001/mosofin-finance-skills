<!-- goodwill-and-impairment-testing · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding) — Mosofin addition
- Step 0b — Scope from the balance sheet (Mosofin addition)
- Step 1 — Identify the asset and applicable rules
- Step 2 — Assess for triggering events
- Step 3 — Optional qualitative assessment ("Step 0" — US GAAP only)
- Step 4 — Quantitative test — goodwill (US GAAP ASC 350)
- Step 5 — Quantitative test — goodwill (IFRS IAS 36)
- Step 6 — Long-lived assets / amortizable intangibles
- Step 7 — Value-in-use / DCF mechanics (IFRS, and US GAAP fair value)
- Step 8 — Reversal of impairment (IFRS only)
- Step 9 — Record the impairment
- Step 10 — Disclosures
- Step 11 — Output
- Step 12 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Never drop a task because no tool covers it.** The valuation work here is legitimately `[manual]` and
specialist, and saying so is the honest result.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding) — Mosofin addition

**Batch independent reads into one message** — the balances, the segment performance, the customer revenue
and the impairment history do not depend on each other. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`search_accounts`* — **goodwill, intangibles, PP&E, accumulated depreciation and amortization, and any
  impairment expense account** — usually **[auto]**
- *`get_balance_sheet`* / *`get_trial_balance`* — **the carrying amounts** — usually **[auto]**
- *`get_profit_and_loss`* **by period and by class / department / location** — **the segment performance
  trend, which is the triggering-event evidence** — usually **[auto]**
- *`get_general_ledger`* on **goodwill and impairment accounts** — **prior impairments and their dates** —
  usually **[auto]**
- *`search_customers`* + revenue by customer over time — **customer attrition** — usually **[auto]**
- *`get_cash_flow_statement`* or cash movements by segment where available — usually **[auto]**
- *`search_classes`* / *`search_departments`* / *`search_locations`* — **candidate unit-of-account
  structure** — usually **[auto]**
- *`get_company_info`* — legal name, currency, **year-end** — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — **an impairment conclusion is a material,
audit-scrutinised charge to profit.** A carrying amount from fixtures makes the whole comparison
meaningless.

## Step 0b — Scope from the balance sheet (Mosofin addition)

**Run before Step 1.** **[auto]**, one query, and it saves the rest of the exercise from being hypothetical:

| Test | Applies if the balance sheet shows… |
|---|---|
| **Goodwill impairment** | a goodwill balance |
| **Indefinite-lived intangible test** | intangibles not being amortized |
| **Long-lived asset test** | material PP&E or amortizing intangibles **and** a triggering event |

**Report what exists, with amounts and as-at dates — and report what does not.** *"No goodwill on the
balance sheet, so the ASC 350 test does not apply"* is a documented scoping conclusion.

**[auto]** check while you are there: **an intangible with no amortization being charged** is either
indefinite-lived — and therefore subject to annual testing, which may not be happening — or finite-lived
with amortization that stopped. Both are worth raising.

## Step 1 — Identify the asset and applicable rules

**Different assets follow different impairment guidance** — **[manual]** to apply, `[auto]` to scope:

**Goodwill**:
- **Not amortized; tested for impairment at least annually and on triggering events**
- **US GAAP (ASC 350)**: tested at the **reporting unit** level; **impairment = carrying amount of the
  reporting unit (including goodwill) − fair value of the reporting unit, limited to the carrying amount of
  goodwill** (post-**ASU 2017-04** simplification)
- **IFRS (IAS 36)**: goodwill allocated to **cash-generating units (CGUs) or groups of CGUs**; **impairment
  = carrying amount of CGU − recoverable amount** (higher of **fair value less costs of disposal** and
  **value in use**)

**Indefinite-lived intangibles** — e.g. trade names with indefinite life: **tested annually and on
triggers; similar to goodwill but at the asset level**, not reporting unit / CGU level.

**Long-lived assets and finite-lived intangibles** (PP&E, amortizable intangibles): **tested only on
triggering events**:
- **US GAAP (ASC 360)**: **two-step — recoverability test (undiscounted cash flows vs. carrying amount). If
  not recoverable, impairment = carrying amount − fair value**
- **IFRS (IAS 36)**: **one-step — carrying amount vs. recoverable amount** (higher of fair value less costs
  and value in use)

**The framework and asset type determine the mechanics.**

## Step 2 — Assess for triggering events

**Indicators that might indicate impairment.** **This is where the workspace contributes most** — each
indicator is marked with its verdict:

- **Significant decline in market value** — **[manual]**; needs a market price
- **Adverse changes in business climate, market, or regulatory environment** — **[manual]**
- **Loss of key customers, contracts, or markets** — **[auto]** ⭐ **Revenue by customer across periods
  shows attrition directly**: customers who bought last year and not this one, concentration shifting, a
  top-ten list that has changed. Quantifiable, and one of the earliest real signals.
- **Significant declines in operating performance or cash flows** — **[auto]** ⭐ **Segment P&L across
  periods, by class, department or location.** The single most testable indicator, and it maps to the unit
  of account.
- **Cost overruns, accumulated costs exceeding expectations** — **[gated]**; actual costs are `[auto]`,
  the expectation is `[manual]`
- **Net assets exceeding market capitalization** (for public entities) — **[gated]**; **net assets are
  `[auto]`, market capitalization is `[manual]`.** Supply the market cap and the comparison is immediate
- **Adverse changes in legal factors** — **[manual]**
- **Restructuring, disposal plans** — **[manual]**; intent is not in a ledger

**If a triggering event exists for long-lived assets, perform the test. For goodwill and indefinite-lived,
the annual test is required regardless, but triggering events require an interim test.**

**Mosofin addition — make this monitoring, not an annual question.** The two `[auto]` indicators can be
**run every month**, which is how a triggering event is meant to be caught — **between annual tests, when
there is still time to respond.** Store the segment and customer baselines (Step 12) and compare each
period. **Report the trend with its magnitude and duration**: a single weak month is noise, three declining
quarters in one unit is an indicator.

## Step 3 — Optional qualitative assessment ("Step 0" — US GAAP only)

**For goodwill and indefinite-lived intangibles under US GAAP, an entity may first perform a qualitative
assessment to determine whether it's more likely than not that the fair value is less than the carrying
amount. If "not more likely than not," skip the quantitative test. If yes, perform the quantitative test.**

**IFRS does not have this qualitative shortcut for goodwill — the quantitative test is required annually.**

**Document the qualitative factors and conclusion.** **[gated]**: the conclusion is judgment, but **the
`[auto]` evidence from Step 2 is exactly what a qualitative assessment should be built on.** A qualitative
conclusion supported by segment trend data is defensible; one supported by assertion is not — and this is
the assessment auditors challenge most.

## Step 4 — Quantitative test — goodwill (US GAAP ASC 350)

**For each reporting unit with allocated goodwill:**

1. **Determine the fair value of the reporting unit** — typically **income approach DCF and/or market
   approach comparables** — **valuation work**. **[manual]**
2. **Compare to the carrying amount of the reporting unit**, including allocated goodwill — **[gated]**:
   balances `[auto]`, allocation `[manual]`
3. **If carrying amount > fair value: impairment = carrying amount − fair value, limited to the goodwill
   carrying amount** — **[auto]** arithmetic
4. **Recognize impairment loss in operating P&L**

**The post-ASU 2017-04 model eliminated the previous "Step 2" hypothetical PPA — the impairment is simply
the carrying-vs-fair-value difference, subject to the goodwill cap.**

## Step 5 — Quantitative test — goodwill (IFRS IAS 36)

**For each CGU (or group of CGUs) to which goodwill is allocated:**

1. **Determine recoverable amount = higher of:**
   - **Fair value less costs of disposal**
   - **Value in use** = **present value of future cash flows from the CGU**, using a **pre-tax discount rate
     consistent with the cash flow basis**

   **[manual]**, both.
2. **Compare to carrying amount of the CGU** — **[gated]**
3. **If carrying amount > recoverable amount: impairment = the difference** — **[auto]** arithmetic
4. **Allocation of impairment loss: first reduce goodwill in the CGU to zero; then allocate the remainder
   pro rata to other assets in the CGU** — subject to a floor that **no individual asset is reduced below
   the higher of its fair value less costs, value in use, or zero**

**The allocation floor is easy to miss and it constrains the result** — applying the pro-rata allocation
without it writes assets below values they demonstrably still have.

## Step 6 — Long-lived assets / amortizable intangibles

**US GAAP (ASC 360) — only when triggers exist:**

1. **Recoverability test**: are **undiscounted** cash flows from the asset group **≥ carrying amount**? **If
   yes, no impairment. If no, proceed.** **[manual]** on the cash flows
2. **Measurement**: **impairment = carrying amount − fair value** — a discounted-cash-flow-based or market
   value. **[manual]**
3. **Allocate the impairment within the asset group**

**IFRS (IAS 36) — when triggers exist**: **directly compare carrying amount to recoverable amount;
impairment = the shortfall.**

**The undiscounted / discounted distinction is the trap here** — see the edge cases. **The US GAAP
recoverability test uses undiscounted cash flows deliberately, as a higher bar**; using discounted figures
there finds impairments that the standard does not require.

## Step 7 — Value-in-use / DCF mechanics (IFRS, and US GAAP fair value)

**For DCF-based valuations** — **[manual]** throughout, and **specialist work**:

- **Cash flow projections: 5 years typical; beyond that, extrapolate with a long-term growth rate not
  exceeding industry / economy long-term growth**
- **Projections based on the entity's most recent budgets / forecasts** (`budget-builder`,
  `rolling-forecast`), **with caution on uncommitted improvements** — **IAS 36 specifically excludes the
  benefit of future restructurings not yet committed and enhancements to performance**
- **Pre-tax discount rate** (IFRS value in use); **post-tax for fair value** (often)
- **Terminal value** (if applicable)
- **Sensitivity to key assumptions** — **this is heavy specialist work; flag for valuation specialists**

**Mosofin contribution — the historical anchor.** **[auto]**: the entity's **actual** results by segment for
recent years are readable, which lets you state **how the projection compares to what has actually
happened.** A forecast of 12% growth against three years of decline is not a valuation judgment to make
here — but **stating the divergence is a factual observation**, and it is precisely what the edge case
about defensible projections is warning about. **Anchor in actual budgets, not aspirational targets** — and
the actuals are right there.

## Step 8 — Reversal of impairment (IFRS only)

**IFRS (IAS 36):**

- **Impairment of goodwill: never reversed**
- **Impairment of other assets: reversed if recoverable amount has increased, up to the carrying amount
  that would have existed (net of depreciation / amortization) without the impairment**

**US GAAP: impairment generally not reversed** — once impaired, **the new carrying amount is the new cost**.

**A key conversion difference** (`gaap-vs-ifrs-conversion`).

**[gated]**: **the prior impairment and its date are `[auto]`** from the impairment account history, and the
notional carrying amount without the impairment is computable — **but whether the recoverable amount has
recovered is `[manual]`.**

## Step 9 — Record the impairment

`DR` is a debit, `CR` a credit. **Mosofin does not post** — this is a proposal:

```
DR  Impairment Loss (P&L)                  $impairment
    CR  Goodwill / Asset                       $impairment
```

**For long-lived asset groups under US GAAP, allocate the impairment within the group** — typically **pro
rata to long-lived assets, subject to floors**. **For IFRS CGUs, allocate to goodwill first, then pro
rata.**

Use the **real account names from the connected chart of accounts** (*`search_accounts`*, **[auto]**).

## Step 10 — Disclosures

For `notes-to-financial-statements`:

- **The asset / unit impaired and the loss** — **[auto]** once determined
- **Description of facts and circumstances** — **[gated]**; the `[auto]` trend evidence supports it
- **The method of determining fair value / recoverable amount, including key assumptions** — discount rate,
  growth rates — **and sensitivity** — **[manual]**
- **For goodwill: changes by reporting unit / CGU** — **[gated]**
- **Reversals (IFRS) where applicable** — **[gated]**

**Significant disclosure rigor is expected — assumptions are scrutinized.** Record **every assumption with
its source and date**; this is the disclosure area where preparers are challenged hardest.

## Step 11 — Output

Deliver an `.xlsx` workpaper:

**Sheet 1: Test Scope** — **what's tested, framework, unit of account (reporting units / CGUs), triggering
events.** Plus the Mosofin header block: workspace name; the entity by `display_name`; each excluded company
file and why; whether any figure rests on `mock` data.

**Sheet 2: Qualitative Assessment** (US GAAP option) — factors considered, conclusion, **with the `[auto]`
trend evidence supporting it**.

**Sheet 3: Reporting Unit / CGU Identification** — **composition, carrying amounts, allocated goodwill.**
Add a column for **how the unit was identified** — segment dimension, entity, or definitional analysis.

**Sheet 4: Fair Value / Recoverable Amount Computation** — **DCF, market comparables, key assumptions,
sensitivity.** **Every input `[manual]`, with source and date.**

**Sheet 5: Impairment Computation** — **carrying vs. fair value / recoverable; impairment by asset / unit;
allocation within CGU / group**, with the **allocation floor** applied and shown.

**Sheet 6: Journal Entries** — marked as **proposals**.

**Sheet 7: Reversal Assessment** (IFRS, non-goodwill) — if applicable, with the prior impairment and its
date from the ledger.

**Sheet 8: Disclosures** — disclosure-ready data including assumption sensitivity.

**Sheet 9: Open Items / Valuation Specialist** — specialist-required valuation work.

**Sheet 10: Triggering Event Monitoring — NEW, Mosofin-specific**

| Indicator | Verdict | Measure | This period | Trend | Threshold crossed? |

The eight indicators, with the two `[auto]` ones measured and trended, and the six `[manual]` ones recorded
with their owner. **Designed to be re-run between annual tests.**

**Sheet 11: Coverage — NEW, Mosofin-specific**

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used / external source | As-at date | Policy | `mock` | Gap |

**Every valuation row reads `manual`.** That is the correct entry, and the honest one.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming:** `Impairment_Test_[YYYY-MM]_[EntityName].xlsx`

Every file states which datasource and `display_name` it covers.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where the data does not
cover something — every fair value, every projection, every rate — **name the source required** instead of
estimating.

## Step 12 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The unit-of-account definitions** — which reporting units or CGUs exist, **what each comprises**, and
  **how the definitional test was satisfied**. The most valuable asset here, and it should not change
  between periods without a reason
- **The goodwill allocation to units and its basis** — **the allocation drives the outcome**, so it must be
  consistent and documented
- **The framework** and the elections within it, including whether the qualitative shortcut is used
- **The annual test date**
- **The account map**: goodwill, intangibles by life type, impairment expense
- **The segment-to-unit mapping** — which classes, departments or locations correspond to which unit, for
  the monitoring in Step 2
- **The valuation approach and specialist** — who performs it, on what basis, how often. **Not the values**
- **The discount rate basis** — pre-tax or post-tax, and how it is derived. **Not the rate**
- The replay recipe: the exact sequence of reads that produced the carrying amounts and the trend monitoring

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist fair values, recoverable amounts, cash flow projections, discount rates, carrying amounts or
impairment conclusions.** All of it is state, and **a stale fair value reused in a later period is a
material misstatement waiting to happen** — recoverable amounts move with exactly the conditions the test
exists to detect.

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / Northbrook
Services — IFRS, two CGUs mapped to the Consulting and Managed Services classes, goodwill allocated 60/40 on
acquisition-date revenue, annual test at 31 December, pre-tax VIU" — not "two CGUs". **Units of account are
entity-specific by construction**, and applying one company file's CGU structure to another tests groupings
that do not exist there. Record the chosen **scenario** (single vs multi, and whether units map to entities)
as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's.**

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. Units of account are identified within
the entity, usually by segment dimension.

**Multi-entity.** **The common case where goodwill exists**, since goodwill usually arises from acquiring a
business. Steps 0–11 run **once per entity**, each call targeting exactly one `data_source_id`, every
carrying amount carrying its entity's `display_name`. Then:

- **A reporting unit or CGU may be an entire connected entity.** Where an acquisition was kept as a separate
  company file, **that file is the natural unit of account** — and its full P&L history is exactly the
  monitoring data Step 2 needs. This is the cleanest case this skill ever gets.
- **But goodwill often sits in the parent's books while the business sits in the subsidiary's.** The
  goodwill balance and the cash flows that support it are then **in different company files**. **Read both**,
  and say so in the workpaper — a carrying amount from one file compared to a recoverable amount derived
  from another needs that stated plainly.
- **A CGU can span entities**, where operations are integrated across legal boundaries. The definitional
  test is about **independent cash inflows**, not about legal structure. Do not let the connected file list
  decide the answer.
- **Goodwill allocation across units and entities must be documented and consistent** — reallocating between
  periods changes which unit fails.
- **Impairment recorded in the wrong entity** misstates two sets of accounts. Record it where the goodwill
  is carried.
- **On consolidation, goodwill arising at group level may not exist in any entity's own books.** Test it at
  the level it exists; see `consolidation-and-eliminations` and `business-combinations-asc805`.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict per company
file.
