<!-- chart-of-accounts-designer · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**Existing COA has accumulated noise** (dozens of unused accounts, duplicates, miscoded items):
**Recommend cleanup before adding new accounts. Output a "Retire" list separately.** *Mosofin note*:
this is the skill's strongest automated contribution — the retire list is **measured** from usage,
not guessed, and each entry carries its transaction count, last activity date and balance.

**Account numbers conflict with the target system's reserved ranges**: some systems reserve certain
ranges. If the user's existing scheme conflicts, **propose remapping with a clear migration table.**

**Same account used for very different purposes**: **recommend splitting. Show the rationale.**
*Mosofin note*: detectable — an account whose transactions come from wildly different sources
(customers and vendors, or several unrelated dimensions) is being used for more than one thing.

**Cross-currency reporting**: functional currency accounts **plus CTA / FX revaluation accounts**.
The ongoing revaluation entries are separate work.

**Migrating from a chart that uses descriptive text only (no numbers)** to a numbered system: assign
numbers per the conventional ranges; **provide the mapping.**

**User insists on a sub-account explosion** (e.g. separate accounts per customer or vendor): **push
back — that's what dimensions or sub-ledgers are for.** Show how dimensions achieve the same
reporting without bloating the COA. *Mosofin note*: quantify the argument — show the current account
count, and how many accounts the request would add.

**Old vs. new GAAP transitions** (e.g. a new lease standard requiring ROU assets and lease
liabilities for the first time): **add those accounts as part of the design and flag the transition
entries needed**.

**A dormant account still holds a balance** — *Mosofin-specific*. Do **not** put it on the retire
list. No activity plus a live balance usually means a forgotten reconciling item, and deactivating
the account buries it. Investigate first.

**Balances mistaken for usage** — *Mosofin-specific*. A nil balance does not mean an account is
unused (clearing accounts sit at nil by design), and a large balance does not mean it is active.
Classify on transactions and last activity, never on balance alone.

**Inactive accounts excluded from the read** — *Mosofin-specific*. Much of the noise is already
deactivated but still appears in reports and import files. Search including inactive accounts, or the
cleanup is incomplete.

**The target system differs from the connected one** — *Mosofin-specific*. Account types and detail
types will not map one-to-one, and some concepts have no equivalent. Say which mappings are exact and
which are approximations, and never present a converted detail type as certain.

**The registered industry is generic or stale** — *Mosofin-specific*. Confirm the industry before
adding a whole industry account block; the profile's code is often set once at registration and never
revisited.

**A company file is connected but not active** — *Mosofin-specific*. Name it as excluded and say whose
chart is therefore unexamined. Surface any `reconnect_url`.

**A result comes back with `mock: true`** — *Mosofin-specific*. A retire list built on fixture usage
would recommend deactivating accounts a real business depends on.

**A stored numbering scheme conflicts with the live chart** — *Mosofin-specific*. If the chart has
changed since the preference was saved, the stored scheme may no longer describe it. Re-read the
chart and reconcile before applying a stored map.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it.
Never apply one entity's chart design to another; never drop it silently.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
