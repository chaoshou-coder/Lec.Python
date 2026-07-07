# 重构计划 · 教师使用指南

## 如何使用本计划

这份计划是 **21 天 Python 零基入门到 OOP + 小项目** 的教学蓝图,供教师 1 周内(每天 9 个 45 分钟课时)讲授。

### 每日教学流程

1. 课前:看 `lessonXX/README.md` 与 `slides.md`,把 `slides.md` 补充完整
2. 课中:用 `demo/` 演示;让学员做 `in_class/` 巡场点评
3. 课后:学员做 `homework/`;教师写 `teacher_notes.md`
4. 每周五:做"中型项目"`weekly_projects/weekXX_xxx/`

### 各目录角色

| 目录 | 谁写 | 何时用 |
|---|---|---|
| `slides.md` | 教师可改 | 授课主线(课前备好) |
| `demo/` | 已在前面 7 天填完,后续由 sub-agent 生成 | 演示用 |
| `in_class/` | 已在前面 7 天填完,后续由 sub-agent 生成 | 学员课上写 |
| `homework/` | 已在前面 7 天填完,后续由 sub-agent 生成 | 学员课后写 |
| `assets/` | 教师按需放 | 素材(图片/文本) |
| `mini_project/` | 教师做 | 每 2~3 天的综合项目 |
| `teacher_notes.md` | 教师课后写 | 错题积累 |

### 评分构成

- 当堂小作品 30%(21 次,取最高 10 次)
- 每周中型项目 40%(3 个)
- 期末作品 README + Demo 20%
- 出勤与错题本 10%

### Bug 修复清单(必须修)

见 `summary.md` §3 的"Day01-Day07 原有缺陷修复清单",在新 plan 同步落地时**必须改**。

### 进度追踪

- Day07 阶段测 ≥ 70%
- Day14 阶段测 ≥ 65%
- Day21 期末项目过 7 项验收点

### 参考资料

- `references.md`:外部成熟课程的习题 / 项目 / 教学思路素材库(附 side-agent 并行搜集)
- `../day01/` ~ `../day07_code/`:旧 day01-day07 源码参考(可复用但不要直接拷贝)

### 配合的外部计划文件

`../day7-day7-os-glowing-crystal.md`(.claude/plans/)含本计划的 Context / 阶段验收 / 关键习题示例。

---

## 快速启动清单

- [ ] 把 `lessonXX/slides.md` 每课主题填入
- [ ] 复制 `demo/` 模板到每课的细分知识点文件
- [ ] 根据 `references.md` 补 `in_class/` 和 `homework/` 的 Day08-Day21
- [ ] 为每个 weekly_project 准备验收脚本(`test_week_N.py`)
- [ ] 和程序员同学确认:pytest 环境已装,`python3 -m pytest` 可跑
