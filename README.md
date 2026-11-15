# Mosofin Accounting Skills

Accounting agent skills that work against **your own books** — read live through the
Mosofin gateway when it is connected, and from data you supply when it is not.

> ## Works with or without a Mosofin subscription
>
> **With Mosofin connected** (`https://mcp.mosofin.com/mcp`), a skill reads your live
> accounting data: figures come from your own books, validated against the real chart
> of accounts, and most steps run automatically.
>
> **Without it, the skills still work.** No subscription, no connector, or a single
> folder copied out on its own — you are not blocked and you are not asked to buy
> anything first. The Mosofin gates are skipped and the skill asks for what each step
> needs instead: a trial balance, a statement, an export. **The accounting logic, the
> edge cases and the output standards are identical** — only where the numbers come
> from changes, and the output always says which is which.
>
> **Each skill stands on its own.** Every one carries its own gate handling, so nothing
> here depends on anything else being installed. Take a single folder, or install the
> whole set as a plugin — see **Getting started**.

---

## Getting started

**Want it to read your live books?** Steps 1-2 connect Mosofin. **Just want to use a
skill?** Skip to step 3 — it will ask you for the data it needs.

**1. Subscribe** *(optional)*. The gateway returns data only for an authenticated, subscribed account. See [Sign in and account basics](https://docs.mosofin.com/start-here/register-a-mosofin-account) and [Billing](https://docs.mosofin.com/account/billing).

**2. Connect the gateway** *(optional)*.

```bash
claude mcp add --transport http mosofin https://mcp.mosofin.com/mcp
```

On claude.ai, add it through connector settings instead. Authentication is **OAuth** —
no credentials are stored locally, and **no skill here ever asks you for a password,
token or account number.**

Full step-by-step instructions for each destination, and for connecting your books on
the source side, are at **[docs.mosofin.com](https://docs.mosofin.com)** —
[Connect MosoFin to Claude](https://docs.mosofin.com/source-and-destination/destinations/claude/connect-claude)
and [Connect QuickBooks](https://docs.mosofin.com/source-and-destination/sources/quickbooks/connect-quickbooks).
If a connection will not authenticate, see
[Common issues](https://docs.mosofin.com/source-and-destination/destinations/claude/common-issues).

**3. Install the skills.** Either as a plugin, from the MosoFin marketplace in
[MosoFin/mosofin-mcp-plugin](https://github.com/MosoFin/mosofin-mcp-plugin) — this installs
all ten and keeps them updatable:

```text
/plugin marketplace add mosofin/mosofin-mcp-plugin
/plugin install mosofin-finance@financehub
```

Or copy individual folders into `~/.claude/skills/` (all projects) or
`.claude/skills/` (one project), taking only what you want:

```bash
cp -R skills/month-end-close-checklist ~/.claude/skills/
```

**4. Run it.** The skill confirms your workspace by name and waits for an explicit yes
before reading anything.

Start with `month-end-close-checklist` — it's the hub, and it points at the others.

---

## What these skills do differently

**Every task is annotated with who does it.**

| | |
|---|---|
| `[auto]` | Read from your books, unattended |
| `[gated]` | The gateway asks your permission first |
| `[manual]` | **Not in your accounting system.** The step stays; a person does it. |

A skill never quietly drops a step it can't perform. If the evidence isn't in the
ledger — a bank statement, a physical count, a signed confirmation, a cap table — **it
says so and names who owns it.**

**Nothing is ever posted.** The gateway is read-only. Every entry, filing and
communication these skills produce is a **proposal for a person to review and act on.**

**No skill writes to any connected platform.** Not QuickBooks, not Stripe, Square,
PayPal, a bank feed, a payroll or billing system — none of them. There is no code path
that creates, edits, deletes or posts a record in a source, and none that moves data
from one platform into another.

This is enforced in two places. Every skill's **Gate 2** carries a standing guardrail:
if the tool catalogue lists a write operation, it is out of scope **even when the
policy has it enabled** — a permission to write is not an instruction to write. And
`.github/validate-skill.sh` fails any skill that omits that guardrail, names a write
tool, carries an HTTP write verb, or tells the reader to write, sync, push, post or
upload into a connected platform. A skill that does any of those cannot ship.

The one write that exists anywhere goes to **your own Mosofin workspace, never to the
books**: at the end of a run a skill may offer to save what it learned — account
mappings, tolerances, vendor and payer aliases, your naming conventions — so the next
run does not re-ask. It is proposed only after you have seen the results, requires an
explicit yes at that moment, and stores *decisions and rules*, never transaction
records or balances. Decline and nothing is written at all.

**Your permissions are read fresh every run.** No skill assumes what it could do last
time. If your access changes, its behaviour changes with it — and the coverage sheet
produced on every run records exactly what was available.

**Fixture data is always labelled.** If a response comes back as sample rather than
live data, the output says so in the filename and on the first page.

---

## The skills

**Wave 1** — the everyday AP, AR and close work:

| Skill | Automated | What it's for |
|---|---:|---|
| `journal-entry-builder` | 79% | Build and validate any journal entry against your real chart |
| `three-way-match` | 75% | PO / receipt / invoice matching across the whole population |
| `duplicate-invoice-detection` | 75% | Find duplicate payments before they go out |
| `invoice-data-extractor` | 72% | Pull structured data from supplier invoices |
| `gl-coding-assistant` | 72% | Code transactions using your own posting history |
| `expense-report-processor` | 65% | Review expense claims against policy |
| `bank-reconciliation` | 62% | Reconcile an account and explain what doesn't match |
| `month-end-close-checklist` | 61% | Run the close; scopes itself from your live chart |
| `financial-statement-builder` | 50% | Produce the statement set with its tie-outs |
| `ar-aging-and-collections` | 46% | Age receivables and prioritise collection |

**Wave 2** — the close cycle and the sub-ledgers either side of it:

| Skill | Automated | What it's for |
|---|---:|---|
| `prepaid-amortization-schedule` | 70% | Build, maintain and audit the prepaid schedule |
| `closing-entries-and-trial-balance` | 69% | Close the period and produce the post-closing TB |
| `ap-accrual-cutoff` | 67% | Goods and services received but not yet invoiced |
| `customer-invoicing` | 66% | Generate invoices with their AR, revenue and tax entries |
| `balance-sheet-reconciliations` | 63% | Tie each balance sheet account to its support |
| `cash-application` | 63% | Apply customer payments; short pays, overpays, FX |
| `ap-aging-and-payment-runs` | 62% | Age payables and propose a prioritised payment run |
| `credit-card-reconciliation` | 59% | Reconcile the card statement with receipt matching |
| `vendor-statement-reconciliation` | 59% | Tie vendor statements to the AP sub-ledger |
| `accruals-and-deferrals` | 56% | Period-end accruals and deferrals, with reversals |

**Wave 3** — payroll, entry review, forecasting and the long-lived assets:

| Skill | Automated | What it's for |
|---|---:|---|
| `payroll-journal-entry-builder` | 72% | Payroll entries with gross-to-net, employer costs and accruals |
| `payroll-clearing-reconciliation` | 71% | Itemise what is left in the payroll clearing accounts |
| `credit-memo-and-refund-handler` | 69% | Credit memos and refunds with the offsetting entry |
| `budget-vs-actual-analysis` | 69% | Variance report, favourable/unfavourable, with drivers |
| `journal-entry-review` | 67% | Risk-score a journal entry population for anomalies |
| `recurring-transaction-builder` | 64% | Design a recurring schedule, then audit whether it ran |
| `payroll-reconciliation` | 61% | Tie the payroll register to GL, bank and filings |
| `inventory-to-gl-reconciliation` | 59% | Reconcile inventory to the GL; shrinkage and cleanup |
| `cash-flow-forecast-13-week` | 58% | Weekly direct cash forecast with covenant alerts |
| `fixed-asset-register-and-depreciation` | 57% | FA register, depreciation, capitalisation and disposals |

**Wave 4** — payment processors, and the lightweight card format (also applied to `bank-reconciliation` and `three-way-match` in Wave 1):

| Skill | Automated | What it's for |
|---|---:|---|
| `merchant-and-payment-processor-rec` | 64% | Tie Stripe, Square or PayPal payouts to the books; catch revenue recorded net of fees |

**Wave 5** — analysis and reporting read straight from the books, all in the card format:

| Skill | Automated | What it's for |
|---|---:|---|
| `intercompany-reconciliation` | 68% | Match both sides of every entity pair; settlements and eliminations |
| `cash-flow-statement-indirect-method` | 63% | Statement of cash flows, tied exactly to the change in cash |
| `bank-fee-and-interest-analysis` | 63% | Categorise bank charges, cost per transaction, sized savings |
| `working-capital-optimization` | 61% | Cash conversion cycle, where cash is trapped, each lever sized |
| `kpi-dashboard-builder` | 60% | Choose, define and compute the KPIs; list what the books cannot supply |

**Wave 6** — forecasting, customer economics, credit, debt and fraud risk, all in the card format:

| Skill | Automated | What it's for |
|---|---:|---|
| `cohort-and-unit-economics` | 66% | Retention by cohort, CAC, LTV on margin, payback |
| `rolling-forecast` | 59% | Lock actuals, refresh the horizon, score the last forecast |
| `fraud-detection-and-forensics` | 56% | Red-flag tests across the population; patterns, never accusations |
| `credit-limit-and-customer-risk` | 53% | Recommend a limit and terms from your own payment experience |
| `debt-and-covenant-tracking` | 47% | Debt schedule and covenants on the agreement's own definitions |

**Wave 7** — stock, costing, credit policy, audit preparation and what-if analysis, all in the card format:

| Skill | Automated | What it's for |
|---|---:|---|
| `inventory-obsolescence-and-reserve` | 67% | Slow and obsolete stock, the value test, and the reserve |
| `customer-credit-and-collections-policy` | 67% | Design the credit rules and collections cadence on the real customer base |
| `standard-costing-and-variance-analysis` | 66% | Variances and the cost bridge; stale standard or real performance |
| `scenario-and-sensitivity-analysis` | 51% | Scenarios, tornado and breakeven, with ranges from observed history |
| `audit-prep-pbc-list` | 47% | Build the PBC list, score readiness, track owners and dates |

**Wave 8** — controls, audit, treasury, bad debt and the chart of accounts, all in the card format:

| Skill | Automated | What it's for |
|---|---:|---|
| `chart-of-accounts-designer` | 68% | Design or clean up the chart, with usage measured and old-to-new mapping |
| `bad-debt-and-write-offs` | 56% | Allowance from your own loss history; write-off candidates and entries |
| `cash-management-and-treasury` | 51% | Map every cash account; structure, liquidity and payment-control policies |
| `sox-controls-design-and-testing` | 46% | Risk and control matrix; controls tested at full population where traced |
| `internal-audit-workpaper` | 41% | Audit program, workpapers, findings and report |

**Wave 9** — the quarter and year-end closes, planning models and foreign currency, all in the card format:

| Skill | Automated | What it's for |
|---|---:|---|
| `three-statement-financial-model` | 62% | Linked income statement, balance sheet and cash flow, with drivers measured from history |
| `multicurrency-fx-revaluation` | 60% | Revalue foreign balances at period end; translation and proposed entries |
| `quarter-end-close` | 53% | The monthly close plus the quarter's own tasks, and late-posting checks |
| `year-end-close` | 51% | Annual procedures, filings, closing the year and verifying it stayed locked |
| `budget-builder` | 51% | Annual operating budget by month, every line traced to a driver |

**Wave 10** — the accounting standards: revenue, leases, intangibles, groups and equity, all in the card format:

| Skill | Automated | What it's for |
|---|---:|---|
| `intangibles-and-amortization` | 59% | Intangibles register, amortisation and what may be capitalised |
| `statement-of-equity-changes` | 58% | Roll every equity component forward, with each movement sourced |
| `lease-accounting-asc842-ifrs16` | 55% | Right-of-use asset, lease liability, schedules; finds unrecorded leases |
| `revenue-recognition-asc606` | 53% | Five-step revenue model for a contract; schedule and proposed entries |
| `consolidation-and-eliminations` | 50% | Group workpaper, eliminations and non-controlling interest |
| `foreign-currency-translation-asc830` | 50% | Translate a foreign subsidiary and prove the translation adjustment |

**Wave 11** — costing, the notes, segments and a quick working model, all in the card format:

| Skill | Automated | What it's for |
|---|---:|---|
| `cost-accounting-job-order` | 65% | Cost and margin by job; overhead applied; untagged cost shown apart |
| `model-builder-integrated-three-statement` | 61% | A working, formula-driven model from your actuals and assumptions |
| `segment-reporting` | 60% | Reportable segments, their figures, and the reconciliation to the group |
| `cost-accounting-process-costing` | 54% | Equivalent units and cost per unit by department |
| `inventory-costing-fifo-lifo-wavg` | 52% | FIFO, LIFO or weighted average; ending inventory and cost of sales |
| `notes-to-financial-statements` | 51% | Disclosure checklist and draft notes, with every gap flagged |

**Wave 12** — public reporting: filings, narrative, and the judgment-heavy disclosures, all in the card format:

| Skill | Automated | What it's for |
|---|---:|---|
| `management-discussion-and-analysis` | 60% | Draft MD&A from the figures; forward-looking statements flagged |
| `contingencies-and-litigation-asc450` | 55% | Apply management's assessment; accrual and draft disclosure |
| `restatement-and-prior-period-adjustment` | 50% | Quantify a prior-period error and lay out its correction |
| `subsequent-events-asc855` | 44% | Sweep post-period activity; classify events before issue |
| `related-party-disclosures-asc850` | 43% | Compile transactions and balances with each related party |
| `xbrl-tagging-checklist` | 39% | Tag map, extension rules and calculation checks |
| `sec-10q-10k-prep` | 37% | Close-to-file calendar, tie-outs and the disclosure checklist |

**Wave 13** — specialist technical accounting, all in the card format:

| Skill | Automated | What it's for |
|---|---:|---|
| `petty-cash-management` | 57% | Cash plus vouchers against the float; replenishment and differences |
| `gaap-vs-ifrs-conversion` | 56% | Differences for this business, quantified and reconciled |
| `pensions-and-postretirement-asc715` | 55% | From the actuary's report to roll-forwards and entries |
| `crypto-and-digital-asset-accounting` | 54% | Classify, measure and record digital assets; sweep for unlisted holdings |
| `benefits-and-401k-accounting` | 51% | Retirement match, accrued time off and unremitted contributions |
| `derivatives-and-hedging-asc815` | 47% | Instrument inventory, hedge designation checks and entries |
| `equity-compensation-accounting` | 41% | Stock compensation expense schedule from the cap table you supply |
| `esg-sustainability-reporting` | 39% | Scope, metric catalogue and data pipeline for ESG figures |

**Wave 14** — sector-specific accounting, all in the card format:

| Skill | Automated | What it's for |
|---|---:|---|
| `healthcare-revenue-cycle-accounting` | 61% | Net patient revenue and reserves; billing tied to the ledger, totals only |
| `grant-accounting-nonprofit-restricted-funds` | 56% | Each grant's restrictions, budget, allowable costs and reporting dates |
| `real-estate-and-property-accounting` | 56% | Classify and measure property; rental income and sales |
| `nonprofit-fund-accounting` | 51% | Net assets by restriction, releases and the functional expense statement |
| `insurance-accounting-overview` | 51% | Close map for premium, claims, reinsurance and commissions |
| `construction-percentage-of-completion` | 48% | Revenue over time on contracts; loss provisions and contract balances |
| `government-fund-accounting-gasb` | 46% | Fund statements, government-wide statements and the reconciliation |

**Wave 15** — skills released from review items R3 and R4, and the two that sit beside an existing skill, all in the card format:

| Skill | Automated | What it's for |
|---|---:|---|
| `quickbooks-ar-aging-collections` | 64% | Receivables ageing and collections plan for a QuickBooks Online file |
| `ar-cash-application-lockbox` | 64% | Apply a lockbox or bank file to open invoices; companion to cash-application |
| `vendor-onboarding-and-w9-tin` | 56% | Vendor master audit and tax-form validation, identifiers masked |
| `ap-invoice-processing-and-3way-match` | 52% | The whole AP invoice process; wider than three-way-match |
| `aml-kyc-procedures` | 48% | AML and KYC framework documents and review lists for the responsible officer |
| `restructuring-and-severance-asc420` | 38% | Restructuring accrual and reserve roll-forward, by cost type not by name |

**Wave 16** — tax (released from review item R2): computations for a qualified professional to review, never advice, with no rate built in, all in the card format:

| Skill | Automated | What it's for |
|---|---:|---|
| `1099-and-t4a-prep` | 58% | Who must be reported, for how much, and who has no tax form on file |
| `payroll-tax-filings` | 57% | Withheld, deposited and reported, reconciled |
| `corporate-tax-provision-asc740` | 54% | Current and deferred tax in the accounts; effective rate reconciliation |
| `income-tax-deferred-tax-rollforward` | 54% | Temporary differences and the deferred tax roll-forward |
| `tax-planning-and-projections` | 51% | Project the year's tax, payments on account and the effect of options |
| `tax-return-prep-corporate` | 50% | Book profit to taxable profit, with the workpapers |
| `r-and-d-tax-credit` | 50% | Qualifying R&D cost by project and the claim documentation |
| `sales-tax-us-multistate` | 50% | Sales by state against thresholds you supply; liability reconciled to returns |
| `vat-gst-international` | 50% | Output tax, reverse charge, input tax and the VAT account reconciliation |
| `transfer-pricing-documentation` | 50% | Map intercompany flows and assemble the documentation draft |
| `personal-tax-return-prep` | 37% | Organise and compute an individual's return; saves no personal data |

Card-format skills keep `SKILL.md` short — the rules that never bend, an intake step that
asks the basics in one message, and the stages — and move the full text into
`references/` inside the skill folder. Each stage names the file it needs. Explained for
business owners at [mosofin.github.io/mosofin-skill-explainers](https://mosofin.github.io/mosofin-skill-explainers/skills/merchant-and-payment-processor-rec/).

**Automated %** is the measured share of `[auto]` versus `[manual]` steps in each skill —
computed from the files, not estimated. **It is not a quality score.** A low percentage
usually means the work genuinely needs evidence from outside the accounting system, and
the skill tells you which parts and why.

### Dashboards

`dashboards/` holds skills whose output is an interactive HTML file rather than a written
analysis. They are a **separate genre with their own standard** — same read-only posture and
the same choice of data path, but built around a visual spec and a generator script instead of
the four-gate protocol.

| Dashboard | What it builds |
|---|---|
| [`multi-entity-forecast-dashboard`](dashboards/multi-entity-forecast-dashboard/) | A single-file cash forecast for a multi-entity group — per-entity and consolidated views, P10/P90 band, receivables detail, and a paper-style report. Reads through MosoFin when you agree, or from a CSV you upload. |

Each dashboard skill carries its own `references/` — the UI spec, both data paths, and its
method — and is checked by [`.github/validate-dashboard.sh`](.github/validate-dashboard.sh)
against the rules it sets for itself, not against the analysis-skill protocol.

**Install one dashboard without cloning the repo.** Each is self-contained, so you can pull
just that folder:

```bash
curl -sL https://github.com/MosoFin/mosofin-finance-skills/archive/refs/heads/main.tar.gz | tar -xz -C ~/.claude/skills --strip-components=2 mosofin-finance-skills-main/dashboards/multi-entity-forecast-dashboard
```

Python 3 and nothing else — the generator is standard library only. See
[`dashboards/README.md`](dashboards/README.md) for pinning a release, the `git sparse-checkout`
alternative, and a one-line check that the copy works.

---

## Validating

```bash
.github/validate-skill.sh skills
```

Dependency-free. Every skill must carry frontmatter, the four gates, verdict
annotations, a coverage sheet, a lifecycle section, **the subscription onboarding
block**, and clean tool naming with no internal identifiers leaked. Runs on every PR.
For a card-format skill the checks read `SKILL.md` and every `references/*.md` together,
and `.github/sync-shared.sh` keeps the shared blocks in `references/mosofin-protocol.md`.

---

## Docs

Product and setup documentation lives at **[docs.mosofin.com](https://docs.mosofin.com)**.
The same table appears in every skill, so it is to hand at the point you need it.

| If you need to… | Read |
|---|---|
| Do the whole setup start to finish | [Quickstart](https://docs.mosofin.com/start-here/quickstart) |
| Create an account or sign in | [Sign in and account basics](https://docs.mosofin.com/start-here/register-a-mosofin-account) |
| Create the workspace a skill will read | [Set up your first workspace](https://docs.mosofin.com/start-here/create-your-first-data-flow) |
| **Connect Mosofin to your destination** | [Destinations overview](https://docs.mosofin.com/source-and-destination/destinations) → [Claude](https://docs.mosofin.com/source-and-destination/destinations/claude) → [Connect MosoFin to Claude](https://docs.mosofin.com/source-and-destination/destinations/claude/connect-claude) |
| Connect the books themselves | [Sources overview](https://docs.mosofin.com/source-and-destination/sources) → [Connect QuickBooks](https://docs.mosofin.com/source-and-destination/sources/quickbooks/connect-quickbooks) |
| See which data and tools are exposed | [Available financial data](https://docs.mosofin.com/source-and-destination/sources/quickbooks/data-overview) · [API tools reference](https://docs.mosofin.com/source-and-destination/sources/quickbooks/api-tools) |
| Fix a connection that will not authenticate | [Common issues](https://docs.mosofin.com/source-and-destination/destinations/claude/common-issues) · [Claude FAQ](https://docs.mosofin.com/source-and-destination/destinations/claude/faq) |
| Check your subscription, seats or limits | [Billing](https://docs.mosofin.com/account/billing) · [Usage and plan limits](https://docs.mosofin.com/account/plan-limits) |
| Get a person involved | [Contact support](https://docs.mosofin.com/troubleshooting/contact-support) |

In this repo:

| | |
|---|---|
| [`deploy-queue.tsv`](deploy-queue.tsv) | Full ship order |

Related repos:

| | |
|---|---|
| [MosoFin/mosofin-mcp-plugin](https://github.com/MosoFin/mosofin-mcp-plugin) | The `financehub` marketplace that publishes these skills as the `mosofin-finance` plugin, and the `mosofin` plugin that provides the MCP connection itself |

---

## Licence

Copyright © 2026 MosoFin.

This program is free software: you can redistribute it and/or modify it under the
terms of the **GNU Affero General Public License, version 3**, as published by the
Free Software Foundation. See [LICENSE](LICENSE).

**AGPL §13 — network use.** If you modify these skills and make them available to
users over a network, you must offer those users the source of your modified version.

This licence governs the skills themselves. It does not grant access to the MosoFin
service — **running these skills against live data still requires an active MosoFin
subscription**, governed separately by the MosoFin Terms of Service.

This program is distributed in the hope that it will be useful, but **WITHOUT ANY
WARRANTY**; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.

## Support

Skills are delivered to Mosofin subscribers. For access, billing or connection issues,
contact [Mosofin support](https://docs.mosofin.com/troubleshooting/contact-support). For setup
questions start at [docs.mosofin.com](https://docs.mosofin.com). For a problem with a
skill's accounting logic, open an issue.
