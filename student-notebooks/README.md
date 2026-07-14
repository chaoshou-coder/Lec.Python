# 学生版 Jupyter Notebook(Day 1-20)

> 为零基础成年学员编写的交互式学习笔记
> 内容对齐 `course/lesson01/` ~ `course/lesson20/` 的 slides.md
> 遵循"趁热打铁"循环:痛点 → 类比 → 代码 → 逐行解剖 → 练习 → 参考答案

---

## 📚 快速开始

### 环境准备

```bash
# 1. 安装 Python 3.10+(官网下载 python.org)
# 2. 安装 Jupyter + 科学计算库
pip install jupyter numpy pandas matplotlib seaborn

# 3. 启动
cd student-notebooks
jupyter notebook
```

### 学习方式(每天 1 个 Notebook ≈ 6 小时)

1. **读** markdown 单元格中的概念解释(痛点→类比→解释)
2. **跑** code 单元格,观察输出(每行都有`逐行解剖`注释)
3. **做** 学员代码区练习题(`pass` 占位符处)
4. **对** 参考答案(同一 code 单元格下方)

### 从未用过 Jupyter?

需要找教师指导基础操作。

---

## 📂 Day 1-20 完整导航

### 基础阶段(Day 1-6)

| 文件 | 主题 | 核心知识点 | 练习数 |
|---|---|---|---|
| `Day01_Python与开发环境.ipynb` | 入门 | print/input/变量/type/id | 6+3 |
| `Day02_字符串与格式化.ipynb` | 字符串 | 索引切片/f-string/isdigit/find | 6+3 |
| `Day03_条件分支.ipynb` | 分支 | if/elif/else/and or not/嵌套 | 6+3 |
| `Day04_循环入门.ipynb` | 循环 | while/for/range/break/continue | 6+3 |
| `Day05_函数入门.ipynb` | 函数 | def/return/形参实参/默认参数/作用域 | 6+3 |
| `Day06_列表与字典.ipynb` | 容器 | 列表CRUD/字典CRUD/推导式/in | 6+3 |

### OOP 阶段(Day 7-11,4 天递进)

| 文件 | 主题 | 核心知识点 | 练习数 |
|---|---|---|---|
| `Day07_OOP封装_L1.ipynb` | 封装 | class/__init__/@property/__str__/类属性 | 6+3 |
| `Day08_OOP继承_L2.ipynb` | 继承 | 单继承/super()/重写/MRO/isinstance | 6+3 |
| `Day09_OOP多态契约_L3.ipynb` | 多态+契约 | 鸭子类型/abc.ABC/@abstractmethod/接口 | 6+3 |
| `Day10_OOP组合Pythonic_L4.ipynb` | 组合+Pythonic | 组合优于继承/__add__/__len__/__iter__/__eq__ | 6+3 |

### 模块与阶段复习(Day 12-13)

| 文件 | 主题 | 核心知识点 |
|---|---|---|
| `Day11_模块与高级特性.ipynb` | 模块 | 包/生成器/装饰器/import |
| `Day12_阶段复习与购物车项目.ipynb` | 综合 | Day01-11 知识综合应用 |

### 数据处理(Day 14-20)

| 文件 | 主题 | 核心知识点 |
|---|---|---|
| `Day13_NumPy基础.ipynb` | NumPy | 数组/广播/向量化/线性代数 |
| `Day14_NumPy进阶.ipynb` | NumPy | 随机数/统计/索引/切片 |
| `Day15_Pandas基础.ipynb` | Pandas | Series/DataFrame/索引/过滤 |
| `Day16_Pandas进阶.ipynb` | Pandas | 分组/合并/透视/清洗 |
| `Day17_数据可视化.ipynb` | 可视化 | 折线/柱状/散点/热力图 |
| `Day18_数据摄取.ipynb` | 数据 | CSV/JSON/Excel/SQL/API |
| `Day19_EDA综合项目.ipynb` | EDA | 数据清洗→可视化→洞察全流程 |

---

## ✅ 学习建议

1. **每天 1 个 Notebook**,约 6 小时
2. **先读后写**:理解概念(痛点→类比)再动手
3. **独立练习**:先不看参考答案,自己写
4. **逐行验证**:每个 code cell 都看`逐行解剖`注释
5. **Homework 选做**:学有余力再做 homework/

---

## 🎯 OOP 4 天学习路径(Day 7-10)

```
Day07 L1 封装:变量散乱 → 用 class 打包数据+行为
     ↓
Day08 L2 继承:代码重复 → 用继承抽取共性
     ↓
Day09 L3 多态:if-elif 痛 → 用多态统一接口
     ↓
Day10 L4 组合+Pythonic:对象不自然 → 运算符重载
```

**贯穿案例**:电商订单系统 v2 —— 从散落的 dict 演进到可合并购物车

**NCDL 负案例驱动**:Day09 含 3 段 Break It 实测代码,体会"为什么需要契约"

---

## 配套资源

- **课程 slides**: `course/lesson01/slides.md` ~ `course/lesson20/slides.md`
- **当堂练习**: `course/lessonXX/in_class/practice01-06.py`
- **课后作业**: `course/lessonXX/homework/task01-03.py`
- **中型项目**: `weekly_projects/` (购物车/图书/订单系统)

---

## ⚠️ 教学红线提醒

每个 Notebook 都标注了常见易错点:

Day01-06 重点:
- **`=` 与 `==` 混淆** — `=` 是赋值,`==` 是比较
- **缩进混用 Tab/Space** — 统一用 4 空格
- **函数定义后不调用** — 写了 `def` 不等于执行

Day07-10 OOP 重点:
- **忘写 `self`** — 实例方法第一个参数必写 `self`
- **`@property` 漏写 setter** — 外部赋值不触发校验
- **重写 `__init__` 忘调 `super()`** — 父类属性丢失
- **用 `isinstance` 做分发** — 违反多态原则
