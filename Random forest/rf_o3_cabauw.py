# Random forest model for O3 at Cabauw-Wielsekade (NL10644), steps 3-6.
# Train on 2016-2018 with 8 meteorological variables, predict 2019.
# Run: conda run -n college python rf_o3_cabauw.py
import os
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
NEGATIVE_TO_ZERO = True   # True: set negative O3 to 0; False: keep them as measured
N_TREES = 30

os.makedirs(OUT_DIR, exist_ok=True)

# ---------------- step 3: read data ----------------
frames = []
for year in TRAIN_YEARS + [PRED_YEAR]:
    f = os.path.join(DATA_DIR, f"{STATION}_{year}.csv")
    frames.append(pd.read_csv(f, sep=";", na_values=["NA"], low_memory=False))
data = pd.concat(frames, ignore_index=True)
data["date"] = pd.to_datetime(data["date"])
data["year"] = data["date"].dt.year
data = data[["date", "year", TARGET] + FEATURES]

# ---------------- step 5: missing data and negative values ----------------
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
x_pred = pred[FEATURES].values
log.append(f"Training hours ({TRAIN_YEARS[0]}-{TRAIN_YEARS[-1]}): {len(train)}, "
           f"prediction hours ({PRED_YEAR}): {len(pred)}")

# ---------------- step 4: build and train the random forest ----------------
model = RandomForestRegressor(n_estimators=N_TREES, min_samples_leaf=5, random_state=42)
model.fit(x_train, y_train)
score = model.score(x_train, y_train)
log.append(f"R2 score (training data): {score:6.3f}")

# ---------------- step 6: predict 2019 ----------------
y_pred = model.predict(x_pred)

# ---------------- export ----------------
out_train = train[["date", TARGET]].rename(columns={TARGET: "o3_obs"})
out_train["o3_pred"] = model.predict(x_train)
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
print(f"\nResults written to {OUT_DIR}")
