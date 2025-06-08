john_ai.py

import requests from utils.indicators import calculate_rsi, calculate_stochastic from utils.data import get_price_data

def generate_john_report(): try: # Ambil data 1H dan 4H data_1h = get_price_data(interval="1h", limit=100) data_4h = get_price_data(interval="4h", limit=100)

# Kira RSI dan Stochastic
    rsi_1h = calculate_rsi(data_1h['close'], period=5)
    rsi_4h = calculate_rsi(data_4h['close'], period=5)

    stoch_1h_k, stoch_1h_d = calculate_stochastic(data_1h, k_period=5, d_period=3, slowing=3)
    stoch_4h_k, stoch_4h_d = calculate_stochastic(data_4h, k_period=5, d_period=3, slowing=3)

    current_price = data_1h['close'][-1]

    report = f"""
    **📊 Analisis Teknikal JohnAI**
    Harga Semasa: ${current_price:.2f}

    **1H RSI(5):** {rsi_1h[-1]:.2f}
    **4H RSI(5):** {rsi_4h[-1]:.2f}

    **1H Stochastic(5,3,3):** %K={stoch_1h_k[-1]:.2f}, %D={stoch_1h_d[-1]:.2f}
    **4H Stochastic(5,3,3):** %K={stoch_4h_k[-1]:.2f}, %D={stoch_4h_d[-1]:.2f}

    📌 RSI mula naik? {'Ya' if rsi_1h[-1] > rsi_1h[-2] else 'Belum'}
    📌 Stochastic crossover? {'Ya' if stoch_1h_k[-1] > stoch_1h_d[-1] else 'Belum'}
    """
    return report.strip()

except Exception as e:
    return f"❌ JohnAI gagal jana laporan: {str(e)}"

