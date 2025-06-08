
import requests
import numpy as np

def fetch_price_data():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {"vs_currency": "usd", "days": "2", "interval": "hourly"}
    response = requests.get(url, params=params)
    data = response.json()
    prices = [price[1] for price in data["prices"]]
    return prices

def calculate_rsi(data, period=5):
    deltas = np.diff(data)
    seed = deltas[:period+1]
    up = seed[seed >= 0].sum()/period
    down = -seed[seed < 0].sum()/period
    rs = up / down if down != 0 else 0
    rsi = np.zeros_like(data)
    rsi[:period] = 100. - 100. / (1. + rs)

    for i in range(period, len(data)):
        delta = deltas[i - 1]
        gain = max(delta, 0)
        loss = -min(delta, 0)
        up = (up * (period - 1) + gain) / period
        down = (down * (period - 1) + loss) / period
        rs = up / down if down != 0 else 0
        rsi[i] = 100. - 100. / (1. + rs)
    return rsi

def calculate_stochastic(data, k_period=5, d_period=3):
    stoch_k = []
    for i in range(k_period, len(data)):
        low = min(data[i-k_period:i])
        high = max(data[i-k_period:i])
        if high - low == 0:
            stoch_k.append(0)
        else:
            stoch_k.append((data[i] - low) / (high - low) * 100)
    stoch_d = np.convolve(stoch_k, np.ones(d_period)/d_period, mode='valid')
    return stoch_k[-1], stoch_d[-1]

def run_analysis(timeframe):
    prices = fetch_price_data()
    rsi = calculate_rsi(prices)[-1]
    k, d = calculate_stochastic(prices)
    message = f"📊 1H/4H Analysis:
RSI: {rsi:.2f}
Stochastic K: {k:.2f}, D: {d:.2f}"
    print(message)
