import numpy as np

def calculate_rsi(closes, period=5):
    deltas = np.diff(closes)
    seed = deltas[:period]
    up = seed[seed >= 0].sum() / period
    down = -seed[seed < 0].sum() / period
    rs = up / down if down != 0 else 0
    return 100. - 100. / (1. + rs)

def calculate_stochastic(closes, k=5):
    highest_high = max(closes[-k:])
    lowest_low = min(closes[-k:])
    return ((closes[-1] - lowest_low) / (highest_high - lowest_low)) * 100 if highest_high != lowest_low else 0
