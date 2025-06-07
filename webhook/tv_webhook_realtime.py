from flask import Flask, request, jsonify
from datetime import datetime
import json

app = Flask(__name__)

@app.route('/tv-alert', methods=['POST'])
def tv_webhook():
    data = request.json
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    alert_msg = f"""
📡 TradingView Alert Received:
📅 Time: {now}
📊 Symbol: {data.get('symbol', 'N/A')}
⏱️ Interval: {data.get('interval', 'N/A')}
💰 Price: {data.get('price', 'N/A')}
🧠 Condition: {data.get('condition', 'N/A')}
"""
    print(alert_msg)

    return jsonify({"status": "received", "message": "TV alert processed", "symbol": data.get("symbol", "N/A")})
