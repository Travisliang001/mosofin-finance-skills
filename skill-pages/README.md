# Mosofin finance skills: what each one does

One page per skill (116) and per n8n workflow (18). Each page says what it is for, when to use it, what it asks you, what to upload if you are not connected to Mosofin, and what you get back.

Everything here is **read-only**: it reads and analyses, and anything that would change your books comes back as a proposal for a person to approve.

**Automated** is the share of a skill's checks that run without asking you for a document when a Mosofin workspace is connected. The rest need evidence that is not in the books, such as a bank statement or a contract.

## Everyday payables, receivables and close

| Skill | What it's for | Automated |
|---|---|---:|
| [`journal-entry-builder`](journal-entry-builder.md) | Build and validate any journal entry against your real chart | 79% |
| [`duplicate-invoice-detection`](duplicate-invoice-detection.md) | Find duplicate payments before they go out | 75% |
| [`three-way-match`](three-way-match.md) | PO / receipt / invoice matching across the whole population | 75% |
| [`gl-coding-assistant`](gl-coding-assistant.md) | Code transactions using your own posting history | 72% |
| [`invoice-data-extractor`](invoice-data-extractor.md) | Pull structured data from supplier invoices | 72% |
| [`expense-report-processor`](expense-report-processor.md) | Review expense claims against policy | 65% |
| [`bank-reconciliation`](bank-reconciliation.md) | Reconcile an account and explain what doesn't match | 62% |
| [`month-end-close-checklist`](month-end-close-checklist.md) | Run the close; scopes itself from your live chart | 61% |
| [`financial-statement-builder`](financial-statement-builder.md) | Produce the statement set with its tie-outs | 50% |
| [`ar-aging-and-collections`](ar-aging-and-collections.md) | Age receivables and prioritise collection | 46% |

## The close cycle and the sub-ledgers

| Skill | What it's for | Automated |
|---|---|---:|
| [`prepaid-amortization-schedule`](prepaid-amortization-schedule.md) | Build, maintain and audit the prepaid schedule | 70% |
| [`closing-entries-and-trial-balance`](closing-entries-and-trial-balance.md) | Close the period and produce the post-closing TB | 69% |
| [`ap-accrual-cutoff`](ap-accrual-cutoff.md) | Goods and services received but not yet invoiced | 67% |
| [`customer-invoicing`](customer-invoicing.md) | Generate invoices with their AR, revenue and tax entries | 66% |
| [`balance-sheet-reconciliations`](balance-sheet-reconciliations.md) | Tie each balance sheet account to its support | 63% |
| [`cash-application`](cash-application.md) | Apply customer payments; short pays, overpays, FX | 63% |
| [`ap-aging-and-payment-runs`](ap-aging-and-payment-runs.md) | Age payables and propose a prioritised payment run | 62% |
| [`credit-card-reconciliation`](credit-card-reconciliation.md) | Reconcile the card statement with receipt matching | 59% |
| [`vendor-statement-reconciliation`](vendor-statement-reconciliation.md) | Tie vendor statements to the AP sub-ledger | 59% |
| [`accruals-and-deferrals`](accruals-and-deferrals.md) | Period-end accruals and deferrals, with reversals | 56% |

## Payroll, entry review, forecasting and fixed assets

| Skill | What it's for | Automated |
|---|---|---:|
| [`payroll-journal-entry-builder`](payroll-journal-entry-builder.md) | Payroll entries with gross-to-net, employer costs and accruals | 72% |
| [`payroll-clearing-reconciliation`](payroll-clearing-reconciliation.md) | Itemise what is left in the payroll clearing accounts | 71% |
| [`budget-vs-actual-analysis`](budget-vs-actual-analysis.md) | Variance report, favourable/unfavourable, with drivers | 69% |
| [`credit-memo-and-refund-handler`](credit-memo-and-refund-handler.md) | Credit memos and refunds with the offsetting entry | 69% |
| [`journal-entry-review`](journal-entry-review.md) | Risk-score a journal entry population for anomalies | 67% |
| [`recurring-transaction-builder`](recurring-transaction-builder.md) | Design a recurring schedule, then audit whether it ran | 64% |
| [`payroll-reconciliation`](payroll-reconciliation.md) | Tie the payroll register to GL, bank and filings | 61% |
| [`inventory-to-gl-reconciliation`](inventory-to-gl-reconciliation.md) | Reconcile inventory to the GL; shrinkage and cleanup | 59% |
| [`cash-flow-forecast-13-week`](cash-flow-forecast-13-week.md) | Weekly direct cash forecast with covenant alerts | 58% |
| [`fixed-asset-register-and-depreciation`](fixed-asset-register-and-depreciation.md) | FA register, depreciation, capitalisation and disposals | 57% |

