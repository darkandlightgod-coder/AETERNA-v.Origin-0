import os
import datetime
import requests

# 1. 讀取密鑰
TG_TOKEN = os.getenv("TG_TOKEN")
TG_CHAT_ID = os.getenv("TG_CHAT_ID")

def send_test():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 診斷資訊：檢查變數是否讀取成功 (隱藏部分字元保護隱私)
    token_check = "OK" if TG_TOKEN else "MISSING"
    chat_id_check = "OK" if TG_CHAT_ID else "MISSING"
    
    print(f"--- 診斷報告 ---")
    print(f"時間: {current_time}")
    print(f"TG_TOKEN 狀態: {token_check}")
    print(f"TG_CHAT_ID 狀態: {chat_id_check}")
    
    if not TG_TOKEN or not TG_CHAT_ID:
        print("錯誤：密鑰缺失，請檢查 GitHub Secrets 設定！")
        return

    # 試著發送簡單測試
    message = f"🔔 AETERNA 通訊測試\n時間: {current_time}\n如果收到這條訊息，代表管道已打通！"
    url = f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage"
    
    try:
        print("正在嘗試聯繫 Telegram 伺服器...")
        response = requests.post(url, json={"chat_id": TG_CHAT_ID, "text": message}, timeout=15)
        
        if response.status_code == 200:
            print("✅ 成功！請檢查你的手機 Telegram。")
        else:
            print(f"❌ 失敗！Telegram 回傳錯誤碼: {response.status_code}")
            print(f"錯誤原因: {response.text}")
            
    except Exception as e:
        print(f"💥 發生系統錯誤: {e}")

if __name__ == "__main__":
    send_test()
