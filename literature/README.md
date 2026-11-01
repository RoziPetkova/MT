# Literature corpus & citation tools

Three scripts turn the Zotero library into something that can be searched and checked quickly.
They only **read** Zotero (via a temp copy of `~/Zotero/zotero.sqlite`), so the library itself is never changed.

| Script | What it does | Output |
|---|---|---|
| `build_corpus.py` | One text file per paper: metadata, abstract, **your Zotero highlights/comments**, full text with `[PDF page N]` markers. Merges the unfiled duplicate copies in the library, and also picks up PDFs in this folder that aren't in Zotero. | `_corpus/index.md`, `_corpus/index.json`, `_corpus/papers/<citekey>.txt` |
| `check_citations.py` | Scans every draft (`texts/_*.md`, the three latest lit-review `.docx`, `Onwoing_work.md`) for author–year citations and checks each one against the corpus | `_corpus/citation_report.md` |
| `search_corpus.py` | Finds passages for checking a claim, returning the citekey, PDF page and context | printed to the terminal |

```bash
python literature/build_corpus.py                     # re-run after adding papers / PDFs to Zotero (~1 min)
python literature/check_citations.py                  # re-run after editing drafts
python literature/search_corpus.py "sensory attenuation" "N1"           # all terms in the same passage
python literature/search_corpus.py --key chambon "fluency"              # restrict to citekeys containing 'chambon'
```

**Citation-report statuses:**
- **OK:** full text available, so the claim can be checked.
- **NO-TEXT:** in Zotero but without a PDF. Attach one in Zotero.
- **LOCAL:** only a PDF in this folder. Add it to Zotero.
- **YEAR?:** the author is in Zotero but not with that year. Likely a typo or a different paper.
- **MISSING:** not in Zotero at all.

The parsing is heuristic, so use the report as a checklist.

**Citekeys** come from `Agency and CG - merged.bib`, matched by DOI or title. Items not in the `.bib` get a key in the same Better BibTeX style (`surname_firstword_year`). Re-export the `.bib` after adding papers to Zotero so the keys match what pandoc will use.

**Page numbers** are PDF page indices, not the journal page printed on the page. Check the printed page before quoting.

`_corpus/` contains copyrighted full text, so it is git-ignored. Regenerate it on any machine that has the Zotero library.
