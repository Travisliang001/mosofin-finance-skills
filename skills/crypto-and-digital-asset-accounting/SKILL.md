---
name: crypto-and-digital-asset-accounting
description: "Accounts for cryptocurrencies and other digital assets: sweeps the books for payments to exchanges that point to holdings not on the list, classifies each asset under the framework, measures it initially and afterwards, recognises purchases, sales, rewards and payments, considers custody and control, tests impairment where the cost model applies, and prepares disclosures. Reads the cash side through a connected Mosofin workspace when the user agrees, or works from uploaded wallet and exchange records. Use when the user asks about accounting for bitcoin or other crypto, digital asset fair value, staking or mining rewards, crypto received as payment, cost basis on disposal, or stablecoins. Do not use for foreign currency balances (use multicurrency-fx-revaluation) or for tax treatment. Read-only: produces the schedules and proposed entries, and never supplies a price."
---

# Digital assets: not cash, not a share, not inventory

Crypto sits awkwardly in accounting, and the rules have been changing. Whether it is carried at
**cost or at fair value**, and where gains and losses go, depends on the framework, the asset and
why it is held. This skill classifies the holdings, measures them, records the transactions and
proposes the entries.

**Works with or without Mosofin.** With Mosofin connected it reads the cash side of every purchase
and sale, and sweeps for **payments to exchanges with no holding recorded**. Without it, you
upload the wallet and exchange records and the method is the same.

**The books see the cash leg, not the crypto leg.** Quantities, lots, prices from a principal
market and custody arrangements come from you. And the standard in force at the reporting date is
confirmed with you, never asserted from memory. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** Every entry is a proposal for a
  person to post.
- **Never supplies a price.** It asks for the value, the venue and the time.
- **Never asserts which standard applies without the user confirming it for the reporting date.**
- **Never picks the cost basis method on a disposal.**
- **Gives no tax treatment.**

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–9" always mean the steps in `references/method.md`.*

Before reading any data, collect the basics in **one short batch**, not one question at a time.
Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which company and reporting date, and US GAAP or IFRS?* | Decides the measurement model | **Never default the date.** |
| **C** | *What is held and transacted: asset, quantity, dates, and in which wallet or exchange?* | The holdings are not in the books | Run the completeness sweep only, and list what it found as leads. |
| **D** | *Why is it held: investment, payment, trading, or something else?* | Drives classification | **Ask again.** |
| **E** | *What are the fair values at the relevant dates, from which market?* | Never supplied here | **Blocking** for fair-value measurement. |
| **F** | *How is it held in custody, and which cost basis method applies on disposal?* | Custody decides whether there is an asset at all | List custody as not confirmed, and compute no gain or loss on disposals. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Report payments to and receipts from exchanges and wallet providers, with amounts.
- Say which entity owns which wallet.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Wallet and exchange records**: holdings and transactions | Required | CSV |
| **Fair values** at the relevant dates, with venue | Required | XLSX, or type it in the chat |
| **Ledger detail** for the digital asset and related accounts | Recommended | XLSX or CSV |

**Read back before starting, then wait for a yes:**

> *Accounting for **bitcoin and one stablecoin** held by **Northbrook Trading** at **31 December**
> under **US GAAP**, from **the exchange export you uploaded** and the cash side in **your Mosofin
> connection**. Held as an **investment**, in **exchange custody**; prices from **the exchange's
> closing price**; disposals on **FIFO**. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the asset, the
quantity and the dates. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, and read the company profile, so Stage 1's
answers do not need asking twice. On the upload path, go straight to Stage 3.

## Stage 3 — Read the cash side and sweep for holdings

Pull the cash legs, run the completeness sweep, then classify each asset:
[`references/method.md`](references/method.md) Steps 0–1, including Step 0b.

## Stage 4 — Measure and recognise

Initial and subsequent measurement, the transactions, and custody and control:
[`references/method.md`](references/method.md) Steps 2–5. Check
[`references/edge-cases.md`](references/edge-cases.md) for stablecoins, forks and airdrops, lost
or stolen assets, and the price source.

## Stage 5 — Impairment, disclosures, and present

Impairment where the cost model applies, the disclosures, then the output:
[`references/method.md`](references/method.md) Steps 6–8. Before presenting, check it against
[`references/output.md`](references/output.md). Ask whether the user wants the workpaper as an
Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 9. Persist the classification, the cost basis
method and the price source. Holdings and prices are supplied again each period.

---

## Files

| File | Read when |
|---|---|
| [`references/mosofin-protocol.md`](references/mosofin-protocol.md) | Before the first tool call |
| [`references/gates.md`](references/gates.md) | Stage 2, Mosofin path |
| [`references/method.md`](references/method.md) | Stages 3–6 |
| [`references/edge-cases.md`](references/edge-cases.md) | Stage 4, and whenever something looks unusual |
| [`references/output.md`](references/output.md) | Before presenting |
| [`references/overview.md`](references/overview.md) | Background, or when a user asks why |
| [`references/tools-and-glossary.md`](references/tools-and-glossary.md) | When you need a tool name or a term |
