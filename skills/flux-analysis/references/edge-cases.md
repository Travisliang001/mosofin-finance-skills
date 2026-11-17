<!-- flux-analysis · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge cases

**An account goes to nil.** A recurring cost that stops is almost always a posting that did not
happen: an unposted subscription, rent paid from another account, depreciation not run. Treat it
as timing or error, look for the posting in the next period's early days, and propose the accrual
if the charge is evidenced. Never report it as a saving.

**An account appears from nil.** Either a new activity, a reclassification out of another
account, or a mis-posting. Look for the matching drop elsewhere before calling it new.

**A reclassification between accounts.** Two accounts moving by the same amount in opposite
directions. Explain them together, as one movement; do not flag them twice.

**The comparison month is the odd one.** If last month had a one-off, this month's "decrease" is
a return to normal. Check the 13-month history before writing the explanation.

**Sign change.** An expense with a credit balance or an asset with a credit balance is a finding
whatever the amount: usually a reversal without the original, or a payment posted twice.

**Different accounting methods between periods.** A cash-basis read compared with an accrual
read produces movement in every account. Stop and re-read on one method.

**Small percentage, large amount.** A 3% change in revenue can be larger than every expense
movement. The amount threshold catches it; explain it even though the percentage looks quiet.

**Partial periods.** A comparison month with a different number of trading days, or a period
that is still open, moves everything. Say so before explaining individual accounts.

**Only a trial balance supplied.** The flux runs on accounts, but statement subtotals need the
grouping: use the account type, and say the grouping was inferred.
