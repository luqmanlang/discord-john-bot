import pandas as pd

def calculate_rsi(df, period=5):
    delta = df['close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_stochastic(df, k_period=5, d_period=3, smooth_k=3):
    low_min = df['low'].rolling(window=k_period).min()
    high_max = df['high'].rolling(window=k_period).max()
    k = 100 * ((df['close'] - low_min) / (high_max - low_min))
    k_smooth = k.rolling(window=smooth_k).mean()
    d = k_smooth.rolling(window=d_period).mean()
    return k_smooth, d
