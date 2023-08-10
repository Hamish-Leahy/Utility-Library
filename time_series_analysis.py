import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

def calculate_rolling_statistics(time_series, window=7):
    """
    Calculate rolling mean and rolling standard deviation of a time series.

    Args:
        time_series (pd.Series): Time series data.
        window (int, optional): Rolling window size. Defaults to 7.

    Returns:
        pd.DataFrame: DataFrame with rolling mean and rolling std columns.
    """
    rolling_mean = time_series.rolling(window=window).mean()
    rolling_std = time_series.rolling(window=window).std()
    rolling_statistics = pd.DataFrame({'Rolling Mean': rolling_mean, 'Rolling Std': rolling_std})
    return rolling_statistics

def perform_seasonal_decomposition(time_series, model='additive'):
    """
    Perform seasonal decomposition of a time series.

    Args:
        time_series (pd.Series): Time series data.
        model (str, optional): Type of decomposition ('additive' or 'multiplicative'). Defaults to 'additive'.

    Returns:
        statsmodels.tsa.seasonal.DecomposeResult: Result of seasonal decomposition.
    """
    decomposition = seasonal_decompose(time_series, model=model)
    return decomposition

def visualize_time_series(time_series, title=None, x_label='Date', y_label='Value', color='blue'):
    """
    Visualize a time series data.

    Args:
        time_series (pd.Series): Time series data.
        title (str, optional): Plot title. Defaults to None.
        x_label (str, optional): X-axis label. Defaults to 'Date'.
        y_label (str, optional): Y-axis label. Defaults to 'Value'.
        color (str, optional): Plot color. Defaults to 'blue'.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(time_series.index, time_series, color=color)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Sample time series data
    date_rng = pd.date_range(start='2023-01-01', periods=100, freq='D')
    values = np.sin(np.linspace(0, 4 * np.pi, num=100)) + np.random.normal(0, 0.2, 100)
    time_series = pd.Series(values, index=date_rng)

    # Calculate rolling statistics
    rolling_stats = calculate_rolling_statistics(time_series)

    # Perform seasonal decomposition
    decomposition = perform_seasonal_decomposition(time_series)

    # Visualize the original time series
    visualize_time_series(time_series, title='Original Time Series')

    # Visualize rolling statistics
    visualize_time_series(rolling_stats['Rolling Mean'], title='Rolling Mean', color='green')
    visualize_time_series(rolling_stats['Rolling Std'], title='Rolling Std', color='orange')

    # Visualize seasonal decomposition components
    visualize_time_series(decomposition.trend, title='Trend Component', color='blue')
    visualize_time_series(decomposition.seasonal, title='Seasonal Component', color='red')
    visualize_time_series(decomposition.resid, title='Residual Component', color='purple')
