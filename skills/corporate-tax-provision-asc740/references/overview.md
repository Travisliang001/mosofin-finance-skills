<!-- corporate-tax-provision-asc740 · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Corporate Tax Provision (ASC 740 / IAS 12) — Mosofin

Computes the corporate **income tax provision for financial statement purposes** — current tax,
deferred tax, valuation allowances, uncertain tax positions, and the **effective tax rate
reconciliation**. This is the financial-reporting tax number (the book provision), distinct from the
tax return (`tax-return-prep-corporate`), though the two connect.

**In plain words:** the tax charge in your accounts is not the cheque you write to the tax authority.
Accounting rules and tax rules disagree about *when* things count, so the accounts carry two numbers:
the tax owed on this year's taxable profit (**current tax**), and the tax effect of all those timing
disagreements that will unwind in future years (**deferred tax**). This skill computes both, explains
why the resulting rate differs from the headline statutory rate, and produces the note.

This skill is **framework-aware** (US GAAP **ASC 740** / IFRS **IAS 12**) and does **not hardcode tax
rates** — statutory rates are inputs confirmed for the entity's jurisdiction(s) and year.

It is **workspace-scoped**: pre-tax income, account balances and the loss history come from tool calls
against a company file connected to your Mosofin workspace in this conversation, or from something you
supplied by hand and that is labelled as such.

## How a connected workspace changes this skill

**The no-hardcoded-rates rule is structurally enforced.** The original insists that statutory and
enacted future rates are inputs, never assumptions. Mosofin's grounding rule says the same thing, and
there is no tax-rate datasource — so **every rate must be supplied with its source and its year, or
listed as outstanding**. A plausible rate recalled from training is exactly the failure this standard
exists to prevent.

**Three things are usefully `[auto]`:**

1. **Pre-tax book income** — the starting point, readable by period and, where entities or dimensions
   map to jurisdictions, by jurisdiction.
2. **Opening deferred tax balances and their movement** — the DTA and DTL accounts are in the ledger,
   so the roll-forward has a real opening position rather than a rekeyed one.
3. **The multi-year loss history**, which matters more than it sounds. The original says *"a recent
   history of losses is significant negative evidence"* for valuation-allowance purposes — and
   **cumulative pre-tax results over three years is a single read**. That turns the most heavily
   scrutinised judgment in this skill from an assertion into an evidenced one.

**And a useful partial:** permanent-difference *candidates* are often detectable by account — fines,
penalties, entertainment, and similar accounts whose names indicate non-deductibility. That is a
prompt list for the tax preparer, not a conclusion.

**What stays `[manual]`:** every rate, tax depreciation and other tax-basis amounts, NOLs and credit
carryforwards, uncertain tax positions, and the framework. Tax returns are not in the accounting
system, and the tax basis of an asset is not a ledger field.

**Mosofin is read-only.** Every entry below is a *proposal*, and the provision is a deliverable for
review by the tax function.
