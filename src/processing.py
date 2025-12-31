import pandas as pd

def merge_all(dfs):
    merged = dfs[0]
    for df in dfs[1:]:
        merged = merged.merge(df, on="time", how="outer")
    return merged.sort_values("time").reset_index(drop=True)

def align_to_hourly(df):
    df["time"] = pd.to_datetime(df["time"])
    df = df.sort_values("time").set_index("time")

    # average everything to hourly resolution
    hourly = df.resample("1H").mean()

    # Kp (3-hour cadence)
    kp3 = df[["Kp"]].resample("3H").mean()
    kp3["Kp_int"] = (kp3["Kp"] * 3).round()
    kp_hourly = kp3.reindex(hourly.index, method="ffill")

    hourly["Kp"] = kp_hourly["Kp"]

    return hourly.reset_index()
