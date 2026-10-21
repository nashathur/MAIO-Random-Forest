import glob
import pandas as pd

fs = sorted(glob.glob(r"D:\MAIO\Street_NL10639\*.csv"))
df = pd.concat([pd.read_csv(f, sep=";", na_values=["NA"], low_memory=False) for f in fs])
df["year"] = df["date"].str[:4].astype(int)
met = ["wd", "ws", "t", "q", "hourly_rain", "p", "n", "rh"]

print("missing hours per year:")
print(df.groupby("year")[["o3"] + met].apply(lambda g: g.isna().sum()).to_string())
print("\nwd==990 (variable):", (df.wd == 990).sum(), " wd==0 (calm):", (df.wd == 0).sum())
print("rows with any missing (o3+met):", df[["o3"] + met].isna().any(axis=1).sum(), "of", len(df))

print("\nws (m/s) when wd missing:", df.loc[df.wd.isna(), "ws"].describe().round(2).to_dict())
print("ws (m/s) overall mean:", round(df.ws.mean(), 2))

for c in ["o3", "wd"]:
    runs, n = [], 0
    for v in df[c].isna().values:
        if v:
            n += 1
        elif n:
            runs.append(n)
            n = 0
    if n:
        runs.append(n)
    s = pd.Series(runs)
    print(f"\n{c} gaps: {len(s)} gaps; 1h: {(s == 1).sum()}, 2-3h: {s.between(2, 3).sum()}, "
          f"4-24h: {s.between(4, 24).sum()}, >24h: {(s > 24).sum()}; longest {s.max()} h")
