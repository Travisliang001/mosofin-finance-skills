<!-- bank-fee-and-interest-analysis · overview.md · read for: background — what the books can show about bank fees and what only the statement can. Edit here, not in SKILL.md. -->

# Bank Fee and Interest Analysis (Mosofin)

Analyzes bank charges and credits over time, categorizes them, ties them to **general ledger
(GL)** postings, and provides actions to reduce costs and improve coding accuracy.

**In plain words:** banks charge for a great many small things — keeping the account open,
sending each wire, handling cash, processing each card payment — and those charges are easy to
stop noticing. This skill gathers them all up, sorts them into categories, checks they were
recorded correctly, works out what you are paying *per transaction*, and identifies where the
cost can come down.

It is **workspace-scoped**: every fee, balance, and account name comes from a tool call against
a company file connected to your Mosofin workspace in this conversation, or from something you
supplied by hand and that is labelled as such.

**The central limitation of this skill in a Mosofin workspace, stated first because it changes
what the answer means.** Mosofin connects the **accounting system**, not the bank. It reads fees
that have been **posted to the books**. It cannot read a bank statement, a bank's fee analysis
statement, or a merchant processor's settlement report unless that processor is itself a
connected datasource.

That produces a specific and important blind spot:

> **The fees you are missing are, by definition, the ones that are not in the books.** A fee
> silently netted out of a deposit, or debited and never coded, is exactly what Step 3 exists to
> catch — and it is exactly what a GL-only analysis cannot see directly. **A GL-only fee analysis
> systematically under-reports total bank cost.** Say so on the face of the output. Never present
> a total from the books as "total bank fees" without that qualification.

What the connected books *can* do here is genuinely valuable, and worth being equally clear
about:

- **Analyse and categorise every fee that *was* posted** — fully supported.
- **Compute unit rates against real transaction volumes** — how many wires, ACH payments,
  deposits and card transactions actually occurred is readable, which supplies the *denominator*
  that makes "cost per wire" meaningful. This is often better data than the bank's own summary.
- **Find miscodings** — fees posted to the wrong account or dimension.
- **Detect probable netting indirectly** — where a deposit's total is less than the receipts it
  covers, a fee was almost certainly deducted. That is a strong signal even without the
  statement.

**Mosofin is read-only.** It cannot post an entry, recode a transaction, close an account, or
renegotiate anything. Every entry and recommendation below is a *proposal* for a human.
