---
name: esg-sustainability-reporting
description: "Designs an ESG and sustainability reporting process: the reporting scope and boundaries, the catalogue of metrics, the data pipeline and controls behind each one, and the reporting and narrative, built so the figures can stand up to assurance. Reads spend through a connected Mosofin workspace to show which activity data the books can point to, and states that spend is not consumption. Works from uploaded activity data when Mosofin is not used. Use when the user asks to set up ESG or sustainability reporting, choose ESG metrics, plan emissions data collection, prepare for assurance over ESG data, or map data sources for a sustainability report. Do not use for a financial KPI dashboard (use kpi-dashboard-builder). Read-only: produces the scope, the catalogue and the data plan, and never supplies an emission factor."
---

# ESG reporting: the same discipline as the financial figures

ESG reporting means publishing figures about environmental and social impact, such as energy used,
emissions and workforce, with the discipline applied to financial numbers. The hard part is rarely
the report. It is that the data lives in utility portals, travel systems and HR files. This skill
designs the **scope, the metric catalogue and the data pipeline**.

**Works with or without Mosofin.** With Mosofin connected it reads spend by vendor and category,
which shows where activity data should exist. Without it, you supply the activity data and the
method is the same.

**Spend is not consumption.** The books show what was paid for energy or travel, not the
kilowatt-hours or the kilometres. Physical quantities and emission factors come from you, each
with its source and year. Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.**
- **Never supplies an emission factor.** It asks for the source, the version and the year.
- **Never converts spend into a physical quantity without a stated factor**, and labels any
  spend-based figure as an estimate.
- **Never reports a metric with no named owner and no source.**
- **Never claims assurance readiness.** It lists what an assurer would ask for.

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–5" always mean the steps in `references/method.md`.*

Before reading any data, collect the basics in **one short batch**, not one question at a time.
Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *What is the reporting for: a regulation, investors, customers, or voluntary?* | Decides what is mandatory | **Ask again.** |
| **C** | *Which entities and sites are in the boundary, and on what basis: control or equity share?* | Determines whose impact is counted | Use the connected entities, and say the boundary was not confirmed. |
| **D** | *Which metrics are tracked today, and under which framework, if any?* | The honest starting point | Propose a minimal catalogue, and ask. |
| **E** | *Where does the activity data live: utility bills, travel, procurement, HR? Which emission factor source?* | Most of it is outside the books | Map the spend categories, and list each quantity as not supplied. |
| **F** | *Will the figures be assured, and what was published before?* | Changes the controls needed | Design for limited assurance, and say so. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Report spend by category that points to activity data: energy, fuel, travel, freight.
- Say whether the ESG boundary matches the company files in scope.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Activity data**: energy, fuel, travel, headcount | Required for any metric | XLSX or CSV |
| **Emission factors** with source, version and year | Required for emissions | XLSX or PDF |
| Prior disclosures | Recommended | PDF |

**Read back before starting, then wait for a yes:**

> *Designing ESG reporting for **Northbrook Trading**, for **customer requests**, on an
> **operational control** boundary of **two sites**, with spend from **your Mosofin connection**.
> Metrics today: **electricity and headcount** only. Emission factors from **the source you
> named**. No assurance planned this year. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the period, the
sites and the units. Flag anything unreadable straight away.

**Then validate the upload before any work, every time.** For each file: is it the right kind of
document, for the right company and period, usable, and necessary for this skill? Give a verdict
per file, list what is still missing, and wait for the user's answer. Full wording:
[`references/mosofin-protocol.md`](references/mosofin-protocol.md), *After an upload, validate the
input before any work*.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, and read the company profile, so Stage 1's
answers do not need asking twice. On the upload path, go straight to Stage 3.

## Stage 3 — Read the spend and set the scope

Pull spend by category, then define the reporting scope and boundaries:
[`references/method.md`](references/method.md) Steps 0–1.

## Stage 4 — Build the metric catalogue and the data pipeline

The metric catalogue, then the data pipeline and controls:
[`references/method.md`](references/method.md) Steps 2–3. Check
[`references/edge-cases.md`](references/edge-cases.md) for spend read as consumption, a missing
emission factor, a factor version change and a boundary that differs from the financial one.

## Stage 5 — Reporting, narrative, and present

The reporting and narrative, then the output: [`references/method.md`](references/method.md) Steps
4–4b. Before presenting, check it against [`references/output.md`](references/output.md). Ask
whether the user wants the metric catalogue as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 5. Persist the boundary, the metric catalogue,
the owners and the factor sources with their versions.

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
