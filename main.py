import os
import discord
from discord.ext import commands, tasks
import requests

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))
BOT_PREFIX = "!"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)

def get_btc_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    try:
        response = requests.get(url)
        data = response.json()
        return data['bitcoin']['usd']
    except Exception as e:
        return f"Error: {e}"

@bot.event
async def on_ready():
    print(f"✅ Bot aktif sebagai {bot.user.name}")
    channel = bot.get_channel(DISCORD_CHANNEL_ID)
    if channel:
        await channel.send("🤖 JohnAI sudah aktif dengan real-time data dari CoinGecko.")
        hourly_alert.start()

@tasks.loop(hours=1)
async def hourly_alert():
    price = get_btc_price()
    channel = bot.get_channel(DISCORD_CHANNEL_ID)
    if channel:
        await channel.send(f"📈 BTC Price (1H Update): ${price}")

@bot.command()
async def analisis(ctx):
    price = get_btc_price()
    await ctx.send(f"📊 BTC sekarang: ${price} (Real-time via CoinGecko)")

bot.run(DISCORD_TOKEN)
