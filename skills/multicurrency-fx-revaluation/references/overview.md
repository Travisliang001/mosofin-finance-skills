<!-- multicurrency-fx-revaluation · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Multicurrency FX and Revaluation (Mosofin)

Handles **foreign-currency accounting** — recording foreign-currency transactions, **revaluing monetary
balances at period-end**, distinguishing **realized vs. unrealized FX**, and **translating foreign
operations** into the presentation currency, with **CTA in OCI**.

**In plain words:** if you are owed money in a currency that is not yours, what you are owed changes value
every day even though nobody has done anything. At period end you restate what you still hold, and when it
finally settles you find out what it was really worth. That is different again from converting an entire
foreign subsidiary's accounts into the group's currency — same arithmetic, different destination.

This skill is **framework-aware** — **US GAAP ASC 830 / IFRS IAS 21**, closely aligned — and **applies to
both transaction-level FX and full translation.**

It is **workspace-scoped**: each entity's home currency, the foreign-currency balances where the platform
tags them, the recorded FX gains and losses and the CTA balance come from tool calls against a company file
connected to your Mosofin workspace in this conversation, or from something you supplied by hand and that is
labelled as such.

**Companion skill**: the foreign currency translation work covers the same standards with the emphasis on
**translation and proving CTA**. **This skill's emphasis is transaction FX and revaluation.** Where they
overlap they agree; **read that one for the CTA proof, and this one for the revaluation population.**

## The question that decides whether revaluation is possible at all

**Revaluation needs to know which balances are denominated in a foreign currency.** So:

> **Does the platform tag currency per transaction and per balance?**
>
> **Multicurrency-enabled books do**, and then **the revaluation population is `[auto]`** — every
> foreign-currency monetary balance, by currency, with its recorded rate.
>
> **Books that are not multicurrency-enabled do not.** A euro invoice raised by a sterling entity may have
> been **converted on entry and recorded only in sterling**, with the euro amount surviving in a memo field
> or nowhere at all. **In that case revaluation cannot be performed from the ledger**, because the ledger no
> longer knows which balances are foreign. **Say so plainly** and ask where the currency detail lives.

**Establish this at Gate 2, before promising a revaluation.**

**Three more things the workspace contributes:**

1. **Realized versus unrealized splits itself.** **[auto]**: **balances settled during the period produce
   realized FX; balances still open at period end produce unrealized.** The original asks for the
   distinction to be tracked; **the ledger already draws it**, in the difference between a settled
   transaction and an open one.
2. **Each entity's home currency is `[auto]`** from its profile — which tells you immediately **which
   entities need translation** and **which pairs are cross-currency**.
3. **The recorded FX gain or loss and the CTA balance are `[auto]`**, so **the entries proposed can be
   compared to what was actually posted** — and a revaluation that was supposed to run and did not is
   visible.

**And the standing rule, unchanged from every other skill in this pack that touches rates:**

> **Every FX rate is `[manual]`.** Closing, average, historical. **Never supply one from memory.** Ask for
> the table, its source and its dates. **There is no rate service on this surface.**

**Mosofin is read-only.** It cannot post a revaluation or a translation entry. Every entry below is a
*proposal*.
