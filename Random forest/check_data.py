# Step 1: check data availability of air quality components and meteorology
# for all stations and years (2016-2019).
import glob
import os
import pandas as pd

BASE = r"D:\MAIO"
COMPONENTS = ["no2", "nox", "no", "o3", "ox", "pm10", "pm25", "bc", "co", "nh3", "so2"]
METEO = ["wd", "ws", "t", "q", "hourly_rain", "p", "n", "rh"]

rows = []
for f in sorted(glob.glob(os.path.join(BASE, "*", "*_20??.csv"))):
    df = pd.read_csv(f, sep=";", na_values=["NA"], low_memory=False)
    station = os.path.basename(os.path.dirname(f))
    year = int(os.path.basename(f)[-8:-4])
    row = {"station": station, "year": year, "hours": len(df),
           "site_eu": df["site_eu"].iloc[0], "name": df["name"].iloc[0]}
    for c in COMPONENTS + METEO:
        row[c] = 100 * df[c].notna().mean()
    for c in ["no2", "nox", "o3", "pm10", "pm25"]:
        row[c + "_neg"] = int((df[c] < 0).sum())
        row[c + "_mean"] = df[c].mean()
    rows.append(row)

res = pd.DataFrame(rows)
pd.set_option("display.width", 250)
pd.set_option("display.max_columns", 50)

print("\n=== Station info ===")
print(res.groupby("station")[["site_eu", "name"]].first().to_string())

print("\n=== Hours per file ===")
print(res.pivot(index="station", columns="year", values="hours").to_string())

print("\n=== Air quality: % hours with data (per year 2016/17/18/19) ===")
for c in COMPONENTS:
    t = res.pivot(index="station", columns="year", values=c).round(0).astype(int)
    if t.values.max() == 0:
        continue
    print(f"\n-- {c} --")
    print(t.to_string())

print("\n=== Meteo: min % available over all years ===")
print(res.groupby("station")[METEO].min().round(1).to_string())

print("\n=== Negative values (count, all years) and mean (2016-2019) ===")
neg = res.groupby("station")[[c + "_neg" for c in ["no2", "nox", "o3", "pm10", "pm25"]]].sum()
mean = res.groupby("station")[[c + "_mean" for c in ["no2", "nox", "o3", "pm10", "pm25"]]].mean().round(1)
print(pd.concat([neg, mean], axis=1).to_string())

res.to_csv(os.path.join(BASE, "data_availability.csv"), index=False)
