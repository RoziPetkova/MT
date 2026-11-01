"""Build a searchable plain-text corpus of the Zotero library.

Output: literature/_corpus/
    index.md          one row per item: citekey, authors, year, title, journal, collections, full text y/n
    index.json        same, machine-readable (used by check_citations.py)
    papers/<citekey>.txt   metadata header + abstract + your Zotero annotations + full text with
                           ===== [PDF page N] ===== markers (PDF page index, not journal page number)

Read-only: works on a temp copy of zotero.sqlite; never writes to the Zotero data directory.
Re-run any time the library changes:  python literature/build_corpus.py
"""
import json
import os
import re
import sys
import shutil
import sqlite3
import subprocess
import tempfile
import unicodedata
from pathlib import Path

ZOTERO = Path.home() / "Zotero"
HERE = Path(__file__).resolve().parent
OUT = HERE / "_corpus"
BIB = HERE / "My Library" / "My Library.bib"  # latest Better BibTeX export of the whole library
EXPORT_FILES = HERE / "My Library" / "files"   # PDF copies made by the export; same PDFs as Zotero storage

STOPWORDS = {"a", "an", "the", "on", "of", "in", "and", "to", "for", "is", "does", "do", "how",
             "what", "why", "when", "with", "are", "can", "from", "by", "at", "as"}


def ascii_lower(s):
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()


def norm_title(t):
    return re.sub(r"[^a-z0-9]", "", ascii_lower(t or ""))[:60]


def _prefer(mapping, k, key):
    """Duplicate library items export as key, key-1, ...; keep the unsuffixed key."""
    if k not in mapping or re.search(r"-\d+$", mapping[k]) and not re.search(r"-\d+$", key):
        mapping[k] = key


def parse_bib(path):
    """Map DOI / normalized title -> citekey from the Better BibTeX export."""
    by_doi, by_title = {}, {}
    if not path.exists():
        return by_doi, by_title
    text = path.read_text(encoding="utf-8", errors="ignore")
    for m in re.finditer(r"^@\w+\{([^,]+),(.*?)^\}", text, re.S | re.M):
        key, body = m.group(1).strip(), m.group(2)
        doi = re.search(r"^\s*doi\s*=\s*\{(.+?)\},?\s*$", body, re.M)
        title = re.search(r"^\s*title\s*=\s*\{(.+?)\},?\s*$", body, re.M)
        if doi:
            _prefer(by_doi, doi.group(1).lower(), key)
        if title:
            _prefer(by_title, norm_title(title.group(1).replace("{", "").replace("}", "")), key)
    return by_doi, by_title


def make_key(creators, title, year):
    """Better BibTeX default style: surname_firstword_year."""
    surname = ascii_lower(creators[0][0]) if creators else "anon"
    surname = re.sub(r"[^a-z]", "", surname) or "anon"
    words = [w for w in re.findall(r"[a-z0-9]+", ascii_lower(title or "")) if w not in STOPWORDS]
    return f"{surname}_{words[0] if words else 'untitled'}_{year or 'nd'}"


def ascii_path(pdf):
    """pdftotext on Windows can't open non-ASCII filenames (e.g. 'Kühn_2013.pdf'); use a temp copy."""
    if str(pdf).isascii():
        return pdf
    tmp = Path(tempfile.gettempdir()) / "corpus_nonascii.pdf"
    shutil.copy(pdf, tmp)
    return tmp


