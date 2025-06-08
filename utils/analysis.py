import requests
import pandas as pd

def fetch_price_data(symbol="bitcoin", currency="usd", interval="hourly", limit=100):
    url = f"https://api.coingecko.com/api/v3/coins/{symbol}/market_chart"
    params = {
        "vs_currency": currency,
        "days": "7",
        "interval": interval
    }
    response = requests.get(url, params=params)
    data = response.json()
    prices = [price[1] for price in data["prices"][-limit:]]
    return pd.Series(prices)

def calculate_rsi(series, period=14):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_stochastic(series, k_period=14, d_period=3):
    low_min = series.rolling(window=k_period).min()
    high_max = series.rolling(window=k_period).max()
    stoch_k = 100 * ((series - low_min) / (high_max - low_min))
    stoch_d = stoch_k.rolling(window=d_period).mean()
    return stoch_k, stoch_d

def get_indicators():
    prices = fetch_price_data()
    rsi = calculate_rsi(prices).iloc[-1]
    stoch_k, stoch_d = calculate_stochastic(prices)
    return {
        "rsi": round(rsi, 2),
        "stoch_k": round(stoch_k.iloc[-1], 2),
        "stoch_d": round(stoch_d.iloc[-1], 2)
    }
