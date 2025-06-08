async def send_alert(channel, data):
    msg = f"📈 Harga: {data['price']}\nRSI: {data['rsi']}\nStochastic: {data['stochastic']}"
    await channel.send(msg)
