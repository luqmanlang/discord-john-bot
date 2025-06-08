
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
    print(f"Bot aktif sebagai {bot.user.name}")
    hourly_alert.start()
    four_hour_alert.start()

@tasks.loop(hours=1)
async def hourly_alert():
    channel = bot.get_channel(DISCORD_CHANNEL_ID)
    result = get_full_analysis("1h")
    await channel.send(f"📊 1H Alert:\n{result}")

@tasks.loop(hours=4)
async def four_hour_alert():
    channel = bot.get_channel(DISCORD_CHANNEL_ID)
    result = get_full_analysis("4h")
    await channel.send(f"📊 4H Alert:\n{result}")

@bot.command()
async def analisis(ctx):
    result = get_full_analysis("1h")
    await ctx.send(result)

bot.run(DISCORD_TOKEN)
