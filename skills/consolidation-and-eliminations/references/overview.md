<!-- consolidation-and-eliminations · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Consolidation and Eliminations (Mosofin)

Consolidates multiple entity trial balances into **group financial statements**. Performs
**intercompany eliminations**, **currency translation**, **non-controlling interest** calculations,
and produces consolidated statements.

**In plain words:** a group of companies has to present itself to the outside world as though it were
one business. That means adding up all the entities, then removing everything they did with *each
other* — because a group cannot sell to itself, owe itself money, or make a profit on itself. What is
left is what the group did with the actual outside world.

This skill is **framework-aware** (US GAAP **ASC 810** / **IFRS 10**) and **multi-currency capable**
(**ASC 830** / **IAS 21**).

It is **workspace-scoped**: every entity trial balance, balance and intercompany figure comes from a
tool call against a company file connected to your Mosofin workspace in this conversation, or from
something you supplied by hand and that is labelled as such.

## Why this is the flagship multi-entity skill

Consolidation normally begins with a data-gathering problem: someone exports a trial balance from
each entity's system, at the right date, on the right basis, and pastes them into a spreadsheet. Every
month. **In a connected workspace, that is a set of reads** — one per entity, all as at the same date,
all on the same accounting method, all in one conversation.

Two consequences matter more than the time saved:

1. **Both sides of every intercompany relationship are visible.** Entity A's receivable from B *and*
   B's payable to A can be read and compared directly. The original's final quality standard is
   **"no unmatched intercompany amount eliminated (reconcile first)"** — normally an instruction to
   go and find out. Here you can **measure the mismatch** before deciding what to eliminate.
2. **The trial balances are internally consistent.** Pulled the same way at the same moment, they
   cannot silently differ in accounting method or cut-off — a classic source of a consolidation that
   will not balance.

**What remains `[manual]`, and it is not trivial:** ownership percentages, the group presentation
currency, **every FX rate**, acquisition-date fair values and goodwill, the framework, and the
unrealised-profit markup on intercompany inventory. There is no rate source and no cap table in an
accounting datasource.

**Mosofin is read-only.** There is usually no "group ledger" to post to in any case — consolidation
lives in a workpaper. Every elimination below is a *proposal*, and the consolidated statements are a
deliverable.
