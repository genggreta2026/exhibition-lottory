from flask import Flask, request
import datetime
import requests

app = Flask(__name__)

# 正确的表格ID（只留中间一串）
GOOGLE_SHEET_ID = "1RwLOYYzNj3L46Q-6aC01WvcKaqfnNvL9CmHJZfjYKLI"

# 谷歌脚本地址（你自己去替换成你真实的）
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzH4O1qZJk2xYz4H4G1e8Z1e8Z1e8Z1/exec"

@app.route('/')
def home():
    with open('index.html', 'r', encoding='utf-8') as f:
        return f.read()

@app.route('/api/log', methods=['POST'])
def save_log():
    name = request.form.get('name', '')
    phone = request.form.get('phone', '')
    email = request.form.get('email', '')
    prize = request.form.get('prize', '')
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        data = {
            "sheetId": GOOGLE_SHEET_ID,
            "time": now,
            "name": name,
            "phone": phone,
            "email": email,
            "prize": prize
        }
        requests.post(GOOGLE_SCRIPT_URL, data=data, timeout=10)
    except:
        pass

    return "ok"

if __name__ == '__main__':
    app.run()
