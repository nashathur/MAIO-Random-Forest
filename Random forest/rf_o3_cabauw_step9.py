# Step 9: effect of the number of trees (n_estimators) on the random forest O3 model at Cabauw.
# Same data, cleaning and settings as rf_o3_cabauw.py; only n_estimators is changed.
# Run: conda run -n college python rf_o3_cabauw_step9.py
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
N_TREES_LIST = [10, 30, 100, 300]

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
x_train, y_train = train[FEATURES].values, train[TARGET].values
x_pred, y_obs = pred[FEATURES].values, pred[TARGET].values

# ---------------- loop over number of trees ----------------
rows = []
for n_trees in N_TREES_LIST:
    model = RandomForestRegressor(n_estimators=n_trees, min_samples_leaf=5, random_state=42)
    model.fit(x_train, y_train)
    for period, obs, mod in [("2016-2018 (training)", y_train, model.predict(x_train)),
                             ("2019 (prediction)", y_obs, model.predict(x_pred))]:
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
    print(f"n_estimators = {n_trees} done")

table = pd.DataFrame(rows)
table.to_csv(os.path.join(OUT_DIR, "step9_n_estimators.csv"), index=False, float_format="%.3f")
pd.set_option("display.width", 250)
pd.set_option("display.max_columns", 30)
print()
print(table.round(2).to_string(index=False))
