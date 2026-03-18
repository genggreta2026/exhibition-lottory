from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "页面正常运行！"

@app.route('/api/log', methods=['POST'])
def save_log():
    return "ok"

if __name__ == '__main__':
    app.run()
