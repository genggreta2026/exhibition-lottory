import random
from datetime import datetime
from supabase import create_client, Client

# 你的 Supabase 信息（已经帮你填好）
SUPABASE_URL = "https://hvjtxwprbjkmkuonbtec.supabase.co"
SUPABASE_KEY = "sb_publishable_nDCBFBG78Ali6LZrJUvglA_0SV5KSNq"

# 连接数据库
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# 奖品设置
PRIZES = ["一等奖", "二等奖", "三等奖", "谢谢参与"]

def draw(user_name, user_phone):
    # 检查手机号是否已经抽过
    res = supabase.table("prize_records").select("*").eq("phone", user_phone).execute()
    
    if len(res.data) > 0:
        return f"手机号 {user_phone} 已经抽过奖，不能重复抽！"

    # 随机抽奖
    result = random.choice(PRIZES)

    # 写入数据库
    supabase.table("prize_records").insert({
        "name": user_name,
        "phone": user_phone,
        "award": result,
        "create_time": datetime.now().isoformat()
    }).execute()

    return f"抽奖成功！姓名：{user_name}，奖品：{result}"

# 测试一下（你可以删掉这行）
if __name__ == "__main__":
    print(draw("测试用户", "13800138000"))
