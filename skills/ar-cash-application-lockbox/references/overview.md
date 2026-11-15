<!-- ar-cash-application-lockbox · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# AR Cash Application (Lockbox / Remittance) — Mosofin

Applies customer receipts to open invoices, manages **deductions / short-pays**, and keeps
**accounts receivable (A/R)** aligned with the bank.

**In plain words:** money arrives from customers — by bank transfer, card, or a batch of
cheques collected at a **lockbox** (a bank service that receives and banks your customer
payments for you). Someone then has to work out *which invoices each payment was meant to
settle*. That is **cash application**. When a customer pays less than the invoice, you have to
decide whether that shortfall is a mistake, a dispute, or an agreed reduction. When you cannot
tell who a payment came from at all, it sits in **unapplied cash** until someone works it out.

It is **workspace-scoped**: every invoice, payment, customer and account name comes from a
tool call against a company file connected to your Mosofin workspace in this conversation, or
from something you supplied by hand and that is labelled as such.

**One structural limit, stated up front, because it shapes most of the verdicts below.**
Mosofin connects the **accounting system**. It can read a payment once it has been *recorded
in the books*. It cannot read:

- a **lockbox file** or bank download,
- a **bank statement**,
- a **remittance advice** arriving by email, EDI or PDF,
- a card processor's settlement report unless that processor is itself a connected datasource.

So the honest shape of this skill in a Mosofin workspace is:

- **Reviewing** how receipts already recorded were applied — fully supported.
- **Finding** unapplied cash, open invoices, short-pays and overpays — fully supported.
- **Proposing** matches between recorded receipts and open invoices — fully supported.
- **Intaking** raw bank or lockbox data, and **tying to the bank** — `[manual]` unless the
  user supplies the file or a banking datasource is connected.

Say which of those you are doing. "All receipts matched" over a population that never included
the bank file is a much weaker statement than it sounds.

**Mosofin is read-only.** It cannot apply a payment, create a credit, post a write-off, open a
deduction case, or move anything out of unapplied cash. Every match below is a *proposal* for a
human to review and post.