def pdf_text(pdf):
    """pdftotext keeps page breaks (\\f) so we can mark pages; None if it fails."""
    try:
        out = subprocess.run(["pdftotext", "-enc", "UTF-8", str(ascii_path(pdf)), "-"],
                             capture_output=True, timeout=120)
    except (OSError, subprocess.TimeoutExpired):
        return None
    txt = out.stdout.decode("utf-8", errors="ignore")
    if len(txt.strip()) < 500:
        return None
    txt = re.sub(r"(\w)-\n(\w)", r"\1\2", txt)  # re-join words hyphenated across lines
    pages = txt.split("\f")
    return "\n".join(f"\n===== [PDF page {i}] =====\n{p.strip()}" for i, p in enumerate(pages, 1) if p.strip())


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    tmp = Path(tempfile.gettempdir()) / "zotero_corpus_copy.sqlite"
    shutil.copy(ZOTERO / "zotero.sqlite", tmp)
    db = sqlite3.connect(tmp)
    db.row_factory = sqlite3.Row
    by_doi, by_title = parse_bib(BIB)

    def fields(item_id):
        rows = db.execute("""select f.fieldName, v.value from itemData d
                             join fields f using(fieldID) join itemDataValues v using(valueID)
                             where d.itemID=?""", (item_id,))
        return {r["fieldName"]: r["value"] for r in rows}

    def collection_path(cid):
        parts = []
        while cid:
            r = db.execute("select collectionName, parentCollectionID from collections where collectionID=?",
                           (cid,)).fetchone()
            parts.append(r["collectionName"])
            cid = r["parentCollectionID"]
        return " / ".join(reversed(parts))

    items = db.execute("""select i.itemID, i.key, t.typeName from items i join itemTypes t using(itemTypeID)
                          where t.typeName not in ('attachment','note','annotation')
                          and i.itemID not in (select itemID from deletedItems)""").fetchall()

    (OUT / "papers").mkdir(parents=True, exist_ok=True)
    for old in (OUT / "papers").glob("*.txt"):
        old.unlink()

    records = []
    for it in items:
        f = fields(it["itemID"])
        title = f.get("title", "")
        year = (re.search(r"\d{4}", f.get("date", "")) or [None])[0]
        rows = db.execute("""select c.lastName, c.firstName, t.creatorType from itemCreators ic
                             join creators c using(creatorID) join creatorTypes t using(creatorTypeID)
                             where ic.itemID=? order by ic.orderIndex""", (it["itemID"],)).fetchall()
        authors_only = [r for r in rows if r["creatorType"] == "author"]  # editors are not first authors
        creators = [(r["lastName"], r["firstName"]) for r in (authors_only or rows)]
        doi = (f.get("DOI") or "").lower()
        key = by_doi.get(doi) or by_title.get(norm_title(title)) or make_key(creators, title, year)

        colls = [collection_path(r["collectionID"]) for r in db.execute(
            "select collectionID from collectionItems where itemID=?", (it["itemID"],))]
        tags = [r["name"] for r in db.execute(
            "select t.name from itemTags it join tags t using(tagID) where it.itemID=?", (it["itemID"],))]

        # full text: prefer pdftotext (page markers), fall back to Zotero's own cache
        text, source = None, None
        atts = db.execute("""select i.itemID, i.key, a.path, a.contentType from itemAttachments a
                             join items i using(itemID) where a.parentItemID=?""", (it["itemID"],)).fetchall()
        annots = []
        for a in atts:
            folder = ZOTERO / "storage" / a["key"]
            if text is None and a["contentType"] == "application/pdf" and a["path"]:
                pdf = folder / a["path"].replace("storage:", "")
                if pdf.exists():
                    text, source = pdf_text(pdf), "pdftotext"
            if text is None and (folder / ".zotero-ft-cache").exists():
                text = (folder / ".zotero-ft-cache").read_text(encoding="utf-8", errors="ignore")
                source = "zotero-ft-cache (no page markers)"
            for r in db.execute("""select text, comment, pageLabel from itemAnnotations
                                   where parentItemID=? order by sortIndex""", (a["itemID"],)):
                if r["text"] or r["comment"]:
                    annots.append((r["pageLabel"], r["text"], r["comment"]))
        notes = [re.sub(r"<[^>]+>", " ", r["note"]) for r in db.execute(
            "select note from itemNotes where parentItemID=?", (it["itemID"],))]

        records.append(dict(it=it, f=f, title=title, year=year, creators=creators, key=key, colls=colls,
                            tags=tags, text=text, source=source, annots=annots, notes=notes))

    # The library holds unfiled duplicates of most papers (pre-merge copies). Group by title, keep the
    # copy that is filed in a collection as canonical, and borrow full text / annotations from the others.
    groups = {}
    for r in records:
        groups.setdefault(norm_title(r["title"]) or r["it"]["key"], []).append(r)
    # PDFs sitting in literature/ (not necessarily in Zotero): use them to fill missing full text,
    # and index the ones that match no Zotero item so they are still searchable.
    local = {}
    for pdf in sorted(set(HERE.rglob("*.pdf")) | set(HERE.rglob("*.PDF"))):
        if OUT in pdf.parents or EXPORT_FILES in pdf.parents:
            continue
        head = subprocess.run(["pdftotext", "-l", "2", str(ascii_path(pdf)), "-"], capture_output=True).stdout
        local[pdf] = re.sub(r"[^a-z0-9]", "", ascii_lower(head.decode("utf-8", errors="ignore")))
    matched = set()

    def merge_group(grp):
        grp.sort(key=lambda r: (not r["colls"], not r["text"]))
        canon = grp[0]
        for other in grp[1:]:
            if not canon["text"] and other["text"]:
                canon["text"], canon["source"] = other["text"], other["source"]
            canon["annots"] += other["annots"]
            canon["notes"] += other["notes"]
            canon["tags"] = sorted(set(canon["tags"]) | set(other["tags"]))
        return canon

    def local_hits(canon):
        """(position, pdf) for local PDFs whose first pages contain this item's title or DOI."""
        nt = norm_title(canon["title"])[:40]
        doi = re.sub(r"[^a-z0-9]", "", (canon["f"].get("DOI") or "").lower())
        hits = []
        for pdf, flat in local.items():
            pos = [i for i in ((flat.find(nt) if len(nt) > 20 else -1),
                               (flat.find(doi) if len(doi) > 8 else -1)) if i >= 0]
            if pos:
                hits.append((min(pos), pdf))
        return sorted(hits)

    canons = [merge_group(g) for g in groups.values()]
    # Pass 1: a title/DOI near the top of a PDF is that PDF's own title. Pass 2: further down it may be
    # a reference-list entry of another paper (e.g. a commentary citing it), so later matches only
    # use PDFs that no item claimed in pass 1 (Nature-style first pages start with the previous
    # article, which pushes the real title down).
    all_hits = {id(c): local_hits(c) for c in canons}
    claimed = {pdf for hits in all_hits.values() for pos, pdf in hits if pos < 2500}
    for c in canons:
        near = [pdf for pos, pdf in all_hits[id(c)] if pos < 2500]
        far = [pdf for pos, pdf in all_hits[id(c)] if pos >= 2500 and pdf not in claimed]
        use = near or far
        matched.update(use)
        if use and not c["text"]:
            c["text"], c["source"] = pdf_text(use[0]), f"local PDF: {use[0].relative_to(HERE)}"

    index, used_keys = [], set()
    for canon in canons:
        it, f, title, year, creators = canon["it"], canon["f"], canon["title"], canon["year"], canon["creators"]
        colls, tags, text, source = canon["colls"], canon["tags"], canon["text"], canon["source"]
        annots, notes = canon["annots"], canon["notes"]
        key = base = canon["key"]
        n = 1
        while key in used_keys:  # disambiguate like BBT: key, keya, keyb ...
            key = base + "abcdefghij"[n - 1]
            n += 1
        used_keys.add(key)
        authors = "; ".join(f"{l}, {fn}" if fn else l for l, fn in creators)
        venue = f.get("publicationTitle") or f.get("bookTitle") or f.get("publisher") or f.get("university") or ""
        entry = dict(key=key, authors=authors, surnames=[ascii_lower(l) for l, _ in creators], year=year,
                     title=title, venue=venue, doi=f.get("DOI", ""), type=it["typeName"], collections=colls,
                     tags=tags, fulltext=bool(text), annotations=len(annots), zotero_key=it["key"])
        index.append(entry)

        with open(OUT / "papers" / f"{key}.txt", "w", encoding="utf-8") as out:
            out.write(f"CITEKEY: {key}\nAUTHORS: {authors}\nYEAR: {year}\nTITLE: {title}\n"
                      f"VENUE: {venue} {f.get('volume', '')}({f.get('issue', '')}) {f.get('pages', '')}\n"
                      f"DOI: {f.get('DOI', '')}\nTYPE: {it['typeName']}\nCOLLECTIONS: {' | '.join(colls)}\n"
                      f"TAGS: {', '.join(tags)}\nFULLTEXT SOURCE: {source}\n")
            if f.get("abstractNote"):
                out.write(f"\n## ABSTRACT\n{f['abstractNote']}\n")
            if annots:
                out.write("\n## MY ZOTERO ANNOTATIONS\n")
                for page, t, c in annots:
                    out.write(f"- p.{page}: {(t or '').strip()}" + (f"  [comment: {c.strip()}]" if c else "") + "\n")
            if notes:
                out.write("\n## MY ZOTERO NOTES\n" + "\n".join(n.strip() for n in notes) + "\n")
            out.write("\n## FULL TEXT\n" + (text or "[no full text in Zotero]") + "\n")

    for pdf in local:
        if pdf in matched:
            continue
        text = pdf_text(pdf)
        stem = re.sub(r"[^a-z0-9]+", "_", ascii_lower(pdf.stem)).strip("_")[:50]
        key = f"local_{stem}"
        index.append(dict(key=key, authors="", surnames=[], year=None, title=f"[NOT IN ZOTERO] {pdf.name}",
                          venue="", doi="", type="local-pdf", collections=[], tags=[], fulltext=bool(text),
                          annotations=0, zotero_key=None, local_path=str(pdf.relative_to(HERE))))
        with open(OUT / "papers" / f"{key}.txt", "w", encoding="utf-8") as out:
            out.write(f"CITEKEY: (none - NOT IN ZOTERO; add it to Zotero before citing)\nFILE: {pdf.relative_to(HERE)}\n"
                      f"FULLTEXT SOURCE: local PDF\n\n## FULL TEXT\n{text or '[could not extract text]'}\n")

    index.sort(key=lambda e: (e["surnames"][0] if e["surnames"] else "", e["year"] or ""))
    (OUT / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=1), encoding="utf-8")
    with open(OUT / "index.md", "w", encoding="utf-8") as md:
        n_ft = sum(e["fulltext"] for e in index)
        md.write(f"# Literature corpus index\n\n{len(index)} items, {n_ft} with full text. "
                 "Generated by `build_corpus.py` — do not edit by hand.\n\n"
                 "| citekey | first author | year | title | FT | notes | collection |\n|---|---|---|---|---|---|---|\n")
        for e in index:
            first = e["authors"].split(";")[0]
            md.write(f"| {e['key']} | {first} | {e['year'] or ''} | {e['title'][:90].replace('|', '/')} | "
                     f"{'✓' if e['fulltext'] else '—'} | {e['annotations'] or ''} | "
                     f"{'; '.join(c.split(' / ')[-1] for c in e['collections'])} |\n")
    print(f"{len(index)} items, {sum(e['fulltext'] for e in index)} with full text -> {OUT}")


if __name__ == "__main__":
    main()
