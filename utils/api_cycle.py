import requests

def fetch_price_data():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {"vs_currency": "usd", "days": 1, "interval": "hourly"}
    try:
        response = requests.get(url, params=params)
        data = response.json()
        prices = [point[1] for point in data["prices"]]
        return prices
    except Exception as e:
        print(f"Error API: {e}")
        return []