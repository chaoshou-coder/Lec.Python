# 教学计划迭代方案 v2(基于 references.md 研究)

> 调研日期:2026-07-07
> 原始课程计划:`day7-day7-os-glowing-crystal.md`(通常在 `~/.claude/plans/`)
> 本文件 = 迭代提案,**不直接修改**现有 lesson 内容
> 版本控制:`.versions/` 时间戳目录(原始做法)

---

## 1. 调研核心发现(来自 references.md)

### 1.1 市面优秀课程的共性

| 课程 | 关键实践 | 对我们可借鉴的点 |
|---|---|---|
| **MIT 6.0001** | 6 套 PS(Problem Set),项目驱动(猜字/密码/订阅过滤) | 每 3 天一个"综合 PS"代替一道大题 |
| **Harvard CS50P** | 10 周每周 4~6 题 + check50 自动评测 + Final Project 自选 | 引入自动评测脚本(`test_NN.py`) |
| **Python Crash Course** | 500+ 编号练习,两部(基础 + 项目),3 大项目(Space Invaders/数据可视化/Web 应用) | 把练习量从 178 → 300+ |
| **Automate the Boring Stuff** | 34 个真实场景项目(PDF/Excel/爬虫/发邮件) | Day14-Day17 文件批量操作可借鉴 |
| **Think Python 2E** | 每章 3~10 题 + 4 Case Study(龟/单词/Markov/扑克) | 引入"Mini Case Study"作为阶段项目 |
| **小甲鱼** | 98 课,OOP 讲得最深(含元类/描述符),3 大项目 | Day18-Day21 OOP 可延伸到魔术方法 |

### 1.2 当前计划 vs 市场差距

| 维度 | 当前 v1 计划 | 市场最佳实践 | 差距 |
|---|---|---|---|
| **练习总量** | 178 道 | Python Crash Course 500+ | 差 300+ |
| **自动评测** | 无 | MIT/Harvard 用 check50/submit50 | 完全缺失 |
| **调试教学** | 分散在各课 | CS50P 第 1 周专门讲调试 | 需要单独 1 小时 |
| **装饰器** | Day11 仅提 lambda | 廖雪峰/Think Python 都有 1~2 天课时 | 缺失 |
| **生成器/迭代器** | 未涉及 | Think Python Ch18 重点 | 缺失 |
| **正则表达式** | Day17 JSON/CSV 同日 | Automate Ch7 单独 1 天 | 混入 Day17 过密 |
| **单元测试** | Day21 期末提一下 | MIT/Harvard 每 PS 都带测试 | 薄弱 |
| **抽象类(ABC)** | Day20 仅提接口 | PyNative OOP Ex18 单独练习 | 薄弱 |
| **日志模块** | 未涉及 | Automate Ch11 单独章节 | 缺失 |
| **阶段项目数量** | 5 mini + 3 weekly | MIT 6 PS + Harvard 10 周作业 | 密度够但缺"真实场景" |

---

## 2. 迭代 v2 方案(建议)

### 2.1 方案 A:保守迭代(不调整 21 天骨架,只填充缺口)

**适用**:已有学员即将按 v1 开课时

| 动作 | 位置 | 工作量 |
|---|---|---|
| 2.1.1 为所有 in_class 题补 `test_NN.py` 自动评测脚本 | `lessonXX/in_class/` | ~178 个 test 文件 |
| 2.1.2 Day17 JSON/CSV 拆为 Day17(文件进阶+正则) + Day18(JSON/CSV),阶段复习顺延至 Day19 |重构 lesson17~19 | 需拆文件 + 调整 README |
| 2.1.3 Day11 追加 2 道装饰器当堂练习 | `lesson11/in_class/` | +2 题 |
| 2.1.4 Day12 追加 2 道生成器当堂练习 | `lesson12/in_class/` | +2 题 |
| 2.1.5 Day16 异常处理尾声追加 1 道日志记录题 | `lesson16/homework/` | +1 题 |
| 2.1.6 Day20 OOP 追加 1 道 ABC 抽象类题 | `lesson20/in_class/` | +1 题 |
| 2.1.7 Day21 期末前插入 1 天 Day20.5("调试 + 单元测试"专项) | 插入 lesson20.5 | 需新目录 |
| 2.1.8 每周五下午安排 30 分钟"错题复盘"固定环节 | 教师执行层面 | 零文件改动 |

