from flask import Flask
from webhook.tv_webhook_realtime import app as tv_app

# This reuses the tv_webhook Flask app
app = tv_app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
