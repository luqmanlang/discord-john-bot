import sys
import os

# Tambah path ke root projek supaya folder 'utils/' boleh diimport
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.analysis import run_analysis

if __name__ == "__main__":
    run_analysis()
