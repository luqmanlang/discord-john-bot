import requests
import numpy as np

# Fungsi untuk ambil data dari Binance (price history)
def fetch_binance(symbol="BTCUSDT", interval="1h", limit=100):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    try:
        data = requests.get(url).json()
        return [float(c[4]) for c in data]  # Close price
    except Exception as e:
        print(f"Error fetching Binance data: {e}")
        return []

# Fungsi RSI
def rsi(closes, period=14):
    if len(closes) < period:
        return None
    delta = np.diff(closes)
    gain = delta[delta > 0].sum() / period
    loss = -delta[delta < 0].sum() / period
    rs = gain / loss if loss != 0 else 0
    return round(100 - (100 / (1 + rs)), 2)

# Fungsi Stochastic
def stochastic(closes, period=14):
    if len(closes) < period:
        return None, None
    low = min(closes[-period:])
    high = max(closes[-period:])
    current = closes[-1]
    k = ((current - low) / (high - low)) * 100 if high != low else 0
    d = np.mean([((closes[i] - min(closes[i - period + 1:i + 1])) / 
                  (max(closes[i - period + 1:i + 1]) - min(closes[i - period + 1:i + 1])) * 100
                  if max(closes[i - period + 1:i + 1]) != min(closes[i - period + 1:i + 1]) else 0)
                 for i in range(len(closes) - period + 1, len(closes))])
    return round(k, 2), round(d, 2)

# Fungsi utama untuk analisis penuh
def get_full_analysis(interval="1h"):
    closes = fetch_binance(interval=interval)
    if not closes:
        return f"⚠️ Gagal ambil data {interval}"
    rsi_val = rsi(closes)
    k, d = stochastic(closes)
    rsi_msg = f"RSI ({interval.upper()}): {rsi_val} " + ("🚨" if rsi_val is not None and (rsi_val < 30 or rsi_val > 70) else "✅")
    stoch_msg = f"Stoch K/D: {k}/{d} " + ("⚠️" if k is not None and d is not None and k > d else "✅")
    return f"[{interval.upper()}] {rsi_msg} | {stoch_msg}"
