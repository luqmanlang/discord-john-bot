import requests

def get_full_analysis(symbol='bitcoin'):
    url = f"https://api.coingecko.com/api/v3/coins/{symbol}?localization=false&tickers=false&market_data=true&community_data=false&developer_data=false&sparkline=false"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Gagal ambil data dari CoinGecko."}

    data = response.json()
    market_data = data.get("market_data", {})

    return {
        "price_usd": market_data.get("current_price", {}).get("usd"),
        "rsi_status": "🔻 RSI oversold (simulasi)" if market_data.get("price_change_percentage_24h", 0) < -2 else "🔺 RSI neutral (simulasi)",
        "stochastic_status": "🔼 Stochastic bullish crossover (simulasi)",
        "trend": "📈 Trend jangka pendek bullish (simulasi)",
        "support": f"${market_data.get('low_24h', {}).get('usd')}",
        "resistance": f"${market_data.get('high_24h', {}).get('usd')}"
    }
