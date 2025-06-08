import schedule
import time
from utils.analysis import run_analysis

def job_1h():
    run_analysis("1h")

def job_4h():
    run_analysis("4h")

# Jadual tugas
schedule.every().hour.at(":00").do(job_1h)      # setiap jam
schedule.every(4).hours.at(":00").do(job_4h)     # setiap 4 jam

print("Bot indikator Bitcoin telah bermula... ⏳")

while True:
    schedule.run_pending()
    time.sleep(1)
