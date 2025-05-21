# https://api.telegram.org/bot<YOUR_TOKEN>/setWebhook?url=https://yourapp.onrender.com/webhook/<YOUR_TOKEN>

from flask import Flask, request
import requests
import os

app = Flask(__name__)

TOKEN = os.getenv("BOT_TOKEN")  # You can set this in Render environment
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

@app.route('/')
def home():
    return "Bot is running!"

@app.route(f'/webhook/{TOKEN}', methods=['POST'])
def webhook():
    data = request.get_json()
    
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        # Simple echo bot
        reply = f"You said: {text}"
        payload = {
            "chat_id": chat_id,
            "text": reply
        }
        requests.post(TELEGRAM_API_URL, json=payload)

    return "ok", 200

if __name__ == '__main__':
    app.run()
