<!-- chart-of-accounts-designer · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Chart of Accounts Designer (Mosofin)

Designs or restructures a **chart of accounts (COA)** tailored to the entity's industry, size,
reporting needs, and accounting system. Produces a consistent, scalable COA with clear account
types, numbering, descriptions, and intended-use guidance.

**In plain words:** the chart of accounts is the set of buckets every transaction gets sorted into.
Get it right and your reports answer questions without anyone reformatting anything. Get it wrong —
too many buckets, overlapping buckets, buckets nobody remembers the purpose of — and every month-end
becomes an argument about where things go.

This skill remains **jurisdiction-agnostic**, and it **adapts to the target accounting system's
account-type taxonomy and numbering conventions** and to the entity's reporting framework (GAAP,
IFRS, or other) as stated by the user. Note the direction: the *target* system is whatever the user
names; the *source* is the connected workspace.

It is **workspace-scoped**: the existing chart of accounts, the dimensions in use, the tax codes, and
the usage behind every account come from tool calls against a company file connected to your Mosofin
workspace in this conversation, or from something you supplied by hand and that is labelled as such.

**This is one of the best-fitting skills in the pack for a connected workspace, for two reasons.**

1. **The existing COA is not an input you have to ask for — it is readable in full**, with every
   account's name, type, sub-type, active status and hierarchy.
2. **And so is the usage behind it.** This is the decisive advantage. The original's first edge case
   is *"existing COA has accumulated noise (dozens of unused accounts, duplicates, miscoded items):
   recommend cleanup"* — advice that is easy to give and hard to act on. Here you can **measure it**:
   which accounts carry transactions, how many, how much, and when they were last used. A retire list
   backed by "no activity in 24 months, balance nil" is actionable in a way that "consider cleaning
   up" never is.

A third, in multi-entity workspaces: **several charts of accounts can be compared directly**, which
is exactly what "consolidate the COA across entities" asks for.

**Mosofin is read-only.** It cannot create, rename, merge or deactivate an account, and it cannot
import anything. The COA and its import file are **deliverables**; loading them is a human action —
and a consequential one, since account changes affect historical reporting.
