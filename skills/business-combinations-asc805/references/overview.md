<!-- business-combinations-asc805 · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Business Combinations (ASC 805 / IFRS 3) — Mosofin

Accounts for business combinations under the **acquisition method** — identifying the acquirer,
determining the acquisition date and consideration transferred, allocating purchase price to the
identifiable assets acquired and liabilities assumed at **fair value**, recognizing **goodwill**
(or a **bargain purchase**), and handling **contingent consideration** and **measurement-period
adjustments**.

**In plain words:** when one business buys another, you cannot simply add the two sets of books
together. You have to work out what you really paid, then value everything you bought — including
things the seller never had on their balance sheet, like their customer relationships and their
brand. Whatever you paid above the value of all those identifiable things becomes **goodwill**.
Getting this allocation right matters for years afterwards, because it determines how much
amortisation hits your profits.

This skill is **framework-aware** (US GAAP **ASC 805** / **IFRS 3** — largely converged). Business
combinations involve significant valuation judgment; the skill structures the accounting and
**flags where valuation specialists are required** for fair values of intangibles and complex
consideration. **It does not fabricate fair values.**

It is **workspace-scoped**: every book value and post-acquisition result comes from a tool call
against a company file connected to your Mosofin workspace in this conversation, or from something
you supplied by hand and that is labelled as such.

**Where a connected workspace genuinely helps — and it is a narrower but sharper set than usual.**
Almost everything in this skill is judgment or specialist valuation, so most verdicts below are
`[manual]`. But three things are `[auto]`, and they happen to be among the most laborious parts:

1. **If the acquiree is itself a connected company file** — a real and increasingly common setup
   after a deal closes — **its pre-acquisition book values are directly readable**. That is the
   left-hand column of the whole purchase price allocation, and it is normally rekeyed by hand.
2. **The acquiree's revenue and earnings since the acquisition date** is a required disclosure and
   is directly readable once that entity is connected. So is the **prior-period comparative** that
   feeds the pro-forma disclosure.
3. **Testing that transaction costs were expensed, not capitalized.** Legal and advisory fees are
   visible in the ledger, and capitalising them into the acquisition is a specific, common,
   material error that this check catches.

Everything else — every fair value, the acquirer determination, the business-versus-asset screen,
the earnout valuation — is `[manual]`, and the skill's job is to structure it, not to guess it.

**Mosofin is read-only.** It cannot post the acquisition entry or consolidate anything. Every entry
below is a *proposal* for a human.
