# 产品全生命周期 AI 团队 - 使用指南

## 快速开始

### 1. 启动新项目

```bash
# 进入工作区
cd /home/admin/openclaw/workspace

# 创建项目目录
mkdir -p projects/{你的产品名}

# 复制项目初始化模板
cp teams/product-team/templates/project-init.md projects/{你的产品名}/config.md
```

### 2. 配置项目

编辑 `projects/{你的产品名}/config.md`，填写：
- 产品名称
- 产品方向
- 目标用户
- 预期上线时间

### 3. 启动团队

向 PM Agent 发送消息启动项目：

```
启动新项目：{产品名}
产品方向：{一句话描述}
目标用户：{描述}
预期上线：{时间}

请开始 Phase 1：产品定义
```

---

## 团队架构

本团队包含 **9 个专业 AI Agent**：

| Agent | 职责 | 阶段 |
|-------|------|------|
| PM Agent | 项目统筹、进度追踪、风险管理 | 全周期 |
| **Pre-Research Agent** | **前期可行性调研、立项建议** | **Phase 0** |
| Research Agent | 市场调研、竞品分析、用户画像 | Phase 1 |
| Design Agent | PRD 撰写、功能设计 | Phase 2 |
| Architecture Agent | 技术选型、架构设计 | Phase 3 |
| Dev Agent | 代码实现、单元测试 | Phase 4 |
| QA Agent | 测试计划、Bug 追踪 | Phase 5 |
| DevOps Agent | CI/CD、部署上线 | Phase 6 |
| Ops Agent | 数据分析、迭代规划 | Phase 7-8 |

---

## 工作流程

```
Phase 0: 前期调研 → Phase 0.5: 立项决策 → Phase 1: 产品定义 → Phase 2: 产品设计
                                                  ↓
Phase 8: 迭代规划 ← Phase 7: 运营追踪 ← Phase 6: 上线部署 ← Phase 5: 测试 QA ← Phase 4: 开发实现 ← Phase 3: 技术架构
```

每个阶段完成后，PM Agent 会进行评审，批准后才能进入下一阶段。

---

## 文档模板

团队提供以下标准模板：

| 模板 | 用途 | 路径 |
|------|------|------|
| 可行性报告模板 | 前期可行性调研 | `templates/feasibility-report-template.md` |
| 项目初始化模板 | 项目配置 | `templates/project-init.md` |
| PRD 模板 | 产品需求文档 | `templates/prd-template.md` |
| 架构模板 | 技术架构文档 | `templates/architecture-template.md` |
| 测试报告模板 | 测试总结 | `templates/test-report-template.md` |
| 运营报告模板 | 运营分析 | `templates/ops-report-template.md` |

---

## 状态管理

项目状态文件位于 `projects/{项目名}/`：

- `config.md` - 项目配置
- `status.md` - 当前状态
- `decisions.md` - 重要决策
- `blockers.md` - 阻塞问题

---

## 沟通方式

### 与 PM Agent 沟通
- 项目启动、暂停、终止
- 审批请求
- 资源协调

### 与各专业 Agent 沟通
- 直接提问（如"竞品分析进展如何？"）
- 请求特定文档（如"请输出 PRD"）

---

## 最佳实践

### 1. 明确输入
启动每个阶段前，确保上一阶段交付物已完成并评审通过。

### 2. 及时评审
阶段完成后 24 小时内完成评审，避免阻塞。

### 3. 文档先行
任何重要决策先形成文档，再执行。

### 4. 风险早报
发现风险立即记录到 `blockers.md`，不要等到阶段结束。

---

## 常见问题

### Q: 如何并行多个项目？
A: 每个项目独立目录，PM Agent 会分别管理。可以在项目配置中指定优先级。

### Q: 如何跳过某个阶段？
A: 需要 PM Agent 审批，说明跳过理由和风险评估。

### Q: 如何添加自定义 Agent？
A: 在 `agents/` 目录创建新的 Agent 配置文件，在 `team-config.md` 中注册。

---

## 文件结构

```
teams/product-team/
├── team-config.md          # 团队配置
├── README.md               # 使用指南
├── agents/                 # 9 个 Agent 配置
│   ├── pm-agent.md
│   ├── pre-research-agent.md   # 前期调研师
│   ├── research-agent.md
│   ├── design-agent.md
│   ├── architecture-agent.md
│   ├── dev-agent.md
│   ├── qa-agent.md
│   ├── devops-agent.md
│   └── ops-agent.md
├── workflows/
│   └── lifecycle-workflow.md   # 阶段流转规则
└── templates/              # 6 个标准模板
    ├── feasibility-report-template.md
    ├── project-init.md
    ├── prd-template.md
    ├── architecture-template.md
    ├── test-report-template.md
    └── ops-report-template.md
```

---

## 版本

- 团队版本：v1.0
- 创建日期：2026-03-23
- 最后更新：2026-03-23
