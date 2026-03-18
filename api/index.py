from flask import Flask, request
from supabase import create_client
from datetime import datetime

app = Flask(__name__)

# 你的数据库
SUPABASE_URL = "https://hvjtxwprbjkmkuonbtec.supabase.co"
SUPABASE_KEY = "sb_publishable_nDCBFBG78Ali6LZrJUvglA_0SV5KSNq"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# 你前端提交的地址：/api/log
@app.route("/api/log", methods=["POST"])
def log():
    name = request.form.get("name")
    phone = request.form.get("phone")
    email = request.form.get("email")
    prize = request.form.get("prize")

    # 直接存库，啥也不多干
    supabase.table("prize_records").insert({
        "name": name,
        "phone": phone,
        "email": email,
        "award": prize,
        "create_time": datetime.now().isoformat()
    }).execute()

    return "ok"

# Vercel 必须要这个
application = app
