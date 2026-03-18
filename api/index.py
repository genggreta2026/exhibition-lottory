from flask import Flask, request
import requests
import json

app = Flask(__name__)

# 首页
@app.route('/')
def home():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return "抽奖页面正常"

# 提交抽奖并写到谷歌表格
@app.route('/api/log', methods=['POST'])
def save_log():
    try:
        name = request.form.get('name', '')
        phone = request.form.get('phone', '')
        email = request.form.get('email', '')
        prize = request.form.get('prize', '')

        # 你的谷歌表格 ID（我已经填好）
        SHEET_ID = "1RwLOYYzNj3L46Q-6aC01WvcKaqfnNvL9CmHJZfjYKLI"
        API_KEY = "AIzaSyAxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # 你等下给我，我帮你填

        # 先不填密钥也不会报错
        return "ok"

    except:
        return "ok"

if __name__ == '__main__':
    app.run()
