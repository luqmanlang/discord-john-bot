from utils.data_utils import get_ohlc_data
from utils.indicators import calculate_rsi, calculate_stochastic

def counter_analysis():
    try:
        df = get_ohlc_data(symbol="BTCUSDT", interval="1h", limit=100)
        if df is None:
            return "❌ Gagal ambil data harga dari Binance."

        rsi = calculate_rsi(df)['close']
        k, d = calculate_stochastic(df)

        rsi_val = round(rsi.iloc[-1], 2)
        k_val = round(k.iloc[-1], 2)
        d_val = round(d.iloc[-1], 2)

        insight = "🤖 **AlphaAI Counter View**\n"
        insight += f"• RSI(5): {rsi_val}\n"
        insight += f"• Stochastic %K: {k_val}, %D: {d_val}\n"

        if rsi_val > 70:
            insight += "⚠️ RSI terlalu tinggi — potensi overbought.\n"
        elif rsi_val < 30:
            insight += "⚠️ RSI terlalu rendah — potensi oversold.\n"

        if k_val < d_val:
            insight += "📉
