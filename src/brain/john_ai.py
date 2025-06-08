from utils.indicators import calculate_rsi, calculate_stochastic
from utils.data_utils import get_ohlc_data

def generate_analysis():
    try:
        # Ambil data harga BTC
        data_1h = get_ohlc_data(symbol="BTCUSDT", interval="1h", limit=100)
        data_4h = get_ohlc_data(symbol="BTCUSDT", interval="4h", limit=100)

        if data_1h is None or data_4h is None:
            return "❌ JohnAI Gagal Jana Laporan: Data tidak berjaya diambil."

        closes_1h = data_1h['close'].tolist()
        closes_4h = data_4h['close'].tolist()

        if len(closes_1h) < 6 or len(closes_4h) < 6:
            return "❌ JohnAI Gagal Jana Laporan: Data terlalu pendek."

        rsi_1h = calculate_rsi(closes_1h, period=5)
        rsi_4h = calculate_rsi(closes_4h, period=5)

        stoch_1h_k, stoch_1h_d = calculate_stochastic(data_1h, k_period=5, d_period=3, smooth_k=3)
        stoch_4h_k, stoch_4h_d = calculate_stochastic(data_4h, k_period=5, d_period=3, smooth_k=3)

        current_price = closes_1h[-1]

        report = f"""
📊 **Analisis Teknikal JohnAI**
Harga Semasa: ${current_price:.2f}

🔹 **RSI(5)** 1H: {rsi_1h[-1]:.2f} | 4H: {rsi_4h[-1]:.2f}
🔹 **Stochastic(5,3,3)** 1H: %K = {stoch_1h_k[-1]:.2f}, %D = {stoch_1h_d[-1]:.2f}
                          4H: %K = {stoch_4h_k[-1]:.2f}, %D = {stoch_4h_d[-1]:.2f}

📈 RSI mula naik? {'✅ Ya' if rsi_1h[-1] > rsi_1h[-2] else '❌ Belum'}
📈 Stochastic crossover? {'✅ Ya' if stoch_1h_k[-1] > stoch_1h_d[-1] else '❌ Belum'}
        """

        return report.strip()

    except Exception as e:
        return f"❌ JohnAI Gagal Jana Laporan: {str(e)}"
