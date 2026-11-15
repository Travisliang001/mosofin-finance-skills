<!-- management-discussion-and-analysis · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Management's Discussion and Analysis (Mosofin)

Drafts the **MD&A narrative** — management's explanation of **financial condition, results of operations,
and liquidity**. **Grounds every statement in the entity's actual financial data and avoids boilerplate.**

**In plain words:** the statements say what happened. The MD&A says why, what it means, and what management
expects next — in management's own voice, to people who will make decisions with it.

**This skill produces a draft for management review. MD&A is management's own narrative and carries legal
weight** — especially for public filers. **Claude drafts from the data and flags forward-looking statements
and areas needing management and legal sign-off.**

It is **workspace-scoped**: every figure, every variance and every tie-out comes from tool calls against a
company file connected to your Mosofin workspace in this conversation, or from something you supplied by
hand and that is labelled as such.

## The defining tension — and it is written into the original's own example

Step 3 contrasts two sentences:

> **Bad**: *"Revenue increased $2M, from $10M to $12M, an increase of 20%."*
>
> **Good**: *"Revenue increased $2.0 million, or 20%, to $12.0 million. The increase was driven primarily by
> volume growth in X product line of $1.5M from N new customers and price increases of $0.7M, partially
> offset by unfavorable foreign currency translation of $0.2M."*

**The "bad" version is entirely `[auto]`. The "good" version is mostly not.** The workspace supplies **the
what** — every number, every movement, every percentage, exactly — **and almost never the why.** Drivers
live in commercial decisions, market conditions and management's knowledge of its own business.

> **That gap is the skill.** An MD&A written only from what the ledger can prove is the "bad" version at
> length. **The workspace's job here is to make the arithmetic irrefutable and the drivers easy to attach**
> — not to supply the drivers.

**With one important exception, and it is the driver that matters most:**

> **Price, volume and mix on revenue are decomposable from invoice line detail.** **[gated]**: where lines
> carry quantities and unit prices, **the revenue bridge can be computed** — how much of the movement came
> from selling more, how much from charging more, and how much from a change in what was sold. **That is a
> genuine, evidenced driver for the largest line in the statement**, and it turns the single most important
> sentence in the MD&A from an assertion into a calculation.

**Three more things the workspace contributes:**

1. **The tie-out is native.** Sheet 2 asks that **every figure cited be traced to its source.** **That is
   what a tool call is** — record the call, the parameters and the as-at date beside each figure, and the
   grounding workpaper writes itself.
2. **New versus existing customers is `[auto]`** — a real driver, and one management often asserts without
   measuring.
3. **Critical estimates are scopeable.** Step 6 asks which estimates matter most here; **the balance sheet
   answers half of that** — which reserves, allowances and judgment-heavy balances actually exist and how
   large they are.

**And a hard boundary:**

> **Never generate guidance, and never author a forward-looking statement.** The original says it plainly:
> *"Claude drafts based on management's stated expectations — it doesn't generate guidance
> independently."* **A plausible-sounding forecast in an MD&A is a legal exposure**, and a drafting tool is
> exactly where one would appear. **Every forward-looking statement in the draft must trace to something
> management said**, and every one goes in the Sheet 4 log for safe-harbour and legal review.

**Mosofin is read-only, and this skill writes nothing back — but the deeper point is that the narrative is
not ours.** Deliver a draft, marked as a draft, with the ungrounded assertions visible.
