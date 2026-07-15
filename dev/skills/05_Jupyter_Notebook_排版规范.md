# 05 · Jupyter Notebook 排版规范 —— 反复调试后的最终标准

> 用途:所有 60 天课程的 Notebook 必须遵守的排版规范。
> 适用场景:新 Notebook 制作、现有 Notebook 格式审查、自动化排版脚本。

> **版本**:v3.2 (2026-07-15)
> **以 Day01-20 notebook 全体为 gold standard 重写(1227 cells, 210 traces)**
> **关键升级**:8 步趁热打铁循环 + ASCII 内存图 + NCDL Break It + 常见错误 + per-Day边界清单 + 完整示例模板
> v3.2 新增:基于 20 天 notebook 重构的全过程验收,补充常见示例和代码格式规范

---

## 1. 最终确定的格式规范

### 1.1 标题层级:h3(标题) + h4(小节),无 H1/H2

```
### Day 08 · OOP 基础                         ← h3(唯一)
#### __init__ 构造函数 —— 给对象"贴标签"       ← h4(小节)
#### 实例方法 —— 对象能做什么                  ← h4(小节)
**逐行解剖**                                    ← 正文加粗(不是标题)
**为什么:**这是解释,不是标题                    ← 正文加粗
```

**为什么不用 H1/H2:**
- H1 字体 ~28px,H2 ~22px:太大,页面显得拥挤
- h3 ~18px,h4 ~16px:舒适,适合长时间阅读
- 多层标题(H1+H2+H3+H4)会让页面"很碎"

**规则:**
- `###` 只用一次(当天标题)
- `####` 用于每个知识点的标题
- 不再往下嵌套(不用 `#####`)
- 解释性文字用 **加粗** + 正文,不额外加标题层级

### 1.2 加粗:只加关键词

```
✅ **类** = 蓝图/模板
✅ 使用 **append()** 方法可以在末尾添加元素
❌ **类是蓝图模板,用来创建对象**(整句加粗)
```

**规则:**
- 每行最多 **1 处** 加粗
- 加粗对象:关键词、方法名、重要概念
- 不整句加粗,除非是"核心定义"

### 1.3 一个 md cell = 完整小节(可多段)

```
✅ md cell 包含:
  - 概念解释(1-3 段)
  - 为什么需要它(痛点)
  - 类比(1 段)
  - 注意事项(1 段)
  - 常见错误(1 段)
```

**规则:**
- 一个 md cell 至少 **2 段**,最多 **5 段**
- 段落之间空一行
- 如果只有 1 句话,合并到上一个或下一个 md cell

### 1.4 md/code 交替

```
✅ md → code → md → code → md
❌ md → md → code → code → md
```

**规则:**
- 两个 code cell 之间**最多一个** md cell
- 两个 md cell 之间**最多一个** code cell

### 1.5 一个概念 = 一个 code cell

```
✅ print("Hello")      ← cell 1:基础用法
✅ print("你好")       ← cell 2:中文
✅ print("A", "B")    ← cell 3:多值
✅ print("A" + "B")   ← cell 4:拼接

❌ 以上 4 行全放在一个 cell 里
```

**为什么:**
- 学员可以逐个运行,逐个观察输出
- 如果多个示例挤在一个 cell 里,输出混在一起,看不出每个示例独立的结果

---

## 2. 每个知识点 = 完整的 8 步趁热打铁循环

### 2.1 8 步循环结构(必须完整)

每个完整知识点必须包含以下 8 步,**缺一不可**:

```
① 概念 md: 痛点(为什么需要) → 类比(生活例子) → 解释(是什么)
② ASCII 内存图 md(可选但推荐):文字画内存关系
③ 代码示例 code: 每行中文注释 + 执行过程跟踪(必须内嵌在 code cell 中)
④ 逐行解剖 md: 逐行解释语法和参数
⑤ 常见错误 md: 学员最容易犯的错(≥2 条)
⑥ 苏格拉底引导 md: 问自己(≥3 个引导问题)
⑦ 学员代码区 code: pass 占位
⑧ 参考答案 code: 完整可运行代码 + 注释
```

### 2.1.1 执行过程跟踪格式(⚠️ 最关键,最常见的错)

