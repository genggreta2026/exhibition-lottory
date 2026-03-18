from flask import Flask, request
import datetime
import requests

app = Flask(__name__)

# ====================== 在这里填你的谷歌表格ID ======================
GOOGLE_SHEET_ID = "把你表格ID粘贴在这里"
# ===================================================================

@app.route('/')
def home():
    with open('index.html', 'r', encoding='utf-8') as f:
        return f.read()

@app.route('/api/log', methods=['POST'])
def save_log():
    # 接收前端传过来的内容
    content = request.form.get('content', '')
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        # 自动写到谷歌表格
        url = "https://script.google.com/macros/s/AKfycbzH4O1qZJk2xYz4H4G1e8Z1e8Z1e8Z1/exec"
        data = {
            "sheetId": GOOGLE_SHEET_ID,
            "time": now,
            "content": content
        }
        requests.post(url, data=data, timeout=10)
    except:
        pass

    return "ok"
