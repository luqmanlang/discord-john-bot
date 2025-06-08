
from discord_bot import send_alert
from utils.api_cycle import get_price
from utils.indicators import get_indicators
import time

def run_alert():
    price, source = get_price()
    rsi, stochastic = get_indicators()
    send_alert(price, rsi, stochastic, source)

if __name__ == "__main__":
    while True:
        run_alert()
        time.sleep(3600)  # Setiap 1 jam
