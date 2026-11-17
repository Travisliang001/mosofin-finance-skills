<!-- cash-flow-statement-indirect-method · method.md · read for: Stages 3–6 — building the statement and tying it out. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding)
- Step 1 — Establish the change in cash to explain
- Step 2 — Operating activities (indirect method)
- Step 3 — Investing activities
- Step 4 — Financing activities
- Step 5 — Effect of exchange rate changes
- Step 6 — Assemble and tie out
- Step 7 — Supplemental disclosures
- Step 8 — Direct method (optional)
- Step 9 — Output
- Step 10 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with
plain-language wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool
added.

**Never drop a task because no tool covers it.** A `[manual]` task is a task with a *named gap*, not
an absence — and in this statement an unexplained gap simply prevents the tie-out, which is the
whole point.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding)

Pull the `[auto]` / `[gated]` reads. **Batch independent reads into one message** — the two balance
sheets, the income statement, the platform's cash flow report and the ledger extracts do not depend
on each other. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`get_balance_sheet`* **at the current period end** and **at the prior period end** — the two
  points the statement bridges — usually **[auto]**
- *`get_profit_and_loss`* for the period — net income and the non-cash charges within it — usually
  **[auto]**
- *`get_cash_flow`* — **the platform's own report, as a cross-check** — usually **[auto]**
- *`get_trial_balance`* at both dates — account-level detail behind both balance sheets — usually
  **[auto]**
- *`search_accounts`* — to classify every account as operating, investing or financing, and to
  identify cash, restricted cash, debt and equity accounts — usually **[auto]**
- *`get_general_ledger`* on the **fixed-asset, accumulated-depreciation, intangible, debt and equity
  accounts** — **this is what separates capex from disposals from depreciation** — usually **[auto]**
- *`search_journal_entries`* — non-cash entries: reclassifications, write-downs, non-cash
  acquisitions — usually **[auto]**
- *`search_transfers`* — movements between the entity's own cash accounts, which must **not** appear
  as cash flows — usually **[auto]**
- *`get_company_info`* — currency and year-end — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — it cannot support a published financial
statement.

## Step 1 — Establish the change in cash to explain

```
Cash & cash equivalents — end of period          $X
Cash & cash equivalents — beginning of period     $Y
Net change in cash to explain                      $X − $Y
```

**This is the target. The completed statement must sum to exactly this amount. The whole exercise is
explaining what moved cash from $Y to $X.** **[auto]** to establish both figures
(*`get_balance_sheet`*, *`search_accounts`*).

**Define cash equivalents consistently**: short-term, highly liquid investments readily convertible
to known amounts of cash with **original maturity ≤ 3 months**. **Restricted cash** treatment differs
slightly between **US GAAP (include in the total per ASU 2016-18)** and **IFRS** — apply the
framework. **[gated]**: the accounts are readable, which of them are restricted is **[manual]**.

State the accounts included in cash on the face of the workpaper. Two people building this statement
from the same books will disagree on the answer if they disagree on what counts as cash.

## Step 2 — Operating activities (indirect method)

**Start with net income and adjust for non-cash items and working-capital changes.**

```
Net Income / (Loss)                                $NI

Adjustments for non-cash items:
  + Depreciation
  + Amortization (intangibles)
  + Amortization of ROU assets / lease (under the framework's treatment)
  + Stock-based compensation expense
  + Bad debt expense (allowance increase, non-cash portion)
  + Inventory write-downs (non-cash)
  + Impairment losses
  + Deferred income tax expense / (benefit)
  + / − Loss / (Gain) on disposal of assets  (reverse — it's an investing item)
  + / − Unrealized FX loss / (gain)
  + Other non-cash items

Changes in operating working capital:
  − Increase / + Decrease in Accounts Receivable
  − Increase / + Decrease in Inventory
  − Increase / + Decrease in Prepaid Expenses
  + Increase / − Decrease in Accounts Payable
  + Increase / − Decrease in Accrued Liabilities
  + Increase / − Decrease in Deferred Revenue
  + Increase / − Decrease in Income Tax Payable
  + / − changes in other operating assets/liabilities

= Net Cash Provided by / (Used in) Operating Activities
```

