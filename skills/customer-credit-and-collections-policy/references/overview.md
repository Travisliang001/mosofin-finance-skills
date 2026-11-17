<!-- customer-credit-and-collections-policy · overview.md · read for: background — policy as written against policy as operated. Edit here, not in SKILL.md. -->

# Customer Credit and Collections Policy (Mosofin)

Builds a comprehensive **credit risk and collections operating model** to reduce **DSO** and bad debt
while preserving customer relationships.

**In plain words:** most businesses collect money by improvisation — somebody chases whoever shouts
loudest, terms get agreed on the hoof, and nobody knows whether it is getting better or worse. A credit
and collections policy replaces that with a system: who gets credit and how much, what happens on day
15 versus day 60, who can approve an exception, and how you know it is working.

It is **workspace-scoped**: the customer base, the aging, payment behaviour and the KPI baseline come
from tool calls against a company file connected to your Mosofin workspace in this conversation, or from
something you supplied by hand and that is labelled as such.

**Related skills:** `credit-limit-and-customer-risk` decides the limit for **one customer**;
`ar-aging-and-collections` **runs** the collections cycle. **This skill designs the system both of them
operate inside.** Use it when the question is "how should we do this", not "what about this customer".

## Why a connected workspace changes a policy-design skill

Policy is judgment, so most of what follows is `[manual]`. But this skill has **two quantitative
anchors**, and both are almost entirely `[auto]`:

1. **Step 1 — segmentation.** Segmenting by *revenue*, *payment behaviour*, *disputes* and
   *concentration* is a set of queries, not a workshop. You can segment the **actual** customer base
   before writing a single policy line — and the shape of that base usually decides the policy. A book
   of ten customers needs a different model from one with four thousand.
2. **Step 6 — KPIs.** **Four of the six are directly computable** from the ledger: DSO, CEI, % current
   A/R, and bad debt %. That means you can state **the baseline before the policy exists**, which is the
   only way to know afterwards whether it worked.

**Design against the measured base, not an imagined one.** A policy written without looking is
frequently a policy for a different business — thirty-day terms for customers who have always taken
fifty-five, an escalation ladder for volumes nobody has, a credit committee for a book of twelve
accounts.

**What stays `[manual]`:** the policy itself, the roles, the approval limits, the escalation ladder,
the dispute reason codes, the outreach templates, and anything about promises customers made verbally.

**Mosofin is read-only.** It cannot set a limit, place an order hold, or send an outreach message.
Everything below is a *proposal* for a human.
