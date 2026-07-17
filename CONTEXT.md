# Master Thesis Context — GC + Agency

## Research Topic
Gaze Cuing (GC) and Sense of Agency (SoA): how gaze direction affects sense of agency over actions.
Supervisor: Armina.

---

## Experiment 1 — SoA_Color_Gaze (COMPLETED)

**Task:** Color discrimination with gaze cuing; keyboard responses (a=left, d=right).
**N:** 55 collected → 45 after exclusions (see below).
**Scripts:** A and B versions (counterbalanced). E-Prime files in `experiment1/52 ss-roz/`.
**Trials:** 168 experimental + 48 question trials per subject.

**Exclusions:**
- 3 removed for technical problems (ss 1, 17, 45)
- 7 removed for ACC < 80-85% (ss 3, 6, 8, 10, 15, 19, 21) — threshold TBC with Armina
- 3 more removed from Q data for clicking >75% same button (ss 18, 23, 25, 55)
- 2 more removed for mean RT > grand mean + 2*SD (ss 2, 51)
- Final N = 45 → 7560 trials → 7083 correct (ACC=1) → 6732 after outlier cut

**Grand mean RT:** 525.91ms, SD = 92.20ms, cutoff = 710.30ms

**Key columns (exp1):**
- action-consistency: consistent / inconsistent / control
- gaze congruency: congruent / incongruent
- Coding: incongruent=0, congruent=1; inconsistent=0, consistent=1, control=2
- SlideXeroA.RT = initiation time (action conditions)
- XeroDur = initiation time (control conditions, 350–550ms range)

**Analysis:**
- Main: 2×3 rANOVA (gaze congruency × action consistency)
- Effect size: subtract congruent from incongruent per action consistency level → 3-level rANOVA
- Time bins: 5 bins, 3 ANOVAs (consistent/inconsistent/control) with congruency × bin
- Questions: 3 Q-types × 3 action consistency → ANOVA on ratings
- ANCOVA: initiation time as covariate

