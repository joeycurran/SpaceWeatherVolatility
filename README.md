## ⚠️ Development of this project is on-going

# SpaceWeatherVolatility 🌌

**Predicting geomagnetic volatility using solar-wind and flare data**

This project models short-term geomagnetic storm probability and tail-risk using real-time NASA and NOAA data.  
It draws inspiration from quantitative-finance volatility forecasting, applying logistic, EVT, and GARCH-style models to understand how solar flares and solar-wind dynamics drive extreme Kp events.

---

## 🛰️ Overview

**Goal:** Estimate the conditional probability and tail-risk of geomagnetic storms (`Kp ≥ 5`) from upstream solar and flare variables.  

The pipeline integrates open satellite data (OMNI, GOES, SWPC), performs feature engineering, and fits statistical models for:
- Storm probability via logistic regression  
- Tail behaviour via **Extreme Value Theory (Generalised Pareto Distribution)**  
- Optional volatility dynamics via **GARCH(1,1)** or **Hawkes processes**

---
## 🔗 Data Sources

| Dataset | Description | Key Variables | Access |
|----------|--------------|---------------|---------|
| **NASA OMNIWeb** | Solar-wind & geomagnetic indices (1-min, hourly) | IMF Bz, V<sub>SW</sub>, density, AE, Kp, Dst, F10.7 | [OMNIWeb API](https://omniweb.gsfc.nasa.gov/ow_min.html) |
| **NOAA GOES XRS** | X-ray flux & flare events | Short/long flux, flare start/end/class | [SWPC GOES API](https://services.swpc.noaa.gov/json/goes/) |
| **NOAA SWPC Alerts** | Solar-storm alerts (CME, flare) | Event class, type, intensity | [SWPC Alerts](https://services.swpc.noaa.gov/json/alerts.json) |

Each API is wrapped in lightweight Python clients under `src/api/`.

---


