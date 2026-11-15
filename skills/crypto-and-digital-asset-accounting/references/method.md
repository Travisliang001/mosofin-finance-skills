<!-- crypto-and-digital-asset-accounting · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding)
- Step 0b — Completeness sweep (Mosofin addition)
- Step 1 — Classify the digital asset
- Step 2 — Initial measurement
- Step 3 — Subsequent measurement
- Step 4 — Recognize transactions
- Step 5 — Custody and control considerations
- Step 6 — Impairment (where the cost model applies)
- Step 7 — Disclosures
- Step 8 — Output
- Step 9 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Never drop a task because no tool covers it.** In this skill most of the substance is legitimately
`[manual]`, and recording that is the honest result.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding)

Pull the `[auto]` / `[gated]` reads. **Batch independent reads into one message** — the asset accounts,
the cash movements and the gain / loss accounts do not depend on each other. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`search_accounts`* — **the digital asset, gain / loss, impairment and mining-revenue accounts** —
  usually **[auto]**
- *`get_balance_sheet`* / *`get_trial_balance`* — **the recorded carrying value** — usually **[auto]**
- *`get_general_ledger`* on those accounts — **every movement recorded**, including impairments and
  revaluations — usually **[auto]**
- *`search_purchases`* / *`search_bill_payments`* / *`search_transfers`* — **fiat paid out to exchanges
  and custodians** — usually **[auto]**
- *`search_deposits`* — **fiat received back from exchanges** — usually **[auto]**
- *`search_vendors`* / *`get-vendor`* — exchanges and custodians as counterparties — usually **[auto]**
- *`get_profit_and_loss`* — gains, losses and mining or staking revenue recorded — usually **[auto]**
- *`search_invoices`* / *`search_payments`* — customer invoices settled in crypto — usually **[auto]**
- *`search_journal_entries`* — manual crypto entries, which is how most of this gets recorded — usually
  **[auto]**
- *`get_company_info`* — base currency and calendar — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — it cannot support a carrying value, an
impairment, or a disclosure about assets whose existence is already the hardest thing to prove.

## Step 0b — Completeness sweep (Mosofin addition)

**Run before Step 1.** The holdings list is what the user knows about; this tests it against what the money
says. It is the same technique as the legal-spend sweep in `contingencies-and-litigation-asc450`, and it
works for the same reason: **crypto is bought with fiat, and fiat leaves a trail.**

**[auto]** signals, each of which may indicate an unrecorded or under-recorded position:

- **Cash paid to an exchange or custodian** (*`search_purchases`*, *`search_transfers`*,
  *`search_vendors`*) with **no corresponding digital asset recorded**
- **Cash received from an exchange** with no corresponding disposal recorded — money came back from
  somewhere, and a sale happened
- **A digital asset account with movement but no supporting holdings data supplied**
- **Mining or staking revenue recorded** with no corresponding asset addition
- **A customer invoice marked settled** with no matching fiat receipt — it may have been paid in crypto

**Report each signal as a question**, and where the sweep finds nothing, **say it was run and found
nothing** — that is what makes the holdings list's completeness defensible. If the relevant tools are
unavailable, record the sweep as **not performed** rather than reporting no exceptions.

## Step 1 — Classify the digital asset

Different digital assets have different accounting. **[manual]** throughout — classification depends on
the asset's characteristics and the entity's purpose, neither of which is in the ledger.

**Cryptocurrencies (e.g. BTC, ETH) held as investments:**

- **US GAAP (post-ASU 2023-08)**: certain crypto assets meeting specific criteria — fungible, on a public
  blockchain, not an issuer's own, and others — are measured at **fair value through net income** each
  reporting period. **Confirm scope; ASU 2023-08 has specific scope.**
- **Pre-ASU 2023-08** (or for crypto outside the scope): **cost less impairment** as an indefinite-lived
  intangible — impairment to the **lowest observed price during the period, no reversal**
- **IFRS**: typically an **intangible asset under IAS 38** (cost model, or revaluation model if there is
  an active market). Some entities classify as **inventory under IAS 2** if held for sale in the ordinary
  course of business (broker-dealers / traders). Specific entity-type guidance can apply

**Stablecoins**: **assessment depends on the right to redeem** — may be a receivable or cash equivalent if
redeemable at par on demand for fiat, or treated like other crypto if not. **Carefully assess.** A
stablecoin is a claim on an issuer, and its accounting follows that claim, not its name.

**NFTs**: typically intangible assets, generally indefinite-lived. **Limited fungibility means typically
cost-less-impairment under both frameworks** (ASU 2023-08 scope criteria typically not met).

**Tokens received in exchange for goods / services** (revenue or barter): consideration measured at fair
value; revenue recognition per `revenue-recognition-asc606`.

**Mining / staking rewards**:

