from flask import Flask, request
from supabase import create_client
from datetime import datetime

app = Flask(__name__)

SUPABASE_URL = "https://hvjtxwprbjkmkuonbtec.supabase.co"
SUPABASE_KEY = "sb_publishable_nDCBFBG78Ali6LZrJUvglA_0SV5KSNq"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/', methods=['GET'])
def home():
    return "后端正常运行"

@app.route('/save', methods=['POST'])
def save():
    name = request.form.get("name")
    phone = request.form.get("phone")
    prize = request.form.get("prize")

    supabase.table("prize_records").insert({
        "name": name,
        "phone": phone,
        "award": prize,
        "create_time": datetime.now().isoformat()
    }).execute()

    return "success"

application = app
