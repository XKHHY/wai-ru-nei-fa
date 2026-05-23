# 外儒内法 (wai-ru-nei-fa) — 个人自适应行为框架

> 外儒（Confucian exterior）降低摩擦，内法（Legalist interior）守卫边界。

一个 [Agent Skills](https://agentskills.io) 标准格式的职场生存 Skill。装到 Claude Code、Cursor、Gemini CLI、GitHub Copilot 等 AI 编程工具中，遇到职场决策场景时自动触发，用期望→定位→同理→行动四步框架帮你分析判断。

## v3.0 更新

- **生态式思维**：不再每次判断，而是设计环境让同类问题不再出现（eco-mode）
- **场景库扩展**：新增 8 个 AI 时代场景（#13-#20），覆盖 AI 替代焦虑、远程办公边界、代际冲突、副业与职业转型
- **自检工具强化**：30 秒触发器增加"第三方案"检查、周复盘增加趋势列、新增季度 eco-check
- **训练体系升级**：新增 L5 生态式和 L6 无招层级
- **场景集中管理**：新增 `references/scenario-library.md`

## 快速安装

根据你使用的工具，放到对应的 skills 目录：

| 工具 | 安装路径 |
|------|---------|
| Claude Code | `~/.claude/skills/wai-ru-nei-fa/` |
| Cursor | `.cursor/skills/wai-ru-nei-fa/` |
| Gemini CLI | `.gemini/skills/wai-ru-nei-fa/` |
| GitHub Copilot | `.github/copilot-skills/wai-ru-nei-fa/` |
| OpenCode/Crush | `.opencode/skills/wai-ru-nei-fa/` |
| OpenClaw | `~/.openclaw/skills/wai-ru-nei-fa/` |
| Codex | `~/.codex/skills/wai-ru-nei-fa/` |

```bash
# 克隆到临时目录再复制
git clone https://github.com/XKHHY/wai-ru-nei-fa.git /tmp/wai-ru-nei-fa
cp -r /tmp/wai-ru-nei-fa ~/.codex/skills/  # 以 Codex 为例
```

装完不用刻意调用，对话中提到领导画饼、同事甩锅、要不要加班、AI 替代焦虑等话题时，AI 会自动加载。

## 框架核心

**八字口诀：期望、定位 ； 同理、行动**

1. **期望** — 他人/组织对我真正的盼望是什么？（日结工/学徒/合伙人）
2. **定位** — 我的综合判断是什么？（能干什么/要不要干/底线在哪）
3. **同理** — 我能理解对方的动机吗？与我的定位是否背离？
4. **行动** — 成本可接受吗？迎合 / 控距 / 重新定义

**表里合一：**
- 策略层（内法）：理性分析，情绪不作为判断依据
- 表达层（外儒）：感谢抱歉共情，情绪作为润滑工具

**三级演化：**
- 1.0 反应式：遇到问题→走四步→做判断
- 2.0 预判式：预判问题→提前设置语境→问题被消解
- 3.0 生态式：设计环境→他人自发调整→框架接近自我消亡

## 目录结构

```
wai-ru-nei-fa/
├── SKILL.md              # 核心框架 + 执行协议 + 速查卡 + 自检工具
├── references/
│   ├── original-system.md    # 原文体系（12章）
│   ├── advanced-expansion.md # 升华拓展（9章）
│   ├── operating-system.md   # 操作系统（9章 + v3.0升级说明）
│   └── scenario-library.md   # 场景库（20个场景详细分析）
```

## License

CC-BY-4.0 — 原始方法论作者：星空的后花园
