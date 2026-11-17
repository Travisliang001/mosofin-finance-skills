<!-- inventory-obsolescence-and-reserve · overview.md · read for: background — what the books show about stock movement and what needs a count or a market price. Edit here, not in SKILL.md. -->

# Inventory Obsolescence and Reserve (Mosofin)

Assesses inventory for **excess, slow-moving, damaged, or obsolete** items and calculates the appropriate
**reserve or write-down** under applicable accounting guidance (US GAAP / IFRS).

**In plain words:** stock sitting on a shelf is recorded at what it cost, but some of it will never sell for
that — it is out of date, there is far too much of it, or nobody has wanted it for two years. The accounts
have to recognise that before the day someone finally throws it away.

It is **workspace-scoped**: the item list, the movement history, the selling prices and the reserve balance
come from tool calls against a company file connected to your Mosofin workspace in this conversation, or
from something you supplied by hand and that is labelled as such.

## The most computable skill in the inventory family — and its two honest limits

**Nearly every input this skill needs is a movement question, and movement is readable.**

1. **Movement by item over time is `[auto]`.** Sales and issues by SKU, by month, from invoice and issue
   line detail. **This is the core input, and it is a query.**
2. **Days on hand and months of supply are `[auto]`** — arithmetic on quantity and usage rate.
3. **No-move items are `[auto]`**, and it is the single highest-value query here: **every item with no sales
   or usage in N days**, with its quantity and carrying value. One read.
4. **Selling prices are `[auto]`** from recent sales lines, the anchor for net realisable value.
5. **The reserve balance and its movements are `[auto]`**, so the roll-forward in Step 6 ties to the ledger.

**And the best of them:**

> **The reserve percentage can be derived rather than assumed.** Step 1 asks for a reserve % by bucket
> **"based on history"** — and **the history is readable**: what actually happened to the items that sat in
> each age bucket in prior periods. How much was eventually written off, how much sold at full price, how
> much sold below cost. **That converts the central assumption of the whole model from a number someone
> picked into a rate this business's own experience supports.** It is the most valuable thing the workspace
> contributes here.

**Now the two limits, because they bound everything above:**

> **First: quantity on hand does not carry an age.** Aging buckets need **receipt dates by lot**. Where the
> platform tracks lots or serial numbers, aging is `[auto]`; **where it does not, the best available proxy
> is the last purchase date — and a proxy it remains.** A fast-turning item bought last week looks new even
> if some units have been there for years. **Label the aging basis explicitly**, because a reserve model
> built on a mislabelled age is confidently wrong.
>
> **Second: no-move is not obsolete.** A slow item may be a critical spare part, a seasonal line out of
> season, a long-tail product that sells twice a year at good margin, or genuinely dead stock. **The query
> produces candidates; the business decides.** Presenting a no-move list as an obsolescence list is the
> error this skill most easily commits.

**What stays outside entirely:** the demand forecast, the write-off policy and its thresholds, **physical
condition** — damaged, expired, contaminated — and the costs to complete and sell that turn a price into
NRV.

**Mosofin is read-only.** It cannot post a reserve, a write-down or a write-off. Every entry below is a
*proposal*.
