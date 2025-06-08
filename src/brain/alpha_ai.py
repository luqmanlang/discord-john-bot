from utils.data_utils import get_holc_data
from utils.indicators import calculate_rsi

def counter_analysis():
    try:
        df = get_holc_data(symbol="BTCUSDT", interval="1h", limit=50)
        rsi = calculate_rsi(df)

        rsi_latest = round(rsi.iloc[-1], 2)
        rsi_prev = round(rsi.iloc[-2], 2)

        message = f"""
🤖 **AlphaAI Counter View**
• RSI(5): {rsi_latest} (Sebelumnya: {rsi_prev})
"""

        if rsi_latest > rsi_prev:
            message += "📈 RSI menunjukkan pemulihan kecil"
        elif rsi_latest < rsi_prev:
            message += "📉 RSI melemah, potensi retrace"
        else:
            message += "➖ RSI mendatar"

        return message
    except Exception as e:
        return f"❌ AlphaAI Gagal Jana Laporan: {str(e)}"
