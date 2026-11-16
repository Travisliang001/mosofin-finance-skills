<!-- ar-deductions-and-short-pays · overview.md · read for: background — what deductions are, and why evidence decides them. Edit here, not in SKILL.md. -->

# Customer deductions and short pays (Mosofin)

A **deduction** is an amount a customer holds back from a payment and gives a reason for:
damaged goods, a shortage, a price they dispute, a promotion they are owed, freight they say is
not theirs. Retail and distribution businesses see many of them; some are fair, many are not.

**In plain words:** a customer paid less than the bill and said why. This skill checks whether
they were right, using the paperwork, and proposes what to do: give them the credit, ask them to
pay, ask for proof, or write off a small amount under policy.

**Why it matters.** Deductions sit inside receivables looking like ordinary unpaid balances.
They age quietly, and past the customer's dispute window they become hard to recover. A
business that works them monthly recovers the invalid ones; one that does not writes them off in
bulk at year end.

**What decides a deduction.** Evidence, not the reason code. A signed delivery note for the
full quantity defeats a shortage claim. A carrier's damage report supports a damage claim. A
promotion agreement supports a promotion deduction only for its dates and rate. Freight follows
the contract's terms.

**What the books hold, and what they do not.** The books hold the invoice, the payment and any
credit already issued. The **backup** (delivery notes, carrier reports, agreements) lives
elsewhere, so the decision step is manual on every path: the skill asks for the documents by
deduction.

**Mosofin is read-only.** It cannot issue a credit memo, write anything off or send a letter.
Every one below is a *proposal* for a person.

**Where it sits.** Matching full payments to invoices is cash-application. Chasing invoices that
are simply unpaid is ar-aging-and-collections. Issuing an approved credit is
credit-memo-and-refund-handler.
