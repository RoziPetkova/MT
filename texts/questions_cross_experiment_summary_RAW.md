# Cross-Experiment Summary — Questionnaire (SoA Ratings) Results

[NOTE TO SELF — working document. This consolidates the questionnaire-data trends flagged separately in each experiment's Analyses section (see the [NOTE TO SELF] markers in `_03.exp1_full_RAW.md`, `_03.exp2_full_RAW.md`, `_03.exp3_full_RAW.md`). Intended destination: the cross-experiment / General Discussion chapter (see `2.structure.md`, Chapter 6) — this file is raw material for that section, not finished prose, and it is a candidate for absorbing the "Question type within each Consistency level" decomposition that is currently repeated in full in each experiment's chapter.]

All three experiments used the same 3 (Question type: caused, controlled, predicted) × 3 (Action Consistency: consistent, inconsistent, control) repeated-measures ANOVA on the questionnaire ratings, with Greenhouse–Geisser correction throughout. Final samples: Experiment 1, N = 40; Experiment 2, N = 48; Experiment 3, N = 49.

## Omnibus effects across experiments

| Effect | Experiment 1 | Experiment 2 | Experiment 3 |
|---|---|---|---|
| Action Consistency | F(1.85, 72.09) = 80.23, *p* < .001, η²ₚ = .673 | F(1.73, 81.10) = 30.57, *p* < .001, η²ₚ = .394 | F(1.64, 78.71) = 29.13, *p* < .001, η²ₚ = .378 |
| Question type | F(1.70, 66.47) = 20.36, *p* < .001, η²ₚ = .343 | F(1.64, 77.01) = 3.52, *p* = .043, η²ₚ = .070 | F(1.87, 89.85) = 1.93, *p* = .153, η²ₚ = .039 (n.s.) |
| Consistency × Question type | F(2.33, 90.76) = 26.31, *p* < .001, η²ₚ = .403 | F(2.18, 102.31) = 11.14, *p* < .001, η²ₚ = .192 | F(2.41, 115.46) = 6.27, *p* = .001, η²ₚ = .116 |

**Action Consistency** — the manipulation check — holds in all three experiments; the paradigm reliably shifts explicit SoA ratings regardless of response modality. The effect size roughly halves from Experiment 1 to Experiment 2, then stays essentially flat into Experiment 3 (.673 → .394 → .378). This is not a smooth three-point gradient — it looks like a single step down after Experiment 1, followed by a plateau, rather than a continuous decline tracking the keypress → mouse → touch embodiment progression.

**Question type** — the questions' overall differences in endorsement, collapsed across condition — shows the cleanest monotonic trend in the whole dataset: strongly significant in Experiment 1, weak but still significant in Experiment 2, and gone entirely by Experiment 3. Taken at face value, this says the three questions become *less distinguishable from one another in general level* as the direction-selection response becomes more embodied — the opposite of what an embodiment-amplifies-everything account would predict, and worth flagging explicitly rather than glossing over.

**Interaction** — also shrinks monotonically (.403 → .192 → .116) but stays significant throughout, meaning the two decompositions below remain worth reporting in every experiment even as the effect gets smaller.

## Direction A: does Action Consistency affect each question differently?

Simple main effects of Consistency, within each question:

| Question | Experiment 1 | Experiment 2 | Experiment 3 |
|---|---|---|---|
| Caused | F(2,78) = 87.62, *p* < .001 | F(2,94) = 33.06, *p* < .001 | F(2,96) = 26.33, *p* < .001 |
| Controlled | F(2,78) = 54.29, *p* < .001 | F(2,94) = 23.40, *p* < .001 | F(2,96) = 25.86, *p* < .001 |
| Predicted | F(2,78) = 44.77, *p* < .001 | F(2,94) = 8.32, *p* < .001 | F(2,96) = 13.44, *p* < .001 |

The **ranking of item sensitivity is identical in all three experiments** (causation ≈ control > prediction) — a genuinely robust pattern. But the pairwise structure underneath it is *not* a monotonic gradient:

- **Experiment 1**: causation and control fully separate all three consistency levels (consistent > inconsistent > control, all pairwise *p* < .001); prediction separates consistent from the other two but not inconsistent from control.
- **Experiment 2**: for *all three* questions, consistent and inconsistent no longer differ from each other — only the active-vs-control distinction survives. Participants register "I made a choice," not "my choice matched the outcome."
- **Experiment 3**: the consistent-vs-inconsistent distinction *returns* for all three questions (all *p* ≤ .003) — closer to Experiment 1 than to Experiment 2. The one exception that survives unchanged from Experiment 1 is prediction's failure to separate inconsistent from control {note to self - make sence .... they "predicted the opposite direction) (Exp1 *p* = .660; Exp3 *p* = .159).

So this is a dip, not a trend: Exp2 is the outlier here, not the midpoint of a straight line from Exp1 to Exp3. Whatever caused the loss of graded consistent/inconsistent discrimination in the mouse-based experiment did not persist into the touchscreen version.

## Direction B: do the three questions differ from each other within a condition?

Simple main effects of Question type, within each consistency level:

