from utils.indicators import calculate_rsi, calculate_stochastic
from utils.data_utils import get_ohlc_data

def generate_analysis():
    df = get_ohlc_data(symbol="BTCUSDT", interval="1h", limit=100)
    if df is None:
        return "❌ Gagal ambil data harga dari Binance."

    rsi = calculate_rsi(df)
    k, d = calculate_stochastic(df)

    current_rsi = round(rsi.iloc[-1], 2)
    current_k = round(k.iloc[-1], 2)
    current_d = round(d.iloc[-1], 2)

    advice = "📊 AI John Analysis:\n"
    advice += f"• RSI(5): {current_rsi}\n"
    advice += f"• Stochastic %K: {current_k}, %D: {current_d}\n"

    if current_rsi < 30 and current_k < 20 and current_k > current_d:
        advice += "✅ Sinyal Beli Kuat Dikesan!"
    elif current_rsi > 70 and current_k > 80 and current_k < current_d:
        advice += "⚠️ Sinyal Jual Kuat Dikesan!"
    else:
        advice += "⏳ Masih Neutral / Tidak Sah."

    return advice