## Payment processors

| Skill | What it's for | Automated |
|---|---|---:|
| [`merchant-and-payment-processor-rec`](merchant-and-payment-processor-rec.md) | Tie Stripe, Square or PayPal payouts to the books; catch revenue recorded net of fees | 64% |

## Analysis and reporting

| Skill | What it's for | Automated |
|---|---|---:|
| [`intercompany-reconciliation`](intercompany-reconciliation.md) | Match both sides of every entity pair; settlements and eliminations | 68% |
| [`bank-fee-and-interest-analysis`](bank-fee-and-interest-analysis.md) | Categorise bank charges, cost per transaction, sized savings | 63% |
| [`cash-flow-statement-indirect-method`](cash-flow-statement-indirect-method.md) | Statement of cash flows, tied exactly to the change in cash | 63% |
| [`working-capital-optimization`](working-capital-optimization.md) | Cash conversion cycle, where cash is trapped, each lever sized | 61% |
| [`kpi-dashboard-builder`](kpi-dashboard-builder.md) | Choose, define and compute the KPIs; list what the books cannot supply | 60% |

## Forecasting, customers, credit, debt and fraud risk

| Skill | What it's for | Automated |
|---|---|---:|
| [`cohort-and-unit-economics`](cohort-and-unit-economics.md) | Retention by cohort, CAC, LTV on margin, payback | 66% |
| [`rolling-forecast`](rolling-forecast.md) | Lock actuals, refresh the horizon, score the last forecast | 59% |
| [`fraud-detection-and-forensics`](fraud-detection-and-forensics.md) | Red-flag tests across the population; patterns, never accusations | 56% |
| [`credit-limit-and-customer-risk`](credit-limit-and-customer-risk.md) | Recommend a limit and terms from your own payment experience | 53% |
| [`debt-and-covenant-tracking`](debt-and-covenant-tracking.md) | Debt schedule and covenants on the agreement's own definitions | 47% |

## Stock, costing, credit policy and audit preparation

| Skill | What it's for | Automated |
|---|---|---:|
| [`customer-credit-and-collections-policy`](customer-credit-and-collections-policy.md) | Design the credit rules and collections cadence on the real customer base | 67% |
| [`inventory-obsolescence-and-reserve`](inventory-obsolescence-and-reserve.md) | Slow and obsolete stock, the value test, and the reserve | 67% |
| [`standard-costing-and-variance-analysis`](standard-costing-and-variance-analysis.md) | Variances and the cost bridge; stale standard or real performance | 66% |
| [`scenario-and-sensitivity-analysis`](scenario-and-sensitivity-analysis.md) | Scenarios, tornado and breakeven, with ranges from observed history | 51% |
| [`audit-prep-pbc-list`](audit-prep-pbc-list.md) | Build the PBC list, score readiness, track owners and dates | 47% |

## Controls, audit, treasury and the chart of accounts

| Skill | What it's for | Automated |
|---|---|---:|
| [`chart-of-accounts-designer`](chart-of-accounts-designer.md) | Design or clean up the chart, with usage measured and old-to-new mapping | 68% |
| [`bad-debt-and-write-offs`](bad-debt-and-write-offs.md) | Allowance from your own loss history; write-off candidates and entries | 56% |
| [`cash-management-and-treasury`](cash-management-and-treasury.md) | Map every cash account; structure, liquidity and payment-control policies | 51% |
| [`sox-controls-design-and-testing`](sox-controls-design-and-testing.md) | Risk and control matrix; controls tested at full population where traced | 46% |
| [`internal-audit-workpaper`](internal-audit-workpaper.md) | Audit program, workpapers, findings and report | 41% |

## Quarter-end and year-end close, planning and foreign currency

