# 产品全生命周期 AI 团队配置

## 团队概述

本团队负责产品从 0 到 1 的全生命周期管理，由 8 个专业 AI agent 组成，覆盖产品定义、设计、开发、测试、上线、运营各阶段。

## 团队架构

```
┌─────────────────────────────────────────────────────────────┐
│                    Project Manager Agent                     │
│                    (项目统筹 & 风险管理)                      │
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│    Pre-       │    │  Architecture │    │  Development  │
│   Research    │    │     Agent     │    │     Agent     │
│    Agent      │    │               │    │               │
│ (前期调研师)   │    │  (技术架构)    │    │  (代码实现)    │
└───────────────┘    └───────────────┘    └───────────────┘
        │                     │                     │
        ▼                     ▼                     ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│   Product     │    │      QA       │    │    DevOps     │
│   Research    │    │    Agent      │    │    Agent      │
│    Agent      │    │   (测试 QA)    │    │  (上线部署)    │
│ (市场调研)    │    │               │    │               │
└───────────────┘    └───────────────┘    └───────────────┘
        │                     │
        ▼                     ▼
┌───────────────┐    ┌───────────────┐
│   Product     │    │  Operations   │
│   Design      │    │    Agent      │
│    Agent      │    │  (运营追踪)    │
│  (产品设计)    │    │               │
└───────────────┘    └───────────────┘
```

## Agent 列表

| Agent | 职责 | 输入 | 输出 |
|-------|------|------|------|
| `pm-agent` | 项目统筹、进度追踪、风险管理 | 所有阶段状态 | 项目报告、风险预警 |
| `pre-research-agent` | 前期可行性调研、立项建议 | 产品想法 | 可行性报告、立项建议 |
| `research-agent` | 市场调研、竞品分析、用户需求 | 产品方向 | 调研报告、用户画像 |
| `design-agent` | PRD 撰写、功能设计、原型思路 | 调研结果 | PRD 文档、功能列表 |
| `architecture-agent` | 技术选型、系统架构、API 设计 | PRD 文档 | 架构文档、API 规范 |
| `dev-agent` | 代码生成、Code Review、单元测试 | 架构文档 | 代码、测试用例 |
| `qa-agent` | 测试计划、Bug 追踪、性能测试 | 代码 + 需求 | 测试报告、Bug 列表 |
| `devops-agent` | CI/CD、发布计划、监控配置 | 测试通过版本 | 部署包、监控配置 |
| `ops-agent` | 数据分析、用户反馈、迭代规划 | 上线产品 | 运营报告、迭代建议 |

## 工作流程阶段

```
[Phase 1: 产品定义] → [Phase 2: 产品设计] → [Phase 3: 技术架构]
         ↓                    ↓                    ↓
   research-agent       design-agent       architecture-agent
         │                    │                    │
         └────────────────────┼────────────────────┘
                              ↓
[Phase 6: 上线部署] ← [Phase 5: 测试 QA] ← [Phase 4: 开发实现]
         ↓                    ↓                    ↓
    devops-agent          qa-agent            dev-agent
         │
         ↓
[Phase 7: 运营追踪] → [Phase 8: 迭代规划] → (回到 Phase 2 或 3)
         ↓
    ops-agent
```

## 协作协议

### 1. 阶段流转规则
- 每个阶段完成后，负责 Agent 必须生成**交付物清单**
- 下一阶段 Agent 必须确认收到交付物后才能开始工作
- PM Agent 负责审批阶段流转

### 2. 通信机制
- 所有 Agent 通过共享文件系统交换信息
- 每个 Agent 在 `teams/product-team/state/` 下维护状态文件
- 重要决策需要 PM Agent 确认

### 3. 版本控制
- 所有交付物必须有版本号
- 重大变更需要创建变更日志
- 回滚策略由 DevOps Agent 维护

## 状态管理

团队状态文件位于：`teams/product-team/state/`

- `current-phase.md` - 当前阶段
- `phase-history.md` - 阶段流转历史
- `blockers.md` - 当前阻塞问题
- `decisions.md` - 重要决策记录

## 使用方式

### 启动新產品项目
```bash
# 1. 创建项目目录
mkdir -p projects/{项目名}

# 2. 初始化项目配置
cp teams/product-team/templates/project-init.md projects/{项目名}/config.md

# 3. 启动 PM Agent 开始流程
```

### 查询项目状态
```bash
# 查看当前阶段
cat teams/product-team/state/current-phase.md

# 查看项目进度
cat projects/{项目名}/status.md
```

## 配置说明

- **工作模式**: 支持串行（默认）和并行（独立任务）
- **审批机制**: 关键节点需要人工确认
- **通知机制**: 阶段完成/阻塞时发送通知
