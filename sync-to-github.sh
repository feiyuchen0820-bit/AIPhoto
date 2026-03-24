#!/bin/bash
# AIPhoto 项目自动同步脚本
# 用法：./sync-to-github.sh [提交信息]

cd /home/admin/openclaw/workspace

# 添加所有变更
git add -A

# 检查是否有变更
if git diff --staged --quiet; then
    echo "✅ 没有变更需要提交"
    exit 0
fi

# 提交
COMMIT_MSG="${1:-Auto-sync: $(date '+%Y-%m-%d %H:%M')}"
git commit -m "$COMMIT_MSG"

# 推送
git push origin main

echo "✅ 同步完成：$COMMIT_MSG"