| Skill | What it's for | Automated |
|---|---|---:|
| [`three-statement-financial-model`](three-statement-financial-model.md) | Linked income statement, balance sheet and cash flow, with drivers measured from history | 62% |
| [`multicurrency-fx-revaluation`](multicurrency-fx-revaluation.md) | Revalue foreign balances at period end; translation and proposed entries | 60% |
| [`quarter-end-close`](quarter-end-close.md) | The monthly close plus the quarter's own tasks, and late-posting checks | 53% |
| [`budget-builder`](budget-builder.md) | Annual operating budget by month, every line traced to a driver | 51% |
| [`year-end-close`](year-end-close.md) | Annual procedures, filings, closing the year and verifying it stayed locked | 51% |

## Accounting standards

| Skill | What it's for | Automated |
|---|---|---:|
| [`intangibles-and-amortization`](intangibles-and-amortization.md) | Intangibles register, amortisation and what may be capitalised | 59% |
| [`statement-of-equity-changes`](statement-of-equity-changes.md) | Roll every equity component forward, with each movement sourced | 58% |
| [`lease-accounting-asc842-ifrs16`](lease-accounting-asc842-ifrs16.md) | Right-of-use asset, lease liability, schedules; finds unrecorded leases | 55% |
| [`revenue-recognition-asc606`](revenue-recognition-asc606.md) | Five-step revenue model for a contract; schedule and proposed entries | 53% |
| [`consolidation-and-eliminations`](consolidation-and-eliminations.md) | Group workpaper, eliminations and non-controlling interest | 50% |
| [`foreign-currency-translation-asc830`](foreign-currency-translation-asc830.md) | Translate a foreign subsidiary and prove the translation adjustment | 50% |

## Costing, notes, segments and modelling

| Skill | What it's for | Automated |
|---|---|---:|
| [`cost-accounting-job-order`](cost-accounting-job-order.md) | Cost and margin by job; overhead applied; untagged cost shown apart | 65% |
| [`model-builder-integrated-three-statement`](model-builder-integrated-three-statement.md) | A working, formula-driven model from your actuals and assumptions | 61% |
| [`segment-reporting`](segment-reporting.md) | Reportable segments, their figures, and the reconciliation to the group | 60% |
| [`cost-accounting-process-costing`](cost-accounting-process-costing.md) | Equivalent units and cost per unit by department | 54% |
| [`inventory-costing-fifo-lifo-wavg`](inventory-costing-fifo-lifo-wavg.md) | FIFO, LIFO or weighted average; ending inventory and cost of sales | 52% |
| [`notes-to-financial-statements`](notes-to-financial-statements.md) | Disclosure checklist and draft notes, with every gap flagged | 51% |

## Public reporting

| Skill | What it's for | Automated |
|---|---|---:|
| [`management-discussion-and-analysis`](management-discussion-and-analysis.md) | Draft MD&A from the figures; forward-looking statements flagged | 60% |
| [`contingencies-and-litigation-asc450`](contingencies-and-litigation-asc450.md) | Apply management's assessment; accrual and draft disclosure | 55% |
| [`restatement-and-prior-period-adjustment`](restatement-and-prior-period-adjustment.md) | Quantify a prior-period error and lay out its correction | 50% |
| [`subsequent-events-asc855`](subsequent-events-asc855.md) | Sweep post-period activity; classify events before issue | 44% |
| [`related-party-disclosures-asc850`](related-party-disclosures-asc850.md) | Compile transactions and balances with each related party | 43% |
| [`xbrl-tagging-checklist`](xbrl-tagging-checklist.md) | Tag map, extension rules and calculation checks | 39% |
| [`sec-10q-10k-prep`](sec-10q-10k-prep.md) | Close-to-file calendar, tie-outs and the disclosure checklist | 37% |

## Specialist technical accounting

| Skill | What it's for | Automated |
|---|---|---:|
| [`petty-cash-management`](petty-cash-management.md) | Cash plus vouchers against the float; replenishment and differences | 57% |
| [`gaap-vs-ifrs-conversion`](gaap-vs-ifrs-conversion.md) | Differences for this business, quantified and reconciled | 56% |
| [`pensions-and-postretirement-asc715`](pensions-and-postretirement-asc715.md) | From the actuary's report to roll-forwards and entries | 55% |
| [`crypto-and-digital-asset-accounting`](crypto-and-digital-asset-accounting.md) | Classify, measure and record digital assets; sweep for unlisted holdings | 54% |
| [`benefits-and-401k-accounting`](benefits-and-401k-accounting.md) | Retirement match, accrued time off and unremitted contributions | 51% |
| [`derivatives-and-hedging-asc815`](derivatives-and-hedging-asc815.md) | Instrument inventory, hedge designation checks and entries | 47% |
| [`equity-compensation-accounting`](equity-compensation-accounting.md) | Stock compensation expense schedule from the cap table you supply | 41% |
| [`esg-sustainability-reporting`](esg-sustainability-reporting.md) | Scope, metric catalogue and data pipeline for ESG figures | 39% |

