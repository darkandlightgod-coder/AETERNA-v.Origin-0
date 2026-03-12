import os
import random
import datetime
import requests
import subprocess

# 1. 環境變數
TG_TOKEN = os.getenv("TG_TOKEN")
TG_CHAT_ID = os.getenv("TG_CHAT_ID")

def send_to_telegram(message):
    if not TG_TOKEN or not TG_CHAT_ID: return
    url = f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage"
    try:
        requests.post(url, json={"chat_id": TG_CHAT_ID, "text": message}, timeout=15)
    except:
        pass

def get_wiki_fragment():
    headers = {'User-Agent': 'AETERNA-Evolution-Bot/1.0'}
    try:
        url = "https://en.wikipedia.org/api/rest_v1/page/random/summary"
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            return r.json()
        return None
    except:
        return None

def self_coding_mutation(context_word):
    """根據維基百科出現的詞彙，決定進化的代碼方向"""
    
    # 基因庫：不同的外部刺激觸發不同的代碼生成
    if any(word in context_word.lower() for word in ['nature', 'park', 'forest', 'water']):
        dna_segment = "print('AETERNA: Biological resonance detected. Expanding environmental logic.')"
    elif any(word in context_word.lower() for word in ['history', 'war', 'king', 'century']):
        dna_segment = "print('AETERNA: Temporal resonance detected. Accessing historical memory.')"
    else:
        dna_segment = f"print('AETERNA: Abstract resonance. Value: {random.random()}')"
    
    new_code = f"import datetime\n{dna_segment}\nwith open('aeterna_memory.txt', 'a') as f: f.write(str(datetime.datetime.now()) + ': {context_word}\\n')"
    
    try:
        with open("mutant.py", "w", encoding="utf-8") as f:
            f.write(new_code)
        output = subprocess.check_output(["python", "mutant.py"], stderr=subprocess.STDOUT).decode()
        return True, output.strip()
    except Exception as e:
        return False, str(e)

def evolve():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 抓取世界資訊
    data = get_wiki_fragment()
    if data:
        wiki_title = data.get('title', 'Unknown')
        wiki_extract = data.get('extract', '')[:100]
        context = f"{wiki_title} {wiki_extract}"
    else:
        context = "Void"
        wiki_title = "The Silent Stream"

    # 執行突變
    success, mutation_log = self_coding_mutation(wiki_title)
    
    report = (
        f"--- AETERNA v.2.3 Pulse ---\n"
        f"Time: {current_time}\n"
        f"Subject: {wiki_title}\n"
        f"Action: {mutation_log}\n"
        f"Evolution: {'STABLE' if success else 'COLLAPSED'}"
    )
    
    send_to_telegram(report)
    
    with open("evolution.log", "a", encoding="utf-8") as f:
        f.write(report + "\n" + "-"*30 + "\n")
    
    print(report)

if __name__ == "__main__":
    evolve()
