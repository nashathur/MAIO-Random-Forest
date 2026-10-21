# Oral discussion prep: Random forest O3 at Cabauw (10 min)

Based on the submitted hand-in `MAIO_Hand_In_Thursina-Ahsan_8256675.pdf` (5 pages: abstract p. 1–2, code p. 3–5).
Goal of the discussion (from the assignment): show you can **explain and understand** what you wrote. Explain in your own words; the points below are facts and background to support that.

---

## 1. The study in 30 seconds
- **What:** Hourly O3 at Cabauw-Wielsekade (NL10644), a rural background station, predicted from 8 meteorological variables with a random forest.
- **How:** Trained on 2016–2018 (25,450 h), tested on unseen 2019 (8,565 h).
- **Main numbers (2019):** r = 0.87, R² = 0.74, RMSE = 15.5 µg m⁻³, bias = −3.48 ≈ **−3.5** µg m⁻³ (−7.3%). Fig. 2 (−3.5) is correct; the text's −3.4 and predicted mean 44.5 are rounding errors (exact: 47.93 obs, 44.45 → **44.4** pred).
- **Main findings in your abstract:** daily cycle reproduced, amplitude slightly too small; highest values underpredicted (258 observed vs 168 predicted); 30 trees enough; rh > t > q as single predictors; all 8 together clearly better than any single one.

---

## 2. Your choices and the reasons you gave
| Choice | Reason (your reasoning during the work) | Supporting fact |
|---|---|---|
| **O3, not NO2** | O3 is formed photochemically, so it is directly linked to meteorology; NO2 is mainly driven by emissions (traffic), which are not model inputs | NO2 weekend/weekday ratio 0.77 at Cabauw (traffic cycle); O3 1.08 |
| **Rural station** | The model sees only weather; other drivers (e.g. traffic NO) are unexplained noise for it | Mean NO: Cabauw 3.8 vs street Erzeijstraat 15.7 µg m⁻³ |
| **Cabauw (not Wekerom / Biddinghuizen)** | Complete data, one fixed site, well-studied location (KNMI Cabauw tower); Biddinghuizen = two different sites + 2017 O3 only 27% | O3 coverage 97–98% every year |
| **Drop hours with missing O3 or meteo** | Your choice (complete-case analysis): simple, nothing invented. Missing O3 can never be used (it's the value predicted and evaluated). For missing predictors, alternatives exist (filling them, or scikit-learn's built-in NaN support), but you chose to drop | 1,049 h dropped (3.0%). At Cabauw, wind direction is missing mostly at low wind (mean ws 1.3 vs 4.1 m/s overall), suggesting calm conditions, but the cause isn't documented |
| **Negative O3 → 0** | O3 cannot be physically negative; negatives are instrument noise near zero (median −0.34, min −1.66 µg m⁻³ at Erzeijstraat); dropping them would remove real near-zero hours | 608 h at Cabauw |
| **Keep all hours (no outlier removal)** | Error check found the highest values are real: smooth rise and fall, also measured at Wekerom | 25 Jul 2019: 246→253→258→254→246; Cabauw–Wekerom r = 0.92 |
| **30 trees, min_samples_leaf 5** | Template settings; step 9 showed little change beyond 30 | RMSE 15.80 / 15.54 / 15.42 / 15.42 for 10 / 30 / 100 / 300 |
| **Figure A = mean daily cycle; Figure B = hourly scatter** | Hourly is the model's resolution; daily cycle shows the processes behind O3 | — |
| **Times in UTC+1** | The data files use NL winter time all year (no summer-time jump) | Radiation peaks in the 12–13 h row; solar noon ≈ 12:40 UTC+1 |

---

## 3. Concepts you must be able to explain

### Random forest
- **One tree:** splits the data with yes/no questions on the variables (e.g. "rh > 80%?"), chosen to separate high- from low-O3 hours; each leaf predicts the **mean O3 of the training hours in it**.
- **Forest:** many trees, each built on a **random sample of hours drawn with replacement (bootstrap)**; the prediction is the **average of all trees** → more stable, less overfitting than one tree. (In your settings every split may use all 8 variables: `max_features` was left at its default. Random subsets of variables per split are an option, not used here.)
- **n_estimators** = number of trees. More trees → averaging converges; beyond some point no gain (your step 9).
- **min_samples_leaf = 5:** each leaf must contain ≥ 5 training hours → smoother predictions.
- **Cannot extrapolate:** a prediction is an average of training values, so it can never exceed the training maximum (195 µg m⁻³). Averaging within leaves and across trees lowers the reachable maximum further: the highest 2019 prediction was 168.5. At the observed peak itself (258 at 16 h on 25 Jul) the model predicted **163.4**.
- **Pulls toward the mean:** averaging smooths extremes → high values too low, low values too high (Fig. B; predicted std 24.5 vs observed 30.4).
- **No memory:** each hour is predicted from that hour's weather only; it does not know O3 of previous hours/days.

