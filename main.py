import os
import discord
from discord.ext import commands, tasks
from utils.indicators import get_full_analysis

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID", "0"))
BOT_PREFIX = "!"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot aktif sebagai {bot.user.name}")
    channel = bot.get_channel(DISCORD_CHANNEL_ID)
    if channel:
        await channel.send("🤖 AI John & Alpha Pro aktif di Discord!")
        hourly_alert.start()
        four_hour_alert.start()
        daily_analysis.start()
        weekly_analysis.start()
        monthly_analysis.start()

@bot.command()
async def ping(ctx):
    await ctx.send("🔴 Bot aktif dan responsif!")

@bot.command()
async def analisis(ctx):
    report = get_full_analysis("1h")
    await ctx.send(report)

@tasks.loop(hours=1)
async def hourly_alert():
    print("⏱ 1H Alert Triggered")

@tasks.loop(hours=4)
async def four_hour_alert():
    print("⏱ 4H Alert Triggered")

@tasks.loop(hours=24)
async def daily_analysis():
    print("📊 Daily Analysis Triggered")

@tasks.loop(hours=24*7)
async def weekly_analysis():
    print("📈 Weekly Analysis Triggered")

@tasks.loop(hours=24*30)
async def monthly_analysis():
    print("📅 Monthly Analysis Triggered")

bot.run(DISCORD_TOKEN)
