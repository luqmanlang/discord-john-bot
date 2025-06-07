from flask import Flask
from utils.webhook_receiver import webhook_bp

app = Flask(__name__)
app.register_blueprint(webhook_bp, url_prefix="/webhook")

@app.route("/")
def home():
    return "Bot is running!"

if __name__ == "__main__":
    app.run(debug=True)
