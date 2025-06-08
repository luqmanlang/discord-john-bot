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
async def john(ctx):
    report = john_analysis()
    await ctx.send(report)

@bot.command()
async def alpha(ctx):
    report = alpha_analysis()
    await ctx.send(report)

bot.run(os.getenv("DISCORD_BOT_TOKEN"))
