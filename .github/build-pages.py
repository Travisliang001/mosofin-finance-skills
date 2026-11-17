#!/usr/bin/env python3
"""Build one public explanation page per skill, plus an index, in skill-pages/.

A page says what a skill is for, when to use it, what it asks, what to upload and what
comes back. It never carries the method: no steps, gates, thresholds, tool names or
entries. Everything is read from the skill card and the README skill tables, so the pages
can stay public even where the skill files themselves are not.

    python3 .github/build-pages.py           write the pages
    python3 .github/build-pages.py --check   fail if a page is missing, stale or leaks
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")
OUT = os.path.join(ROOT, "skill-pages")

GROUPS = {
    1: "Everyday payables, receivables and close",
    2: "The close cycle and the sub-ledgers",
    3: "Payroll, entry review, forecasting and fixed assets",
    4: "Payment processors",
    5: "Analysis and reporting",
    6: "Forecasting, customers, credit, debt and fraud risk",
    7: "Stock, costing, credit policy and audit preparation",
    8: "Controls, audit, treasury and the chart of accounts",
    9: "Quarter-end and year-end close, planning and foreign currency",
    10: "Accounting standards",
    11: "Costing, notes, segments and modelling",
    12: "Public reporting",
    13: "Specialist technical accounting",
    14: "Sector-specific accounting",
    15: "Further payables, receivables and compliance skills",
    16: "Tax, for a qualified professional to review",
    17: "Valuation and transactions, for a qualified professional to review",
    18: "Movement analysis and customer deductions",
}

# Anything matching these in a finished page is method detail that must not be published.
LEAKS = [
    r"references/", r"\b(?:Step|Gate|Stage) \d", r"\[(?:auto|gated|manual)\]",
    r"data_source_id", r"display_name", r"\bmock\b", r"effective_policy",
    r"`(?:get|search|list|create|invoke|update|delete)_[a-z_]+`", r"approved=",
    r"reference file", r"tool name", r"capability map",
]

MARK = (r"(?:Use this skill (?:when|whenever|for)|Use when|Use for|Triggers include|Also trigger|"
        r"Trigger for|Workspace-scoped|Do not use|Do NOT use|Read-only:|Outputs |"
        r"Reads the books through|Reads your books through)")


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def readme_rows():
    rows, wave = {}, 0
    for line in read(os.path.join(ROOT, "README.md")).splitlines():
        m = re.match(r"\*\*Wave (\d+)\*\*", line)
        if m:
            wave = int(m.group(1))
            continue
        m = re.match(r"\| `([a-z0-9-]+)` \| (\d+)% \| (.+?) \|\s*$", line)
        if m and wave:
            rows[m.group(1)] = (wave, int(m.group(2)), m.group(3).strip())
    return rows


def sentences(text):
    return [s for s in re.split(r"(?<=[.!?])\s+(?=[A-Z*`'\"(])", text.strip()) if s]


def clean(text):
    """Drop sentences that point into the method, and strip internal markers."""
    text = re.sub(r"\s*—\s*usually\s*\*{0,2}\[(?:auto|gated|manual)\]\*{0,2}", "", text)
    text = re.sub(r"\s*\((?:Stage|Step|Gate) \d[^)]*\)", "", text)
    text = text.replace("by `display_name`", "by name").replace("`display_name`", "name")
    kept = []
    for s in sentences(text):
        if any(re.search(p, s) for p in LEAKS):
            continue
        kept.append(s)
    out = " ".join(kept).strip()
    out = re.sub(r"\s*\((?:[A-F])(?:, [A-F])*\)", "", out)
    out = re.sub(r"\*\*\s*\*\*", "", out)
    out = re.sub(r"\s{2,}", " ", out)
    if out.count("**") % 2:
        out += "**"
    return second_person(out)


def second_person(text):
    text = re.sub(r"\b([Tt])he user (states|supplies|names|gives|provides|confirms|uploads|chooses|sets|"
                  r"says|approves|decides|declines|lists|selects|picks|uses|holds|sends|knows|types|"
                  r"answers|closes|describes|tells|brings|keeps|owns|runs|expects|specifies|identifies)\b",
                  lambda m: ("You " if m.group(1) == "T" else "you ")
                  + {"supplies": "supply", "specifies": "specify", "identifies": "identify"}.get(m.group(2), m.group(2)[:-1]),
                  text)
    text = re.sub(r"\bthe user does\b", "you do", text)
    for a, b in [("the user asks", "you ask"), ("the user wants", "you want"),
                 ("the user needs", "you need"), ("the user has", "you have"),
                 ("the user is", "you are"), ("the user agrees", "you agree"),
("their Mosofin workspace", "your Mosofin workspace"),
                 ("the user's", "your"), ("The user's", "Your"), ("the user", "you")]:
        text = text.replace(a, b)
    return text


def cap(text):
    return text[:1].upper() + text[1:] if text else text


def table_after(text, *header_words):
    """Rows (as cell lists) of the first table whose header holds all the given words."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("|") and all(w in line for w in header_words):
            rows = []
            for row in lines[i + 2:]:
                if not row.startswith("|"):
                    break
                rows.append([c.strip() for c in re.split(r"(?<!\\)\|", row.strip().strip("|"))])
            head = [c.strip() for c in line.strip().strip("|").split("|")]
            return head, rows
    return None, []


