<!-- business-combinations-asc805 · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding)
- Step 1 — Determine the acquirer and acquisition date
- Step 2 — Confirm it's a business combination (not asset acquisition)
- Step 3 — Measure consideration transferred
- Step 4 — Identify and measure assets acquired and liabilities assumed at fair value
- Step 5 — Compute goodwill (or bargain purchase)
- Step 6 — Build the acquisition entry
- Step 7 — Measurement period
- Step 8 — Subsequent accounting
- Step 9 — Disclosures
- Step 10 — Output
- Step 11 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with
plain-language wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool
added.

**Never drop a task because no tool covers it.** In this skill most tasks are `[manual]` by the
nature of the domain — valuation is specialist work — and recording them as structured open items
with named owners *is* the deliverable.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding)

Pull the `[auto]` / `[gated]` reads. **Batch independent reads into one message** — the acquiree's
balance sheet, the acquirer's ledger, and the post-acquisition results do not depend on each other.
Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries — and here
that matters more than usual, because you are deliberately reading **two different company files**
and passing the wrong id silently reads the wrong entity.

Typical opening batch:

**From the acquiree (where connected)** — pass the acquiree's `data_source_id`:

- *`get_balance_sheet`* / *`get_trial_balance`* **as at the acquisition date** — the
  pre-acquisition book values — usually **[auto]**
- *`get_profit_and_loss`* **from the acquisition date onward** — the post-acquisition results
  required for disclosure — usually **[auto]**
- *`get_profit_and_loss`* for the **comparable prior period** — the pro-forma input — usually
  **[auto]**
- *`search_accounts`* — the acquiree's chart of accounts, for mapping to the acquirer's — usually
  **[auto]**
- *`get_general_ledger`* — detail behind any acquired balance — usually **[auto]**
- *`get_company_info`* — legal name, currency, year-end — usually **[auto]**

**From the acquirer** — pass the acquirer's `data_source_id`:

- *`search_bills`* / *`get_vendor_expenses`* / *`search_purchases`* — **deal-related legal,
  advisory and due-diligence costs**, to test they were expensed — usually **[auto]**
- *`search_accounts`* / *`get_balance_sheet`* — where goodwill and acquired intangibles sit —
  usually **[auto]**
- *`search_journal_entries`* — any acquisition entry already posted — usually **[auto]**
- *`get_company_info`* — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — it cannot support an acquisition entry, a
goodwill figure, or a disclosure. A purchase price allocation is audited and lives on the balance
sheet for years.

## Step 1 — Determine the acquirer and acquisition date

- **Acquirer**: the entity **obtaining control** of the other. Usually the legal acquirer, but
  **reverse acquisitions** (where the legal acquirer is the accounting acquiree) occur — **assess
  control transfer**, not legal form. **[manual]**.
- **Acquisition date**: the date the acquirer **obtains control** — typically the closing date.
  **This is the measurement date for everything.** **[manual]** to establish; once established,
  **[auto]** to use consistently as the boundary in every read.

Say the acquisition date once, prominently, and use exactly that date in every subsequent query.
An allocation measured on a date a few days out is wrong in every line.

## Step 2 — Confirm it's a business combination (not asset acquisition)

This screen changes the accounting entirely, so it comes before anything else is measured.

A **"business"** requires **inputs** and **substantive processes** that together significantly
contribute to the ability to create **outputs**. The screen under both ASC 805 (post-ASU 2017-01)
and IFRS 3 (post-2018 amendments) helps — **[manual]**:

- **If substantially all the fair value is concentrated in a single asset (or group of similar
  assets) → likely an asset acquisition** — different accounting: **no goodwill, transaction costs
  capitalized**
- **Otherwise, evaluate the substantive process criterion → likely a business combination**

**Apply the screen and document it.** This skill covers business combinations; asset acquisitions
follow different rules.

Note the inversion that makes misclassification so consequential: in a business combination
transaction costs are **expensed**; in an asset acquisition they are **capitalized**. The same
invoice is treated in opposite ways depending on this answer.

## Step 3 — Measure consideration transferred

Work out what was really paid — which is not the same as the headline price.

Total consideration at **fair value at the acquisition date**:

- **Cash**: at amount — **[gated]**; the payment may be visible in the acquirer's ledger
  (*`search_purchases`*, *`get_general_ledger`*), the deal terms are **[manual]**
- **Equity issued by the acquirer**: at fair value at the acquisition date (share price × shares) —
  **[manual]**
- **Replacement awards** (the acquirer's awards replacing the acquiree's): the portion attributable
  to **pre-combination service is consideration**; the **post-combination portion is compensation
  expense** (`equity-compensation-accounting`) — **[manual]**
