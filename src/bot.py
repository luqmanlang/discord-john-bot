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
    if not channel:
        print("❌ Gagal jumpa channel. Semak CHANNEL_ID dan pastikan bot telah join server.")
        return

    try:
        john_msg = generate_analysis()
        alpha_msg = counter_analysis()

        if not john_msg or not alpha_msg:
            await channel.send("❌ Gagal jana analisis. Data mungkin tidak lengkap.")
            return

        full_msg = f"📈 **Analisis Bitcoin Terkini**\n\n{john_msg}\n\n{alpha_msg}"
        await channel.send(full_msg)

    except Exception as e:
        await channel.send(f"⚠️ Error dalam `send_analysis`: {str(e)}")

bot.run(TOKEN)