def section(text, heading_re):
    m = re.search(r"^#{2,3} (?:" + heading_re + r")[^\n]*\n(.*?)(?=^#{1,3} |\Z)", text, re.M | re.S)
    return m.group(1) if m else ""


def bullets(block):
    items, cur = [], None
    for line in block.splitlines():
        if line.startswith("- "):
            if cur:
                items.append(cur)
            cur = line[2:].strip()
        elif cur is not None and line.startswith("  ") and line.strip():
            cur += " " + line.strip()
        elif cur is not None and not line.strip():
            items.append(cur)
            cur = None
    if cur:
        items.append(cur)
    return items


def parse_description(desc):
    parts = re.split(r"(?<=[.!?])\s+(?=" + MARK + ")", desc)
    d = {"what": "", "when": "", "examples": [], "not_for": [], "produces": ""}
    for i, p in enumerate(parts):
        low = p.lower()
        if p.startswith(("Triggers include", "Also trigger", "Trigger for")):
            d["examples"] += [e.rstrip(",.") for e in re.findall(r"(?<=[\s:(])'([^']{3,90}?)'(?=[,.;)\s])", p)]
        elif low.startswith("do not use"):
            d["not_for"].append(cap(re.sub(r"^Do (?:not|NOT) use (?:this skill )?(?:for |when |to )?", "", p)))
        elif p.startswith("Outputs "):
            d["produces"] = p + (" " + d["produces"] if d["produces"] else "")
        elif p.startswith("Read-only:"):
            d["produces"] += (" " if d["produces"] else "") + cap(p[len("Read-only:"):].strip())
        elif p.startswith(("Workspace-scoped", "Reads the books through", "Reads your books through")):
            continue
        elif re.match(r"Use this skill (?:when|whenever|for)|Use when|Use for", p) and i > 0:
            d["when"] += (" " if d["when"] else "") + p
        else:
            d["what"] += (" " if d["what"] else "") + p
    w = re.sub(r"^Use this skill (?:whenever|when) the user (?:wants|needs|asks) to ", "", d["what"])
    if w != d["what"]:
        w = "Helps you " + w
    w = re.sub(r"^Use the confirmed Mosofin workspace and its connected accounting datasource to ", "Helps you ", w)
    w = w.replace("from their Mosofin workspace", "from your books").replace("against their Mosofin workspace", "against your books")
    d["what"] = w
    if d["when"]:
        d["when"] = re.sub(r"^Use (?:this skill )?(?:when|whenever)\b", "Use it when", d["when"])
    return d


