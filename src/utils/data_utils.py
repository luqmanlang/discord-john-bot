import requests
import pandas as pd
from datetime import datetime

BINANCE_APIS = [
    "https://api.binance.com",
    "https://api1.binance.com",
    "https://api2.binance.com"
]

def get_ohlc_data(symbol="BTCUSDT", interval="1h", limit=100):
    for base_url in BINANCE_APIS:
        try:
            url = f"{base_url}/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
            response = requests.get(url, timeout=5)

            if response.status_code == 200:
                data = response.json()

                df = pd.DataFrame(data, columns=[
                    'timestamp', 'open', 'high', 'low', 'close', 'volume',
                    'close_time', 'quote_asset_volume', 'number_of_trades',
                    'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
                ])

                df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
                df.set_index('timestamp', inplace=True)

                df[['open', 'high', 'low', 'close', 'volume']] = df[['open', 'high', 'low', 'close', 'volume']].astype(float)
                return df

            else:
                print(f"❌ API gagal dari {base_url} — Status Code: {response.status_code}")

        except Exception as e:
            print(f"⚠️ Tidak dapat akses {base_url}: {str(e)}")

    print("❌ Semua endpoint Binance gagal. Data tidak berjaya diambil.")
    return None
