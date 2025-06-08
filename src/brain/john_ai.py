from utils.data_utils import get_ohlc_data
from utils.indicators import calculate_rsi, calculate_stochastic

def generate_analysis():
    data = get_price_data(symbol="BTCUSDT", interval="1h", limit=100)

    if not data:
        return "❌ Gagal ambil data harga dari Binance."

    closes = [candle['close'] for candle in data]
    rsi_list = calculate_rsi(closes, period=5)
    stoch_k, stoch_d = calculate_stochastic(data, k_period=5, d_period=3, smooth_k=3)

    current_rsi = round(rsi_list[-1], 2)
    current_k = round(stoch_k[-1], 2)
    current_d = round(stoch_d[-1], 2)

    advice = "🤖 **AI John Analysis**\n"
    advice += f"• RSI(5): {current_rsi}\n"
    advice += f"• Stochastic %K: {current_k}, %D: {current_d}\n"

    if current_rsi < 30 and current_k < 20 and current_k > current_d:
        advice += "✅ Sinyal Beli Kuat Dikesan!"
    elif current_rsi > 70 and current_k > 80 and current_k < current_d:
        advice += "⚠️ Sinyal Jual Kuat Dikesan!"
    else:
        advice += "⏳ Masih Neutral / Tidak Sah."

    return advice
