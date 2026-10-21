# Verify numerical claims from the Codex review of oral_prep.md
import glob
import pandas as pd

BASE = r"D:\MAIO\Random forest"

# finding 8: mean predicted 2019 and bias
s = pd.read_csv(rf"{BASE}\results\statistics_step8.csv")
row = s[(s["period"] == "2019 (prediction)") & (s["resolution"] == "hourly")].iloc[0]
print("2019 mean obs", row["mean obs"], " mean pred", row["mean pred"], " bias", row["bias (pred-obs)"], " NMB", row["NMB (%)"])

# finding 7: prediction at the observed peak
p = pd.read_csv(rf"{BASE}\results\o3_cabauw_pred_2019.csv", parse_dates=["date"])
print(p.nlargest(3, "o3_obs").to_string(index=False))
print(p.nlargest(3, "o3_pred").to_string(index=False))

# finding 9: wind speed when wd missing, Cabauw vs Erzeijstraat
for station in ["Rural_NL10644", "Street_NL10639"]:
    frames = []
    for f in sorted(glob.glob(rf"{BASE}\{station}\*.csv")):
        frames.append(pd.read_csv(f, sep=";", na_values=["NA"], low_memory=False))
    df = pd.concat(frames, ignore_index=True)
    print(station, "ws when wd missing:", round(df.loc[df["wd"].isna(), "ws"].mean(), 2),
          " ws overall:", round(df["ws"].mean(), 2), " wd==0:", (df["wd"] == 0).sum(), " wd==990:", (df["wd"] == 990).sum())
