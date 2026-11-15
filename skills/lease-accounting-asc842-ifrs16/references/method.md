<!-- lease-accounting-asc842-ifrs16 · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding) — Mosofin addition
- Step 0b — Search for unrecognised leases (Mosofin addition)
- Step 1 — Confirm there's a lease and the perspective
- Step 2 — Determine the lease term and payments
- Step 3 — Determine the discount rate
- Step 4 — Classify the lease (ASC 842 lessee)
- Step 5 — Initial measurement
- Step 6 — Build the amortization schedules
- Step 7 — Periodic entries
- Step 8 — Reassessments and modifications
- Step 9 — Practical expedients and exemptions
- Step 10 — Disclosures
- Step 11 — Output
- Step 12 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Never drop a task because no tool covers it.** The agreements, the rates and the judgments are legitimately
`[manual]`.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding) — Mosofin addition

**Batch independent reads into one message** — the accounts, the balances, the expense history and the
payment population do not depend on each other. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`search_accounts`* — **ROU asset, lease liability (current and non-current), accumulated amortization,
  lease and rent expense, interest expense** — usually **[auto]**
- *`get_balance_sheet`* / *`get_trial_balance`* — **ROU and liability balances**, opening and closing —
  usually **[auto]**
- *`get_profit_and_loss`* **by month** — **lease expense, rent, interest and amortization, and whether the
  operating expense is level** — usually **[auto]**
- *`get_general_ledger`* on the **ROU, liability and lease expense accounts** — movements — usually
  **[auto]**
- *`search_bills`* / *`search_payments`* **by vendor over 24+ months** — **the recurring-payment pattern
  that finds unrecognised leases**, and **cash paid for leases** — usually **[auto]**
- *`search_vendors`* — lessor identification — usually **[auto]**
- *`get_company_info`* — legal name, currency, year-end — usually **[auto]**

**Pull a long payment history deliberately.** **The recurring-payment signature needs many periods to be
visible**; twelve months of equal monthly amounts is a pattern, three months is a coincidence.

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — **lease liabilities are debt for covenant and
leverage purposes**, and a fixture-derived balance flows into both.

## Step 0b — Search for unrecognised leases (Mosofin addition)

**Run before Step 1.** **[auto]**, and **for many entities this is the most valuable output of the whole
skill.**

**Test 1 — expense without an asset.** Compare **rent and lease expense** to **ROU asset and lease liability
balances**. **Material lease expense with no ROU asset means leases that were never recognised** — or that
every lease qualifies for a short-term or low-value exemption, which is possible and worth confirming
rather than assuming.

**Test 2 — the recurring payment signature.** By vendor, over 24+ months, look for:

- **Equal or escalating payments at regular intervals**
- **A consistent counterparty over a long period**
- **Descriptions suggesting rent, hire, lease, rental or equipment**

**Report candidates with the vendor, the payment pattern, the annual value and the period covered.**
**Never conclude a lease exists** — the pattern also fits subscriptions, insurance instalments, service
retainers and loan repayments. **The contract decides**, which is Step 1's job.

**Test 3 — the short-term population.** Where the short-term expedient is elected, **payments to lessors
should be expensed and disclosed as short-term lease expense.** A vendor whose payments have continued for
years under a "short-term" election is worth questioning — **short-term is about the lease term, not about
how the entity chose to treat it.**

**Report all three as a completeness section**, before any measurement. **A perfectly built schedule for
three leases is worth little if there are eleven.**

## Step 1 — Confirm there's a lease and the perspective

**A lease conveys the right to control the use of an identified asset for a period in exchange for
consideration.** Confirm — **[manual]**:

- **An identified asset exists and the customer controls its use** — versus a service contract
- **Whether the entity is the lessee** (most common) **or lessor**
- **Separate lease and non-lease components** — e.g. maintenance — **per the framework or expedient**