**新增总量**:+7 题 + 178 test 脚本 + 调整 3 天目录

---

### 2.2 方案 B:结构迭代(重新排布 21 天)

**适用**:第二轮招生或暑假重装时

| Day | 主题 | 变化 |
|---|---|---|
| 01-07 | 同 v1 | 不变 |
| 08 | 字符串提升 | 同 v1 |
| 09 | 列表进阶 | 同 v1 |
| 10 | 函数入门 | 同 v1 |
| 11 | 函数进阶 + 装饰器 | 新增装饰器(2 题) |
| 12 | 生成器 / 迭代器 / 递归 | 新增生成器(3 题) |
| 13 | 文件操作基础 | 同 v1 |
| 14 | 文件操作进阶 + os + 正则 | 新增正则(3 题) |
| 15 | JSON + CSV | 同 v1 |
| 16 | 异常处理 + 日志 | 新增日志(2 题) |
| 17 | 阶段复习② + 中型项目 | 同 v1 |
| 18 | OOP 封装 + 魔术方法 | 新增 `__call__`/`__len__`/`__add__` |
| 19 | OOP 继承 + 多态 + ABC | 新增 ABC 抽象类 |
| 20 | 调试专项 + 单元测试 | **全新**(原 Day21 部分拆分) |
| 21 | 期末总复习 + 图书管理系统 v2 答辩 | 同 v1 |

**新增 Day**:Day20(调试+测试专项)

---

### 2.3 方案 C:重练迭代(练习量冲 300+)

**适用**:长期优化,目标是"Python Crash Course 级别"的练习密度

| 动作 | 说明 |
|---|---|
| C.1 每课 in_class 从 6 题扩充至 10 题 | 简单题 + 中等题 + 挑战题 = 5 + 3 + 2 |
| C.2 每课 homework 从 2~3 题扩充至 5 题 | 基础 2 + 进阶 2 + 挑战 1(选做) |
| C.3 引入"每日一题"(LeetCode Easy 级) | 每天课前 5 分钟,单独 `daily/` 目录 |
| C.4 每 3 天安排 1 个 Mini Case Study | MIT/Think Python 风,即用真实小案例 |
| C.5 增设"选做挑战题库" | `lessonXX/challenge/`,学有余力者自取 |

**新增总量**:约 200~300 题 + 50+ Case Study / Challenge

---

## 3. 推荐执行路径

```
第一轮(已完成) → v1 计划落地,56+178 道题验证
     ↓
第二轮(本轮)   → 采用方案 A(保守迭代)
                 - 先补 178 个 test_NN.py 自动评测脚本
                 - 再补 7 道缺口题(装饰器/生成器/日志/ABC 等)
                 - 阶段复习日调整至 Day19
     ↓
第三轮(下月)   → 方案 B(结构迭代)重新排 21 天
                 - Day20 引入调试+单元测试专项
                 - Day11-12 补充装饰器+生成器
                 - Day14 引入正则
     ↓
第四轮(长期)   → 方案 C(重练迭代)
                 - 练习量从 178 冲至 300+
                 - 每日一题 + Mini Case Study
```

---

## 4. 高优先级行动(立即可做)

### 4.1 补自动评测脚本(`test_NN.py`)

MIT/Harvard 都用自动化评测减轻教师负担。为 178 道 in_class 题各补 1 个 `pytest` 脚本。

**目录结构**:
```
lesson01/in_class/
├── practice01.py
├── practice01_test.py   ← 新增
├── practice02.py
├── practice02_test.py   ← 新增
└── ...
```

