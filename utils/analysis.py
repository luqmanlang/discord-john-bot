import requests
import numpy as np
import os
from utils.discord_notifier import send_discord_alert

def fetch_price_data():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {"vs_currency": "usd", "days": "2", "interval": "hourly"}
    response = requests.get(url, params=params)
    data = response.json()
    prices = [price[1] for price in data.get("prices", [])[-24:]]
    return prices

def calculate_rsi(prices, period=5, smooth=3):
    delta = np.diff(prices)
    up = np.maximum(delta, 0)
    down = np.abs(np.minimum(delta, 0))
    ma_up = np.convolve(up, np.ones(period)/period, mode='valid')
    ma_down = np.convolve(down, np.ones(period)/period, mode='valid')
    rs = ma_up / (ma_down + 1e-6)
    rsi = 100 - (100 / (1 + rs))
    rsi_smooth = np.convolve(rsi, np.ones(smooth)/smooth, mode='valid')
    return round(rsi_smooth[-1], 2) if len(rsi_smooth) else None

def calculate_stochastic(prices, period=5):
    if len(prices) < period:
        return None
    low_min = min(prices[-period:])
    high_max = max(prices[-period:])
    current_close = prices[-1]
    stoch = ((current_close - low_min) / (high_max - low_min + 1e-6)) * 100
    return round(stoch, 2)

def run_analysis():
    prices = fetch_price_data()
    rsi = calculate_rsi(prices)
    stoch = calculate_stochastic(prices)
    message = f"📊 1H/4H Analysis
Price: ${prices[-1]:,.2f}
RSI (5,3,3): {rsi}
Stochastic (5): {stoch}"
    send_discord_alert(message)