### Training vs test
- Training scores (r 0.96, RMSE 8.1) are measured on the **same hours the model learned from**, so they are optimistic.
- **2019** (unseen data) estimates how well the model generalises to a new year. The drop (RMSE 8.1 → 15.5) combines this training optimism with real differences in 2019 (e.g. higher extremes: max 258 vs 195 in training), so it is not purely "memorisation".

### Statistics
| Metric | Meaning | Your 2019 value |
|---|---|---|
| r | Linear association pred vs obs; ignores both an offset (bias) and a wrong amplitude (scale) | 0.87 |
| R² | 1 − SS_res/SS_tot: fraction of variance explained; penalises bias and amplitude errors; can be negative (worse than predicting the mean) | 0.74 |
| RMSE | Typical error size, penalises large errors | 15.5 µg m⁻³ |
| Bias | Mean(pred − obs); negative = underestimate | −3.5 µg m⁻³ |
| NMB | Bias relative to the observed mean | −7.3% |

- r² (0.76) ≠ R² (0.74) in 2019 because R² also penalises the bias (largest part here) and the too-small amplitude (predicted std 24.5 vs observed 30.4).
- **Regression line in Fig. B** flatter than 1:1 → model compresses the range (low overpredicted, high underpredicted).

### Single-variable runs (step 10)
- 8 **separate random forests**, each given only one variable, tested on 2019. Not simple correlations.
- All 8 runs have positive r (pred vs obs), as expected when a model has some skill; a simple correlation keeps the direction (rh–O3 is −0.70). A model r is not guaranteed positive in general.
- R² < 0 for rain and pressure → worse than predicting the 2019 mean.

---

## 4. Physics and chemistry background

### O3 formation and loss
- O3 is **secondary**: NO2 + sunlight → NO + O; O + O2 + M → O3 + M (M = any air molecule taking up excess energy).
- **Titration:** NO + O3 → NO2 + O2 (removes O3; strong near traffic). Photolysis + titration alone give **no net** O3.
- **Net production** needs radicals (HO2, RO2) that convert NO → NO2 **without using O3**. They come from the oxidation of **CO and VOCs** (incl. methane, isoprene). NOx-limited vs VOC-limited regimes (your CLASS exercise).
- **Dry deposition** to vegetation/soil removes O3 day and night (stomatal uptake is often larger by day). At night it can strongly deplete a **shallow, stable surface layer** that isn't replenished from above.

### Daily cycle (Fig. A)
| Observed (2019 means) | Value | Model |
|---|---|---|
| Minimum | 32.4 at 06 h | 30.0 at 04 h |
| Maximum | 66.8 at 15 h | 61.2 at 14 h |
| Range (max − min) | 34.4 | 31.2 |
| Model lower than obs | 11–06 h (incl. evening 19–23 h, gap 4.4–5.0) | largest gap 15–16 h (6.1) |
| Model higher than obs | 07–10 h (+0.2 to +1.3) | — |

Each hour's mean uses 355–365 days, except **02 h: only 272 days** (more missing O3 at that hour; cause not investigated).

Processes behind the cycle (your CLASS work):
- **Morning:** boundary layer grows, mixes down O3 from the **residual layer** (entrainment) + photochemistry starts.
- **Afternoon peak (~15 h):** the *concentration* peaks after hours of accumulated production, mixing, transport and loss; it is not necessarily the time of maximum production (that is closer to the radiation peak, ~12–13 h).
- **Evening/night:** photochemistry stops; shallow **stable nocturnal boundary layer**; O3 near the surface lost to deposition and NO titration; O3 aloft stays in the residual layer.

### Why rh, t and q (step 10) — material for your own explanation
- **q (radiation):** a proxy for photolysis conditions (sunlight drives the radical chemistry behind net production); also linked to daytime mixing.
- **t (temperature):** faster reactions, more biogenic VOC (isoprene); hot days often coincide with sunny, stagnant high-pressure weather; also varies with season and time of day.
- **rh (relative humidity):** low rh tends to go with sunny, dry, warm, well-mixed afternoons; high rh with night, cloud, fog and winter. So rh carries time-of-day and season information, which helps explain why it predicts well. rh may also matter physically (e.g. plant stomatal uptake of O3 depends on humidity). Your experiment **cannot separate** how much of rh's skill is proxy and how much is cause. (Correlation ≠ causation.)
- **Wind, pressure, cloud, rain** alone predict little in your runs (R² ≤ 0.09).
- **Otero et al. (2016):** for **MDA8** O3 (maximum daily 8-hour mean, not hourly) in central Europe, maximum temperature is the main driver, especially in summer; rh and radiation matter more in spring.

### Things the model does not explicitly include (possible discussion)
- **Multi-day build-up** during heatwaves (O3 carried over in the residual layer; your CLASS day-1→4 runs). Fan et al. (2022) found previous-day O3 consistently important as a predictor.
- **Background/transported O3** (e.g. spring maximum, continental air). Wind direction and speed give the model *some* indirect information about transport, but no trajectories or background levels. The 25 Jul 2019 peak had easterly wind (90°).
- **Emissions and background trends:** O3 at Cabauw rose 41.6 → 48.0 µg m⁻³ from 2016 to 2019 (raw annual means). Possible causes include weather, emissions and background changes; **you did not attribute** the rise or the 2019 bias to any of them.
- **No boundary-layer height** among the inputs; only indirect proxies (t, ws, q).

