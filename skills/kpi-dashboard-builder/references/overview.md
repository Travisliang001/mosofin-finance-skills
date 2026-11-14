<!-- kpi-dashboard-builder · overview.md · read for: background — which KPIs the books can and cannot supply, and why recognised revenue is not ARR. Edit here, not in SKILL.md. -->

# KPI Dashboard Builder (Mosofin)

Designs and builds a **KPI dashboard** — selecting the right metrics for the entity, **defining each
precisely**, computing them, and laying them out with **trends, targets, and alerts**. **Avoids vanity
metrics; focuses on decision-useful indicators.**

**In plain words:** a dashboard is a small number of figures that tell you whether the business is working.
The hard parts are choosing which figures, defining them so precisely that they mean the same thing every
month, and being honest about which of them you can actually measure.

This skill is **industry-aware**. **The right KPIs for SaaS differ from retail, services, manufacturing,
and so on.**

It is **workspace-scoped**: the financial metrics, their history and the tie-outs come from tool calls
against a company file connected to your Mosofin workspace in this conversation, or from something you
supplied by hand and that is labelled as such.

## The mapping: financial KPIs are computable, operational ones mostly are not

**The general financial set in Step 1 — all of it — is `[auto]`.** Revenue growth, every margin, EBITDA,
operating and free cash flow, cash and runway, DSO / DPO / DIO and the cash conversion cycle, current and
quick ratios, leverage and coverage, returns on equity, assets and capital. **Every one of them is
arithmetic over the profit and loss and the balance sheet, across as many periods as the system holds.**

**The industry sets are a different story**, and the split is worth stating per set before any dashboard is
designed:

| Industry set | Readable here | Needs another system |
|---|---|---|
| **SaaS / Subscription** | almost nothing | **MRR/ARR, churn, NRR/GRR, CAC, LTV, payback, magic number, ARPA** — billing and CRM |
| **E-commerce / Retail** | revenue, margins, inventory turnover, days inventory | **AOV, conversion, traffic, repeat rate, return rate, sell-through** — order and web analytics |
| **Professional Services** | revenue per employee, project margin where projects are classed, WIP and unbilled | **utilization, realization, bill rate, backlog** — a time and practice system |
| **Manufacturing** | gross and contribution margin, inventory turns, cost variances where posted | **capacity utilization, OEE, on-time delivery, scrap and yield** — production systems |
| **General financial** | **all of it** | — |

> **A dashboard built only from the accounting workspace will be entirely financial.** That is a real
> limitation, not a feature: **financial metrics are lagging by construction.** They tell you what happened
> after it happened. **The operational metrics — the ones that move first — mostly live elsewhere.**
>
> **Say this when scoping.** A board dashboard of nine financial ratios is not wrong, but it is not a
> dashboard of the business, and the user should choose that knowingly.

**And the near-substitute that does the most damage here:**

> **Recognised revenue is not ARR.** They diverge constantly — **deferred revenue, annual prepayments,
> usage-based billing, mid-period starts and cancellations** all break the link. **An ARR figure derived
> from the general ledger will be wrong and will look authoritative.** The same applies to **churn derived
> from revenue decline** and **customer counts derived from invoice counts**. **If the billing system is not
> connected, mark these `[manual]` and leave them blank rather than approximating them.**

**What the workspace contributes beyond computation — and it is the thing the original says matters most:**

> **Step 2 says a KPI without a precise, consistent definition "will be computed differently each period and
> mislead", and calls this the most important step.** **A stored query recipe solves it structurally.** When
> a metric is defined as *this tool, these parameters, these accounts*, **recomputing it next period cannot
> drift** — it is the same operation on new data. **Persist the recipe, never the number** (Step 9), and the
> definition-drift problem largely disappears for every `[auto]` metric.

**Mosofin is read-only.** It reads and computes; it changes nothing.
