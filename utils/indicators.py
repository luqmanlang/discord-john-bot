
import random

def get_indicators():
    rsi = round(random.uniform(30, 70), 2)
    stochastic = round(random.uniform(20, 80), 2)
    return rsi, stochastic
