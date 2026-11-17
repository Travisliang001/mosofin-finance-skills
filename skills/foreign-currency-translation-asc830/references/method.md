<!-- foreign-currency-translation-asc830 · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding) — Mosofin addition
- Step 1 — Determine functional currency
- Step 2 — Remeasurement (transactions in non-functional currency)
- Step 3 — Translation (functional currency ≠ reporting currency)
- Step 3b — Prove CTA independently (Mosofin addition)
- Step 4 — Intercompany and consolidation considerations
- Step 5 — Journal entries
- Step 6 — Controls
- Step 6b — Output (Mosofin addition)
- Step 7 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Never drop a task because no tool covers it.** Every exchange rate here is legitimately `[manual]`, and
saying so is the honest result.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding) — Mosofin addition

Pull the `[auto]` / `[gated]` reads **per entity**.

**Batch independent reads into one message** — each entity's trial balance, profile and intercompany
accounts are independent of every other entity's. **In a five-entity group this is the difference between
one round trip and fifteen.** Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, **per in-scope entity**:

- *`get_company_info`* — **legal name and home currency** — usually **[auto]**
- *`get_trial_balance`* at the period end, **in local currency** — the primary input — usually **[auto]**
- *`get_balance_sheet`* opening and closing — **for the net-asset movement CTA proof** — usually **[auto]**
- *`get_profit_and_loss`* for the period — translated at average rate — usually **[auto]**
- *`search_accounts`* — **account names and types, for monetary / nonmonetary classification** — usually
  **[auto]**
- *`get_general_ledger`* on **intercompany, equity and CTA accounts** — usually **[auto]**
- *`search_invoices`* / *`search_bills`* filtered to intercompany counterparties — the intercompany
  population — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`. **In this skill you will see
  this envelope often** — it means you omitted the entity on a call that needs one.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap, **naming the entity**.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag** **per entity**. `mock: true` on one subsidiary contaminates the group total, and
because CTA absorbs differences, **a fixture-based subsidiary produces a group balance sheet that balances
perfectly and means nothing.**

## Step 1 — Determine functional currency

**Assess** — **[manual]** judgment, `[auto]` evidence:

- **Primary economic environment**
- **Revenue and cost drivers**
- **Financing currency**
- **Cash retention and repatriation**

**Document the conclusion per entity.**

**Mosofin contribution — the evidence is largely readable.** **[auto]**:

- **Revenue and cost drivers**: read the P&L and the customer and vendor lists (*`get_profit_and_loss`*,
  *`search_customers`*, *`search_vendors`*). **An entity billing in euros to European customers and paying
  European suppliers has a euro functional currency**, whatever its file is set to.
- **Financing currency**: read the loan and intercompany accounts. **Funding denominated in the parent's
  currency is a pointer toward the parent's currency being functional.**
- **Cash retention**: read the bank accounts and their currencies. **Cash held locally and not repatriated
  points to local functional currency.**

**Then compare the conclusion against the file's home currency.** **Where they disagree, stop and raise
it** — that is a finding with consequences for every number that follows, and it is one of the most
valuable things this skill can surface.

## Step 2 — Remeasurement (transactions in non-functional currency)

**When an entity has transactions in a currency other than its own functional currency** — **[gated]**:

- **For monetary items** (cash, AR / AP, loans): **remeasure at period-end spot rate**
- **For nonmonetary items** (inventory at cost, PP&E): **use historical rates, as applicable**
- **Recognize remeasurement gains / losses in earnings**

**The monetary / nonmonetary split is the whole difficulty.** **[gated]**: account names and types are
`[auto]`, but classification is judgment. The rule of thumb: **monetary means a fixed number of currency
units — cash, receivables, payables, loans. Nonmonetary means an item whose value is not a fixed claim —
inventory, fixed assets, prepayments, deferred revenue.** Deferred revenue and prepayments catch people out
regularly: **they are nonmonetary**, because what is owed is goods or services, not money.

**Classify every account explicitly and store the classification** (Step 7). It does not change between
periods, and rebuilding it each time is where errors enter.

**Note the difference from Step 3, because the two are constantly confused:** **remeasurement** converts
transactions into the entity's *own* functional currency and **hits earnings**. **Translation** converts an
entity's whole statements into the *group's* reporting currency and **hits OCI**. Same arithmetic, opposite
destination.

## Step 3 — Translation (functional currency ≠ reporting currency)

**Translate the financial statements** — **[auto]** arithmetic on **[manual]** rates:

- **Assets / liabilities: closing (spot) rate**
- **Income statement: average rate** — unless better approximations are needed
- **Equity: historical rates**
- **CTA: plug to balance, recorded in OCI**

**The average rate is an approximation.** Where results are seasonal or rates moved sharply within the
period, a simple average misstates the translated result — **use a weighted average, or translate by month
and sum.** **[auto]** to detect the risk: read the P&L by month (*`get_profit_and_loss`* with a
summarize-by-month argument) and check whether earnings are evenly spread. **If they are not, say so
rather than defaulting to the annual average.**

## Step 3b — Prove CTA independently (Mosofin addition)

**Run this every period. It is the control that makes the rest meaningful.**

Because CTA is the plug, **it cannot fail — so prove it another way.** **[gated]**: the balances are
`[auto]`, the rates are `[manual]`.

Derive what CTA should be:

```
Expected CTA movement =
    Opening net assets × (closing rate − opening rate)
  + Net income for the period × (closing rate − average rate)
  − Dividends / capital movements × (closing rate − transaction-date rate)
