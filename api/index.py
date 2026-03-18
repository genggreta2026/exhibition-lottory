from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return "页面正常"

@app.route('/api/log', methods=['POST'])
def save_log():
    name = request.form.get('name', '')
    phone = request.form.get('phone', '')
    email = request.form.get('email', '')
    prize = request.form.get('prize', '')
    
    # 这里以后再加谷歌表格，现在先保证不报错
    return "ok"

if __name__ == '__main__':
    app.run()
