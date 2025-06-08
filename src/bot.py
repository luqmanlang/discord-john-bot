import os
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

from john_ai import generate_john_report
from alpha_ai import generate_alpha_counter
from utils.notifier import send_embed_message

load_dotenv()

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
DISCORD_CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot telah log masuk sebagai {bot.user}")
    report_task.start()

@tasks.loop(hours=1)
async def report_task():
    try:
        john_report = await generate_john_report()
        alpha_report = await generate_alpha_counter(john_report)
        await send_embed_message(bot, DISCORD_CHANNEL_ID, "JohnAI Alert", john_report, "💡 AI John")
        await send_embed_message(bot, DISCORD_CHANNEL_ID, "AlphaAI Counter", alpha_report, "🔍 AI Alpha")
    except Exception as e:
        print("❌ Error semasa laporan:", e)

bot.run(DISCORD_BOT_TOKEN)
