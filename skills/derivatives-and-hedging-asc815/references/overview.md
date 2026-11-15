<!-- derivatives-and-hedging-asc815 · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Derivatives and Hedging (ASC 815 / IFRS 9) — Mosofin

Supports accounting and close procedures for **derivatives and hedging activities**, including:

- **Derivative identification and scope**
- **Hedge designation** (cash flow, fair value, net investment)
- **Documentation requirements**
- **Effectiveness assessment**
- **Fair value measurement**
- **Journal entries and disclosures**

**In plain words:** a derivative is a contract whose value depends on something else — an interest rate, an
exchange rate, a commodity price. Businesses use them to remove a risk they do not want. The accounting
problem is that the derivative gets revalued every period while the thing it protects usually does not, so
without special treatment the profit and loss account swings around for no economic reason. **Hedge
accounting** is the special treatment that lines the two up — and it is optional, heavily conditional, and
easy to lose.

It is **workspace-scoped**: recorded derivative balances, OCI movements and settlements come from tool
calls against a company file connected to your Mosofin workspace in this conversation, or from something
you supplied by hand and that is labelled as such.

## What is external here — which is most of it

This is the **most externally-dependent skill in the pack**, and it is better to say so at the outset than
to imply otherwise:

- **The contracts** — ISDAs, confirmations, notionals, terms — are documents. `[manual]`.
- **The valuations** — the counterparty's mark-to-market and the methodology behind it. `[manual]`, and no
  accounting datasource will ever produce one.
- **The market data** — discount curves, forward rates, volatilities. `[manual]`, the same structural rule
  as in a business valuation and `crypto-and-digital-asset-accounting`.
- **The hedge documentation and the effectiveness testing** — `[manual]`, and both are the substance of
  whether hedge accounting is available at all.

**What the workspace does contribute is narrow but genuinely useful, and it is mostly about catching
errors rather than producing figures:**

1. **The OCI reclassification check.** A cash flow hedge parks the effective portion in OCI and releases it
   to earnings **when the hedged item affects earnings**. Whether that release actually happened is
   **readable** from the OCI account's movement. **Amounts stranded in OCI after the hedged transaction has
   occurred is a real and common error**, and it is invisible unless someone looks.
2. **A settlement completeness sweep.** Derivatives settle in cash, and cash movements are visible. **A
   payment to or receipt from a derivative counterparty with no corresponding instrument recorded** points
   to a contract nobody told accounting about.
3. **A documentation-timing check.** Hedge accounting requires **contemporaneous designation** — you cannot
   designate a hedge after the fact. Where a derivative appears on the balance sheet before any hedge
   documentation is dated, **hedge accounting is not available for the intervening period**, and every fair
   value change in it belongs in profit and loss. This is the harshest rule in the area and the most
   expensive one to discover late.

**Mosofin is read-only.** It cannot designate a hedge, execute a trade, or value anything. Every entry
below is a *proposal* for a human.
