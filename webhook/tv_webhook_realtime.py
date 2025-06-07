from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    print(f"📡 [TradingView Alert @ {timestamp}] Data Diterima:")
    print(data)
    if "indicator" in data:
        print(f"📊 Indikator: {data['indicator']}")
    if "price" in data:
        print(f"💰 Harga: {data['price']}")
    if "symbol" in data:
        print(f"🪙 Simbol: {data['symbol']}")
    return jsonify({"status": "OK", "message": "Alert diterima oleh Webhook!"})

def start_webhook():
    app.run(host="0.0.0.0", port=5000)
