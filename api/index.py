from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# 首页：Python 自己读 index.html 显示
@app.route('/')
def index():
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return html_content

# 提交表单：写数据库
@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form.get('name')
        phone = request.form.get('phone')

        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute('''
        CREATE TABLE IF NOT EXISTS users
        (name TEXT, phone TEXT)
        ''')
        c.execute("INSERT INTO users VALUES (?, ?)", (name, phone))
        conn.commit()
        conn.close()

        return "提交成功！"
    except Exception as e:
        return f"错误：{str(e)}"

if __name__ == '__main__':
    app.run()
