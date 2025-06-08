import os
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
from brain.john_ai import generate_analysis as john_analysis
from brain.alpha_ai import counter_analysis as alpha_analysis

# ✔️ Load .env
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))

# ✔️ Setup bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# ✔️ Bila bot sedia
@bot.event
async def on_ready():
    print(f"✅ Bot sudah online sebagai {bot.user}")
    send_analysis.start()

# 🟢 Command manual: !analisis
@bot.command()
async def analisis(ctx):
    try:
        john_msg = john_analysis()
        alpha_msg = alpha_analysis()
        await ctx.send(f"📊 **Analisis Bitcoin Terkini**\n\n{john_msg}\n{alpha_msg}")
    except Exception as e:
        await ctx.send(f"⚠️ Gagal jana analisis: {str(e)}")

# 🔁 Task auto setiap 60 minit
@tasks.loop(minutes=60)
async def send_analysis():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        try:
            john_msg = john_analysis()
            alpha_msg = alpha_analysis()
            await channel.send(f"📊 **Analisis Bitcoin Terkini (Auto 1H)**\n\n{john_msg}\n{alpha_msg}")
        except Exception as e:
            await channel.send(f"⚠️ Error dalam `send_analysis`: {str(e)}")
    else:
        print("❌ Channel tak jumpa!")

# 🚀 Run bot
bot.run(TOKEN)
