import os
import discord
from discord.ext import commands, tasks
import datetime

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
BOT_PREFIX = "!"
DISCORD_CHANNEL_ID = os.getenv("DISCORD_CHANNEL_ID")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)

# === AI John & Alpha System ===

@bot.event
async def on_ready():
    print(f"✅ Bot aktif sebagai {bot.user.name}")
    channel_id = os.getenv("DISCORD_CHANNEL_ID")
    if channel_id:
        channel = bot.get_channel(int(channel_id))
        if channel:
            await channel.send("🤖 AI John & Alpha telah aktif di Discord!")
            hourly_alert.start()
            four_hour_alert.start()
            daily_analysis.start()
            weekly_analysis.start()
            monthly_analysis.start()

@tasks.loop(hours=1)
async def hourly_alert():
    print("🔔 1H Alert Triggered")

@tasks.loop(hours=4)
async def four_hour_alert():
    print("🔔 4H Alert Triggered")

@tasks.loop(hours=24)
async def daily_analysis():
    print("📊 Daily Analysis Triggered")

@tasks.loop(hours=24*7)
async def weekly_analysis():
    print("📊 Weekly Analysis Triggered")

@tasks.loop(hours=24*30)
async def monthly_analysis():
    print("📊 Monthly Analysis Triggered")

bot.run(DISCORD_TOKEN)
