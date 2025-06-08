import os
import discord
from discord.ext import commands

token = os.getenv("DISCORD_BOT_TOKEN")
intents = discord.Intents.default()
intents.message_content = True  # penting kalau nak baca mesej

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot John sudah online sebagai {bot.user}")

bot.run(token)
