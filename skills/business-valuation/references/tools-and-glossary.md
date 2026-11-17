<!-- business-valuation · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| `create_skill` | Persists the evolved skill. Step 12. | `name`, `description`, `destination`, `files`, `datasources`, `confirmed` |

Typical evidence tools — **resolve real names and policies from your Gate 2 catalog**. Every one of
these is read **as at the valuation date**:

| Purpose | Typical tool | Key arguments |
|---|---|---|
| Earnings history, EBITDA, D&A, effective tax rate | `get_profit_and_loss` | `start_date`, `end_date`, `summarize_column_by`, `accounting_method` |
| Capital structure, net debt, working capital | `get_balance_sheet` | `start_date`, `end_date`, `accounting_method`, `summarize_column_by` |
| Capex, D&A, actual cash generation | `get_cash_flow` | `start_date`, `end_date`, `summarize_column_by` |
| Complete account-level position | `get_trial_balance` | `start_date`, `end_date`, `accounting_method` |
| **Itemising debt-like and restricted-cash accounts** | `search_accounts` / `get_account` | `query`/`name`, `active_only`; `id` |
| Detail behind debt, cash and fixed assets | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| Revenue concentration (company-specific risk evidence) | `get_customer_sales` | `start_date`, `end_date`, `customer`, `summarize_column_by` |
| Customer base and churn evidence | `search_customers` / `search_invoices` | `query`/`name`; `start_date`, `end_date` (required) |
| Working-capital components in detail | `get_aged_receivables` / `get_aged_payables` | `report_date`, `customer`/`vendor` |
| Inventory position | `search_items` / `read_item` | `query`/`name`, `active_only`; `id` |
| Segment view where classes / departments are used | `search_classes` / `search_departments` | `query`/`name`, `active_only` |
| Legal name, currency, year-end, industry | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There is no market-data tool in this table because none exists.** Risk-free rates, equity risk
premia, betas, peer multiples, transaction multiples, control premia and DLOM studies are all
external, `[manual]`, and must carry a source and a date.

---

## Plain-language glossary

- **Valuation date** — the as-of date. Every figure, company and market, must be measured at it.
- **Standard of value** — *whose* value: an open-market buyer, a market participant, a specific
  buyer, or a statutory definition.
- **Fair market value** — price between willing, informed, unrelated parties.
- **Investment value** — value to one particular buyer, including their synergies.
- **Premise of value** — going concern, orderly liquidation, or forced liquidation.
- **Level of value** — control or minority; marketable or not.
- **DCF (discounted cash flow)** — valuing a business by the cash it will produce, discounted to
  today.
- **FCFF / unlevered free cash flow** — cash generated before paying lenders or shareholders.
- **EBIT / EBITDA** — earnings before interest and tax; and before depreciation and amortisation too.
- **WACC** — the blended cost of the company's debt and equity funding; the DCF discount rate.
- **CAPM** — the standard model for cost of equity: risk-free rate plus beta times the equity risk
  premium.
- **Beta** — how much a company's returns move with the market. **Unlevering / relevering** strips
  out and reapplies the effect of debt.
- **Equity risk premium** — the extra return investors demand for holding shares over government
  bonds.
- **Size premium / company-specific premium** — extra return demanded for smaller or riskier
  businesses.
- **Terminal value** — the value of everything beyond the forecast period. Usually most of the
  answer.
- **Gordon growth / perpetuity growth** — valuing the terminal period as a cash flow growing forever
  at rate g.
- **Exit multiple** — valuing the terminal period as a multiple of final-year earnings.
- **Enterprise value (EV)** — the value of the operating business, before financing.
- **Equity value** — what is left for shareholders after lenders are paid.
- **Net debt** — debt minus available cash. **Debt-like items** — obligations that behave like debt
  even if not called debt.
- **Restricted cash** — cash the business cannot freely use.
- **Minority interest / NCI** — the share of a subsidiary owned by others.
- **Diluted shares** — the share count including options, warrants and convertibles that would be
  exercised. **Treasury stock method** — the standard way of counting them.
- **LTM / NTM** — last twelve months / next twelve months.
- **Trading comps** — multiples from similar listed companies. **Precedent transactions** —
  multiples from similar completed deals.
- **Control premium** — the extra someone pays for control. **DLOM** — a discount because a private
  stake cannot be sold quickly. **DLOC** — a discount for not having control.
- **USPAP / SSVS / IVS** — professional valuation standards.
- **QofE** — quality of earnings: the diligence exercise that normalises reported earnings.
- **Fairness opinion** — a formal opinion that a deal's terms are fair. **ESOP** — an employee share
  ownership plan requiring periodic valuation.