def output_names(text):
    block = section(text, r"Step \d+ — Output|Outputs")
    names = re.findall(r"\*\*Sheet \d+: ([^*]+?)\*\*", block)
    if not names:
        block = block.split("**Coverage sheet")[0]
        names = [m for m in re.findall(r"^- \*\*([^*]+?)\*\*", block, re.M)]
    out = []
    for n in names:
        n = re.sub(r"\s*—.*$", "", n).strip().rstrip(".,:")
        if n and len(n) <= 60 and not any(re.search(p, n) for p in LEAKS) and n not in out:
            out.append(n)
    return out[:10]


def title_of(card, name):
    for m in re.finditer(r"^# (.+)$", card, re.M):
        t = m.group(1).strip()
        if not re.match(r"(ONBOARDING|PART )", t):
            return re.sub(r"\s*\(Mosofin\)\s*$", "", t)
    return name.replace("-", " ").capitalize()


def linkify(text, names, me):
    def sub(m):
        n = m.group(1)
        return f"[{n}]({n}.md)" if n in names and n != me else m.group(0)
    text = re.sub(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`", sub, text)
    return re.sub(r"(?<![\[\w/(-])([a-z0-9]+(?:-[a-z0-9]+)+)(?![\w\]-]|\.md)", sub, text)


def build_page(name, rows, names):
    card = read(os.path.join(SKILLS, name, "SKILL.md"))
    mpath = os.path.join(SKILLS, name, "references", "method.md")
    method = read(mpath) if os.path.exists(mpath) else card
    desc = re.search(r'^description:\s*"?(.*?)"?\s*$', card, re.M).group(1).replace('\\"', '"')
    d = parse_description(desc)
    wave, pct, blurb = rows.get(name, (0, None, ""))

    L = [f"# {title_of(card, name)}", ""]
    if blurb:
        L += [f"> {blurb}.", ""]
    facts = [f"**Skill:** `{name}`"]
    if wave:
        facts.append(f"**Area:** {GROUPS[wave]}")
    if pct is not None:
        facts.append(f"**Automated with Mosofin connected:** {pct}%")
    facts.append("**Read-only**")
    L += ["  ·  ".join(facts), ""]

    L += ["## What it does", "", clean(d["what"]) or blurb, ""]

    if d["when"] or d["examples"] or d["not_for"]:
        L += ["## When to use it", ""]
        if d["when"]:
            L += [clean(d["when"]), ""]
        if d["examples"]:
            L += ["Typical requests:", ""] + [f"- \"{e}\"" for e in d["examples"][:8]] + [""]
        nf = [clean(x) for x in d["not_for"] if clean(x)]
        if nf:
            L += ["Not for:", ""] + [f"- {x}" for x in nf] + [""]

    head, ask = table_after(card, "Ask", "Why it matters")
    if ask:
        L += ["## What it asks you first", "", "| It asks | Why |", "|---|---|"]
        for r in ask:
            if len(r) >= 3 and clean(r[1]):
                L.append(f"| {clean(r[1])} | {clean(r[2])} |")
        L.append("")
    else:
        head, ask = table_after(card, "What to confirm", "Required?")
        if ask:
            L += ["## What it asks you first", "", "| It confirms | Needed? |", "|---|---|"]
            for r in ask:
                if len(r) >= 2 and clean(r[0]):
                    L.append(f"| {clean(r[0])} | {clean(r[1]) or 'Recommended'} |")
            L.append("")

    L += ["## With or without Mosofin", "",
          "With a Mosofin workspace connected, and only after you agree, the skill reads the "
          "figures from your own books. Without a connection it runs the same analysis on "
          "files you upload, and the output says which figures came from where.", ""]
    head, up = table_after(card, "Upload", "Needed?")
    if up:
        L += ["If you upload the data yourself:", "", "| Upload | Needed? | Format |", "|---|---|---|"]
        for r in up:
            if len(r) >= 3 and clean(r[0]):
                L.append(f"| {clean(r[0])} | {clean(r[1])} | {clean(r[2])} |")
        L.append("")
    L += ["Every uploaded file is checked before any work starts: that it is the right kind "
          "of document, for the right company and period, and usable.", ""]

    outs = output_names(method)
    if d["produces"] or outs:
        L += ["## What you get", ""]
        if d["produces"]:
            L += [cap(clean(d["produces"])), ""]
        if len(outs) >= 2:
            L += [f"- {o}" for o in outs] + [""]

    rules = [clean(b) for b in bullets(section(card, "Rules that never bend"))]
    rules = [r for r in rules if r]
    if not rules:
        rules = ["**Asks before using Mosofin.** A connected account is not permission to read it.",
                 "**Never writes, updates or deletes anything, in any system.** Every entry, "
                 "message or change it suggests is a proposal for a person to approve.",
                 "**Says what it could not check.** Anything it could not verify is listed, "
                 "with what you would need to supply."]
    L += ["## What it never does", ""] + [f"- {r}" for r in rules] + [""]

    L += ["---", "", "[All skills](README.md) · [Getting started](../README.md#getting-started)", "",
          "<!-- Generated by .github/build-pages.py from the skill card. Edit the skill, not this page. -->", ""]
    page = "\n".join(L)
    return linkify(page, names, name)


def build_index(names, rows):
    L = ["# Mosofin finance skills: what each one does", "",
         f"One page per skill, {len(names)} in all. Each page says what the skill is for, when to "
         "use it, what it asks you, what to upload if you are not connected to Mosofin, and what "
         "you get back.", "",
         "Every skill is **read-only**: it reads and analyses, and anything that would change "
         "your books comes back as a proposal for a person to approve.", "",
         "**Automated** is the share of a skill's checks that run without asking you for a "
         "document when a Mosofin workspace is connected. The rest need evidence that is not in "
         "the books, such as a bank statement or a contract.", ""]
    by = {}
    for n in names:
        by.setdefault(rows.get(n, (0, None, ""))[0], []).append(n)
    for wave in sorted(by):
        L += [f"## {GROUPS.get(wave, 'Other skills')}", "", "| Skill | What it's for | Automated |", "|---|---|---:|"]
        for n in sorted(by[wave], key=lambda x: -(rows.get(x, (0, 0, ""))[1] or 0)):
            _, pct, blurb = rows.get(n, (0, None, ""))
            L.append(f"| [`{n}`]({n}.md) | {blurb} | {'' if pct is None else str(pct) + '%'} |")
        L.append("")
    L += ["<!-- Generated by .github/build-pages.py. -->", ""]
    return "\n".join(L)


def main():
    check = "--check" in sys.argv
    names = sorted(n for n in os.listdir(SKILLS) if os.path.isfile(os.path.join(SKILLS, n, "SKILL.md")))
    rows = readme_rows()
    files = {"README.md": build_index(names, rows)}
    for n in names:
        files[n + ".md"] = build_page(n, rows, set(names))

    problems = []
    for fn, text in files.items():
        for p in LEAKS:
            m = re.search(p, text)
            if m:
                problems.append(f"{fn}: method detail in page: {m.group(0)!r}")
    for n in names:
        if n not in rows:
            problems.append(f"{n}: no row in the README skill tables")

    os.makedirs(OUT, exist_ok=True)
    on_disk = {f for f in os.listdir(OUT) if f.endswith(".md")}
    if check:
        for fn, text in files.items():
            p = os.path.join(OUT, fn)
            if not os.path.exists(p) or read(p) != text:
                problems.append(f"{fn}: out of date; run .github/build-pages.py")
        for fn in sorted(on_disk - set(files)):
            problems.append(f"{fn}: no matching skill")
    else:
        for fn, text in files.items():
            with open(os.path.join(OUT, fn), "w", encoding="utf-8") as f:
                f.write(text)
        for fn in on_disk - set(files):
            os.remove(os.path.join(OUT, fn))

    for p in problems:
        print("PROBLEM", p)
    print(f"{len(names)} skill pages, {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
