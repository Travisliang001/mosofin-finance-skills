<!-- multicurrency-fx-revaluation · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding) — Mosofin addition
- Step 0b — Establish the currency tagging and the platform's own behaviour (Mosofin addition)
- Step 1 — Determine functional currency (foundational)
- Step 2 — Distinguish transaction FX from translation
- Step 3 — Transaction-level FX accounting
- Step 4 — Translation of foreign operations (functional ≠ presentation)
- Step 5 — Hyperinflationary economies
- Step 6 — Hedge accounting interaction
- Step 7 — Build the FX revaluation entries
- Step 8 — Disclosures
- Step 9 — Output
- Step 10 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Never drop a task because no tool covers it.** Every rate here is legitimately `[manual]`.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding) — Mosofin addition

**Batch independent reads into one message** — the balances, the accounts, the FX history and each entity's
profile are independent. **In a multi-entity group, batch every entity together.**

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`get_company_info`* — **home currency** — usually **[auto]**
- *`get_trial_balance`* / *`get_balance_sheet`* at period end — **the balance population** — usually
  **[auto]**
- *`search_accounts`* — **the chart with types, for monetary classification, plus the FX gain/loss and CTA
  accounts** — usually **[auto]**
- *`get_general_ledger`* on **the FX gain / loss and CTA accounts** — **what was actually posted** — usually
  **[auto]**
- *`search_invoices`* / *`search_bills`* / *`search_payments`* — **open versus settled balances, with
  currency where tagged: the realized / unrealized split** — usually **[auto]**
- *`get_profit_and_loss`* — the FX result recorded — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap, **naming the entity**.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag** **per entity**. `mock: true` means the revaluation is against fixture balances.

## Step 0b — Establish the currency tagging and the platform's own behaviour (Mosofin addition)

**Run before Step 1.** **[gated]**, two questions, both decisive:

1. **Are balances tagged by currency?** If yes, the revaluation population is `[auto]`. **If no, revaluation
   cannot be performed from the ledger** — the foreign balances are indistinguishable from domestic ones.
   **Report this and ask where the currency detail is held.**
2. **Does the platform revalue automatically?** **[auto]** to corroborate: **look for periodic FX entries in
   the FX gain / loss account with no manual journal behind them.** If the platform revalues, **a proposed
   manual revaluation would double-count** — the same class of error as proposing a closing entry to a
   platform that auto-closes, in `closing-entries-and-trial-balance`.

**Both answers go in the workpaper header.** Everything after depends on them.

## Step 1 — Determine functional currency (foundational)

**The functional currency is the currency of the primary economic environment in which an entity operates —
usually where it generates and spends cash.** **Factors** — **[manual]** to conclude, **[auto]** evidence:

- **Currency in which sales prices are denominated and settled** — **[auto]** where invoices carry currency
- **Currency in which costs are incurred** — **[auto]**, same
- **Currency of financing** — **[auto]** from loan balances
- **Currency in which receipts are retained** — **[auto]** from bank account currencies

**Functional currency is a determination, not a choice. It's typically stable; changes are prospective and
significant.**

**The functional currency drives whether and how a sub is translated, and the method used. Document the
determination per entity.**

**Mosofin check — home currency versus functional currency.** **[auto]** to read, **[manual]** to conclude.
**The platform's home currency is a setup choice; the functional currency is an accounting conclusion.**
**Where they disagree, raise it before any revaluation or translation** — it changes which method applies
and therefore where every difference lands. **The same check appears in
the foreign currency translation work**, and it matters equally in both.

## Step 2 — Distinguish transaction FX from translation

**Two distinct concepts:**

- **Transaction FX**: **an entity transacts in a currency other than its own functional currency** — e.g. a
  USD-functional entity sells in EUR. **Creates FX gains / losses in the income statement**, with one
  exception — see hedges
- **Translation**: **an entity's financial statements, already in its functional currency, are translated
  into a different presentation currency** for reporting, typically a foreign sub into the parent's
  currency. **The resulting difference goes to OCI (CTA), not P&L**

**Apply the right concept; mixing them is a common error.**

**[auto]** to determine which applies: **the entity's home currency against the transaction currencies it
uses** gives transaction FX; **the entity's functional currency against the group's presentation currency**
gives translation. **Both can apply to the same entity at once**, and they are computed separately and land
in different statements.

**A useful shorthand**: **transaction FX asks "what is this balance worth to me?"; translation asks "what is
this whole entity worth in the group's currency?" The first hits profit; the second does not.**

## Step 3 — Transaction-level FX accounting

For each foreign-currency transaction — **[gated]**, and this is the revaluation core:

- **Record at the spot rate on the transaction date** — **[auto]** where the platform did so
- **At period-end, remeasure monetary balances** — cash, receivables, payables, debt denominated in the
  foreign currency — **to the closing rate; FX gain / loss to P&L** — **[gated]**: **the population is
  `[auto]` where tagged; the closing rate is `[manual]`**
