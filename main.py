import os
import discord
from discord.ext import commands, tasks
from utils.indicators import get_full_analysis

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"🤖 JohnAI ULTRA PRO aktif sebagai {bot.user}")
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("🚀 JohnAI ULTRA PRO online – auto alert, smart entry, trend watch aktif!")
        hourly_alert.start()
        daily_alert.start()

@tasks.loop(hours=1)
async def hourly_alert():
    channel = bot.get_channel(CHANNEL_ID)
    msg = get_full_analysis("1h")
    await channel.send(msg)

@tasks.loop(hours=24)
async def daily_alert():
    channel = bot.get_channel(CHANNEL_ID)
    msg = get_full_analysis("1d") + "\n\n" + get_full_analysis("1w") + "\n\n" + get_full_analysis("1M")
    await channel.send(msg)

bot.run(TOKEN)
