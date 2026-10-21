# Check the time convention of the Cabauw data: no summer-time shift, and where the radiation peak falls.
import pandas as pd
import os
RF_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(RF_DIR, "data", "raw")

frames = []
for year in [2016, 2017, 2018, 2019]:
    frames.append(pd.read_csv(os.path.join(RAW_DIR, "Rural_NL10644", f"Rural_NL10644_{year}.csv"), sep=";", na_values=["NA"], low_memory=False))
df = pd.concat(frames, ignore_index=True)
df["date"] = pd.to_datetime(df["date"])
df["date_end"] = pd.to_datetime(df["date_end"])

steps = df["date"].diff().dropna().value_counts()
print("Time steps between rows:", steps.to_dict())
print("Duplicate timestamps:", df["date"].duplicated().sum())
print("date_end - date:", (df["date_end"] - df["date"]).value_counts().to_dict())

# Around the summer-time switch (last Sunday of March 2019 = 31 March, 02:00 -> 03:00 local)
print("\nRows around 31 March 2019, 00-04 h:")
print(df[(df["date"] >= "2019-03-31 00:00") & (df["date"] <= "2019-03-31 04:00")][["date", "date_end"]].to_string(index=False))

# Mean global radiation per hour of day, June-July (summer) and December-January (winter)
df["hour"] = df["date"].dt.hour
df["month"] = df["date"].dt.month
summer = df[df["month"].isin([6, 7])].groupby("hour")["q"].mean()
winter = df[df["month"].isin([12, 1])].groupby("hour")["q"].mean()
print("\nMean q (J/cm2) per 'date' hour:")
print(pd.DataFrame({"Jun-Jul": summer, "Dec-Jan": winter}).round(1).loc[8:17].to_string())
print("Hour with max q: Jun-Jul", summer.idxmax(), " Dec-Jan", winter.idxmax())