- **Contingent consideration** (**earnouts** — extra payments if the acquired business hits
  targets): at fair value at the acquisition date. Treated as a **liability** (if cash) or
  **equity** (if shares meeting the equity criteria); subsequently remeasured (liability) **through
  P&L, not goodwill**, after acquisition. US GAAP and IFRS rules align in principle — **[manual]**
- **Assumed debt and obligations**: at fair value — **[gated]**; the acquiree's carrying amounts are
  **[auto]** where connected, fair value is **[manual]**
- For a **step acquisition**, the **previously-held equity interest is remeasured to fair value at
  the acquisition date, with a gain / loss recognized in P&L** — **[manual]**

**Transaction costs (legal, advisory, due diligence) are expensed as incurred under both
frameworks (NOT capitalized into the acquisition — a key contrast with asset acquisitions).**

**[auto]** and worth running every time: identify deal-related professional fees in the acquirer's
ledger around the acquisition date (*`search_bills`*, *`get_vendor_expenses`*, *`search_accounts`*)
and **check where they were posted**. Capitalising them into goodwill or into the investment is a
common, material error, and it is directly detectable. Report the total identified, the accounts
they landed in, and any that appear capitalized.

## Step 4 — Identify and measure assets acquired and liabilities assumed at fair value

At the acquisition date, recognize the **identifiable** assets and liabilities at **fair value**.
The acquiree's own book values are the *starting point*, not the answer.

**Tangible assets**: inventory at fair value (often a **step-up** from book — inventory carried at
cost is revalued toward selling price, which then flows through cost of sales as it is sold and
depresses margin for a period); PP&E at fair value; etc. **[gated]**: book values **[auto]** where
the acquiree is connected, fair values **[manual]**.

**Identifiable intangibles** — must be identified separately from goodwill if they meet the
**contractual-legal** or **separability** criterion (it arises from a contract or legal right, or it
could be sold on its own). Common categories — **[manual]**, every one:

- **Customer relationships** (typically separable)
- **Technology / patents**
- **Trade names / brands**
- **In-process R&D (IPR&D)** — capitalized as an **indefinite-lived intangible** until completion
  or abandonment
- **Order backlog**
- **Licenses, franchises**
- **Non-compete agreements**

Each identified intangible needs a fair value — typically from a valuation specialist using
**income, market, or cost approaches**. **Flag for valuation-specialist involvement; this skill does
not fabricate fair values.**

**[auto]** contribution: the acquiree's own records can *evidence the existence* of several of
these — a customer list and its revenue history (*`search_customers`*, *`get_customer_sales`*), an
order backlog (*`search_estimates`*, *`search_purchase_orders`*), licences held. That supports the
**identification** step and gives the valuer their inputs. It does **not** value them.

**Liabilities assumed**: at fair value. Includes **contingent liabilities** meeting recognition
criteria (probable + estimable under US GAAP; IFRS uses present obligation + reliable estimate) —
**[manual]**.

**Deferred taxes**: recognize deferred tax on the differences between assigned fair values and tax
bases of acquired assets and liabilities (`corporate-tax-provision-asc740`) — **[manual]**. Note
that the fair-value step-ups themselves create these differences, so this cannot be done until
Step 4's valuations are final.

**Assembled workforce**: **NOT recognized separately — it's part of goodwill.** A trained team has
real value and is specifically excluded from separate recognition; do not let a valuer's schedule
smuggle it in as an intangible.

## Step 5 — Compute goodwill (or bargain purchase)

```
Consideration transferred (Step 3)
+ Fair value of any non-controlling interest at acquisition date
+ Fair value of any previously-held equity interest in the acquiree
− Fair value of identifiable net assets acquired (Step 4)
= Goodwill
```

**[auto]** arithmetic on **[manual]** inputs. Show every component with its source.

**If the result is negative (rare): a bargain purchase. Reassess all measurements first — bargain
purchases are unusual and warrant double-checking. If still negative, recognize a gain in P&L
immediately.** A negative result is far more often a missed liability or an overstated asset value
than a genuine bargain.

**Non-controlling interest measurement** (when acquiring less than 100%) — **[manual]**:

- **US GAAP: NCI at fair value** (full-goodwill method)
- **IFRS 3: choice per transaction** — fair value (full goodwill) or proportionate share of net
  assets (partial goodwill)

**This affects the goodwill amount and subsequent impairment testing**
(`goodwill-and-impairment-testing`). Record which choice was made and why — the choice is per
transaction, so it must be documented at the time.

## Step 6 — Build the acquisition entry

Conceptually — **Mosofin proposes; a human posts**:

```
DR  Identifiable assets acquired (at fair value)
DR  Goodwill
    CR  Identifiable liabilities assumed (at fair value)
    CR  Non-controlling interest (at chosen measurement)
    CR  Consideration transferred (cash, equity, contingent at fair value)
    +/- (Gain on bargain purchase, or gain/loss on previously-held interest remeasurement)
```

