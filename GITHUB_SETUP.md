# GitHub 同步配置指南

## 目标
将 AIPhoto 项目的所有文档和进度汇报同步到 GitHub 仓库。

## 步骤

### 1. 创建 GitHub 仓库

在 GitHub 上创建新仓库：
- 仓库名：`aiphoto-product-team`
- 可见性：公开（Public）
- 初始化：不要添加 README/.gitignore

### 2. 配置认证

创建 GitHub Personal Access Token：
1. 访问 https://github.com/settings/tokens
2. 点击 "Generate new token (classic)"
3. 选择权限：`repo` (Full control of private repositories)
4. 生成后复制 token

### 3. 配置本地 Git

```bash
# 设置 token（替换 YOUR_TOKEN）
git remote add origin https://YOUR_TOKEN@github.com/YOUR_USERNAME/aiphoto-product-team.git

# 或者使用 git credential 存储
git config --global credential.helper store
```

### 4. 首次推送

```bash
cd ~/openclaw/workspace
git branch -M main
git add -A
git commit -m "Initial commit: AIPhoto project setup"
git push -u origin main
```

### 5. 目录结构

```
aiphoto-product-team/
├── progress/           # 进度汇报
│   └── 2026-03-24.md   # 按日期记录
├── docs/               # 项目文档
│   ├── prd.md          # 产品需求文档
│   ├── research/       # 调研报告
│   ├── design/         # 设计稿
│   └── architecture/   # 技术架构
├── skills/             # 安装的 ClawHub 技能
└── memory/             # 会议记录和决策
```

### 6. 自动同步

配置 cron job 每次汇报后自动推送：
```bash
# 添加到 crontab
0 */2 * * * cd ~/openclaw/workspace && git add -A && git commit -m "Auto-sync: $(date)" && git push origin main
```

## 需要提供的信息

请提供以下信息完成配置：
1. GitHub 用户名
2. Personal Access Token
3. 仓库 URL
