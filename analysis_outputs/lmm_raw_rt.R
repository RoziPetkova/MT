# Linear mixed models on raw trial-level RT, across all 3 experiments.
#
# Data: each experiment's 05b_floor_cut.xlsx (RT >= 200ms floor-cut applied,
# no +/-2SD trim). Low-accuracy subjects (<85%) are already excluded upstream
# at each pipeline's Step 02, before this file is written, so no separate
# accuracy filtering is needed here. The subject-level RT-outlier exclusions
# used elsewhere (ss2/ss17/ss11/ss32) are NOT applied here, since that
# criterion is itself computed from the trimmed data downstream of this step.
#
# Run with working directory set to the repo root, e.g.:
#   Rscript analysis_outputs/lmm_raw_rt.R
#
# Requires: lme4, lmerTest, readxl (installed into a user library since the
# system library isn't writable without admin rights):
#   userlib <- Sys.getenv("R_LIBS_USER")
#   dir.create(userlib, recursive = TRUE, showWarnings = FALSE)
#   install.packages(c("lme4", "lmerTest", "readxl"), lib = userlib,
#                     repos = "https://cloud.r-project.org")

userlib <- Sys.getenv("R_LIBS_USER")
library(readxl, lib.loc = userlib)
library(lme4, lib.loc = userlib)
library(lmerTest, lib.loc = userlib)

options(width = 120)

paths <- list(
  `1` = "experiment1/data_processing3/exp_data/05b_floor_cut.xlsx",
  `2` = "experiment2/data_processing/exp_data/05b_floor_cut.xlsx",
  `3` = "experiment3/data_processing/exp_data/05b_floor_cut.xlsx"
)

read_exp <- function(exp, path) {
  df <- read_excel(path)[, c("Subject", "gaze_congruency", "action_consistency", "rt")]
  df$Experiment <- exp
  df$subject_id <- paste(exp, df$Subject, sep = "_")
  df
}

frames <- Map(read_exp, names(paths), paths)

for (exp in names(paths)) {
  cat("\n\n================ EXPERIMENT", exp, "================\n")
  df <- frames[[exp]]
  df$gaze_congruency <- factor(df$gaze_congruency)
  df$action_consistency <- factor(df$action_consistency)
  df$Subject <- factor(df$Subject)

  cat("N subjects:", length(unique(df$Subject)), " N trials:", nrow(df), "\n\n")

  m <- lmer(rt ~ gaze_congruency * action_consistency + (1 | Subject), data = df,
            control = lmerControl(optimizer = "bobyqa"))

  cat("--- Fixed effects (Satterthwaite) ---\n")
  print(summary(m)$coefficients)

  cat("\n--- Type III ANOVA (omnibus F tests) ---\n")
  print(anova(m, type = 3))

  cat("\n--- Random effects ---\n")
  print(VarCorr(m))
}

cat("\n\n================ COMBINED CROSS-EXPERIMENT MODEL ================\n")
dc <- do.call(rbind, frames)
dc$gaze_congruency <- factor(dc$gaze_congruency)
dc$action_consistency <- factor(dc$action_consistency)
dc$Experiment <- factor(dc$Experiment)
dc$subject_id <- factor(dc$subject_id)

cat("N subjects:", length(unique(dc$subject_id)), " N trials:", nrow(dc), "\n\n")

mc <- lmer(rt ~ gaze_congruency * action_consistency * Experiment + (1 | subject_id), data = dc,
           control = lmerControl(optimizer = "bobyqa"))

cat("--- Fixed effects (Satterthwaite) ---\n")
print(summary(mc)$coefficients)

cat("\n--- Type III ANOVA (omnibus F tests) ---\n")
print(anova(mc, type = 3))

cat("\n--- Random effects ---\n")
print(VarCorr(mc))
