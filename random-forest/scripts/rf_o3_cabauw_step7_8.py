# Steps 7-8: plot observed vs predicted O3 at Cabauw and calculate statistics.
# Needs the output of rf_o3_cabauw.py (steps 3-6, n_estimators = 30).
# Run: conda run -n college python rf_o3_cabauw_step7_8.py
import os
import numpy as np
import pandas as pd
from scipy.stats import gaussian_kde
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
RF_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(RF_DIR, "data", "raw")

# ---------------- settings ----------------
OUT_DIR = os.path.join(RF_DIR, "results")
UNIT = "µg m$^{-3}$"

# ---------------- read results of steps 3-6 ----------------
train = pd.read_csv(os.path.join(OUT_DIR, "o3_cabauw_train_2016-2018.csv"), parse_dates=["date"])
pred = pd.read_csv(os.path.join(OUT_DIR, "o3_cabauw_pred_2019.csv"), parse_dates=["date"])

# ---------------- step 8: statistics ----------------
# Hourly values, and daily means (days with at least 18 valid hours).
rows = []
for period, df in [("2016-2018 (training)", train), ("2019 (prediction)", pred)]:
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
pd.set_option("display.width", 250)
pd.set_option("display.max_columns", 30)
print(stats.round(2).to_string(index=False))

# ---------------- step 7: plots ----------------
plt.rcParams.update({"font.size": 10})

# Figure A: mean daily cycle in 2019 (mean of all hourly values per hour of day)
pred["hour"] = pred["date"].dt.hour
cycle = pred.groupby("hour")[["o3_obs", "o3_pred"]].mean()
cycle_out = cycle.rename(columns={"o3_obs": "o3_obs_mean", "o3_pred": "o3_pred_mean"})
cycle_out.insert(0, "n_hours", pred.groupby("hour")["o3_obs"].count())
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
obs = pred["o3_obs"].values
mod = pred["o3_pred"].values
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
ax.plot(pred["date"], pred["o3_obs"], color="black", lw=0.4, label="Observed")
ax.plot(pred["date"], pred["o3_pred"], color="tab:red", lw=0.4, alpha=0.8, label="Random forest")
ax.set_ylabel(f"Hourly O$_3$ ({UNIT})")
ax.set_title("Cabauw (NL10644), 2019, hourly")
ax.legend(loc="upper left", frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(OUT_DIR, "fig_hourly_2019_full.png"), dpi=200)
plt.close(fig)

print(f"\nFigures and statistics written to {OUT_DIR}")
