<!-- income-tax-deferred-tax-rollforward · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Income Tax Deferred Tax Rollforward — ASC 740 / IAS 12 (Mosofin)

Builds and maintains a **deferred tax model** that bridges **book basis and tax basis**, calculates
**DTAs / DTLs by jurisdiction**, and **ties to the total tax provision**.

**In plain words:** the accounts and the tax return count the same things at different times. Depreciation
runs faster for tax; a bonus is an expense in the accounts before it is deductible. Those gaps unwind
eventually, and until they do, the future tax they represent sits on the balance sheet — an asset if it
will save tax later, a liability if it will cost tax later.

It is **workspace-scoped**: the trial balance, the book basis of each difference, the existing deferred
balances and the results history come from tool calls against a company file connected to your Mosofin
workspace in this conversation, or from something you supplied by hand and that is labelled as such.

## The split: book basis `[auto]`, tax basis `[manual]`

**A temporary difference is book basis minus tax basis. The workspace holds one of those two, exactly, and
the other not at all.**

- **Book basis is `[auto]`, item by item.** Accrued compensation, the bad debt allowance, the inventory
  reserve, deferred revenue, the lease liability and right-of-use asset, capitalized software, accumulated
  depreciation — **every one of them is a balance sheet account you can read.** The original's Step 1
  inventory is, on its book side, a series of queries.
- **Tax basis is `[manual]`, always.** It comes from the tax return, the tax depreciation schedule, the NOL
  workpapers. **There is no tax basis anywhere in an accounting ledger.**
- **Enacted tax rates are `[manual]`, always.** Never supply a rate from memory — see the standing rule
  about jurisdiction-specific values.

**What the workspace adds beyond the book side — three things that matter:**

1. **The cumulative-loss test is `[auto]`, and it is the heaviest single piece of evidence in the whole
   skill.** **Cumulative pre-tax results over the recent period — typically three years — is one query.**
   A cumulative loss is **objectively verifiable negative evidence** that is very difficult to overcome, and
   it drives more full valuation allowances than any other factor. **Computing it takes one read and it
   frames the entire Step 4 assessment.**
2. **The rollforward must foot to the balance sheet.** **[auto]**: the opening and closing DTA and DTL
   balances are readable, and **the deferred tax expense in the P&L is readable.** So the rollforward is not
   a free-standing schedule — **it has two independent anchors**, and if it does not tie to both, it is
   wrong.
3. **The double-count check the original asks for becomes testable.** Quality check four says *"DTAs do not
   double-count items captured elsewhere."* **[auto]**: map each inventory item to the account carrying its
   book basis. **Two items mapping to one account is a double count; an item with no account is a
   difference nobody can support.**

**Mosofin is read-only.** It cannot post a deferred tax entry, a valuation allowance or a true-up. Every
entry below is a *proposal*.
