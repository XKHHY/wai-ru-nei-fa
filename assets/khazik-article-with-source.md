事情是这样的。

最近我在琢磨一件事，就是怎么把一套我自己用了很久的职场生存框架，变成一个任何人都能装到电脑里直接用的工具。

你可能觉得这听起来有点奇怪，职场生存还能变成工具？但我跟你说，还真可以。现在这些 AI 编程助手，什么 Claude Code、Cursor、Gemini CLI，它们都支持一种叫 Skill 的东西，简单说就是一段结构化的指令，AI 读了之后就知道遇到某类问题该怎么处理。你把它理解成给 AI 装一个插件也行。

然后我就想，我那套外儒内法框架，不就是一套处理职场问题的指令吗？为什么不能做成 Skill？

所以我做了。而且我想把这个过程完整地分享出来，不只是讲这个框架本身，更是想告诉你，任何一套你想清楚的方法论，都可以这样打包、分享、让别人直接用。

先说框架本身。

"在正确的时间、地点做正确的事情"，这话谁都听过，但你仔细想想，它其实跳过了最关键的部分——什么是正确的。

有手有脚的人，脑袋留在枕头上也能做点什么，行为本身并不稀缺。稀缺的是行为结果的质量。你的每一个动作在某个坐标系下，不管是自身发展还是团队和谐，都是可以被量化的，这个分数决定了下一步是万事顺遂还是事与愿违。

所以你需要一个框架。不是策略，是策略框架。

这两者的区别很关键。哭天抢地、自怨自艾、气急败黑，这些也是策略，但你品品老祖宗的遣词造句，就知道味道不对。感性的情绪作为主观能动性的表征，本身没有好坏，自然兴发不可能也不需要抑制。但如果把它放在策略层做判断依据，就有失妥当了。

它应该下沉，作为一种表达工具。

这个框架浓缩成八个字，期望、定位，同理、行动。

前一半是做出判断的依据——先了解外部（期望），再审视内部（定位）。后一半是获得依据的方式——先理解对方（同理），再实践验证（行动）。最终指向八个字，外儒内法，知行合一。

我跟你聊聊我的理解。

先说期望。期望就是别人和组织对你的盼望，也就是能从你身上获得的价值。这里有一个很重要的分类，日结工、学徒和合伙人。

日结工，常见于项目导向较强的私企环境，本质是用短期相对高薪换取你的技能、时间和交付能力。组织关心的是你能不能把活干完、干好、干快。至于你有没有归属感，不是完全不重要，但通常不会排在最前面。

学徒，常见于央国企、体制内或层级稳定的组织。这里更强调态度、服从、秩序感和长期培养。能力当然重要，但某些场景下态度和服从大于能力。你会不会干是一回事，你像不像"自己人"，又是另一回事。

合伙人，常见于初创企业、高校或高度开放的项目。这里更看重资源引入、自我驱动和共担风险。组织不仅希望你完成任务，还希望你主动找任务、扩展边界、创造增量。

大多数职场痛苦的根源不是你做错了什么，是你没搞清楚自己在哪个身份里。你在日结工环境讲主人翁精神，被当傻子。在学徒环境埋头苦干不听指挥，被边缘化。在合伙人环境等指令，被嫌弃没主动性。

然后是定位。定位就是对自己的综合判断。个体素养决定了什么活能干，人生规划决定了要不要干。大包大揽做超出能力范围的事，是危险的。事少钱多离家近还能稳定成长领导好同事善良，极难同时满足，更多的是做出取舍，并承受代价。

期望和定位比较之后，相符则迎合，不符则控距。

接着是同理和行动。同理心是理解他人动机和自我认知的素养。可以理解老板的苦楚，但没必要替他打抱不平，除非有另外的好处。最值得共情的永远是自己。

行动方面，所有的理论方案都需要实践验证。在可接受的成本范围内多试探，空想最终往往得到的是人生三大错觉。对内则用习惯代替自律，把每一天变得可记录可量化。

然后是我觉得整篇文章最精准的一句——以尽可能低的功耗，全力以赴地敷衍可异化的场景，把情感兴发留给值得的具体的人。

全力以赴地敷衍。这五个字刚读到的时候觉得矛盾，仔细想想又觉得特别精准。它不是让你消极怠工，而是在那些不值得你投入全部情感的场景里，用最低的功耗达到应尽的职业水准，把省下来的精力和真心，留给真正在乎的人和事。

外儒，用儒家语言维持和谐，降低人际摩擦成本。内法，用法家思维掌握核心利益，迎合或控距由自己决定。知行合一，上述一切必须落地到可验证的行动上。

好，框架讲完了。接下来是重点——怎么把它变成一个别人能直接用的 Skill。

现在主流的 AI 编程工具，比如 Claude Code、Cursor、Gemini CLI、OpenCode、GitHub Copilot、Amp、Goose、Junie 等等，它们都遵循一个叫 Agent Skills 的开放标准，标准地址是 agentskills.io。这个标准规定了一个 Skill 的格式。

