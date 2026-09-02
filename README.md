# Personal AI Skills

这个仓库用于维护个人可复用的 AI skills。每个 skill 都是一个独立目录，入口文件为 `SKILL.md`。

## 快速开始

```bash
make new NAME=my-skill
make validate
```

创建后，编辑 `skills/my-skill/SKILL.md`，删除无用说明，并只在确有需要时添加 `scripts/`、`references/` 或 `assets/`。

## 目录结构

```text
.
├── skills/                 # 所有个人 skills
│   └── <skill-name>/
│       ├── SKILL.md        # 必需：元数据与执行说明
│       ├── agents/         # 可选：产品 UI 元数据与调用策略
│       ├── scripts/        # 可选：可重复、确定性的工具脚本
│       ├── references/     # 可选：按需读取的详细资料
│       └── assets/         # 可选：输出中会使用的模板或媒体
├── scripts/                # 仓库维护工具
├── AGENTS.md               # AI 在本仓库工作的规则
└── CONTRIBUTING.md         # 创建与评审规范
```

## 设计原则

- Skill 名称使用小写字母、数字和连字符，目录名与 frontmatter 中的 `name` 一致。
- `description` 同时说明“做什么”和“何时使用”，并避免吸引不相关任务。
- `SKILL.md` 只保留共享流程、关键约束和资料路由；条件性细节放入 `references/`。
- 不预建空目录，不复制通用知识，不添加没有明确用途的占位资源。
- 稳定、重复且需要确定性的操作才写入 `scripts/`，并提供实际验证方式。
- 默认允许自动发现；只有明确需要仅显式调用时，才在 `agents/openai.yaml` 中关闭隐式调用。

更完整的新增、修改和评审要求见 [CONTRIBUTING.md](CONTRIBUTING.md)。

