#!/usr/bin/env python3
"""Build the public explanation pages in skill-pages/: one per skill, one per n8n workflow,
an index, and a sitemap (sitemap.md and sitemap.xml).

A page says what a skill or workflow is for, when to use it, what it asks, what to upload
and what comes back. It never carries the method: no steps, gates, thresholds, tool names
or entries. Everything is read from the skill cards, the workflow READMEs and the README
tables, so the pages can stay public even where the skill files themselves are not.

Every page has the same sections, in the same order, and a quality gate fails the build
when a section is missing, thin, or leaks method detail.

    python3 .github/build-pages.py           write the pages
    python3 .github/build-pages.py --check   fail if a page is missing, stale or leaks
"""
import os
import re
import sys
import json
import subprocess
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")
WORKFLOWS = os.path.join(ROOT, "workflows")
OUT = os.path.join(ROOT, "skill-pages")
BASE_URL = "https://github.com/MosoFin/mosofin-finance-skills/blob/main/skill-pages/"

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
    18: "Flux analysis and customer deductions",
}

# Anything matching these in a finished page is method detail that must not be published.
LEAKS = [
    r"references/", r"\b(?:Step|Gate|Stage) \d", r"\[(?:auto|gated|manual)\]",
    r"data_source_id", r"display_name", r"\bmock\b", r"effective_policy",
    r"`(?:get|search|list|create|invoke|update|delete)_[a-z_]+`", r"approved=",
    r"reference file", r"tool name", r"capability map", r"proposed_actions", r"requires_approval",
    r"workflow\.json", r"\.schema\.json", r"sample-(?:input|output)",
]

# Sentences a page drops because they point at something the reader cannot see.
DROP = [r"LLM node", r"edge case", r"[Nn]ormally pulled", r"^Pulled\.?$", r"profile contradiction", r"\bprofile's\b",
        r"[Rr]ead back", r"[Rr]ecord what was not"]

# The sections every skill page carries, in order.
SKILL_SECTIONS = ["## What it does", "## When to use it", "## What it asks you first",
                  "## With or without Mosofin", "## What you get", "## What it never does"]
WORKFLOW_SECTIONS = ["## What it does", "## When it runs", "## What you send it",
                     "## What you can change", "## What comes back", "## What it never does"]

MARK = (r"(?:Use this skill (?:when|whenever|for)|Use when|Use for|Triggers include|Also trigger|"
        r"Trigger for|Workspace-scoped|Do not use|Do NOT use|Read-only:|Outputs |"
        r"Reads the books through|Reads your books through)")

READ_WORDS = {
    "get_profit_and_loss": "the profit and loss", "get_balance_sheet": "the balance sheet",
    "get_trial_balance": "the trial balance", "get_general_ledger": "the general ledger",
    "search_bills": "supplier bills", "search_invoices": "customer invoices",
    "search_payments": "customer payments", "search_vendors": "the vendor list",
}


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def cap(text):
    return text[:1].upper() + text[1:] if text else text


def sentences(text):
    return [s for s in re.split(r"(?<=[.!?])\s+(?=[A-Z*`'\"(])", text.strip()) if s]


def second_person(text):
    text = re.sub(r"\b([Tt])he user (states|supplies|names|gives|provides|confirms|uploads|chooses|sets|"
                  r"says|approves|decides|declines|lists|selects|picks|uses|holds|sends|knows|types|"
                  r"answers|closes|describes|tells|brings|keeps|owns|runs|expects|specifies|identifies)\b",
                  lambda m: ("You " if m.group(1) == "T" else "you ")
                  + {"supplies": "supply", "specifies": "specify", "identifies": "identify"}.get(m.group(2), m.group(2)[:-1]),
                  text)
    text = re.sub(r"\bthe user does\b", "you do", text)
    # "when the user asks to X, or uploads Y" -> "when you ask to X, or upload Y"
    verbs = "asks|uploads|wants|needs|mentions|pastes|sends|names|provides|gives|has|says|shares|attaches"
    text = re.sub(r"(\bthe user (?:asks|wants|needs)\b[^.?!]*?\b(?:or|and) )(" + verbs + r")\b",
                  lambda m: m.group(1) + ("have" if m.group(2) == "has" else m.group(2)[:-1]), text)
    for a, b in [("the user asks", "you ask"), ("the user wants", "you want"),
                 ("the user needs", "you need"), ("the user has", "you have"),
                 ("the user is", "you are"), ("the user agrees", "you agree"),
                 ("their Mosofin workspace", "your Mosofin workspace"),
                 ("the user's", "your"), ("The user's", "Your"), ("the user", "you")]:
        text = re.sub(r"\bthe user's or their\b", "yours or your", text)
        text = re.sub(r"\bthe user's(?=[.,;:!?)]|\s*$| or\b)", "yours", text)
        text = text.replace(a, b)
    return text