**执行过程跟踪必须内嵌在 code cell 中,不能放在 markdown cell 里。**

正确格式(跟踪在代码**下方**,与代码在同一 cell):

```python
password = ""
while password != "123":
    password = input("请输入密码:")
print("密码正确,欢迎!")

# --- 执行过程 ---
# 第 1 行 password = "":
#   ① 创建 password, 初值空字符串
#
# 第 2 行 while password != "123":
#   ① "" != "123" → True → 进循环
#
# 第 3 行 password = input(...):
#   ① 显示提示,等待用户输入
#   ② 把输入赋给 password
#
# 回到第 2 行再判断:
#   ① 若输入 "abc" → True → 继续循环
#   ② 若输入 "123" → False → 退出循环
```

**❌ 常见错误**:把执行跟踪放在 markdown cell(逐行解剖 md)里。
**✅ 正确做法**:执行跟踪 = 代码 cell 内的注释(`# --- 执行过程 ---`)。
**执行跟踪 + 逐行解剖 是两个不同的步骤,不能合并。**
- 执行跟踪(code cell 内):逐步解释代码执行时内存/流程变化
- 逐行解剖(md cell):解释语法和参数含义

### 2.1.2 per-Day 禁止语法清单

编写 notebook 前,**必须确认当日知识点范围**,禁止使用后续才教的语法:

| Days | 已教 | 禁止 |
|---|---|---|
| Day01 | print/input/变量/类型 | def/class/循环/列表/字典 |
| Day02 | +字符串/索引/切片/f-string | def/class/循环/列表/字典 |
| Day03 | +if/elif/else/比较/逻辑运算符 | def/class/循环/列表/字典 |
| Day04 | +while/for/range/break/continue | def/class/列表/字典 |
| Day05 | +def/函数 | class/列表/字典 |
| Day06 | +列表/字典 | class |
| Day07-10 | +class/OOP | 外部库 |
| Day11-13 | +模块/生成器/装饰器 | NumPy/Pandas |
| Day14+ | +NumPy/Pandas | sklearn/PyTorch/HF |

## 3. 完整示例(8 步趁热打铁)

```markdown
① #### __init__ 构造函数 —— 给对象"贴标签"

> **痛点**:之前用多个变量描述一个对象,变量散落在各处,传参时容易遗漏。
> **类比**:类 = 图纸/模具,对象 = 按图纸造出的产品。'学生'是图纸,'张三'是具体学生。
> **解释**:`class` 定义图纸;`__init__` 是构造函数,创建对象时自动执行;`self` 代表当前实例。
```

```markdown
② > **ASCII 内存图**
>
> ```
> 内存中:
> ┌─────────────────────┐
> │ 类对象 Student      │
> │ __init__(self,name) │
> └──────────┬──────────┘
>            │ 实例化
> ┌──────────┴──────────┐
> │ 实例 stu1           │
> │ name = "张三"       │
> │ age = 18            │
> └─────────────────────┘
> ```
```

```python
③ class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# --- 执行过程 ---
# 第 1 行 class Student:
#   ① Python 在内存中创建类对象 Student(图纸)
#   ② 把 __init__ 方法挂到类上,暂不执行
#
# 第 2 行 stu1 = Student("张三", 18):
#   ① Python 看到 Student(...),调用构造函数
#   ② 自动调用 __init__(stu1, "张三", 18)
#   ③ self 就是 stu1,把 "张三" 绑到 stu1.name
#   ④ self.age = 18 → stu1.age = 18
#   ⑤ 创建完毕,stu1 指向新对象

stu1 = Student("张三", 18)
print(stu1.name)  # 张三
```

```markdown
④ > **逐行解剖**
> - `class Student:` 声明类名,惯例首字母大写
> - `def __init__(self, name, age):` 双下划线 == dunder 方法
> - `self.name = name` 把参数值赋给实例属性
```

```markdown
⑤ > **常见错误**
> 1. **忘写 self 参数**:`def __init__(name, age):` → TypeError
> 2. **漏写冒号**:`class Student` → SyntaxError
```

