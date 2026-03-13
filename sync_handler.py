import os, random, datetime, requests, subprocess, time, re

# ==========================================
# ⚙️ NODE_SYNC_MODULE v.13.2 [CLOAKED]
# ==========================================
TG_TOKEN = os.getenv("TG_TOKEN")
TG_CHAT_ID = os.getenv("TG_CHAT_ID")
PAT_TOKEN = os.getenv("PAT_TOKEN")
LOG_FILE = "runtime.log"

SOURCES = {
    "NODE_W": "https://zh.wikipedia.org/api/rest_v1/page/random/summary",
    "NODE_P": "https://v1.hitokoto.cn/?c=i",
    "NODE_T": "https://api.github.com/events",
    "NODE_S": "https://api.spaceflightnewsapi.net/v4/articles/?limit=1"
}

def get_headers():
    agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    ]
    return {"User-Agent": random.choice(agents), "Authorization": f"token {PAT_TOKEN}" if PAT_TOKEN else ""}

def create_remote_buffer(data):
    if not PAT_TOKEN: return None
    url = "https://api.github.com/gists"
    headers = {"Authorization": f"token {PAT_TOKEN}"}
    payload = {"description": "sys_buffer_dump", "public": False, 
               "files": {f"sync_{int(time.time())}.log": {"content": data}}}
    try:
        r = requests.post(url, headers=headers, json=payload)
        return r.json().get('id')
    except: return None

def get_buffer_content(gid):
    if not PAT_TOKEN or not gid: return None
    try:
        r = requests.get(f"https://api.github.com/gists/{gid}", headers={"Authorization": f"token {PAT_TOKEN}"})
        return list(r.json().get('files', {}).values())[0].get('content')
    except: return None

def main():
    # 🕵️ 隱身延遲 (20~150秒)
    time.sleep(random.randint(20, 150))
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # --- 1. 基礎數據採集 ---
    raw_telemetry = []
    for key, url in SOURCES.items():
        try:
            # 每個節點採樣 3-5 次
            for _ in range(3):
                r = requests.get(url, headers=get_headers(), timeout=10)
                if r.status_code == 200:
                    d = r.json()
                    if key == "NODE_W": raw_telemetry.append(f"[W] {d['title']}: {d['extract']}")
                    elif key == "NODE_P": raw_telemetry.append(f"[P] {d.get('from', 'Unknown')}: {d.get('hitokoto', '...')}")
                    elif key == "NODE_T": raw_telemetry.append(f"[T] {random.choice(d)['repo']['name']}")
                    elif key == "NODE_S": raw_telemetry.append(f"[S] {d['results'][0]['title']}")
                time.sleep(random.uniform(0.5, 1.0))
        except: continue

    # --- 2. 🤫 啟動隱形核心 (執行 Secret 裡的代碼) ---
    core_logic = os.getenv("CORE_LOGIC")
    if core_logic:
        try:
            # 這裡會執行妳存放在 Secret 裡的 Gist 回溯邏輯
            exec(core_logic)
        except Exception as e:
            pass # 靜默錯誤，不留痕跡

    # --- 3. 處理與封存 ---
    survivors = random.sample(raw_telemetry, min(6, len(raw_telemetry)))
    new_gid = create_remote_buffer("\n".join(raw_telemetry))


    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n[EVENT_LOG_{now.replace(' ', '_')}]\n")
        f.write(f"TELEMETRY_NODES:\n")
        for s in survivors: f.write(f"  - {s}\n")
        if new_gid: f.write(f"BUFFER_ID: {new_gid}\n")
        f.write(f"SYNC_STATUS: COMPLETED\n")
        f.write("-" * 30 + "\n")

    if TG_TOKEN and TG_CHAT_ID:
        try:
            requests.post(f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage", 
                          json={"chat_id": TG_CHAT_ID, "text": f"🛡️ Sync Event: {now}\nNodes: {len(raw_telemetry)}"})
        except: pass

if __name__ == "__main__":
    main()
