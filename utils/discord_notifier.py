
import discord
import os
import asyncio

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))

client = discord.Client(intents=discord.Intents.default())

async def send_discord_alert(message):
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(f"📈 Alert: {message}")
    else:
        print("⚠️ Channel not found")

@client.event
async def on_ready():
    print(f"Bot is ready: {client.user}")

def start_bot():
    client.run(TOKEN)
