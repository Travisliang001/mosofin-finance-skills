<!-- debt-and-covenant-tracking · overview.md · read for: background — why covenant definitions come from the agreement and never from the books. Edit here, not in SKILL.md. -->

# Debt and Covenant Tracking (Mosofin)

Manages the debt portfolio operationally — schedules of facilities and balances, amortization, interest
accruals, **covenant computations and compliance monitoring**, maturity profile, and reporting to lenders
and management. The discipline that prevents covenant surprises and refinancing emergencies.

**In plain words:** when you borrow money, the lender attaches promises — keep your debt below this
multiple of profits, keep your interest cover above that level, tell us within so many days. Break one
and the loan can become repayable immediately, which is how solvent businesses fail. This skill tracks
what you owe, works out where you stand against each promise, and shows how much room you have left.

This skill is **facility-and-covenant-agnostic** — covenants vary widely by agreement — and **works from
the actual loan documents, which are the source of truth.**

It is **workspace-scoped**: balances, interest, principal movements and the financial inputs to each
ratio come from tool calls against a company file connected to your Mosofin workspace in this
conversation, or from something you supplied by hand and that is labelled as such.

## The trap this skill must not fall into

The original states the central discipline plainly:

> **"A covenant computed against book numbers without the agreement's specific definitions will be wrong.
> Always work from the agreement."**

**A connected workspace supplies exactly those book numbers**, and that makes the error easy, fast and
convincing. It takes one read to produce a leverage ratio from book EBITDA and book debt. That ratio will
almost certainly differ from the covenant ratio — often materially — because **"EBITDA" in a loan
agreement is a defined term with addbacks, exclusions and caps, and "Debt" and "Cash" are defined too.**
A book-based ratio can show comfortable headroom while the covenant ratio is in breach.

**So the rule for this skill is explicit: do not compute or report a covenant ratio until the agreement's
definitions have been supplied.** Where they have not been, produce the **book components clearly
labelled as book components**, and say that they are inputs to a covenant calculation, **not** the
calculation. Never present a book ratio as a compliance position.

**With that said, what the workspace does supply is genuinely valuable:**

- **The actual debt position** — every debt account, its balance, and its movement
- **Actual principal repaid and interest charged**, period by period — which validates the amortization
  schedule against reality rather than against the schedule's own assumptions
- **The book components of every ratio** — EBITDA, interest, cash, debt — as the starting point the
  agreement's definitions then adjust
- **A completeness sweep for debt-like items** the facility inventory may have missed: finance leases,
  shareholder loans, deferred consideration, invoice financing. **Covenant definitions of "Debt" often
  capture these**, and an inventory built from the agreements alone will not include them

**Mosofin is read-only.** It cannot draw down, repay, or agree a waiver. Everything below is analysis for
a human.
