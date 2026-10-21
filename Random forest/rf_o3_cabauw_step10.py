# Step 10: random forest O3 model at Cabauw with one meteorological variable at a time.
# Same data, cleaning and settings as rf_o3_cabauw.py (n_estimators = 30).
# All runs use the same hours (rows with all 8 variables present), so only the variable differs.
# Run: conda run -n college python rf_o3_cabauw_step10.py
import os
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# ---------------- settings ----------------
STATION = "Rural_NL10644"
DATA_DIR = rf"D:\MAIO\{STATION}"
OUT_DIR = r"D:\MAIO\results"
TARGET = "o3"
FEATURES = ["wd", "ws", "t", "q", "hourly_rain", "p", "n", "rh"]
TRAIN_YEARS = [2016, 2017, 2018]
PRED_YEAR = 2019
NEGATIVE_TO_ZERO = True
N_TREES = 30

# ---------------- read data (as in step 3) ----------------
frames = []
for year in TRAIN_YEARS + [PRED_YEAR]:
    f = os.path.join(DATA_DIR, f"{STATION}_{year}.csv")
    frames.append(pd.read_csv(f, sep=";", na_values=["NA"], low_memory=False))
data = pd.concat(frames, ignore_index=True)
data["date"] = pd.to_datetime(data["date"])
data["year"] = data["date"].dt.year

# ---------------- clean data (as in step 5) ----------------
clean = data.dropna(subset=[TARGET] + FEATURES).copy()
if NEGATIVE_TO_ZERO:
    clean[TARGET] = clean[TARGET].clip(lower=0)
train = clean[clean["year"].isin(TRAIN_YEARS)]
pred = clean[clean["year"] == PRED_YEAR]
y_train = train[TARGET].values
y_obs = pred[TARGET].values

# ---------------- runs: all 8 variables, then each variable alone ----------------
runs = [("all 8", FEATURES)]
for var in FEATURES:
    runs.append((var, [var]))

rows = []
for name, variables in runs:
    model = RandomForestRegressor(n_estimators=N_TREES, min_samples_leaf=5, random_state=42)
    model.fit(train[variables].values, y_train)
    for period, obs, mod in [("2016-2018 (training)", y_train, model.predict(train[variables].values)),
                             ("2019 (prediction)", y_obs, model.predict(pred[variables].values))]:
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
    print(f"{name} done")

table = pd.DataFrame(rows)
table.to_csv(os.path.join(OUT_DIR, "step10_single_variables.csv"), index=False, float_format="%.3f")
pd.set_option("display.width", 250)
pd.set_option("display.max_columns", 30)
print()
print(table.round(2).to_string(index=False))