def clean(text):
    """Drop sentences that point into the method, and strip internal markers."""
    text = re.sub(r"\s*—\s*usually\s*\*{0,2}\[(?:auto|gated|manual)\]\*{0,2}", "", text)
    text = re.sub(r"\s*\((?:Stage|Step|Gate) \d[^)]*\)", "", text)
    text = text.replace("by `display_name`", "by name").replace("`display_name`", "name")
    text = text.replace("~~", "").replace("(regex)", "(pattern)")
    kept = [s for s in sentences(text) if not any(re.search(p, s) for p in LEAKS + DROP)]
    out = " ".join(kept).strip()
    out = re.sub(r"\s*\((?:[A-F])(?:, [A-F])*\)", "", out)
    out = re.sub(r"\*\*\s*\*\*", "", out)
    out = re.sub(r"\s{2,}", " ", out)
    if out.count("**") % 2:
        out += "**"
    return second_person(out)


# Writing rules applied to every finished page (the no-ai-slop editing rules): plain
# punctuation, no binary contrasts, no filler words, no decorative bold mid-sentence.
SLOP = [
    r"—", r"–",
    r"\b(?:delve|foster|leverage|utili[sz]e|facilitate|empower|streamline|robust|cutting-edge|"
    r"seamless|game.?changer|multifaceted|meticulous|intricate|paramount|transformative|"
    r"elevate|embark|supercharge|harness|ever-evolving|tapestry|realm|beacon)\w*\b",
    r"\b(?:it(?:'s| is) (?:worth noting|important to note)|at the end of the day|when it comes to|"
    r"at its core|in today's world|the reality is|the truth is|in terms of|in order to|"
    r"going forward|let's dive in|here's the thing|needless to say)\b",
    r"\bnot just (?:a|an|the)\b",
    r"\b(?:isn't|is not|aren't) (?:about |a |an )?[^.]{0,40}[,.] (?:it's|It's|it is|It is) \b",
    r"\b(?:crucial|vital|pivotal|game-changing)(?:ly)? \b",
]

CONJ = r"(?:and|but|or|nor|so|yet|then|which|not|if|unless|whether|was|is|as|plus|in|to|with|without|for|on|at|from)\b"


def undash(s, cell=False):
    """Replace the dashes in one sentence or table cell with plain punctuation."""
    parts = re.split(r"\s*—\s*", s)
    if len(parts) == 1:
        return s
    if len(parts) == 3 and not parts[2].startswith((".", ",", "?")):
        # paired dashes: "ties A — Stripe, PayPal — to the GL" -> "ties A (Stripe, PayPal) to the GL"
        return f"{parts[0]} ({parts[1]}) {parts[2]}"
    out = parts[0]
    for nxt in parts[1:]:
        if re.match(r"(?:Required|Recommended|Optional)\**$", out.split()[-1] if out.split() else ""):
            out += ". " + nxt[0].upper() + nxt[1:]        # "Recommended — sets ..." -> "Recommended. Sets ..."
        elif re.match(CONJ, nxt):
            out += ", " + nxt                             # "the tax — and if" -> "the tax, and if"
        elif cell:                                        # "Period being closed — exact dates" -> "(exact dates)"
            body, tail = re.match(r"(.*?)([.!?]*\**)$", nxt).groups()
            out += f" ({body}){tail}"
        else:
            out += ": " + nxt                             # "hasn't been billed — you used" -> ": you used"
    return out


