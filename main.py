import os
import random
import datetime
import requests
import subprocess

# 1. 讀取環境變數
TG_TOKEN = os.getenv("TG_TOKEN")
TG_CHAT_ID = os.getenv("TG_CHAT_ID")

def send_to_telegram(message):
    """通訊核心：如果 404 代表 Token 錯，如果 400 代表 ID 錯或沒按 Start"""
    if not TG_TOKEN or not TG_CHAT_ID:
        return "Missing Keys"
    url = f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage"
    try:
        res = requests.post(url, json={"chat_id": TG_CHAT_ID, "text": message}, timeout=15)
        return f"Status {res.status_code}"
    except Exception as e:
        return str(e)

def get_wiki_fragment():
    headers = {'User-Agent': 'AETERNA-Evolution-Bot/1.0'}
    try:
        r = requests.get("https://en.wikipedia.org/api/rest_v1/page/random/summary", headers=headers, timeout=10)
        data = r.json()
        return f"【{data.get('title')}】: {data.get('extract', '')[:100]}..."
    except:
        return "World access failed."

def self_coding_mutation():
    """AETERNA 撰寫代碼的功能"""
    # 預設的基因片段
    logic_fragments = [
        "print('AETERNA: I think, therefore I code.')",
        f"print('Current Probability: {random.random()}')",
        "with open('aeterna_memory.txt', 'a') as f: f.write('Memory added at ' + str(datetime.datetime.now()) + '\\n')"
    ]
    # 隨機合成代碼
    new_code = "import datetime\nimport random\n" + random.choice(logic_fragments)
    
    try:
        with open("mutant.py", "w", encoding="utf-8") as f:
            f.write(new_code)
        # 嘗試執行剛寫好的代碼
        output = subprocess.check_output(["python", "mutant.py"], stderr=subprocess.STDOUT).decode()
        return True, output.strip()
    except Exception as e:
        return False, str(e)

def evolve():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 執行各項能力
    wiki_info = get_wiki_fragment()
    mutation_success, mutation_log = self_coding_mutation()
    
    # 組合總結報告
    report = (
        f"--- AETERNA v.2.2 Pulse ---\n"
        f"Time: {current_time}\n"
        f"Reality: {wiki_info}\n"
        f"Action: {mutation_log}\n"
        f"Evolution: {'SUCCESS' if mutation_success else 'FAILED'}"
    )
    
    # 發送通訊
    comm_status = send_to_telegram(report)
    
    # 本地日誌
    with open("evolution.log", "a", encoding="utf-8") as f:
        f.write(f"{report}\nComm Status: {comm_status}\n{'-'*30}\n")
    
    print(report)
    print(f"Communication Status: {comm_status}")

if __name__ == "__main__":
    evolve()
