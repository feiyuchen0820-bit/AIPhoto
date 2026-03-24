#!/usr/bin/env python3
import json
import requests
import base64
from pathlib import Path
from datetime import datetime

home = Path.home()
account_path = home / '.openclaw/openclaw-weixin/accounts/1ce99953c95e-im-bot.json'
with open(account_path) as f:
    account = json.load(f)

token = account['token']
user_id = account['userId']
base_url = account['baseUrl']

message = """✅ **GitHub Pages 主页已更新！**

**主页地址：**
https://feiyuchen0820-bit.github.io/AIPhoto/

---

## 📄 页面内容

### 1️⃣ 进度报告
📊 实时项目进度追踪
👉 reports/01-Progress-Reports.html

### 2️⃣ 设计文档 ✅
🎨 高保真 UI/UX 设计
👉 design/AIPhoto-UI-Design.md

包含：
- 设计规范（颜色/字体/图标/组件）
- 9 个完整页面设计（启动页、首页、编辑页等）
- 交互说明和动效参数
- 主色调：活力紫 #7C5CFF + 渐变粉 #FF6B9D

### 3️⃣ 调研报告 🔄
📝 市场调研、用户分析、竞品分析
👉 research/

### 4️⃣ 产品团队
👥 9 人团队配置
👉 teams/product-team/

### 5️⃣ ClawHub 技能
🛠️ 7 个已安装技能
👉 skills/

---

## 🔗 快速访问

**主页：** https://feiyuchen0820-bit.github.io/AIPhoto/

**设计文档：**
https://feiyuchen0820-bit.github.io/AIPhoto/design/AIPhoto-UI-Design.md

**进度报告：**
https://feiyuchen0820-bit.github.io/AIPhoto/reports/01-Progress-Reports.html

---

页面已更新，可以立即访问！🚀"""

payload = {
    "msg": {
        "from_user_id": "",
        "to_user_id": user_id,
        "client_id": f"index-update-{datetime.now().strftime('%Y%m%d%H%M')}",
        "message_type": 2,
        "message_state": 2,
        "item_list": [{
            "type": 1,
            "text_item": {"text": message}
        }]
    },
    "base_info": {"channel_version": "2.0.1"}
}

body = json.dumps(payload)
uin = base64.b64encode(str(int.from_bytes(base64.b64decode('AAAA'), 'big')).encode()).decode()

headers = {
    'Content-Type': 'application/json',
    'AuthorizationType': 'ilink_bot_token',
    'Authorization': f'Bearer {token}',
    'Content-Length': str(len(body.encode('utf-8'))),
    'X-WECHAT-UIN': uin
}

resp = requests.post(f'{base_url}/ilink/bot/sendmessage', data=body, headers=headers)
print(f'状态码：{resp.status_code}')
if resp.status_code == 200:
    print('✅ 微信通知已发送！')
else:
    print('❌ 发送失败')
