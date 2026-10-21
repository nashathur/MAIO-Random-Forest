# Random forest O3 hand-in: project summary

Course hand-in: *Handin Random Forest analyses air quality* (G. Velders, 2 Sep 2026)
Working folder: `D:\MAIO\random-forest` · Python env: `college` · Last update: 7 Oct 2026

---

## 1. Assignment requirements (from the PDF)

| Item | Requirement |
|---|---|
| Task | Random forest model for one air quality component from meteorology; train 2016–2018, predict 2019, evaluate |
| Steps | 1 choose component and station · 2 predictors · 3 read data · 4 build RF (8 meteo variables, 30 trees) · 5 train, handle missing and negative values · 6 predict 2019 · 7 plot · 8 statistics for training and 2019 · 9 vary number of trees or other parameters · 10 single-variable runs and physical/chemical interpretation · 11 optional: other location |
| Hand-in | Extended abstract: title, name, student number; what and why, methods and data, results discussion, conclusion; ≤ 3 references |
| Limits | ≤ 2 A4 pages, **≤ 900 words including everything**, **≤ 2 figures** |
| Appendix | Computer code (not graded) |
| Grading | Completeness 25%, discussion of results 50%, layout (figures, legends, units) 25%; oral check afterwards |

---

## 2. Decisions

### 2.1 Component and station
| Decision | Choice | Notes |
|---|---|---|
| Component | **O3** | Chosen over NO2 (O3 is formed photochemically; NO2 follows emissions and the weekly traffic cycle) |
| Station type | **Rural background** | Fewer non-meteorological influences (e.g. traffic NO) that the model cannot see |
| Station | **Cabauw-Wielsekade, NL10644** (Lopik, Utrecht) | Chosen over Wekerom NL10738; Biddinghuizen NL10617 skipped (two different sites, 2017 O3 only 27%) |
| Coordinates | 51.974489 N, 4.923301 E | From data file |

**Cabauw vs Wekerom (2016–2019):**

| | Cabauw NL10644 | Wekerom NL10738 |
|---|---|---|
| O3 coverage per year (%) | 98 / 97 / 98 / 98 | 99 / 99 / 98 / 98 |
| Mean NO / NO2 / NOx (µg m⁻³) | 3.8 / 17.0 / 22.8 | 3.2 / 14.6 / 19.5 |
| Mean O3 (µg m⁻³) | 44.4 | 44.3 |
| Max O3 training / 2019 | 195 / 258 | 179 / 218 |
| Surroundings (OpenStreetMap) | Polder grassland; Lopik ≈ 1 km E; N210 ≈ 0.5–1 km; IJsselstein/Nieuwegein ≈ 10 km; A27 ≈ 11 km E | Edge of Wekerom village; N801 adjacent; Veluwe forest 1–2 km S; Barneveld ≈ 10 km, Ede ≈ 9 km |

### 2.2 Data handling (step 5)
| # | Decision | Effect |
|---|---|---|
| 1 | Drop hours with missing O3 **or** any missing meteo value (missing wd = calm wind) | 1,049 hours dropped (3.0%) |
| 2 | Negative O3 set to 0 | 608 hours |
| 3 | Same cleaning for training and 2019 | — |
| 4 | Meteo variables used as given (wd in degrees, rain −1 code and n = 9 kept) | — |
| — | Error/outlier check (spikes, comparison with Wekerom) | **All hours kept** |

Missing hours at Cabauw:

| Year | Missing O3 | Missing meteo | Negative O3 |
|---|---|---|---|
| 2016 | 215 | 76 | 111 |
| 2017 | 285 | 89 | 6 |
| 2018 | 136 | 62 | 255 |
| 2019 | 132 | 63 | 240 |

Error check summary: hour-to-hour change median 3.7, 99.9th percentile 38.6 µg m⁻³; spikes (up and back) > 30: 2 hours, > 40: 0. Cabauw–Wekerom correlation 0.92. Hours flagged by both checks (spike > 20 and |difference| > 40): 4. The highest values (25 July 2019, max 257.9) rise and fall smoothly and were also measured at Wekerom.

### 2.3 Model
| Setting | Value | Source |
|---|---|---|
| Model | `RandomForestRegressor` (scikit-learn) | template |
| Predictors | wd, ws, t, q, hourly_rain, p, n, rh | assignment |
| n_estimators | 30 | template |
| min_samples_leaf | 5 | template |
| random_state | 42 | template |
| Training | 2016–2018, 25,450 hours | — |
| Prediction | 2019, 8,565 hours | — |

