
import asyncio
from utils.discord_notifier import send_discord_alert
from utils.indicators import check_rsi_stochastic_signals

async def run_bot():
    while True:
        signal = check_rsi_stochastic_signals()
        if signal:
            await send_discord_alert(signal)
        await asyncio.sleep(3600)  # Check every hour

if __name__ == "__main__":
    asyncio.run(run_bot())
