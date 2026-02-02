# 🏬 Demand Forecasting – Walmart Sales (M5-Style)

An end-to-end **time series demand forecasting** project using Walmart weekly sales data.
This project is inspired by the **M5 Forecasting competition** and focuses on building
**interpretable, production-style forecasting pipelines** rather than leaderboard optimization.

---

## 📌 Project Overview

Demand forecasting is a critical data science problem in **retail, supply chain, finance, and operations**.
In this project, historical Walmart sales data is used to forecast **weekly demand** and compare
classical and modern time-series models.

The emphasis is on:
- Clean project structure
- Reproducibility
- Business-oriented evaluation
- Clear comparison of models

---

## 🎯 Objectives

- Analyze trends, seasonality, and anomalies in sales data
- Build multiple forecasting models
- Compare model performance using meaningful metrics
- Present results in a professional, GitHub-ready format

---

## 🗂️ Project Structure

m5-demand-forecasting/
│
├── data/
│   ├── raw/
│   │   └── walmart-sales-dataset-of-45stores.csv
│   └── processed/
│       └── company_level_sales.csv
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_sarima_model.ipynb
│   ├── 04_prophet_model.ipynb
│   └── 05_model_comparison.ipynb
│
├── src/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── evaluation.py
│   └── visualization.py
│
├── results/
│   ├── metrics.csv
│   └── plots/
│       ├── sarima_forecast.png
│       └── prophet_forecast.png
│
├── requirements.txt
└── README.md

---

## 📂 Dataset Description

Source: Walmart Sales Dataset (45 stores)

Raw Data (data/raw/):
- Date – Weekly start date
- Weekly_Sales – Weekly sales per store
- Holiday_Flag – Indicates holiday weeks
- Store, Temperature, Fuel_Price, CPI, Unemployment

Processed Data (data/processed/):
- Aggregated to company-level weekly sales
- Cleaned and standardized date format
- Sorted time index for modeling
- Saved for reproducibility

---

## 🔍 Exploratory Data Analysis

Key insights from EDA:
- Strong weekly and yearly seasonality
- Significant holiday-driven demand spikes
- Higher volatility during peak seasons
- Presence of anomalies affecting forecast accuracy

---

## 🤖 Models Implemented

SARIMA (Seasonal ARIMA):
- Classical statistical time-series model
- Explicit modeling of trend and seasonality
- Used as a stable baseline forecast

Prophet (Meta):
- Modern forecasting framework
- Automatic seasonality and changepoint detection
- More robust to demand spikes and trend shifts

---

## 📈 Model Evaluation

Evaluation metrics:
- MAE – Mean Absolute Error
- RMSE – Root Mean Squared Error
- MAPE – Mean Absolute Percentage Error

Metrics are stored in:
results/metrics.csv

Results Summary (12-week holdout):

| Model   | MAE   | RMSE  | MAPE |
|--------|-------|-------|------|
| SARIMA | ~760K | ~890K | ~1.6% |
| Prophet | See metrics.csv | | |

---

## 📊 Visual Results

- SARIMA Forecast vs Actual:
  Captures overall trend and seasonality, smoothing sharp holiday spikes.

- Prophet Forecast:
  Adapts to trend changes and seasonal surges, with uncertainty intervals.

Plots are available in:
results/plots/

---

## 💼 Business Impact

Accurate demand forecasting helps:
- Reduce stock-outs and over-inventory
- Improve inventory planning
- Optimize staffing and logistics
- Detect abnormal demand patterns early

---

## 🛠️ How to Run the Project

Google Colab (Recommended):
1. Upload the repository to Colab
2. Place raw data in data/raw/
3. Run notebooks in order: 01 → 05

Local Setup:
pip install -r requirements.txt
Open notebooks using Jupyter or VS Code.

---

## 🚀 Production Considerations

In a real production system:
- Retrain models weekly or monthly
- Monitor forecast errors and trigger alerts
- Add external regressors (holidays, promotions)
- Extend to store-level hierarchical forecasting

---

## 📌 Key Takeaways

- Built a complete end-to-end demand forecasting pipeline
- Compared classical and modern time-series models
- Focused on interpretability and business relevance
- Followed clean, professional GitHub project structure

---

## 🔮 Future Improvements

- Hierarchical forecasting (store → region → company)
- Feature-based ML models (XGBoost / LightGBM)
- Deep learning models (LSTM / TFT)
- Rolling cross-validation
- Forecast monitoring dashboards

---

## 👤 Author

Saiprasad Lendale  
Aspiring Data Scientist | Time Series & Demand Forecasting

If you find this project useful, feel free to star the repository.
