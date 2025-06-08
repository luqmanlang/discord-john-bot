import os
import discord
from discord.ext import commands

# Ambil token dari environment variable
token = os.getenv("DISCORD_BOT_TOKEN")

if not token:
    raise ValueError("❌ DISCORD_BOT_TOKEN not set!")

intents = discord.Intents.default()
intents.message_content = True  # Penting untuk baca mesej

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot John sudah online sebagai {bot.user}")

# Jalankan bot
bot.run(token)
