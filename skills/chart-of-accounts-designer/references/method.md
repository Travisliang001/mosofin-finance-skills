<!-- chart-of-accounts-designer · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding)
- Step 0b — Measure account usage (Mosofin addition to Step 1)
- Step 1 — Establish the structure
- Step 2 — Build the account list by section
- Step 3 — Industry-specific accounts
- Step 4 — Tax accounts
- Step 5 — Multi-entity considerations
- Step 6 — Output
- Step 7 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with
plain-language wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool
added.

**Never drop a task because no tool covers it.** A `[manual]` task is a task with a *named gap*, not
an absence.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding)

Pull the `[auto]` / `[gated]` reads. **Batch independent reads into one message** — the account list,
the dimensions, the tax codes and the ledger activity do not depend on each other. Never serialize
them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`search_accounts`* — **the full chart of accounts**, including inactive accounts — usually
  **[auto]**
- *`get_account`* — one account's full detail: type, sub-type, parent, active status — usually
  **[auto]**
- *`get_general_ledger`* over a long window (24 months where available) — **the usage behind every
  account**: transaction counts, amounts, and last activity date — usually **[auto]**
- *`get_trial_balance`* — every account's balance, to pair with usage — usually **[auto]**
- *`get_profit_and_loss`* / *`get_balance_sheet`* — how accounts currently roll up in reporting —
  usually **[auto]**
- *`search_classes`* / *`search_departments`* — **the dimensions actually in use** — usually **[auto]**
- *`search_tax_codes`* / *`search_tax_rates`* / *`search_tax_agencies`* — the tax structure actually
  in use — usually **[auto]**
- *`search_items`* — products and services, which reveal how revenue is really segmented — usually
  **[auto]**
- *`search_journal_entries`* — manual entries, which often reveal accounts used as workarounds —
  usually **[auto]**
- *`get_company_info`* — industry, currency, legal name — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — a retire list built on fixture usage would
recommend deactivating accounts a real business depends on.

## Step 0b — Measure account usage (Mosofin addition to Step 1)

Before designing, **measure what is actually there**. This is the analysis that makes every
recommendation below evidenced rather than asserted, and it takes one ledger read.

For each account — **[auto]**:

- **Transaction count** over the lookback window
- **Total value** posted
- **Last activity date**
- **Current balance**
- **Active / inactive status**
- **Whether it is used by any dimension, item, or tax code**

Then classify:

- **Live** — regular activity
- **Occasional** — used, but rarely; check whether a dimension would serve better
- **Dormant** — no activity in the window, **nil balance** → a retire candidate
- **Dormant with a balance** — no activity but money sitting in it → **investigate before retiring**;
  this is often a forgotten reconciling item rather than a dead account
- **Never used** — created and never posted to → the clearest retire candidates

State the lookback window used. An account dormant for 24 months is a different claim from one
dormant for 3.

## Step 1 — Establish the structure

Decide the overall structure based on the target system and entity needs.

**Numbering schemes** (pick one and apply consistently) — **[manual]** to choose, **[auto]** to see
what is currently in use:

- **4-digit (1000s)**: suitable for small entities, fewer than ~200 accounts
- **5-digit**: suitable for mid-market with departments or locations
- **6–7 digit**: enterprise with deep segmentation
- **Alphanumeric**: some systems allow text codes

**[auto]** input: the current account count tells you whether the existing scheme still fits. A
4-digit chart with 380 accounts has already outgrown itself.

