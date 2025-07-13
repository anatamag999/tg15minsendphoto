import os
import datetime
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

# Get current UTC time
now = datetime.datetime.utcnow()
minute = now.minute

# Round down to nearest target minute (15, 30, 45)
if 15 <= minute < 30:
    target = 15
elif 30 <= minute < 45:
    target = 30
elif 45 <= minute < 60:
    target = 45
else:
    target = None  # 00–14: no photo

# Assign URL based on target
photo_map = {
    15: "https://i.imgur.com/8yja6ge.png",
    30: "https://i.ibb.co/KcL7j81V/xx30.png",
    45: "https://i.ibb.co/g0gXSBZ/xx45.png",
}

PHOTO_URL = photo_map.get(target)

# Send photo if valid
if PHOTO_URL:
    data = {"chat_id": CHAT_ID, "photo": PHOTO_URL}
    r = requests.post(f"https://api.telegram.org/bot{TOKEN}/sendPhoto", data=data)
    print(f"Sent photo for minute {target}: {r.status_code}")
else:
    print("No photo scheduled at this time.")
