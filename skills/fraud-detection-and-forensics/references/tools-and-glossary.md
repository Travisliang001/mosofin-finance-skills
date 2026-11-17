<!-- fraud-detection-and-forensics · tools-and-glossary.md · read for: when you need a tool name, an argument, or a term explained. Edit here, not in SKILL.md. -->

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
| **Vendor master — names, addresses, phones, created dates** | `search_vendors` / `get_vendor` | `query`/`name`, `active_only`; `id` |
| **Employee master — names, addresses, phones, status** | `search_employees` / `get_employee` | `query`/`name`, `active_only`; `id` |
| **The disbursement population** | `search_bills` / `search_purchases` / `search_expenses` | `start_date`, `end_date` (required) |
| Payments made | `search_payments` / `search_checks` | `start_date`, `end_date` (required) |
| **Manual entries — the FS-fraud surface** | `search_journal_entries` / `get_journal_entry` | `start_date`, `end_date` (required); `id` |
| **Voids, refunds and write-offs** | `search_credit_memos` / `search_refund_receipts` | `start_date`, `end_date` (required) |
| **The full population — what Benford's needs** | `get_general_ledger` | `start_date`, `end_date`, `accounting_method`, `account` |
| **Trends, ratios and reserve movements** | `get_profit_and_loss` / `get_balance_sheet` | `start_date`, `end_date`, `summarize_column_by` |
| Customers, for skimming and lapping context | `search_customers` / `get_customer` | `query`/`name`, `active_only`; `id` |
| Legal name, currency, year-end | `get_company_info` | none (uses the connected company) |

Each tool's **own description in your Gate 2 catalog is the authority** on its arguments and failure
envelopes. Where this table and the live description disagree, the live description wins.

**There are no bank details, no payroll registers, no documents, no communications and no external
verification on this surface.**

---

## Plain-language glossary

- **Forensic accounting** — examining records for signs of impropriety, in a way that could stand up in a
  legal or insurance process.
- **Red flag / indicator** — a pattern that is *sometimes* associated with wrongdoing. **Most red flags have
  innocent explanations.**
- **Fraud triangle** — pressure, opportunity and rationalization: the three conditions usually present.
  **A framework for finding weak spots, not for profiling people.**
- **Asset misappropriation** — theft from the business. **Skimming** — taking receipts before they are
  recorded. **Fraudulent disbursement** — making the business pay for something it should not.
- **Financial statement fraud** — manipulating reported results rather than taking assets.
- **Corruption** — bribery, kickbacks, undisclosed conflicts of interest.
- **Ghost employee** — someone on the payroll who does not work there.
- **Fictitious vendor** — a supplier that does not exist, invoicing for nothing.
- **Lapping** — hiding a stolen receipt by covering it with the next customer's payment.
- **Benford's Law** — in many real datasets, the digit 1 leads about 30% of numbers and 9 about 5%. Made-up
  numbers often do not follow this. **A screen, never proof.**
- **Chain of custody** — the documented handling of evidence that keeps it admissible.
- **Tipping off** — alerting someone that they are being looked at, which can lead to destroyed evidence.
- **Privilege** — legal protection for communications directed by counsel.
- **Management override** — senior people bypassing the controls that constrain everyone else.
- **Collusion** — two or more people cooperating, which defeats segregation of duties.
- **CFE (Certified Fraud Examiner)** — a qualified fraud investigation professional.
- **Segregation of duties** — splitting a process so no one person controls it end to end.
- **False positive** — a flagged item with an innocent explanation. **In wide screens, most of them.**
