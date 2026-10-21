import pandas as pd

met = ["t", "q", "ws", "rh", "p", "n", "hourly_rain"]
for s in ["Rural_NL10644", "Rural_NL10738", "Street_NL10639"]:
    df = pd.concat([pd.read_csv(rf"D:\MAIO\{s}\{s}_{y}.csv", sep=";", na_values=["NA"], low_memory=False)
                    for y in range(2016, 2020)])
    df["date"] = pd.to_datetime(df.date)
    df["year"] = df.date.dt.year
    wkend = df.date.dt.dayofweek >= 5
    print(f"\n=== {s} ===")
    for c in ["o3", "no2"]:
        r = df[met].corrwith(df[c]).round(2).to_dict()
        ratio = df.loc[wkend, c].mean() / df.loc[~wkend, c].mean()
        trend = df.groupby("year")[c].mean()
        print(f"{c}: corr {r}")
        print(f"     weekend/weekday ratio {ratio:.2f}; yearly mean {trend.round(1).to_dict()} "
              f"({100 * (trend[2019] / trend[2016] - 1):+.0f}% 2016->2019)")
