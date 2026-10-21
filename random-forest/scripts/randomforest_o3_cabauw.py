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
