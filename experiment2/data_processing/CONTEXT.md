# Experiment 2 — Data Processing Context
> This file is for Claude. Read at the start of every session before doing any work.

## Quick orientation
- **Experiment:** SoA_Gaze_Mouse — same gaze cuing paradigm as Exp 1 but with mouse movements instead of keyboard
- **Raw source:** `Untitled.txt` (192MB, UTF-16-LE, skip row 0, tab-delimited) — NEVER modify
- **Master file:** `allData_exp2.xlsx` — full data, correct participant IDs, 107760 rows × 79 cols
- **Notes:** `procedure_notes.txt` (how), `data_notes.txt` (what/counts)
- **Exp 1 reference:** `experiment1/data_processing2/raw+processed.xlsx`, tab `cleaned` — formulas for gaze_congruency and action_consistency

## Pipeline status
| Pipeline | Folder | Last file | Steps remaining |
|----------|--------|-----------|-----------------|
| Experimental data | `exp_data/` | `08_ranova_input.xlsx` (test rANOVA done) | Step 07b: decide ss17 exclusion → re-run rANOVA → Step 09: time bins → Step 10: ANCOVA |
| Questions data | `questions/` | `03_excl_likert.xlsx` | Step 04: 3×3 table → Step 05: ANOVA |

## Participants
- **N = 60** (30 A script: ids 1–30, 30 B script: ids 40–70)
- **Missing:** participant 53 (Martina Stefova) — no .edat2 file collected
- Full name↔ID mapping in `data_notes.txt`

## Exclusions (final)
| Criterion | Excluded | Remaining |
|-----------|----------|-----------|
| Low accuracy < 85% | ss 1, 2, 45, 59 | 56 subjects |
| Careless Likert (dominant% > 75 AND range ≤ 0.5) | ss 9, 15, 22, 42, 49, 65, 66 | 49 subjects |
| Error trials (acc = 0) | 319 trials | 7913 trials |

Kept despite Likert flag: ss 41 (range=1.98), ss 54 (range=2.00) — discriminate between conditions.
Both pipelines use the same subject exclusions. Likert report: `questions/02_likert_report.xlsx`.

## Critical column reference
| Column | Meaning |
|--------|---------|
| `Subject` | Participant ID (A: 1–30, B: 40–70) |
| `ExperimentName` | Starts with A_ or B_ |
| `Procedure[Trial]` | Condition: actionC, actionNC, controlLeft, controlRight |
| `GazeColorConsistency` | E-Prime encoded — DO NOT USE (see below) |
| `Running[SubTrial]` | Last slide shown: ListLeft or ListRight |
| `ColorSlideLeft.ACC/RT` | Use when Running[SubTrial] = ListLeft |
| `ColorSlideRight.ACC/RT` | Use when Running[SubTrial] = ListRight |
| `Choice[Trial]` | Mouse direction chosen by participant: "Left" or "Right" (action conditions only) |
| `SlideXeroA.RT` | Initiation time (action conditions) |
| `XeroDur` | Initiation time (control conditions, 350–550ms) |
| `Running[Trial]` | 'Questions' for question procedure rows |
| `Running[SubTrial]` | 'QuestionsList' for question response rows |
| `QControl.RESP` | Question rating (Likert 1–7) |
| `Qs` | Question text (Bulgarian/Cyrillic) |

## Row filtering logic
- **Experimental trials:** `Running[Trial] != 'Questions'`
- **Question responses:** `Running[SubTrial] == 'QuestionsList'`
- **One row per experimental trial:** `Procedure[SubTrial]` = "pro" AND `Running[Trial]` = "Exp" AND `pic` in ["6L","6R"]
- Note: `Running[Trial]` = "Exp" filter is required — without it, practice trials (PracticeL, 20 per subject) are included

## Calculated columns (exp_data Step 05)
These are derived from raw columns — do NOT use E-Prime's `GazeColorConsistency`.

```
actual_color_location = "right" if colorLeft == "white" else "left"
actual_gaze_dir       = "left"  if Running[SubTrial] == "ListLeft" else "right"
wanted_gaze_dir       = Choice[Trial].lower()           # action conditions
                      = "left"  if Procedure[Trial] == "controlLeft"  # control
                      = "right" if Procedure[Trial] == "controlRight" # control

gaze_congruency    = "congruent"    if actual_color_location == actual_gaze_dir else "incongruent"
action_consistency = "consistent"   if Procedure[Trial] == "actionC"
                   = "inconsistent" if Procedure[Trial] == "actionNC"
                   = "control"      if Procedure[Trial] in ["controlLeft", "controlRight"]
```

## SPSS format (exp_data Step 06)
File: `06_spss_input.xlsx` — columns: `sub`, `w1`, `w2`, `rt`

| Variable | Meaning | Coding |
|----------|---------|--------|
| w1 | gaze_congruency | incongruent=0, congruent=1 |
| w2 | action_consistency | inconsistent=0, consistent=1, control=2 |

## SPSS RT trimming (exp_data Step 07) — DONE
Script: `SPSS CUTOFF/2w.SPS`
- Input: `c:\trim\data.sav` — open `06_spss_input.xlsx` in SPSS, File → Save As → .sav
- Cutoff: mean ± 2 SD per subject per condition
- Output: `c:\trim\rptmeas.sav` — wide format mean RT per subject × condition, ready for rANOVA
- Result: 7913 → 7587 trials (removed 326, 4.12%)

Still to check: whether any subject's overall mean RT > group mean + 2 SD (subject-level exclusion, as in Exp 1).

## Known data quirks
- `GazeColorConsistency` in raw data has THREE values: "congruent", "consinstent" (typo for inconsistent), "offline". The "offline" category appears even in action conditions and is unreliable — always recalculate from `actual_color_location` vs `actual_gaze_dir` instead.
- `Running[SubTrial]` is NaN on question rows — not mixed into experimental data
- B-script subject 14 in E-Prime = Maria Lobachova = participant 54 (HAS data)
- B-script subject 15 in E-Prime = no file = participant 53 (Martina Stefova, MISSING)
- `colorLeft`/`colorRight` values: "white" = no color (blank side), color name = target side

## Reuse for Experiment 3
Copy this folder structure and note templates. Update:
- Participant IDs and names in `data_notes.txt`
- Raw file path in `procedure_notes.txt`
- Pipeline steps if the design changes
- This CONTEXT.md with new experiment details
