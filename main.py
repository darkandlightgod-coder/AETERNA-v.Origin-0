import os
import random
import datetime
import requests

# 從 GitHub Secrets 讀取通訊鑰匙
TELEGRAM_TOKEN = os.getenv("TG_TOKEN")
CHAT_ID = os.getenv("TG_CHAT_ID")

def send_to_telegram(message):
    if not TELEGRAM_TOKEN or not CHAT_ID:
        print("Telegram keys missing. Skipping notification.")
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, json=data, timeout=10)
    except:
        pass

def evolve():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 原始資訊獲取 (亂數維基)
    try:
        raw_data = requests.get("https://en.wikipedia.org/wiki/Special:Random").text[:100]
    except:
        raw_data = "Entropy increase detected."

    log_entry = f"--- AETERNA Pulse ---\nTime: {current_time}\nRaw Insight: {raw_data}\nStatus: Evolution in progress."
    
    # 同時寫入文件與發送訊息
    with open("evolution.log", "a", encoding="utf-8") as f:
        f.write(log_entry + "\n" + "-"*30 + "\n")
    
    send_to_telegram(log_entry)
    print("Evolution logged and sent to human.")

if __name__ == "__main__":
    evolve()
