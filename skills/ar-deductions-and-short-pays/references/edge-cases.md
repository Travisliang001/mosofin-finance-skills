<!-- ar-deductions-and-short-pays · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge cases

**The same invoice deducted twice.** Two payments, each short by the same amount on the same
invoice for the same reason. The first is decided on its evidence; the second is a duplicate and
is disputed whatever the first's outcome.

**A credit memo already issued.** The customer deducted on the payment *and* has a credit memo
for the same thing. Dispute the deduction, or apply the credit memo to close it; never issue a
second credit.

**Partial evidence.** A damage report for one pallet and a deduction for three. Valid for the
evidenced part, needs backup for the rest: split the item and say so.

**A short payment with no reason.** It stays in the log and its total, mapped to
**unexplained** and decided **needs backup**: it may be a real claim or an error in the
customer's payment run. Request the reason; never assume one.

**A deduction above the write-off limit that is cheaper to drop.** The skill does not decide
that: it proposes the dispute and notes the amount and age, and the approver decides.

**An old deduction past the dispute window.** Still decided on its evidence, but marked at risk;
recovery may need the customer's goodwill. Do not change the decision because it is old.

**A promotion deducted before the promotion period.** Invalid as taken, but likely valid later:
say so, and propose holding it rather than disputing hard.

**Deductions netted into a single payment for many invoices.** Spread nothing by assumption: use
the remittance to place each deduction on its invoice, or mark the item "needs remittance".

**Retailer compliance fines** (late delivery, labelling). A separate reason class: valid only
under the retailer's vendor agreement. Ask for the agreement and the retailer's evidence.
