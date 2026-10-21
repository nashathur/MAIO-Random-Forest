import pandas as pd
import os
RF_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(RF_DIR, "data", "raw")

stations = ["Street_NL10639", "Rural_NL10644", "Rural_NL10738", "Urban_NL10418", "Street_NL10236"]
met = ["t", "ws", "q", "rh", "p"]
d = {s: pd.read_csv(os.path.join(RAW_DIR, s, f"{s}_2018.csv"), sep=";", na_values=["NA"], low_memory=False) for s in stations}
ref = d["Street_NL10639"]
for s in stations[1:]:
    same = {c: round(100 * (d[s][c] == ref[c]).mean(), 1) for c in met}
    print(f"{s} vs Street_NL10639, % identical hours 2018:", same)

for s in ["Rural_NL10644", "Rural_NL10738"]:
    df = pd.concat([pd.read_csv(os.path.join(RAW_DIR, s, f"{s}_{y}.csv"), sep=";", na_values=["NA"], low_memory=False)
                    for y in range(2016, 2020)])
    df["hour"] = pd.to_datetime(df.date).dt.hour
    print(f"\n{s}: O3 mean {df.o3.mean():.1f}, NO mean {df.no.mean():.1f}, NO2 mean {df.no2.mean():.1f}, "
          f"O3<0 {100 * (df.o3 < 0).mean():.1f}%, night(0-5h) O3 {df[df.hour < 6].o3.mean():.1f}, "
          f"afternoon(13-16h) O3 {df[df.hour.between(13, 16)].o3.mean():.1f}, max {df.o3.max():.0f}")
    print("  corr with O3:", df[["t", "q", "ws", "rh"]].corrwith(df.o3).round(2).to_dict())
