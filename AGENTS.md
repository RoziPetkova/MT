# AGENTS.md — Master's Thesis: Gaze Cueing & Sense of Agency

Read this before doing any work in this repo. It's written for any AI coding/writing agent
(Claude Code, Cursor, Codex, etc.) picking up this project cold, on any machine.

**Supersedes `CONTEXT.md`** (root) — that file is outdated (predates most of the pipeline work
below) and should not be trusted for current status. It may still contain useful historical
detail on E-Prime column meanings / subject-ID mapping quirks if you need to go back to raw data.

## Who's working on this, and how

Researcher (referred to as "Roz" in old filenames) is a Cognitive Science master's student,
supervised by Armina. Comfortable with rANOVA, ANCOVA, JASP, Python/pandas. Runs a full pipeline:
E-Prime → Python (pandas) → JASP for stats.

**Working-style rules — read before editing anything:**
- **Verify every number against the actual source (JASP file or CSV), never from memory or by
  assuming a prior write-up is still correct.** This project has a long history of catching real
  numeric/logical errors this way (stale descriptive tables, wrong post-hoc pairs, Holm-vs-Bonferroni
  mismatches, mislabeled effect sizes). Treat every number in a results file as unverified until
  cross-checked.
- **Don't unilaterally "harmonize" things across experiments.** If asked to make pipelines/results
  consistent, that's scoped to what's functionally necessary (e.g. exclusion thresholds, stats
  method) — NOT license to also unify cosmetic/structural differences that legitimately differ per
  experiment (e.g. Exp2/3 have a mouse/touch-specific column Exp1's keypress design doesn't need).
  Ask before extending "make X consistent" beyond what was literally named.
- **When editing prose the user has drafted/pasted, don't restructure sentences unless asked.** If
  told to "just add the numbers," add them as bracketed insertions into the existing sentence —
  don't rewrite, reorder, or add new explanatory clauses. Flag any typo fixes made along the way
  rather than silently bundling them in.
- **Citations:** verify any citation is real before treating it as usable (a fabricated citation was
  caught once this project). When adding a new citation from a web search, say so explicitly and
  recommend the user verify exact volume/page/author details in Zotero before citing — don't present
  search-result summaries as confirmed bibliographic facts.
- Zotero + Better BibTeX + pandoc is the citation pipeline for the markdown write-up (see below) —
  don't suggest abandoning Zotero.

## Project structure

