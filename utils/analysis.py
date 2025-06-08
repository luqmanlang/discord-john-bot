import requests
import numpy as np
from utils.discord_notifier import send_alert

def fetch_price_data():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=2&interval=hourly"
    response = requests.get(url)
    data = response.json()
    prices = [price[1] for price in data.get("prices", [])]
    return prices

def calculate_rsi(prices, period=14):
    if len(prices) < period + 1:
        return None
    deltas = np.diff(prices)
    seed = deltas[:period]
    up = seed[seed >= 0].sum() / period
    down = -seed[seed < 0].sum() / period
    rs = up / down if down != 0 else 0
    rsi = 100 - (100 / (1 + rs))
    return round(rsi, 2)

def calculate_stochastic(prices, period=14):
    if len(prices) < period:
        return None
    low = min(prices[-period:])
    high = max(prices[-period:])
    current = prices[-1]
    stochastic = (current - low) / (high - low) * 100 if high != low else 0
    return round(stochastic, 2)

def run_analysis():
    prices = fetch_price_data()
    rsi = calculate_rsi(prices)
    stochastic = calculate_stochastic(prices)
    message = f"📊 1H/4H Analysis
Price: ${prices[-1]:,.2f}\nRSI: {rsi}\nStochastic: {stochastic}"
    send_alert(message)