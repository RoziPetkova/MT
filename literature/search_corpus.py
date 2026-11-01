"""Find passages in the literature corpus to check a claim.

Usage:
    python literature/search_corpus.py "intentional binding" "delay"         all terms, same passage
    python literature/search_corpus.py --key chambon "angular gyrus"        only citekeys containing 'chambon'
    python literature/search_corpus.py --regex "SOA of \\d+ ms"              regular expression
Options: --key SUBSTR  --window N (chars of context, default 300)  --max N (hits per paper, default 3)

Each hit prints the citekey, the PDF page (page index of the PDF file, which may differ from the
journal page number printed on the page) and the surrounding text.
"""
import argparse
import re
import sys
from pathlib import Path

PAPERS = Path(__file__).resolve().parent / "_corpus" / "papers"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("terms", nargs="+")
    ap.add_argument("--key", default="")
    ap.add_argument("--regex", action="store_true")
    ap.add_argument("--window", type=int, default=300)
    ap.add_argument("--max", type=int, default=3)
    a = ap.parse_args()

    pats = [re.compile(t if a.regex else re.escape(t).replace(r"\ ", r"\s+"), re.I) for t in a.terms]
    total = 0
    for f in sorted(PAPERS.glob("*.txt")):
        if a.key.lower() not in f.stem.lower():
            continue
        text = f.read_text(encoding="utf-8", errors="ignore")
        body_start = text.find("## FULL TEXT")
        hits, last_end = [], -1
        header_end = text.find("\n## ")  # skip the metadata header block
        for m in pats[0].finditer(text, max(header_end, 0)):
            lo, hi = max(0, m.start() - a.window), m.end() + a.window
            if lo < last_end:
                continue
            ctx = text[lo:hi]
            if all(p.search(ctx) for p in pats[1:]):
                page = re.findall(r"\[PDF page (\d+)\]", text[:m.start()])
                where = ("p." + page[-1]) if page and m.start() > body_start else (
                    "abstract/notes" if m.start() < body_start else "no page info")
                hits.append((where, re.sub(r"\s+", " ", ctx).strip()))
                last_end = hi
            if len(hits) >= a.max:
                break
        for where, ctx in hits:
            print(f"\n[{f.stem}  {where}]\n  …{ctx}…")
        total += len(hits)
    print(f"\n{total} passage(s).")


if __name__ == "__main__":
    main()
