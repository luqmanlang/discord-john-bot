def calculate_rsi(closes, period=5):
    deltas = [closes[i] - closes[i - 1] for i in range(1, len(closes))]
    gains = [max(delta, 0) for delta in deltas]
    losses = [-min(delta, 0) for delta in deltas]

    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period

    rsi_values = []

    for i in range(period, len(closes) - 1):
        gain = gains[i - 1]
        loss = losses[i - 1]

        avg_gain = ((avg_gain * (period - 1)) + gain) / period
        avg_loss = ((avg_loss * (period - 1)) + loss) / period

        if avg_loss == 0:
            rsi = 100
        else:
            rs = avg_gain / avg_loss
            rsi = 100 - (100 / (1 + rs))

        rsi_values.append(rsi)

    # Untuk samakan panjang dengan input
    padding = [None] * (len(closes) - len(rsi_values))
    return padding + rsi_values


def calculate_stochastic(data, k_period=5, d_period=3, smooth_k=3):
    close = [c['close'] for c in data]
    low = [c['low'] for c in data]
    high = [c['high'] for c in data]

    k_values = []

    for i in range(len(close)):
        if i < k_period - 1:
            k_values.append(None)
            continue
        low_min = min(low[i - k_period + 1:i + 1])
        high_max = max(high[i - k_period + 1:i + 1])
        k = 100 * (close[i] - low_min) / (high_max - low_min) if (high_max - low_min) != 0 else 0
        k_values.append(k)

    # Smooth %K
    smoothed_k = []
    for i in range(len(k_values)):
        if i < smooth_k - 1 or k_values[i] is None:
            smoothed_k.append(None)
            continue
        smoothed = sum(k_values[i - smooth_k + 1:i + 1]) / smooth_k
        smoothed_k.append(smoothed)

    # Calculate %D
    d_values = []
    for i in range(len(smoothed_k)):
        if i < d_period - 1 or smoothed_k[i] is None:
            d_values.append(None)
            continue
        d = sum(smoothed_k[i - d_period + 1:i + 1]) / d_period
        d_values.append(d)

    return smoothed_k, d_values