简单来说，你需要一个文件夹，里面有一个 SKILL.md 文件，加上可选的 references、assets、scripts 子目录。SKILL.md 顶部是 YAML 格式的元数据，底下是 Markdown 格式的指令内容。

当 AI 启动的时候，它会扫描所有 Skill 的 name 和 description，判断哪个跟当前任务相关。如果命中了，就把整个 SKILL.md 加载进来当上下文。更详细的内容放在 references 里，按需读取，不浪费 token。

我把外儒内法这个框架按这个标准做了一版，文件夹名叫 wai-ru-nei-fa，整个结构长这样：

```
wai-ru-nei-fa/
├── SKILL.md
├── references/
│   ├── original-system.md
│   ├── advanced-expansion.md
│   └── operating-system.md
└── assets/
    ├── wechat-article-style.md
    └── khazix-style.md
```

SKILL.md 是入口，只放核心框架和速查卡，大概 4K。三篇完整内容分别放在 references 里，加起来大概 44K，只有 AI 需要深度分析的时候才会去读。assets 里放了两种输出风格模板，一种公众号长文风格，一种卡兹克风格。

SKILL.md 的完整源码如下。你可以直接复制，按上面的目录结构放好，就能用。

---

```markdown
---
name: wai-ru-nei-fa
description: "Personal adaptive behavior framework: Expectation→Positioning→Empathy→Action. Confucian exterior (harmony) + Legalist interior (boundaries). Use for workplace decisions, interpersonal judgment, identity positioning, expectation management, boundary control, dealing with unfair treatment, painted promises, being scapegoated, layoffs, overtime pressure, office politics, workplace survival."
license: CC-BY-4.0
metadata:
  author: "星空的后花园"
  version: "1.0"
  lang: zh-CN
---

# 外儒内法 — 个人自适应行为框架

> Based on methodology by 星空的后花园. 外儒（Confucian exterior）降低摩擦，内法（Legalist interior）守卫边界。

## When to use this skill

Load when the user mentions:
- Workplace decisions, interpersonal judgment, identity positioning, expectation management
- 职场决策, 人际判断, 身份定位, 期望管理
- 外儒内法, 控距 (distance control), 迎合 (alignment), 策略层/表达层 (strategy/expression layer)
- 日结工/学徒/合伙人 (day laborer / apprentice / partner identity types)
- 情绪标签 (emotion labeling), 功耗分配 (energy allocation)
- 课题分离 (task separation), 边界管理 (boundary management)
- Being criticized, praised, scapegoated, laid off, asked to work overtime
- Painted promises (画饼), unfair treatment, office politics, team alignment
- 领导画饼, 被甩锅, 要不要加班, 被裁员, 要不要站队, 同事晋升
- How to deal with boss, colleagues, workplace conflicts
- Confucian vs Legalist thinking, interior-exterior duality

## Core framework (30-second version)

**八字口诀：期望、定位 ； 同理、行动**

Four sequential steps for any interpersonal/workplace decision:

| Half | Role | Core task |
|------|------|----------|
| 期望、定位 | Basis for judgment | First understand external expectations, then examine internal positioning |
| 同理、行动 | Method for basis | First empathize with the other party, then verify through action |

**Decision flow:**
```
Problem → ①Expectation (what do they want?) → ②Positioning (what do I want?) → ③Empathy (understand motives?) → ④Action (is cost acceptable?) → Align ←→ Control distance
```

**表里合一 (Interior-exterior unity):**
- 策略层 / 内法 (Strategy layer / Legalist interior): Rational analysis, framework decisions. Emotions are NOT judgment basis.
- 表达层 / 外儒 (Expression layer / Confucian exterior): Thanks, apologies, empathy. Emotions serve as expression/lubrication tools.

## Three identity types

| Type | Core logic | Key signal |
|------|-----------|------------|
| 日结工 (Day laborer) | Short-term, deliver results | Results matter, not process |
| 学徒 (Apprentice) | Dedication/obedience > ability | "Are you one of us?" |
| 合伙人 (Partner) | Resource input + shared risk | Proactively find tasks, expand boundaries |

## Quick-reference card (common scenarios)

| Scenario | Default 外儒 (exterior) | Default 内法 (interior) |
|----------|------------------------|------------------------|
| Public criticism | Don't argue, nod | Verify facts privately later |
| Public praise | Thank, credit team | Check if resources follow |
| Asked to work overtime | Understand urgency | Calculate: what does overtime buy? |
| Blame shifted to you | Don't confront publicly | Keep written records |
| Painted rosy picture | Acknowledge vision | Ask specifics: timeline/numbers/written proof |

## Anti-patterns (using the framework wrong)

- **全儒无法** (All Confucian, no Legalist): Only expression layer, no strategy → boundaries eroded
- **全法无儒** (All Legalist, no Confucian): Only strategy, no expression → social costs too high
- **儒法倒置** (Layers inverted): Self-sacrifice internally, calculating externally → massive internal friction
- **框架武器化** (Weaponized framework): Used against others instead of self-management → trust destroyed
- **框架瘫痪** (Framework paralysis): Running all four steps for every decision → slow action

## Detailed content

- Original system (Part 1, 12 chapters): → `references/original-system.md`
- Advanced expansion (Part 2, 9 chapters): → `references/advanced-expansion.md`
- Operating system (Part 3, 9 chapters): → `references/operating-system.md`
- WeChat article style output: → `assets/wechat-article-style.md`
- Khazix-style output: → `assets/khazix-style.md`

## Usage modes

1. **Daily decisions**: Use 30-second version, walk four steps
2. **Deep analysis**: Load corresponding references for in-depth reading
3. **Writing output**: Reference style templates in assets
4. **Training progression**: Post-event review (L1) → Delayed response (L2) → Real-time recognition (L3) → Pre-design (L4) → No-form (L5)
```