### 2.4 Statistics (step 8)
Bias, NMB, r, r², R², RMSE, MAE, standard deviations, maxima; hourly and daily means (days with ≥ 18 valid hours); training and 2019.

### 2.5 Figures (step 7)
| Figure | Content | Details |
|---|---|---|
| **A** | Mean daily cycle of O3, 2019, observed vs predicted | One curve for the whole year, means only; black = observed, red = random forest; x-axis hour of day (UTC+1) |
| **B** | Predicted vs observed, hourly, 2019 (no averaging) | Density scatter; dashed 1:1 line; red least-squares regression line (no equation); r, RMSE, bias on plot; **no legend**; axis limit = maximum data value |
| C | Full hourly series 2019 | For checking only, not for the abstract |

### 2.6 Experiments
| Step | Decision |
|---|---|
| 9 | n_estimators 10, 30, 100, 300; one at a time; other settings as template; table only |
| 10 | 8 runs, one meteo variable each; 30 trees; same hours for all runs; table only (all-8 run added as reference row) |

### 2.7 Story and references
| Item | Decision |
|---|---|
| Main story | Fits the figures: hourly O3 and its **daily cycle** (seasonal cycle in the background at most) |
| Model resolution | Hourly |
| References | Your choice (≤ 3); candidates in section 5 |

---

## 3. Results (numbers only)

### 3.1 Step 8: training vs 2019 (µg m⁻³ unless stated)
| | Training hourly | Training daily | **2019 hourly** | 2019 daily |
|---|---|---|---|---|
| n | 25,450 | 1,077 | 8,565 | 364 |
| Mean obs / pred | 43.0 / 43.0 | 43.1 / 43.1 | 47.9 / 44.5 | 47.9 / 44.4 |
| Bias | 0.0 | 0.0 | −3.5 | −3.5 |
| NMB (%) | 0.0 | 0.0 | −7.3 | −7.3 |
| r | 0.96 | 0.97 | 0.87 | 0.91 |
| R² | 0.91 | 0.94 | 0.74 | 0.78 |
| RMSE | 8.1 | 4.8 | 15.5 | 11.0 |
| MAE | 6.0 | 3.7 | 11.7 | 8.5 |
| Std obs / pred | 27.1 / 24.5 | 20.0 / 17.9 | 30.4 / 24.5 | 23.5 / 17.4 |
| Max obs / pred | 195 / 169 | 110 / 120 | 258 / 168 | 153 / 119 |

### 3.2 Figure A values: mean daily cycle 2019 (µg m⁻³)
| Hour | n | Obs | Pred | | Hour | n | Obs | Pred |
|---|---|---|---|---|---|---|---|---|
| 0 | 364 | 39.90 | 34.19 | | 12 | 358 | 61.34 | 58.80 |
| 1 | 365 | 38.43 | 33.19 | | 13 | 355 | 64.57 | 60.69 |
| 2 | 272 | 36.81 | 31.60 | | 14 | 355 | 65.87 | 61.21 |
| 3 | 358 | 36.20 | 30.92 | | 15 | 355 | 66.80 | 60.73 |
| 4 | 359 | 34.85 | 30.02 | | 16 | 362 | 64.92 | 58.82 |
| 5 | 362 | 32.83 | 30.05 | | 17 | 363 | 61.78 | 56.45 |
| 6 | 363 | 32.38 | 31.95 | | 18 | 362 | 56.89 | 52.22 |
| 7 | 363 | 34.68 | 35.59 | | 19 | 363 | 52.42 | 48.06 |
| 8 | 359 | 39.08 | 40.33 | | 20 | 362 | 48.18 | 43.25 |
| 9 | 362 | 44.89 | 45.58 | | 21 | 362 | 45.36 | 40.77 |
| 10 | 359 | 50.41 | 50.61 | | 22 | 360 | 42.88 | 37.85 |
| 11 | 358 | 56.42 | 55.58 | | 23 | 364 | 40.86 | 36.28 |

Hour 2 has fewer valid hours (272) than the others (355–365); not investigated.

