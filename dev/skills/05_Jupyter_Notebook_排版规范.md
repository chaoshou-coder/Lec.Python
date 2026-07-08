# 05 · Jupyter Notebook 排版规范 —— 反复调试后的最终标准

> 用途:所有 60 天课程的 Notebook 必须遵守的排版规范。
> 适用场景:新 Notebook 制作、现有 Notebook 格式审查、自动化排版脚本。

> **版本**:v1.0 (2026-07-08)
> **经过**:N 次迭代,踩过所有坑,最终定型。

---

## 1. 最终确定的格式规范

### 1.1 标题层级:只有 H1

```
✅ # Day 05 · 字符串基础
❌ ## 1.1 字符串创建
❌ ### 1.1.1 索引
#### 1.1.1.1 正索引
```

**为什么**:
- 我们的 Notebook 已经有"Day ×X · 主题"作为文件名标识
- H2/H3/H4 的默认字体太大,会让 Notebook 看起来"很碎"
- 一个 Notebook = 一天的内容,不需要多级标题

**替代方案**:
- 用 **加粗文本** 代替 H2:**本节要点** / **常见错误**
- 用 --- 分隔线代替 H3
- 用 emoji 标识特殊章节:✏️ 练一练 / 📝 试题集 / 📌 小结

### 1.2 加粗:只加关键词

```
✅ **列表** 是 Python 最常用的数据结构之一
✅ 使用 **append()** 方法可以在末尾添加元素
❌ **列表是 Python 最常用的数据结构之一,它支持增删改查**
❌ 使用 append() 方法可以在列表的末尾添加一个元素
```

**为什么**:
- 大面积加粗会让页面看起来"很吵"
- 加粗应该引导学员的视线到关键词,不是整段强调

**规则**:
- 每行最多 **1 处** 加粗
- 加粗对象是:关键词、方法名、重要概念
- 不整句加粗,除非是"核心定义"

### 1.3 一个 md cell = 一个完整小节

```
✅ md cell 1:字符串创建(多段,但不切碎)
✅ code cell 1:演示字符串创建
✅ md cell 2:字符串索引(多段,但不切碎)
✅ code cell 2:演示字符串索引

❌ md cell 1:字符串创建(只有一句话)
❌ md cell 2:补充说明(只有一句话)
❌ md cell 3:注意事项(只有一句话)
```

**为什么**:
- 多个小 md cell 切碎 → 读起来像碎片,不像教程
- 一个 md cell 应该是一个"完整的小节",可以包含:
  - 概念解释(1-3 段)
  - 示例代码说明(1 段)
  - 注意事项(1 段)
  - 常见错误(1 段)

**规则**:
- 一个 md cell 至少 **2 段**,最多 **5 段**
- 如果只有 1 句话,合并到上一个或下一个 md cell
- 如果超过 5 段,拆分成两个 md cell

### 1.4 md/code 交替

```
✅ md → code → md → code → md
❌ md → md → code → code → md
❌ code → code → code → md
```

**为什么**:
- 两个 code 之间没有 md → 学员不知道第二个 code 在干什么
- 两个 md 之间没有 code → 学员只读不练,容易走神

**规则**:
- 两个 code cell 之间**最多一个** md cell
- 两个 md cell 之间**最多一个** code cell
- 例外:代码演示序列(如"错误写法 → 正确写法")可以连续 2 个 code

---

## 2. 每个知识点后必须有练习

### 2.1 练习的标准格式

```markdown
✏️ 练一练

给定一个列表 `nums = [3, 1, 4, 1, 5, 9, 2, 6]`,
编写代码找出列表中的最大值和最小值。

[学员代码区 - pass 占位]

<details>
<summary>参考答案</summary>

```python
def max_min_diff(nums):
    if not nums:
        return None
    max_val = min_val = nums[0]
    for n in nums:
        if n > max_val: max_val = n
        if n < min_val: min_val = n
    return max_val - min_val
```

</details>
```

**为什么**:
- ✏️ emoji 让学员一眼看到"这是练习"
- 学员代码区用 pass 占位,学员可以直接在 Notebook 里写
- 参考答案用 `<details>` 折叠,学员先自己想,再展开看

**注意**:`<details>` 在某些环境(如 GitHub)渲染不一致,见"踩过的坑"。

### 2.2 练习的数量

| 知识点类型 | 练习数量 | 示例 |
|---|---|---|
| 概念型(理解为主) | 1 道 | "解释列表和元组的区别" |
| 操作型(动手为主) | 2 道 | "创建一个列表" + "添加元素" |
| 综合型(应用为主) | 3 道 | "创建" + "操作" + "综合应用" |

---

## 3. 章节末尾附试题集链接

### 3.1 标准格式

```markdown
📝 本节试题集

- 当堂练:`course/lesson05/in_class/practice01.py` ~ `practice06.py`
- 课后作业:`course/lesson05/homework/task01.py` ~ `task03.py`
- 参考答案:`course/lesson05/homework/answer_key.md`
```

**为什么**:
- 学员在 Notebook 里学完后,需要"跳到 .py 文件"做练习
- 链接让学员知道"去哪里找题"
- 参考答案让学员自我检查

