import requests
import numpy as np

def fetch_binance(symbol="BTCUSDT", interval="1h", limit=100):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    try:
        data = requests.get(url).json()
        return [float(c[4]) for c in data]
    except:
        return []

def rsi(closes, period=14):
    if len(closes) < period: return None
    delta = np.diff(closes)
    up = delta[delta > 0].sum() / period
    down = -delta[delta < 0].sum() / period
    rs = up / down if down != 0 else 0
    return round(100 - (100 / (1 + rs)), 2)

def stochastic(closes, period=14):
    if len(closes) < period: return None, None
    low, high = min(closes[-period:]), max(closes[-period:])
    k = ((closes[-1] - low) / (high - low)) * 100 if high != low else 0
    d = sum([((closes[-i] - low) / (high - low)) * 100 for i in range(1, 4)]) / 3
    return round(k, 2), round(d, 2)

def get_full_analysis(interval):
    closes = fetch_binance(interval=interval)
    if not closes:
        return f"⚠️ Gagal ambil data {interval}"
    rsi_val = rsi(closes)
    k, d = stochastic(closes)
    rsi_msg = f"RSI {interval.upper()}: {rsi_val} 🚨" if rsi_val < 30 or rsi_val > 70 else f"RSI {interval.upper()}: {rsi_val}"
    stoch_msg = f"Stoch K/D: {k}/{d} 🔁" if k > d else f"Stoch K/D: {k}/{d}"
    return f"📊 [{interval.upper()}] {rsi_msg} | {stoch_msg}"
