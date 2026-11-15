<!-- government-fund-accounting-gasb · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Government / Public-Sector Fund Accounting — GASB / IPSAS (Mosofin)

Handles accounting for **state and local governments** and similar public-sector entities — the distinctive
**fund accounting** model, **dual-perspective reporting** (fund vs. government-wide), **modified vs. full
accrual** basis, and the public-sector-specific classifications and disclosures.

**In plain words:** a government does not have one set of books, it has many — one per pot of money, each
with rules about what it may be spent on. And it has to report twice: once fund by fund, showing what money
came in and went out this year, and once for the whole government, showing everything it owns and owes.
The two views are prepared on different accounting bases, which is why they never agree without a bridge.

This skill is **framework-aware** — **GASB** for US state / local governments; **IPSAS** for many other
countries' public-sector entities; **central-government frameworks vary**. **Public-sector accounting
differs substantially from commercial accounting; this skill applies the right model. Confirm current
standards for the entity's jurisdiction.**

It is **workspace-scoped**: the trial balances, the fund dimension and the capital and debt balances come
from tool calls against a company file connected to your Mosofin workspace in this conversation, or from
something you supplied by hand and that is labelled as such.

## The structural problem: one book, three bases

**Read this before anything else, because it determines what this skill can honestly produce.**

GASB requires **three views of the same government at once**:

| View | Basis | Measurement focus |
|---|---|---|
| **Governmental funds** | **Modified accrual** | Current financial resources — **no capital assets, no long-term debt** |
| **Proprietary and fiduciary funds** | **Full accrual** | Economic resources — capital assets and debt **on** the balance sheet |
| **Government-wide** | **Full accrual** | Everything, including capital assets, long-term debt and net pension liability |

**A commercial accounting platform has one accounting-method setting for the whole company file** — cash or
accrual. **It cannot maintain modified accrual for some funds and full accrual for others simultaneously**,
and it has no concept of a measurement focus that excludes capital assets from a subset of funds.

**So exactly one of those three views can be "what the books say". The other two are conversions prepared
outside the ledger.** Your first job is to establish **which one the books are on**, and to say so
explicitly in the output. Everything else follows:

- If the books are kept on the **governmental fund** basis, then capital assets and long-term debt are
  probably tracked outside the system entirely, and the **government-wide** statements are a build.
- If the books are kept on **full accrual** with everything on the balance sheet, then the **governmental
  fund** statements require *removing* capital assets and long-term debt and re-applying the availability
  test — and that removal is the conversion.

**Never present a platform-generated report as a governmental fund statement without saying which basis
produced it.** The most common error in this whole area is applying the wrong basis to a fund, and here the
platform will produce a plausible-looking statement on the wrong one without complaint.

**The second structural question: is there a fund dimension at all?**

Small governments, school districts and special districts frequently do keep their books in commercial
software, **using classes, departments or locations as funds.** Where that is so, **a trial balance by fund
is `[auto]`** and much of this skill works. Where no such dimension exists, **fund-level reporting cannot be
produced from the ledger at all** — say so plainly rather than aggregating everything into a General Fund.

**But a class is not a fund.** A fund is a **separate fiscal and accounting entity with its own
self-balancing set of accounts**. A class is a tag. They coincide when someone set them up to coincide.
**Confirm the mapping; never assume it.**

**Mosofin is read-only.** It cannot post, close, transfer between funds or reclassify fund balance. Every
entry below is a *proposal*.
