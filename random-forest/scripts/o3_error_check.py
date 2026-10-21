# Systematic check for suspect O3 values at Cabauw (NL10644), 2016-2019.
# Flags only, nothing is removed.
# Check 1: jump from the previous hour; spike = jump up and back down (or down and back up).
# Check 2: difference with Wekerom (NL10738) at the same hour.
import pandas as pd
import os
RF_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(RF_DIR, "data", "raw")

OUT_DIR = os.path.join(RF_DIR, "results")
frames_c = []
frames_w = []
for year in [2016, 2017, 2018, 2019]:
    frames_c.append(pd.read_csv(os.path.join(RAW_DIR, "Rural_NL10644", f"Rural_NL10644_{year}.csv"), sep=";", na_values=["NA"], low_memory=False))
    frames_w.append(pd.read_csv(os.path.join(RAW_DIR, "Rural_NL10738", f"Rural_NL10738_{year}.csv"), sep=";", na_values=["NA"], low_memory=False))
cab = pd.concat(frames_c, ignore_index=True)[["date", "o3", "no", "t", "q", "ws", "wd"]]
wek = pd.concat(frames_w, ignore_index=True)[["date", "o3"]].rename(columns={"o3": "o3_wekerom"})
df = cab.merge(wek, on="date", how="left")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date").reset_index(drop=True)

# ---------------- check 1: hour-to-hour jumps ----------------
df["jump_prev"] = df["o3"] - df["o3"].shift(1)       # change from previous hour
df["jump_next"] = df["o3"].shift(-1) - df["o3"]      # change to next hour
# spike: up then down (or down then up), size = smaller of the two jumps
df["spike"] = 0.0
up_down = (df["jump_prev"] > 0) & (df["jump_next"] < 0)
down_up = (df["jump_prev"] < 0) & (df["jump_next"] > 0)
df.loc[up_down, "spike"] = pd.concat([df["jump_prev"], -df["jump_next"]], axis=1).min(axis=1)[up_down]
df.loc[down_up, "spike"] = pd.concat([-df["jump_prev"], df["jump_next"]], axis=1).min(axis=1)[down_up]

print("Hour-to-hour change |O3(t) - O3(t-1)|, percentiles (ug/m3):")
print(df["jump_prev"].abs().describe(percentiles=[0.5, 0.9, 0.99, 0.999]).round(1).to_string())
print("\nNumber of hours with |jump| above threshold:")
for thr in [20, 30, 40, 50]:
    print(f"  > {thr}: {(df['jump_prev'].abs() > thr).sum()}")
print("Number of spikes (jump there and back) above threshold:")
for thr in [15, 20, 30, 40]:
    print(f"  > {thr}: {(df['spike'] > thr).sum()}")

# ---------------- check 2: difference with Wekerom ----------------
df["diff_wek"] = df["o3"] - df["o3_wekerom"]
both = df["o3"].notna() & df["o3_wekerom"].notna()
print(f"\nHours with both stations: {both.sum()}, correlation Cabauw-Wekerom: "
      f"{df.loc[both, 'o3'].corr(df.loc[both, 'o3_wekerom']):.2f}")
print("Difference Cabauw - Wekerom, percentiles (ug/m3):")
print(df.loc[both, "diff_wek"].describe(percentiles=[0.001, 0.01, 0.5, 0.99, 0.999]).round(1).to_string())
print("Number of hours with |difference| above threshold:")
for thr in [40, 50, 60, 80]:
    print(f"  > {thr}: {(df['diff_wek'].abs() > thr).sum()}")

# ---------------- hours flagged by both checks ----------------
print("\nHours flagged by both (spike > 20 and |diff Wekerom| > 40):")
both_flag = df[(df["spike"] > 20) & (df["diff_wek"].abs() > 40)]
print(both_flag[["date", "o3", "o3_wekerom", "jump_prev", "jump_next", "spike", "diff_wek"]].round(1).to_string(index=False)
      if len(both_flag) else "  none")

# ---------------- largest cases for inspection ----------------
cols = ["date", "o3", "o3_wekerom", "jump_prev", "jump_next", "spike", "diff_wek", "no", "t", "ws", "wd"]
print("\nTop 10 spikes:")
print(df.nlargest(10, "spike")[cols].round(1).to_string(index=False))
print("\nTop 10 |difference with Wekerom|:")
print(df.loc[df["diff_wek"].abs().sort_values(ascending=False).index[:10], cols].round(1).to_string(index=False))
print("\nThe 10 highest O3 hours with their checks:")
print(df.nlargest(10, "o3")[cols].round(1).to_string(index=False))

df[cols].to_csv(os.path.join(OUT_DIR, "o3_error_check_cabauw.csv"), index=False, float_format="%.2f")
