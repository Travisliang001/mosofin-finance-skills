<!-- crypto-and-digital-asset-accounting · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

## Tool reference

Mosofin workflow tools — call by these bare names, whatever your client displays:

| Tool | What it does | Key arguments |
|---|---|---|
| `list_workspaces` | Lists / confirms the workspace(s). Gate 0. | none on discovery; then `workspace_ids`, `mode` (`single` / `multi`) |
| `get_agent_datasources` | Lists live connections and their `connected` flag. Gate 1. | `workspace_id` |
| `get_datasource_tools` | Lists read tools and each one's `effective_policy`. Gate 2. | `workspace_id`, `datasource`, `data_source_id` (required when several files are live) |
| `invoke_datasource_api_tool` | Reads business data. | `datasource`, `tool_name`, `params`, `data_source_id` (**every call**), `approved` (only after an explicit yes) |
| `get_skills` | Lists saved skills in this workspace. | `workspace_id` |
| `get_my_skill` | Fetches one saved skill's bundle. | `skill_id`, `confirmed` |
| `create_skill` | Persists the evolved skill. Step 9. | `name`, `description`, `destination`, `files`, `datasources`, `confirmed` |

Typical evidence tools — **resolve real names and policies from your Gate 2 catalog**:

| Purpose | Typical tool | Key arguments |
|---|---|---|
| Digital asset, gain/loss, impairment and revenue accounts | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| **Recorded carrying value** | `get_balance_sheet` / `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| **Every movement recorded, incl. impairments** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| **Fiat paid out to exchanges and custodians** | `search_purchases` / `search_bill_payments` / `search_transfers` | `start_date`, `end_date` (required), `vendor_id` |
| **Fiat received back from exchanges** | `search_deposits` / `get_deposit` | `start_date`, `end_date` (required); `id` |
| Exchanges and custodians as counterparties | `search_vendors` / `get-vendor` / `get_vendor_expenses` | `query`/`name`; `start_date`, `end_date`, `vendor` |
| Gains, losses, mining and staking revenue recorded | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by` |
| Customer invoices settled in crypto | `search_invoices` / `search_payments` | `start_date`, `end_date` (required), `customer_id` |
| **Manual crypto entries** | `search_journal_entries` / `get_journal_entry` | `start_date`, `end_date` (required); `id` |
| Base currency and calendar | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no price feed, no chain explorer and no wallet balance in an accounting datasource.**

---

## Plain-language glossary

- **Digital asset / crypto asset** — a token recorded on a blockchain rather than by a bank or registrar.
- **Fungible** — interchangeable, one unit identical to another. **NFT (non-fungible token)** — the
  opposite: each one unique.
- **Stablecoin** — a token intended to hold a fixed value, usually by being redeemable for a currency.
  Whether it *is* redeemable is the accounting question.
- **Wallet / private key / seed phrase** — the store of value and the secrets that control it. **Whoever
  holds the key holds the asset.**
- **Self-custody vs. custodian** — you hold the keys, or someone else does on your behalf.
- **ASU 2023-08** — the US standard introducing fair-value measurement for certain crypto assets.
- **IAS 38 / IAS 2 / IAS 36** — the IFRS standards for intangibles, inventories and impairment, applied
  to crypto in the absence of a specific one.
- **Indefinite-lived intangible** — an intangible with no fixed life, tested for impairment rather than
  amortised.
- **Cost less impairment** — carry at what you paid, written down when worth less, and (under US GAAP)
  **never written back up**.
- **Revaluation model** — carry at fair value, with gains going to a reserve in equity rather than profit.
- **Revaluation surplus / OCI** — where those gains sit.
- **NRV (net realisable value)** — what you could sell it for, less costs to sell.
- **Principal market** — the venue with the greatest volume for that asset; the price source fair value
  should come from.
- **Level 1 / 2 / 3** — the fair value hierarchy: quoted prices, observable inputs, unobservable inputs.
- **Lot** — a specific parcel bought at a specific time and price.
- **Specific identification / FIFO** — which parcel you treat as sold, which changes the gain.
- **Mining** — earning tokens by validating transactions. **Staking** — earning by committing tokens to
  secure a network.
- **Fork** — a blockchain splitting, sometimes giving holders new tokens. **Airdrop** — tokens distributed
  free to holders.
- **DeFi / yield farming / liquidity provision** — lending and market-making through smart contracts.