**In consolidation, the acquired entity's individual identified assets and liabilities (at fair
value) replace its pre-acquisition book values in the consolidated balance sheet, and goodwill is
recognized.**

Use the **acquirer's real account names** (*`search_accounts`* against the acquirer's
`data_source_id`, **[auto]**), and where the acquiree is connected, show the **mapping from its
chart of accounts to the acquirer's** — an acquisition almost always requires one, and doing it
explicitly now prevents months of misposted transactions afterwards.

## Step 7 — Measurement period

The acquirer has a **measurement period** of **up to one year** from the acquisition date to
finalize **provisional** fair values as new information about facts **existing at the acquisition
date** becomes available. During this period:

- **Adjust provisional amounts retrospectively**
- **Adjust goodwill correspondingly**
- **Disclose the nature of measurement-period adjustments**

**After one year: any adjustments to acquisition accounting are accounted for as errors**
(`restatement-and-prior-period-adjustment`) **or as normal subsequent activity, not
measurement-period adjustments.**

The distinction that governs everything here: an adjustment qualifies only if it reflects facts
that **existed at the acquisition date** and were merely unknown. A genuinely new event after that
date is not a measurement-period adjustment, however soon it happens.

**[auto]** contribution: track the one-year clock from the confirmed acquisition date, and flag
each reporting date remaining. **[manual]** for every adjustment itself.

## Step 8 — Subsequent accounting

After acquisition:

- **Identifiable intangibles**: amortize over useful lives (or test for impairment if
  indefinite-lived) — `intangibles-and-amortization`. **[gated]**: the amortisation posted is
  **[auto]**, the lives are **[manual]**
- **Goodwill**: **not amortized**; tested for impairment at least annually and on triggering events
  — `goodwill-and-impairment-testing`. **[auto]** to read the carrying balance
- **Contingent consideration (liability)**: **remeasure to fair value at each reporting date;
  changes through P&L** — **[manual]** for the remeasurement; **[auto]** to flag that a reporting
  date has arrived and a remeasurement is due
- **Contingent consideration (equity)**: **not remeasured**
- **Acquired NOLs / DTAs**: any recognized at acquisition; subsequent changes (including
  **valuation allowance** changes) generally affect the **post-acquisition P&L, not goodwill** —
  **[manual]**

## Step 9 — Disclosures

Required disclosures (for `notes-to-financial-statements`):

- **Name and description of the acquiree, acquisition date, percentage acquired** — **[gated]**;
  the legal name and currency are **[auto]** from the acquiree's profile
- **Primary reasons for the acquisition** — **[manual]**
- **Consideration transferred by class** — **[manual]**
- **Recognized amounts of each major class of assets acquired and liabilities assumed** —
  **[gated]**; the classes and book values are **[auto]** where connected, the fair values
  **[manual]**
- **Goodwill (and a qualitative description of factors), or bargain purchase gain** — **[manual]**
- **The acquiree's revenue and earnings since the acquisition date** — **[auto]** where the
  acquiree is connected: pull its P&L from the acquisition date to the reporting date. This is one
  of the more tedious disclosures to assemble by hand and one of the easiest here
- **Pro forma revenue and earnings as if the acquisition had occurred at the start of the
  comparable prior period** (public entities) — **[gated]**: the acquiree's actual prior-period
  results are **[auto]** where connected, but the pro-forma **adjustments** (extra amortisation on
  the stepped-up intangibles, financing costs, removal of transaction costs) are **[manual]**. Say
  which half is which — a pro forma that is simply two P&Ls added together is not a pro forma
- **Measurement-period adjustments** — **[manual]**

## Step 10 — Output

Deliver an `.xlsx` workpaper.

**Sheet 1: Deal Summary & Acquirer/Date Determination** — parties, dates, structure, the screen for
business vs. asset acquisition. Add: workspace name; **which `display_name` is acquirer and which is
acquiree**; each excluded company file and why; whether any figure rests on `mock` data.

**Sheet 2: Consideration Transferred** — by class, at fair value at the acquisition date.

**Sheet 3: Acquired Net Assets at Fair Value**

| Item | Pre-Acquisition Book Value | Fair Value | Source / Valuation |

The **Source / Valuation** column is where this skill's discipline lives: every fair value names its
valuer and report date, and **any line where fair value equals book value says whether that was a
conclusion or a default**.

**Sheet 4: Identifiable Intangibles** — each intangible identified, fair value, life, source.

**Sheet 5: Goodwill Computation** — the Step 5 build, including NCI and step-acquisition components.

**Sheet 6: Acquisition Journal Entry** — the full consolidation entry, marked as a **proposal**,
with the chart-of-accounts mapping where the acquiree is connected.

