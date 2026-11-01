"""Cross-check every author-year citation in the thesis drafts against the literature corpus.

Usage:  python literature/check_citations.py            (all drafts)
        python literature/check_citations.py FILE ...   (specific .md / .docx files)

Writes literature/_corpus/citation_report.md. Run build_corpus.py first.
Status per citation:
    OK        in Zotero, full text available -> claim can be checked against the paper
    NO-TEXT   in Zotero, metadata only       -> attach the PDF in Zotero to make it checkable
    LOCAL     only a PDF in literature/      -> add to Zotero before citing (no citekey yet)
    YEAR?     author found, but not with that year -> likely a year typo, or a different paper
    MISSING   no item by that first author  -> add to Zotero (or the citation may be wrong)
Parsing is heuristic (regex over prose): it can miss unusual citation formats and occasionally
picks up a non-citation; treat the report as a checklist, not ground truth.
"""
import json
import re
import subprocess
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CORPUS = HERE / "_corpus"

DEFAULT_DRAFTS = sorted((ROOT / "texts").glob("_*.md")) + [
    ROOT / "texts/literatire reviews/1.Gaze cueing effect 1.2.docx",
    ROOT / "texts/literatire reviews/Sense of agency 1.1.docx",
    ROOT / "texts/literatire reviews/2.2Intentional actions, movement and SoA.docx",
    ROOT / "texts/Onwoing_work.md",
]

NAME = r"(?:(?:[Dd]e|[Dd]i|[Vv]an|[Vv]on|[Ll]e|[Dd]a|[Dd]el)\s)?[A-Z][\w'’\-]+"
YEAR = r"((?:19|20)\d{2})[a-z]?"
# narrative: "Moore, Wegner, and Haggard (2009)", "Friesen and Kingstone (1998)", "Jones et al. (2010)"
NARRATIVE = re.compile(rf"\b({NAME})(?:(?:,\s|\s(?:and|&)\s|,\s(?:and|&)\s){NAME})*(?:\set\sal\.)?['’]?s?\s\({YEAR}")
# parenthetical piece: "Driver et al., 1999" / "Friesen & Kingstone, 1998" / "see Dalmaso et al., 2020"
PIECE = re.compile(rf"({NAME})(?:(?:,\s|\s(?:and|&)\s|,\s(?:and|&)\s){NAME})*(?:\set\sal\.)?,?\s{YEAR}")
SKIP = {"Experiment", "Exp", "Table", "Figure", "Part", "Chapter", "Section", "Step", "In", "See", "The", "As",
        "For", "January", "July", "August", "September", "October", "June", "Note", "NOTE", "Fig", "E", "Version",
        "Accordingly", "Finally", "However", "Moreover", "Similarly", "Together", "Indeed", "Using", "Thus",
        "Consistent", "Unlike", "Although", "While", "Following", "Later", "Earlier", "Recently", "Here"}


def ascii_lower(s):
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()


def read_text(path):
    if path.suffix == ".docx":
        out = subprocess.run(["pandoc", str(path), "-t", "plain", "--wrap=none"], capture_output=True)
        text = out.stdout.decode("utf-8", errors="ignore")
    else:
        text = path.read_text(encoding="utf-8", errors="ignore")
    # drop a trailing reference list so only in-text citations are checked
    m = re.search(r"\n\s*(#+\s*)?(References|Reference list|Bibliography)\s*\n", text)
    if m:
        text = text[:m.start()]
    return re.split(r"\n\s*1\.\s+[A-Z][\w\-]+, [A-Z]\.", text)[0]  # numbered ref list (GC 1.2)


def extract(text):
    cites = []
    for m in NARRATIVE.finditer(text):
        cites.append((m.group(1), m.group(2), m.start()))
    for par in re.finditer(r"\(([^()]*?(?:19|20)\d{2}[^()]*?)\)", text):
        for piece in par.group(1).split(";"):
            for m in PIECE.finditer(piece):
                cites.append((m.group(1), m.group(2), par.start()))
    out = []
    for name, year, pos in cites:
        first = name.split()[-1] if name.split()[0].lower() in {"de", "di", "van", "von", "le", "da", "del"} else name
        first = re.sub(r"['’]s$", "", first)
        if first in SKIP or first.isupper() and len(first) > 1 and len(first) < 4:
            continue
        line = text.count("\n", 0, pos) + 1
        out.append((first, year, line))
    return out


_heads = {}


def _local_head(key):
    """First ~900 chars of a local-only PDF (title, authors, year) for matching."""
    if key not in _heads:
        txt = (CORPUS / "papers" / f"{key}.txt").read_text(encoding="utf-8", errors="ignore")
        body = txt[txt.find("## FULL TEXT"):]
        _heads[key] = ascii_lower(body[:900])
    return _heads[key]


def lookup(index, name, year):
    n = ascii_lower(name).replace("’", "'")
    hits = [e for e in index if e["surnames"] and (ascii_lower(e["surnames"][0]) == n
                                                   or ascii_lower(e["surnames"][0]).endswith(" " + n)
                                                   or ascii_lower(e["surnames"][0]).replace(" ", "") == n.replace(" ", ""))]
    exact = [e for e in hits if e["year"] == year]
    if exact:
        return ("OK" if any(e["fulltext"] for e in exact) else "NO-TEXT"), exact
    local = [e for e in index if e["type"] == "local-pdf" and _local_head(e["key"]).count(n) and year in _local_head(e["key"])]
    if local:
        return "LOCAL", local
    if hits:
        return "YEAR?", hits
    return "MISSING", []


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    index = json.loads((CORPUS / "index.json").read_text(encoding="utf-8"))
    files = [Path(a) for a in sys.argv[1:]] or [p for p in DEFAULT_DRAFTS if p.exists()]
    seen = defaultdict(lambda: {"where": set()})
    for f in files:
        for name, year, line in extract(read_text(f)):
            seen[(name, year)]["where"].add(f"{f.name}:{line}" if f.suffix == ".md" else f.name)

    rows = []
    for (name, year), info in seen.items():
        status, hits = lookup(index, name, year)
        rows.append((status, name, year, hits, info["where"]))
    order = {"MISSING": 0, "YEAR?": 1, "LOCAL": 2, "NO-TEXT": 3, "OK": 4}
    rows.sort(key=lambda r: (order[r[0]], r[1], r[2]))

    counts = defaultdict(int)
    for r in rows:
        counts[r[0]] += 1
    with open(CORPUS / "citation_report.md", "w", encoding="utf-8") as out:
        out.write("# Citation report\n\nGenerated by `check_citations.py` from: "
                  + ", ".join(f.name for f in files) + "\n\n"
                  + " · ".join(f"**{k}** {counts[k]}" for k in order) + "\n\n"
                  "| status | cited as | corpus match | where |\n|---|---|---|---|\n")
        for status, name, year, hits, where in rows:
            match = "; ".join(f"`{e['key']}`" + ("" if status != "YEAR?" else f" ({e['year']})") for e in hits[:4])
            locs = ", ".join(sorted(where)[:4]) + (" …" if len(where) > 4 else "")
            out.write(f"| {status} | {name} {year} | {match} | {locs} |\n")
    print(" · ".join(f"{k} {counts[k]}" for k in order), "->", CORPUS / "citation_report.md")


if __name__ == "__main__":
    main()
