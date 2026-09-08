---
name: agent-notes
description: Maintain durable engineering decision records in .agents/notes during non-trivial codebase changes. Use for architecture, public API or protocol, cross-module responsibility, persistence, security, infrastructure, testing-strategy, or important workflow decisions; skip mechanical edits, ordinary bug fixes, and local refactors that introduce no durable tradeoff.
---

# Agent Notes

记录重要工程选择存在的原因、被放弃的方案、产生的后果及验证方式。Note 是代码和当前文档的补充，不是任务日志、实施计划，也不是每次变更的摘要。

## 首次在仓库中使用

如果 `.agents/notes/README.md` 或根 `AGENTS.md` 中的触发规则不存在，运行：

```bash
python3 <skill-directory>/scripts/bootstrap.py <repository-root>
```

继续之前检查生成的文件。初始化脚本只做增量修改：不会覆盖已有的 Note 规则文件，并且仅在根规则不存在时插入带标记的规则。如果仓库已有 Agent Notes 约定，应遵循现有约定，不要替换它。

创建或修改 Note 前，阅读 [references/convention.md](references/convention.md)。该文件是分类、文件格式和生命周期迁移规则的事实来源。

## 判断是否需要 Note

当工作涉及架构、公共 API 或协议、跨模块职责、持久化、安全、基础设施、测试策略或重要工程流程，并作出需要长期遵循的选择时，创建或更新 Note。

如果变更只是机械修改、常规依赖升级、局部实现细节、恢复既定行为的普通缺陷修复，或不涉及长期权衡的重构，则不要新建 Note。如果这些修改使现有 implemented Note 中的路径、符号、默认值或机制等事实过时，应更新该 Note。

不确定时，用以下问题判断：未来维护者是否可能因为无法从代码和当前文档中了解理由，而撤销或违背这个选择？如果不会，就不要创建 Note。

## 使用当前有效的决策集合

设计或修改之前，按概念、受影响模块、API 和机制搜索 `proposed/`、`implemented/` 与 `rejected/`，不要只搜索标题。不要把 `archived/` 视为当前权威来源。

- 遵循适用的有效决策。
- 更新 implemented Note 中关于实际实现的事实，但不要改写其原始决策。
- 只有真正出现新决策时才创建 proposed Note。
- 如果新选择推翻或替代旧选择，应在两个 Note 之间互相链接。完全被替代的 implemented Note 应归档；部分被替代的 Note 应保持有效，并说明仍然适用的范围。
- 不要悄悄把一个决策改成它的反面。

## 保持生命周期同步

当决策具体到足以陈述时，在实现之前或实现过程中创建提案。内容应聚焦理由和验收标准，不要叙述工作过程。

任务结束时，根据实际结果调整 Note：

- 已交付：移入 `implemented/`，修改状态，并将提案阶段的章节重写为现在时态的决策、后果和验证结果。
- 已否决：移入 `rejected/`，保留提案背景，并在状态行中填写一行否决原因。
- 尚未解决或只完成一部分：保留 proposed 状态，并说明仍未解决的内容。不要仅仅因为编码工作停止就标记为 implemented。
- 不再适合作为当前指导：将 implemented Note 移入 `archived/`。归档 Note 必须保持冻结；需要替代时创建新的有效 Note，不要修改归档内容。

不要创建集中式索引。通过生命周期与分类路径以及仓库搜索查找 Note。

## 验证

每次创建、修改或移动 Note 后，运行：

```bash
python3 <skill-directory>/scripts/validate.py <repository-root>
```

修复所有报告的结构与格式错误，同时运行仓库原有的验证流程。机械校验无法判断是否遗漏了本应创建的 Note，也无法证明记录的理由真实准确；这些问题需要在审查中确认。