**Sheet 7: Contingent Consideration** — fair value at acquisition; classification (liability vs.
equity); subsequent remeasurement plan with the dates it falls due.

**Sheet 8: Measurement Period Tracker** — provisional amounts and adjustments through the one-year
period, **with the end date of the measurement period stated**.

**Sheet 9: Disclosures** — disclosure-ready data, marking which items are `[auto]` from the
acquiree's ledger and which are supplied.

**Sheet 10: Open Items / Valuation Specialist** — items awaiting specialist valuations or
refinement, each with an owner and a target date.

**Sheet 11: Coverage — NEW, Mosofin-specific**

| Task | Entity (`display_name`) and role | Verdict (auto / gated / manual) | Tool used | Policy (enabled / permission / disabled) | `mock` | Gap — what could not be evidenced and who owns it |

Every fair-value row reads `manual` with the gap "valuation specialist required". That is the
correct, expected entry — not a defect.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming:** `Business_Combination_[AcquireeName]_[YYYY-MM-DD].xlsx`

Use the acquiree's `display_name` where it is a connected company file. Every file states which
datasources and which `display_name`s it covers, and in which role.

**Grounding:** every figure traces to a tool result in this conversation or to labelled
user-supplied evidence. End with a single **Data sources** line grouping calls by datasource. Where
the data does not cover something — which for every fair value it will not — **name the specialist
required** instead of estimating.

## Step 11 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them,
ask — explicitly, at that point, not earlier — whether to save this as their own customized version.
A general "yes, go ahead" from earlier does not count.

This skill recurs through the measurement period and at every subsequent reporting date, so
persisting the deal's structure matters.

On an explicit yes, persist the **decisions**:

- **The deal's fixed facts**: acquisition date, acquirer and acquiree by `display_name` and role,
  percentage acquired, framework, and the **NCI measurement choice with its rationale**
- **The business-versus-asset screen conclusion** and its reasoning
- **The chart-of-accounts mapping** between acquiree and acquirer — used every month afterwards
- **The intangible register**: each intangible identified, its life, its amortisation method, and
  its valuer
- **The contingent consideration terms**, its classification, and **the dates remeasurement falls
  due**
- **The measurement period end date**, so the one-year boundary is not missed
- The valuation specialists engaged and what each covered
- The replay recipe: the exact sequence of reads that produced the acquiree's book values and
  post-acquisition results

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files;
set `datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference
files alongside the installed skill.

**Do not persist the consideration amounts, fair values, goodwill figure, or any valuation report
contents.** Deal terms are commercially sensitive and often subject to confidentiality
undertakings; the figures belong in the acquisition file. Persist the *structure, the dates and the
decisions*.

**Key every preference and asset by datasource + entity `display_name` and role.** Write
"quickbooks / Northbrook Trading (acquirer) ← quickbooks / Harbour Supplies (acquiree), acquired
2026-03-31, IFRS 3, NCI at proportionate share" — not "acquired 2026-03-31". A group making several
acquisitions will otherwise apply one deal's structure to another. Record the chosen **scenario**
as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run — and after an acquisition the connected set
changes, often more than once. **Decisions are the user's; state is the workspace's.**

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that
is no longer connected is **flagged** — never silently dropped, never applied elsewhere. For an
acquiree this is a live possibility: its file may be merged into the acquirer's during integration,
and the disclosure of post-acquisition results then becomes `[manual]`.

---

## Both entity scenarios

This skill is **inherently two-entity**. The scenarios below describe how much of it the workspace
can evidence.

**Acquirer only connected.** The acquiree's balance sheet, results and history are **[manual]**.
The skill still structures the whole allocation, tests transaction-cost treatment in the acquirer's
ledger, and tracks the measurement period — but the entire left-hand column of Sheet 3 must be
supplied.

**Both connected.** The acquiree's pre-acquisition book values, post-acquisition results and
prior-period comparatives are **[auto]**. Additionally:

- **Read the acquiree strictly as at the acquisition date** for book values, and strictly **from**
  it for results. Mixing the two is the commonest error, and it double-counts a period.
- **Watch for the acquiree's books continuing to be kept separately** after the deal. That is
  normal during integration and is what makes the disclosure of post-acquisition revenue and
  earnings easy — but it also means the acquirer's own ledger does **not** contain those results
  until consolidation. Do not report group figures from the acquirer's file alone.
- **Intercompany transactions begin immediately** after the acquisition date and must be eliminated
  on consolidation — see `consolidation-and-eliminations` and `intercompany-reconciliation`. They
  do not affect the acquisition entry itself, which is measured on one date.
- **Capability is checked per entity**: a newly connected acquiree often has narrower permissions,
  so a task `[auto]` for the acquirer may be `[manual]` for the acquiree. The coverage sheet shows
  this per file and per role.
