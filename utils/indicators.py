import asyncio
import aiohttp

async def fetch_price(session, url):
    async with session.get(url) as response:
        return await response.json()

async def start_data_cycle():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    async with aiohttp.ClientSession() as session:
        while True:
            data = await fetch_price(session, url)
            print("📊 Harga BTC:", data.get("bitcoin", {}).get("usd", "N/A"))
            await asyncio.sleep(3600)  # Tukar selang masa jika mahu
