<!-- grant-accounting-nonprofit-restricted-funds · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Grant Accounting — Nonprofit Restricted Funds (Mosofin)

Implements detailed **grant and restricted fund accounting**: tracking **restrictions**, **conditions**,
**allowable costs**, and required reporting.

**In plain words:** when a funder gives money for a particular purpose, it is not simply income. It comes
with strings — spend it on this, by then, and tell us how. The accounting has to keep those strings visible:
show what is still restricted, recognise it as freely usable only as the conditions are actually met, and
prove to the funder and the auditor that the money went where it was promised.

It is **workspace-scoped**: the chart of accounts, the fund and program structure, the grant-tagged
expenditure and the receipts come from tool calls against a company file connected to your Mosofin
workspace in this conversation, or from something you supplied by hand and that is labelled as such.

## Why this skill fits the workspace unusually well

Most skills in this pack need something the accounting system does not hold. **This one mostly needs
expenditure tagged by program — and nonprofits are the sector where that tagging actually exists.** Class,
program or fund tracking is not an optional nicety in a nonprofit ledger; it is how restricted funds are
administered day to day. So:

1. **Grant-tagged expenditure is `[auto]`.** Spend by grant, by category, by period — one query.
2. **Release from purpose restriction becomes computable.** This is the important one. **A purpose
   restriction is satisfied as qualifying costs are incurred**, and the costs are readable. Given the award
   and its purpose, **the release calculation follows from the ledger** rather than from a spreadsheet
   somebody maintains by hand. That converts the most error-prone monthly entry in nonprofit accounting into
   a derivation with evidence behind it.
3. **Time restrictions are `[auto]`** — they turn on dates, and dates are in the data.
4. **Overspend is `[auto]`.** Cumulative spend against the award amount, by grant and by budget category.
   **Spending past an award is a compliance failure with real consequences**, and it is a single comparison.
5. **Untagged spend is `[auto]`.** Expenditure in a grant-funded program carrying no grant tag is either a
   coding error or unrecovered cost — both worth surfacing before the funder report goes out.

**What remains firmly outside:**

- **The grant agreements.** Terms, restrictions, conditions, barriers, reporting deadlines, allowable cost
  rules, indirect cost rates — **all `[manual]`, all documents.** The ledger records the consequences of a
  grant agreement; it never records the agreement.
- **The conditional / unconditional determination**, which depends on whether the agreement contains a
  **barrier and a right of return** — a reading of terms, not of balances.
- **The grant register itself**, unless the entity maintains one inside the accounting system.

**And one warning specific to this area:** **recognising a conditional contribution as revenue before the
condition is met is the classic nonprofit misstatement.** The workspace cannot detect it, because a
prematurely recognised grant looks exactly like a properly recognised one. **Only the agreement tells you**,
which is why Step 1 comes first and is `[manual]`.

**Mosofin is read-only.** It cannot post a contribution, a release or a reclassification. Every entry below
is a *proposal*.