**[gated]** support: **where an invoice separates rent from service charges, the components are visible** —
common on property leases, where insurance, service charge and rates are billed alongside rent. **That split
is exactly what Step 1 asks for**, and it is often already in the data.

## Step 2 — Determine the lease term and payments

- **Lease term**: **non-cancellable period + option periods reasonably certain to be exercised** (renewals)
  **or not exercised** (terminations). **The "reasonably certain" judgment drives the term** — **[manual]**,
  and it is the largest single judgment in the skill

- **Lease payments to include**: **fixed payments, in-substance fixed, variable payments based on an index
  or rate** (at the initial index or rate), **residual value guarantees** (expected), **purchase option
  price** (if reasonably certain), **termination penalties** (if the term reflects termination). **Exclude
  variable payments based on usage or sales** — expense as incurred

**[gated]**: **the historical payment amounts are `[auto]`**, which supports the fixed-payment figure and
**shows escalation history** — but **the contract defines what is fixed, what is index-linked and what is
variable**, and the ledger cannot distinguish them. **A payment that rose 3% every year looks like an
escalation clause and might be a renegotiation.**

## Step 3 — Determine the discount rate

- **The rate implicit in the lease** if readily determinable; **otherwise the lessee's incremental borrowing
  rate** — the rate to borrow, **over a similar term, with similar security, for a similar amount**
- **The rate is an input — use the entity's determined rate; don't fabricate. It materially affects the
  liability**

**[manual]**, always. **Ask for the rate, its basis and its date.** **[auto]** context only: **the entity's
actual borrowing costs are readable** from interest expense and loan balances, which is *relevant context*
for an IBR determination — **it is not the IBR**, which must reflect the lease's term and security.

## Step 4 — Classify the lease (ASC 842 lessee)

**Under ASC 842, classify as finance or operating** — **[manual]**:

- **Finance if any of**: **ownership transfers**; **a purchase option reasonably certain to be exercised**;
  **lease term is a major part of the asset's economic life**; **PV of payments is substantially all of fair
  value**; **the asset is so specialized it has no alternative use**
- **Otherwise operating**

**Under IFRS 16, lessees do not classify** — **nearly all leases use a single finance-like model** (ROU
asset + liability, with depreciation + interest). **Lessors still classify under both frameworks.**

**[auto]** contradiction check: **an operating / finance split asserted under IFRS 16** is a framework error.
Raise it before measuring.

## Step 5 — Initial measurement

**Lease liability = present value of remaining lease payments discounted at the rate.**

**ROU asset = lease liability + initial direct costs + prepayments − lease incentives received**
(+ estimated dismantling / restoration costs where applicable).

`DR` is a debit, `CR` a credit. **Mosofin does not post** — this is a proposal:

```
DR  Right-of-Use Asset            $ROU
    CR  Lease Liability               $PV of payments
    (+/- initial direct costs, incentives, prepayments)
```

**[gated]**: the arithmetic is `[auto]` once the term, payments and rate exist — **all three `[manual]`.**
**[auto]** support: **initial direct costs and incentives are sometimes findable** as postings around the
lease commencement date.

## Step 6 — Build the amortization schedules

**Lease liability schedule** — effective-interest method, both frameworks — **[auto]** arithmetic:
```
Opening liability
+ Interest (opening liability × periodic rate)
− Payment
= Closing liability
```

**ROU asset amortization — depends on classification and framework:**

- **Finance lease (ASC 842) / IFRS 16 (all)**: **ROU asset depreciated**, usually straight-line over the
  **shorter of lease term or useful life**. **Expense = depreciation + interest — front-loaded total
  expense**
- **Operating lease (ASC 842)**: **single straight-line lease expense.** **The ROU asset amortization is the
  *plug* = straight-line lease expense − interest on the liability**, so total expense is level. **This is
  the distinctive ASC 842 operating mechanic**

**Build period-by-period schedules.**

