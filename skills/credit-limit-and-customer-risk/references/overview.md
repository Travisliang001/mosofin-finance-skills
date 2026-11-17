<!-- credit-limit-and-customer-risk · overview.md · read for: background — what comes from your own payment history and what must come from outside. Edit here, not in SKILL.md. -->

# Credit Limit and Customer Risk (Mosofin)

Assesses customer **creditworthiness**, recommends **credit limits**, and monitors ongoing credit risk.
Designed for credit and A/R management functions extending **trade credit** to B2B customers.

**In plain words:** every time you invoice a customer instead of taking payment up front, you are lending
them money. This skill decides how much you are willing to lend each one, on what terms, and what would
make you change your mind.

This skill is **jurisdiction-agnostic** and **industry-agnostic**.

It is **workspace-scoped**: your trading history with the customer, their current exposure, and your
concentration position come from tool calls against a company file connected to your Mosofin workspace in
this conversation, or from something you supplied by hand and that is labelled as such.

## The split that defines this skill

There are two kinds of evidence in a credit decision, and a connected workspace supplies exactly one of
them — but it happens to be the one people underuse.

**`[manual]` — information *about* the customer.** Their financial statements, their credit bureau
report, trade references from other suppliers, their ownership and management. **Your workspace holds
your books, not theirs.** Step 2's entire ratio analysis is computed on the *customer's* financials, and
none of it is readable here. This is worth being explicit about, because a connected accounting system
can create the impression that customer analysis is available when it is not.

**`[auto]` — your own experience *of* the customer**, and it is rich:

- **Payment history**: every invoice, every payment, and therefore **actual days-to-pay** and its trend
- **Current exposure**: what they owe now, and how much of it is overdue
- **Trading volume and its trajectory** — including a sudden increase, which is a monitoring trigger
- **Disputes and credit notes** issued to them
- **Write-off history** — whether this customer has been written off before
- **Whether they are also a vendor**, which changes net exposure
- **Concentration**: what share of total receivables and total revenue sits with them

**Your own payment experience is frequently a better predictor than a bureau score**, because it measures
how this customer treats *you* rather than how they treat the average creditor — and it is current
rather than lagged. It is also, in most businesses, the least systematically used input in the decision.
Lead with it.

**Mosofin is read-only.** It cannot set a limit in the accounting system, place a hold, or change terms.
Every recommendation is a *proposal* for the credit function.
