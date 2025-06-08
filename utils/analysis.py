
import requests
import numpy as np

def fetch_price_data():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {"vs_currency": "usd", "days": "1", "interval": "hourly"}
    response = requests.get(url, params=params)
    data = response.json()
    prices = [price[1] for price in data["prices"][-24:]]
    return prices

def calculate_rsi(prices, period=5):
    deltas = np.diff(prices)
    seed = deltas[:period]
    up = seed[seed > 0].sum() / period
    down = -seed[seed < 0].sum() / period
    rs = up / down if down != 0 else 0
    rsi = 100. - 100. / (1. + rs)
    return round(rsi, 2)

def calculate_stochastic(prices, k_period=5, d_period=3):
    close = prices[-1]
    lowest_low = min(prices[-k_period:])
    highest_high = max(prices[-k_period:])
    k = ((close - lowest_low) / (highest_high - lowest_low)) * 100 if highest_high != lowest_low else 0
    d = k  # simplifikasi, tak guna average penuh
    return round(k, 2), round(d, 2)

def run_analysis():
    prices = fetch_price_data()
    rsi = calculate_rsi(prices)
    k, d = calculate_stochastic(prices)
    message = f"📈 1H/4H Analysis:\nPrice: ${prices[-1]:,.2f}\nRSI(5): {rsi}\nStochastic(5,3,3): %K={k} %D={d}"
    print(message)
