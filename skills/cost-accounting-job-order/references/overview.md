<!-- cost-accounting-job-order · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Cost Accounting (Job Order Costing) — Mosofin

Implements **job order costing** for environments where costs are accumulated by **discrete jobs,
projects or orders** — construction, custom manufacturing, professional services with billable
projects.

**In plain words:** some businesses make the same thing over and over, and some make a different thing
each time. If every job is different, you cannot know whether you made money until you can see what
*that job* cost — the materials that went into it, the hours people spent on it, and a fair share of
the costs that keep the lights on. Job costing is the discipline of attaching all three to the right
job.

Focus areas:

- **Direct materials and direct labor capture**
- **Overhead pools and application bases**
- **WIP rollforward**
- **Job profitability and variance analysis**
- **Cutoff and close controls**

It is **workspace-scoped**: costs, hours, overhead and WIP balances come from tool calls against a
company file connected to your Mosofin workspace in this conversation, or from something you supplied
by hand and that is labelled as such.

## What a connected workspace changes here

**The controls become tests.** The original's quality checks are good ones, and **three of the four can
be *run* rather than described:**

1. **"Job IDs present on all direct cost postings"** — **`[auto]`, and the foundational one.** Scan
   direct-cost transactions for a missing job tag. Every other figure in this skill depends on it: an
   untagged cost is a cost that belongs to some job and is sitting in none of them, so **every job's
   margin is overstated and the untagged total is the size of the error.** Run this first, every time.
2. **"WIP does not include costs for closed jobs"** — **`[auto]`**: compare WIP by job against job
   status. Stranded WIP on a finished job is unrelieved cost that will surface as a nasty surprise.
3. **"Overhead pool excludes non-overhead items"** — **`[gated]`**: the pool's contents are readable
   account by account, so the pool can be listed for review rather than assumed correct.

Beyond the controls, **`[auto]`** covers: costs by job where tagged, **labour hours by job** where time
is tracked, the overhead accounts and their balances, applied-versus-actual overhead once a rate
exists, and the WIP roll-forward.

**`[manual]`:** labour **rates** (hours are usually in the books; pay rates are not, absent a payroll
connection), machine hours, the budgeted overhead and budgeted base behind a predetermined rate, the
revenue model, and the WIP capitalisation policy.

**Mosofin is read-only.** Every entry below is a *proposal* for a human.
