# 📊 Demand Forecasting – Walmart Sales (M5-Style)

End-to-end **time series demand forecasting** project using Walmart sales data, inspired by the **M5 Forecasting competition**.  
The goal is to build, evaluate, and compare multiple forecasting models while following **production-ready project structure**.

---

## 📌 Project Overview

Demand forecasting is a core data science skill used across **retail, supply chain, finance, and operations**.  
In this project, we forecast **weekly sales** using historical Walmart data and compare classical and modern time-series models.

### Key Objectives
- Understand sales trends, seasonality, and anomalies  
- Build multiple forecasting models  
- Compare model performance using business-relevant metrics  
- Present results in a clean, reproducible GitHub structure  

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
│   ├── preprocessing.py
│   ├── evaluation.py
│   └── visualization.py
│
├── results/
│   ├── plots/
│   │   ├── sarima_forecast_vs_actual.png
│   │   └── prophet_forecast.png
│   └── metrics.csv
│
├── requirements.txt
└── README.md

---

## 📂 Dataset Description

**Source:** Walmart Sales Dataset (45 stores)

### Raw Data (`data/raw/`)
Key columns:
- Date – Weekly start date  
- Weekly_Sales – Sales per store per week  
- Holiday_Flag – Indicates holiday weeks  
- Store, Temperature, Fuel_Price, CPI, Unemployment

### Processed Data (`data/processed/`)
- Aggregated to **company-level weekly sales**
- Cleaned and standardized date format
- Ready for time-series modeling

---

## 🔍 Exploratory Data Analysis

Key observations:
- Clear **weekly and yearly seasonality**
- Strong **holiday-driven spikes**
- Sales volatility increases during peak seasons
- Presence of anomalies that impact forecasting accuracy

---

## 🤖 Models Implemented

### 1️⃣ SARIMA (Seasonal ARIMA)
- Classical statistical forecasting model
- Explicitly models trend, seasonality, and autocorrelation
- Strong baseline for structured time-series data

### 2️⃣ Prophet (Meta)
- Modern forecasting framework
- Handles multiple seasonalities and changepoints automatically
- More robust to missing data and trend shifts

---

## 📈 Model Evaluation

Metrics used:
- MAE – Mean Absolute Error  
- RMSE – Root Mean Squared Error  
- MAPE – Mean Absolute Percentage Error  

Results stored in `results/metrics.csv`

| Model   | MAE   | RMSE  | MAPE |
|--------|-------|-------|------|
| SARIMA | ~760K | ~890K | ~1.6% |
| Prophet | See metrics.csv | | |

---

## 📊 Visual Results

- SARIMA Forecast vs Actual – Captures trend and seasonality with minor lag during holiday spikes  
- Prophet Forecast – Better handling of changepoints with uncertainty intervals  

(Plots available in `results/plots/`)

---

## 💼 Business Impact

Accurate demand forecasting enables:
- Improved inventory planning
- Reduced stockouts and overstock
- Better staffing and logistics decisions
- Early detection of abnormal demand patterns

---

## 🛠️ How to Run This Project

### Google Colab (Recommended)
1. Upload the repository to Colab
2. Place raw data in `data/raw/`
3. Run notebooks in order (01 → 05)

### Local Setup
pip install -r requirements.txt  
Open notebooks using Jupyter or VS Code.

---

## 🚀 Production Considerations

If deployed in production:
- Retrain models weekly or monthly
- Monitor forecast error with alert thresholds
- Add external regressors (holidays, promotions)
- Extend to hierarchical forecasting (store → region → company)

---

## 📌 Key Takeaways

- Built a full end-to-end forecasting pipeline
- Compared classical and modern forecasting approaches
- Focused on interpretability and business relevance
- Followed clean, professional GitHub project structure

---

## 🔮 Future Improvements
- Store-level and hierarchical forecasting
- Deep learning models (LSTM / TFT)
- Rolling cross-validation
- Automated monitoring dashboards

---

## 👤 Author

**Saiprasad Lendale**  
Aspiring Data Scientist | Time Series & Forecasting  

⭐ If you find this project useful, feel free to star the repository!