### 3.3 Step 9: number of trees, 2019 hourly
| n_estimators | r | R² | RMSE | MAE | Bias | Max pred |
|---|---|---|---|---|---|---|
| 10 | 0.86 | 0.73 | 15.80 | 11.90 | −3.47 | 168.8 |
| 30 | 0.87 | 0.74 | 15.54 | 11.70 | −3.48 | 168.5 |
| 100 | 0.87 | 0.74 | 15.42 | 11.61 | −3.45 | 170.6 |
| 300 | 0.87 | 0.74 | 15.42 | 11.60 | −3.46 | 169.4 |

Training RMSE: 8.43 / 8.15 / 8.04 / 8.01 for 10 / 30 / 100 / 300 trees.

### 3.4 Step 10: single variables, 2019 hourly (sorted by RMSE)
| Variable | r | R² | RMSE | MAE | Bias | Std pred | Max pred |
|---|---|---|---|---|---|---|---|
| *all 8* | *0.87* | *0.74* | *15.54* | *11.70* | *−3.48* | *24.51* | *168.5* |
| rh | 0.70 | 0.47 | 22.07 | 16.71 | −4.09 | 19.78 | 131.1 |
| t | 0.67 | 0.42 | 23.21 | 19.02 | −4.50 | 17.04 | 165.3 |
| q | 0.50 | 0.23 | 26.74 | 20.69 | −4.79 | 14.80 | 106.3 |
| wd | 0.34 | 0.09 | 29.11 | 21.20 | −5.39 | 10.13 | 60.9 |
| ws | 0.32 | 0.08 | 29.22 | 21.41 | −4.48 | 10.08 | 72.4 |
| n | 0.17 | 0.01 | 30.34 | 23.15 | −4.64 | 4.61 | 51.4 |
| hourly_rain | 0.03 | −0.03 | 30.82 | 23.55 | −4.88 | 1.55 | 59.7 |
| p | 0.14 | −0.03 | 30.95 | 23.67 | −5.17 | 8.82 | 63.4 |

Observed 2019: std 30.44, max 257.86. Training (2016–2018) r for single variables: rh 0.71, t 0.62, q 0.54, ws 0.37, wd 0.37, p 0.29, n 0.20, hourly_rain 0.06.

### 3.5 Background numbers (Cabauw, 2016–2019 means)
| Month | O3 | NO2 | NO | t | q | ws | rh |
|---|---|---|---|---|---|---|---|
| Jan | 32.7 | 22.9 | 6.5 | 3.7 | 10.6 | 4.8 | 88.1 |
| Feb | 34.6 | 23.9 | 4.9 | 4.0 | 23.7 | 4.8 | 83.6 |
| Mar | 48.2 | 17.9 | 2.9 | 6.6 | 38.1 | 5.0 | 80.8 |
| Apr | 57.9 | 14.3 | 1.8 | 9.9 | 63.7 | 3.9 | 75.9 |
| May | 64.3 | 12.2 | 1.4 | 14.3 | 80.9 | 3.7 | 73.9 |
| Jun | 60.6 | 10.6 | 1.3 | 17.5 | 80.7 | 3.8 | 77.1 |
| Jul | 58.0 | 10.8 | 1.5 | 18.9 | 84.5 | 3.5 | 74.4 |
| Aug | 50.6 | 13.2 | 1.9 | 18.2 | 67.9 | 3.5 | 78.0 |
| Sep | 41.0 | 16.3 | 2.9 | 15.4 | 49.2 | 3.6 | 81.0 |
| Oct | 32.3 | 16.8 | 3.9 | 11.7 | 27.7 | 4.0 | 85.4 |
| Nov | 23.7 | 22.2 | 7.2 | 6.5 | 13.4 | 4.0 | 88.7 |
| Dec | 28.3 | 22.9 | 8.9 | 5.2 | 7.7 | 4.7 | 90.4 |

Variance of hourly O3 explained by month alone: 23%; by hour of day alone: 16%. Daily-cycle range per season: DJF 13.2, MAM 42.2, JJA 54.2, SON 30.0 µg m⁻³.

---

## 4. Structure of the extended abstract (prompts only)

### Header (≈ 15 words)
- Title (your own; meaningful: O3, Cabauw, random forest, meteorology, hourly/daily cycle)
- Name, student number

