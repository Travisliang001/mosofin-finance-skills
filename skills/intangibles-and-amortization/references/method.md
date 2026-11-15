<!-- intangibles-and-amortization · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding) — Mosofin addition
- Step 0b — The amortization presence check (Mosofin addition)
- Step 1 — Identify intangible asset categories
- Step 2 — Determine useful life
- Step 3 — Choose amortization method
- Step 4 — Capitalization of internally developed intangibles
- Step 4b — Scan both directions (Mosofin addition)
- Step 5 — Compute amortization
- Step 6 — Construct the amortization JE
- Step 7 — Impairment testing
- Step 8 — Useful life reassessment
- Step 9 — Disposal / derecognition
- Step 10 — Roll-forward and tie-out
- Step 11 — Disclosure inputs
- Step 12 — Output
- Step 13 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Never drop a task because no tool covers it.** The stage determinations and the useful lives are
legitimately `[manual]`.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding) — Mosofin addition

**Batch independent reads into one message** — the accounts, the balances, the movements and the project
spend do not depend on each other. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`search_accounts`* — **intangible asset accounts by class, accumulated amortization, amortization
  expense, impairment, and the R&D, software, contractor and hosting expense accounts** — usually **[auto]**
- *`get_balance_sheet`* / *`get_trial_balance`* — **cost and accumulated amortization**, opening and
  closing — usually **[auto]**
- *`get_general_ledger`* on the **intangible accounts** — **capitalizations and disposals** — usually
  **[auto]**
- *`get_general_ledger`* on **accumulated amortization and amortization expense** — the charge and its
  pattern — usually **[auto]**
- *`get_profit_and_loss`* **by class / project / department** — **development spend by project, the Step 4
  population** — usually **[auto]**
- *`search_bills`* / *`search_purchases`* — **contractor and external development invoices** — usually
  **[auto]**
- *`search_classes`* / *`search_departments`* / *`search_projects`* — **the project dimension** — usually
  **[auto]**
- *`get_company_info`* — legal name, currency, year-end — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — **capitalizing development costs moves expense off
the income statement**, so a fixture-based capitalization figure misstates reported profit directly.

## Step 0b — The amortization presence check (Mosofin addition)

**Run before Step 1.** **[auto]**, one read, and it is the cheapest useful finding in the skill.

**For each intangible account, compare cost against accumulated amortization and the period charge.**

| Pattern | What it means | Action |
|---|---|---|
| **Cost, no accumulated amortization, no charge** | **Indefinite-lived, or amortization never started** | Ask which. **If indefinite, an annual impairment test is mandatory — confirm it happens.** |
| **Accumulated amortization equals cost** | Fully amortized | Is the asset still in use? Should it be derecognised? |
| **Charge stopped mid-life** | A recurring journal that lapsed | Investigate |
| **Charge with no cost** | A posting error | Investigate |

**An indefinite-lived intangible that has never been impairment-tested is a real audit finding**, and it is
readable from two numbers.

## Step 1 — Identify intangible asset categories

**Common identifiable intangible assets** — **[gated]**: the accounts are `[auto]`, the classification is
`[manual]`:

**Acquired intangibles** — from business combinations or asset purchases:

- **Customer lists / customer relationships**
- **Trade names / trademarks**
- **Patents**
- **Copyrights**
- **Licenses and franchises**
- **Contracts / leases (favorable terms)**
- **Non-compete agreements**
- **Software (purchased)**
- **Domain names**
- **Order backlog**

**Internally developed intangibles:**

- **Internal-use software** (per **ASC 350-40 / IAS 38**)
- **Capitalizable development costs (under IFRS)** — **research costs always expensed**
- **Patent application and registration costs**
- **Trademark registration costs**

**Goodwill: separate from this skill. Recognized only in business
combinations.** **[auto]** check: **a goodwill balance in the intangibles accounts should be identified and
routed to that skill**, not amortized here.

## Step 2 — Determine useful life

**Per intangible** — **[manual]**:

- **Finite useful life**: **amortized over the life**
- **Indefinite useful life**: **NOT amortized; tested for impairment annually** and on triggering events

**Useful life considerations:**

- **Legal or contractual life** — patents: 20 years from application; trademark: indefinite as long as
  renewed; copyright: per jurisdiction
- **Economic useful life** — **often shorter than legal**
- **Renewal expected without significant cost or effort?**
- **Pattern of consumption**

**If the intangible is renewable indefinitely at minimal cost — e.g. a maintained trademark — it may be
indefinite-lived.**

**For finite-life intangibles, useful life ranges:**

