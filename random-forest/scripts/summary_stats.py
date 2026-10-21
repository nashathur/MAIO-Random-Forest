import glob
import pandas as pd
import os
RF_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(RF_DIR, "data", "raw")

fs = sorted(glob.glob(os.path.join(RAW_DIR, "Street_NL10639", "*.csv")))
df = pd.concat([pd.read_csv(f, sep=";", na_values=["NA"], low_memory=False) for f in fs])
df["date"] = pd.to_datetime(df["date"])
df["year"] = df.date.dt.year
print("columns:", len(df.columns))
print("all-empty columns:", [c for c in df.columns if df[c].isna().all()])

g = df.groupby("year")
o3 = g.o3.agg(["mean", "median", lambda s: s.quantile(0.95), "max"]).round(1)
o3.columns = ["O3 mean", "O3 median", "O3 p95", "O3 max"]
o3["hours O3>120"] = g.o3.apply(lambda s: (s > 120).sum())
o3["NO2 mean"] = g.no2.mean().round(1)
o3["NO mean"] = g.no.mean().round(1)
o3["Ox mean"] = g.ox.mean().round(1)
print(o3.to_string())

met = pd.DataFrame({
    "t mean": g.t.mean(), "t max": g.t.max(), "t min": g.t.min(),
    "ws mean": g.ws.mean(), "q sum (MJ/m2)": g.q.sum() / 100,
    "rain (mm)": g.hourly_rain.apply(lambda s: s.clip(lower=0).sum()),
    "rh mean": g.rh.mean(), "p mean": g.p.mean(), "n mean": g.n.mean(),
}).round(1)
print(met.to_string())

df["season"] = df.date.dt.month.map({12: "DJF", 1: "DJF", 2: "DJF", 3: "MAM", 4: "MAM", 5: "MAM",
                                     6: "JJA", 7: "JJA", 8: "JJA", 9: "SON", 10: "SON", 11: "SON"})
print(df.groupby("season")[["o3", "no2", "t", "q", "ws"]].mean().round(1).to_string())
print(df.groupby(df.date.dt.hour)[["o3", "no2"]].mean().round(1).T.to_string())

hw = df[(df.date >= "2019-07-22") & (df.date < "2019-07-28")]
print("heatwave 22-27 Jul 2019: t max", hw.t.max(), " O3 max", hw.o3.max(),
      " daily O3 max:", hw.groupby(hw.date.dt.day).o3.max().round(0).to_dict())
top = df.nlargest(5, "o3")[["date", "o3", "t", "q", "ws"]]
print(top.to_string(index=False))
print("corr with O3:", df[["t", "q", "ws", "rh", "p", "n", "hourly_rain", "no", "no2"]].corrwith(df.o3).round(2).to_dict())
print("prevailing wd sector share (%):",
      (100 * pd.cut(df.wd, [0, 45, 135, 225, 315, 360], labels=["N", "E", "S", "W", "N2"])
       .replace("N2", "N").value_counts(normalize=True)).round(0).to_dict())
