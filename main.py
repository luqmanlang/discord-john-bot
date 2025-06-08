import time
import schedule
from utils.api_cycle import get_price_data
from utils.indicators import calculate_rsi, calculate_stochastic
from discord_notifier import send_discord_message

def run_analysis():
    data = get_price_data()
    if not data:
        return

    price = data['price']
    source = data['source']
    closes = data['closes']

    rsi = calculate_rsi(closes)
    stochastic = calculate_stochastic(closes)

    message = f"""
📈 **Auto Alert 1H/4H**
Harga: ${price}
RSI(5): {rsi:.2f}
Stochastic(5,3,3): {stochastic:.2f}
Data by: {source}
"""
    send_discord_message(message)

schedule.every().hour.do(run_analysis)
schedule.every(4).hours.do(run_analysis)

print("Bot bermula... Menunggu alert...")
while True:
    schedule.run_pending()
    time.sleep(1)
