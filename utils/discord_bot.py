
import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

client = discord.Client(intents=discord.Intents.default())

def send_alert(price, rsi, stochastic, source):
    @client.event
    async def on_ready():
        channel = client.get_channel(CHANNEL_ID)
        msg = f"🔔 **ALERT 1H**
Harga: ${price}\nRSI(5): {rsi}\nStochastic: {stochastic}\nSumber: {source}"
        await channel.send(msg)
        await client.close()

    client.run(TOKEN)