**脚本模板**(保守,只验证输出):
```python
"""当堂练习 practice01 的自动评测脚本(极简版)"""
import subprocess
import sys

def test_intro_output():
    """验证 print 输出包含 3 个关键要素"""
    result = subprocess.run(
        [sys.executable, "practice01.py"],
        input="\n",  # 无需输入
        capture_output=True,
        text=True
    )
    out = result.stdout
    assert "我是" in out, f"输出应包含'我是',实际输出: {out!r}"
    assert "我来自" in out, f"输出应包含'我来自',实际输出: {out!r}"
    assert "我的爱好是" in out, f"输出应包含'我的爱好是',实际输出: {out!r}"
    print("✅ practice01 通过")

if __name__ == "__main__":
    test_intro_output()
```

**优先级**:高(每补 1 个脚本 = 学员多得 1 次即时反馈循环)

### 4.2 补 7 道缺口题(按方案 A)

| # | 题 | 嵌入 Day | 文件路径 |
|---|---|---|---|
| 1 | 装饰器:计时器 | Day11 | `lesson11/in_class/practice07.py` |
| 2 | 装饰器:日志记录 | Day11 | `lesson11/homework/task04.py` |
| 3 | 生成器:无限斐波那契 | Day12 | `lesson12/in_class/practice07.py` |
| 4 | 生成器:Range 迭代器类 | Day12 | `lesson12/homework/task04.py` |
| 5 | 正则:提取邮箱和手机号 | Day14 | `lesson14/in_class/practice06.py` |
| 6 | 日志:logging 模块基础 | Day16 | `lesson16/homework/task04.py` |
| 7 | ABC 抽象类:Shape | Day20 | `lesson20/in_class/practice07.py` |

### 4.3 阶段复习日调整

当前 v1 的 Day17 是阶段复习③(Day14-17 综合),Day18-Day21 OOP 收尾。
方案 A 建议重新分配:

- Day18 → 阶段复习③(Day14-17 综合)
- Day19-Day21 → OOP(Day19 封装 + Day20 继承+多态 + Day21 期末综合作品)

这样 OOP 部分从 3 天压缩到 2.5 天,阶段复习后移,逻辑更清晰。

---

## 5. 版本追踪(原始做法)

由于不能用 git,采用时间戳目录 + CHANGELOG 文件追踪版本:

```
重构计划/
├── .versions/
│   ├── lessons-v1-20260707-152921/    ← v1 完整版(已备份)
│   ├── lessons-v2-20260708-XXXXXX/    ← 方案 A 落地后
│   └── ...
├── CHANGELOG.md                        ← 版本变更日志
├── iteration-v2-plan.md                ← 本文件:迭代方案
└── references.md                       ← 本次调研素材池
```

### CHANGELOG.md 格式

```markdown
# 教学计划变更日志

## v1.0.0 (2026-07-07)
- 初始版本,21 天教学计划,178 道习题,3 个中型项目

## v1.1.0 (待定)
- +7 道缺口题(装饰器/生成器/日志/ABC)
- +178 个自动评测脚本(test_NN.py)
- Day17/18 阶段复习日调整
```

---

## 6. 验收清单(方案 A 落地后)

- [ ] 178 个 `test_NN.py` 全部通过 `pytest -q`
- [ ] 7 道新题全部写入对应 lesson 目录
- [ ] Day17/18 README 已更新阶段复习说明
- [ ] CHANGELOG.md 已记录 v1.1.0 变更
- [ ] `.versions/lessons-v2-<时间戳>/` 备份已创建
- [ ] 学员测"No Regressions":Day01-Day17 原有题全部仍能跑

---

## 7. 关键资源链接(从 references.md 提取)

- **自动评测参考**:
  - MIT 6.0001 PS 评分模式:每 PS 有 `check` 脚本
  - Harvard CS50P check50:https://cs50.harvard.edu/python/
- **新增题源**:
  - 装饰器:廖雪峰 https://www.liaoxuefeng.com/wiki/1016959663602400/1017451662295584
  - 生成器:廖雪峰 https://www.liaoxuefeng.com/wiki/1016959663602400/1017318208925568Think Python 2E Ch18
  - 正则:Automate the Boring Stuff Ch7 https://automatetheboringstuff.com/2e/chapter7/
  - ABC 抽象类:PyNative OOP Ex18 https://pynative.com/python-object-oriented-programming-oop-exercise/
  - 日志:Automate Ch11 https://automatetheboringstuff.com/2e/chapter11/
