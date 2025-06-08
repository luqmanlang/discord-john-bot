from utils.indicators import calculate_rsi_stochastic
from utils.discord_notifier import send_discord_alert

def run_analysis():
    message = f"📊 1H/4H Analysis:\n{calculate_rsi_stochastic()}"
    send_discord_alert(message)
