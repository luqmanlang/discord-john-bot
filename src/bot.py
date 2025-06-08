import os
import discord
from discord.ext import commands
from brain.john_ai import generate_analysis as john_analysis
from brain.alpha_ai import counter_analysis as alpha_analysis

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot sudah online sebagai {bot.user}")

@bot.command()
async def analisis(ctx):
    from brain.john_ai import generate_analysis
    from brain.alpha_ai import counter_analysis
    john_msg = generate_analysis()
    alpha_msg = counter_analysis()
    await ctx.send(f"📊 **Analisis Bitcoin Terkini**\n\n{john_msg}\n{alpha_msg}")

bot.run(os.getenv("DISCORD_BOT_TOKEN"))
