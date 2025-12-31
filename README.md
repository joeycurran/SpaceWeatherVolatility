# SpaceWeatherVolatility 🌌

**Predicting geomagnetic storm probability and tail-risk using solar-wind and flare data**

This project applies quantitative-finance volatility forecasting techniques to space weather prediction, using statistical models (logistic regression, Extreme Value Theory, GARCH) and machine learning to understand how solar flares and solar-wind dynamics drive extreme geomagnetic events.

---

## 🎯 Project Overview

**Primary Goal:** Estimate the conditional probability and tail-risk of geomagnetic storms (`Kp ≥ 5`) from upstream solar and flare variables in real-time.

The project integrates open satellite data from NASA and NOAA, performs comprehensive feature engineering, and fits multiple statistical and machine learning models for:

- **Storm Probability Prediction** via logistic regression and gradient boosting (XGBoost, LightGBM)
- **Tail Risk Analysis** via **Extreme Value Theory (Generalized Pareto Distribution)**
- **Volatility Dynamics** via **GARCH(1,1)** or **Hawkes processes** (optional)

---

## 📊 Data Sources

| Dataset | Description | Key Variables | Access |
|---------|-------------|---------------|--------|
| **NASA OMNIWeb** | Solar-wind & geomagnetic indices (1-min, hourly) | IMF Bz, V<sub>SW</sub>, density, AE, Kp, Dst, F10.7 | [OMNIWeb API](https://omniweb.gsfc.nasa.gov/ow_min.html) |
| **NOAA GOES XRS** | X-ray flux & flare events | Short/long flux, flare start/end/class | [SWPC GOES API](https://services.swpc.noaa.gov/json/goes/) |
| **NOAA SWPC Alerts** | Solar-storm alerts (CME, flare) | Event class, type, intensity | [SWPC Alerts](https://services.swpc.noaa.gov/json/alerts.json) |
| **Kyoto DST/AE** | Geomagnetic indices | Dst, AE, AL, AU, AO, AX | Kyoto World Data Center |

Data ingestion is handled through lightweight Python clients using `pyspedas` and direct API access.

### Data Processing

Merge and align datasets to hourly resolution:

```python
from src.processing import merge_all, align_to_hourly

# Merge all datasets
df_merged = merge_all([df_omni, df_kyoto, df_kp, df_goes])

# Align to hourly resolution
df_hourly = align_to_hourly(df_merged)
```

### Model Training

See the notebooks for complete examples:
- `storm_prediciton.ipynb` - Storm prediction using XGBoost, LightGBM, and Random Forest
- `evt_analysis.ipynb` - Extreme Value Theory analysis for tail risk

---

## 🔬 Methodology

### Feature Engineering

- **Lag Features:** Time-lagged variables (1-6 hour lags)
- **Derived Features:** Negative Bz, dynamic pressure, flare intensity
- **Temporal Features:** Hour, day of week, seasonal patterns

### Model Approaches

1. **Classification Models:**
   - Logistic Regression
   - Random Forest
   - XGBoost
   - LightGBM

2. **Extreme Value Theory:**
   - Generalized Pareto Distribution (GPD) for tail risk
   - Peak Over Threshold (POT) method

3. **Time Series Considerations:**
   - Temporal train/validation/test splits (60/20/20)
   - Proper handling of missing values to avoid data leakage
   - Interpolation applied after splitting

---

## 🔄 Development Status

⚠️ **This project is under active development.**

Current focus areas:
- Model refinement and hyperparameter tuning
- Feature engineering improvements
- EVT model validation
- Real-time prediction pipeline

---


