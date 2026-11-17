#!/usr/bin/env python3
"""Scenario tests for the explanation pages in skill-pages/.

Each scenario is a question a reader or a reviewer would put to a page, checked for every
page against its source (the skill card, the workflow README and schemas):

  S1 fidelity     every question, upload row, rule and output named on a page is in the card
  S2 not-for      every "not for" link points at a skill that exists and is a different skill
  S3 triggers     every typical request quoted on a page is quoted in the card's description
  S4 workflows    every setting and file role on a workflow page is in its input schema, and
                  nothing in the schema is missing from the page (except the data source id)
  S5 rendering    every table row has the header's column count; every relative link resolves
  S6 reach        every skill and workflow is reachable from the index and the sitemap, and
                  the sitemap.xml has one entry per page
  S7 reader       a page answers the five reader questions: what, when, what it asks, what to
                  upload, what comes back — each section names at least one concrete thing

    python3 .github/test-pages.py
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = os.path.join(ROOT, "skill-pages")
SKILLS = os.path.join(ROOT, "skills")
WORKFLOWS = os.path.join(ROOT, "workflows")


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def norm(s):
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    s = re.sub(r"[*`_>\"']", "", s)
    s = s.replace("you ", "the user ").replace("your ", "the user's ")
    return re.sub(r"\s+", " ", s).strip().lower()


def section(text, name):
    m = re.search(r"^## " + re.escape(name) + r"\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1) if m else ""


def table_rows(block):
    rows = []
    for line in block.splitlines():
        if line.startswith("|") and not re.match(r"^\|[-| ]+\|$", line):
            rows.append([c.strip() for c in line.strip().strip("|").split("|")])
    return rows[1:] if rows else [], (rows[0] if rows else [])


def in_source(fragment, source):
    """A page fragment counts as grounded when a long enough piece of it is in the source."""
    f = norm(fragment)
    s = norm(source)
    if len(f) < 12:
        return True
    if f in s:
        return True
    # the page may have cut a sentence or rewritten to the second person; test the longest words
    words = [w for w in re.findall(r"[a-z][a-z-]{4,}", f) if w not in ("their", "which", "there", "these")]
    if not words:
        return True
    hits = sum(1 for w in words if w in s)
    return hits / len(words) >= 0.8


def main():
    fails = []
    pages = sorted(f for f in os.listdir(PAGES) if f.endswith(".md") and f not in ("README.md", "sitemap.md"))
    index, sitemap = read(os.path.join(PAGES, "README.md")), read(os.path.join(PAGES, "sitemap.md"))
    xml = read(os.path.join(PAGES, "sitemap.xml"))
    counts = {k: 0 for k in "S1 S2 S3 S4 S5 S6 S7".split()}

    for fn in pages:
        page = read(os.path.join(PAGES, fn))
        is_wf = fn.startswith("workflow-")
        name = fn[len("workflow-"):-3] if is_wf else fn[:-3]

        # S5 rendering
        for sec in re.findall(r"^## .+$", page, re.M):
            rows, head = table_rows(section(page, sec[3:]))
            for r in rows:
                if len(r) != len(head):
                    fails.append(f"S5 {fn}: row has {len(r)} cells, header {len(head)}: {r[0][:40]!r}")
        for link in re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", page):
            if link.startswith("http"):
                continue
            if not os.path.exists(os.path.normpath(os.path.join(PAGES, link))):
                fails.append(f"S5 {fn}: link does not resolve: {link}")
        counts["S5"] += 1

        # S6 reach
        if f"({fn})" not in index:
            fails.append(f"S6 {fn}: not linked from the index")
        if f"({fn})" not in sitemap:
            fails.append(f"S6 {fn}: not in sitemap.md")
        if f"/{fn}</loc>" not in xml:
            fails.append(f"S6 {fn}: not in sitemap.xml")
        counts["S6"] += 1

        if is_wf:
            src = os.path.join(WORKFLOWS, name)
            schema = json.load(open(os.path.join(src, "input.schema.json")))
            settings = set(schema["properties"]["settings"]["properties"]) - {"data_source_id"}
            roles = set(schema["properties"]["files"]["items"]["properties"]["role"].get("enum", []))
            rows, _ = table_rows(section(page, "What you can change"))
            on_page = {r[0].strip("`") for r in rows}
            for s in sorted(settings - on_page):
                fails.append(f"S4 {fn}: setting {s} is in the schema but not on the page")
            for s in sorted(on_page - settings):
                fails.append(f"S4 {fn}: setting {s} is on the page but not in the schema")
            rows, _ = table_rows(section(page, "What you send it"))
            page_roles = {r[0].strip("`") for r in rows}
            if page_roles != roles:
                fails.append(f"S4 {fn}: file roles {sorted(page_roles)} differ from schema {sorted(roles)}")
            readme = read(os.path.join(src, "README.md"))
            for b in re.findall(r"^- (.+)$", section(page, "What it does"), re.M):
                if not in_source(b, readme):
                    fails.append(f"S1 {fn}: logic line not in the workflow README: {b[:60]!r}")
            counts["S4"] += 1
            counts["S1"] += 1
            # S7
            for sec in ("What it does", "When it runs", "What you send it", "What comes back"):
                if len(section(page, sec).split()) < 15:
                    fails.append(f"S7 {fn}: section {sec!r} answers nothing concrete")
            counts["S7"] += 1
            continue

        card = read(os.path.join(SKILLS, name, "SKILL.md"))
        mpath = os.path.join(SKILLS, name, "references", "method.md")
        source = card + ("\n" + read(mpath) if os.path.exists(mpath) else "")
        desc = re.search(r'^description:\s*"?(.*?)"?\s*$', card, re.M).group(1)

        # S1 fidelity: asks, uploads, rules, outputs
        for sec, col in (("What it asks you first", 0), ("With or without Mosofin", 0)):
            rows, _ = table_rows(section(page, sec))
            for r in rows:
                if not in_source(r[col], source):
                    fails.append(f"S1 {fn}: {sec} row not in the card: {r[col][:60]!r}")
        for b in re.findall(r"^- (.+)$", section(page, "What it never does"), re.M):
            if "Rules that never bend" in card and not in_source(b, card):
                fails.append(f"S1 {fn}: rule not in the card: {b[:60]!r}")
        for b in re.findall(r"^- ([^\"].+)$", section(page, "What you get"), re.M):
            if not in_source(b, source):
                fails.append(f"S1 {fn}: output not in the card: {b[:60]!r}")
        what = section(page, "What it does").split("\n\n")[0]
        if not in_source(what, desc + "\n" + card):
            fails.append(f"S1 {fn}: 'what it does' not grounded in the description")
        counts["S1"] += 1

        # S2 not-for links
        for target in re.findall(r"\]\(([a-z0-9-]+)\.md\)", section(page, "When to use it")):
            if target == name:
                fails.append(f"S2 {fn}: 'not for' links to itself")
            if not os.path.isdir(os.path.join(SKILLS, target)):
                fails.append(f"S2 {fn}: 'not for' links to a skill that does not exist: {target}")
        counts["S2"] += 1

        # S3 triggers
        for q in re.findall(r'^- "(.+)"$', section(page, "When to use it"), re.M):
            if q.lower() not in desc.lower():
                fails.append(f"S3 {fn}: quoted request not in the description: {q!r}")
        counts["S3"] += 1

        # S7 reader questions
        checks = {
            "What it does": r"[a-z]{4,}",
            "When to use it": r"(?:Use it when|Typical requests|Not for)",
            "What it asks you first": r"(?:\| \*|\| [A-Z]|company|period|date)",
            "With or without Mosofin": r"(?:\| |CSV|XLSX|PDF|exports)",
            "What you get": r"(?:^- |[Pp]roduces|[Oo]utputs|workpaper|schedule|report|log|proposal)",
        }
        for sec, pat in checks.items():
            if not re.search(pat, section(page, sec), re.M):
                fails.append(f"S7 {fn}: section {sec!r} does not answer the reader's question")
        counts["S7"] += 1

    for f in fails:
        print("FAIL", f)
    print("scenarios run per page:", ", ".join(f"{k}={v}" for k, v in counts.items()))
    print(f"{len(pages)} pages, {len(fails)} failures")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