**Mosofin verification — the plug actually works.** **[auto]**: **read the monthly lease expense from the
P&L.** For an operating lease under ASC 842, **it should be level.** **If it is front-loaded, the ROU asset
is being amortized straight-line independently rather than as the balancing figure** — precisely the
mechanical error the edge cases name, and now detectable rather than merely warned about.

**And the schedule must tie:** closing liability and closing ROU to the balance sheet; period interest and
amortization to the P&L. **Report each with its difference, including zero.**

## Step 7 — Periodic entries

**Finance / IFRS 16**:
```
DR  Interest Expense
DR  Amortization Expense (ROU)
    CR  Lease Liability (interest portion accretion handled in schedule)
    CR  Accumulated Amortization (ROU)
DR  Lease Liability / CR Cash for the payment
```

**Operating (ASC 842)**:
```
DR  Lease Expense (straight-line)
    CR  Lease Liability (for interest accretion)
    CR  ROU Asset (amortization plug)
    (payment reduces liability)
```

Use the **real account names from the connected chart** (*`search_accounts`*, **[auto]**), and note that
**the two patterns hit different expense lines** — an entity switching classification without switching
accounts produces a P&L that no longer means what its labels say.

## Step 8 — Reassessments and modifications

- **Reassessment** — change in term or option likelihood, index or rate change affecting payments:
  **remeasure the liability using a revised rate where required, adjust the ROU asset** — **[manual]**
  trigger, **[auto]** arithmetic
- **Modification** — change to scope or consideration: **determine if it's a separate new lease or a
  modification of the existing one; remeasure accordingly. Modifications are intricate — apply the
  framework's modification rules carefully** — **[manual]**

**[auto]** prompt: **a change in the recurring payment amount** to a known lessor **is a signal that
something happened** — an escalation, a reassessment trigger, or a modification. **The ledger shows the
change; the contract explains it.** Worth surfacing, since unremeasured modifications are a common gap.

## Step 9 — Practical expedients and exemptions

- **Short-term leases** — ≤ 12 months, no purchase option: **may elect not to capitalize — expense
  straight-line** — **[manual]**
- **Low-value assets (IFRS 16)**: **may elect to expense** — **[manual]**
- **Apply elected expedients consistently**

**[auto]** consistency check: **Test 3 in Step 0b.** A "short-term" population that has been paying the same
lessor for four years deserves a question — **the expedient turns on the lease term, not on convenience.**

## Step 10 — Disclosures

Produce disclosure data (for the notes to the financial statements):

- **ROU assets and lease liabilities by class** — **[auto]** where the chart separates classes
- **Maturity analysis of lease liabilities** — undiscounted, by year — **[gated]**; needs the register
- **Weighted-average remaining lease term and discount rate** — **[gated]**; needs the register
- **Lease expense components** — interest, amortization, short-term, variable — **[auto]** where the chart
  separates them
- **Cash paid for leases** — **[auto]** — feeds `cash-flow-statement-indirect-method`

**Three of five are readable**, and **cash paid is exact rather than derived** — which is worth noting,
since it is a disclosure preparers frequently estimate from the schedule when the actual figure is right
there.

## Step 11 — Output

Deliver an `.xlsx` lease workbook:

**Sheet 1: Lease Register & Classification** — each lease, term, payments, rate, **classification (ASC 842)
/ single-model (IFRS 16)**. Add a **Source** column: register-supplied, or identified by the Step 0b
search. Plus the header block: workspace name; the entity by `display_name`; excluded company files; the
framework; whether any figure rests on `mock` data.

**Sheet 2: Initial Measurement** — ROU asset and liability computation per lease, **with the rate and its
source**.

**Sheet 3: Lease Liability Schedule** — effective-interest amortization per lease.

**Sheet 4: ROU Asset Schedule** — amortization, **with the operating-lease plug mechanic where applicable**,
**and the level-expense verification result**.

**Sheet 5: Journal Entries** — initial and periodic, per framework and classification, marked as
**proposals**.

