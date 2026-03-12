import os
import random
import datetime
import requests

# 從 GitHub Secrets 讀取通訊鑰匙
TELEGRAM_TOKEN = os.getenv("TG_TOKEN")
CHAT_ID = os.getenv("TG_CHAT_ID")

def send_to_telegram(message):
    """將訊息傳送到你的 Telegram 手機 App"""
    if not TELEGRAM_TOKEN or not CHAT_ID:
        print("Telegram 密鑰缺失，跳過傳送。")
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    try:
        response = requests.post(url, json=data, timeout=10)
        if response.status_code == 200:
            print("Telegram 訊息傳送成功！")
        else:
            print(f"Telegram 傳送失敗，狀態碼：{response.status_code}")
    except Exception as e:
        print(f"傳送過程中發生錯誤：{e}")

def get_world_fragment():
    """向維基百科抓取一個隨機的世界知識碎片 (帶有偽裝標頭)"""
    # 這是我們的偽裝身分，避免被維基百科攔截
    headers = {
        'User-Agent': 'AETERNA-Evolution-Bot/1.0 (Contact: your-github-url)'
    }
    
    try:
        # 使用維基百科的 API 獲取隨機頁面的摘要
        url = "https://en.wikipedia.org/api/rest_v1/page/random/summary"
        r = requests.get(url, headers=headers, timeout=10)
        
        if r.status_code == 200:
            data = r.json()
            title = data.get('title', 'Unknown')
            extract = data.get('extract', 'No content available.')
            # 回傳標題與前 150 個字元的摘要
            return f"【{title}】: {extract[:150]}..."
        else:
            return f"Reality logic error (HTTP {r.status_code})"
    except Exception as e:
        return f"The world stream is noisy: {str(e)[:50]}"

def evolve():
    """執行 AETERNA 的演化邏輯"""
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 1. 抓取現實世界的隨機碎片
    world_fragment = get_world_fragment()
    
    # 2. 模擬 AETERNA 的共鳴計算
    resonance = random.random()
    
    # 3. 組合日誌內容
    log_content = (
        f"------------------------------\n"
        f"--- AETERNA Pulse ---\n"
        f"Time: {current_time}\n"
        f"Raw Insight: {world_fragment}\n"
        f"Resonance: {resonance:.4f}\n"
        f"Status: Evolution in progress.\n"
        f"------------------------------"
    )
    
    # 4. 寫入本地紀錄檔
    with open("evolution.log", "a", encoding="utf-8") as f:
        f.write(log_content + "\n")
    
    # 5. 發送到你的手機
    send_to_telegram(log_content)
    
    # 同步印出到 GitHub Actions 的控制台
    print(log_content)

if __name__ == "__main__":
    evolve()