### Extremes (Fig. B)
- 2019 max observed 258 vs highest prediction 168.5 (and 163.4 at the hour of the observed peak); training max 195 → the peak is outside the training range (extrapolation limit), and averaging lowers predictions further.
- 25 Jul 2019: Dutch heatwave, > 40 °C nationally, 36–37 °C at Cabauw, easterly wind.

---

## 5. Likely questions — where your answer comes from
| Question | Key facts |
|---|---|
| Why did you choose O3 and Cabauw? | Section 2 rows 1–3 |
| How did you treat missing and negative data, and why? | Section 2 rows 4–5 (negatives are explained in the hand-in; the reason for dropping missing hours is not) |
| Explain how a random forest works | Section 3 |
| Why is training better than 2019? | In-sample vs unseen; RMSE 8.1 vs 15.5 |
| Why are peaks underpredicted? | Can't extrapolate, averaging, no memory; 195 vs 258 |
| What does the daily cycle show / where does the model fail? | Section 4 table |
| Why is rh the best single predictor? Is it causal? | Carries sunshine, time-of-day and season information; possibly some physical role; proxy vs cause not separated |
| Why does adding trees not help much? | Averaging converges; RMSE 15.54 → 15.42 |
| Why is R² 0.74 but best single 0.47? | The other variables add information that rh alone lacks. The experiment doesn't show whether this comes from interactions or simply extra information, nor causal importance (rh also has by far the highest feature importance, 0.49) |
| What is missing from the model? | Previous O3, boundary-layer height, transport, emissions, time variables |
| How could the model be improved? | e.g. add hour/day of year, lagged O3, BL height, more years with extremes |
| Why UTC+1? | Data convention, no summer-time jump |
| What does the bias mean? | Pred − obs < 0 → underestimate; possibly trend/background not in weather |
| Did you use AI? | Code yes (must be acknowledged); abstract text your own |

---

## 6. Weak spots an examiner may ask about (submitted version)
**Fixed in the hand-in:** AI disclosure added · reason for negatives → 0 given · conclusion now links r/R² to hourly data, daily cycle separately.

**Still open — be ready to explain in words:**
1. **Bias and predicted mean.** Exact: obs 47.932, pred 44.448, bias −3.483. Correctly rounded that is 47.9, **44.4**, **−3.5** (Fig. 2 is right). The text's **44.5** and **−3.4** are rounding errors. If asked: say the bias is −3.48 ≈ −3.5 µg m⁻³ (−7.3%).
2. **Why missing hours were dropped** — not stated (only negatives got a reason). Facts: complete-case choice; missing O3 can't be used; only 3.0% of hours; alternatives (filling predictors, built-in NaN support) exist but weren't used.
3. **Why rh is the best single predictor (step 10)** — the hand-in explains radiation and temperature in the daily-cycle paragraph, but not the single-variable ranking, especially rh. Expect this question (Section 4).
4. **Figure 2 caption** no longer explains the lines, and the plot has no legend: dashed = 1:1 line, red = least-squares regression, colour = point density.
5. **"night and late afternoon":** model is lower at 11–06 h (incl. evening 19–23 h), slightly higher at 07–10 h; largest gap 15–16 h.
6. **"don't significantly explain":** no statistical test was done; you mean their R² is near zero (or negative).
7. **"n = 10, 30, 100, 300":** n here = number of trees, not cloud cover.
8. **Training vs 2019 sentence:** be ready to say *why* training is better (in-sample vs unseen data).
9. **AI disclosure:** says references, LaTeX layout, bibliography and code. If asked, be ready to describe honestly how else Claude was involved (e.g. data checks, explaining concepts, feedback on drafts).
10. **Appendix:** "Phyton" typo; strings show "␣" for spaces (LaTeX listings display, not in the code itself).

---

## 7. Numbers card
| | Training 2016–18 | 2019 |
|---|---|---|
| Hours | 25,450 | 8,565 |
| r / R² | 0.96 / 0.91 | 0.87 / 0.74 |
| RMSE | 8.1 | 15.5 |
| Bias | 0.0 | −3.48 ≈ −3.5 (−7.3%) |
| Mean obs / pred | 43.0 / 43.0 | 47.9 / 44.4 (hand-in says 44.5) |
| Max obs / pred | 195 / 169 | 258 / 168 |

Single variables 2019 (r / R² / RMSE): rh 0.70 / 0.47 / 22.1 · t 0.67 / 0.42 / 23.2 · q 0.50 / 0.23 / 26.7 · wd 0.34 / 0.09 / 29.1 · ws 0.32 / 0.08 / 29.2 · n 0.17 / 0.01 / 30.3 · rain 0.03 / −0.03 / 30.8 · p 0.14 / −0.03 / 31.0 · all 8: 0.87 / 0.74 / 15.5

Cleaning: 35,064 h read · 1,049 dropped (3.0%) · 608 negatives → 0
Units: µg m⁻³ · Times: UTC+1 · Station: 51.97 N, 4.92 E, Lopik (Utrecht)
