<!-- bank-fee-and-interest-analysis · edge-cases.md · read for: Stage 3, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

*The original did not carry an Edge Cases section; these are Mosofin additions plus the hazards
implicit in the steps above.*

**No bank statement was supplied** — the analysis covers only posted fees. **Report "missing
postings" as not performed**, and state on the face of the output that the total understates true
bank cost. This is the default situation, not an exception, so handle it gracefully rather than
refusing.

**A fee bucket shows zero for a product the entity uses** — far more likely to mean the fee is
netted or miscoded than free. Investigate rather than reporting a zero.

**A deposit is smaller than the receipts it covers** — a fee was almost certainly netted out.
Quantify it, propose the gross-up entry, and note that revenue was understated by the same amount.

**Fees posted with a generic memo** — "bank charge" cannot be categorised from the descriptor.
Say the classification was inferred from amount and timing, and flag it for the coding-rule
recommendation in Step 5.

**A unit rate is quoted without its denominator** — meaningless and un-negotiable. Always state
the count and the period.

**One-time items left inside the trend** — a single annual charge or a one-off penalty will
distort every month-on-month comparison. Separate them explicitly.

**Interest income and interest expense netted into one account** — common in small charts of
accounts, and it hides both. Split them in the analysis and recommend separate accounts.

**Merchant fees sit with the processor, not the bank** — if a processor is connected, pull from
it; if not, this whole bucket is `[manual]` even when every bank fee is available. Say which
buckets were evidenced and which were not.

**The ECR makes a "saving" illusory** — moving cash out of an account can *increase* net fees if
the balance was earning a credit that offset them. Never recommend moving balances without the
ECR arrangement confirmed.

**A company file is connected but not active** — *Mosofin-specific*. Name it as excluded and say
whose fees are therefore unanalysed. Surface any `reconnect_url`.

**The detailed ledger tool is `disabled`** — *Mosofin-specific*. A P&L expense total cannot
support unit rates, miscoding detection, or outlier analysis. Say the analysis collapsed to a
trend of totals; do not present it as a fee analysis.

**A result comes back with `mock: true`** — *Mosofin-specific*. Fixture data must not support a
renegotiation position or a proposed entry.

**A stored contracted rate is out of date** — *Mosofin-specific*. A superseded rate sheet produces
a variance against a price nobody agreed. Record the date each rate applied from, and re-confirm
when a variance appears.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag
it. Never apply it to a different entity; never drop it silently.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
