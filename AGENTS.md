# Repository Instructions

本仓库维护个人 AI skills。修改时遵循以下规则。

## Scope

- Skill 位于 `skills/<skill-name>/`，必需入口为 `SKILL.md`。
- 不要把仓库级文档、构建逻辑或临时文件放进单个 skill。
- 保留用户已有内容；不要顺手重写无关 skill。

## Skill authoring

- 名称必须匹配 `^[a-z0-9]+(?:-[a-z0-9]+)*$`，且少于 64 个字符。
- `SKILL.md` 的 YAML frontmatter 必须包含且至少包含有效的 `name` 与 `description`；保留已有且受支持的其他字段。
- `description` 应准确描述能力与触发条件。相似能力容易误触发时，补充必要边界。
- 假设 AI 已具备通用能力，只记录会改变决策、提高可靠性或表达真实业务约束的信息。
- 保持渐进披露：共享规则写在 `SKILL.md`，长篇或条件性内容写入 `references/`，并从入口明确说明何时读取。
- 只在有实际用途时创建 `agents/`、`scripts/`、`references/`、`assets/`。不要保留占位文件或示例内容。
- `agents/openai.yaml` 中字符串使用引号；`default_prompt` 必须显式包含 `$skill-name`。
- 默认允许隐式调用。仅在用户明确要求 explicit-only 时设置 `policy.allow_implicit_invocation: false`。

## Verification

- 完成修改后运行 `make validate`。
- 新增或修改的脚本必须实际执行，至少验证正常路径和关键失败路径。
- 检查所有 reference 都能从 `SKILL.md` 或相关资料被发现，且没有重复维护同一规则。
- 不用只匹配标题或固定措辞的脆弱测试代替行为验证。

