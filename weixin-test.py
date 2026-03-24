#!/usr/bin/env python3
import json
import requests
import base64
from pathlib import Path

# 读取账号信息
home = Path.home()
account_path = home / '.openclaw/openclaw-weixin/accounts/1ce99953c95e-im-bot.json'
with open(account_path) as f:
    account = json.load(f)

token = account['token']
user_id = account['userId']
base_url = account['baseUrl']

message = """✅ 微信连接成功！

工作安排确认：
📱 沟通：微信私聊（你 ↔ 皮蛋）
👥 团队：我安排 9 个 Agent 干活
⏰ 汇报：每 2 小时同步进度

AIPhoto 项目 - Phase 0 前期调研：
- Pre-Research: PEST 分析、竞品扫描 🔄
- Research: 用户画像、需求分析 🔄

下次汇报：2 小时后

有任何问题随时找我！"""

payload = {
    "msg": {
        "from_user_id": "",
        "to_user_id": user_id,
        "client_id": "openclaw-weixin-test",
        "message_type": 2,
        "message_state": 2,
        "item_list": [{
            "type": 1,
            "text_item": {"text": message}
        }]
    },
    "base_info": {
        "channel_version": "2.0.1"
    }
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

print(f'发送消息到：{user_id}')
print(f'消息内容：{message[:50]}...')
print()

resp = requests.post(f'{base_url}/ilink/bot/sendmessage', data=body, headers=headers)
print(f'状态码：{resp.status_code}')
print(f'响应：{resp.text}')

if resp.status_code == 200:
    try:
        data = resp.json()
        if data.get('ret') == 0 or resp.text == '{}':
            print('✅ 微信消息发送成功！请检查微信！')
        else:
            print(f'❌ 发送失败，错误码：{data.get("ret")}')
    except:
        if resp.text.strip() == '{}':
            print('✅ 微信消息发送成功！请检查微信！')
        else:
            print('❌ 响应解析失败')
else:
    print('❌ 请求失败')
