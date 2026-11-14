<!-- cash-management-and-treasury · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**Multi-entity tax / transfer-pricing on pooling**: cash pooling across entities creates intercompany
loans and positions requiring **arm's-length interest** and may
have **thin-cap / withholding tax implications. Don't design pooling without tax / legal review.**

**Trapped cash**: regulatory or contractual constraints (capital requirements, currency controls,
joint-venture agreements) can prevent moving cash. **Identify and disclose; exclude from available
liquidity in policy.** *Mosofin note*: `[manual]` — a restricted account looks like any other in the
chart of accounts. Ask explicitly at Gate 3.

**Counterparty concentration**: large balances at one bank (above deposit insurance, or above
comfort) expose the entity to bank failure. **Diversify or use structures that mitigate** (sweep to
government instruments). *Mosofin note*: cannot be computed until accounts are mapped to banks.

**Money market funds**: **not always equivalent to cash** — check the type (government, prime),
gating risk, and the entity's accounting treatment.

**Business email compromise / payment fraud**: **the #1 corporate payment fraud risk.** Controls —
callback verification for new payees, positive pay, dual approval for high-value, training — are
essential. *Mosofin note*: the books can flag **a new payee paid soon after creation**; they cannot
show whether the callback happened.

**Bank fees**: an overlooked cost — **fee analysis often finds material savings.** Review
periodically; see `bank-fee-and-interest-analysis`.

**Negative interest rates / cash holding costs**: in some currencies and periods, **large balances
cost money.** Treasury policy may need to address minimising idle cash rather than maximising it.

**Sovereign / country risk**: cash in some jurisdictions carries higher transfer or stability risk.
Reflect it in counterparty and jurisdiction limits.

**Cyber / wire fraud**: large wires are targets; **ensure approval and verification procedures match
the risk.**

**Coordination across functions**: treasury intersects with A/P (timing of disbursements), A/R
(collection mechanics), tax, legal and FP&A (forecasting). **Build cross-functional alignment.**

**Controls presented as tested rather than designed** — *Mosofin-specific, and the most consequential
error available here*. Mosofin cannot see signatories, access rights or approvals. **An absence of
evidence of fraud is not evidence of control.** Head Sheet 5 "designed, not tested".

**A balance grouped by account name presented as counterparty concentration** — *Mosofin-specific*.
Two accounts at the same bank look unrelated in the chart of accounts. Map accounts to banks first,
or state that the concentration analysis is outstanding.

**A dormant account still holds a material balance** — *Mosofin-specific and a genuine find*. Zero
activity with a real balance is both an unnecessary counterparty exposure and, occasionally, cash
nobody remembered they had. Rank closure candidates by balance, not just by inactivity.

**An entity in the group has no connected company file** — *Mosofin-specific*. Its cash is invisible.
Name it as a gap; never present a group total that silently excludes it.

**A facility limit treated as liquidity** — *Mosofin-specific*. Drawn balances are readable; limits,
borrowing-base restrictions and covenants are not. Undrawn is not the same as available.

**A company file is connected but not active** — *Mosofin-specific*. Name it as excluded and say
whose accounts are therefore unmapped. Surface any `reconnect_url`.

**A result comes back with `mock: true`** — *Mosofin-specific*. Fixture data cannot support a
liquidity policy, a counterparty limit, or a decision to close an account.

**A stored account-to-bank map is stale** — *Mosofin-specific*. Accounts get opened and closed, and
banking relationships change. Re-confirm the map whenever a new cash account appears in the chart of
accounts.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it.
Never apply one entity's floor or counterparty cap to another; never drop it silently.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
