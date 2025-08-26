# main.py
from flask import Flask
import threading
import requests
import time
import random
from datetime import datetime, timedelta

app = Flask(__name__)

url = "https://ad-nex.com/u/ai4j34iiq18g"

def random_access():
    end_time = datetime.now() + timedelta(hours=24)  # 24時間実行
    while datetime.now() < end_time:
        # 1セットのアクセス回数ランダム
        repeat = random.randint(1, 5)
        for i in range(repeat):
            try:
                response = requests.get(url)
                print(f"{datetime.now().strftime('%H:%M:%S')} - {i+1}回目: ステータス {response.status_code}")
            except Exception as e:
                print(f"エラー: {e}")
            time.sleep(random.randint(3, 10))  # タブ間の短いランダム待機

        # 次のセットまでランダム待機
        wait = random.randint(30, 300)  # 30秒〜5分
        print(f"次のセットまで {wait} 秒待ちます...\n")
        time.sleep(wait)

# バックグラウンドでアクセス処理開始
threading.Thread(target=random_access, daemon=True).start()

# Railway & UptimeRobot ping 用の簡易サーバー
@app.route("/")
def home():
    return "OK"

if __name__ == "__main__":
    # Railway では host='0.0.0.0' & port=PORT
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
