import random
from datetime import datetime
from supabase import create_client

# 你的信息
SUPABASE_URL = "https://hvjtxwprbjkmkuonbtec.supabase.co"
SUPABASE_KEY = "sb_publishable_nDCBFBG78Ali6LZrJUvglA_0SV5KSNq"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def handler(request):
    # 接收姓名、手机号
    name = request.args.get("name", "")
    phone = request.args.get("phone", "")

    if not name or not phone:
        return {"code": 400, "msg": "请输入姓名和手机号"}

    # 检查是否抽过
    check = supabase.table("prize_records").select("*").eq("phone", phone).execute()
    if check.data:
        return {"code": 201, "msg": "该手机号已抽奖"}

    # 抽奖
    awards = ["一等奖", "二等奖", "三等奖", "谢谢参与"]
    result = random.choice(awards)

    # 写入数据库
    supabase.table("prize_records").insert({
        "name": name,
        "phone": phone,
        "award": result,
        "create_time": datetime.now().isoformat()
    }).execute()

    return {
        "code": 200,
        "msg": "抽奖成功",
        "name": name,
        "award": result
    }