**Conventional ranges** (**recommended but not mandatory** — the user's existing scheme may differ):

- **1000–1999**: Assets
- **2000–2999**: Liabilities
- **3000–3999**: Equity
- **4000–4999**: Revenue
- **5000–5999**: Cost of Goods Sold / Cost of Services
- **6000–7999**: Operating Expenses
- **8000–8999**: Other Income / Other Expense
- **9000–9999**: Income tax, special items

**Dimension strategy**:

**Prefer dimensions (class / department / location / project) for slicing reporting rather than
proliferating accounts.** Example: **one "Salaries" account with a Department dimension is better
than separate Salaries accounts per department.**

**[auto]** and directly useful here: read the dimensions in use (*`search_classes`*,
*`search_departments`*) **and** look for accounts whose names encode a dimension — "Salaries –
Sales", "Salaries – Ops", "Rent – London". Those are exactly the accounts that should collapse into
one account plus a dimension, and they are mechanically detectable by name pattern. Present them as
a consolidation list.

## Step 2 — Build the account list by section

Every section below is **[manual]** to design and **[auto]** to check against what already exists —
so present each as *keep / add / merge / retire* rather than as a fresh list, wherever a chart is
already in place.

#### Assets (1000s)

**Current assets:**
- **Cash and cash equivalents** (one or several — one per bank account if practical)
- **Marketable securities / short-term investments**
- **Accounts receivable**
- **Allowance for doubtful accounts** (contra-AR — a *contra* account reduces the account it sits
  against)
- **Other receivables** (employee advances, related parties — **separate from trade A/R**)
- **Inventory** (with sub-accounts if multiple categories)
- **Prepaid expenses**
- **Input tax recoverable** (if the jurisdiction supports recovery)
- **Other current assets**

**Non-current assets:**
- **Property, plant & equipment (gross)**
- **Accumulated depreciation** (contra)
- **Intangible assets (gross)**
- **Accumulated amortization** (contra)
- **Right-of-use assets** (under ASC 842 / IFRS 16)
- **Goodwill**
- **Long-term investments**
- **Deferred tax assets**
- **Other non-current assets**

#### Liabilities (2000s)

**Current liabilities:**
- **Accounts payable**
- **Accrued expenses / accrued liabilities**
- **Customer deposits / deferred revenue** (current portion)
- **Sales tax / VAT / GST payable** (per jurisdiction)
- **Payroll liabilities** — **separate by type**: wages payable, income tax withheld, social-charge
  withheld, benefits payable
- **Current portion of long-term debt**
- **Lease liability** (current portion)
- **Income tax payable**
- **Other current liabilities**

**Non-current liabilities:**
- **Long-term debt**
- **Lease liability** (non-current portion)
- **Deferred revenue** (non-current portion)
- **Deferred tax liabilities**
- **Other non-current liabilities**

#### Equity (3000s)

Structure depends on entity type — **[manual]**, since legal form is not in the books:

- **Sole proprietor**: Owner's Capital, Owner's Draw
- **Partnership / LLC**: Member Capital, Member Distributions, Member Contributions (per member if
  needed)
- **Corporation**: Common Stock, Preferred Stock, Additional Paid-in Capital, Treasury Stock,
  Retained Earnings, Accumulated OCI

#### Revenue (4000s)

- **Primary revenue stream(s)** — one account per stream **if the entity reports them separately**
- **Sales returns and allowances** (contra)
- **Sales discounts** (contra)
- **Other revenue** (separate from primary)

**[auto]** input worth using: the **items** list (*`search_items`*) and revenue by customer
(*`get_customer_sales`*) show how revenue is *actually* segmented today, which is often finer or
coarser than the account structure suggests.

- **For SaaS**: subscription revenue / professional services revenue / other
- **For Services firms**: by service line if material
- **For Product companies**: by product family if material
- **For Construction**: by contract type (percentage-of-completion may require separate billings and
  costs accounts)

#### Cost of Goods / Services (5000s)

- **Direct materials**
- **Direct labor**
- **Manufacturing overhead allocated**
- **Inventory adjustments / shrinkage**
- **Cost of services delivered**

#### Operating Expenses (6000–7000s)

Group **by function or by nature**, depending on the user's reporting framework:

- **By nature**: Salaries, Benefits, Rent, Utilities, Travel, Marketing, Professional Fees, Software,
  Insurance, Depreciation, etc.
- **By function**: Cost of Revenue, R&D, S&M, G&A (common for SaaS / tech)

**Always include:**
- **Bad debt expense**
- **Foreign exchange gain / loss**
- **Bank charges**

#### Other Income / Expense (8000s)

- **Interest income**
- **Interest expense**
- **Gain / loss on disposal of assets**
- **Impairment losses**
- **Other one-off items**

#### Tax (9000s)

- **Current income tax expense**
- **Deferred income tax expense**
- **Other tax expense** (if separate)

## Step 3 — Industry-specific accounts

**Add accounts the entity's industry typically needs (only if the user confirms the industry).**

| Industry | Specific accounts |
|----------|-------------------|
| **SaaS / Tech** | Deferred revenue (sub-ledger), Subscription revenue, Hosting costs, R&D capitalized vs. expensed, Stock-based compensation |
| **Construction** | Contracts receivable, Retainage, Costs in excess of billings, Billings in excess of costs, WIP |
| **Real Estate** | Rental income, Tenant improvements, Property management fees, CAM recoveries, Security deposits held |
| **Manufacturing** | Raw materials, WIP, Finished goods, Manufacturing variances |
| **Retail / E-commerce** | Sales by channel, Returns reserve, Gift card liability, Loyalty program liability |
| **Professional Services** | WIP unbilled, Project accounts, Sub-contractor costs |
| **Nonprofit** | Restricted vs. unrestricted net assets, Grant revenue, Program vs. supporting expenses |
| **Restaurants / Hospitality** | Food cost, Beverage cost, Tip liability, Comp meals |
| **Healthcare** | Patient revenue, Insurance receivable by payer, Contractual adjustments |
| **Financial services** | Interest income / expense by category, Loan loss reserves, Trading gains / losses |

**[gated]**: the profile gives the industry (**[auto]**) but **confirm it** — a registered industry
code is frequently generic or out of date, and adding a whole block of construction accounts to a
consultancy is a costly error.

## Step 4 — Tax accounts

Add tax accounts **per the entity's jurisdictions (only if the user has provided them)**:

- **Output tax payable** per jurisdiction
- **Input tax recoverable** per jurisdiction (if the regime allows)
- **Tax-exempt sales tracking**
- **Tax suspense / clearing**

**Do not assume any specific jurisdiction's tax accounts. Build to what the user specifies.**

**[auto]** input: the tax codes, rates and agencies actually in use (*`search_tax_codes`*,
*`search_tax_rates`*, *`search_tax_agencies`*) show which jurisdictions the entity genuinely
transacts in — a much better starting point than the registered address, and a useful cross-check
against what the user says.

## Step 5 — Multi-entity considerations

If the entity is part of a group — **[gated]**:

- **Intercompany receivable / payable accounts** (**one per counterparty entity**) — **[auto]** to
  propose the list, since the connected entities are known by name
- **Equity in investees**
- **Investment in subsidiaries**
- **Elimination accounts** (only if using elimination journals)

**One intercompany account per counterparty is the rule that makes intercompany reconciliation
possible at all** — a single "Intercompany" account across three counterparties cannot be reconciled
to anything. See `intercompany-reconciliation`.

## Step 6 — Output

Deliver an `.xlsx` COA workpaper.

**Sheet 1: Chart of Accounts**

| Account # | Account Name | Type | Sub-type / Detail Type | Normal Balance | Description / Intended Use | Active Y/N | Reporting Tag(s) |

- **Type**: Asset / Liability / Equity / Revenue / Expense
- **Sub-type**: per the user's accounting system (each platform uses its own detail-type taxonomy) —
  **ask if uncertain**
- **Description**: 1–2 sentences explaining what posts here
- **Reporting Tag**: how this rolls up on the P&L / Balance Sheet

**Add:** a **Source** column — *existing (read from the connected system)* or *proposed* — so a
reader can see at a glance what is new.

**Sheet 2: System-Specific Import File**

Formatted to the target accounting system's import template. **Ask for the system's template if not
standard.** Where the target differs from the connected source, note that account types and detail
types will not map one-to-one.

**Sheet 3: Migration Map** (if restructuring an existing COA)

| Old Account # | Old Account Name | New Account # | New Account Name | Action (Keep / Merge / Rename / Retire) | Migration JE Needed Y/N |

**Add:** **Transaction count**, **last activity date** and **balance** per old account — the evidence
behind every Retire and Merge decision.

**Sheet 4: Dimensions / Classes** (if using)

Recommended class, department, location, and project lists. **Add:** the accounts whose *names*
encode a dimension and should collapse into one account plus a dimension.

**Sheet 5: Account Usage Analysis — NEW, Mosofin-specific**

| Account | Type | Transactions (window) | Value posted | Last activity | Balance | Classification (live / occasional / dormant / dormant-with-balance / never used) | Recommendation |

This sheet is what turns the first edge case from advice into a work list.

**Sheet 6: Coverage — NEW, Mosofin-specific**

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used | Window used | Policy | `mock` | Gap — what could not be evidenced and who supplied it |

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming:** `[EntityName]_COA_[YYYY-MM-DD].xlsx`

`[EntityName]` is the company file's `display_name`. In a harmonisation run, one file per entity plus
a combined comparison file. Every file states which datasource and `display_name` it covers, and the
usage window measured.

**Grounding:** every figure traces to a tool result in this conversation or to labelled
user-supplied evidence. End with a single **Data sources** line grouping calls by datasource. Where
the data does not cover something, **name the tool that would have covered it** instead of
estimating.

## Step 7 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask
— explicitly, at that point, not earlier — whether to save this as their own customized version. A
general "yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The numbering scheme and the range convention** actually adopted — which may not be the
  conventional one
- **The dimension strategy**: which dimensions exist, what each means, and the rule for when to add
  an account versus a dimension value
- **The account descriptions and intended use** — the single thing most charts lack, and the reason
  they decay
- **The industry account set** confirmed for this entity, and any deliberately excluded
- **The tax account structure** per confirmed jurisdiction
- **The target system** and its detail-type mapping
- **The retire / merge decisions taken and deferred**, with the reason — so next review does not
  re-litigate them
- The replay recipe: the exact sequence of reads that produced the chart and the usage analysis

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files;
set `datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference
files alongside the installed skill.

**Do not persist account balances or transaction values.** The *structure* is the durable decision;
the *amounts* are state and go stale immediately.

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks /
Northbrook Trading — 5-digit scheme, departments for Ops/Sales/G&A, construction account set
excluded" — not "5-digit scheme". Sibling entities frequently run different charts, and an unlabelled
numbering scheme applied to the wrong company file produces a migration map that maps nothing.
Record the chosen **scenario** (single vs harmonisation, and which set) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's** — and account usage is state, re-measured every review.

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is
no longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One chart, one usage analysis,
one migration map.

**Multi-entity harmonisation.** Read each entity's chart **separately**, each call targeting exactly
one `data_source_id`, every account carrying its entity's `display_name`. Then compare — and this
comparison is the deliverable:

- **A side-by-side account map across entities**: which accounts exist everywhere, which exist at only
  one, and which mean the same thing under different names. **Accounts that differ only in wording
  are the main obstacle to group reporting**, and they are mechanically detectable.
- **Propose a common core chart** plus permitted entity-specific extensions. A fully identical chart
  across entities in different businesses is usually the wrong goal; a common core with controlled
  local additions is the workable one.
- **Harmonise the numbering before the names.** If the same concept sits at 6100 in one entity and
  6400 in another, every consolidation mapping has to be maintained by hand forever.
- **Intercompany accounts need one per counterparty, at every entity**, and they must be symmetrical:
  A's receivable from B must have a counterpart in B. Propose the full matrix.
- **Usage differs by entity.** An account dormant at one entity may be core at another — never build
  a group retire list from one entity's activity.
- **Capability is checked per entity**: the ledger tool may be enabled for one company file and not
  its sibling, so the usage analysis can be evidenced for one and unevidenced for another. The
  coverage sheet shows this per file.