### 3.2 链接路径规范

```
✅ course/lesson05/in_class/practice01.py
❌ /Users/bang/Documents/code/Lec.Python/lesson05/in_class/practice01.py
❌ ../lesson05/in_class/practice01.py
```

**规则**:
- 使用**相对路径**,以 `course/` 为根
- 不使用绝对路径(不同学员的路径不同)
- 不使用 `../` 相对路径(容易出错)

---

## 4. 每日结构

### 4.1 标准结构

```
# Day XX · [主题]                    ← H1 标题(唯一)

[引入:1-2 段,讲为什么学这个]

---

## 第一讲:[主题名]

[概念解释:2-3 段]

[代码演示:1 个 code cell]

✏️ 练一练
[练习题目]
[学员代码区]
[参考答案]

---

## 第二讲:[主题名]

[概念解释:2-3 段]

[代码演示:1 个 code cell]

✏️ 练一练
[练习题目]
[学员代码区]
[参考答案]

---

📝 本节试题集
[链接到 .py 文件]

---

📌 今日小结
[3-5 个要点]
[下节预告]
```

### 4.2 各部分字数建议

| 部分 | 字数 | 说明 |
|---|---|---|
| 引入 | 100-200 字 | 讲"为什么学",不是"是什么" |
| 概念解释 | 200-400 字 | 2-3 段,配 1 个示例 |
| 代码演示 | 10-30 行 | 不要太长,学员记不住 |
| 练习 | 50-100 字 | 题目描述要简洁 |
| 参考答案 | 10-20 行 | 核心代码,不加注释 |
| 小结 | 100-200 字 | 3-5 个要点,不重复正文 |

---

## 5. 踩过的坑

### 5.1 ❌ 多个小 md cell 切碎

**尝试**:每个概念一个 md cell,每个示例一个 md cell。
**问题**:读起来像碎片,不像教程。学员需要频繁滚动,找不到"完整的一段话"。
**放弃原因**:视觉上太碎,学员容易走神。

### 5.2 ❌ 标题层级(H2/H3/H4)

**尝试**:用 H2 做章节标题,H3 做小节标题,H4 做知识点标题。
**问题**:Jupyter 默认 H2 字体 22px,H3 字体 18px,H4 字体 16px,看起来"很吵"。
**放弃原因**:字体太大,页面显得拥挤。改用加粗 + 分隔线。

### 5.3 ❌ `<details>` 标签

**尝试**:用 `<details>` 折叠参考答案。
**问题**:在 Jupyter Notebook 里渲染正常,但在 JupyterLab / VS Code / GitHub 里渲染不一致。
**放弃原因**:不同环境渲染不一致,学员可能看不到答案。
**替代方案**:把参考答案放在单独的 `.md` 文件,或放在 code cell 里用 `#` 注释。

### 5.4 ❌ CSS 注入字体大小

**尝试**:用自定义 CSS 调整字体大小。
**问题**:学员需要手动复制 CSS 到 Jupyter 配置,太麻烦。
**放弃原因**:90% 的学员不会用,反而增加学习成本。
**替代方案**:接受 Jupyter 默认字体,用加粗和分隔线做视觉引导。

### 5.5 ❌ 代码块写在 md 里