## Sector-specific accounting

| Skill | What it's for | Automated |
|---|---|---:|
| [`healthcare-revenue-cycle-accounting`](healthcare-revenue-cycle-accounting.md) | Net patient revenue and reserves; billing tied to the ledger, totals only | 61% |
| [`grant-accounting-nonprofit-restricted-funds`](grant-accounting-nonprofit-restricted-funds.md) | Each grant's restrictions, budget, allowable costs and reporting dates | 56% |
| [`real-estate-and-property-accounting`](real-estate-and-property-accounting.md) | Classify and measure property; rental income and sales | 56% |
| [`insurance-accounting-overview`](insurance-accounting-overview.md) | Close map for premium, claims, reinsurance and commissions | 51% |
| [`nonprofit-fund-accounting`](nonprofit-fund-accounting.md) | Net assets by restriction, releases and the functional expense statement | 51% |
| [`construction-percentage-of-completion`](construction-percentage-of-completion.md) | Revenue over time on contracts; loss provisions and contract balances | 48% |
| [`government-fund-accounting-gasb`](government-fund-accounting-gasb.md) | Fund statements, government-wide statements and the reconciliation | 46% |

## Further payables, receivables and compliance skills

| Skill | What it's for | Automated |
|---|---|---:|
| [`ar-cash-application-lockbox`](ar-cash-application-lockbox.md) | Apply a lockbox or bank file to open invoices; companion to cash-application | 64% |
| [`quickbooks-ar-aging-collections`](quickbooks-ar-aging-collections.md) | Receivables ageing and collections plan for a QuickBooks Online file | 64% |
| [`vendor-onboarding-and-w9-tin`](vendor-onboarding-and-w9-tin.md) | Vendor master audit and tax-form validation, identifiers masked | 56% |
| [`ap-invoice-processing-and-3way-match`](ap-invoice-processing-and-3way-match.md) | The whole AP invoice process; wider than three-way-match | 52% |
| [`aml-kyc-procedures`](aml-kyc-procedures.md) | AML and KYC framework documents and review lists for the responsible officer | 48% |
| [`restructuring-and-severance-asc420`](restructuring-and-severance-asc420.md) | Restructuring accrual and reserve roll-forward, by cost type not by name | 38% |

## Tax, for a qualified professional to review

| Skill | What it's for | Automated |
|---|---|---:|
| [`1099-and-t4a-prep`](1099-and-t4a-prep.md) | Who must be reported, for how much, and who has no tax form on file | 58% |
| [`payroll-tax-filings`](payroll-tax-filings.md) | Withheld, deposited and reported, reconciled | 57% |
| [`corporate-tax-provision-asc740`](corporate-tax-provision-asc740.md) | Current and deferred tax in the accounts; effective rate reconciliation | 54% |
| [`income-tax-deferred-tax-rollforward`](income-tax-deferred-tax-rollforward.md) | Temporary differences and the deferred tax roll-forward | 54% |
| [`tax-planning-and-projections`](tax-planning-and-projections.md) | Project the year's tax, payments on account and the effect of options | 51% |
| [`r-and-d-tax-credit`](r-and-d-tax-credit.md) | Qualifying R&D cost by project and the claim documentation | 50% |
| [`sales-tax-us-multistate`](sales-tax-us-multistate.md) | Sales by state against thresholds you supply; liability reconciled to returns | 50% |
| [`tax-return-prep-corporate`](tax-return-prep-corporate.md) | Book profit to taxable profit, with the workpapers | 50% |
| [`transfer-pricing-documentation`](transfer-pricing-documentation.md) | Map intercompany flows and assemble the documentation draft | 50% |
| [`vat-gst-international`](vat-gst-international.md) | Output tax, reverse charge, input tax and the VAT account reconciliation | 50% |
| [`personal-tax-return-prep`](personal-tax-return-prep.md) | Organise and compute an individual's return; saves no personal data | 37% |