- **Mining**: rewards earned from validating blocks — generally recognized at **fair value as revenue**
  (per the entity's business activity) or other income; **tax treatment is a separate area**
- **Staking**: rewards from staking — recognition depends on whether services are provided

**Document the classification for each asset.**

## Step 2 — Initial measurement

- **Crypto purchased**: cost — purchase price plus directly attributable acquisition costs and transaction
  fees. **[gated]**: the **fiat outflow is [auto]**; the allocation across lots and assets is **[manual]**
- **Crypto received in exchange**: **fair value of the crypto received** — or of the goods / services given
  up, **whichever is more reliable**. **[gated]**: the invoice value is **[auto]** where a customer settled
  in crypto
- **Mining / staking rewards**: **fair value of the crypto received at the date of receipt** —
  **[manual]**, and note that "the date of receipt" for frequent rewards may mean many valuations

## Step 3 — Subsequent measurement

Apply the right basis and **document the measurement model, applying it consistently**. **[manual]** for
the choice; **[auto]** arithmetic once the model and the prices exist.

**US GAAP (ASU 2023-08 scope)**: **fair value each reporting date, with changes in net income.** Use the
**principal market's** price.

**US GAAP (out of ASU 2023-08 scope) / indefinite-lived intangible legacy**: **cost less impairment.
Impairment when fair value at any time during the period is below carrying amount; written down to that
lowest observable fair value. No reversal** under US GAAP. Note what this demands in practice: you need
prices **throughout** the period, not just at period end.

**IFRS (IAS 38 cost model)**: cost less impairment (per IAS 36). **Reversals permitted** up to original
cost.

**IFRS (IAS 38 revaluation model)**: revalue to fair value **if an active market exists**, with changes to
**revaluation surplus in OCI** (gains) or **P&L** (losses, to the extent they reverse a prior surplus); on
derecognition the surplus may be transferred within equity.

**IFRS (IAS 2 inventory)** for broker-dealers and traders: **fair value less costs to sell, changes to
P&L**. For other entities holding as inventory: **lower of cost and NRV**.

## Step 4 — Recognize transactions

`DR` is a debit, `CR` a credit. **Mosofin does not post** — these are proposals. Use the **real account
names from the connected chart of accounts** (*`search_accounts`*, **[auto]**).

**Purchase**:
```
DR  Digital Asset (at cost)
    CR  Cash
    (+ DR Transaction Fee Expense if not capitalized)
```
**[gated]** — the cash leg is **[auto]**, the asset leg **[manual]**.

**Sale**:
```
DR  Cash
    CR  Digital Asset (at carrying amount)
    CR  Gain on Sale (or DR Loss)
```
**Use the cost basis per the entity's method** — **specific identification is typical; FIFO or other
methods possible. Confirm what's permitted under the framework and the entity's policy.** The method
choice can change the gain materially and is **[manual]**.

**Receipt as payment**:
```
DR  Digital Asset (at fair value)
    CR  Revenue (or other applicable account)
```

**Use as payment** (the entity sends crypto to pay a vendor):
```
DR  Expense / Liability
    CR  Digital Asset (carrying)
    +/- Gain/Loss on transfer (FV vs. carrying)
```
Worth noting because it surprises people: **paying a supplier in crypto is a disposal**, and it crystallises
a gain or loss on the way past.

**Mining / staking reward**:
```
DR  Digital Asset (at fair value at receipt)
    CR  Mining/Staking Revenue (or other income)
```

## Step 5 — Custody and control considerations

- **Self-custody** (the entity holds private keys): the entity has the asset **and the risk of key loss**
- **Exchange / custodian**: **assess whether the entity has the asset or merely a claim against the
  custodian.** The FTX-type failure highlighted that assets on a failed custodian can become a
  **receivable subject to collectibility risk**; assess control and counterparty risk
- **Internal controls over keys, access, and transactions are critical**
  (`sox-controls-design-and-testing`)

**Disclose custody arrangements and significant concentrations.**

All **[manual]** — the accounting system does not know where the keys are. **[auto]** contribution only:
the exchanges and custodians the entity has *paid* are visible as counterparties, which is a starting
list of where assets might be held.

## Step 6 — Impairment (where the cost model applies)

For cost-model crypto and NFTs — **[gated]**: the arithmetic and the recorded impairments are **[auto]**,
**every price is [manual]**:

- **US GAAP**: impair to the **lowest observable fair value during the period** — **no reversal**
- **IFRS**: impair if recoverable amount < carrying; **reversible up to original cost**

**For NFTs without an active market**, impairment can be hard to measure; **document the basis** — often the
most recent comparable sale or another reliable indicator. **Frequent assessment is required given
volatility.**

The US GAAP rule deserves emphasis because it is punitive and easily missed: it requires the **lowest**
price at **any point** in the period, not the period-end price. A price series is therefore needed, and a
single closing quote is not sufficient evidence.

## Step 7 — Disclosures

**Disclosure expectations are evolving and significant.** For `notes-to-financial-statements`:

- **Description of digital assets held and the purpose**
- **Accounting policy applied** (framework, model, classification)
- **Carrying amounts and fair values**, with the **fair value measurement category — Level 1 / 2 / 3**
- **Activity in the period**: purchases, sales, gains / losses, mining and staking — **[auto]** where the
  movements were recorded
- **Custody arrangements and risks**
- **For US GAAP under ASU 2023-08**: specific required disclosures including a **reconciliation by
  significant holding**

**Confirm current disclosure requirements — they have changed and may change further.**

## Step 8 — Output

Deliver an `.xlsx` workpaper.

**Sheet 1: Digital Asset Inventory** — by asset, quantity, custody location, classification. **Mark, per
line, whether the quantity was supplied or read**, and **as at what date the holding was evidenced**.

**Sheet 2: Classification & Measurement Policy** — per asset type: framework, classification, measurement
model, rationale. Add a header block: workspace name; the entity by `display_name`; each excluded company
file and why; **the date the standard was last confirmed**; whether any figure rests on `mock` data.

**Sheet 3: Lot-Level Cost Basis** — acquisition lots with costs, for cost-basis tracking on sales.

**Sheet 4: Fair Value Measurement** — period-end and period-activity fair values; **principal market
source and timestamp for every price**.

**Sheet 5: Transactions Register** — purchases, sales, transfers, payments, mining and staking, with
entries. **Add a column showing whether the fiat leg was read from the ledger.**

**Sheet 6: Impairment** (cost model) — triggers, computations, reversals (IFRS) where applicable.

**Sheet 7: Mining / Staking Revenue** — per receipt at fair value.

**Sheet 8: Disclosures** — disclosure-ready data including custody and counterparty risk.

**Sheet 9: Open Items / Specialist** — areas needing accounting, legal or tax specialist input; **standards
confirmation**.

**Sheet 10: Completeness Sweep — NEW, Mosofin-specific**

| Signal | Evidence (counterparty, amount, date) | Matched to a recorded holding or transaction? | Question for the user |

**Sheet 11: Coverage — NEW, Mosofin-specific**

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used / external source | As-at date | Policy | `mock` | Gap |

Every holding and every price reads `manual` with its source and timestamp. That is the correct, expected
result.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming:** `Crypto_Accounting_[YYYY-MM]_[EntityName].xlsx`

`[EntityName]` is the company file's `display_name`. Every file states which datasource and `display_name`
it covers.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where the data does not
cover something — every holding, every price — **name the source required** instead of estimating.

## Step 9 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The framework and the classification per asset type**, with the rationale — and **the date the
  classification was reached**, since it depends on standards that change
- **The measurement model** applied to each classification
- **The cost basis method** on disposals
- **The account map**: digital asset accounts, gain / loss, impairment, mining and staking revenue
- **The custody map**: which exchanges and custodians hold what, and which entity owns each wallet — **by
  name and role, never by address or key**
- **The price source**: which venue is the principal market for each asset, and how prices are obtained.
  **Not the prices themselves**
- **The specialists engaged** for tax, DeFi and legal questions
- The replay recipe: the exact sequence of reads that produced the recorded movements and the completeness
  sweep

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist wallet addresses, private keys, seed phrases, exchange credentials, holdings or prices.**
This is the strictest persistence rule in the pack alongside the litigation one, and for a blunt reason:
**a private key or seed phrase is the asset.** Anyone holding it can take the funds irreversibly. Wallet
addresses are also a privacy exposure, since a public address reveals the entire transaction history and
balance to anyone who has it. **Persist the policy, the classification and the counterparty names — never
anything that identifies or controls a wallet.**

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / Northbrook
Digital — IFRS, IAS 38 cost model for BTC and ETH, specific identification on disposal, custody with a
named institutional custodian" — not "IAS 38 cost model". Entities in a group may hold for different
purposes and therefore classify differently, and an unlabelled measurement model applied to the wrong
company file misstates the balance sheet and the P&L together. Record the chosen **scenario** (single vs
multi, and which set) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's** — and holdings, prices and the current text of a standard are all state.

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One holdings schedule, one policy.

**Multi-entity.** Steps 0–8 run **once per entity**, each call targeting exactly one `data_source_id`,
every holding carrying its entity's `display_name`. Then:

- **Which entity owns a wallet is not recorded on the chain.** An address has no legal owner. Ownership is
  established by the **fiat trail** — which entity's bank account paid for the assets — and by
  documentation. **Where two entities have both funded the same wallet, ownership is genuinely ambiguous
  and must be resolved with legal advice**, not assumed.
- **The fiat trail is `[auto]` and is your best evidence of attribution.** Run the completeness sweep per
  entity and compare: cash out from entity A funding a wallet whose assets sit on entity B's balance sheet
  is either an intercompany loan or a misattribution.
- **Classification may legitimately differ by entity** — one holding for investment, another trading — so
  a group total carries mixed measurement bases. Say so rather than presenting a single figure.
- **Concentration and custody risk aggregate.** Three entities each holding a modest position with the
  same custodian is one counterparty exposure at group level, and the custodian-failure risk is a group
  risk.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict per company
file.
