
# utils/api_store.py

# Simpan semua URL API dan fungsi bina URL (boleh guna untuk cycle)
def get_api_sources(symbol="BTCUSDT", interval="1h", limit=100):
    return [
        {
            "name": "Binance",
            "url": f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
        },
        {
            "name": "CoinGecko",
            "url": f"https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=1&interval=hourly"
        }
        # Tambah lagi API jika perlu
    ]
