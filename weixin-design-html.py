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

message = """✅ **设计文档 HTML 版本已生成！**

之前 Markdown 格式在 GitHub Pages 无法直接预览，现已转换为 HTML 格式。

---

## 📄 设计文档访问地址

**HTML 版本（推荐）：**
https://feiyuchen0820-bit.github.io/AIPhoto/design/AIPhoto-UI-Design.html

**Markdown 版本（源码）：**
https://feiyuchen0820-bit.github.io/AIPhoto/design/AIPhoto-UI-Design.md

---

## 📋 设计文档内容

### 1. 设计规范
- 颜色系统（主色/辅助色/功能色/中性色/渐变）
- 字体系统（7 级字号）
- 图标规范（24px 网格）
- 组件库（按钮/输入框/滑块/开关/选择器）

### 2. 启动页/引导页
- 3 屏设计（欢迎页、功能亮点、开始使用）
- 渐变背景、插画区域、分页指示器

### 3. 首页
- 搜索框、Banner 轮播
- 8 功能网格入口
- 最近项目横向滚动
- 底部 4 Tab 导航

### 4. 图片编辑页（核心）
- 顶部工具栏
- 图片预览区（支持手势）
- 工具分类 Tab
- 工具选项横向滚动

### 5. 滤镜选择页
- 预览 + 强度滑块
- 6 分类 Tab（推荐/胶片/复古/清新/电影/黑白）
- 滤镜卡片网格

### 6. 美颜调节页
- 8 美颜项目（磨皮/美白/瘦脸/大眼等）
- 强度调节面板
- 模式切换

### 7. 拼图编辑页
- 模板/自由拼图切换
- 画布比例选择
- 模板网格（2-9 格 + 自由）

### 8. 个人中心页
- 用户信息卡片
- VIP 入口
- 我的服务、通用设置、其他设置

### 9. 交互说明
- 页面跳转流程图
- 手势操作表（图片/列表/调节）
- 动效设计（转场/按钮/加载/反馈）

---

**设计风格：** 现代简约、年轻化、活力感
**主色调：** 活力紫 #7C5CFF + 渐变粉 #FF6B9D

点击链接即可查看完整设计文档！🎨"""

payload = {
    "msg": {
        "from_user_id": "",
        "to_user_id": user_id,
        "client_id": f"design-html-{datetime.now().strftime('%Y%m%d%H%M')}",
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