```markdown
⑥ > 问自己:
> - 如果运行报错 `TypeError: __init__() takes 2 positional arguments but 3 were given`,检查什么?
> - `self.name = name` 左边和右边的 `name` 分别是什么?
> - 创建两个实例,修改一个会影响另一个吗?
```

```python
⑦ # ============ 学员代码区 ============
class Student:
    pass

# stu1 = Student(...)
pass

# ============ 参考答案 ============
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

stu1 = Student("张三", 18)
print(stu1.name, stu1.age)
```

### 2.2 ASCII 内存图(可选但强烈推荐)

对于理解内存关系重要的知识点(类/对象/继承链/组合),用 ASCII 画图:

```
✅ 继承链:
┌──────────────┐
│ Animal       │
│ name         │
│ breathe()    │
└──────┬───────┘
       │ 继承
┌──────┴──────┐
│ Dog         │  ← 自动拥有 name/breathe
│ bark()      │  ← 子类扩展
└─────────────┘

✅ 组合关系:
┌─────────────────────────────┐
│ Order                       │
│ cart: Cart ──────────┐      │
│ payment: Payment ────┤      │  has-a
│ address: Address ────┘      │
└─────────────────────────────┘
```

### 2.3 苏格拉底式引导格式

```markdown
> 问自己:
> - 这个练习要用到今天学的哪个知识点?
> - 题目中的"XX"对应对象的哪个属性?
> - 如果运行报错,检查:缩进对不对?冒号有没有忘?
```

**规则**:
- 至少 **3 个**引导问题
- 给出思考方向,但不直接说答案
- 培养独立思考和调试能力

### 2.4 常见错误格式

```markdown
> **常见错误**
> 1. **错误现象**:`TypeError: __init__() takes 2 positional arguments but 3 were given`
>    **原因**:忘写 self 参数
> 2. **错误现象**:`AttributeError: 'Student' object has no attribute 'name'`
>    **原因**:`self.name = name` 漏写或拼写错
```

**规则**:每个知识点至少 **2 条**常见错误,包含错误现象 + 原因

### 2.5 NCDL Break It 模式(用于关键知识点)

对于容易理解错误的知识点,使用"故意破坏"模式:

```python
# ============ BREAK IT 演示 ============
class BrokenAlipay:
    # 注意:execute 方法被漏写了!
    pass

def checkout(total, payment):
    return payment.execute(total)

alipay = BrokenAlipay()
print("创建成功,一切看似正常...")

try:
    checkout(99.0, alipay)
except AttributeError as e:
    print(f"报错: {e}")
    print("错误在运行中才暴露,难以追溯!")
# ============ END BREAK IT ============
```

**规则**:
- 故意写错代码,让学员读 Traceback
- 用 `try/except` 捕获预期错误
- 注释说明"为什么错了"和"如何修复"
- 适用于:漏写方法、忘继承 abc.ABC、忘调 super().__init__() 等

---

## 3. 执行过程跟踪

### 3.1 标准格式(在 code cell 内)

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# --- 执行过程 ---
# 第 1 行 dog1 = Dog("旺财", 3):
#   ① Python 看到 Dog(...) → 调用 Dog 类创建对象
#   ② 自动调用 __init__(self=新对象, name="旺财", age=3)
#   ③ self.name = "旺财" → 新对象的 name 属性 = "旺财"
#   ④ self.age = 3 → 新对象的 age 属性 = 3
#   ⑤ 创建完毕,把对象赋值给变量 dog1
#
# 第 2 行 print(dog1.name):
#   ① 读取 dog1.name → "旺财"
#   ② print 输出: 旺财

dog1 = Dog("旺财", 3)
print(dog1.name)  # 输出: 旺财
```

**为什么:**
- 学员运行代码后只看到最终输出,不知道中间发生了什么
- 执行过程让学员"看到"程序是一步一步执行的
- 配合`①②③`编号,清晰易懂

**规则:**
- 以 `# --- 执行过程 ---` 开头
- 按执行顺序逐行解释
- 用 `①②③` 编号表示步骤
- 重要的中间状态要说明(如 `self = dog1`)

---

## 4. 章节末尾附试题集链接

### 4.1 标准格式