```

Then:

```
Opening CTA
+ Expected CTA movement
= Expected closing CTA        →  compare to the plugged CTA
```

**A difference is a translation error**, and it will be one of a short list of causes: an account translated
at the wrong rate, an equity item translated at closing instead of historical, a rate applied in the wrong
direction, or an entity omitted. **Report the difference and investigate it — never absorb it.**

Also **[auto]**: **read the CTA balance already sitting in equity** (*`get_balance_sheet`*,
*`get_general_ledger`*) and roll it forward. **A CTA balance that has never moved despite years of rate
changes means translation is not actually happening** — the group is probably being consolidated at one
rate, or not translated at all.

## Step 4 — Intercompany and consolidation considerations

- **Ensure intercompany balances agree after translation** — **[gated]**
- **Consider settlement vs. long-term investment classification** — **[manual]**
- **Align translation methodology with `consolidation-and-eliminations`**

**The intercompany point deserves expansion, because it is guaranteed to arise.** **Two sides of an
intercompany balance that agree perfectly in local currency will not agree after translation**, because each
side is translated at a different rate. That difference is **not** an error to be forced away — it is a real
FX effect, and where it goes depends on the classification:

- **A balance expected to be settled** → the FX difference goes to **earnings**
- **A balance that is, in substance, part of the net investment** — a long-term intercompany loan with no
  planned settlement → the FX difference goes to **CTA / OCI**

**That designation is `[manual]` and it must be documented**, because it changes reported profit. Ask for it
explicitly; do not infer it from the account name.

**[auto]** contribution: **measure the intercompany mismatch in local currency first, before translating.**
A mismatch that exists *before* translation is a genuine reconciliation break — a missing invoice, a timing
difference — and it must be fixed first. **Translating an already-broken intercompany balance produces a
difference nobody can attribute.** Read both sides (*`search_invoices`*, *`search_bills`*,
*`get_general_ledger`*) and report the pre-translation mismatch separately from the translation effect.

## Step 5 — Journal entries

`DR` is a debit, `CR` a credit. **Mosofin does not post** — these are proposals:

**Remeasurement gain / loss:**
```
DR/CR FX Gain/Loss                   XXX
    CR/DR Monetary Asset/Liability       XXX