### 1. Introduction (≈ 90 words)
- How is surface O3 formed (secondary, not emitted)?
- Which processes cause its **daily cycle** (daytime photochemical production, night-time loss, boundary-layer mixing; link to CLASS exercise)?
- Why it matters (health, vegetation)
- Why a random forest (reference)
- Research question (one sentence, about **hourly** O3 and its **daily cycle**)

### 2. Data and methods (≈ 140 words)
| Item | Content | Source |
|---|---|---|
| Station + reason | Cabauw NL10644, rural background, one site 2016–2019; few local sources (mean NO ≈ 3.8 µg m⁻³); O3 97–98% complete | `rural_compare.py` |
| Data | Hourly O3 (µg m⁻³) and 8 meteo variables | assignment |
| Missing data | 1,049 h (3.0%) dropped | `run_log.txt` |
| Negative O3 | 608 h set to 0 | `run_log.txt` |
| Error check | Spikes and Wekerom comparison; all hours kept | `o3_error_check.py` |
| Model | RF, 30 trees, min_samples_leaf 5 | template |
| Train / test | 2016–2018 (25,450 h) / 2019 (8,565 h) | `run_log.txt` |
| Metrics | r, RMSE, bias (R² optional) | step 8 |
| Experiments | Trees 10/30/100/300; 8 single-variable runs | steps 9–10 |
| Code | "see appendix" | step 14 |

### 3. Results (≈ 230 words)
- **3a Overall skill (≈ 50):** r, RMSE, bias for training vs 2019; what the difference says about generalisation → `statistics_step8.csv`
- **3b Figure A (≈ 100):** timing of observed vs predicted minimum and maximum; amplitude (max − min) observed vs predicted; at which hours the gap is largest or smallest → `fig_daily_cycle_2019_values.csv`
- **3c Figure B (≈ 80):** points relative to the 1:1 and regression lines at low, middle and high O3; max observed vs max predicted 2019, and the training maximum

### 4. Experiments and interpretation (≈ 210 words)
- **4a Number of trees (≈ 40):** change in r and RMSE from 10 to 300 trees; is 30 sufficient? → `step9_n_estimators.csv`
- **4b Single variables (≈ 90):** ranking; *why* each variable performs as it does (sunlight, temperature, humidity, wind, mixing); best single variable vs all 8 → `step10_single_variables.csv`
- **4c What meteorology cannot explain (≈ 80):** your interpretation of the gaps in Figure A and at the extremes in Figure B; which processes are missing from the 8 variables (references, CLASS)

### 5. Conclusion (≈ 75 words)
- Answer the research question
- Main strength, main limitation, one improvement

### References (≤ 3, ≈ 60 words)

### Figure captions (≈ 40 words each)
- **Fig. A:** mean O3 per hour of day, 2019, Cabauw; black observed, red random forest; units; UTC+1
- **Fig. B:** hourly O3 2019 (n = 8,565); colour = point density; dashed = 1:1, red = regression; r, RMSE, bias on plot; units (no legend, so the caption must explain the lines)

### Word budget
| Part | Words |
|---|---|
| Header | 15 |
| Introduction | 90 |
| Data and methods | 140 |
| Results | 230 |
| Experiments and interpretation | 210 |
| Conclusion | 75 |
| References | 60 |
| Captions | 80 |
| **Total** | **900** |

### Checklist
- [ ] Title, name, student number
- [ ] Research question stated and answered
- [ ] Missing-data and negative-O3 choices explained (step 5)
- [ ] Statistics for training **and** 2019 (step 8)
- [ ] Number-of-trees result (step 9)
- [ ] Single-variable result with physical/chemical explanation (step 10)
- [ ] ≤ 2 figures, axis labels with units, captions explaining the lines
- [ ] ≤ 3 references
- [ ] Code appendix (`randomforest_o3_cabauw.py`)
- [ ] ≤ 900 words, ≤ 2 A4 pages

---

## 5. Reference candidates (checked to exist; read at least the abstract before citing)