## Valuation and transactions, for a qualified professional to review

| Skill | What it's for | Automated |
|---|---|---:|
| [`due-diligence-quality-of-earnings`](due-diligence-quality-of-earnings.md) | Adjusted EBITDA bridge, working capital and net debt for a deal | 64% |
| [`goodwill-and-impairment-testing`](goodwill-and-impairment-testing.md) | Scope, triggers and the impairment test on your projections | 54% |
| [`valuation-agent-dcf-comps-football-field`](valuation-agent-dcf-comps-football-field.md) | DCF with visible WACC, comparable screens and a football field | 49% |
| [`business-combinations-asc805`](business-combinations-asc805.md) | Purchase accounting from the valuer's fair values; goodwill and the entry | 44% |
| [`model-auditor-financial-model-review`](model-auditor-financial-model-review.md) | Last review of a model: tie-out, formulas, issue log, pass or hold | 44% |
| [`ipo-readiness-accounting`](ipo-readiness-accounting.md) | Finance roadmap to public-company readiness, with the close measured | 41% |
| [`business-valuation`](business-valuation.md) | A value range from three approaches, and the bridge to equity | 40% |

## Movement analysis and customer deductions

| Skill | What it's for | Automated |
|---|---|---:|
| [`flux-analysis`](flux-analysis.md) | Month-on-month and year-on-year movements over two thresholds, each with a driver and evidence, and a cash proof | 78% |
| [`ar-deductions-and-short-pays`](ar-deductions-and-short-pays.md) | Customer deductions decided valid, invalid or needs backup on their evidence; credits, write-offs and disputes proposed | 62% |

## n8n workflows

Checks that run on a schedule or on demand, with every setting in one place and one result for the next tool to pick up.

| Workflow | Runs | Proposes |
|---|---|---|
| [`invoice-ingestion`](workflow-invoice-ingestion.md) | webhook | bill drafts with GL coding, new vendors |
| [`bank-reconciliation`](workflow-bank-reconciliation.md) | webhook | entries for bank-only fees and interest |
| [`three-way-match`](workflow-three-way-match.md) | webhook | holds on bills with exceptions |
| [`duplicate-invoice-detection`](workflow-duplicate-invoice-detection.md) | daily + webhook | holds on likely duplicates |
| [`ar-collections`](workflow-ar-collections.md) | weekly + webhook | one collection email draft per customer |
| [`expense-receipts`](workflow-expense-receipts.md) | webhook | reimbursement of clean lines |
| [`month-end-close-orchestrator`](workflow-month-end-close-orchestrator.md) | days 1–7 + webhook | nudges to task owners |
| [`recurring-journal-automator`](workflow-recurring-journal-automator.md) | monthly + webhook | missing recurring entries |
| [`cash-application`](workflow-cash-application.md) | webhook | payment-to-invoice applications |
| [`pbc-chase-up`](workflow-pbc-chase-up.md) | weekdays + webhook | one reminder per owner |
| [`vendor-onboarding`](workflow-vendor-onboarding.md) | webhook | vendor set-up or an information request |
| [`scheduled-financial-pack`](workflow-scheduled-financial-pack.md) | monthly + webhook | the pack, ready to deliver |
| [`gl-flux-monitor`](workflow-gl-flux-monitor.md) | monthly + webhook | explanation requests per owner |
| [`vendor-statement-reconciliation`](workflow-vendor-statement-reconciliation.md) | webhook | queries to the vendor |
| [`fixed-asset-rollforward`](workflow-fixed-asset-rollforward.md) | monthly + webhook | missing depreciation entries |
| [`inventory-obsolescence-reserve`](workflow-inventory-obsolescence-reserve.md) | quarterly + webhook | reserve adjustment entry |
| [`sales-tax-compliance-monitor`](workflow-sales-tax-compliance-monitor.md) | monthly + webhook | registration reviews |
| [`intercompany-netting-settlement`](workflow-intercompany-netting-settlement.md) | monthly + webhook | settlement payments |

[Sitemap](sitemap.md)

<!-- Generated by .github/build-pages.py. -->