**尝试**:在 md cell 里用 ```python 写代码。
**问题**:不能交互执行,学员需要复制到 code cell 才能运行。
**放弃原因**:学员需要"边看边写",不能交互执行的代码块是反人类的。
**替代方案**:所有可执行代码都放在 code cell 里,md cell 只放解释文字。

### 5.6 ❌ 大面积加粗

**尝试**:把"重要概念"都加粗。
**问题**:超过 30% 的文字加粗 → 加粗失去强调作用,页面看起来"很吵"。
**放弃原因**:加粗应该引导视线,不是整段强调。
**替代方案**:每行最多 1 处加粗,只加关键词。

### 5.7 ❌ 长 code cell

**尝试**:一个 code cell 写 50 行代码。
**问题**:学员记不住前面的内容,需要频繁上下滚动。
**放弃原因**:短代码块更容易理解和记忆。
**替代方案**:一个 code cell 最多 30 行,超过就拆分。

---

## 6. JSON 结构示例

以下是一个完整 Notebook 的 cell 列表(JSON 格式):

```json
{
  "nbformat": 4,
  "nbformat_minor": 5,
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {"name": "python", "version": "3.10.0"}
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# Day 05 · 字符串基础\n",
        "\n",
        "在 Python 中,**字符串**是最常用的数据类型之一。",
        "本节我们将学习字符串的创建、索引、切片和常用方法。"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "\n",
        "## 第一讲:字符串创建\n",
        "\n",
        "字符串可以用单引号 `'` 或双引号 `\"` 创建。",
        "如果字符串内部需要包含引号,可以使用转义字符 `\\`。\n",
        "\n",
        "**常见错误**:忘记闭合引号,导致 `SyntaxError`。"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {},
      "source": [
        "# 字符串创建\n",
        "s1 = 'Hello'\n",
        "s2 = \"World\"\n",
        "s3 = \"It's a book\"\n",
        "print(s1, s2, s3)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "✏️ 练一练\n",
        "\n",
        "创建一个字符串 `name = '张三'`,",
        "然后用 f-string 输出 `我的名字是张三`。"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {},
      "source": [
        "# 学员代码区\n",
        "name = '张三'\n",
        "print(f'我的名字是{name}')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "\n",
        "## 第二讲:字符串索引\n",
        "\n",
        "字符串的每个字符都有一个**索引**,从 0 开始。",
        "也可以用负数索引,从 -1 开始(最后一个字符)。"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {},
      "source": [
        "# 字符串索引\n",
        "s = 'Python'\n",
        "print(s[0])   # P\n",
        "print(s[-1])  # n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "✏️ 练一练\n",
        "\n",
        "给定 `s = 'Hello World'`,输出第 3 个字符和倒数第 2 个字符。"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {},
      "source": [
        "# 学员代码区\n",
        "s = 'Hello World'\n",
        "print(s[2], s[-2])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "\n",
        "📝 本节试题集\n",
        "\n",
        "- 当堂练:`course/lesson05/in_class/practice01.py` ~ `practice06.py`\n",
        "- 课后作业:`course/lesson05/homework/task01.py` ~ `task03.py`\n",
        "- 参考答案:`course/lesson05/homework/answer_key.md`"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "\n",
        "📌 今日小结\n",
        "\n",
        "1. 字符串可以用单引号或双引号创建\n",
        "2. 索引从 0 开始,负数索引从 -1 开始\n",
        "3. 切片语法:`s[start:end:step]`\n",
        "\n",
        "下节预告:列表基础"
      ]
    }
  ]
}
```

---

## 7. 排版检查清单

在提交 Notebook 之前,逐项检查:

- [ ] 只有 H1 标题(# Day XX · Topic),无 H2/H3/H4
- [ ] 每行最多 1 处加粗,加粗对象是关键词
- [ ] 一个 md cell = 一个完整小节(2-5 段)
- [ ] md/code 交替(两个 code 之间最多一个 md)
- [ ] 每个知识点后有 ✏️ 练一练
- [ ] 练习有学员代码区(pass 占位)
- [ ] 章节末尾有 📝 本节试题集链接
- [ ] 每日末尾有 📌 今日小结
- [ ] 代码 cell ≤ 30 行
- [ ] 所有可执行代码都在 code cell 里(不在 md 里)
- [ ] 链接使用相对路径(course/lessonXX/...)
- [ ] 无 `<details>` 标签(或确认目标环境支持)

---

## 8. 自动化排版脚本(可选)

如果需要批量检查排版,可以使用以下 Python 脚本:

```python
import json
import sys

def check_notebook(path):
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    errors = []
    cells = nb['cells']
    
    for i, cell in enumerate(cells):
        if cell['cell_type'] == 'markdown':
            source = ''.join(cell['source'])
            # 检查 H2/H3/H4
            if any(line.startswith(('## ', '### ', '#### '))
                   for line in source.split('\n')):
                errors.append(f'Cell {i}:包含 H2/H3/H4 标题')
            # 检查加粗数量
            bold_count = source.count('**') // 2
            if bold_count > 5:
                errors.append(f'Cell {i}:加粗过多({bold_count} 处)')
        
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            # 检查代码行数
            if len(source.split('\n')) > 30:
                errors.append(f'Cell {i}:代码过长({len(source.split(chr(10)))} 行)')
    
    # 检查 md/code 交替
    for i in range(len(cells) - 2):
        if (cells[i]['cell_type'] == cells[i+1]['cell_type'] == 'code' and
            cells[i+2]['cell_type'] == 'code'):
            errors.append(f'Cell {i}-{i+2}:连续 3 个 code cell')
    
    return errors

if __name__ == '__main__':
    for path in sys.argv[1:]:
        errors = check_notebook(path)
        if errors:
            print(f'\n{path}:')
            for e in errors:
                print(f'  ❌ {e}')
        else:
            print(f'✅ {path}:通过')
```

---

## 9. 排版的迭代历史

| 版本 | 日期 | 变更 | 原因 |
|---|---|---|---|
| v0.1 | 2026-07-01 | 使用 H2/H3/H4 多级标题 | 传统教材习惯 |
| v0.2 | 2026-07-02 | 去掉 H3/H4,保留 H2 | H3/H4 字体太大 |
| v0.3 | 2026-07-03 | 去掉 H2,只用 H1 | H2 仍然太大,页面碎 |
| v0.4 | 2026-07-04 | 引入 `<details>` 折叠答案 | 让学员先自己想 |
| v0.5 | 2026-07-05 | 去掉 `<details>`,改用链接 | 不同环境渲染不一致 |
| v0.6 | 2026-07-06 | 限制加粗数量(每行 1 处) | 大面积加粗太吵 |
| v0.7 | 2026-07-07 | 限制代码 cell ≤ 30 行 | 长代码块记不住 |
| v1.0 | 2026-07-08 | 定型,不再大改 | 经过 N 次迭代,达到平衡 |