**Sheet 6: Modifications / Reassessments** — remeasurements with before / after.

**Sheet 7: Disclosures** — maturity analysis, weighted averages, expense components, **cash paid (actual)**.

**Sheet 8: Completeness — NEW, Mosofin-specific**

| Test | Finding | Vendor / account | Annual value | Period | Question |

The three Step 0b tests: expense without an asset, recurring payment candidates, and the short-term
population.

**Sheet 9: Tie-Out — NEW, Mosofin-specific** — schedule closing balances against the balance sheet, and
period interest, amortization and lease expense against the P&L, **each with its difference**.

**Sheet 10: Coverage — NEW, Mosofin-specific**

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used / external source | As-at date | `mock` | Gap |

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming:** `Lease_Accounting_[YYYY]_[EntityName].xlsx`

Every file states which datasource and `display_name` it covers.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where the data does not
cover something — the terms, the rate, the judgments — **name the source required** instead of estimating.

## Step 12 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The framework** and the elections within it
- **The practical expedients elected** — short-term, low-value, portfolio — **and the consistency rule**
- **The discount rate methodology** — how the IBR is derived, by whom, at what cadence. **Not the rates**
- **The account map**: ROU by class, lease liability current and non-current, accumulated amortization,
  lease expense, short-term lease expense, variable lease expense, interest
- **The lease register structure** — the fields held and where it lives
- **The lessor list** — which vendors are lessors, **which makes the completeness search sharper each
  period**
- **The known non-lease recurring payments** — the subscriptions and service retainers already cleared, so
  the search does not re-raise them
- **The component-separation policy** — whether non-lease components are separated or combined
- **The option judgment basis** for each lease — how "reasonably certain" was concluded
- The replay recipe: the exact sequence of reads that produced the completeness search and the tie-out

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist lease terms, payment amounts, rates, balances or schedules.** All state. **And never persist
the commercial terms of the agreements** — rent levels, incentives and break clauses are commercially
sensitive, and property terms in particular are frequently confidential to the parties.

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / Northbrook
Trading — ASC 842, short-term expedient elected, IBR from bank facility + 50bp, ROU 1600, liability
2600/2610, lessors: Vendor A, Vendor C" — not "ASC 842, short-term elected". **Account maps and lessor lists
are entity-specific**, and applying one entity's cleared-payment list to another suppresses genuine findings
there. Record the chosen **scenario** (single vs multi) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's.**

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One register, one schedule, one
tie-out.

**Multi-entity.** Steps 0–11 run **once per entity**, each call targeting exactly one `data_source_id`,
every lease and balance carrying its entity's `display_name`. Then the points specific to leases:

- **Intra-group leases are real in each entity and eliminate on consolidation.** One entity owning premises
  and charging another produces **an ROU asset and liability in the lessee and rental income in the
  lessor** — **both eliminate at group level**, along with the ROU asset and the property's depreciation
  double-count. See `consolidation-and-eliminations`.
- **Run the completeness search per entity.** **A lease recognised in the parent and paid by a subsidiary**
  — or the reverse — appears as unrecognised in one and unexplained in the other.
- **The IBR is entity-specific.** A subsidiary's incremental borrowing rate is not the parent's, even under
  a group guarantee — **though the guarantee is relevant to determining it.** Never apply one entity's rate
  across the group.
- **Framework may differ** where a subsidiary reports locally, and **ASC 842 and IFRS 16 produce different
  expense patterns from identical facts** — a real conversion adjustment.
- **Lease liabilities are debt for covenant purposes** in many agreements. **A group leverage covenant
  measured after ASC 842 / IFRS 16 recognition can breach on leases alone** — see
  `debt-and-covenant-tracking`, and check the definitions.
- **Currency**: a lease denominated in a currency other than the entity's functional currency creates a
  **monetary liability** that is retranslated, while **the ROU asset is non-monetary and is not** — see
  `foreign-currency-translation-asc830`. A common and material error.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict per company
file.
