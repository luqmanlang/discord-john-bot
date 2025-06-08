import requests
import random

apis = [
    {"name": "CoinGecko", "url": "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"},
    {"name": "Binance", "url": "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1h&limit=20"}
]

def get_price_data():
    for api in apis:
        try:
            if api["name"] == "CoinGecko":
                res = requests.get(api["url"])
                price = res.json()["bitcoin"]["usd"]
                return {"price": price, "source": "CoinGecko", "closes": [price]*20}
            elif api["name"] == "Binance":
                res = requests.get(api["url"])
                data = res.json()
                closes = [float(item[4]) for item in data]
                return {"price": closes[-1], "source": "Binance", "closes": closes}
        except:
            continue
    return None
