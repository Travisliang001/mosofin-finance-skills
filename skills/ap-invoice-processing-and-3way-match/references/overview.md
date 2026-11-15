<!-- ap-invoice-processing-and-3way-match · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# AP Invoice Processing and 3-Way Match (Mosofin)

Designs and executes a robust **accounts payable (A/P)** invoice processing workflow,
including intake, validation, vendor controls, coding standards, approval routing,
**2-way / 3-way match**, and exception handling.

**In plain words:** before you pay a supplier's bill, you want three things to agree — what
you *ordered*, what you actually *received*, and what you are being *billed for*. Checking
all three against each other is a **3-way match**. Checking just the order against the bill
is a **2-way match**. Most money lost in payables is lost where those three disagree and
nobody looked.

It is **workspace-scoped**: every bill, purchase order, vendor, tax code, and account name
comes from a tool call against a company file connected to your Mosofin workspace in this
conversation, or from something you supplied by hand and that is labelled as such.

**Two structural limits, stated up front, because they shape most of the verdicts below.**

1. **Mosofin sees bills that are already in the books — not the invoices arriving in an
   inbox.** A Mosofin workspace connects the accounting system, so it can read a bill once
   someone has entered it. It cannot read a PDF in an email, an AP automation queue, or a
   scanner's output. **Step 1 intake is therefore largely `[manual]`** for invoices not yet
   posted, and fully `[auto]` for bills already recorded. Say which population you are
   working on: *invoices arriving*, or *bills already entered*. They are different jobs and
   confusing them is how a duplicate gets paid.
2. **Most accounting connectors carry orders and bills but no separate goods-receipt
   record.** That makes the third leg of a 3-way match — the receipt — the usual `[manual]`
   gap. A 2-way match is often fully automatable; a 3-way match usually is not, unless the
   workspace connects an inventory or warehouse system that records receipts.

**Mosofin is read-only.** It cannot post a bill, approve an invoice, release a payment,
change a vendor record, or update bank details. Every entry and every routing decision below
is a *proposal* for a human.
