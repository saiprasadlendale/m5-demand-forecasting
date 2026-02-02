# 🏬 Demand Forecasting – Walmart Sales (M5-Style)

## Overview
End-to-end demand forecasting project using Walmart weekly sales data.
The project compares classical statistical models and modern forecasting
approaches with a focus on business impact.

## Dataset
- Weekly sales data from 45 Walmart stores
- Time range: 2010–2012
- Includes seasonal spikes and holiday effects

## Project Structure
- data/ → raw and processed datasets
- notebooks/ → EDA and model experimentation
- src/ → reusable preprocessing, evaluation, and visualization code
- results/ → saved forecasts and performance metrics

## Models Implemented
- SARIMA (statistical baseline model)
- Prophet (trend + seasonality + changepoints)

## Results
- SARIMA achieved ~1.6% MAPE on a 12-week holdout set
- Prophet handled demand spikes and trend changes more effectively
- Forecasts are stable and suitable for inventory planning

## Business Impact
- Better demand forecasting reduces overstocking and stock-outs
- Helps optimize inventory, staffing, and supply-chain planning

## Future Work
- Store-level (hierarchical) forecasting
- Rolling cross-validation
- LSTM-based deep learning forecasting
