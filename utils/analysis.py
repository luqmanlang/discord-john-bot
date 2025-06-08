from utils.discord_notifier import send_discord_alert

def run_analysis():
    message = "✅ Bot John telah aktif dan berjaya jalan fungsi `run_analysis()`"
    print("📨 Menghantar ke Discord:", message)
    send_discord_alert(message)
