
import requests
import time
from telegram import Bot

# CONFIG
BOT_TOKEN = 'your_bot_token_here'
CHAT_ID = 'your_chat_id_here'
FETCH_URL = 'http://51.68.35.151/ints/agent/res/data_smscdr.php?...'

def fetch_sms():
    try:
        response = requests.get(FETCH_URL)
        if response.status_code == 200:
            return response.text.strip()
        else:
            return None
    except Exception as e:
        print("Error fetching SMS:", e)
        return None

def send_to_telegram(message):
    bot = Bot(token=BOT_TOKEN)
    try:
        bot.send_message(chat_id=CHAT_ID, text=message)
        print("Message sent to Telegram")
    except Exception as e:
        print("Error sending message:", e)

def main():
    last_sms = ""
    while True:
        sms = fetch_sms()
        if sms and sms != last_sms:
            send_to_telegram(sms)
            last_sms = sms
        time.sleep(5)

if __name__ == '__main__':
    main()
