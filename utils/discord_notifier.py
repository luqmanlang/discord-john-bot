import os
import requests

DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")

def send_alert(message):
    if not DISCORD_WEBHOOK:
        print("⚠️ Webhook tidak diset. Alert tidak dihantar.")
        return
    data = {"content": message}
    try:
        requests.post(DISCORD_WEBHOOK, json=data)
    except Exception as e:
        print(f"Gagal hantar alert: {e}")