**[auto]** for net income and every working-capital change (the two balance sheets give them
directly), and for most non-cash charges (*`get_profit_and_loss`*, *`get_general_ledger`* on the
depreciation, amortisation, impairment and allowance accounts). **[gated]** for stock-based
compensation and deferred tax where they are not separately presented.

**Sign logic for working capital (the part people get wrong):**

- **Asset increase = cash used (subtract). Asset decrease = cash freed (add).**
- **Liability increase = cash deferred / source (add). Liability decrease = cash used (subtract).**

The intuition: money tied up in receivables and inventory is money not in the bank; money owed to
suppliers is money you are still holding.

**Important exclusions from working-capital changes:**

- **Only the operating portion of each balance changes.** Non-operating movements (e.g. A/R from an
  asset sale, A/P for capex) belong in investing or financing. **[auto]** to investigate — the
  ledger shows what each movement actually was
- **Balance changes caused by non-cash events (acquisitions, FX translation, reclassifications) must
  be stripped out — they didn't move cash.** **[gated]**: reclassifications and non-cash journals
  are visible (*`search_journal_entries`*); acquisitions and FX are **[manual]**. **This is the
  single most common cause of a statement that will not tie**, so investigate every material
  balance change rather than assuming it was cash

## Step 3 — Investing activities

Cash flows from acquiring and disposing of long-term assets and investments:

```
  − Purchases of property, plant & equipment (capex)
  + Proceeds from sale of PP&E
  − Purchases of intangible assets
  − Acquisitions of businesses, net of cash acquired
  + Proceeds from sale of businesses / divestitures
  − Purchases of investments
  + Proceeds from sale / maturity of investments
  − Loans made to others
  + Collections on loans made to others
= Net Cash Provided by / (Used in) Investing Activities
```

**Reconcile capex to the change in gross PP&E:**

```
Opening gross PP&E + Capex − Disposals (at cost) +/− FX +/− acquisitions = Closing gross PP&E
```

**Solve for capex if not directly given.** **This is why supplemental detail matters — the BS change
alone doesn't separate capex from disposals from depreciation.**

**Mosofin note — and this is the step the workspace improves most.** You usually do **not** have to
solve for capex. Read the **actual movements** on the fixed-asset and accumulated-depreciation
accounts (*`get_general_ledger`*, **[auto]**): additions, disposals at cost, the depreciation charge
and any reclassification each appear as their own transactions. Build the roll-forward from the
movements and use the equation above as a **check** rather than as the method. Where the two
disagree, something non-cash is in there — usually an acquisition or an FX translation.

Acquisitions of businesses remain **[manual]**: purchase accounting is outside this skill.

## Step 4 — Financing activities

Cash flows from owners and lenders:

```
  + Proceeds from issuance of debt
  − Repayments of debt
  − Principal portion of lease payments (under ASC 842 — finance leases; operating lease payments split per guidance)
  + Proceeds from issuance of equity (stock issuances)
  − Repurchases of stock (treasury)
  − Dividends / distributions paid
  + / − Other financing
= Net Cash Provided by / (Used in) Financing Activities
```

**[auto]** for most of this: debt draws and repayments, equity issuances, buybacks and dividends
each appear as movements on their accounts (*`get_general_ledger`* on the debt and equity accounts).
Build a **debt roll-forward** and an **equity roll-forward** from the movements rather than from the
net balance change — a net change of zero can conceal a draw and a repayment of equal size, and
those are two real cash flows that both belong on the statement.

**Interest and dividends classification differs by framework** — **[manual]**:

- **US GAAP**: interest paid and interest / dividends received → **operating**; dividends paid →
  **financing**
