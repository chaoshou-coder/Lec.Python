# 学生版 Jupyter Notebook

> 为零基础成年学员编写的交互式学习笔记
> 内容基于 `course/lesson01/` ~ `course/lesson21/` 的 slides.md

---

## 📚 使用指南

### 环境准备

1. 安装 Python 3.10+ (官网下载 python.org)
2. 安装 Jupyter:
   ```bash
   pip install jupyter
   ```
3. 启动:
   ```bash
   jupyter notebook
   ```

### 学习方式

- **阅读** markdown 单元格中的概念解释
- **运行** code 单元格,观察输出
- **完成** `# 学员代码区` 练习题
- **参考答案**用 `<details>` 折叠,先独立完成再看

### 各 Day 难度递进

- Day 1-2: ⭐~⭐⭐ (基础概念)
- Day 3-4: ⭐⭐~⭐⭐⭐⭐ (逻辑与循环)
- Day 5+: ⭐⭐⭐~⭐⭐⭐⭐⭐ (函数与抽象)

### 零基础?先学 Jupyter!

**从未用过 Jupyter Notebook?** → 先打开 [`00_JupyterNotebook使用教程.ipynb`](00_JupyterNotebook使用教程.ipynb),30 分钟学会:

- 安装/启动 Jupyter
- Cell 操作(创建/编辑/运行/删除)
- Markdown 笔记写法
- 快捷键速查
- Kernel 操作(重启/中断)
- 常见问题排查(Q1-Q5)
- 实战:创建你的第一个 Notebook

---

## 📂 文件导航

| 文件 | 主题 | 核心知识点 |
|---|---|---|
| `Day01_Python与开发环境.ipynb` | Python 入门 | print/input/变量/搭建环境 |
| `Day02_字符串与格式化.ipynb` | 字符串 | 索引切片/f-string/isdigit |
| `Day03_条件分支.ipynb` | 分支结构 | if/elif/else/and or not/三元 |
| `Day04_循环入门.ipynb` | 循环 | while/for/range/break/continue |
| `Day05_函数入门.ipynb` | 函数 | def/return/形参实参/默认参数 |

---

## 🎯 各 Day 学习目标速览

### Day 1 · Python 与开发环境
1. 搭建环境,跑通第一个程序
2. 掌握 `print()` 输出
3. 掌握 `input()` 输入,理解它永远返回字符串
4. 理解变量与命名规则
5. 区分 `=` 与 `==`

### Day 2 · 字符串与格式化
1. 掌握字符串索引,理解"从零开始"
2. 掌握切片 `s[start:end:step]`
3. 掌握 `find()`/`rfind()`/`isdigit()`
4. 掌握 `replace()` 批量替换
5. 重点掌握 f-string

### Day 3 · 条件分支
1. 掌握比较运算符
2. 掌握 `if/elif/else`
3. 掌握 `and/or/not`
4. 掌握嵌套条件和三元表达式
5. 能用 `in` 判断包含

### Day 4 · 循环入门
1. 掌握 `while` 循环三要素
2. 掌握 `for` + `range()`
3. 掌握累加器与累乘器
4. 掌握 `break` 与 `continue`
5. 能打印三角形、九九乘法表

### Day 5 · 函数入门
1. 理解函数的作用
2. 掌握 `def` 定义与调用
3. 掌握四种形式
4. 掌握形参/实参/默认参数
5. 掌握 `return` 与多值返回

---

## ✅ 学习建议

1. **每天 1 个 Notebook**,约 6 小时
2. **先读后写**,理解概念再动手
3. **独立完成练习**,不看参考答案
4. **运行验证**,每个 code 单元格都要跑一遍
5. **挑战题**是选做的,学有余力再做

---

## 配套资源

- 课程 slides: `course/lesson01/slides.md` ~ `course/lesson05/slides.md`
- 练习文件: `lessonXX/in_class/practiceNN.py`
- 作业文件: `lessonXX/homework/taskNN.py`
- 教师笔记: `lessonXX/teacher_notes.md`
