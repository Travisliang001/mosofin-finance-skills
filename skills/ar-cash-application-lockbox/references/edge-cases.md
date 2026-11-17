<!-- ar-cash-application-lockbox · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

*The original did not carry an Edge Cases section; these are Mosofin additions plus the hazards
implicit in the steps above.*

**The bank / lockbox file was never supplied** — the Step 5 tie-out cannot be done. Report it as
**not done**, not as passed. A book-to-book tie is not a bank tie.

**A book-to-book tie is presented as a bank reconciliation** — it is not. Recorded deposits are
what someone entered, not what the bank received. Use `bank-reconciliation` for the real check.

**Two open invoices at the same amount** — an exact-amount match is no longer unambiguous. Drop
to the research queue or present both options; do not pick one silently.

**Several invoice combinations sum to the receipt total** — report the combination you chose and
say another was possible. This is where level-3 matching quietly goes wrong.

**A fuzzy match was auto-accepted** — never do this. Present it with its reason and confidence
and let a human decide. A wrongly applied receipt makes one customer look paid and another look
delinquent.

**A short-pay matches an outstanding credit memo** — it is not a deduction. Check credits before
opening a case or writing anything off.

**An overpay is actually a duplicate payment** — a customer paying the same invoice twice looks
identical to one overpaying once. Check for a matching earlier receipt before proposing a
credit.

**The payer name differs from the customer name** — a parent company, a factoring agent, or a
payment platform paying on the customer's behalf. This is the main cause of unapplied cash;
resolve it into the payer-alias map rather than re-solving it every month.

**Unapplied cash is ageing** — it overstates the receivable, damages the customer's apparent
payment record, and often hides a dispute. Age it and escalate it explicitly; do not let it sit.

**A receipt is net of processor fees** — the deposit will not equal the invoice. Record the
gross receipt and the fee separately; netting them hides the cost and breaks the tie-out.

**A company file is connected but not active** — *Mosofin-specific*. Name it as excluded and say
whose receipts are therefore unexamined. Surface any `reconnect_url`.

**A result comes back with `mock: true`** — *Mosofin-specific*. Fixture data can demonstrate the
matching logic but must never drive a real application or write-off.

**The receipt is already recorded and applied** — *Mosofin-specific*. This becomes a **review**
of how it was applied, not a proposal to apply it. Say which of the two you did.

**A stored payer alias is wrong or stale** — *Mosofin-specific*. An alias that has changed will
misapply cash to the wrong customer. Re-confirm an alias when the match it produces is
contradicted by amount or timing.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag
it. Never apply it to a different entity; never drop it silently.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
