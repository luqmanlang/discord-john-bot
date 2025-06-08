
import requests

def get_price():
    try:
        data = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd').json()
        return data['bitcoin']['usd'], "CoinGecko"
    except:
        data = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT').json()
        return float(data['price']), "Binance"
