import os
import requests

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_CHANNEL_ID = os.getenv("DISCORD_CHANNEL_ID")

def send_alert(message):
    if not DISCORD_TOKEN or not DISCORD_CHANNEL_ID:
        print("⚠️ Discord credentials not set.")
        return
    url = f"https://discord.com/api/v10/channels/{DISCORD_CHANNEL_ID}/messages"
    headers = {
        "Authorization": f"Bot {DISCORD_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "content": message
    }
    response = requests.post(url, json=payload, headers=headers)
    print("📤 Alert sent:", response.status_code, response.text)