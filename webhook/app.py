from flask import Flask, request, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)

LOG_FILE = "webhook/alerts_log.txt"

@app.route('/webhook', methods=["POST"])
def webhook():
    data = request.json
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_msg = f"""📡 Alert Diterima:
🕒 Masa: {now}
📊 Symbol: {data.get('symbol', 'N/A')}
⏱ Interval: {data.get('interval', 'N/A')}
💰 Harga: {data.get('price', 'N/A')}
🧭 Syarat: {data.get('condition', 'N/A')}
"""

    print(log_msg)
    with open(LOG_FILE, "a") as f:
        f.write(log_msg + "\n")

    return jsonify({
        "status": "received",
        "timestamp": now,
        "summary": {
            "symbol": data.get("symbol", "N/A"),
            "price": data.get("price", "N/A"),
            "interval": data.get("interval", "N/A"),
            "condition": data.get("condition", "N/A")
        }
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
