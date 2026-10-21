# How large is the seasonal variation of O3 at Cabauw compared with other time scales?
import pandas as pd

STATION = "Rural_NL10644"
frames = []
for year in [2016, 2017, 2018, 2019]:
    frames.append(pd.read_csv(rf"D:\MAIO\{STATION}\{STATION}_{year}.csv", sep=";", na_values=["NA"], low_memory=False))
df = pd.concat(frames, ignore_index=True)
df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["hour"] = df["date"].dt.hour

# monthly means per year and averaged over the 4 years
monthly = df.groupby(["year", "month"])["o3"].mean().unstack("year")
monthly["2016-2019"] = df.groupby("month")["o3"].mean()
print("Monthly mean O3 (ug/m3):")
print(monthly.round(1).to_string())

# size of variation at different time scales
month_mean = df.groupby("month")["o3"].mean()
hour_mean = df.groupby("hour")["o3"].mean()
daily = df.set_index("date")["o3"].resample("D").mean()
print(f"\nSeasonal cycle (range of monthly means): {month_mean.min():.1f} to {month_mean.max():.1f} "
      f"= {month_mean.max() - month_mean.min():.1f}")
print(f"Daily cycle (range of hour-of-day means): {hour_mean.min():.1f} to {hour_mean.max():.1f} "
      f"= {hour_mean.max() - hour_mean.min():.1f}")
print(f"Std of daily means: {daily.std():.1f}; std of hourly values: {df['o3'].std():.1f}")

# share of hourly variance explained by month (between-month variance / total variance)
df["month_mean"] = df.groupby("month")["o3"].transform("mean")
df["hour_mean"] = df.groupby("hour")["o3"].transform("mean")
ok = df["o3"].notna()
total_var = df.loc[ok, "o3"].var()
print(f"Fraction of hourly variance explained by month alone: {df.loc[ok, 'month_mean'].var() / total_var:.2f}")
print(f"Fraction of hourly variance explained by hour of day alone: {df.loc[ok, 'hour_mean'].var() / total_var:.2f}")

# monthly means of O3 together with weather and NO2 (2016-2019)
print("\nMonthly means 2016-2019:")
print(df.groupby("month")[["o3", "no2", "no", "t", "q", "ws", "rh", "n"]].mean().round(1).to_string())

# daily cycle amplitude per season
df["season"] = df["month"].map({12: "DJF", 1: "DJF", 2: "DJF", 3: "MAM", 4: "MAM", 5: "MAM",
                                6: "JJA", 7: "JJA", 8: "JJA", 9: "SON", 10: "SON", 11: "SON"})
cyc = df.groupby(["season", "hour"])["o3"].mean().unstack("hour")
print("\nDaily cycle per season (min, max, range):")
print(pd.DataFrame({"min": cyc.min(axis=1), "max": cyc.max(axis=1),
                    "range": cyc.max(axis=1) - cyc.min(axis=1)}).round(1).to_string())