- **Customer relationships**: 5–15 years typically
- **Customer lists**: 5–10 years
- **Patents**: legal life or shorter economic life
- **Software**: 3–7 years
- **Non-compete**: term of the non-compete
- **Order backlog**: typically less than 1 year — **so often expensed quickly or recognized as revenue
  allocated**

**These are ranges, not a policy.** Record the entity's own life per class and its basis.

**[auto]** support for the renewal question: **whether renewal costs are actually being incurred** —
trademark renewal fees, licence fees — is readable, and **an "indefinite because we always renew" conclusion
sits better when the renewal spend is in the ledger** than when it is asserted.

## Step 3 — Choose amortization method

**Most common: straight-line over useful life.** — **[manual]** to elect, `[auto]` to compute.

**Alternative: pattern of expected consumption.** If clearly identifiable — based on units, time-decay — use
that pattern. **Otherwise, default to straight-line.**

**For both US GAAP (ASC 350) and IFRS (IAS 38), straight-line is the default if the pattern is not reliably
determinable.**

## Step 4 — Capitalization of internally developed intangibles

**This is the step the workspace most changes**, so the verdicts are given per element.

**Internal-use software (ASC 350-40 / similar IFRS guidance via IAS 38):**

**Three stages:**

1. **Preliminary project stage**: planning, exploration → **expense**
2. **Application development stage**: design, coding, testing, configuration → **capitalize** — direct
   labor, materials, fees, allocated overhead
3. **Post-implementation / operation stage**: training, maintenance, upgrades → **expense**, except
   **significant upgrades that add functionality**

**Capitalization starts when:**
- **Preliminary stage is complete**
- **Management has authorized and committed to the project**
- **It's probable the project will be completed and used**

**Capitalization stops when:**
- **The software is ready for its intended use** — substantially complete and ready for production

**[gated]**, split cleanly:

- **The cost population is `[auto]`.** Development spend by project and by month — salaries, contractors,
  external fees, hosting — is readable where project tagging exists (*`get_profit_and_loss`* by class or
  project, *`search_bills`*). **Present it as a cost profile by month**, which is exactly the shape the
  stage analysis needs.
- **The stage boundaries are `[manual]`.** Ask for the dates on which the preliminary stage completed and
  the software became ready for use. **Then the capitalizable amount follows from the profile** — costs
  between those two dates, of the qualifying types.
- **Allocated overhead is `[gated]`** — the pool is readable, the allocation basis is policy.

**Mosofin check — the cost profile shape.** **[auto]**: **development spend continuing at the same rate
after the stated go-live date** suggests either the ready-for-use date is wrong or post-implementation costs
are being capitalized. **A cost profile that starts before the authorization date** raises the mirror
question. **Report the profile against the stated dates; do not adjudicate the stage.**

**Externally developed software for sale (ASC 985-20):**
- **Costs prior to establishing technological feasibility → expense (R&D)**
- **Costs after technological feasibility → capitalize until product is available for general release**
- **After general release → either inventory or amortization begins**

**IFRS development costs (IAS 38):**
- **Research costs → always expensed**
- **Development costs → capitalize ONLY if all six criteria are met**: **technical feasibility, intent to
  complete, ability to use or sell, future economic benefits, resources to complete, reliable measurement**
- **Strict in practice; many tech companies expense rather than capitalize even under IFRS**

**US GAAP and IFRS differ materially on this — apply the user's framework.**

## Step 4b — Scan both directions (Mosofin addition)

**[auto]**, and it mirrors the capitalization threshold scan in
`fixed-asset-register-and-depreciation`:

1. **Expensed costs that might qualify.** Development spend on a project that was capitalized, sitting in
   expense accounts during the capitalization window. **Either a coding inconsistency or a deliberate
   exclusion** — worth knowing which.
2. **Capitalized costs that might not qualify.** Amounts in intangible accounts that look like training,
   maintenance, data conversion, or **marketing**. **Built brands are never recognized** — marketing spend
   capitalized as brand value is a straightforward error.
3. **Cloud and hosting spend.** Readable, and **the cloud arrangement question in the edge cases turns on
   it** — implementation costs in a cloud arrangement may be a prepaid asset rather than an intangible.

**Report candidates with vendor, date, amount, account and description. Never adjudicate — the stage and
policy calls are the user's.**

## Step 5 — Compute amortization

For finite-life intangibles — **[gated]**: arithmetic `[auto]`, register `[manual]`:

```
Monthly amortization = (Cost − Residual) / Useful life in months
```

**Residual value is usually $0 for intangibles** unless a third party has committed to acquire it at end of
useful life.

**For partial periods, prorate based on the days / months of in-service.**

**For indefinite-life intangibles: no amortization. Carry at cost less impairment.**

