import os
import requests

def send_to_discord(message):
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    if webhook_url:
        data = {"content": message}
        requests.post(webhook_url, json=data)