| Condition | Experiment 1 | Experiment 2 | Experiment 3 |
|---|---|---|---|
| Consistent | F(2,78) = 14.50, *p* < .001 | F(2,94) = 2.95, *p* = .057 (n.s.) | F(2,96) = 0.24, *p* = .788 (n.s.) |
| Inconsistent | F(2,78) = 28.74, *p* < .001 | F(2,94) = 4.23, *p* = .017 | F(2,96) = 0.32, *p* = .725 (n.s.) |
| Control | F(2,78) = 23.05, *p* < .001 | F(2,94) = 13.17, *p* < .001 | F(2,96) = 11.82, *p* < .001 |

**This is the cleanest monotonic trend across the whole questionnaire dataset.** In the two active conditions, the ability of the three questions to differentiate from one another declines in a straight line across the embodiment gradient — strong in Experiment 1, weakening in Experiment 2, gone by Experiment 3 — while staying essentially constant and highly significant in the control condition throughout. In other words, the more effortful/embodied the direction-selection response becomes, the less participants seem to separate causation from control from prediction *while they are actively doing something*, even though they still separate them clearly *when they are not*.

## The one finding that replicates without exception

In the control (passive) condition, **prediction is rated higher than both causation and control in all three experiments**, with causation and control never differing significantly from each other:

| | Experiment 1 | Experiment 2 | Experiment 3 |
|---|---|---|---|
| Caused vs. Predicted | *p* < .001, *d* = −0.63 | *p* < .001, *d* = −0.62 | *p* < .001, *d* = −0.55 |
| Controlled vs. Predicted | *p* < .001, *d* = −0.77 | *p* = .003, *d* = −0.52 | *p* = .021, *d* = −0.39 |
| Caused vs. Controlled | *p* = .048, *d* = 0.15 (marginal) | *p* = .444, *d* = −0.09 (n.s.) | *p* = .075, *d* = −0.16 (marginal) |

(note to self - is this table for contol condition? maibe in additional material we cal also add tables for the other two)

This is arguably the single most trustworthy cross-experiment claim available from the questionnaire data: whenever the gaze movement was externally generated (no action taken), participants rated it as more *predictable* than either *caused* or *controlled* — and never rated causation and control as different from each other. It survives response modality, sample, and the general shrinkage of every other effect in the dataset. A natural candidate for a strong, low-risk claim in the General Discussion.

## Theoretical interpretation (working notes)

This is not treated as a failed replication of a predicted gradient. The original prediction (H3, `2.structure.md`) was that increasing embodiment would simply *amplify* the action-outcome-consistency modulation across experiments. What the data show instead is more differentiated, and arguably more informative: some aspects of the questionnaire structure collapse across the embodiment gradient while others stay fully intact.

**Why the Question-type main effect disappears while the Consistency main effect does not.** As the direction-selection response becomes more embodied (keypress → mouse → touch), the experience of having acted appears to become sufficiently automatic and holistic that its sub-components — causation, control, prediction — stop being finely differentiated from one another; they collapse toward a single undifferentiated sense of "I did this." The coarser active-versus-passive distinction survives throughout because it doesn't depend on that finer differentiation: "I acted" versus "I did not act" remains an obvious judgment even once the finer structure within the active conditions has blurred.

**Why the consistent-vs-inconsistent gap shrinks.** With a more embodied action, the act itself may carry enough felt responsibility that a mismatched outcome is easy to own regardless — "I moved my hand, so I'm responsible for what happened, whichever direction it went." With a minimal action like a keypress, a mismatched outcome is comparatively easy to disown ("that wasn't really me"), which is consistent with Experiment 1 showing the largest consistent-vs-inconsistent gaps of the three experiments, and Experiment 2/3 showing routinely smaller ones (see the Direction A pairwise *d*s above).

**Important scope restriction — no cross-experiment comparison of absolute rating level.** This account must be stated purely in terms of *relative, within-experiment structure* (how much conditions differ from one another; how much items differ from one another), not in terms of absolute SoA intensity rising or falling across experiments. Each experiment is an independent between-subjects sample, and no participant ever rated more than one response modality — there is no shared calibration point across experiments, so a given numeral on the 7-point scale is not guaranteed to mean the same subjective intensity in Experiment 1 as in Experiment 2 or 3. The raw means happen to be lower in Experiments 2 and 3 than in Experiment 1, but this is not usable as evidence either — the comparison itself is not licensed by the design. What *is* legitimately comparable across experiments is the relative structure computed independently within each sample: effect sizes, simple-effects patterns, and pairwise differentiation — which is exactly what the tables above report, and exactly what this interpretation should be restricted to.

## Methodological note on data quality

Normality (Shapiro–Wilk) does **not** track the embodiment gradient cleanly: Experiment 1 was worst (8 of 9 cells violated), Experiment 2 was best (3 of 9), Experiment 3 intermediate (5 of 9). This is presumably driven by how close each experiment's control-condition ratings sit to the scale floor (lowest in Exp1, closer to the scale midpoint in Exp2/3) rather than by anything about the response modality itself — worth a one-line caveat if the cross-experiment section leans on effect-size comparisons, since floor effects can themselves shrink measured effect sizes independent of any real psychological change.
