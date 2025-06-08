import sys
import os

# Tambah path ke folder atas supaya boleh import dari utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import alert & bot
from utils.analysis import run_analysis
from utils.discord_bot import bot  # INI PENTING

if __name__ == "__main__":
    run_analysis()
    bot.run(os.getenv("DISCORD_BOT_TOKEN"))  # HIDUPKAN BOT
