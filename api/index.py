from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    with open('index.html', 'r', encoding='utf-8') as f:
        return f.read()

@app.route('/api/log', methods=['POST'])
def save_log():
    content = request.form.get('content', '')
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(content + '\n')
    return '保存成功'

if __name__ == '__main__':
    app.run()
