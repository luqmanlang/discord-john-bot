import sys
import os
import utils.discord_bot

# Tambah path ke folder atas supaya boleh import dari utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.analysis import run_analysis

if __name__ == "__main__":
    run_analysis()
