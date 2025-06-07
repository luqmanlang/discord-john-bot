from flask import Flask, request, jsonify
from discord_notifier import send_to_discord

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    symbol = data.get("symbol", "Unknown")
    price = data.get("price", "N/A")
    condition = data.get("condition", "N/A")
    message = f"📡 Webhook Alert!\nSymbol: {symbol}\nPrice: {price}\nCondition: {condition}"
    send_to_discord(message)
    return jsonify({"status": "success", "msg": "Sent to Discord!"})

if __name__ == '__main__':
    app.run(port=5000)
