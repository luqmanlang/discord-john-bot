
import os
import discord
from discord.ext import commands, tasks
import datetime

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))
BOT_PREFIX = "!"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)

# === Event Bila Bot Siap ===
@bot.event
async def on_ready():
    print(f"✅ Bot aktif sebagai {bot.user.name}")
    channel = bot.get_channel(DISCORD_CHANNEL_ID)
    if channel:
        await channel.send("🤖 AI John & Alpha telah aktif di Discord!")
        hourly_alert.start()
        four_hour_alert.start()
        daily_analysis.start()
        weekly_analysis.start()
        monthly_analysis.start()

# === Command Manual ===
@bot.command()
async def ping(ctx):
    await ctx.send("📡 Bot aktif dan responsif!")

@bot.command()
async def bantuan(ctx):
    await ctx.send("📘 Perintah: !ping, !bantuan, !analisis")

@bot.command()
async def analisis(ctx):
    await ctx.send("📊 Analisis Bitcoin 1H/4H/1D/1W/1M sedang disediakan... (simulasi)")

# === Auto Alert Tasks ===
@tasks.loop(hours=1)
async def hourly_alert():
    channel = bot.get_channel(DISCORD_CHANNEL_ID)
    await channel.send("⏰ [1H] Analisis Bitcoin automatik dihantar. (simulasi)")

@tasks.loop(hours=4)
async def four_hour_alert():
    channel = bot.get_channel(DISCORD_CHANNEL_ID)
    await channel.send("🔁 [4H] Analisis Bitcoin automatik dihantar. (simulasi)")

@tasks.loop(hours=24)
async def daily_analysis():
    now = datetime.datetime.now()
    if now.hour == 12:
        channel = bot.get_channel(DISCORD_CHANNEL_ID)
        await channel.send("📆 [1D] Analisis Harian Bitcoin dihantar. (simulasi)")

@tasks.loop(hours=24)
async def weekly_analysis():
    now = datetime.datetime.now()
    if now.weekday() == 0 and now.hour == 9:
        channel = bot.get_channel(DISCORD_CHANNEL_ID)
        await channel.send("📅 [1W] Analisis Mingguan Bitcoin dihantar. (simulasi)")

@tasks.loop(hours=24)
async def monthly_analysis():
    now = datetime.datetime.now()
    if now.day == 1 and now.hour == 9:
        channel = bot.get_channel(DISCORD_CHANNEL_ID)
        await channel.send("📈 [1M] Analisis Bulanan Bitcoin dihantar. (simulasi)")

bot.run(DISCORD_TOKEN)
