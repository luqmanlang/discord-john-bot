from utils.indicators import calculate_rsi, calculate_stochastic
from utils.data_utils import get_ohlc_data

def generate_john_report():
    try:
        # Ambil data harga (pastikan cukup panjang)
        data_1h = get_price_data(symbol="bitcoin", interval="1h", limit=100)
        data_4h = get_price_data(symbol="bitcoin", interval="4h", limit=100)

        if data_1h is None or data_4h is None:
            return "❌ JohnAI: Gagal ambil data 1H atau 4H"

        closes_1h = [c['close'] for c in data_1h]
        closes_4h = [c['close'] for c in data_4h]

        if len(closes_1h) < 6 or len(closes_4h) < 6:
            return "❌ JohnAI: Data harga tidak mencukupi untuk analisis"

        rsi_1h = calculate_rsi(closes_1h, period=5)
        rsi_4h = calculate_rsi(closes_4h, period=5)

        stoch_1h_k, stoch_1h_d = calculate_stochastic(data_1h, k_period=5, d_period=3, smooth_k=3)
        stoch_4h_k, stoch_4h_d = calculate_stochastic(data_4h, k_period=5, d_period=3, smooth_k=3)

        current_price = closes_1h[-1]

        report = f"""
📊 **Analisis Teknikal JohnAI**
💰 Harga Semasa: ${current_price:.2f}

🕐 **1H RSI(5):** {rsi_1h[-1]:.2f}
⏰ **4H RSI(5):** {rsi_4h[-1]:.2f}

📈 **1H Stochastic(5,3,3):** %K={stoch_1h_k[-1]:.2f}, %D={stoch_1h_d[-1]:.2f}
📉 **4H Stochastic(5,3,3):** %K={stoch_4h_k[-1]:.2f}, %D={stoch_4h_d[-1]:.2f}

📌 RSI mula naik? {'✅ Ya' if rsi_1h[-1] > rsi_1h[-2] else '❌ Belum'}
📌 Stochastic crossover? {'✅ Ya' if stoch_1h_k[-1] > stoch_1h_d[-1] else '❌ Belum'}
"""
        return report.strip()

    except Exception as e:
        return f"❌ JohnAI gagal jana laporan: {str(e)}"
