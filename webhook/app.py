from flask import Flask, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"🔔 Alert diterima {now}: {data}")
    return jsonify({"status": "received", "data": data})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