| Topic | Reference |
|---|---|
| Method: RF meteorological normalisation | Grange, S. K., Carslaw, D. C., Lewis, A. C., Boleti, E., & Hueglin, C. (2018). Random forest meteorological normalisation models for Swiss PM10 trend analysis. *Atmos. Chem. Phys.*, 18, 6223–6239. https://doi.org/10.5194/acp-18-6223-2018 |
| Meteorological drivers of O3 in Europe | Otero, N., Sillmann, J., Schnell, J. L., Rust, H. W., & Butler, T. (2016). Synoptic and meteorological drivers of extreme ozone concentrations over Europe. *Environ. Res. Lett.*, 11, 024005. https://doi.org/10.1088/1748-9326/11/2/024005 |
| RF for O3 and meteorology | Weng, X., Forster, G., & Nowack, P. (2022). A machine learning approach to quantify meteorological drivers of ozone pollution in China from 2015 to 2019. *Atmos. Chem. Phys.*, 22, 8385–8402. https://doi.org/10.5194/acp-22-8385-2022 |
| RF limitations (low peaks, high lows) | Fan, K., Dhammapala, R., Harrington, K., Lamastro, R., Lamb, B., & Lee, Y. (2022). Development of a machine learning approach for local-scale ozone forecasting: Application to Kennewick, WA. *Frontiers in Big Data*, 5, 781309. https://doi.org/10.3389/fdata.2022.781309 |
| RF limitations at extremes | Gao, Z., Wang, Y., Vasilakos, P., Ivey, C. E., Do, K., & Russell, A. G. (2022). Predicting peak daily maximum 8 h ozone ... using machine learning methods (SoCAB-8HR V1.0). *Geosci. Model Dev.*, 15, 9015–9029. https://doi.org/10.5194/gmd-15-9015-2022 |
| Random forest (original) | Breiman, L. (2001). Random Forests. *Machine Learning*, 45, 5–32. |
| Other | Grange & Carslaw (2019), *Sci. Total Environ.*, 653, 578–588 · Vu et al. (2019), *Atmos. Chem. Phys.*, 19, 11303–11314 · Jacob & Winner (2009), *Atmos. Environ.*, 43, 51–63 · Monks (2000), *Atmos. Environ.*, 34, 3545–3561 |

---

## 6. Files

### Scripts in `D:\MAIO\random-forest\scripts`
| File | Role |
|---|---|
| **`randomforest_o3_cabauw.py`** | **Appendix code: steps 3–10 in one linear script** |
| `rf_o3_cabauw.py`, `rf_o3_cabauw_step7_8.py`, `rf_o3_cabauw_step9.py`, `rf_o3_cabauw_step10.py` | The same work as separate scripts (kept) |
| `o3_error_check.py`, `rural_compare.py` | Optional appendix (error check; station NOx comparison) |
| `check_data.py`, `gaps_check.py`, `neg_o3_check.py`, `summary_stats.py`, `meteo_compare.py`, `rural_peaks.py`, `o3_vs_no2.py`, `seasonal_check.py` | Exploration (kept for now; three are about Erzeijstraat) |

### Outputs in `D:\MAIO\random-forest\results`
| File | Content |
|---|---|
| `fig_daily_cycle_2019.png` | Figure A |
| `fig_scatter_2019.png` | Figure B |
| `fig_hourly_2019_full.png` | Figure C (check only) |
| `fig_daily_cycle_2019_values.csv` | Numbers behind Figure A |
| `statistics_step8.csv` | Step 8 statistics |
| `step9_n_estimators.csv` | Step 9 table |
| `step10_single_variables.csv` | Step 10 table |
| `o3_cabauw_train_2016-2018.csv`, `o3_cabauw_pred_2019.csv` | Observed and predicted O3 |
| `run_log.txt` | Cleaning counts, training R², feature importance |
| `o3_error_check_cabauw.csv` | Error-check flags |

### Open items
- Optional step 11 (another location): not decided
- Exploration scripts: keep for now

---

## 7. Appendix code: `randomforest_o3_cabauw.py`

Run with: `conda run -n college python D:\MAIO\random-forest\scripts\randomforest_o3_cabauw.py`

