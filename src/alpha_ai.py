alpha_ai.py

from utils.data import get_price_data from utils.indicators import calculate_rsi, calculate_stochastic

def alpha_analysis(): analysis = [] for tf in ["1h", "4h"]: data = get_price_data("bitcoin", tf) if not data: analysis.append(f"❌ Gagal ambil data untuk {tf}") continue

closes = [candle['close'] for candle in data]
    rsi = calculate_rsi(closes, period=5)
    stoch_k, stoch_d = calculate_stochastic(data, k_period=5, d_period=3, smooth_k=3)

    signal = "❓ Neutral"
    if rsi < 30 and stoch_k < 20 and stoch_k > stoch_d:
        signal = "⚠️ Berpotensi Rebound (Oversold)"
    elif rsi > 70 and stoch_k > 80 and stoch_k < stoch_d:
        signal = "🚨 Awas! Berpotensi Jatuh (Overbought)"

    analysis.append(
        f"⏱ Timeframe: {tf.upper()}\n"
        f"📊 RSI(5): {rsi:.2f}\n"
        f"📈 Stoch %K: {stoch_k:.2f} | %D: {stoch_d:.2f}\n"
        f"🔎 Pandangan Alpha: {signal}\n"
    )
return "\n".join(analysis)

if name == "main": print(alpha_analysis())

