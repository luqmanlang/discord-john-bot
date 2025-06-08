from utils.indicators import calculate_rsi, calculate_stochastic
from utils.data_utils import get_ohlc_data

def generate_john_report():
    try:
        data_1h = get_ohlc_data(symbol="BTCUSDT", interval="1h", limit=100)
        data_4h = get_ohlc_data(symbol="BTCUSDT", interval="4h", limit=100)

        if data_1h is None or data_4h is None:
            return "❌ JohnAI: Gagal ambil data 1H atau 4H"

        closes_1h = data_1h['close']
        closes_4h = data_4h['close']

        rsi_1h = calculate_rsi(data_1h)['close']
        rsi_4h = calculate_rsi(data_4h)['close']

        stoch_1h_k, stoch_1h_d = calculate_stochastic(data_1h)
        stoch_4h_k, stoch_4h_d = calculate_stochastic(data_4h)

        current_price = closes_1h.iloc[-1]

        report = f"""
📊 **Analisis Teknikal JohnAI**
Harga Semasa: ${current_price:.2f}

**1H RSI(5):** {rsi_1h.iloc[-1]:.2f}
**4H RSI(5):** {rsi_4h.iloc[-1]:.2f}

**1H Stochastic(5,3,3):** %K={stoch_1h_k.iloc[-1]:.2f}, %D={stoch_1h_d.iloc[-1]:.2f}
**4H Stochastic(5,3,3):** %K={stoch_4h_k.iloc[-1]:.2f}, %D={stoch_4h_d.iloc[-1]:.2f}

📌 RSI mula naik? {'✅ Ya' if rsi_1h.iloc[-1] > rsi_1h.iloc[-2] else '❌ Belum'}
📌 Stochastic crossover? {'✅ Ya' if stoch_1h_k.iloc[-1] > stoch_1h_d.iloc[-1] else '❌ Belum'}
"""
        return report.strip()

    except Exception as e:
        return f"❌ JohnAI gagal jana laporan: {str(e)}"
