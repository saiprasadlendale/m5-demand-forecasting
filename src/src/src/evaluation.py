import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error


def mape(y_true, y_pred):
    """
    Mean Absolute Percentage Error
    """
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100


def evaluate_forecast(y_true, y_pred) -> dict:
    """
    Evaluate forecast using standard regression metrics.
    """
    return {
        "MAE": mean_absolute_error(y_true, y_pred),
        "RMSE": mean_squared_error(y_true, y_pred, squared=False),
        "MAPE": mape(y_true, y_pred)
    }