```python
# Random forest model for O3 at Cabauw-Wielsekade (NL10644), steps 3-10.
# Train on 2016-2018 with 8 meteorological variables, predict 2019, evaluate,
# vary the number of trees (step 9) and use one variable at a time (step 10).
# Run: conda run -n college python randomforest_o3_cabauw.py
import os
import numpy as np
import pandas as pd
from scipy.stats import gaussian_kde
from sklearn.ensemble import RandomForestRegressor
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
RF_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(RF_DIR, "data", "raw")

# ======================= settings =======================
STATION = "Rural_NL10644"
DATA_DIR = os.path.join(RAW_DIR, STATION)
OUT_DIR = os.path.join(RF_DIR, "results")
TARGET = "o3"
FEATURES = ["wd", "ws", "t", "q", "hourly_rain", "p", "n", "rh"]
TRAIN_YEARS = [2016, 2017, 2018]
PRED_YEAR = 2019
NEGATIVE_TO_ZERO = True          # True: set negative O3 to 0; False: keep them as measured
N_TREES = 30                     # number of trees of the main model
N_TREES_LIST = [10, 30, 100, 300]  # step 9
UNIT = "µg m$^{-3}$"

os.makedirs(OUT_DIR, exist_ok=True)
pd.set_option("display.width", 250)
pd.set_option("display.max_columns", 30)

# ======================= step 3: read data =======================
frames = []
for year in TRAIN_YEARS + [PRED_YEAR]:
    f = os.path.join(DATA_DIR, f"{STATION}_{year}.csv")
    frames.append(pd.read_csv(f, sep=";", na_values=["NA"], low_memory=False))
data = pd.concat(frames, ignore_index=True)
data["date"] = pd.to_datetime(data["date"])
data["year"] = data["date"].dt.year
data = data[["date", "year", TARGET] + FEATURES]

# ======================= step 5: missing data and negative values =======================
log = [f"Station: {STATION}, target: {TARGET}, features: {', '.join(FEATURES)}"]
log.append(f"Hours read: {len(data)}")
for year, g in data.groupby("year"):
    log.append(f"  {year}: {len(g)} hours, missing O3 {g[TARGET].isna().sum()}, "
               f"missing meteo {g[FEATURES].isna().any(axis=1).sum()}, "
               f"negative O3 {(g[TARGET] < 0).sum()}")

# Missing O3 is never filled (it is the value we predict and evaluate against).
# Missing wd means calm wind (no direction), so those hours are dropped too.
clean = data.dropna(subset=[TARGET] + FEATURES).copy()
log.append(f"Hours dropped (missing O3 or meteo): {len(data) - len(clean)} "
           f"({100 * (len(data) - len(clean)) / len(data):.1f}%)")

if NEGATIVE_TO_ZERO:
    n_neg = (clean[TARGET] < 0).sum()
    clean[TARGET] = clean[TARGET].clip(lower=0)
    log.append(f"Negative O3 set to 0: {n_neg} hours")

train = clean[clean["year"].isin(TRAIN_YEARS)]
pred = clean[clean["year"] == PRED_YEAR]
x_train, y_train = train[FEATURES].values, train[TARGET].values
x_pred, y_obs = pred[FEATURES].values, pred[TARGET].values
log.append(f"Training hours ({TRAIN_YEARS[0]}-{TRAIN_YEARS[-1]}): {len(train)}, "
           f"prediction hours ({PRED_YEAR}): {len(pred)}")

# ======================= step 4: build and train the random forest =======================
model = RandomForestRegressor(n_estimators=N_TREES, min_samples_leaf=5, random_state=42)
model.fit(x_train, y_train)
score = model.score(x_train, y_train)
log.append(f"R2 score (training data): {score:6.3f}")

# ======================= step 6: predict 2019 =======================
y_pred = model.predict(x_pred)
y_fit = model.predict(x_train)

out_train = train[["date", TARGET]].rename(columns={TARGET: "o3_obs"})
out_train["o3_pred"] = y_fit
out_pred = pred[["date", TARGET]].rename(columns={TARGET: "o3_obs"})
out_pred["o3_pred"] = y_pred
out_train.to_csv(os.path.join(OUT_DIR, "o3_cabauw_train_2016-2018.csv"), index=False, float_format="%.2f")
out_pred.to_csv(os.path.join(OUT_DIR, "o3_cabauw_pred_2019.csv"), index=False, float_format="%.2f")

importance = pd.Series(model.feature_importances_, index=FEATURES).sort_values(ascending=False)
log.append("Feature importance (impurity-based, training):")
for name, value in importance.items():
    log.append(f"  {name:12s} {value:.3f}")
with open(os.path.join(OUT_DIR, "run_log.txt"), "w") as f:
    f.write("\n".join(log) + "\n")
print("\n".join(log))

# ======================= step 8: statistics =======================
# Hourly values, and daily means (days with at least 18 valid hours).
rows = []
for period, df in [("2016-2018 (training)", out_train), ("2019 (prediction)", out_pred)]:
    daily = df.set_index("date").resample("D").agg(["mean", "count"])
    daily = daily[daily[("o3_obs", "count")] >= 18]
    for resolution, obs, mod in [("hourly", df["o3_obs"].values, df["o3_pred"].values),
                                 ("daily mean", daily[("o3_obs", "mean")].values,
                                  daily[("o3_pred", "mean")].values)]:
        diff = mod - obs
        r = np.corrcoef(obs, mod)[0, 1]
        rows.append({
            "period": period,
            "resolution": resolution,
            "n": len(obs),
            "mean obs": obs.mean(),
            "mean pred": mod.mean(),
            "bias (pred-obs)": diff.mean(),
            "NMB (%)": 100 * diff.sum() / obs.sum(),
            "r": r,
            "r2": r ** 2,
            "R2 (1-SSres/SStot)": 1 - (diff ** 2).sum() / ((obs - obs.mean()) ** 2).sum(),
            "RMSE": np.sqrt((diff ** 2).mean()),
            "MAE": np.abs(diff).mean(),
            "std obs": obs.std(),
            "std pred": mod.std(),
            "max obs": obs.max(),
            "max pred": mod.max(),
        })
stats = pd.DataFrame(rows)
stats.to_csv(os.path.join(OUT_DIR, "statistics_step8.csv"), index=False, float_format="%.3f")
print("\nStep 8 statistics:")
print(stats.round(2).to_string(index=False))

# ======================= step 7: plots =======================
plt.rcParams.update({"font.size": 10})

# Figure A: mean daily cycle in 2019 (mean of all hourly values per hour of day)
out_pred["hour"] = out_pred["date"].dt.hour
cycle = out_pred.groupby("hour")[["o3_obs", "o3_pred"]].mean()
cycle_out = cycle.rename(columns={"o3_obs": "o3_obs_mean", "o3_pred": "o3_pred_mean"})
cycle_out.insert(0, "n_hours", out_pred.groupby("hour")["o3_obs"].count())
cycle_out.to_csv(os.path.join(OUT_DIR, "fig_daily_cycle_2019_values.csv"), float_format="%.2f")

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(cycle.index, cycle["o3_obs"], color="black", lw=1.5, marker="o", ms=3, label="Observed")
ax.plot(cycle.index, cycle["o3_pred"], color="tab:red", lw=1.5, marker="o", ms=3, label="Random forest")
ax.set_xlim(0, 23)
ax.set_xticks(range(0, 24, 3))
ax.set_xlabel("Hour of day (UTC+1)")
ax.set_ylabel(f"Mean O$_3$ ({UNIT})")
ax.set_title("Mean daily cycle of O$_3$, Cabauw (NL10644), 2019")
ax.legend(loc="upper left", frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(OUT_DIR, "fig_daily_cycle_2019.png"), dpi=300)
plt.close(fig)

# Figure B: density scatter of hourly predicted vs observed O3 in 2019
obs = out_pred["o3_obs"].values
mod = out_pred["o3_pred"].values
density = gaussian_kde(np.vstack([obs, mod]))(np.vstack([obs, mod]))
order = density.argsort()          # plot the densest points last (on top)
slope, intercept = np.polyfit(obs, mod, 1)
row = stats[(stats["period"] == "2019 (prediction)") & (stats["resolution"] == "hourly")].iloc[0]
lim = max(obs.max(), mod.max())   # axis limit = maximum data value

fig, ax = plt.subplots(figsize=(5.5, 4.8))
sc = ax.scatter(obs[order], mod[order], c=density[order], s=4, cmap="viridis", edgecolors="none")
ax.plot([0, lim], [0, lim], color="black", lw=1, ls="--")
ax.plot([0, lim], [intercept, intercept + slope * lim], color="tab:red", lw=1.5)
ax.set_xlim(0, lim)
ax.set_ylim(0, lim)
ax.set_aspect("equal")
ax.set_xlabel(f"Observed O$_3$ ({UNIT})")
ax.set_ylabel(f"Predicted O$_3$ ({UNIT})")
ax.set_title("Hourly O$_3$, Cabauw (NL10644), 2019")
ax.text(0.04, 0.96, f"r = {row['r']:.2f}\nRMSE = {row['RMSE']:.1f} {UNIT}\nbias = {row['bias (pred-obs)']:.1f} {UNIT}",
        transform=ax.transAxes, va="top", fontsize=9)
cb = fig.colorbar(sc, ax=ax, shrink=0.85)
cb.set_label("Relative point density")
fig.tight_layout()
fig.savefig(os.path.join(OUT_DIR, "fig_scatter_2019.png"), dpi=300)
plt.close(fig)

# Figure C: full 2019 hourly series (for checking, too dense for the abstract)
fig, ax = plt.subplots(figsize=(10, 3.5))
ax.plot(out_pred["date"], out_pred["o3_obs"], color="black", lw=0.4, label="Observed")
ax.plot(out_pred["date"], out_pred["o3_pred"], color="tab:red", lw=0.4, alpha=0.8, label="Random forest")
ax.set_ylabel(f"Hourly O$_3$ ({UNIT})")
ax.set_title("Cabauw (NL10644), 2019, hourly")
ax.legend(loc="upper left", frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(OUT_DIR, "fig_hourly_2019_full.png"), dpi=200)
plt.close(fig)

# ======================= step 9: number of trees =======================
rows = []
for n_trees in N_TREES_LIST:
    model9 = RandomForestRegressor(n_estimators=n_trees, min_samples_leaf=5, random_state=42)
    model9.fit(x_train, y_train)
    for period, obs, mod in [("2016-2018 (training)", y_train, model9.predict(x_train)),
                             ("2019 (prediction)", y_obs, model9.predict(x_pred))]:
        diff = mod - obs
        r = np.corrcoef(obs, mod)[0, 1]
        rows.append({
            "n_estimators": n_trees,
            "period": period,
            "n": len(obs),
            "mean obs": obs.mean(),
            "mean pred": mod.mean(),
            "bias (pred-obs)": diff.mean(),
            "NMB (%)": 100 * diff.sum() / obs.sum(),
            "r": r,
            "r2": r ** 2,
            "R2 (1-SSres/SStot)": 1 - (diff ** 2).sum() / ((obs - obs.mean()) ** 2).sum(),
            "RMSE": np.sqrt((diff ** 2).mean()),
            "MAE": np.abs(diff).mean(),
            "std obs": obs.std(),
            "std pred": mod.std(),
            "max obs": obs.max(),
            "max pred": mod.max(),
        })
table9 = pd.DataFrame(rows)
table9.to_csv(os.path.join(OUT_DIR, "step9_n_estimators.csv"), index=False, float_format="%.3f")
print("\nStep 9 (number of trees):")
print(table9.round(2).to_string(index=False))

# ======================= step 10: one meteorological variable at a time =======================
# All runs use the same hours (rows with all 8 variables present), so only the variable differs.
runs = [("all 8", FEATURES)]
for var in FEATURES:
    runs.append((var, [var]))

rows = []
for name, variables in runs:
    model10 = RandomForestRegressor(n_estimators=N_TREES, min_samples_leaf=5, random_state=42)
    model10.fit(train[variables].values, y_train)
    for period, obs, mod in [("2016-2018 (training)", y_train, model10.predict(train[variables].values)),
                             ("2019 (prediction)", y_obs, model10.predict(pred[variables].values))]:
        diff = mod - obs
        r = np.corrcoef(obs, mod)[0, 1]
        rows.append({
            "variables": name,
            "period": period,
            "n": len(obs),
            "mean obs": obs.mean(),
            "mean pred": mod.mean(),
            "bias (pred-obs)": diff.mean(),
            "NMB (%)": 100 * diff.sum() / obs.sum(),
            "r": r,
            "r2": r ** 2,
            "R2 (1-SSres/SStot)": 1 - (diff ** 2).sum() / ((obs - obs.mean()) ** 2).sum(),
            "RMSE": np.sqrt((diff ** 2).mean()),
            "MAE": np.abs(diff).mean(),
            "std obs": obs.std(),
            "std pred": mod.std(),
            "max obs": obs.max(),
            "max pred": mod.max(),
        })
table10 = pd.DataFrame(rows)
table10.to_csv(os.path.join(OUT_DIR, "step10_single_variables.csv"), index=False, float_format="%.3f")
print("\nStep 10 (single variables):")
print(table10.round(2).to_string(index=False))

print(f"\nAll results written to {OUT_DIR}")
```
