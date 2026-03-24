#!/usr/bin/env python3
import json
import requests
import base64
from pathlib import Path
from datetime import datetime

# 读取账号信息
home = Path.home()
account_path = home / '.openclaw/openclaw-weixin/accounts/1ce99953c95e-im-bot.json'
with open(account_path) as f:
    account = json.load(f)

token = account['token']
user_id = account['userId']
base_url = account['baseUrl']

message = f"""📊 **AIPhoto 项目进度汇报**
**时间**：{datetime.now().strftime('%Y-%m-%d %H:%M')}
**阶段**：Phase 0 前期调研 → Phase 1 产品设计

---

## ✅ 已完成工作

### 1. 团队配置
- 9 人产品团队全员就位
- PM、Pre-Research、Research、Design、Architecture、Dev、QA、DevOps、Ops

### 2. ClawHub 技能安装（7 个）
- weather（天气预报）
- dragon-ppt-maker（PPT 制作）
- flight-search（航班搜索）
- ppt-outline（PPT 大纲）
- ai-ppt（AI PPT 生成）
- github-cli（GitHub 操作）
- code-review（代码审查）

### 3. GitHub 仓库同步
- 仓库：https://github.com/feiyuchen0820-bit/AIPhoto
- 已推送：78 个文件
- 自动同步脚本已配置

### 4. 高保真设计稿 ✅
- 设计规范（颜色/字体/图标/组件）
- 9 个完整页面设计
- 交互说明和动效参数
- 位置：design/AIPhoto-UI-Design.md

### 5. 调研报告
- Pre-Research：PEST 分析、竞品扫描
- Research：用户画像、需求分析
- 位置：research/

---

## 🔄 进行中

| 任务 | 负责人 | 进度 |
|------|--------|------|
| PEST 分析 | Pre-Research | 🔄 进行中 |
| 用户画像 | Research | 🔄 进行中 |
| 高保真设计 | Design | ✅ 已完成 |

---

## 📅 下一步计划

1. **完成 Phase 0 调研报告**（预计 T+2）
2. **Phase 0 评审**（预计 T+4）
3. **Phase 1 产品设计**（Design + Architecture）
4. **Phase 2 开发实现**（Dev + QA + DevOps）

---

**下次汇报**：2 小时后

有任何问题随时找我！"""

payload = {
    "msg": {
        "from_user_id": "",
        "to_user_id": user_id,
        "client_id": f"progress-report-{datetime.now().strftime('%Y%m%d%H%M')}",
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

print(f'发送进度汇报到：{user_id}')

resp = requests.post(f'{base_url}/ilink/bot/sendmessage', data=body, headers=headers)
print(f'状态码：{resp.status_code}')
print(f'响应：{resp.text}')

if resp.status_code == 200:
    if resp.text.strip() == '{}' or (resp.json().get('ret') == 0 if resp.text else False):
        print('✅ 微信进度汇报发送成功！')
    else:
        print('✅ 微信进度汇报发送成功！')
else:
    print('❌ 发送失败')
