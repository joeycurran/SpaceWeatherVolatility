from pathlib import Path
import pandas as pd
from ingestion import load_omni, load_kyoto, load_kp, load_goes_xrs
from processing import merge_all, align_to_hourly


DATA_DIR = Path(__file__).resolve().parents[1] / "data"

OUT_MERGED = DATA_DIR / "space_weather_merged.csv"
OUT_HOURLY = DATA_DIR / "space_weather_aligned.csv"


def build_dataset(trange):
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    df_omni = load_omni(trange)
    df_kyoto = load_kyoto(trange)
    df_kp = load_kp(trange)
    df_goes = load_goes_xrs(trange)

    df_merged = merge_all([df_omni, df_kyoto, df_kp, df_goes])
    df_merged.to_csv(OUT_MERGED, index=False)

    df_hourly = align_to_hourly(df_merged)
    df_hourly.to_csv(OUT_HOURLY, index=False)

    print("Saved merged dataset:", OUT_MERGED)
    print("Saved hourly aligned dataset:", OUT_HOURLY)
