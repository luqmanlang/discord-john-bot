import requests
import numpy as np

def fetch_price_data():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {"vs_currency": "usd", "days": "2", "interval": "hourly"}
    response = requests.get(url)
    data = response.json()
    prices = [price[1] for price in data["prices"]]
    return prices

def calculate_rsi(data, period=5, smooth=3):
    deltas = np.diff(data)
    gain = np.where(deltas > 0, deltas, 0)
    loss = np.where(deltas < 0, -deltas, 0)

    avg_gain = np.convolve(gain, np.ones(smooth)/smooth, mode='valid')[-1]
    avg_loss = np.convolve(loss, np.ones(smooth)/smooth, mode='valid')[-1]
    rs = avg_gain / avg_loss if avg_loss != 0 else 0
    rsi = 100 - (100 / (1 + rs))
    return round(rsi, 2)

def calculate_stochastic(data, period=5):
    if len(data) < period:
        return None
    low_min = min(data[-period:])
    high_max = max(data[-period:])
    current = data[-1]
    if high_max - low_min == 0:
        return 0
    return round((current - low_min) / (high_max - low_min) * 100, 2)

def run_analysis():
    prices = fetch_price_data()
    rsi = calculate_rsi(prices)
    stoc = calculate_stochastic(prices)
    print(f"📊 1H/4H Analysis:
RSI(5,3,3): {rsi}
Stochastic(5): {stoc}")