def plain(text):
    """Edit a finished page to the writing rules: dashes to plain punctuation, contrasts to
    statements, filler cut. Applied to the whole page, line by line."""
    out = []
    for line in text.splitlines():
        if line.startswith(("<!--", "[")):
            out.append(line)
            continue
        if "—" in line:
            if line.startswith("|"):
                cells = line.strip().strip("|").split("|")
                line = "|" + "|".join(" " + undash(c.strip(), cell=True) + " " for c in cells) + "|"
            else:
                line = " ".join(undash(s) for s in sentences(line))
        line = re.sub(r"\s*–\s*", " to ", line)
        # "a legal document, not just a request" -> "a legal document as well as a request"
        line = re.sub(r",? not just (a|an|the)\b", r" as well as \1", line)
        line = re.sub(r"\bin order to\b", "to", line)
        line = re.sub(r"\b[Ii]t is worth noting that\s*", "", line)
        line = re.sub(r",\s*,", ",", line).replace(" ,", ",")
        out.append(line)
    return "\n".join(out) + ("\n" if text.endswith("\n") else "")


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
            return rows
    return []


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


def paragraphs(block):
    return [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", block) if p.strip()]


def linkify(text, names, me):
    def sub(m):
        n = m.group(1)
        return f"[{n}]({n}.md)" if n in names and n != me else m.group(0)
    text = re.sub(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`", sub, text)
    return re.sub(r"(?<![\[\w/(-])([a-z0-9]+(?:-[a-z0-9]+)+)(?![\w\]-]|\.md)", sub, text)


# ---------------------------------------------------------------- skills

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


def parse_description(desc):
    parts = re.split(r"(?<=[.!?])\s+(?=" + MARK + ")", desc)
    d = {"what": "", "when": "", "examples": [], "not_for": [], "produces": ""}
    for i, p in enumerate(parts):
        low = p.lower()
        if p.startswith(("Triggers include", "Also trigger", "Trigger for")):
            d["examples"] += [e.rstrip(",.") for e in re.findall(r"(?<=[\s:(])'([^']{3,90}?)'(?=[,.;)\s])", p)]
        elif low.startswith("do not use"):
            item = re.sub(r"^Do (?:not|NOT) use (?:this skill )?(?:for |when |to )?", "", p)
            item = re.sub(r"\bor for\b", "or", item)
            d["not_for"].append(cap(item))
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


def plain_words(card):
    """The card's 'In plain words' paragraph, if it has one."""
    m = re.search(r"\*\*In plain words:\*\*\s*(.+?)(?:\n\s*\n|\Z)", card, re.S)
    if not m:
        return ""
    return clean(re.sub(r"\s+", " ", m.group(1)))


def output_names(text):
    block = section(text, r"Step \d+ — Output|Outputs")
    names = re.findall(r"\*\*Sheet \d+: ([^*]+?)\*\*", block)
    if not names:
        block = block.split("**Coverage sheet")[0]
        names = re.findall(r"^- \*\*([^*]+?)\*\*", block, re.M)
    out = []
    for n in names:
        n = re.sub(r"\s*—.*$", "", n).strip().rstrip(".,:")
        n = re.sub(r"\s*\(.*?\)\s*$", "", n)
        if n and len(n) <= 60 and not any(re.search(p, n) for p in LEAKS) and n not in out:
            out.append(n)
    if any(re.search(r"QuickBooks|Xero|NetSuite|Sage|Dynamics|Zoho", o) for o in out):
        return []
    return out[:10]


def title_of(card, name):
    for m in re.finditer(r"^# (.+)$", card, re.M):
        t = m.group(1).strip()
        if not re.match(r"(ONBOARDING|PART )", t):
            return re.sub(r"\s*(?:\(Mosofin\)|—\s*Mosofin Seed|\(Mosofin Seed\)|— Mosofin)\s*$", "", t)
    return name.replace("-", " ").capitalize()


def ask_rows(card):
    """(question, why) rows from whichever intake table the card has."""
    rows = table_after(card, "Ask", "Why it matters")
    if rows:
        return [(clean(r[1]), clean(r[2])) for r in rows if len(r) >= 3 and clean(r[1])]
    rows = table_after(card, "What to confirm", "Required?")
    if rows:
        out = []
        for r in rows:
            if len(r) >= 2 and clean(r[0]):
                item = re.sub(r"^(?:Confirm|Confirm any) ", "", clean(r[0]).replace("**", ""))
                if re.match(r"(?:Scope|Manual evidence|Profile|Any profile)", item, re.I):
                    continue
                need = re.sub(r"\s*—.*$", "", clean(r[1]).replace("**", "")) or "Recommended"
                out.append((cap(item), need))
        return out
    return []


def upload_rows(card):
    rows = table_after(card, "Upload", "Needed?")
    if rows:
        return [(clean(r[0]), clean(r[1]), clean(r[2])) for r in rows if len(r) >= 3 and clean(r[0])]
    rows = table_after(card, "| Input | Format | Required")
    out = []
    for r in rows:
        if len(r) < 3 or not clean(r[0]):
            continue
        item, fmt, need = clean(r[0]).replace("**", ""), clean(r[1]), clean(r[2]).replace("**", "")
        if not re.search(r"CSV|XLSX|PDF|chat|image|text|[Aa]ny|scan|photo", fmt):
            if fmt and fmt.lower() != "export":
                item = f"{item} ({fmt if re.match(r"[A-Z]{2}", fmt) else fmt[0].lower() + fmt[1:]})"
            fmt = "Typed in the chat" if re.search(r"\bdate\b|threshold|policy|rate\b", item, re.I) else "CSV or XLSX"
        out.append((item, need, fmt))
    return out


def build_skill_page(name, rows, names, wf_names):
    card = read(os.path.join(SKILLS, name, "SKILL.md"))
    mpath = os.path.join(SKILLS, name, "references", "method.md")
    method = read(mpath) if os.path.exists(mpath) else card
    desc = re.search(r'^description:\s*"?(.*?)"?\s*$', card, re.M).group(1).replace('\\"', '"')
    d = parse_description(desc)
    wave, pct, blurb = rows.get(name, (0, None, ""))

    L = [f"# {title_of(card, name)}", ""]
    if blurb:
        L += [f"> {blurb.rstrip('.')}.", ""]
    facts = [f"**Skill:** `{name}`"]
    if wave:
        facts.append(f"**Area:** {GROUPS[wave]}")
    if pct is not None:
        facts.append(f"**Automated with Mosofin connected:** {pct}%")
    facts.append("**Read-only**")
    L += ["  ·  ".join(facts), ""]

    L += ["## What it does", "", clean(d["what"]) or blurb, ""]
    pw = plain_words(card)
    if pw:
        L += [f"**In plain words:** {pw}", ""]

    L += ["## When to use it", ""]
    if d["when"]:
        L += [clean(d["when"]), ""]
    elif d["examples"]:
        pass
    else:
        L += [f"Use it when you need {blurb[0].lower() + blurb[1:].rstrip('.')}.", ""]
    if d["examples"]:
        L += ["Typical requests, or anything like them:", ""] + [f"- \"{e}\"" for e in d["examples"][:8]] + [""]
    nf = [clean(x) for x in d["not_for"] if clean(x)]
    if nf:
        L += ["Not for:", ""] + [f"- {x}" for x in nf] + [""]

    L += ["## What it asks you first", ""]
    asks = ask_rows(card)
    old_style = bool(table_after(card, "What to confirm", "Required?")) and not table_after(card, "Ask", "Why it matters")
    if asks:
        if old_style:
            L += ["Before it reads anything, it confirms these with you, in one message:", "",
                  "| It confirms | Needed? |", "|---|---|"]
        else:
            L += ["Before it reads anything, it asks, in one message:", "", "| It asks | Why |", "|---|---|"]
        L += [f"| {q} | {w} |" for q, w in asks] + [""]
    else:
        L += ["Before it reads anything, it asks which company and which period the work is for, "
              "whether to use your Mosofin connection or files you supply, and for the facts the "
              "books cannot hold, such as a policy, a threshold or a date. It reads the answers "
              "back and waits for your yes.", ""]

    L += ["## With or without Mosofin", "",
          "With a Mosofin workspace connected, and only after you agree, the skill reads the "
          "figures from your own books. Without a connection it runs the same analysis on "
          "files you upload, and the output says which figures came from where.", ""]
    ups = upload_rows(card)
    if ups:
        L += ["If you upload the data yourself:", "", "| Upload | Needed? | Format |", "|---|---|---|"]
        L += [f"| {a} | {b or 'Recommended'} | {c or 'XLSX, CSV or PDF'} |" for a, b, c in ups] + [""]
    else:
        need = [q for q, w in asks if re.match(r"Required", w)] if asks and old_style else []
        if need:
            L += ["If you upload the data yourself, each item marked Required above comes from you: "
                  + ", ".join(cap(re.sub(r"\s*—.*$", "", n)).rstrip(".") for n in need[:6])
                  + ". Ledger detail and listings go in as CSV or XLSX exports, statements and documents "
                  "as PDF or CSV, and short facts typed into the chat.", ""]
        else:
            L += ["If you upload the data yourself, it asks for the ledger detail and listings the "
                  "work needs as CSV or XLSX exports, statements and third-party documents as PDF or "
                  "CSV, and short facts typed into the chat.", ""]
    L += ["Every uploaded file is checked before any work starts: that it is the right kind "
          "of document, for the right company and period, and usable.", ""]

    L += ["## What you get", ""]
    outs = output_names(method)
    produces = cap(clean(d["produces"])) if d["produces"] else ""
    names_an_output = re.search(r"\b(?:[Pp]roduces|[Oo]utputs|[Pp]roposes|[Rr]ecommends|[Dd]rafts|[Bb]uilds|"
                                r"workpaper|schedule|report|log|checklist|entries|memo|pack|model)\b", produces)
    if not names_an_output:
        L += ["A workpaper you can keep, as an Excel file if you want one or as tables in the "
              "chat, with every figure traced to where it came from. Anything that would change "
              "the books is a proposal for a person to approve.", ""]
    if produces:
        L += [produces, ""]
    outs = [o for o in outs if not re.match(r"[Cc]overage", o)]
    if len(outs) >= 2:
        L += ["The workpaper has these sheets:", ""] + [f"- {o}" for o in outs] + [""]
    L += ["Every run ends with a coverage sheet: what was checked, what was estimated, and what "
          "could not be done and why.", ""]

    rules = [clean(b) for b in bullets(section(card, "Rules that never bend"))]
    rules = [r for r in rules if r]
    if not rules:
        rules = ["**Asks before using Mosofin.** A connected account is not permission to read it.",
                 "**Never writes, updates or deletes anything, in any system.** Every entry, "
                 "message or change it suggests is a proposal for a person to approve.",
                 "**Says what it could not check.** Anything it could not verify is listed, "
                 "with what you would need to supply."]
    L += ["## What it never does", ""] + [f"- {r}" for r in rules] + [""]

    L += footer()
    return linkify("\n".join(L), names, name)


# ---------------------------------------------------------------- workflows

def wf_rows():
    rows = {}
    for line in read(os.path.join(WORKFLOWS, "README.md")).splitlines():
        m = re.match(r"\| (\d+) \| \[([a-z0-9-]+)\]\([^)]*\) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|", line)
        if m:
            rows[m.group(2)] = (int(m.group(1)), m.group(3).strip(), m.group(4).strip(), m.group(5).strip())
    return rows


def schedule_words(trigger):
    t = trigger.replace(" + webhook", "")
    if t == "webhook":
        return "It runs on demand: whenever another step sends it a request, for example when a file arrives."
    t = t.replace("days 1–7", "on days 1 to 7 of each month")
    return (f"It runs {t} on its own, and whenever another step sends it a request.")


def build_workflow_page(name, rows, names, wf_names):
    md = read(os.path.join(WORKFLOWS, name, "README.md"))
    title = re.search(r"^# (.+)$", md, re.M).group(1).strip()
    intro = paragraphs(md.split("\n**Read-only.**")[0])[1:]
    num, trigger, reads, proposes = rows.get(name, (0, "webhook", "none", ""))
    read_names = re.findall(r"`([a-z_]+)`", reads)
    read_words = [READ_WORDS.get(r, r.replace("_", " ")) for r in read_names]

    L = [f"# {title} (workflow)", ""]
    if proposes:
        how = "on a schedule or on demand" if trigger != "webhook" else "on demand"
        L += [f"> Checks your books {how} and proposes {proposes.rstrip('.')}.", ""]
    L += ["  ·  ".join([f"**Workflow:** `{name}`", "**Runs in:** n8n", "**Read-only**"]), ""]

    L += ["## What it does", ""] + [clean(p).replace("(file fallback)", "(or from a file you send)")
                                       .replace("file fallback", "a file you send as fallback") for p in intro] + [""]
    L += ["It runs inside n8n, an automation tool you host, and reads your books only through "
          "your Mosofin connection, the same read-only connection the skills use.", ""]

    L += ["## When it runs", "", schedule_words(trigger), ""]
    if read_words:
        L += ["With a Mosofin data source set, it reads " + ", ".join(read_words[:-1])
              + (" and " if len(read_words) > 1 else "") + read_words[-1] + " through your Mosofin connection. "
              "Where a file you send covers the same data, the Mosofin figures are used first and the file is the fallback.", ""]
    else:
        L += ["It works from the files you send it and needs no Mosofin read.", ""]

    L += ["## What you send it", ""]
    files = table_after(md, "File role", "What it must be")
    if files:
        L += ["| File | What it must be | Required |", "|---|---|---|"]
        L += [f"| `{r[0].strip('`')}` | {clean(r[1])} | {r[3]} |" for r in files if len(r) >= 4] + [""]
    else:
        L += ["Nothing beyond the run settings: it reads what it needs from Mosofin.", ""]
    L += ["Every file is checked on its content before any work: right kind of document, right "
          "company, usable. A rejected required file stops the run; a rejected optional file is "
          "skipped and named in the result.", ""]

    L += ["## What you can change", "",
          "Every setting sits in one place in the workflow, and any of them can be overridden "
          "for a single run by the request that starts it.", ""]
    settings = table_after(md, "Setting", "Default", "Meaning")
    settings = [r for r in settings if len(r) >= 3 and r[0].strip("`") not in ("data_source_id",)]
    if settings:
        L += ["| Setting | Meaning |", "|---|---|"]
        L += [f"| `{r[0].strip('`')}` | {clean(r[2]).replace('echoed in the envelope', 'shown in the result')} |" for r in settings] + [""]

    L += ["## What comes back", "",
          "One structured result (JSON), for the next step in your automation to use: an email tool, a "
          "chat post, a dashboard or another workflow. It holds the findings, the totals, what "
          "could not be done and why, and the proposed actions, each waiting for a person's "
          "approval.", ""]
    if proposes:
        L += [f"**It proposes:** {cap(proposes.rstrip('.'))}.", ""]

    L += ["## What it never does", "",
          "- **Never posts, sends, pays or changes anything.** The only outbound calls are reads through your Mosofin connection.",
          "- **Never acts on its own proposals.** An email draft, a journal entry, a hold or a payment is handed to a person to approve first.",
          "- **Never takes a file at face value.** Each file is checked on its content, not its name, before it is used.", ""]
    L += footer()
    return linkify("\n".join(L), names, name)


# ---------------------------------------------------------------- index, sitemap, gate

def wf_file(n):
    return "workflow-" + n + ".md"


def footer():
    return ["---", "", "[All skills and workflows](README.md) · [Sitemap](sitemap.md) · "
            "[Getting started](../README.md#getting-started)", "",
            "<!-- Generated by .github/build-pages.py. Edit the skill or workflow, not this page. -->", ""]


def build_index(names, rows, wf_names, wfs):
    L = ["# Mosofin finance skills: what each one does", "",
         f"One page per skill ({len(names)}) and per n8n workflow ({len(wf_names)}). Each page says "
         "what it is for, when to use it, what it asks you, what to upload if you are not connected "
         "to Mosofin, and what you get back.", "",
         "Everything here is read-only: it reads and analyses, and anything that would change "
         "your books comes back as a proposal for a person to approve.", "",
         "**Automated** is the share of a skill's checks that run without asking you for a "
         "document when a Mosofin workspace is connected. The rest need evidence that is not in "
         "the books, such as a bank statement or a contract. Within each group, skills are listed "
         "with the most automated first; the [sitemap](sitemap.md) lists them alphabetically.", "",
         "Some skills sit close together. `quickbooks-ar-aging-collections` is `ar-aging-and-collections` "
         "for books kept in QuickBooks; `ar-cash-application-lockbox` is `cash-application` for a lockbox "
         "or bank file; `ap-invoice-processing-and-3way-match` is the whole invoice cycle around "
         "`three-way-match`. Each page's *Not for* line says which neighbour to use instead.", ""]
    by = {}
    for n in names:
        by.setdefault(rows.get(n, (0, None, ""))[0], []).append(n)
    for wave in sorted(by):
        L += [f"## {GROUPS.get(wave, 'Other skills')}", "", "| Skill | What it's for | Automated |", "|---|---|---:|"]
        for n in sorted(by[wave], key=lambda x: -(rows.get(x, (0, 0, ""))[1] or 0)):
            _, pct, blurb = rows.get(n, (0, None, ""))
            L.append(f"| [`{n}`]({n}.md) | {blurb} | {'' if pct is None else str(pct) + '%'} |")
        L.append("")
    L += ["## n8n workflows", "", "Checks that run on a schedule or on demand inside n8n, an "
          "automation tool you host, with every setting in one place and one result for the next "
          "tool to pick up. *Webhook* means another step can start the check by sending it a request.", "",
          "| Workflow | Runs | Proposes |", "|---|---|---|"]
    for n in sorted(wf_names, key=lambda x: wfs.get(x, (99,))[0]):
        _, trigger, _, proposes = wfs.get(n, (0, "", "", ""))
        L.append(f"| [`{n}`]({wf_file(n)}) | {trigger} | {proposes} |")
    L += ["", "[Sitemap](sitemap.md)", "", "<!-- Generated by .github/build-pages.py. -->", ""]
    return "\n".join(L)


def build_sitemap_md(names, rows, wf_names, wfs):
    L = ["# Sitemap", "", f"Every page under `skill-pages/` in alphabetical order: {len(names)} skills, "
         f"{len(wf_names)} workflows and this index.", "",
         "- [Index](README.md)", ""]
    by = {}
    for n in names:
        by.setdefault(rows.get(n, (0, None, ""))[0], []).append(n)
    for wave in sorted(by):
        L += [f"## {GROUPS.get(wave, 'Other skills')}", ""]
        L += [f"- [{n}]({n}.md)" for n in sorted(by[wave])] + [""]
    L += ["## n8n workflows", ""] + [f"- [{n} (workflow)]({wf_file(n)})" for n in sorted(wf_names, key=lambda x: wfs.get(x, (99,))[0])] + [""]
    L += ["<!-- Generated by .github/build-pages.py. -->", ""]
    return "\n".join(L)


def last_changed(paths):
    """Date of the last commit touching any of the paths, else today."""
    try:
        out = subprocess.run(["git", "log", "-1", "--format=%cs", "--"] + paths, cwd=ROOT,
                             capture_output=True, text=True, timeout=20).stdout.strip()
        return out or date.today().isoformat()
    except Exception:
        return date.today().isoformat()


def build_sitemap_xml(names, wf_names):
    entries = [("README.md", last_changed(["README.md", "workflows/README.md"]), "1.0")]
    entries += [(n + ".md", last_changed([f"skills/{n}"]), "0.8") for n in names]
    entries += [(wf_file(n), last_changed([f"workflows/{n}"]), "0.6") for n in wf_names]
    L = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for fn, d, pr in entries:
        L += ["  <url>", f"    <loc>{BASE_URL}{fn}</loc>", f"    <lastmod>{d}</lastmod>",
              f"    <priority>{pr}</priority>", "  </url>"]
    L += ["</urlset>", ""]
    return "\n".join(L)


def gate(fn, text, sections):
    """Quality rules every page must pass. Returns a list of problems."""
    p = []
    for pat in LEAKS:
        m = re.search(pat, text)
        if m:
            p.append(f"{fn}: method detail in page: {m.group(0)!r}")
    heads = [l for l in text.splitlines() if l.startswith("## ")]
    if heads != sections:
        p.append(f"{fn}: sections are {heads}, expected {sections}")
    for i, h in enumerate(sections):
        body = section(text, re.escape(h[3:]))
        words = len(re.sub(r"[|*`#>-]", " ", body).split())
        if words < 12:
            p.append(f"{fn}: section {h!r} is thin ({words} words)")
    if re.search(r"\b[Tt]he user\b", text):
        p.append(f"{fn}: says 'the user' instead of 'you'")
    for pat in SLOP:
        m = re.search(pat, text)
        if m:
            p.append(f"{fn}: writing rule: {m.group(0)!r}")
            break
    if re.search(r"\|[ \t]*\|", text):
        p.append(f"{fn}: empty table cell")
    for line in text.splitlines():
        if line.count("**") % 2:
            p.append(f"{fn}: unbalanced bold in {line[:60]!r}")
            break
    for m in re.finditer(r"\]\(([a-z0-9-]+\.md)\)", text):
        if not os.path.exists(os.path.join(OUT, m.group(1))) and m.group(1) not in KNOWN:
            p.append(f"{fn}: dead link {m.group(1)}")
    if not text.startswith("# "):
        p.append(f"{fn}: no title")
    return p


KNOWN = set()


def main():
    check = "--check" in sys.argv
    names = sorted(n for n in os.listdir(SKILLS) if os.path.isfile(os.path.join(SKILLS, n, "SKILL.md")))
    wf_names = sorted(n for n in os.listdir(WORKFLOWS) if os.path.isfile(os.path.join(WORKFLOWS, n, "README.md")))
    rows, wfs = readme_rows(), wf_rows()
    KNOWN.update({n + ".md" for n in names} | {wf_file(n) for n in wf_names} | {"README.md", "sitemap.md"})

    files = {}
    for n in names:
        files[n + ".md"] = build_skill_page(n, rows, set(names), set(wf_names))
    for n in wf_names:
        files[wf_file(n)] = build_workflow_page(n, wfs, set(names), set(wf_names))
    files["README.md"] = build_index(names, rows, wf_names, wfs)
    files["sitemap.md"] = build_sitemap_md(names, rows, wf_names, wfs)
    files["sitemap.xml"] = build_sitemap_xml(names, wf_names)
    for fn in files:
        if fn != "sitemap.xml":
            files[fn] = plain(files[fn])

    problems = []
    for n in names:
        problems += gate(n + ".md", files[n + ".md"], SKILL_SECTIONS)
        if n not in rows:
            problems.append(f"{n}: no row in the README skill tables")
    for n in wf_names:
        problems += gate(wf_file(n), files[wf_file(n)], WORKFLOW_SECTIONS)
        if n not in wfs:
            problems.append(f"{n}: no row in workflows/README.md")

    os.makedirs(OUT, exist_ok=True)
    on_disk = {f for f in os.listdir(OUT) if f.endswith((".md", ".xml"))}
    if check:
        for fn, text in files.items():
            p = os.path.join(OUT, fn)
            if fn == "sitemap.xml":
                continue  # lastmod moves with every commit; the .md sitemap is the checked one
            if not os.path.exists(p) or read(p) != text:
                problems.append(f"{fn}: out of date; run .github/build-pages.py")
        for fn in sorted(on_disk - set(files)):
            problems.append(f"{fn}: no matching skill or workflow")
    else:
        for fn, text in files.items():
            with open(os.path.join(OUT, fn), "w", encoding="utf-8") as f:
                f.write(text)
        for fn in on_disk - set(files):
            os.remove(os.path.join(OUT, fn))

    for p in problems:
        print("PROBLEM", p)
    print(f"{len(names)} skill pages, {len(wf_names)} workflow pages, {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