**[auto]** sanity check: **amortization charged ÷ gross cost per class, annualized, gives an implied
life.** Compare it to the policy life. A large divergence means wrong lives, missing assets, or a stale
recurring journal.

## Step 6 — Construct the amortization JE

**Hand off to `journal-entry-builder`.** `DR` is a debit, `CR` a credit. **Mosofin does not post** — this is
a proposal:

```
DR  Amortization Expense                            $period amortization
    CR  Accumulated Amortization (per class)           $period amortization
Memo: Monthly amortization — [class] — [period]
```

**If aggregating across multiple intangibles, sum by expense account.** **[auto]** to determine whether
accumulated amortization is per class or consolidated in this chart (*`search_accounts`*).

## Step 7 — Impairment testing

**Finite-life intangibles** — **[manual]** on the valuation inputs:
- **Test when triggering events occur** — decline in market, change in use, regulatory action, etc.
- **Step 1 (US GAAP): undiscounted cash flows < carrying value?** If so, proceed to step 2
- **Step 2: impairment = carrying value − fair value**
- **IFRS (IAS 36): recoverable amount = higher of fair value less costs of disposal and value in use.
  Impairment = carrying value − recoverable amount**
- **IFRS allows reversal if circumstances change; US GAAP does not**

**Indefinite-life intangibles:**
- **Tested annually** and on triggering events
- **US GAAP: qualitative assessment first** — "more likely than not" impaired? — **if yes, quantitative
  test**
- **IFRS: same general approach but allows reversal**

**Document the test.**

**[auto]** contribution — indicators only, and **carrying amounts**: see
the goodwill impairment test, where the same split applies. **The carrying amount is exact and
readable; the recoverable amount is not on this surface.** **Never conclude impairment from ledger data.**

## Step 8 — Useful life reassessment

**At each reporting date, review the useful life of finite-life intangibles.** **[manual]** to conclude:

- **Useful life shortened**: **amortize remaining NBV over the revised shorter life** — a change in
  estimate, **prospective**
- **Useful life lengthened**: **amortize over the revised longer life**

**If an indefinite-life intangible's life has become finite** — e.g. a trademark no longer renewed —
**begin amortization.**

**[auto]** prompt: **a customer relationship intangible whose associated customers have churned**, or a
trademark whose renewal fees have stopped appearing, are both readable signals that a life needs
revisiting. **Prompts, not conclusions.**

## Step 9 — Disposal / derecognition

**When an intangible is sold, abandoned, or expires** — **[gated]**:

- **Gain / loss = Proceeds − NBV at disposal**
- **Same JE structure as fixed asset disposal** (`fixed-asset-register-and-depreciation`)

**For abandonment (no proceeds), full NBV is a loss.**

**For an intangible expired by its terms** — e.g. a patent expired — **NBV should already be zero if
amortized correctly; if not, write off the remainder.**

**[auto]** check, the same half-disposal test as for fixed assets: **cost removed without the accumulated
amortization, or the reverse**, leaves the balance sheet wrong and usually produces a spurious gain or loss.

## Step 10 — Roll-forward and tie-out

Per intangible class — **[auto]** on the GL side, **[gated]** overall:

```
Opening Cost
+ Acquisitions / capitalizations
- Disposals (at original cost)
+/- Other adjustments
= Closing Cost

Opening Accumulated Amortization
+ Period amortization
- Disposals (accumulated amortization removed)
+/- Impairment
= Closing Accumulated Amortization

NBV = Closing Cost − Closing Accumulated Amortization
```

**Tie to GL.**

**Mosofin addition — reconcile in both directions**, exactly as for fixed assets:

1. **Register → GL.** A register asset with no GL cost is a **phantom**.
2. **GL → register.** **A capitalization with no register entry is an intangible that will never be
   amortized** — it sits at full cost indefinitely, overstating assets and understating expense.

**Report both lists separately.** Different causes, different owners.

## Step 11 — Disclosure inputs

**Both US GAAP and IFRS require disclosures:**

- **Total cost and accumulated amortization by major class** — **[auto]**
- **Weighted average remaining useful life** — **[gated]**; needs the register
- **Amortization expense for the period** — **[auto]**
- **Estimated amortization for the next 5 years** — **[gated]**; **pure arithmetic once the register
  exists**, and one of the more tedious disclosures to prepare by hand
- **Impairment charges with explanation** — **[gated]**; the charge is `[auto]`, the explanation is not
- **Indefinite-life intangibles by class** — **[gated]**; **Step 0b identifies the candidates**

## Step 12 — Output

Deliver an `.xlsx` workpaper:

**Sheet 1: Intangibles Register**

