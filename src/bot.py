import os
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

from brain.john_ai import generate_analysis
from brain.alpha_ai import counter_analysis

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot John & Alpha aktif sebagai {bot.user}")
    send_analysis.start()

@tasks.loop(minutes=60)
async def send_analysis():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        john_msg = generate_analysis()
        alpha_msg = counter_analysis()

        full_msg = f"📈 **Analisis Bitcoin Terkini**\n\n{john_msg}\n\n{alpha_msg}"
        await channel.send(full_msg)

bot.run(TOKEN)
