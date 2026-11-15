<!-- ap-invoice-processing-and-3way-match · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

*The original did not carry an Edge Cases section; these are Mosofin additions plus the
hazards implicit in the steps above.*

**Only a 2-way match was possible, but the output says "3-way"** — the single most misleading
outcome this skill can produce. If no receipt evidence exists, label it a 2-way match. An
open PO is **not** evidence of receipt.

**The bill carries no PO link** — match by vendor, date, amount and description, and record
the match as **inferred**. Put inferred matches in the exception matrix for human review.

**The purchase-order tool is `disabled` in this workspace** — do not substitute a vendor spend
report. Spend shows what was billed, never what was ordered, so it cannot detect an
over-billing. Mark matching `[manual]` and ask for a PO export.

**An attachment exists, so the invoice looks approved** — an attachment listing proves a file
exists, not that anyone authorised the spend. Approvals stay `[manual]`.

**A bank-detail change request arrives mid-process** — the top payment-fraud vector. Mosofin
cannot see, verify, or change bank details. Escalate to a human, verify through a channel the
requester did not supply, and never carry bank details into an output or a stored preference.

**Duplicate entered under two vendor records** — the same invoice posted against "Acme Ltd"
and "Acme Limited" will not be caught by a vendor-plus-number test. Test on amount and date
across similar vendor names too; see `duplicate-invoice-detection`.

**A tolerance was assumed rather than confirmed** — a tolerance is policy. An assumed one
either buries the team in false exceptions or silently clears real variances. Always confirm
at Gate 3.

**A percentage tolerance with no absolute floor** — 2% of a $4 line is a gratuitous exception.
Always pair a percentage with a floor.

**The invoice population is "arriving" rather than "posted"** — Mosofin cannot read an inbound
PDF or an AP automation queue. Say which population was processed; a clean report over posted
bills says nothing about the twenty invoices still sitting in an inbox.

**A company file is connected but not active** — name it as excluded and say whose invoices
were therefore not examined. Surface any `reconnect_url`.

**A result comes back with `mock: true`** — fixture data can demonstrate the match logic but
must never clear a real invoice for payment.

**A bill is already posted and coded** — this becomes a *review* of the coding, not a proposal
to code it. Say which of the two you did; they carry different assurance.

**A stored preference names an entity that is no longer connected** — flag it. Never apply it
to a different entity; never drop it silently.

**A tool is `permission`-gated mid-run** — ask in chat, re-invoke with `approved=true` (**reads only — never for a write**) after an
explicit yes, and record the task as `[gated]` in the coverage sheet.
