<!-- quickbooks-ar-aging-collections · overview.md · read for: background — what was changed from the original and what was kept; read when a user asks why. Edit here, not in SKILL.md. -->

# QuickBooks A/R Aging and Collections — Mosofin Seed

Uses a connected QuickBooks Online company file as the primary data source. Pulls every supported input before asking the user for anything. Produces an evidence-backed aging and a collections plan without writing to QuickBooks and without sending a message to anybody.

This is a **seed skill**, built to be rewritten the first time it runs against a real workspace.

---

## What changed in the conversion, and what did not

Most skills in this pack were written as system-agnostic accounting procedures and had to be reconnected to a live ledger. **This one was not.** It already knew it was reading QuickBooks, already knew the reads were read-only, already tracked which fields came from the system and which from the user, and already refused to send anything. It is the closest thing in the pack to an already-Mosofin-shaped skill, and the conversion below is correspondingly narrow.

So it is worth being precise about what was wrong with it, because "not much" is not the same as "nothing," and three of the problems are exactly the ones a seed is most prone to.

**1. It had no workspace layer at all.** It went straight to "confirm company context" by asking the accounting system its own name. Under Mosofin a consultant may hold several workspaces, and a workspace may hold several company files. Confirming the company is necessary and no longer sufficient. Gate 0 comes first.

**2. It assumed QuickBooks was directly installed.** The original says "the connected QuickBooks Online MCP server" and then instructs the reader to "Call A/R Aging Detail" as though that were a tool sitting in the tool list. Under Mosofin it is not. QuickBooks is a **datasource behind the gateway**, its tools are enumerated by `get_datasource_tools`, and they are invoked through `invoke_datasource_api_tool` carrying a `data_source_id`. The data is the same; the path to it is not, and a skill that hardcodes the wrong path fails at the first call.

**3. It froze a capability snapshot into the text.** The line *"The installed A/R aging capability is accrual-basis only"* may well be true. It is still an assertion about what the connector could do on the day the file was written, baked into a document that will outlive that day. Capabilities change; policies change; a connector gains a parameter. **A seed must read its capabilities, not remember them.** That is what Gate 2 is for, and the accrual-basis constraint is re-derived there rather than asserted here.

**4. It pointed at a bundled reference for tool identity.** `references/quickbooks-mcp-readonly.md` is genuinely useful for orientation — what the QuickBooks surface generally offers, what it does not. It is **not authority on tool names or availability**. The live `get_datasource_tools` response is. Read the reference to understand the shape of the surface; read the gateway to find out what you may actually call today.

**5. It had no notion of a permission gate.** Its input plan has a binary: QuickBooks provides it, or ask the user. That is a good proto-verdict system and it is preserved below — but it collapses two different situations. A tool can be present and **require approval before each call**. The original had no way to express that, so it would have hit an `approval_required` envelope with no idea what to do with it.

**6. It had no way to get better.** It asks the user, every single run, for dispute status, credit-hold status, strategic tier, brand voice, late-fee rules, escalation policy and credit sales. Those answers do not change between Tuesdays. A collections manager asked for their escalation policy for the fourth time will stop using the tool, and they will be right to. The seed-to-evolved section at the end exists mostly for this skill.

### And what was already right, and is preserved without dilution

Several things in the original are better than the pack average and are kept verbatim in substance:

- **Two independent reports, reconciled.** Pulling Detail and Summary separately and tying them is a real control, not a formality.
- **"Do not use Get Invoices as the core population."** Because it defaults to a recent transaction window and will silently drop the oldest unpaid invoices — which are precisely the ones a collections run exists to find. This is a specific, correct, non-obvious trap and it is preserved with emphasis.
- **"Never silently force a tie."**
- **"Call the result a summary-to-detail reconciliation, not a general-ledger control-account reconciliation, unless a separate GL source was actually used."** This is the near-substitute discipline, already present, already correct. It is expanded below rather than replaced.
- **"Do not turn missing flags into negative findings."** Subtle and easy to get wrong.
- **The DSO proxy labelling rule**, and the refusal to present an approximation as the real thing.
- **`REVIEW REQUIRED - NOT SENT`** on every draft.
- **Never invent late fees, service suspension, legal escalation, or payment promises.**
- **Bankruptcy notice stops ordinary dunning. A dispute routes to resolution, not to pressure.**

---

## Related skills

| Skill | Relationship |
|---|---|
| `ar-aging-and-collections` | The system-agnostic version. Use it where the connected file is not QuickBooks, or where the data arrives as an export. |
| `customer-credit-and-collections-policy` | Where the escalation policy, credit limits and tiers come from — the inputs this skill keeps asking for. Establish them once, there. |
| `bad-debt-and-write-offs` | Where the Over-120 bucket leads. This skill deliberately does not write anything off. |
| `cash-application-and-remittance-matching` | Unapplied payments and credits — the reconciling rows this skill surfaces and then hands on. |
| `dso-and-working-capital-analysis` | The metric in depth, including the denominator problem. |
| `invoice-data-extractor` | The upstream side: what was billed, and whether it was billed correctly. |
| `revenue-recognition-asc606` | Where an invoice is not yet revenue, which changes what an overdue balance means. |
| `month-end-close-checklist` | The A/R reconciliation as a close task rather than a collections exercise. |
| `internal-audit-workpaper` | Why a customer confirmation is the only evidence that a debt is agreed, and why it is not on this surface. |
| `consolidation-and-intercompany-eliminations` | Where a group-level customer exposure view would actually have to come from. |
