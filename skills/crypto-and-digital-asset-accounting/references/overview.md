<!-- crypto-and-digital-asset-accounting · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Crypto and Digital Asset Accounting (Mosofin)

Accounts for cryptocurrencies and other digital assets — classifying them under the applicable framework,
measuring at the right basis, recognizing transactions (purchases, sales, payment receipts, mining and
staking rewards), and disclosing them appropriately.

**In plain words:** crypto sits awkwardly in accounting because it is not cash, not a share, and not
inventory — so the rules had to be borrowed from elsewhere, and they have been changing. Whether you
carry it at what you paid or at what it is worth today, and where the gains and losses go, depends on
which framework you report under and exactly what kind of asset you hold.

This area's guidance is **rapidly evolving**. US GAAP has specific recent guidance (**ASU 2023-08**
introduced a fair-value model for certain crypto assets, replacing the prior indefinite-lived-intangible
cost-less-impairment model). IFRS does not have crypto-specific standards and applies **IAS 38**
(intangibles) or **IAS 2** (inventory) per circumstances. **Confirm the current standards and the
entity's reporting framework — do not rely on outdated guidance.** The skill structures the analysis and
flags areas requiring specialist accounting and legal / tax advice.

It is **workspace-scoped**: whatever has been recorded about digital assets, and the fiat side of every
transaction, comes from tool calls against a company file connected to your Mosofin workspace in this
conversation, or from something you supplied by hand and that is labelled as such.

## What a connected workspace can and cannot see here

**Two things are outside it entirely, and they are the two things this subject runs on:**

1. **The wallet and the chain.** Holdings, quantities, addresses, on-chain transfers, staking positions
   and NFT ownership are not in an accounting datasource. **The wallet is to this skill what the bank
   statement is to `bank-reconciliation`** — the independent record without which nothing can be
   verified.
2. **Price.** There is no market-data source. **Every fair value is `[manual]`**, sourced externally with
   its principal market and its timestamp. This is the same structural rule as in a business valuation,
   and it matters more here because prices move so much: a valuation taken from a different venue or a
   few hours apart is a materially different number.

**What is `[auto]`, and it is more useful than it first appears:**

- **What has been recorded**: the digital asset carrying value on the balance sheet, its movement, and any
  gains, losses or impairments posted
- **The fiat leg of every transaction**: cash paid to an exchange, cash received from one, fees paid —
  because those went through a bank account
- **Crypto received as customer payment**, where an invoice was settled that way
- **A completeness sweep** — see Step 0b. Cash leaving for an exchange with no corresponding asset
  recorded is a gap, and it is directly detectable

**And a discipline the original itself demands, which Mosofin's grounding rule enforces:** *"No reliance
on superseded guidance."* **Do not state the current position of ASU 2023-08 or any other standard from
memory.** Standards in this area have changed recently and may change again. Name the standard, state
that it must be confirmed as at the reporting date, and put the confirmation on the open-items sheet.

**Mosofin is read-only.** Every entry below is a *proposal* for a human.