```

**CTA recording** — presentation depends on the system:

- **Translate accounts; record CTA in equity / OCI as the balancing amount**

Use the **real account names from each entity's connected chart of accounts** (*`search_accounts`*,
**[auto]**) — and note that **the FX gain/loss account and the CTA account are different things in different
statements.** An entity posting translation differences to the P&L FX account is making the error Step 2's
distinction exists to prevent.

## Step 6 — Controls

- **Rate source and approval** — **[manual]**. **The single most important control here.** Record the
  source, the rate type, the date and who approved it, for every rate used.
- **Completeness of entities and accounts** — **[auto]**: every connected entity appears; every account in
  each trial balance is classified and translated. **An unclassified account is one that silently defaulted
  to a rate.**
- **Consistent classification (monetary vs. nonmonetary)** — **[gated]**, and **consistency across periods
  matters as much as correctness**: reclassifying an account between periods moves gains between earnings
  and OCI. Store the classification (Step 7).
- **Tie-out translated TB to consolidation** — **[gated]**; the translated trial balance must be what
  `consolidation-and-eliminations` actually consumes.

**Mosofin addition to the controls:** **the CTA proof from Step 3b is itself a control**, and it should
appear in the control list with a named owner. It is the only one that detects a wrong-rate error.

## Step 6b — Output (Mosofin addition)

The original names deliverables but does not specify a workpaper. Produce one.

Deliver an `.xlsx` workpaper:

**Sheet 1: Entity and Currency Map** — each company file by `display_name`, its **home currency**, its
**concluded functional currency**, whether the two agree, and whether it requires translation. Plus the
header block: workspace name; excluded company files and why; the group reporting currency; whether any
entity's data is `mock`.

**Sheet 2: Functional Currency Memo** — the four assessment factors per entity, with the `[auto]` evidence
cited and the `[manual]` conclusion stated.

**Sheet 3: Rate Table** — every rate used: currency pair, rate type (spot / average / historical), value,
**date, source and approver**. **[manual]** in full.

**Sheet 4: Remeasurement Schedule** — monetary items by entity, rate applied, gain / loss to earnings.

**Sheet 5: Account Classification** — every account, monetary or nonmonetary, with the rate type applied
and a flag on anything unclassified.

**Sheet 6: Translation Worksheets** — per entity: local TB, rate applied per line, translated TB.

**Sheet 7: CTA Roll-Forward** — opening, movement, closing, **with the Step 3b derived figure alongside the
plug and the difference explained**.

**Sheet 8: Intercompany** — both sides per pair, **pre-translation mismatch shown separately from the
translation effect**, with the settlement / net-investment designation.

**Sheet 9: Journal Entries** — remeasurement and CTA entries, marked as **proposals**.

**Sheet 10: Disclosure Notes** — the figures the notes to the financial statements needs.

**Sheet 11: Coverage** — Mosofin-specific

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used / external source | As-at date | Policy | `mock` | Gap |

Every rate row reads `manual` with its source. That is the correct entry.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming (Mosofin addition — the original specifies none):**
`FX_Translation_[YYYY-MM]_[GroupOrEntityName].xlsx`

Every file states which datasources and `display_name`s it covers, and the reporting currency.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where the data does not
cover something — every rate, every historical rate, the functional currency conclusion — **name the source
required** instead of estimating.

## Step 7 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The functional currency conclusion per entity**, with the reasoning and the date concluded — **and
  whether it differs from the file's home currency**
- **The group reporting currency**
- **The monetary / nonmonetary classification per account** — **the most valuable stored asset here**, since
  it does not change between periods and rebuilding it is where errors enter
- **The rate *source* and rate-type policy**: which published source, which rate type per statement line,
  who approves. **Not the rates**
- **The average-rate method**: simple, weighted, or monthly translation
- **The intercompany designations**: which balances are settlement and which are net investment — **the
  decision that moves FX between earnings and OCI**
- **The entity map**: which company files form the group, and the ownership percentages
- **The equity historical-rate schedule basis** — how historical rates for equity items are determined
- The replay recipe: the exact sequence of per-entity reads that produced the trial balances and the CTA
  proof

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist exchange rates, translated balances or CTA amounts.** All of it is state, and a stale rate
reused silently is among the easier ways to produce a materially wrong set of group accounts.

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / Northbrook
Europe BV — home EUR, functional EUR, translates to USD, deferred revenue classified nonmonetary,
intercompany loan to parent designated net investment" — not "functional EUR". **Functional currency is
entity-specific by definition**, and an unlabelled classification applied to the wrong company file changes
which rate every account gets. Record the chosen **scenario** (which entities, which reporting currency) as
a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's** — and every rate, balance and CTA figure is state.

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped, never applied elsewhere. **Here that is a stop
condition**: a missing entity means the group translation is incomplete, and CTA will silently absorb its
absence.

---

## Both entity scenarios

**Single-entity.** Do not skip this skill because there is one company file. **Remeasurement applies
whenever the entity transacts in a currency other than its own** — a dollar-functional entity with a euro
supplier balance remeasures that balance every period, with the gain or loss in earnings. **Translation
applies if the entity's functional currency differs from the currency it reports in**, which happens with
foreign-owned subsidiaries filing locally.

**Multi-entity.** The normal case, and Steps 0–6b run **once per entity**, each call targeting exactly one
`data_source_id`, every balance carrying its entity's `display_name` and **its currency**. Then:

- **Never mix currencies in a single figure without labelling it.** Every number in every workpaper carries
  its currency. A column of "balances" spanning three entities in three currencies is the classic
  multi-entity error, and it is invisible once the numbers are side by side.
- **Translate each entity separately, then consolidate** — not the reverse. Consolidating in local
  currencies and translating the total is wrong whenever the entities have different functional currencies,
  and it produces a CTA that cannot be explained.
- **The order matters with `consolidation-and-eliminations`**: **translate first, then eliminate.**
  Eliminating intercompany balances before translation removes the very differences that reveal a wrong
  rate.
- **Ownership percentages affect CTA attribution.** For a partly owned subsidiary, **CTA is split between
  the group and the non-controlling interest** in the same proportion as net assets.
- **Sub-groups and chains.** Where a foreign subsidiary itself owns a foreign sub-subsidiary, **translation
  happens at each level**, and the intermediate functional currency matters. Do not translate straight from
  the bottom entity to the group currency without asking.
- **Each entity's capability is checked separately** at Gate 2 — and because CTA absorbs everything, **a
  subsidiary you could not read does not produce an obvious hole.** Say explicitly which entities were
  translated and which were not.
