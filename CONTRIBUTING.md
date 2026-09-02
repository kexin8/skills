# Skill 维护规范

## 新建 skill

1. 运行 `make new NAME=<skill-name>`。
2. 在 `SKILL.md` 中写清能力、触发条件、关键流程和真实约束。
3. 按实际需要添加资源目录；不要保留空目录或占位文件。
4. 运行新增脚本，并执行 `make validate`。

生成器默认创建 `agents/openai.yaml`，用于 UI 展示和默认提示词。如果目标运行环境不需要该文件，可以删除整个 `agents/` 目录。

## `SKILL.md` 写法

文件以 YAML frontmatter 开始：

```yaml
---
name: example-skill
description: Perform a specific capability when the request requires its specialized workflow.
---
```

正文优先回答以下问题：

- 这个 skill 要达成什么结果？
- 哪些选择、约束或领域知识不是模型可以安全推断的？
- 哪些复杂步骤应交给确定性脚本？
- 哪些细节只在特定场景需要，应路由到 reference？
- 哪些操作需要用户明确授权或明确停止条件？

避免写入通用建议、重复的系统规则、对单次失败的过度拟合，以及与能力无关的安装说明或 changelog。

## 可选资源

| 路径 | 使用时机 |
| --- | --- |
| `agents/openai.yaml` | 需要 UI 名称、简介、默认提示词、依赖或调用策略 |
| `scripts/` | 同一逻辑会重复实现，或确定性显著提升可靠性 |
| `references/` | 大段 schema、政策、API 说明或场景专属流程 |
| `assets/` | 会复制或适配到最终输出的模板、图片、字体等 |

Reference 必须从入口说明“何时读取”，而不只是被动列出链接。Asset 不应被当成指令加载。

## 评审清单

- 名称与目录一致，命名合法。
- Description 既容易发现又不会误触发。
- 指令尊重用户选择、授权边界与任务范围。
- 入口足够短，条件性细节已渐进披露。
- 所有文件都有明确用途，没有 scaffold 残留。
- 脚本可执行、失败信息清楚，相关行为已验证。
- `make validate` 通过。

