# Compare the three rural stations: local NOx level and O3 data availability, 2016-2019.
import pandas as pd
import os
RF_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(RF_DIR, "data", "raw")

for station in ["Rural_NL10644", "Rural_NL10738", "Rural_NL10617"]:
    frames = []
    for year in [2016, 2017, 2018, 2019]:
        frames.append(pd.read_csv(os.path.join(RAW_DIR, station, f"{station}_{year}.csv"), sep=";", na_values=["NA"], low_memory=False))
    df = pd.concat(frames, ignore_index=True)
    df["year"] = df["date"].str[:4].astype(int)
    print(f"\n{station}: {df['name'].unique().tolist()}")
    print(f"  mean NO {df['no'].mean():.1f}, NO2 {df['no2'].mean():.1f}, NOx {df['nox'].mean():.1f}, O3 {df['o3'].mean():.1f}")
    print("  O3 available (%) per year:", (100 * df.groupby("year")["o3"].apply(lambda s: s.notna().mean())).round(0).to_dict())
