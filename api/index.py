from flask import Flask, request
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# 首页显示抽奖页面
@app.route('/')
def home():
    with open('index.html', 'r', encoding='utf-8') as f:
        return f.read()

# 抽奖提交接口 + 写入谷歌表格（已填好你的表格ID）
@app.route('/api/log', methods=['POST'])
def save_log():
    try:
        # 接收前端传过来的抽奖数据
        name = request.form.get('name', '')
        phone = request.form.get('phone', '')
        email = request.form.get('email', '')
        prize = request.form.get('prize', '')

        # 谷歌表格认证（需确保service_account.json和此文件同目录）
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]
        creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
        client = gspread.authorize(creds)

        # 用你的表格ID打开表格（已填好，不用改）
        sheet = client.open_by_key("1RwLOYYzNj3L46Q-6aC01WvcKaqfnNvL9CmHJZfjYKLI").sheet1

        # 追加抽奖记录（姓名、手机号、邮箱、中奖结果）
        sheet.append_row([name, phone, email, prize])

        return "ok"

    except Exception as e:
        # 就算表格写入失败，页面也不会崩，只会打印错误
        print("谷歌表格写入错误：", e)
        return "ok"

if __name__ == '__main__':
    app.run(debug=True)
