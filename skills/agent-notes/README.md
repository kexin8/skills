# Agent Notes Skill

用于让 Coding Agent 在非简单工程变更中自动创建和维护 `.agents/notes` 决策记录。

## 安装

以下命令均在本 skills 仓库根目录执行：

```bash
cd /Users/zhengzi/Project/zhengzi/skills
```

### 安装到当前用户

让所有项目都能发现该 skill：

```bash
make install NAME=agent-notes
```

默认创建以下符号链接：

```text
~/.agents/skills/agent-notes
  → /Users/zhengzi/Project/zhengzi/skills/skills/agent-notes
```

### 仅安装到指定项目

将 `<project-root>` 替换为项目的绝对路径：

```bash
make install \
  NAME=agent-notes \
  SKILLS_HOME=<project-root>/.agents/skills
```

例如：

```bash
make install \
  NAME=agent-notes \
  SKILLS_HOME=/Users/zhengzi/Project/my-app/.agents/skills
```

该命令创建指向本仓库 skill 源目录的符号链接；在本仓库更新 skill 后，无需重复安装。

## 初始化项目

安装 skill 后，在目标项目中初始化 Agent Notes 规则：

```bash
python3 skills/agent-notes/scripts/bootstrap.py <project-root>
```

如果不在本 skills 仓库根目录下执行，请使用脚本的绝对路径：

```bash
python3 \
  /Users/zhengzi/Project/zhengzi/skills/skills/agent-notes/scripts/bootstrap.py \
  <project-root>
```

初始化脚本会：

- 创建 `.agents/notes/README.md`；
- 创建 `.agents/notes/AGENTS.md`；
- 在项目根 `AGENTS.md` 中加入 Agent Notes 触发规则；
- 保留已有规则文件，并避免重复插入触发规则。

建议检查脚本生成的文件后再提交。初始化脚本可以安全地重复运行。

## 验证

创建、修改或移动 Agent Note 后运行：

```bash
python3 skills/agent-notes/scripts/validate.py <project-root>
```

也可以使用绝对路径：

```bash
python3 \
  /Users/zhengzi/Project/zhengzi/skills/skills/agent-notes/scripts/validate.py \
  <project-root>
```

验证器检查 Note 的生命周期目录、分类、文件名、状态行和必需章节。它不能判断一项决策是否值得记录，也不能验证决策理由是否准确；这些内容仍需在审查时确认。

## 使用

初始化完成后，新建 Codex 任务即可让项目规则自动触发该 skill。也可以显式调用：

```text
$agent-notes 为这次架构变更创建并维护 Agent Note
```

Skill 的英文入口是 [SKILL.md](SKILL.md)，中文版本是 [SKILL.zh.md](SKILL.zh.md)。详细格式与生命周期规则见 [references/convention.md](references/convention.md)。
