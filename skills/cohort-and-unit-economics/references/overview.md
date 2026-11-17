<!-- cohort-and-unit-economics · overview.md · read for: background — what the books can and cannot supply for cohort and unit economics. Edit here, not in SKILL.md. -->

# Cohort and Unit Economics (Mosofin)

Analyzes customers grouped by **acquisition cohort** to measure retention, expansion, and lifetime
value, and computes **unit economics** (CAC, LTV, payback, LTV/CAC, contribution margin). Reveals
whether the business model works **at the per-customer level** — often the truth behind aggregate
growth.

**In plain words:** total revenue going up tells you very little. What matters is whether each
customer you win is worth more than it cost to win them, and whether the customers you won last year
are still around. Grouping customers by when they arrived — a **cohort** — and watching each group
over time answers both questions, and frequently contradicts the headline growth number.

This skill is **business-model-aware** (subscription, transactional, marketplace) and **grounds every
metric in a precise definition**.

It is **workspace-scoped**: customer revenue history, acquisition dates and spend all come from tool
calls against a company file connected to your Mosofin workspace in this conversation, or from
something you supplied by hand and that is labelled as such.

**Why this skill fits a connected workspace unusually well.** Cohort analysis normally stalls on data
engineering: someone has to assemble customer-level revenue by month from a billing system, work out
when each customer started, and keep it current. **In a connected workspace that assembly is a
read.**

- **Acquisition date per customer** — derivable as the **first invoice** to that customer
- **Revenue per customer per period** — readable directly, month by month
- **Active / lapsed status** — derivable from whether a customer has transacted recently
- **Sales & marketing spend by period** — readable from the P&L, giving the CAC numerator
- **Customers acquired per period** — derivable from first-invoice dates, giving the CAC denominator
- **Gross margin** — readable at company level

So the **cohort triangle itself is `[auto]`**, which is the expensive part.

**And the two things that are not, both of which matter:**

1. **Acquisition channel is not in the accounting books.** Which customers came from paid search,
   referral, or outbound is invisible here. So **blended CAC is `[auto]` and by-channel CAC is
   `[manual]`** — and the original is emphatic that blended CAC hides bad channels. Say so rather
   than quietly presenting only the blended figure.
2. **Per-customer cost-to-serve is not directly readable.** Company-level gross margin is available
   and is a legitimate starting point, but **applying one uniform margin to every customer hides
   exactly the negative-contribution customers segment analysis exists to find.** Where cost varies
   materially by customer, that variation is `[manual]`.

**Mosofin is read-only.** It produces the analysis; acting on it is a human decision.
