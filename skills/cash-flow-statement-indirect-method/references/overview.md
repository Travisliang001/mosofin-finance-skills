<!-- cash-flow-statement-indirect-method · overview.md · read for: background — what the statement explains and what the general ledger adds over two balance sheets. Edit here, not in SKILL.md. -->

# Cash Flow Statement (Indirect Method) — Mosofin

Builds the **statement of cash flows** — operating, investing, and financing sections — primarily
using the **indirect method** (with direct-method capability). Reconciles net income to operating
cash flow and ties to the period's change in cash.

**In plain words:** the profit and loss account says you made money; the bank says otherwise. The
cash flow statement explains the difference. It starts at profit, strips out everything that never
involved money, adds back what moved in and out, and must end at exactly the change in your bank
balance. If it doesn't, it's wrong — there is no rounding here.

This skill is **framework-aware** (US GAAP **ASC 230** / IFRS **IAS 7**) and
**chart-of-accounts-agnostic**.

It is **workspace-scoped**: every balance and movement comes from a tool call against a company file
connected to your Mosofin workspace in this conversation, or from something you supplied by hand and
that is labelled as such.

**Two things about this skill in a connected workspace, both of which change the work
substantially.**

1. **The "supplemental detail" the original marks *required for accuracy* is largely `[auto]`.** The
   original notes that "the BS change alone doesn't separate capex from disposals from
   depreciation" — and that is true of balance sheets. But the **general ledger does separate
   them**: the actual movements on each fixed-asset, debt and equity account are readable line by
   line. Capex, disposal proceeds, debt draws and repayments, dividends paid — all of these can be
   read rather than solved for. That removes the single biggest source of error in this statement.
2. **The platform may already produce a cash flow report.** Where it does, read it — but **as a
   cross-check against your own build, never as a substitute for it.** Platform-generated cash flow
   statements are notoriously loose about non-cash movements, acquisitions and FX. **Where your
   rebuild and the platform's report differ, that difference is itself the finding**, and it is
   usually one of the five culprits listed at Step 6.

**Mosofin is read-only.** It produces the statement; publishing or filing it is a human action.
