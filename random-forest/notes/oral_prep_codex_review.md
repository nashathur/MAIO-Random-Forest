No files changed; no Python run. I checked the PDFs with `pdftotext`, read the CSVs, and checked auxiliary numbers against the archived station CSVs using PowerShell. Line numbers below refer to [oral_prep.md](</D:/MAIO/random-forest/notes/oral_prep.md>).

**CONFIRMED** means checked against documentary or numerical evidence; **UNVERIFIED** marks scientific interpretation not established by this experiment.

1. **CONFIRMED — L35: “with random variable choice.”**  
   **Wrong:** This suggests random subsets of predictors at each split, which this implementation does not request.  
   **Evidence:** `randomforest_o3_cabauw.py:70` leaves `max_features` at its default: all eight predictors are considered. Bootstrap sampling supplies the main randomness; feature order and tied splits can also be random. [scikit-learn documentation](https://scikit-learn.org/1.5/modules/generated/sklearn.ensemble.RandomForestRegressor.html).  
   **Correct:** Each tree uses a bootstrap sample of training hours, while this configuration considers all eight variables at each split.

2. **UNVERIFIED — L60: “r is always positive (pred vs obs).”**  
   **Wrong:** Prediction–observation correlation has no guaranteed positive sign on unseen data; it can be negative or undefined for constant predictions.  
   **Evidence:** Pearson correlation measures covariance, whose sign is unrestricted. `step10_single_variables.csv` happens to contain eight positive 2019 correlations; that does not establish a general rule. The separate raw rh–O₃ correlation checks out: −0.697 ≈ −0.70 for 2016–2019.  
   **Correct:** All eight single-variable runs here have positive test correlations, but random-forest test correlations need not be positive.

3. **UNVERIFIED — L68, L70, L88: “Net production needs VOCs”; radiation → “direct production.”**  
   **Wrong:** VOCs are not strictly required: CO oxidation also generates HO₂, which converts NO to NO₂ without consuming O₃. NO₂ photolysis alone does not produce net ozone when balanced by NO titration. The ozone-formation reaction also omits its third body, M.  
   **Evidence:** The radical pathways include CO, methane and other VOC oxidation. [Tropospheric ozone chemistry](https://acp.copernicus.org/articles/21/4187/2021/).  
   **Correct:** Net photochemical production requires radical-mediated NO oxidation, supplied by CO/VOC chemistry; O + O₂ + M → O₃ + M, while global radiation is a proxy for photolysis conditions.

4. **CONFIRMED — L117: “Variables combine non-linearly; no single variable dominates.”**  
   **Wrong:** The improvement from single-variable to combined prediction establishes neither nonlinear interactions nor absence of a dominant predictor. Additional information can improve predictions without interactions.  
   **Evidence:** `step10_single_variables.csv:19` gives rh R² = 0.474 versus 0.740 for all eight. `run_log.txt:12` gives rh impurity importance = 0.485, substantially above every other feature; that importance is also not a causal share.  
   **Correct:** Relative humidity is the strongest individual predictor, and additional variables improve predictive performance; these experiments do not determine causal dominance or isolate interactions.

5. **UNVERIFIED — L44: the train–test drop “shows how much the model memorised vs generalised.”**  
   **Wrong:** The gap does not quantify memorisation. It combines training optimism with changes in the test distribution, including unusually high 2019 concentrations. “Only 2019 measures real skill” is also too absolute: other properly held-out periods could estimate generalisation.  
   **Evidence:** `statistics_step8.csv:2,4`: training/test RMSE = 8.146/15.536; observed maxima = 195.190/257.860 µg m⁻³. [Time-series evaluation guidance](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation-of-time-series-data).  
   **Correct:** The in-sample score is optimistic, and 2019 estimates generalisation to that year; their difference cannot be assigned entirely to memorisation.

6. **CONFIRMED — L22, L131: “The RF needs complete (weather, O3) pairs.”**  
   **Wrong:** This presents complete meteorological inputs as a universal RF requirement. Modern scikit-learn random forests support missing predictor values; other workflows can impute predictors. Missing observed targets are a separate issue.  
   **Evidence:** `randomforest_o3_cabauw.py:53` explicitly chooses complete-case filtering. [scikit-learn documents native NaN support](https://scikit-learn.org/1.5/modules/generated/sklearn.ensemble.RandomForestRegressor.html). The version used for the original run was not verified.  
   **Correct:** This workflow chose to drop incomplete hours; fitting and observed-target evaluation require available O₃ targets, while missing predictors have alternative treatments.

7. **CONFIRMED — L38, L101: “195 … → predictions top out around 168.”**  
   **Wrong:** The extrapolation bound does not specifically explain the 168 maximum. Also, “258 observed versus 168 predicted” compares separate maxima, not the prediction at the observed peak.  
   **Evidence:** `statistics_step8.csv:4` gives maxima 257.860/168.493. `o3_cabauw_pred_2019.csv` gives 257.86 observed and **163.37 predicted at 16:00 on 25 July**; the prediction maximum, 168.49, occurs at 17:00.  
   **Correct:** Predictions cannot exceed the training-target maximum, 195.19; leaf and forest averaging further limit the realised maximum, and the observed peak was predicted as 163.37.

8. **CONFIRMED — L130, L150: predicted mean 44.5; “47.9 − 44.5” explains negative bias.**  
   **Wrong:** The predicted mean is incorrectly rounded, and the written subtraction has the wrong sign for pred−obs bias.  
   **Evidence:** `statistics_step8.csv:4`: mean prediction **44.448**, mean observation 47.932, bias −3.483 µg m⁻³. The submitted abstract itself reports 44.5 and −3.4, so the notes reproduce a hand-in error.  
   **Correct:** The predicted mean rounds to **44.4**, and bias is mean(pred−obs), −3.483 ≈ **−3.5 µg m⁻³**, with NMB −7.3%.

9. **CONFIRMED — L22: missing-direction wind speed “1.3 vs 3.3 m/s”; L131: “missing wind direction = calm wind.”**  
   **Wrong:** The comparison belongs to Erzeijstraat, not Cabauw. Lower wind speeds do not establish that every missing direction denotes calm conditions.  
   **Evidence:** Archived 2016–2019 CSVs give Erzeijstraat means **1.3397/3.3004 m s⁻¹**, versus Cabauw **1.2847/4.1091 m s⁻¹**. `gaps_check.py:8` selects `Street_NL10639`. Assignment Table 1 specifies **0** for calm direction, without defining NA as calm.  
   **Correct:** At Cabauw, missing direction is associated with lower wind speeds—1.3 versus 4.1 m s⁻¹—but its exact missing-value cause is not established here.

10. **CONFIRMED — L49, L55: r describes “pattern/timing”; r² differs from R² “because R² also penalises the bias.”**  
    **Wrong:** The explanation omits amplitude calibration. Correlation ignores positive rescaling as well as additive bias, and does not directly establish correct timing.  
    **Evidence:** `statistics_step8.csv:4` gives observed/predicted standard deviations 30.439/24.511. For population standard deviations,
    \[
    r^2-R^2=(\sigma_{\rm pred}/\sigma_{\rm obs}-r)^2+
    (\mathrm{bias}/\sigma_{\rm obs})^2.
    \]
    Here the contributions are approximately **0.0042 from scale mismatch** and **0.0131 from mean bias**.  
    **Correct:** R² penalises both bias and amplitude miscalibration, whereas r measures linear association without ensuring either calibration or correct cycle timing.

11. **UNVERIFIED — L84: “Afternoon peak (~15 h): maximum photochemistry and deep mixing.”**  
    **Wrong:** A concentration maximum is not necessarily a production-rate maximum. Deep mixing can supply ozone or dilute it, depending on vertical gradients.  
    **Evidence:** Concentration reflects accumulated production, transport and losses; its peak can follow the production-rate peak. [Measurements distinguishing ozone production from concentration](https://acp.copernicus.org/articles/24/9805/2024/). No production-rate or boundary-layer-height measurements were analysed here.  
    **Correct:** The afternoon concentration maximum reflects the evolving ozone budget; this daily cycle does not establish when photochemical production or mixing peaks.

12. **UNVERIFIED — L94–98, L118: transport cannot be captured; annual increase presented under “Emission changes.”**  
    **Wrong:** Wind and other meteorological predictors can capture some transport information indirectly. An increase in annual ozone alone does not establish an emissions cause or explain the model bias.  
    **Evidence:** The code includes wind direction and speed. The raw means **41.645 → 48.022 µg m⁻³** check out, but no emissions, trajectories or attribution analysis were supplied. Meteorology, chemistry and transport interact. [Ozone–temperature mechanisms](https://acp.copernicus.org/articles/19/13367/2019/).  
    **Correct:** Emissions, background ozone and transport are not explicitly resolved, although meteorology supplies proxies; the annual increase and negative bias have not been causally attributed.

13. **UNVERIFIED — L89–90: “hot days = stagnant … high-pressure”; rh is “mostly” a proxy.**  
    **Wrong:** These are associations, not identities, and the experiment cannot establish how much of rh’s predictive skill is proxy behaviour. Humidity also affects ozone chemistry and vegetation uptake.  
    **Evidence:** Temperature–ozone relationships involve precursor chemistry, emissions, deposition and circulation; RH can affect stomatal ozone removal. [Temperature mechanisms](https://acp.copernicus.org/articles/19/13367/2019/), [deposition observations](https://acp.copernicus.org/articles/24/12323/2024/).  
    **Correct:** Temperature and RH carry correlated meteorological information and can connect to physical processes; their respective causal and proxy contributions were not separated.

14. **CONFIRMED — L110: missing and negative treatment “not yet explained in the abstract text.”**  
    **Wrong:** This contradicts the submitted version and the notes’ own L127. Negative-value treatment is explicitly explained.  
    **Evidence:** Hand-in p. 1 states that negative concentrations are physically meaningless and may arise from measurement uncertainty or noise. It describes missing-hour removal and its 3.0% extent, but does not justify that choice. Source: :codex-file-citation{path="C:/Users/thurs/Downloads/MAIO_Hand_In_Thursina-Ahsan_8256675.pdf" purpose="source"}  
    **Correct:** The abstract explains zero-clipping of negatives; the rationale for dropping missing hours remains unexplained in the abstract prose.

15. **CONFIRMED — L132: hand-in gives “no meteorology/chemistry explanation” for rh, t and q.**  
    **Wrong:** This is too broad. The hand-in does explain radiation and temperature in its daily-cycle discussion.  
    **Evidence:** Hand-in p. 1 connects daytime ozone increases to stronger photochemical production under higher radiation and temperature, plus boundary-layer mixing. It does not explain why rh wins the single-variable comparison.  
    **Correct:** The missing explanation concerns the single-variable ranking—especially RH’s strength—not a complete absence of temperature/radiation physics.

16. **CONFIRMED — L95: Fan et al. found previous-day O₃ “always selected.”**  
    **Wrong:** The wording drops the model-specific scope. The paper explicitly says “always” for its classifier; its regression discussion uses “mostly” above the selection threshold.  
    **Evidence:** [Fan et al., “Feature Selection”](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2022.781309/full), classifier versus two-phase regression paragraphs.  
    **Correct:** Previous-day ozone was consistently important in Fan et al.; the explicit always-selected statement refers to their classifier.

17. **CONFIRMED — L92: Otero’s “daily max O₃.”**  
    **Wrong:** The shorthand leaves the ozone averaging period unclear, which matters when comparing it with this hourly study.  
    **Evidence:** Otero et al. used **maximum daily eight-hour average ozone (MDA8)**, with temperature especially important in summer and RH/radiation particularly relevant in spring. [Original paper reproduced in the author’s dissertation, pp. 47 and 55](https://refubium.fu-berlin.de/bitstream/handle/fub188/9481/Dissertation_NoeliaOtero_online_feb22.pdf?sequence=1&isAllowed=y).  
    **Correct:** Otero’s result concerns MDA8 ozone with seasonal and regional differences, not an annual hourly predictor ranking.

18. **UNVERIFIED — L71: dry deposition removes ozone “especially at night.”**  
    **Wrong:** This can confuse strong nighttime concentration depletion with a universally larger deposition flux or velocity at night. Stomatal uptake commonly increases during daylight.  
    **Evidence:** Deposition’s effect on concentration depends on mixing depth and replenishment as well as uptake; measured deposition velocities can peak during daytime. [Diurnal ozone deposition measurements](https://acp.copernicus.org/articles/21/18393/2021/index.html).  
    **Correct:** Deposition continues at night and can strongly deplete a shallow, poorly replenished surface layer, without being strongest at night.

**Other numerical checks:** No additional discrepancies found in the reported scores, single-variable results, tree-number experiments, cleaning counts, daily-cycle values, peak sequence, station coordinates, coverage percentages, NO means, weekend ratios or negative-value statistics. The annual 41.6/48.0 means concern raw available observations; 47.9 concerns cleaned 2019 evaluation hours.

**Verification limits:** Authorship history, the referenced CLASS exercise results, the installed scikit-learn version, and the appendix’s exact visual space-marker glyph were not verified.

### Suggestions

- **Check missing-hour representativeness.** `fig_daily_cycle_2019_values.csv:4` contains only 272 samples at 02:00, compared with roughly 355–365 at most other hours. The small overall missing percentage does not guarantee an unbiased hourly climatology.
- **Distinguish retrospective prediction from operational forecasting.** `randomforest_o3_cabauw.py:64–76` uses contemporaneous meteorological observations. Adding lagged ozone would require an explicit forecast horizon and availability rules to avoid unintended information leakage.
- **Check AI-use scope against the assignment.** Coding assistance is allowed with disclosure, while assignment p. 2 prohibits AI use for the extended abstract. The disclosure and L122 cannot independently establish how the prose was produced. Source: :codex-file-citation{path="D:/MAIO/random-forest/report/Handin_Random_Forest_2026.pdf" purpose="source"}
- **Check paths before a future rerun.** Resolved: `randomforest_o3_cabauw.py:18–19` now reads from `random-forest/data/raw/Rural_NL10644` and writes to `random-forest/results`, relative to the script location.

**Overall verdict:** The numerical foundation is mostly sound, but several central machine-learning explanations and physical attributions need correction before the notes are memorised.