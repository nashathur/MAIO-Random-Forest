# Next session: study the hand-in for the oral discussion

Paste or point the new session to this file first:
`D:\MAIO\Random forest\NEXT_SESSION.md`

## Goal
Prepare for a **10-minute oral discussion** with the lecturer (Guus Velders) about my submitted extended abstract. The lecturer checks that I can **explain and understand** what I wrote; the grade can drop by up to 3 points (or rise by 1). I want to **study and practise**, not change the hand-in.

## Rules for the assistant
- The assignment forbids AI for the abstract text. In this session: **explain concepts, quiz me, check my explanations for correctness**. Do not write answers for me to memorise or recite.
- Don't interpret my results for me; give facts, numbers and background, and let me form the explanation. Correct me when I'm wrong.
- Python, if needed: env **college**; run with `conda run -n college python ...` (`C:\Users\thurs\miniconda3\Scripts\conda.exe`).
- Code style: linear scripts, no self-defined functions.

## Suggested way to study
1. Read `oral_prep.md` (summary, concepts, physics, likely questions, weak spots, numbers).
2. **Quiz mode:** ask me one question at a time from the "Likely questions" table and the weak spots; I answer in my own words; you say what's right, what's missing or wrong, and ask a follow-up the way an examiner would.
3. Focus areas, in order:
   1. Why rh, t and q explain O3 (meteorology + chemistry) — not in the hand-in, most likely question
   2. How a random forest works; why peaks are underpredicted (no extrapolation, averaging, no memory)
   3. Training vs 2019 performance (in-sample vs unseen)
   4. The daily cycle in Figure 1: where and why the model differs (boundary layer, residual layer, night-time loss)
   5. My choices: O3, rural station, Cabauw, missing data dropped, negatives set to 0, all hours kept
   6. The weak spots (bias −3.4 vs −3.5, missing-data reason, Fig. 2 lines, "significantly", n = trees)
4. Finish with a 10-minute mock discussion.

## Files
All in `D:\MAIO\Random forest\` unless noted.

| File | What |
|---|---|
| `C:\Users\thurs\Downloads\MAIO_Hand_In_Thursina-Ahsan_8256675.pdf` | **The submitted hand-in** (abstract p. 1–2, code p. 3–5) |
| `oral_prep.md` | Study notes: summary, concepts, physics, likely questions, weak spots, numbers card |
| `oral_prep_codex_review.md` | Codex accuracy review of `oral_prep.md` (if present; see status below) |
| `project_summary.md` | Full record of decisions, results and abstract structure (7 Oct; paths in it say `D:\MAIO\`, files are now in `D:\MAIO\Random forest\`) |
| `Handin_Random_Forest_2026.pdf` | The assignment (steps 1–15, grading) |
| `abstract.tex` / `abstract.pdf` | Local 7 Oct draft (older than the hand-in; contains `% TODO` notes) |
| `randomforest_o3_cabauw.py` | The appendix code (steps 3–10 in one script) |
| `results\` | Figures and result tables: `statistics_step8.csv`, `step9_n_estimators.csv`, `step10_single_variables.csv`, `fig_daily_cycle_2019_values.csv`, `run_log.txt` |
| `Rural_NL10644\` | Cabauw data 2016–2019 (other station folders too) |
| Exploration scripts | `seasonal_check.py`, `o3_error_check.py`, `rural_compare.py`, `o3_vs_no2.py`, `time_check.py`, … (background numbers in `oral_prep.md` come from these) |

**Paths note:** the files were moved from `D:\MAIO\` to `D:\MAIO\Random forest\`. The scripts still point to `D:\MAIO\...`; change `DATA_DIR` / `OUT_DIR` at the top before rerunning anything.

## Key facts (quick reference)
- Station: Cabauw-Wielsekade NL10644, rural background, 51.97 N 4.92 E (Lopik, Utrecht)
- Model: RandomForestRegressor, 30 trees, min_samples_leaf 5, random_state 42; 8 meteo predictors
- Train 2016–2018: 25,450 h; test 2019: 8,565 h; 1,049 h dropped (3.0%); 608 negative O3 set to 0
- 2019: r 0.87, R² 0.74, RMSE 15.5, bias −3.48 ≈ −3.5 µg m⁻³ (−7.3%); mean obs 47.9, pred 44.4 (hand-in text wrongly rounds to 44.5 and −3.4); max obs 258 vs highest pred 168.5 (163.4 at the observed peak hour); training max 195
- Training: r 0.96, R² 0.91, RMSE 8.1
- Trees: RMSE 15.80 / 15.54 / 15.42 / 15.42 (10 / 30 / 100 / 300)
- Single variables (2019 R²): rh 0.47, t 0.42, q 0.23, others ≤ 0.09
- Daily cycle 2019: obs min 32.4 (06 h) max 66.8 (15 h); model min 30.0 (04 h) max 61.2 (14 h); times UTC+1
- References in hand-in: WHO (2021), Otero et al. (2016), Fan et al. (2022)

## Status at end of previous session (13 Oct 2026)
- Hand-in submitted. Prep notes written and updated to the submitted version.
- Codex reviewed `oral_prep.md` (full review: `oral_prep_codex_review.md`). All 18 findings were checked; the numerical ones were re-verified with `verify_codex.py` (college env). All were applied to `oral_prep.md`:
  - **Numbers:** predicted mean is 44.4, not 44.5 (exact 44.448); bias −3.48 ≈ −3.5, so the hand-in text's −3.4 is the error, Fig. 2's −3.5 is right. Prediction at the observed peak hour is 163.4.
  - **Wind data:** the "missing wind direction at 1.3 vs 3.3 m/s" figure was from Erzeijstraat; at Cabauw it's 1.3 vs 4.1 m/s, and "missing = calm" is an inference, not documented.
  - **Random forest:** this model uses bootstrap samples of hours, but all 8 variables at every split (`max_features` default); RF doesn't strictly need complete predictors (scikit-learn 1.9 supports NaN), dropping was a choice; train–test gap isn't purely memorisation.
  - **Statistics:** r ignores bias *and* amplitude; R² penalises both; a model's r isn't guaranteed positive.
  - **Chemistry:** O + O2 + M; net O3 production needs HO2/RO2 radicals from CO and VOC oxidation; afternoon concentration peak ≠ production peak; dry deposition isn't strongest at night, but depletes the shallow night layer.
  - **Interpretation softened:** rh as proxy vs cause not separable; the 2016–2019 O3 rise and 2019 bias were not attributed; Otero et al. is about MDA8, not hourly O3; Fan et al. says previous-day O3 is consistently important (not "always" for every model).
- Note: `project_summary.md` (7 Oct) still contains the old wrong values (44.45 / 44.5, and the Erzeijstraat wind numbers). Trust `oral_prep.md` over it.
