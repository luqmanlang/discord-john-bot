from utils.analysis import get_indicators
from utils.discord_notifier import send_to_discord
import time

def main():
    indicators = get_indicators()
    message = f"🔔 RSI: {indicators['rsi']}, %K: {indicators['stoch_k']}, %D: {indicators['stoch_d']}"
    send_to_discord(message)

if __name__ == "__main__":
    main()
