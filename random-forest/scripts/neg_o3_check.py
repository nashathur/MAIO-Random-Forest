import glob
import pandas as pd
import os
RF_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(RF_DIR, "data", "raw")

fs = sorted(glob.glob(os.path.join(RAW_DIR, "Street_NL10639", "*.csv")))
df = pd.concat([pd.read_csv(f, sep=";", na_values=["NA"], low_memory=False) for f in fs])
df["date"] = pd.to_datetime(df["date"])
df["hour"] = df["date"].dt.hour
df["month"] = df["date"].dt.month
df = df.dropna(subset=["o3"])
neg = df[df.o3 < 0]

print(f"negative O3: {len(neg)} of {len(df)} hours ({100 * len(neg) / len(df):.1f}%)")
print("size of negatives (ug/m3):", neg.o3.describe().round(2).to_dict())
print("hours with O3 < -5:", (neg.o3 < -5).sum())

print("\nshare negative by hour of day (%):")
print((100 * df.groupby("hour").o3.apply(lambda s: (s < 0).mean())).round(1).to_string())
print("\nshare negative by month (%):")
print((100 * df.groupby("month").o3.apply(lambda s: (s < 0).mean())).round(1).to_string())

cols = ["no", "no2", "nox", "ws", "t", "q", "rh"]
comp = pd.DataFrame({"O3 < 0": neg[cols].mean(), "all hours": df[cols].mean()}).round(1)
print("\nconditions (means):")
print(comp.to_string())
print("\nweekday share of negatives (Mon=0):")
print((100 * neg.date.dt.dayofweek.value_counts(normalize=True).sort_index()).round(0).to_string())
