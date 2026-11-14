<!-- audit-prep-pbc-list · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**First-time audit**: more extensive — **opening balances need support**, and there is no
prior-year baseline. Expect more requests and allow more time. *Mosofin note*: opening balances
often predate the connected books entirely, so they are frequently `[manual]` however good the
current-year coverage is. Check the earliest date the connector actually returns before
promising an opening-balance schedule.

**Auditor's PBC list provided**: map their requests to your readiness; **their list governs**,
but anticipate follow-ups beyond it. Do not replace their item names with your own — the
auditor tracks against their wording.

**Tight reporting deadline**: prioritize material and high-risk areas; sequence to deliver
foundational items first so fieldwork can begin.

**Weak monthly close**: if reconciliations aren't done monthly, audit prep becomes a scramble.
Flag the underlying close weakness (`month-end-close-checklist`) — **good close discipline is
the best audit prep.** *Mosofin note*: this is directly detectable — if the balance-sheet
accounts show no reconciling activity month to month, say so.

**Judgmental / estimate-heavy entity**: invest in robust memos; these areas drive most audit
effort and adjustments.

**Confirmations**: auditors initiate confirmations (banks, A/R, debt, legal) — **the client
provides contact details and authorization, not the confirmation itself**. Prepare the support.
*Mosofin note*: Mosofin can list the accounts, customers and lenders needing confirmation
(**[auto]**) but can neither send nor receive one, and must never present a book balance as a
confirmed balance.

**Related party completeness**: auditors test that **all** related parties and transactions are
identified. Prepare a complete listing; **omissions are a common finding**. *Mosofin note*: the
books do not flag related parties. A customer or vendor list is a **starting point for enquiry**,
never a related-party listing — presenting it as one would assert completeness that was never
tested.

**Going concern**: if there is any doubt, prepare management's assessment and plans proactively
— a sensitive, heavily-scrutinized area.

**Group audit / component auditors**: multi-entity audits need consolidation support and component coordination.

**Scope creep during fieldwork**: auditors request more as they find issues. A clean, tied-out
PBC reduces this; **track new requests in the same tracker** rather than in email.

**A company file is connected but not active** — *Mosofin-specific*. Name it as excluded and say
which areas are therefore unassessed. A readiness percentage computed over a partial group is
misleading. Surface any `reconnect_url`.

**A result comes back with `mock: true`** — *Mosofin-specific, and a hard stop here*. Fixture
data must never reach an auditor. Mark any such schedule "illustrative — not audit evidence".

**A schedule was produced but its provenance was not recorded** — *Mosofin-specific*. A number
nobody can reproduce is not audit-ready, however correct it is. Record tool, parameters and
timestamp for every `[auto]` schedule.

**The connected books' period does not cover the whole audit period** — *Mosofin-specific*. A
connector added mid-year cannot evidence the first half. Check the date range the data actually
covers before reporting an area ready.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag
it. Never apply it to a different component; never drop it silently.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the item as `[gated]` in the coverage sheet.
