import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]
PHOTO_URL = "https://i.imgur.com/8yja6ge.png"  # Replace with your image URL

data = {"chat_id": CHAT_ID, "photo": PHOTO_URL}
r = requests.post(f"https://api.telegram.org/bot{TOKEN}/sendPhoto", data=data)
print(r.status_code, r.text)
