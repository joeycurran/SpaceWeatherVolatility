import pandas as pd
import numpy as np
from pyspedas import get_data
from pyspedas.projects.omni import data as omni_data
from pyspedas.projects.kyoto import dst, load_ae
from pyspedas.projects.noaa import noaa_load_kp
from pyspedas.projects.goes import xrs

def _to_df(varname, colname=None):
    try:
        t, v = get_data(varname)
    except Exception:
        return pd.DataFrame()
    if t is None or v is None:
        return pd.DataFrame()

    return pd.DataFrame({
        "time": pd.to_datetime(t, unit="s"),
        colname or varname: v
    })

def load_omni(trange):
    omni_data(trange=trange)

    fields = [
        ("BX_GSE", "BX"),
        ("BY_GSE", "BY"),
        ("BZ_GSE", "BZ"),
        ("flow_speed", "V_SW"),
        ("proton_density", "N_p"),
        ("Pressure", "P_dyn"),
        ("SYM_H", "SYM_H"),
    ]

    dfs = [_to_df(v, c) for v, c in fields]
    df = dfs[0]
    for d in dfs[1:]:
        df = df.merge(d, on="time", how="outer")

    return df.sort_values("time").dropna(subset=["time"])


def load_kyoto(trange):
    dst(trange=trange)
    load_ae(trange=trange)

    df_dst = _to_df("kyoto_dst", "Dst")
    df_ae = _to_df("kyoto_ae", "AE")

    df = df_dst.merge(df_ae, on="time", how="outer")
    return df.sort_values("time").dropna(subset=["time"])


def load_kp(trange):
    noaa_load_kp(trange=trange)
    df = _to_df("Kp", "Kp")
    return df.sort_values("time").dropna(subset=["time"])


def load_goes_xrs(trange, probe="15"):
    xrs(trange=trange, probe=probe)

    dfA = _to_df(f"g{probe}_xrs_A_AVG", "xray_A")
    dfB = _to_df(f"g{probe}_xrs_B_AVG", "xray_B")

    df = dfA.merge(dfB, on="time", how="outer")
    df["flare_intensity"] = np.log10(df["xray_B"] + 1e-12)

    return df.sort_values("time")
