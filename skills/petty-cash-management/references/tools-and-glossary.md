<!-- petty-cash-management · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| `create_skill` | Persists the evolved skill. Step 8. | `name`, `description`, `destination`, `files`, `datasources`, `confirmed` |

Typical evidence tools — **resolve real names and policies from your Gate 2 catalog**:

| Purpose | Typical tool | Key arguments |
|---|---|---|
| **The petty cash accounts and Cash Over/Short** | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| **The petty cash balance** | `get_balance_sheet` / `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| **The imprest invariant test, and the shortage trend** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| **Replenishments, with dates and amounts** | `search_payments` / `search_checks` | `start_date`, `end_date` (required) |
| Where several floats exist | `search_locations` / `search_classes` | `query`/`name`, `active_only` |
| Legal name, **currency** | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no physical count, no voucher, no receipt and no custodian on this surface.**

---

## Plain-language glossary

- **Petty cash** — a small amount of cash kept on hand for minor purchases.
- **Imprest system** — the float is a fixed amount, topped back up to that amount each time. **The GL
  balance never changes**, which is what makes the reconciliation simple and the control real.
- **Float** — the authorised fixed amount.
- **Custodian** — the person responsible for the tin and accountable for what is in it.
- **Voucher** — the slip recording what was spent, ideally with a receipt attached.
- **Replenishment** — topping the fund back up to the float, and the moment the expenses are actually
  recorded.
- **IOU / temporary advance** — cash lent from the float, not yet spent or repaid. **Not an expense**, and
  not a voucher.
- **Cash over / short** — the difference between what should be there and what is. **Short is more common;
  over is more interesting.**
- **Tolerance** — the size of difference the entity accepts without investigating. **Set by policy, never
  assumed.**
- **Dormant float** — one nobody has used in a long time. **Still cash, still someone's responsibility, and
  still needing a count.**