**Files:** `experiment1/data_processing1/` and `experiment1/data_processing2/`
- SPSS outlier script saves to `c:\trim\`; fix: `SELECT IF NOT (SYSMIS(mean)).`
- Results in JASP files in `data_processing1/data_stat/`
- Written up in `texts/` and `IrelandPaper/`

---

## Experiment 2 — SoA_Gaze_Mouse (IN PROGRESS)

**Task:** Same gaze cuing but with mouse movements instead of keyboard.
**N:** 60 subjects — 30 from A script (ids 1–30), 30 from B script (ids 40–70; subject 54 missing = B-script ss 15, no data file).
**Scripts:** `A_SoA_Color_Gaze_Roz_second.es2` and `B_SoA_Color_Gaze_Roz_second.es2`
**Trials:** 168 experimental + 144 question rows (48 trials × 3 questions) per subject.

**Raw data:** `experiment2/data/SoA_Gaze_Mouse-all/`
- Individual `.edat2` files per subject
- Merged: `Untitled1.emrg2` → `Untitled.txt` (192MB, UTF-16-LE, tab-delimited, skip row 0 = file path)

**Processing files:** `experiment2/data_processing/`
- `allData_exp2.xlsx` — full export, 107760 rows × 79 cols, original subject IDs (do not modify)
- `exp_data.xlsx` — experimental trial rows (10080 rows), subject IDs fixed, has `acc` + `rt` columns
- `questions_data.xlsx` — question trial rows (8640 rows), subject IDs fixed
- `questions_all.xlsx` — question rows with all 79 columns, subject IDs fixed
- `notes.txt` — processing log

**Subject ID mapping:**
- A script (ids 1–30): Viktoria Koteva, Natalie Ivanova, Iva Pushkarova, Dilyana Petrova, Radina Spasova, Iana Tsinko, Denis Traichev, Dayana Pavlova, Diyora Ivanova, Beloslava Tsareva, Nina Cholakova, Mihail Dimitrov, Sofia Kaucheva, Denitsa Georgieva, Sofia Simeonova, Giorgia Matteo, Maria Lobocheva, Stella Ivanova, Radina Ivanova, Kristina Popova, Anastasiia Razborova, Nevena Borisova, Daria Koleva, Nikolai Shentsev, Daniela Masarlieva, Bogdana Boncheva, Yoanna Angelcheva, Melany Karshakova, Devora Peneva, Blagovest Kolev
- B script (ids 40–70, missing 54): Olga Ivanova(40), Raya Zarkova(41), Nikoleta Kamburova(42), Elitsa Dialkova(43), Daria Georgieva(44), Boris Filipov(45), Ivalina Petrova(46), Patrisia Tsolova(47), Viktoria Kostova(48), Julia Nenova(49), Todor Savin(50), Jana Damyanova(51), Martin Danielov(52), Martina Stefova(53), [54 missing=Maria Lobachova], Desislava Borisova(55), Atanas Atanasov(56), Mykhailo Zhyzhka(57), Lyuben Mishev(58), Sophia Hadjiiska(59), Ryutaro Yamamoto(60), Amelia Dimitrova(61), Tsvetalina Ivanova(62), Nadezda Katelieva(63), Magdalena Valcheva(64), Nikolaya Nikolova(65), Dana Genkova(66), Denitsa Dimitrova(67), Radina Tsvetkova(68), Mila Nikolova(69), Radostina Stoyanova(70)

**Subject ID fix logic:**
- A-script rows come first in file; rows 0–5039 in exp_data (0–4319 in questions_data) = A script → ids unchanged
- Rows 5040+ in exp_data (4320+ in questions_data) = B script → E-Prime id + 39

**Key columns (exp2):**
- `Column1`: gaze direction / last slide shown — `ListLeft` or `ListRight`
- `ColorSlideLeft.ACC` / `.RT`: used when `Column1 == 'ListLeft'`
- `ColorSlideRight.ACC` / `.RT`: used when `Column1 == 'ListRight'`
- `acc`: merged accuracy (created from above)
- `rt`: merged RT (created from above)
- `Procedure[Trial]`: condition — `actionC`, `actionNC`, `controlLeft`, `controlRight`
- `GazeColorConsistency`: `congruent`, `inconsistent` (typo: "consinstent"), `offline`
- `SlideXeroA.RT`: initiation time (action conditions)
- `XeroDur`: initiation time (control conditions)
- `corR`: correct response key (`a`=left, `d`=right)
- `colorLeft` / `colorRight`: color shown on each side
- `pic`: image file shown
- `Qs`: question text (Bulgarian/Cyrillic)
- `QControl.RESP`: question response rating
- `QControl.RT`: question response time

**Questions (3 types, in Bulgarian):** shown after every experimental trial, 3 questions per trial.

**TODO — following experiment 1 pipeline:**
1. Calculate gaze direction column (actual gaze dir from results)
2. Calculate action consistency column (consistent/inconsistent/control)
3. Calculate gaze congruency column (congruent/incongruent)
4. Remove error trials (acc=0)
5. Remove participants with ACC < threshold (ask Armina: 80% or 85%)
6. SPSS outlier removal: mean RT > grand mean + 2*SD
7. rANOVA (same design as exp1)
8. Time bin analysis
9. Question analysis: 3×3 table
10. ANCOVA with initiation time as covariate

---

## Experiment 3
Folder exists, empty. Not yet conducted.

---

## Toolchain
- **Experiment software:** E-Prime 2 (`.es2`, `.edat2`, `.ebs2`, `.emrg2`)
- **Data merging:** E-DataAid → text export
- **Processing scripts:** Python + pandas (scripts in Claude scratchpad)
- **Statistics:** JASP + SPSS (outlier removal via c:\trim\ script)
- **Notes:** notes.txt per experiment

## Literature
`literature/` folder:
- AgencyandJointAttention.pdf
- Intentional binding and the sense of agency.pdf
- review_attention and sense of agency.pdf
- Eye did this.pdf
- The Impact of eye contact.pdf
- Subliminal priming of actions.pdf

## Key decisions / open questions
- ACC exclusion threshold: 80% or 85%? → ask Armina
- GazeColorConsistency has a typo in data: "consinstent" instead of "consistent"
- Exp2 subject 75 has no data (B-script ss 15 missing)
