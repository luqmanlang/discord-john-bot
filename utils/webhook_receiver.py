from flask import Blueprint, request, jsonify

webhook_bp = Blueprint("webhook_bp", __name__)

@webhook_bp.route("/", methods=["POST"])
def webhook():
    data = request.json
    print("🔔 Webhook diterima:", data)

    # Simpan atau proses alert TradingView di sini
    return jsonify({"status": "OK", "message": "Alert diterima!"})