- **Non-monetary balances** — inventory, PP&E, prepaid, deferred revenue, equity — **carried at historical
  rates, generally not remeasured at period-end**. **An important distinction**
- **When the foreign-currency balance settles, recognize the realized FX gain / loss** — **[auto]** to
  identify settlements

`DR` is a debit, `CR` a credit. **Mosofin does not post** — this is a proposal:

```
Period-end remeasurement of monetary item:
DR  FX Loss (or AR/AP/Cash if gain)        $delta
    CR  AR/AP/Cash (or FX Gain if loss)        $delta
```

**Track realized vs. unrealized:**

- **Unrealized FX**: **from period-end remeasurement of open balances**
- **Realized FX**: **from actual settlement of balances at a different rate than recorded**

**Mosofin contribution — the split is readable.** **[auto]**: **invoices and bills settled during the period
produce realized FX; those still open at period end produce unrealized.** The ledger already distinguishes
settled from open, so **the split does not need to be tracked manually — it needs to be reported.**

**And report it separately in the P&L analysis**, because **the two behave differently**: unrealized FX
reverses when rates move back, realized FX does not. **An entity reporting a large FX loss should know how
much of it is real.**

## Step 4 — Translation of foreign operations (functional ≠ presentation)

**When a sub's functional currency differs from the group's presentation currency, translate per the
framework** — **[gated]**: balances `[auto]` per entity, **rates `[manual]`**:

**Current-rate method** — functional = local currency, **the common case**:

- **Assets and liabilities**: **closing (period-end) rate**
- **Income and expenses**: **average rate for the period**, approximating transaction-date rates
- **Equity**: **historical rates** — rate at date of each equity transaction; **opening equity at the
  opening rate**
- **Translation difference → Cumulative Translation Adjustment (CTA) in OCI**, **accumulated until disposal
  of the operation**

**Temporal / remeasurement method** — functional = parent's currency, but the sub's records are in another
currency, e.g. **a sub operating in a hyperinflationary economy** or whose functional currency is the
parent's:

- **Monetary items**: **closing rate**
- **Non-monetary items** — and related income / expense like **depreciation, COGS from inventory** —
  **historical rates**
- **Income and expenses**: **average for items at average; historical for items tied to non-monetary
  balances**
- **Translation difference → P&L (remeasurement gain / loss), not OCI**

**Determine functional currency first, then apply the right method.**

**Note the consequence of that last sentence**: **the same sub, under the two methods, puts its translation
difference in two different statements.** Getting the functional currency wrong does not produce a small
error — **it produces a difference in the wrong place entirely.**

**See the foreign currency translation work for the CTA proof** — **CTA is computed as a balancing figure,
so a wrong rate does not fail to balance; it lands in CTA and stays there.** Prove it independently.

## Step 5 — Hyperinflationary economies

**If a sub operates in a hyperinflationary economy (IAS 29 / ASC 830 special rules), additional restatement
applies before translation. Flag — specialized.** **[manual]**, entirely.

**Note the frameworks diverge here**: **IFRS restates for inflation and then translates at the closing
rate; US GAAP treats the functional currency as the reporting currency and remeasures instead**, sending
differences to earnings. See the foreign currency translation work, where this is set out in full.

## Step 6 — Hedge accounting interaction

**If FX hedges are in place — forwards, options, designated hedges — and qualify for hedge accounting** —
**[manual]** throughout:

- **The hedge's effective portion may be deferred to OCI (cash flow hedges) or offset the hedged item's FX
  (fair value hedges)** per the framework's hedge accounting rules
- **Without hedge accounting, derivatives are at fair value through P&L**

**Hedge accounting is complex — flag for the entity's hedge designation / documentation, and don't apply
hedge accounting without it.**

**That last clause is a hard rule**: **hedge accounting requires contemporaneous designation and
documentation**, and **it cannot be applied retrospectively.** **There is no hedge documentation on this
surface**. **[auto]** contribution is limited to noting that
derivative balances exist.

## Step 7 — Build the FX revaluation entries

**Period-end** — **[gated]**:

```
For each foreign-currency monetary balance:
  Balance × closing rate − balance at carrying-recorded rate = FX impact
  Recognize in P&L (transaction context)
```

**For translation:**

```
Sub's translated balances per the method
  vs. opening translated balances + period activity at appropriate rates
  Residual = CTA in OCI
```

**Mosofin comparison — what was proposed against what was posted.** **[auto]**: **read the FX gain / loss
account and the CTA account for the period.** Three outcomes:

- **The platform already revalued** — per Step 0b. **Do not propose a duplicate entry**; instead **compare
  the platform's result to yours** and explain any difference, which is usually the rate used.
- **Nothing was posted** — the revaluation has not run. **The proposal stands.**
- **Something was posted that does not match** — **the rate, the population or the classification differs.**
  **The most useful finding here**, and the reason to run the comparison at all.

## Step 8 — Disclosures