| Asset ID | Description | Class | Acquisition / Capitalization Date | In-Service Date | Cost | Useful Life | Method | Currency | Impairment to date |

Add a **Source** column: register-supplied, or derived from a GL movement.

**Sheet 2: Amortization Schedule (current period)**

| Asset ID | Class | Opening NBV | Period Amortization | Closing NBV |

**Sheet 3: Capitalizations** — **for each capitalization, the qualifying costs and basis.** **Now with the
`[auto]` cost profile by month** and the `[manual]` stage dates alongside.

**Sheet 4: Disposals**

**Sheet 5: Roll-Forward by Class**

**Sheet 6: GL Tie-Out** — **with both direction lists**: register assets missing from the GL, and GL
movements missing from the register.

**Sheet 7: Impairment Tests** — documentation and conclusions, with `[auto]`-derived indicators marked as
indicators.

**Sheet 8: 5-Year Amortization Forecast** — for disclosure.

**Sheet 9: GL Posting** — marked as **proposals**.

**Sheet 10: Capitalization Scan — NEW, Mosofin-specific**

| Direction | Date | Vendor / description | Account | Amount | Project | Question |

Both directions from Step 4b, plus cloud and hosting spend for the prepaid-versus-intangible question.

**Sheet 11: Coverage — NEW, Mosofin-specific**

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used / external source | As-at date | Policy | `mock` | Gap |

Include the **Step 0b amortization presence check** per account, and **whether the annual test on any
indefinite-lived intangible has been performed**.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming:** `Intangibles_Register_[YYYY-MM].xlsx`

Every file states which datasource and `display_name` it covers.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where the data does not
cover something — useful lives, stage dates, impairment — **name the source required** instead of
estimating.

## Step 13 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The asset class policies**: useful life or indefinite, and method, per class
- **The capitalization policy for internally developed intangibles** — **which stages qualify, which cost
  types, and the overhead allocation basis.** The most valuable stored asset here
- **The framework** and its elections — **US GAAP and IFRS differ materially on development costs**
- **The account map**: intangible accounts by class, accumulated amortization (per class or consolidated),
  amortization expense, impairment
- **The project-to-intangible mapping** — which project class feeds which capitalized asset. **The join that
  makes each period's capitalization analysis a single run**
- **The indefinite-lived intangibles list** and **the annual test date**
- **The renewal evidence basis** for indefinite-life conclusions
- **The amortization allocation basis** across departments or classes
- The replay recipe: the exact sequence of reads that produced the movements and the development cost
  profile

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist the register itself, asset-level costs, net book values or impairment amounts.** The
register is state. **And never persist the content of the intangibles** — customer list contents, patent
specifications, trade secrets or source code references. These are among the most commercially sensitive
assets a business has, and a skill bundle is not where they belong.

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / Northbrook
Software Ltd — IFRS, internal software 5yr SL capitalized from authorization to go-live, direct labour and
contractors only, no overhead, projects on Class, accum amort per class" — not "internal software 5yr SL".
**Capitalization policies differ by company file**, and applying one entity's policy to another either
capitalizes costs that should be expensed or the reverse — either way misstating profit. Record the chosen
**scenario** (single vs multi) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's.**

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One register, one roll-forward, one
tie-out.

**Multi-entity.** Steps 0–12 run **once per entity**, each call targeting exactly one `data_source_id`,
every asset and balance carrying its entity's `display_name`. Then the points specific to intangibles:

- **Acquired intangibles arise on acquisition and sit where the acquisition was recorded.** Frequently the
  parent's books, while the customer relationships they represent belong to a subsidiary's business.
  **Amortization stays where the asset is carried**; do not move it to make a management report look
  right.
- **Internally developed software is often built by one entity and used by the whole group.** **The
  capitalized asset sits with the entity that bore the cost**, and use by others is a recharge or a licence
  — **a separate transaction**, and `[manual]` from the intra-group agreement.
- **Intra-group transfers of intangibles are a transfer-pricing matter as much as an accounting one**, and
  on consolidation the asset carries at original group cost with intra-group profit and excess amortization
  eliminated. See `consolidation-and-eliminations`.
- **Policies must be consistent for consolidation.** Different useful lives for the same class of intangible
  in different subsidiaries produce a group charge that is not comparable. **Flag policy differences across
  entities.**
- **The framework may differ** where a subsidiary reports locally — and **the US GAAP / IFRS divergence on
  development costs means the same project can be capitalized in one set of books and expensed in another.**
- **Currency**: cost is held at the acquisition-date rate in functional currency; amortization runs in
  functional currency, and group translation is separate.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict per company
file.