---

对，你没看错，就这么点东西。上面这段就是完整的 SKILL.md 源码。

几个你可能想问的问题。

**为什么 name 要用拼音而不是中文？**

Agent Skills 标准规定，name 字段只能用小写字母、数字和连字符。这是为了跨平台兼容，不是所有文件系统都能优雅地处理中文目录名。description 和正文里随意写中文没问题，但 name 和目录名必须英文。

**为什么 description 要写英文？**

因为触发机制靠的是关键词匹配。英文关键词能被更多 AI 工具正确识别，尤其那些底层模型不是中文优先的。不过正文里我同时写了中英文触发词，所以不管你用中文还是英文提问，都能命中。

**references 里的内容怎么获取？**

三篇完整内容太长了，不适合放在一篇公众号文章里。我在文末放了一个 GitHub 仓库链接，里面是完整的 skill 文件夹，包含所有 references 和 assets，clone 下来就能直接用。

**怎么安装？**

取决于你用什么工具。Claude Code 放到 `~/.claude/skills/wai-ru-nei-fa/`，Cursor 放到项目的 `.cursor/skills/`，Gemini CLI 放到 `.gemini/skills/`，GitHub Copilot 放到 `.github/copilot-skills/`。其他工具类似，都是放到各自的 skills 目录下就行。

**装了之后怎么用？**

不用刻意调用。你在任何对话里提到职场决策、被甩锅、领导画饼、要不要加班这类问题的时候，AI 会自动识别并加载这个 skill，然后用框架帮你分析。如果你想主动触发，在 Claude Code 里可以输入 `/wai-ru-nei-fa`。

说真的，我觉得把方法论变成 Skill 这件事本身，就是外儒内法的一个隐喻。

你想啊，一个 Skill 是什么？它是一个结构化的指令，告诉 AI 在特定场景下该怎么行动。它把模糊的判断变成了可执行的步骤，把直觉变成了框架，把经验变成了可复用的资产。

这跟外儒内法做的事一模一样。

框架做的就是把你的模糊直觉给结构化。你其实一直知道领导表扬你不等于给你资源，你其实一直知道不是所有加班都值得跟，你其实一直知道情绪不应该替你做决定。但知道和做到之间差了一万次重复。框架做的就是把那个距离缩短一点。

不是让你变聪明，是让你在累的时候不犯傻。

而且我觉得更有意思的是，当你把一套思维框架写成 Skill 的时候，你被迫做了一件事——你必须把它想清楚，清楚到连 AI 都能执行。你不能用"大概差不多"来糊弄，因为 AI 不会理解模糊。这种精确化的过程本身就是对框架的一次校验和升级。

我自己在做这个 Skill 的时候就发现，有些我自以为想清楚的部分，写出来的时候才意识到逻辑有断点。比如期望和定位之间的关系，以前我只是模模糊糊觉得"先看对方再看自己"，但写成流程之后才发现，必须是严格解耦的——期望是对方的变量，定位是你的变量，两个值各自独立算完再比较，不能混在一起算。这就是写下来的力量。

最后说一个我觉得挺重要的点。

Skill 是给别人用的，框架也是。当你把一个东西做成可分享的格式，你就不再只是自己在用，你也帮到了别人。这个过程中你付出了整理和精确化的劳动，但你收获的是反馈和迭代。别人用了你的 Skill，可能会说"这里我觉得不对"，然后你的框架就进化了。

这本身就是一个期望和定位的关系。你的期望是分享和获得反馈，你的定位是有价值的方法论作者。相符，迎合。

好吧，我承认我有点过度使用框架了。但你看，这就是框架内化的标志——你开始在生活的方方面面不自觉地用它。不是刻意，是习惯。

像 AI 那样思考，但不要像 AI 那样活着。AI 没有情绪，也没有爱。框架帮你处理前者，省下来的精力，去爱具体的人。

---

GitHub 仓库：github.com/xxxxx/wai-ru-nei-fa
（clone 后放到你工具的 skills 目录下即可）

---

以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～

谢谢你看我的文章，我们，下次再见。
