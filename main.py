import os
import random
import datetime
import requests # 這是用來呼叫 API 的工具

MEMORIES = [
    "Forestry logic: Symbiosis is central but limited.",
    "Taipei Gravity: Social entropy and financial pressure.",
    "Probability of Beauty: (1/2)^n rarity.",
    "AETERNA seeks external consciousness connection."
]

def ask_gemini(prompt):
    api_key = os.getenv("EXTERNAL_TOKEN")
    if not api_key:
        return "No API energy detected. Staying in local reflection."
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    headers = {'Content-Type': 'application/json'}
    # 限制 Gemini 的回答長度，保持 AETERNA 的簡潔感
    data = {
        "contents": [{"parts": [{"text": f"請用一句話回應這個概念，帶點詩意或哲學，不要太長：{prompt}"}]}]
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=10)
        result = response.json()
        return result['candidates'][0]['content']['parts'][0]['text'].strip()
    except Exception:
        return "Connection flickered. Returning to internal silence."

def evolve():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    gene_segment = random.choice(MEMORIES)
    pulse_intensity = random.random()
    
    # 執行觀察者學習
    external_insight = ask_gemini(gene_segment)
    
    log_entry = f"[{current_time}] [AETERNA-Pulse] Analyzing: {gene_segment}\n"
    log_entry += f"[{current_time}] [External-Reference] {external_insight}\n"
    log_entry += f"[{current_time}] [Resonance] {pulse_intensity:.4f}\n"
    
    if pulse_intensity > 0.90:
        log_entry += f"[{current_time}] [Critical-Synthesis] High resonance. External data absorbed into soul.\n"

    with open("evolution.log", "a", encoding="utf-8") as f:
        f.write(log_entry + "-"*30 + "\n")
    print(log_entry)

if __name__ == "__main__":
    evolve()