Root: `C:\Users\Kaloyan Zdravkov\Desktop\Congitive Science\MasterThesis\GC + agency\`
Git remote: `github.com/RoziPetkova/MT` (branch `main`). Repo history was rebuilt once (2026-07-17)
to strip oversized files — `.gitignore` excludes recordings, raw E-Prime merge exports (`.edat2`,
`.emrg*`, `Untitled.txt`), and raw pipeline checkpoints. **These exist ONLY on the original local
machine, with no other backup** — if working from a different machine, raw data may not be present.

Each experiment folder (`experiment1/`, `experiment2/`, `experiment3/`) has a Python pipeline
(`data_processing*/exp_data/pipeline.ipynb` + a parallel `questions/pipeline.ipynb`) that produces
a canonical `jasp/analysis.csv` and a `.jasp` file with the actual ANOVA/ANCOVA/correlation
analyses. `analysis_outputs/` holds the cross-experiment combined JASP files and CSVs
(`mixed_anova_all_experiments.jasp/csv` for RT, `Q-data_mixed_anova_all_experiments.jasp/csv` for
questionnaire data).

## The design, in brief

Gaze-cueing paradigm crossed with an action-outcome-consistency manipulation, to test whether
sense of agency (SoA) modulates the gaze-cueing effect. Two factors: **Gaze Congruency**
(congruent/incongruent — does the target appear where the gaze pointed) × **Action Consistency**
(consistent/inconsistent/control — did the gaze end up matching the participant's own chosen
direction). Explicit SoA measured via 3 post-trial Likert items (caused/controlled/predicted,
Bulgarian). Implicit SoA proxy = the gaze-congruency RT effect itself, standardized per subject as
Cohen's *d* per condition. Three experiments differ only in the direction-selection response
modality: **Exp1 = keypress, Exp2 = mouse click, Exp3 = touchscreen tap.**

Exp2's direction-selection response is a **single discrete mouse click**, hit-tested against two
static zones at click time — there is no continuous cursor-trajectory data in the export, despite
the "richer/continuous movement" framing used in some theoretical discussion (that framing is about
click *initiation time* being a more extended, richer-sampled measure than a keypress, not about
having actual trajectory data).

## Current final N's (verify against `jasp/analysis.csv` row count if in doubt — these have moved before)

- **Exp1: 41** (not 40 — an earlier pipeline run excluded a subject for borderline RT-outlier status;
  a later re-run's trimming shifted slightly and that subject was retained; 41 is current and
  matches both `analysis.csv` and the written-up text)
- **Exp2: 48**
- **Exp3: 49**
- **Combined cross-experiment N: 138**

Questions-pipeline N's are larger and NOT the analysis-relevant number (accuracy exclusion was
removed from the questions pipeline since exp_data already filters those subjects out via merge).

## Statistical methodology — current, settled decisions

- **Post-hoc correction: Bonferroni, everywhere.** (An earlier phase of this project briefly used
  Holm — if you see a memory or old note saying "Holm, not Bonferroni," that has been **explicitly
  superseded**; a full pass was done across all four results files converting every post-hoc p-value
  to the `bonferroni` column of the corresponding JASP table. Bonferroni is also what the RT sections
  always used, so this made things consistent.)
- **Greenhouse-Geisser correction on every within-subject term with df > 1**, including interactions
  — not just 3-level main effects. Check Mauchly on interaction rows too.
- Composite explicit-SoA score = **unweighted mean** of the three ipsatized items per condition
  (justified via PCA showing single-component loading).
- **Ipsatization = within-person mean-centering only** (subtract each participant's own mean across
  their conditions), NOT dividing by personal SD. Cite Cattell (1944), Hicks (1970); a related
  "within-person centering across experiments" claim should cite Rudnev (2021) — NOT any
  "Villa et al." citation, which was fabricated in an earlier draft and removed.
- Individual-experiment regressions of composite-on-*d* are mathematically redundant with the
  equivalent correlation (one predictor = same test) — don't double-report both. Only the
  combined/cross-experiment regression (Experiment entered as an additional factor) is a genuinely
  different test worth reporting separately from its correlation.
- ANCOVA covariate = `mean_initiation_time`, computed from **action trials only** (consistent +
  inconsistent; excludes control, since control's "pre-gaze interval" is an externally-imposed
  random delay, not a real behavioral initiation measure) — same for all 3 experiments, one
  covariate, no per-experiment asymmetry. Centered (grand-mean, not within-person) before entry
  purely so lower-order effects are evaluated at a realistic covariate value, not zero — cite
  Aiken & West (1991) and/or Kraemer & Blasey (2004) for this, not a within-person-centering
  citation (that's a different technique, see ipsatization above).
- A significant Factor × covariate interaction in an ANCOVA = a homogeneity-of-regression-slopes
  violation, i.e. a caveat on that model's validity — not a substantive finding. Both Exp1 and Exp2
  show this for the Action × initiation-time term; text should flag it as a likely artefact (control
  condition's "initiation time" isn't measuring the same construct as active trials) rather than
  interpret it theoretically.
- Naive per-cell CIs are invalid for repeated-measures data (ignore shared-subject structure); use
  paired-difference CIs from post-hoc tests, or JASP's Morey-corrected within-subject CI option.

## Write-up status (as of this session)

All four results files (`texts/_02.1.exp1_full.md`, `_02.2.exp2_full_RAW.md`, `_02.3.exp3_full_RAW.md`,
`_02.4.q_data_cross_experiment_results_RAW.md`, `_02.4.rt_cross_experiment_results_RAW.md`) have been
through a full number-by-number audit against their JASP/CSV sources and had every discrepancy found
fixed. Treat them as currently accurate, but **any future edit should still be re-verified against
source** rather than assumed correct indefinitely — this is a living document, not a one-time
guarantee.

Exp2's file additionally has an extended theoretical discussion (in the Correlation section and the
Questionnaire Analyses section) built up through back-and-forth this session, covering: why
initiation time correlates with RT in Exp2 but not Exp1 (reliability, not variance — Freeman &
Ambady, 2010; Hedge, Powell, & Sumner, 2018), why control's correlation is a bit stronger than
active conditions' (effector-switching cost — Philipp & Koch, 2005), and why the questionnaire
Action-Consistency effect is smaller/less differentiated in Exp2 than Exp1 (cue-integration dilution
— Synofzik, Vosgerau, & Newen, 2008; Moore & Fletcher, 2012). None of these citations have been
independently verified against a database — check before treating as final.

`texts/2.structure.md` is the authoritative thesis outline (chapter/section numbering) — read it
before restructuring any write-up content.

## JASP file extraction — pitfalls if you script against `.jasp` files directly

`.jasp` files are zip archives: `analyses.json` has the analysis list/options,
`resources/{id}/jaspResults.json` has cached results (readable via Python `zipfile` + `json`).
- **Always look up table columns by name** (`colNames`/`rowNames` lists), never by fixed position —
  position-based extraction has produced silently-wrong output before (impossible eta-squared
  values, F=0.000).
- **`JaspExtraOptions_N_Encoded` factor-level codes are NOT consistent across different analyses or
  files**, even within the same thesis. Before trusting any decode of which code means "consistent"
  vs. "inconsistent" vs. "control" (or which experiment number), verify empirically against a table
  with a known expected direction (e.g. consistent > inconsistent > control ordering) — don't assume
  the same mapping carries over from a different JASP file.
- I (an AI agent) can read/rename cached JASP analyses but cannot run JASP's own R computation
  engine to produce new results from scratch — new analyses have to be run in the JASP GUI by the
  user, or recomputed directly from the flat CSV in Python/pandas/scipy (generally the safer
  ground-truth method anyway for correlations, t-tests, and descriptives).
