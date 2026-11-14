<!-- cash-flow-statement-indirect-method · edge-cases.md · read for: Stage 3, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**Acquisition during the period**: the acquired entity's opening balances **inflate BS line items
without using operating cash.** Strip the acquisition's effect from working-capital changes; **the
net cash paid (purchase price − cash acquired) goes in investing.** *Mosofin note*: this is the
commonest reason a rebuilt statement will not tie, and it is `[manual]` — the books show the
resulting balances, not that an acquisition caused them. Ask at Gate 3 whether any occurred.

**Foreign subsidiary translation**: BS changes include translation movements that **aren't cash
flows.** Use average rates for activity, period-end for balances; **the residual goes to the
FX-effect-on-cash line.**

**Lease accounting (ASC 842 / IFRS 16)**:
- **Operating lease payments under ASC 842**: typically operating activities
- **Finance lease payments**: principal in financing, interest in operating
- **IFRS 16 (all leases on-balance)**: principal in financing, interest per the entity's interest
  policy
- **Initial recognition of ROU asset + lease liability: non-cash, disclosed separately**

**Restricted cash**: under **US GAAP (ASU 2016-18), include restricted cash in the beginning and
ending totals**; the statement explains the change in (cash + restricted cash). **IFRS may present
differently.**

**Bank overdrafts**: under **IFRS**, overdrafts repayable on demand that fluctuate as part of cash
management are **included in cash & equivalents**. Under **US GAAP**, overdrafts are typically
**financing**. *Mosofin note*: a negative cash account balance is directly visible — check for one
before assuming cash is positive.

**Capitalized interest**: interest capitalized into an asset is an **investing outflow (part of
capex), not an operating interest payment** — split it.

**Discontinued operations**: present cash flows from discontinued operations separately or disclose.
**Don't bury them in continuing-ops cash flows without disclosure.**

**Stock-based comp**: non-cash; **added back in operating.** The tax effects and any cash settlement
need careful handling.

**Deferred taxes**: deferred tax expense is **non-cash (added back)**; the **current tax actually
paid is the cash component** (in supplemental disclosure).

**Changes in non-current operating items** (e.g. long-term deferred revenue): **include in operating
working-capital changes** even though they are non-current on the BS. Classification follows the
nature of the item, not its balance-sheet position.

**Sale of an asset at a gain**: **the full proceeds go in investing; the gain is reversed out of
operating** — it is not operating cash, and the proceeds already capture the cash. Counting both
double-counts the sale.

**The platform's own cash flow report differs from the rebuild** — *Mosofin-specific*. Both may tie
to the same change in cash while classifying differently. **Explain every material difference**;
never silently adopt either version.

**The two balance sheets are at different levels of detail** — *Mosofin-specific*. If the comparative
was pulled with a different summarisation, the account changes will not map. Pull both the same way.

**A transfer between the entity's own bank accounts** — *Mosofin-specific*. It changes two cash
account balances and is **not a cash flow at all**. Identify transfers explicitly, or they appear as
an investing or financing movement that never happened.

**The general-ledger tool is `disabled`** — *Mosofin-specific*. Capex must then be solved for from
the balance-sheet change, which cannot separate it from disposals. Say the investing section is
derived rather than read, and request the supplemental detail.

**A gross draw and repayment net to zero** — *Mosofin-specific*. The balance change shows nothing;
the ledger shows two real cash flows. **Build financing from movements, never from net changes.**

**A company file is connected but not active** — *Mosofin-specific*. Name it as excluded and say
which entity's statement is therefore missing. Surface any `reconnect_url`.

**A result comes back with `mock: true`** — *Mosofin-specific*. A cash flow statement is a published
financial statement. Fixture data cannot support it.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it.
Never apply one entity's classification map to another; never drop it silently.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
