import requests
from datetime import datetime

def get_price_data(symbol="bitcoin", interval="1h", limit=100):
    symbol = "BTCUSDT"  # Untuk Binance, override symbol
    url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}'
    response = requests.get(url)

    if response.status_code != 200:
        return None

    raw_data = response.json()
    result = []

    for candle in raw_data:
        result.append({
            "timestamp": datetime.fromtimestamp(candle[0] / 1000),
            "open": float(candle[1]),
            "high": float(candle[2]),
            "low": float(candle[3]),
            "close": float(candle[4]),
            "volume": float(candle[5])
        })

    return result
