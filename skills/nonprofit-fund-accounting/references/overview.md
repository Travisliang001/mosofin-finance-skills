<!-- nonprofit-fund-accounting · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Nonprofit Fund Accounting (Mosofin)

Handles accounting for **not-for-profit organizations** under the NFP framework — **ASC 958** in US GAAP;
broadly aligned principles internationally. Tracks **net assets by donor restriction**, recognizes
**contributions and grants**, **releases restrictions** when satisfied, and produces the NFP financial
statement set **including the statement of functional expenses**.

**In plain words:** a charity's money mostly arrives with strings attached, and the accounts exist to show
whether those strings were honoured. So the statements are organised around **who restricted what** and
**what the money was spent on** — not around profit, which there isn't.

This skill is **framework-aware** — **US GAAP ASC 958** as the structural reference. **NFPs have distinct
statement names, classifications, and disclosures from for-profits; the skill applies these correctly.**

It is **workspace-scoped**: the net asset balances, the expense data by account and dimension, and the
contribution and release evidence come from tool calls against a company file connected to your Mosofin
workspace in this conversation, or from something you supplied by hand and that is labelled as such.

**Companion skills**: `grant-accounting-nonprofit-restricted-funds` covers the grant and restricted-fund
mechanics in depth; `government-fund-accounting-gasb` covers the public-sector model, which is a different
framework entirely. **Where they overlap, they agree.**

## Two structural questions, and one of them decides a required statement

**Ask both before producing anything.**

**1. Does the chart separate net asset classes?** **[auto]** to check.

> **Net assets must be split into *without donor restrictions* and *with donor restrictions*.** **If the
> chart carries a single equity or net assets account, that split cannot be produced from the ledger** —
> and neither can the roll-forward in Step 3 or the composition disclosure in Step 8. **Report it as a
> structural finding**, exactly as `grant-accounting-nonprofit-restricted-funds` does.

**2. Is *function* tracked as a dimension?** **[auto]** to check — **and this is the big one.**

> **The Statement of Functional Expenses is a required statement for all NFPs**, and it is a matrix:
> **natural classification** (salaries, rent, supplies — **which is the chart of accounts**) **×
> functional classification** (program services, management & general, fundraising — **which is a class,
> department or location dimension**).
>
> **Where the entity tags function as a dimension, the matrix is `[auto]` — one query.** A required
> statement that is usually assembled by hand in a spreadsheet becomes a read.

**But there is a near-substitute here that catches people, and it matters:**

> **A program class is not a functional classification.** Nonprofits very often use classes for **programs
> or grants** — *Youth Services*, *Foundation A Grant* — because that is what
> `grant-accounting-nonprofit-restricted-funds` needs. **Function is a different axis**: those programs are
> all *program services*, and the classes say nothing about **management & general** or **fundraising**.
>
> **Two different dimensions, and an entity may track one, both, or neither.** **Establish which before
> promising the functional matrix**, and where only programs are tracked, **say that the program column can
> be built and the M&G and fundraising split cannot.**

**Three more things the workspace contributes:**

1. **Natural classification is `[auto]`** — the chart of accounts *is* the natural axis.
2. **The release calculation is computable**, exactly as in the grant skill: **a purpose restriction is
   satisfied as qualifying costs are incurred, and the costs are readable.** Step 3's "common error" — the
   release entry nobody made — becomes detectable.
3. **The liquidity disclosure is partly computable.** **[gated]**: cash, receivables and short-term
   investments, **less amounts unavailable because they are donor-restricted** — which is the substance of
   the required disclosure.

**What stays outside:** every donor stipulation, the conditional / unconditional determination, endowment
terms, fair values for underwater testing, in-kind valuations, and **the basis on which shared costs are
allocated between functions.**

**Mosofin is read-only.** It cannot post a contribution, a release or an allocation. Every entry below is a
*proposal*.
