<!-- inventory-costing-fifo-lifo-wavg · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Inventory Costing — FIFO / LIFO / Weighted-Average / Specific ID (Mosofin)

Applies an **inventory costing method** to compute **ending inventory and cost of goods sold**. Builds the
**layer detail** (FIFO / LIFO), the **rolling or period averages** (weighted-average), or
**specific-identification** mapping, applies **lower-of-cost-and-NRV** (or LCM where applicable), and
produces costed inventory and COGS with **method-comparison** where useful.

**In plain words:** if you bought the same item three times at three different prices and then sold two of
them, which price was the cost of what you sold? The accounts need an answer, and there is no physically
correct one — so there are conventions. The convention chosen changes reported profit, the balance sheet,
and in some places the tax bill.

This skill is **framework-aware** — **US GAAP / IFRS, notably IFRS prohibits LIFO** — and supports
**periodic and perpetual** systems.

It is **workspace-scoped**: the purchase and sales history, the item detail, the inventory balance and the
recent selling prices come from tool calls against a company file connected to your Mosofin workspace in
this conversation, or from something you supplied by hand and that is labelled as such.

## Two structural facts to establish before costing anything

**First: the platform applies a costing method of its own, and it may not be the entity's.**

**Most commercial accounting platforms implement exactly one costing method** — usually **FIFO or
weighted-average** — and apply it automatically to every item. **Very few can maintain LIFO at all.** So:

> **If the entity reports on a method the platform does not implement, the platform's inventory value and
> COGS are not the reported figures.** The reported ones are computed in a spreadsheet outside, and **the
> ledger carries an adjustment — or, more often, nobody notices the difference.**
>
> **Establish which method the platform applies, and which method the entity reports on, before computing
> anything.** For a LIFO entity this is nearly always a divergence, and **the LIFO reserve — the difference
> between the two — is the figure that matters.**

**Second: layers are not exposed — but they can be rebuilt.**

Even a FIFO platform typically reports **quantity on hand and a total value**, not the layer stack behind
it. **So layer detail is `[manual]` as a read — and `[gated]` as a reconstruction**, because the inputs are
readable:

> **Purchases with dates, quantities and unit costs are readable. Sales with dates and quantities are
> readable.** Given both, **the layer stack can be rebuilt from transaction history** and the cost flow
> applied properly. That is real work the workspace makes possible, and it is what turns this from a
> theoretical exercise into a computable one.

**And one genuinely useful thing the workspace adds to valuation:**

> **NRV can be anchored in actual recent selling prices.** Step 5 needs estimated selling price. **What each
> item actually sold for in recent months is readable** from sales invoice lines. **An NRV built on this
> entity's own recent realised prices is far better evidence than an assumed list price** — and it takes one
> read.

**What stays outside:** costs to complete and sell, replacement cost for LCM, standard costs and variances,
consignment and FOB terms, and the physical count.

**Mosofin is read-only.** It cannot post a costing adjustment, a write-down or a COGS entry. Every entry
below is a *proposal*.