For the notes to the financial statements — **[gated]**:

- **Functional and presentation currencies** — **[gated]**: home currency `[auto]`, determination `[manual]`
- **FX gain / loss recognized in P&L** — **[auto]**, **and worth splitting realized from unrealized**
- **CTA / accumulated OCI from translation, with movements** — **[auto]** for the balance and movement
- **Rates used (if material)** — **[manual]**
- **Hedge accounting (if applicable)** — **[manual]**

## Step 9 — Output

Deliver an `.xlsx` workpaper:

**Sheet 1: Functional Currency Determinations** — **per entity, with rationale.** Add **the home currency
alongside**, and **flag any disagreement**. Plus the header block: workspace name; entities by
`display_name` with their currencies; the presentation currency; **whether balances are currency-tagged**;
**whether the platform revalues automatically**; whether any entity's data is `mock`.

**Sheet 2: Transaction FX** — **foreign-currency balances by currency; period-end remeasurement;
realized / unrealized split.** **The split is `[auto]`** from settled versus open.

**Sheet 3: Translation Workpaper** — **per foreign sub: local TB, rates applied (asset / liability /
equity / IS), translated balances, CTA computation.**

**Sheet 4: CTA / Accumulated OCI Roll-Forward** — **opening + period movement = closing**, **tied to the CTA
account in the ledger**.

**Sheet 5: Journal Entries** — revaluation and translation entries, marked as **proposals**, **and only
where the platform has not already posted them**.

**Sheet 6: Hedge Accounting** (if applicable) — hedge documentation and effects.

**Sheet 7: Disclosure Data** — for the notes.

**Sheet 8: Posted vs. Proposed — NEW, Mosofin-specific** — what the ledger already contains against what
this workpaper computes, with differences explained.

**Sheet 9: Coverage — NEW, Mosofin-specific**

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used / external source | As-at date | `mock` | Gap |

**Every rate row reads `manual` with its source.** That is the correct entry.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming:** `FX_Revaluation_[YYYY-MM]_[EntityName].xlsx`

Every file states which datasource and `display_name` it covers, and the currencies involved.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where the data does not
cover something — every rate, the hedge documentation, the functional determination — **name the source
required** instead of estimating.

## Step 10 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The functional currency determination per entity**, with its reasoning and date, **and whether it
  differs from the platform's home currency**
- **The presentation currency**
- **The monetary / non-monetary classification per account** — **the most valuable stored asset here**,
  because it does not change between periods and rebuilding it is where errors enter. **Note deferred
  revenue and prepayments as non-monetary explicitly**
- **The translation method** per entity — current-rate or temporal — and why
- **The FX rate *source* and rate-type policy** — which published source, which rate for which line, who
  approves. **Not the rates**
- **The average-rate method** — simple, weighted, or monthly
- **Whether the platform revalues automatically**, and which accounts it touches
- **The account map**: FX gain / loss, CTA, and the foreign-currency balance accounts
- **The hedge designations in force**, by reference
- **The CTA by operation**, so the release on disposal can be identified — **the tracking basis, not the
  amounts**
- The replay recipe: the exact sequence of per-entity reads

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist exchange rates, balances, FX amounts or CTA figures.** All state — **and a stale rate reused
silently misstates every foreign balance on the sheet.**

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / Northbrook
Europe BV — home EUR, functional EUR, presentation USD, current-rate method, deferred revenue classified
non-monetary, platform revalues AR and AP automatically" — not "functional EUR, current-rate". **Functional
currency and classification are entity-specific by definition**, and applying one entity's method to another
sends differences to the wrong statement. Record the chosen **scenario** as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's.**

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** **Transaction FX and revaluation apply wherever the entity deals in a currency other
than its own.** Translation applies only if it reports in a currency other than its functional one. **Do not
skip this skill because there is one company file** — a single entity with foreign customers or suppliers
has FX every period.

**Multi-entity.** Steps 0–9 run **once per entity**, each call targeting exactly one `data_source_id`, every
balance carrying its entity's `display_name` **and its currency**. Then:

- **Read every entity in one batch.** Independent reads, and **the same instant matters**.
- **Never mix currencies in a column without labelling them.** The classic multi-entity error, and
  invisible once numbers sit side by side.
- **Translate each entity separately, then consolidate** — not the reverse.
- **Intercompany monetary balances are remeasured at entity level**, and **the FX may eliminate on
  consolidation while a CTA-like effect remains in OCI for balances that are long-term-investment in
  nature.** See the edge cases and `intercompany-reconciliation`.
- **Two sides of an intercompany balance will not agree after translation**, because each translates at its
  own rate. **That difference is real, not an error** — carry it, do not force it away.
- **Track CTA per operation**, so the release on disposal is identifiable. **A single group CTA balance
  cannot be released selectively.**
- **Each entity's capability is checked separately** at Gate 2, and **an entity whose balances are not
  currency-tagged cannot be revalued from the ledger** even if its siblings can.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict per company
file.