- **IFRS**: more flexibility — interest paid can be operating or financing; interest received
  operating or investing; dividends paid operating or financing — **apply the entity's elected
  policy consistently**

Record the policy applied on the face of the statement, and use the same one as last period.

## Step 5 — Effect of exchange rate changes

For entities with foreign operations or foreign-currency cash:

```
Effect of exchange rate changes on cash and cash equivalents      $±FX
```

**This is a separate line (not in operating / investing / financing) reconciling the FX impact on
cash balances held in foreign currency.** **[gated]**: the existence of foreign-currency accounts is
**[auto]**; the rate movement and the split between translation and transaction effects are
**[manual]**.

Where the entity holds no foreign currency, say the line is nil rather than omitting it — a missing
FX line and a nil FX line look identical on the page but mean different things to a reviewer.

## Step 6 — Assemble and tie out

```
Net cash from Operating                            $O
Net cash from Investing                            $I
Net cash from Financing                            $F
Effect of FX on cash                               $E
                                               ----------
Net change in cash                                 $O + I + F + E

Must equal:  Ending cash − Beginning cash          $X − $Y
```

**If it doesn't tie, the statement is wrong.** Common culprits:

- **Working-capital change includes a non-cash movement**
- **Capex / disposal not separated correctly**
- **A gain / loss not reversed out of operating**
- **FX impact not isolated**
- **An equity / dividend movement missed**

**Iterate until it ties exactly.**

**Mosofin addition — the second tie-out.** Once your statement ties to the change in cash, compare
each section against the platform's own cash flow report (*`get_cash_flow`*, **[auto]**). Both may
tie to the same change in cash while classifying items differently. **Explain every material
difference**; each one is either an error in your build or a limitation in the platform's, and
knowing which is worth having. Do not silently adopt either.

## Step 7 — Supplemental disclosures

Required:

- **Cash paid for interest** (if classified in operating under the indirect method) — **[auto]**
  from the movement on the interest and cash accounts
- **Cash paid for income taxes** — **[auto]** likewise
- **Non-cash investing and financing activities**, e.g. — **[gated]**, and detectable as journal
  entries touching two non-cash accounts (*`search_journal_entries`*):
  - **Assets acquired under leases** (ROU assets / lease liabilities)
  - **Assets acquired by assuming debt**
  - **Equity issued for acquisitions**
  - **Conversion of debt to equity**
  - **Dividends declared but not paid**

These are the transactions that changed the balance sheet without touching cash, which is exactly
why they must be disclosed rather than shown as cash flows.

## Step 8 — Direct method (optional)

If the user wants the direct method for operating activities:

```
  Cash received from customers
  − Cash paid to suppliers
  − Cash paid to employees
  − Cash paid for operating expenses
  − Interest paid
  − Income taxes paid
= Net Cash from Operating Activities
```

**[gated]**, and better supported here than in most tools: cash received from customers is derivable
from actual receipts (*`search_payments`*, *`search_sales_receipts`*, *`search_deposits`*), and cash
paid to suppliers from actual payments (*`search_bill_payments`*, *`search_purchases`*). That gives
a genuine direct-method build rather than a reverse-engineered one — though payroll usually remains
**[manual]** without a payroll connection.

**Both US GAAP and IFRS permit the direct method (and IFRS encourages it), but if you use direct, US
GAAP requires a reconciliation of net income to operating cash flow (essentially the indirect
method) as a supplement. Build both.**

## Step 9 — Output

Deliver an `.xlsx` workpaper.

**Sheet 1: Cash Flow Statement** — the full statement with the comparative period. Add a header
block: workspace name; the entity by `display_name`; each excluded company file and why; the
framework; the accounts counted as cash; the interest / dividend policy applied; whether any figure
rests on `mock` data.

**Sheet 2: Working Capital Bridge**

| Account | Opening | Closing | Change | Non-cash Adjustments | Cash Impact |

