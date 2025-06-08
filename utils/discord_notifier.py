import os
import requests

def send_discord_alert(message):
    webhook_url = os.getenv("DISCORD_WEBHOOK")
    if not webhook_url:
        print("❌ DISCORD_WEBHOOK not set.")
        return
    data = {"content": message}
    try:
        requests.post(webhook_url, json=data)
    except Exception as e:
        print("Error sending to Discord:", e)
