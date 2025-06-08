import numpy as np
from utils.discord_notifier import send_alert
from utils.api_cycle import fetch_price_data

def calculate_rsi(prices, period=5, smooth=3):
    deltas = np.diff(prices)
    seed = deltas[:period]
    up = seed[seed > 0].sum() / period
    down = -seed[seed < 0].sum() / period
    rs = up / down if down != 0 else 0
    rsi = np.zeros_like(prices)
    rsi[:period] = 100. - 100. / (1. + rs)

    for i in range(period, len(prices)):
        delta = deltas[i - 1]
        upval = max(delta, 0)
        downval = -min(delta, 0)
        up = (up * (smooth - 1) + upval) / smooth
        down = (down * (smooth - 1) + downval) / smooth
        rs = up / down if down != 0 else 0
        rsi[i] = 100. - 100. / (1. + rs)

    return rsi

def calculate_stochastic(prices, k_period=5, d_period=3):
    k_values = []
    for i in range(len(prices)):
        if i < k_period:
            k_values.append(0)
            continue
        low_min = min(prices[i - k_period:i])
        high_max = max(prices[i - k_period:i])
        k = 100 * ((prices[i] - low_min) / (high_max - low_min)) if high_max != low_min else 0
        k_values.append(k)
    d_values = np.convolve(k_values, np.ones(d_period) / d_period, mode='same')
    return k_values, d_values

def run_analysis():
    price_data = fetch_price_data()
    if not price_data or len(price_data) < 10:
        return

    rsi = calculate_rsi(price_data)
    k, d = calculate_stochastic(price_data)

    current_price = price_data[-1]
    rsi_value = round(rsi[-1], 2)
    k_value = round(k[-1], 2)
    d_value = round(d[-1], 2)

    message = f"📊 1H/4H Analysis:
Price: ${current_price}
RSI(5,3,3): {rsi_value}
Stochastic(5): K={k_value}, D={d_value}"
    send_alert(message)