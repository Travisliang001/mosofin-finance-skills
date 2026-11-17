<!-- bad-debt-and-write-offs · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**No historical loss data**: you cannot build a properly-supported allowance under CECL/ECL. Use
a peer / industry rate as a starting point (**the user must validate it**) and flag the
limitation. *Mosofin note*: check first — the history may be derivable from past agings and
account movement even when the user believes it does not exist.

**New entity with no A/R history**: same as above — use a management estimate with full
disclosure.

**Customer in bankruptcy with potential dividend** (creditors expected to receive some recovery):
**reserve the un-recoverable portion only.** Writing off the whole balance overstates the loss
and understates a real asset.

**Disputed receivable**: **don't write off** if the dispute is active and the entity expects to
prevail. Reserve only if it loses. A dispute is not a collectibility problem — it is a
resolution problem.

**Government / large institutional customers**: typically very low loss rates regardless of
aging — **adjust the matrix accordingly.** A 120-day balance from a government department is
usually slow, not doubtful, and applying a 50% rate to it materially misstates the allowance.

**Tax recoverability differs by jurisdiction**: **never assume** output tax can be reclaimed on a
write-off without confirming local rules and procedures.

**Multi-currency A/R**: convert at the period-end FX rate for the allowance calculation; FX
revaluation separately.

**Intercompany A/R**: usually **no allowance needed within a consolidated group**; but if a
subsidiary is insolvent, the parent's recoverability is in question. Coordinate with
consolidation. *Mosofin note*: intercompany balances often sit in the aging looking like
ordinary customers. Identify and exclude them explicitly rather than reserving against your own
group.

**Specific write-off in the current period of a receivable already fully reserved**: **net zero
P&L impact** (DR Allowance, CR A/R). Only the A/R control account moves. Do not book a second
expense — that is double-counting the same loss.

**Recovery of a previously written-off receivable in a later period**: book the recovery; **do
not reinstate the original A/R** (administratively messy).

**A company file is connected but not active** — *Mosofin-specific*. Name it as excluded and say
whose receivables are therefore unassessed. Surface any `reconnect_url`.

**The aging tool will not accept a past `report_date`** — *Mosofin-specific*. Historical loss
rates are then `[manual]`. Say so before presenting any rate as historically supported; a
plausible rate presented as a derived one is worse than an admitted estimate.

**A customer balance report is offered instead of an aging** — *Mosofin-specific*. It has no
buckets, so it cannot carry per-bucket loss rates. Reconstruct the aging from invoice-level data
and label it, or mark the task `[manual]`.

**An old balance is actually an unapplied credit or a billing error** — *Mosofin-specific and
common*. Check credit memos and unapplied cash before proposing a write-off. Writing off a
billing error records a loss that never happened and buries the underlying mistake.

**A result comes back with `mock: true`** — *Mosofin-specific*. Fixture data can demonstrate the
calculation but must never support a write-off against a named customer.

**A write-off is proposed with no approval evidence** — *Mosofin-specific emphasis*. Mosofin
cannot capture an approval. Record the write-off as pending approval, name the approver from the
authority matrix, and never present it as complete.

**A stored loss rate is being reused instead of re-derived** — *Mosofin-specific*. Rates are
state, not decisions. Persist the derivation method; re-derive the rate every period.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag
it. Never apply it to a different entity; never drop it silently.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
