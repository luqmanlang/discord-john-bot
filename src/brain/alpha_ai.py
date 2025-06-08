from utils.data_utils import get_ohlc_data
from utils.indicators import calculate_rsi, calculate_stochastic

def counter_analysis():
    data = get_price_data("bitcoin", interval="1h", limit=100)

    if not data:
        return "❌ Gagal ambil data dari Binance."

    closes = [c['close'] for c in data]
    rsi_list = calculate_rsi(closes, period=5)
    stoch_k, stoch_d = calculate_stochastic(data, k_period=5, d_period=3, smooth_k=3)

    # Ambil nilai terakhir yang sah
    rsi_val = round(rsi_list[-1], 2) if rsi_list[-1] else 0
    k_val = round(stoch_k[-1], 2) if stoch_k[-1] else 0
    d_val = round(stoch_d[-1], 2) if stoch_d[-1] else 0

    insight = "🧠 **AlphaAI Counter View**\n"
    insight += f"• RSI(5): {rsi_val}\n"
    insight += f"• Stochastic %K: {k_val}, %D: {d_val}\n"

    if rsi_val > 70:
        insight += "⚠️ RSI terlalu tinggi — potensi overbought.\n"
    elif rsi_val < 30:
        insight += "⚠️ RSI terlalu rendah — potensi oversold.\n"

    if k_val < d_val:
        insight += "📉 %K masih di bawah %D — belum ada crossover naik.\n"
    elif k_val > 80:
        insight += "🚨 %K terlalu tinggi — risiko reversal meningkat.\n"
    else:
        insight += "✅ %K masih tenang."

    return insight
