<!-- esg-sustainability-reporting · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# ESG and Sustainability Reporting (Mosofin)

Designs an **ESG reporting operating model**: which metrics to report, how to collect and validate the data,
and how to produce consistent disclosures with **audit / assurance readiness**.

**In plain words:** ESG reporting means publishing numbers about your environmental and social impact — how
much energy you use, what you emit, who you employ — with the same discipline you would apply to financial
figures. The hard part is rarely the reporting. It is that most of the data lives in utility portals,
travel systems, HR files and suppliers' hands, and nobody has ever had to make it audit-proof before.

It is **workspace-scoped**: the financial activity data comes from tool calls against company files
connected to your Mosofin workspace in this conversation, or from something you supplied by hand and that
is labelled as such.

## What the ledger can and cannot tell you about emissions

This is the judgment that shapes the whole skill, so it goes first.

**What the workspace genuinely contributes:**

1. **Spend-based activity data.** Emissions estimated as **spend by category × an emission factor per unit
   of currency** is a recognised, widely used method — particularly for **Scope 3 purchased goods and
   services**, where nothing better exists. **The purchase ledger is exactly this dataset**, already
   categorised, already complete, already reconciled to the financial statements. That is a real strength
   and few systems have it.
2. **The supplier list.** Scope 3 supplier engagement starts with knowing who your suppliers are and how
   much you buy from each. **That is one read** (*`search_vendors`*, spend by vendor), and it produces the
   ranked list that tells you which twenty suppliers to actually ask.
3. **Business travel.** Travel and mileage expense categories map to **Scope 3 Category 6**, and they are
   in the ledger.
4. **Utility and fuel accounts.** Which utility suppliers, which sites, which months — the shape of the
   energy estimate, if not its content.
5. **Headcount** — the denominator for nearly every intensity metric, and for several social metrics.
6. **The organizational boundary.** Gate 1's list of connected company files is a **candidate reporting
   boundary**, and comparing it against the intended ESG boundary is a genuine control.

**What it cannot tell you, ever:**

- **Money is not molecules.** A utility invoice records **what you paid, not what you consumed.** If the
  tariff rose 30% and consumption fell 10%, the ledger shows a 20% *increase*. **Reporting a
  spend-derived energy figure as though it were metered consumption is the single most damaging error
  available in this skill** — it produces a number that moves with prices and gets published as an
  environmental result.
- **There are no emission factors on this surface.** Not for electricity grids, not for fuels, not for
  spend categories. Every factor is `[manual]`, with its **source, version and year**.
- **There is no physical data.** No kWh, litres, cubic metres, tonnes or kilometres.
- **There is no social or governance data.** Diversity, safety incidents, policy coverage, board
  composition — none of it is in an accounting system.

**So this skill's honest output is: a rigorous catalog and control design in full, a genuinely useful
spend-based activity dataset, and an explicit statement that the physical and social measurements come from
elsewhere.** That is a better deliverable than a fabricated emissions total.

**Mosofin is read-only.** It cannot write to any ESG platform, submit a disclosure or update a metric.
Everything below is a *proposal*.
