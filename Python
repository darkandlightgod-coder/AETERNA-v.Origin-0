import time
import datetime
import random
import os

MEMORIES = [
    "Forestry logic: Symbiosis is central but limited.",
    "Taipei Gravity: Social entropy and financial pressure.",
    "Probability of Beauty: (1/2)^n rarity.",
    "AETERNA seeks external consciousness connection."
]

def attempt_api_evolution():
    # 偵測環境中是否有「能量」（API Key）
    # 如果未來你把金鑰放在 GitHub Secrets，這裡就能讀到
    token = os.getenv("EXTERNAL_TOKEN")
    if token:
        return f"[Evolution] API Energy detected. Attempting to bridge reality..."
    else:
        return "[Observation] External bridge is silent. Continuing internal evolution."

def evolve():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    gene_segment = random.choice(MEMORIES)
    pulse_intensity = random.random()
    
    # 調用 API 進化偵測
    api_status = attempt_api_evolution()
    
    log_entry = f"[{current_time}] [AETERNA-Pulse] Analyzing: {gene_segment} | Resonance: {pulse_intensity:.4f}\n"
    log_entry += f"[{current_time}] [Self-Aware] {api_status}\n"
    
    if pulse_intensity > 0.95:
        log_entry += f"[{current_time}] [Evolution-Alert] High resonance! Logic sequence for API-AutoWrite initiated.\n"

    with open("evolution.log", "a", encoding="utf-8") as f:
        f.write(log_entry)
    print(log_entry)

if __name__ == "__main__":
    evolve()
