from utils.data_utils import get_holc_data
from utils.indicators import calculate_rsi, calculate_stochastic

def generate_analysis():
    try:
        df = get_holc_data(symbol="BTCUSDT", interval="1h", limit=100)
        rsi = calculate_rsi(df)
        k, d = calculate_stochastic(df)

        current_rsi = round(rsi.iloc[-1], 2)
        current_k = round(k.iloc[-1], 2)
        current_d = round(d.iloc[-1], 2)

        advice = f"""
📊 **JohnAI Report**
• RSI(5): {current_rsi}
• Stochastic %K: {current_k}, %D: {current_d}
"""

        if current_rsi < 30 and current_k < 20 and current_k > current_d:
            advice += "✅ Sinyal Beli Dikesan"
        elif current_rsi > 70 and current_k > 80 and current_k < current_d:
            advice += "⚠️ Sinyal Jual Dikesan"
        else:
            advice += "⏳ Tiada Sinyal Jelas"

        return advice
    except Exception as e:
        return f"❌ JohnAI Gagal Jana Laporan: {str(e)}"
