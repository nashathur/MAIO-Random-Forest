import pandas as pd
for s in ["Rural_NL10644", "Rural_NL10738"]:
    df = pd.concat([pd.read_csv(rf"D:\MAIO\{s}\{s}_{y}.csv", sep=";", na_values=["NA"], low_memory=False) for y in range(2016, 2020)])
    df["date"] = pd.to_datetime(df.date)
    print(s, "yearly max:", df.groupby(df.date.dt.year).o3.max().round(0).to_dict())
    print(df.nlargest(6, "o3")[["date", "o3", "no2", "t", "q", "ws", "wd"]].to_string(index=False))