Showing how each BS change maps to the statement. **The "Non-cash Adjustments" column is where this
statement is won or lost** — every material one should name the journal or event behind it.

**Sheet 3: Investing Detail** — capex reconciliation, disposal proceeds, acquisitions. **Built from
ledger movements**, with the gross PP&E equation shown as a check.

**Sheet 4: Financing Detail** — debt roll-forward, equity movements, dividends. **Gross draws and
repayments shown separately**, never netted.

**Sheet 5: Tie-Out** — the Step 6 reconciliation, **proven to the penny** — plus the comparison
against the platform's own cash flow report with every difference explained.

**Sheet 6: Supplemental Disclosures** — interest paid, taxes paid, non-cash items.

**Sheet 7: Direct Method** (if requested) — with the indirect reconciliation.

**Sheet 8: Coverage — NEW, Mosofin-specific**

| Line or adjustment | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used | Policy (enabled / permission / disabled) | `mock` | Gap — what could not be evidenced and who supplied it |

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming:** `Cash_Flow_Statement_[YYYY-MM]_[EntityName].xlsx`

In a multi-entity run, `[EntityName]` is the company file's `display_name`, one per entity plus a
consolidated file. Every file states which datasource and `display_name` it covers.

**Grounding:** every figure traces to a tool result in this conversation or to labelled
user-supplied evidence. End with a single **Data sources** line grouping calls by datasource. Where
the data does not cover something, **name the tool that would have covered it** instead of
estimating — and **never** insert a plug.

## Step 10 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask
— explicitly, at that point, not earlier — whether to save this as their own customized version. A
general "yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The framework** and, under IFRS, **the elected interest and dividend classification policy** —
  which must be applied consistently period after period
- **The cash & cash equivalents definition**: exactly which accounts count, and which are restricted
- **The account classification map**: every account tagged operating, investing or financing. This
  is the highest-value artefact here — it is stable, it is tedious to rebuild, and getting it right
  is most of the statement
- **Which accounts hold the non-cash charges** — depreciation, amortisation, impairment, SBC,
  deferred tax — so they are added back consistently
- **Known recurring non-cash events** and how each is treated
- **The method preference** (indirect, direct, or both)
- The replay recipe: the exact sequence of reads that produced the statement

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files;
set `datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference
files alongside the installed skill.

**Do not persist the statement, the balances, or any figures.** They are one period's results and
belong in the reporting pack. Persist the *classification map and the policies*.

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks /
Northbrook Trading — IFRS, interest paid in financing, cash excludes the escrow account, SBC posts
to Share Scheme Costs" — not "interest paid in financing". Entities in a group may report under
different policies, and an unlabelled classification applied to the wrong company file misstates a
published statement. Record the chosen **scenario** (single vs multi, and which set) as a preference
too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's.**

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that
is no longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One statement, one tie-out.

**Multi-entity.** Steps 0–9 run **once per entity**, each call targeting exactly one
`data_source_id`, every line carrying that entity's `display_name`. Then consolidate deliberately:

- **A consolidated cash flow statement is not the sum of entity statements.** **Intercompany
  transfers are the reason**: a payment from one group entity to another is a real outflow in one
  set of books and a real inflow in the other, but **the group's cash never moved**. Both legs must
  be eliminated, or operating and financing cash flows are both overstated. Identify them
  (*`search_transfers`*, *`search_bill_payments`*, *`search_payments`* across entities) and net them
  explicitly. See `intercompany-reconciliation`.
- **Intercompany loans and dividends** are financing flows in each entity and nothing at group level.
  They are also the easiest to leave in by accident, because each entity's own statement is correct.
- **Each entity's statement must tie individually first.** Consolidating two statements that do not
  tie produces a group statement that ties by coincidence.
- **FX on translating a foreign subsidiary** appears at group level and not in the subsidiary's own
  statement. The FX-effect line is therefore a group phenomenon in a way the other lines are not.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each line's verdict per
company file.
