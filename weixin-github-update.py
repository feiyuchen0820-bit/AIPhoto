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

message = """✅ **GitHub Pages 已更新！**

**进度报告页面：**
https://feiyuchen0820-bit.github.io/AIPhoto/reports/01-Progress-Reports.html

---

## 📊 页面内容

1. **项目概述** - AIPhoto 产品信息
2. **已完成工作** 
   - 9 人团队配置
   - 7 个 ClawHub 技能
   - GitHub 仓库同步（78 文件）
   - 高保真设计稿
   - 调研报告

3. **微信沟通记录** 💬
   - 我们所有的聊天记录
   - 从微信配置到技能安装
   - 从 GitHub 配置到高保真设计

4. **进行中任务** 🔄
   - PEST 分析
   - 用户画像构建
   - 竞品深度分析

5. **下一步计划** 📅
   - Phase 0-3 时间线

---

## 🔒 安全修复

GitHub Secret Scanning 检测到 token 被提交，已移除敏感信息。

---

**页面 1-2 分钟后完全刷新！**

下次汇报：2 小时后 🕐"""

payload = {
    "msg": {
        "from_user_id": "",
        "to_user_id": user_id,
        "client_id": f"github-update-{datetime.now().strftime('%Y%m%d%H%M')}",
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
print(f'响应：{resp.text}')
if resp.status_code == 200:
    print('✅ GitHub 更新通知已发送！')
else:
    print('❌ 发送失败')
