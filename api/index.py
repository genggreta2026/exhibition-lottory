from flask import Flask, request, send_file
import requests

app = Flask(__name__)

# 你的谷歌脚本URL（已经填好）
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbz1vudODw-kpPauY0SMeMnbpY3cASVn6elpyRO_FapKI5m44lS2k4GcTuORCU2RJarN/exec"

@app.route('/')
def index():
    try:
        return send_file('index.html')
    except Exception as e:
        return f"页面加载失败: {str(e)}", 500

@app.route('/api/log', methods=['POST'])
def log_data():
    try:
        # 获取表单数据
        name = request.form.get('name', '')
        phone = request.form.get('phone', '')
        email = request.form.get('email', '')
        prize = request.form.get('prize', '')
        
        # 发送数据到谷歌表格
        response = requests.post(
            GOOGLE_SCRIPT_URL,
            data={
                'name': name,
                'phone': phone,
                'email': email,
                'prize': prize
            },
            timeout=10
        )
        
        # 返回成功响应
        return "success"
    except Exception as e:
        # 出错也不影响抽奖，只打印日志
        print(f"记录失败: {str(e)}")
        return "success"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