```markdown
**更多练习**

- 当堂练:course/lesson08/in_class/practice01-06.py
- 课后作业:course/lesson08/homework/task01-03.py
```

**规则:**
- 不用 emoji(📝 ✏️ 等)
- 用**加粗**做小节标题
- 使用 `course/lessonXX/` 路径(不是 `lessonXX/`)

---

## 5. 每日结构

### 5.1 标准结构

```
### Day XX · [主题]                    ← h3 标题

> **前置**: ...
> **关键问题**: ...

**引入:...(痛点)**

---

#### 知识点 1

[概念解释:痛点→类比→解释]

[代码示例 + 执行过程]

**逐行解剖**

[逐行解释]

> 苏格拉底式引导

[学员代码区:pass]

[参考答案]

---

#### 知识点 2

(同上...)

---

**今日小结**

[表格:概念 vs 解决的痛点]

**更多练习**

- 当堂练:course/lessonXX/in_class/practice01-06.py
- 课后作业:course/lessonXX/homework/task01-03.py
```

---

## 6. 踩过的坑

### 6.1 ❌ H1/H2 标题
**问题:**字体太大(~28px/~22px),页面拥挤。
**放弃:**改用 h3(###) + h4(####)。

### 6.2 ❌ `<details>` 折叠答案
**问题:**JupyterLab/VS Code/GitHub 渲染不一致。
**放弃:**参考答案用独立 code cell。

### 6.3 ❌ CSS 注入字体大小
**问题:**学员不会配置,增加学习成本。
**放弃:**接受 Jupyter 默认,用 h3/h4 控制层级。

### 6.4 ❌ 多行字符串被拆成单字符
**问题:**subagent 生成的代码中,`"Hello"` 被拆成 `H\ne\nl\nl\no`。
**修复:**compile() 验证每个 code cell,发现问题立即修复。

### 6.5 ❌ Emoji 滥用
**问题:**✏️📌✅🚀 大面积使用,页面"很吵"。
**放弃:**只用**加粗**做视觉引导。

---

## 7. 排版检查清单

在提交 Notebook 之前,逐项检查:

### 结构检查
- [ ] 用 h3(###) 做天标题(唯一),用 h4(####) 做小节标题
- [ ] md/code 交替(不出现连续两个 code cell)
- [ ] 一个 md cell = 一个完整小节(2-5 段)
- [ ] 每行 ≤ 100 字符
- [ ] 每行最多 1 处加粗,加粗对象是关键词

### per-Day 边界检查(整本 notebook)
- [ ] 不含后续才教的语法(def/class/循环/列表等,除非当日已教)
- [ ] 引用的知识点在当日进度范围内
- [ ] 题目场景可用已学语法实现

### 趁热打铁 8 步检查(每个知识点)
- [ ] ① 概念:痛点 → 类比 → 解释
- [ ] ② ASCII 内存图(可选但推荐)
- [ ] ③ 代码:每行中文注释 + `# --- 执行过程 ---` **在 code cell 内**
- [ ] ④ 逐行解剖:逐行解释语法(在 md cell)
- [ ] ⑤ 常见错误:≥2 条
- [ ] ⑥ 苏格拉底引导:`> 问自己:` ≥3 个问题
- [ ] ⑦ 学员代码区:`pass` 占位
- [ ] ⑧ 参考答案:完整可运行代码

### 质量检查
- [ ] 章节末尾有"更多练习"链接
- [ ] 链接使用 `course/lessonXX/` 路径
- [ ] 无 `<details>` 标签
- [ ] 所有 code cell 通过 `python3 -m py_compile` 或直接运行验证
- [ ] NCDL Break It(如需要)用 `try/except` 捕获
- [ ] 执行跟踪 ≠ 逐行解剖(跟踪在 code,解剖在 md)

---

> **本文件结束**
> 配套 gold standard: Day01-20 notebook 全体,详见 `student-notebooks/`
> 版本历史:
> - v3.2 (2026-07-15):基于 20 天 notebook 重构全过程验收,补充 per-Day 禁止语法表和完整示例
> - v3.1 (2026-07-14):新增执行跟踪内嵌 constraint、per-Day 边界清单
> - v3.0 (2026-07-14):基于 OOP 教学设计重构
