
# utils/indicators_failsafe.py

import requests
import numpy as np
from utils.api_store import get_api_sources

def fetch_data(symbol="BTCUSDT", interval="1h", limit=100):
    sources = get_api_sources(symbol, interval, limit)
    for src in sources:
        try:
            print(f"[DEBUG] Cuba API: {src['name']}")
            response = requests.get(src["url"], timeout=10)
            response.raise_for_status()
            data = response.json()

            # Struktur berbeza untuk CoinGecko, proses berbeza
            if src["name"] == "CoinGecko":
                prices = [d[1] for d in data["prices"]][-limit:]
                return prices
            else:  # Binance
                return [float(c[4]) for c in data]
        except Exception as e:
            print(f"[DEBUG] Gagal API {src['name']}: {e}")
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
    d = sum([((closes[i] - low) / (high - low)) * 100 for i in range(-3, 0)]) / 3
    return round(k, 2), round(d, 2)

def get_full_analysis(interval="1h"):
    closes = fetch_data(interval=interval)
    if not closes:
        return f"⚠️ Gagal ambil data {interval}"

    rsi_val = rsi(closes)
    k, d = stochastic(closes)

    rsi_msg = f"RSI {interval.upper()}: {rsi_val} " + ("🔻" if rsi_val < 30 or rsi_val > 70 else "✅")
    stoch_msg = f"Stoch K/D: {k}/{d} " + ("📈" if k > d else "📉")

    return f"[{interval.upper()}] {rsi_msg} | {stoch_msg}"
