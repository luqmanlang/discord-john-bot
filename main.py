import discord
import asyncio
from utils.indicators import get_rsi_stochastic
from utils.discord_notifier import send_alert

TOKEN = "YOUR_DISCORD_BOT_TOKEN"
CHANNEL_ID = 123456789012345678  # Ganti dengan ID channel awak

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot {client.user} sudah online!')
    await schedule_alerts()

async def schedule_alerts():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    while not client.is_closed():
        data = get_rsi_stochastic()
        await send_alert(channel, data)
        await asyncio.sleep(3600)  # Setiap 1 jam

client.run(TOKEN)
