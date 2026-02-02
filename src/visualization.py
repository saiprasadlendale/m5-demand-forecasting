import matplotlib.pyplot as plt


def plot_actual_vs_forecast(dates, actual, forecast, title):
    """
    Plot actual vs forecasted values.
    """
    plt.figure(figsize=(14, 5))
    plt.plot(dates, actual, label="Actual", linewidth=2)
    plt.plot(dates, forecast, label="Forecast", linewidth=2)
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Weekly Sales")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()
