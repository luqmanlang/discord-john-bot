from utils.data_utils import get_ohlc_data
from utils.indicators import calculate_rsi, calculate_stochastic

def counter_analysis():
    df = get_ohlc_data(symbol="BTCUSDT", interval="1h", limit=100)
    rsi = calculate_rsi(df)
    k, d = calculate_stochastic(df)

    rsi_val = round(rsi.iloc[-1], 2)
    k_val = round(k.iloc[-1], 2)
    d_val = round(d.iloc[-1], 2)

    insight = "🤖 AlphaAI Counter View:\n"
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
