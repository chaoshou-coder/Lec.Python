# Python 零基入门到 OOP + 小项目 · 21 天教学计划(重构版 v2)

## 1. Context(为什么重做这份计划)

### 1.1 现有课程已达到的水平

七日旧课件(Day01-Day07)已经覆盖了 Python 入门的绝大多数"知识点":
- 原子层:变量/数据类型/`type()` /`id()` / 运算符 / 编码 / 进制
- 控制流:三大结构 / `break`/`continue`/`for-else`/`while-else` / 嵌套循环
- 容器:字符串 / 列表 / 元组 / 集合 / 字典(全部 CRUD + 切片 / 生成式)
- 函数:`*args` / `**kwargs` / 默认参数 / 混合参数顺序 / 组包 / 解包 / 三元表达式
- 未知数:`global` / `globals()` / 匿名函数 `lambda` / 内置函数 `filter` `map` `all` `any`
- 文件:`open` / `with` / `read` / `readline` / `readlines` / `print(…, file=!)` / 二进制 `'rb'`
- 模块:`random.shuffle()` / `time.localtime() / strftime()` / `time.sleep()` / `os`(仅 import 一次)
- 算法:冒泡排序 / 递归(`sum` / `fact` / `feibo`) / 穷举法(鸡兔同笼)
- 综合作品:收银台(Exam01) / 人机猜拳 / 菱形打印 / 猜数字游戏 / 斗地主发牌 / 学员管理系统 v1(二维列表) v2(字典列表)
- Day07 还会讲:`global`、`globals()`、`lambda` 多场景、`filter/map/all/any`、递归、文件读/写/二进制、`time` 模块、`os` 模块(未展开)

### 1.2 当前存在的根本问题

**问题 1:知识点铺得很快,但"讲 → 写 → 纠错 → 再写"这一循环不完整**

- 很多综合作品(v1 学员系统 98 行,v2 学员系统 78 行,"按照字典中的平均分排序" 93 行)"示范代码一次写对",学生在底下看懂了思路,但课后作业还是不会写。
- 根因:前面 1~6 天每个知识点 **只给了 1~2 道例题**,缺少"先脱离示范题也能独立写"的过渡。

**问题 3:os 模块异常和文件操作都严重缺失**

- `os` 只在 Day07 Demo09.py 以 `import os` 出现,没有任何调用;异常处理(`try/except/finally` / `raise` / 常见异常类)从未讲过;CSV / JSON / 大文件 / 目录遍历 / 批量重命名从未遇到。
- 用户这次明确补入的三个主题(os 模块 / 异常 / 文件操作)不仅该贯穿 Day07-Day10,还应该作为"项目实战必备能力"扩展到 Day15-Day20 的每个综合项目里。

**问题 4:面向对象(OOP)完全没系统讲**

- Day06 `Demo05.py` 仅仅一行 `class Person` + `def call(self)` 一闪而过,没有 `__init__` / 实例属性 / 类属性 / 继承 / 多态 / 特殊方法(`__str__`/`__repr__`/`__eq__`)/ 封装(私有属性)——这些恰恰是"小项目"要用的。
- 用户的目标是"到 OOP + 小项目",所以 OOP 必须成为 Day11-Day16 的绝对主角,并在 Day17-Day20 的复杂项目里反复使用。

**问题 5:常用模块(json / csv / re / datetime / pathlib)从未出现**

- 课件的"字典数据获取"虽然给了 JSON 实测数据,但 **从未讲过 JSON 的序列化/反序列化**
- 图书/电商/管理系统的"数据持久化"最常见的手段是 JSON/CSV,应该至少覆盖其中一种

**问题 6:学习曲线存在几处"台阶式跳跃"**

- Day03 嵌套循环一下子就上"鸡兔同笼 + 菱形打印",此前只用嵌套 for 打印过 99 乘法表 → 练习步幅过大
- Day05 一下用字典 + 列表写 v2 学院系统 + "扑克洗牌分牌" + "按照字典平均分排序"(冒泡)三件硬茬并排 → 单日难度峰
- Day06 直接上 `*args` / `**kwargs` / `global` / `globals()` / `lambda` / 递归五件套 → 抽象度过高且彼此关联性低

### 1.3 本次重构的目标和边界

- **目标**:在 21 天内把零基学员带到能独立写"控制台图书管理系统 / 记账本 / 学生管理系统 v3 (OOP+JSON 持久化完成)"这一级
- **范围**:Python 标准库内;不引入第三方包(除了 `colorama` 一支彩笔已经用过可以顺势保留 1~2 次)
- **学习深度**:每个知识点 1~3 道示范 + 5~8 道当堂练习 + 2~4 道课后作业;每 2~3 天必须有一个"小项目"把前几天知识串起来,每 7 天一个"中型项目"做阶段收口
- **作品流**(占期末考核 50%):
  - 每日当堂小项目(21 个) → 取最高 10 次评分
  - 每周中型项目(3 个) → 必须过验收点才给分
  - 期末成长档案(1 份) → 学员自己挑 3 个作品写 README 与 demo

---

## 2. 教学计划目录结构

所有新课件放在 `/Users/bang/Documents/learning/python/课件/重构计划/lesson01/` ~ `lesson21/`,旧的 `day01` ~ `day07` 完全保留。

每个"课"的目录结构统一:

```
lesson03/
├── slides.md                       # 当天讲义(教师用,含知识点清单 + 示范代码)
├── demo/                           # 演示脚本(每个文件对应一个知识点)
│   ├── 01.变量创建.py
│   ├── 02.类型查看.py
│   └── 03.格式化输出.py
├── in_class/                       # 当堂练习(学生写,教师巡场点评)
│   ├── practice01.py
│   ├── practice02.py
│   └── ...
├── homework/                       # 课后作业(2~4 题,难度线性递增)
│   ├── task01.py
│   ├── task02.py
│   └── ...
├── mini_project/                   # 每 2~3 天的小项目
│   └── 温度数据记录器.py
├── assets/                         # 必要的数据素材(xiongmao.txt 之类)
└── teacher_notes.md                # 教师备忘(易错点、延伸题、查缺记录)
```

每周一个"中型项目"放在独立目录:

```
weekly_projects/
├── week01_shopping_cart/           # 第一周中型项目: 购物车
├── week02_library_manager/         # 第二周中型项目: 图书管理系统 v1(函数版)
└── week03_book_manager_oop/        # 第三周中型项目: 图书管理系统 v2(OOP + JSON 持久化)
```

---

## 3. 21 天的授课模块划分

| Day | 主题 | 本节新增知识点 | 当堂练习 | 课后作业 | 小 / 中型项目 |
|---|---|---|---|---|---|
| 01 | Python 入门与开发环境 | `print()`、`input()`、变量命名、`type()`、`id()` | 4 | 2 | 🎯 "我的第一份自我介绍" |
| 02 | 数据类型与运算 | `int/float/str/bool`、算术/比较/逻辑/成员运算符 | 5 | 2 | 🎯 "简易收银台" |
| 03 | 字符串(基础) | 索引/切片/`len()`/`format`/`%`/`f-string`/`isdigit` 三兄弟 | 5 | 2 | 🎯 "手机号脱敏" |
| 04 | 列表(基础) | 创建/CRUD(增删改查)/`append/insert/extend/pop/remove/del/sort/reverse` | 6 | 2 | 🎯 "购物清单簿" |
| 05 | 循环入门 | `while`、`for…in…`、`range()`、转义符 `\n\t`、`end=` | 6 | 3 | 🌟 **小项目 v1: "每日记账本"** |
| 06 | 分支与嵌套 | `if/elif/else`、嵌套 `if`、条件运算符、嵌套循环 | 6 | 3 |  |
| 07 | **阶段复习①** | Day01-Day06 综合题 | 6 | 3 |  |
| 08 | 字符串(提升) | `find/index/rfind/endswith/startswith/replace/拆分 split/连接 join/title/strip` | 6 | 2 | 🎯 "敏感词过滤器" |
| 09 | 列表(进阶) | 切片进阶、列表生成式、二维列表、深拷贝浅拷贝 `copy.copy()/deepcopy()`、打包 `*args` 引入 | 6 | 3 | 🌟 **小项目 v2: "成绩统计表"** |
| 10 | 函数入门 | `def`、无参无返 / 有参无返 / 无参有返 / 有参有返、四种形式、`return` | 6 | 2 | 🎯 "BMI 健康判断仪" |
| 11 | 函数进阶 | 默认参数、`*args`、`**kwargs`、混合参数顺序、组包/解包(`a,b,c=data`)、`lambda` 入门 | 6 | 3 | 🌟 **小项目 v3: "成语词典"(函数版)** |
| 12 | 迭代、内置函数与递归 | `lambda` 进阶、`filter/map/reduce`/`sorted/max/min/sum/any/all`、`global`、递归(`sum` `fact`) | 6 | 3 |  |
| 13 | **阶段复习②** | Day08-Day12 综合题 | 6 | 3 | 🌟 **中型项目 v1: "控制台计算器"(函数+异常)** |
| 14 | 文件操作(基础) | `open/read/readline/readlines/close`、`with … as`、`'w'/'a'/'r'/'rb'`、`print('…', file=fp)`、文件编码(utf8/gbk) | 5 | 2 | 🎯 "日志写入器" |
| 15 | 文件操作(进阶) + os 模块 | `os.getcwd()`、`os.listdir()`、`os.mkdir()`/`os.remove()`、`os.path.exists`、遍历目录 | 6 | 2 | 🌟 **小项目 v4: "批量重命名工具"** |
| 16 | 异常处理 | `try/except/else/finally`、常见异常类(`ValueError/TypeError/FileNotFoundError/KeyError/IndexError`)、`raise`、自定义异常 | 6 | 2 | 🎯 "弹性输入助手" |
| 17 | JSON 与 CSV | `json.loads/json.dumps/json.load/json.dump`、`csv.reader/csv.writer` + `with` | 5 | 2 | 🌟 **小项目 v5: "个人账本(json 持久化)"** |
| 18 | **阶段复习③** | Day14-Day17 综合题 | 6 | 3 |  |
| 19 | 面向对象(封装) | `class`、`__init__(self, …)`、实例属性方法、私有属性 `_name`/`__name`、`@property` 引入、`__str__`/`__repr__` | 6 | 2 | 🎯 "Student 类建模" |
| 20 | 面向对象(继承 + 多态) | 单继承、`super().__init__()`、方法重写、多态体验、类属性 vs 实例属性 | 6 | 3 | 🎯 "图形/动物分类" |
| 21 | 期末总复习 + 作品展示 | Day01-Day20 错题串讲 + 学员秀 3 个作品 + 查缺 | - | - | 🌟 **中型项目 v2: "控制台图书管理系统 v2(OOP+JSON+CSV+异常)"** |

---

## 4. 关键课时"教-学-做-评"节奏表

以下是几节"学生容易转头就忘"的硬课,给教师建议按下列节奏拆分(单位:分钟):

| 阶段 | 时长 | 教师动作 | 学员动作 |
|---|---|---|---|
| **引入** | 5' | 复述上节(抽问)、赏玩本节成品 demo | 带问题看成品 |
| **第一讲** | 10' | 讲概念 + 现场写 **1 道示范**(每行代码立即 `git commit` 留档) | 不做笔记,只带着听 |
| **当堂练 1** | 10' | 巡场 + 用 `code --goto` 定位学员 bug | 完成一道题,教师点评 |
| **第二讲** | 10' | 讲较难的第二个知识点(如嵌套循环) |  |
| **当堂练 2×2** | 15' |  | 完成 2 道进阶题 |
| **小项目(每 2~3 天)** | 20' | 巡场 + 5 分钟展示优秀作品 | 独立完成 |
| **总结** | 5' | 把当天"高频错 3 件事"写进 `teacher_notes.md` | 回去先复盘这 3 件事再做作业 |

> 当堂练习 **不要超过 5 小时练一次完整项目**,否则学员卡住后就没时间"点评 → 修正"循环——这是 Day01-Day07 的主要缺失。

---

## 5. 必须新增的习题示例(按 Day 展开并标注难度)

### Day01 · "我的第一份自我介绍"(小项目)

**难度**:⭐ 当堂,**练习签名 print + input + f-string**

```python
# 1. 从控制台询问学员姓名(string)、年龄(int)、身高(float)
# 2. 用 f-string 输出:
#    "我叫 <name>,今年 <age> 岁,<height> 米高 🐼"
# 3. 进阶:用 "%<10s" 让姓名右对齐 10 字符
```

### Day05 · "每日记账本"(小项目 ★★★★★)

**难度**:⭐⭐ 当堂,结合循环 + 分支 + 列表

```python
# 1. 输入一项支出(项目 + 金额),循环至用户输入 -1
# 2. 同时累积:
#    - 本周支出总金额
#    - 头 3 项最贵的项目
#    - 头 3 项最新的项目
# 3. 结束时输出报表
```

### Day07 · 阶段复习(6 题覆盖) — 故意设置"坑"

1. 写出 2 个让 `bool(x)` 为 False 的值(避免"非空即 True"陷阱)
2. 写一个函数 `yang_number(num) -> bool`,负数也返回 False(边界条件训练)
3. `my_list = [i for i in range(10, 0, -2)]` 输出是什么?(负步长训练)
4. `print('cost is', 99, sep=',')` 训练 `sep` 是**,** 不是自动空白
5. 比较 `"hello".find('x')` 与 `"hello".index('x')` 的输出差异
6. 找错:下面代码为什么打印不出换行?`for i in range(5): print(i, end='')` 后加 `print(i)`

### Day09 · "成绩统计表"(小项目 v2 ⭐⭐⭐)

**难度**:⭐⭐⭐,结合嵌套列表 + 函数 + `sort` + `lambda` key

```python
# 1. 输入 N 个学生数据: [姓名, score]
# 2. 计算平均分、最高分、最低分
# 3. 按分数降序输出
# 4. 进阶:同等分数按学号(输入顺序)升序
```

### Day11 · "成语词典"(函数版)

**难度**:⭐⭐⭐,字典 CRUD + `*args` + `lambda`

```python
# 1. 菜单循环:1.查 2.加 3.改 4.删 0.退出
# 2. 查:支持 *args 多个关键词同时命中
# 3. 排序:menu 项可按拼音顺序,也可按录入顺序
# 4. 支持命令行参数重写菜单入口
```

### Day14 · "日志写入器"(小项目 v4 之前的一堂技术课)

**难度**:⭐⭐ 非小项目,纯技术课,与 Day08 的"敏感词过滤器"形成呼应

```python
# 1. 用 'a' 模式追加写入 + UTF8
# 2. 用 'w' 模式覆盖 + 'r' 验证
# 3. 用 with 写,故意把 `with` 语句 `fp.close()` 漏掉 → 讲 why
# 4. 用 `'rb'` 打开 PNG / txt 并用 `read()` 打印字节
```

### Day15 · "批量重命名工具"(小项目 v4 ⭐⭐⭐⭐)

**难度**:⭐⭐⭐⭐ 综合 文件 + os + 异常 三大新模块

```python
# 1. 给定一个目录 path
# 2. 把所有 *.txt 文件改名为 <filename>_<序号>.txt
# 3. 如果文件已存在,跳过不覆盖
# 4. 用 try/except 捕获异常并在日志里记录
```

### Day16 · "弹性输入助手"(小项目 v5 ★☆☆ 反串)

**难度**:★☆☆ 当堂练,但技术点极度刚需

```python
# 1. 写 `def safe_int(prompt, default=0)`,反复 prompt 直到用户输入整数
# 2. 写 `def safe_float(...)`
# 3. 用 try/except 内部消化 ValueError
# 4. 进阶:prompt 支持验证函数 callback
### Day17 · "个人账本(json 持久化)"

**难度**:⭐⭐⭐ 小项目

```python
# 1. 菜单:1.记一笔 2.删一笔 3.按月统计 4.导出 CSV 5.加载
# 2. 启动时自动加载 ./my_ledger.json
# 3. 退出时自动保存
# 4. 不崩溃:文件损坏时提示"如需清空可删除 ledger.json"
```

### Day18 · 阶段复习(6 题)

故意设计"4 个全是异常"的陷阱:
1. `int(input("请输入年龄:"))` 用户敲回车 → 如何处理?
2. `open('./note.txt', 'r')` 文件不存在 → 建议改用哪种结构?
3. `d['missing']` vs `d.get('missing')` 差异(区分 `KeyError` 与 None)
4. `os.remove('./a.txt')` 文件不存在会怎样?
5. `with open(...) as f: f.write('x')` 模式错成 'r' 会怎样?
6. `json.loads('{"x":1}')` 的字符串是 API 返回时少了末尾的 '}' → 如何优雅处理?

### Day19 · "Student 类建模"

**难度**:⭐⭐ 当堂

```python
# 1. class Student 有 name, height, age, scores(list)
# 2. avg() 方法返回平均分
# 3. __str__ 打印 "小明 · 平均分 85"
# 4. @property is_passed → avg >= 60
```

### Day20 · "图形/动物分类"

**难度**:⭐⭐⭐⭐ 当堂

```python
# 1. Animal 基类有 speak() 默认 "..."
# 2. Dog / Cat / Pig 子类各自重写 speak()
# 3. def letting_zoo(animals: list[Animal]): for a in animals: a.speak() -> 多态体验
# 4. def all_sounds(zoo) → 返回所有叫声 list
```

### Day21 · 期末中型项目:"控制台图书管理系统 v2"

**难度**:⭐⭐⭐⭐⭐,整合 **OOP + JSON 持久化 + CSV 导出 + 异常处理 + os 路径 + 函数 + lambda 排序**

验收点:
- [ ] 能 add / remove / update / search / list / checkout / return 七项核心操作
- [ ] 启动时加载 `./data/books.json`,失败则创建空库
- [ ] 每项操作都有 except 处理,终端提示友好
- [ ] 用 `Book` / `Reader` / `Transaction` 三个类
- [ ] 能导出 `/data/report.csv`(借阅排行)
- [ ] 含单元测试用例(教师事先写好 test 脚本,学员跑通即给分)

---

## 6. 进度追踪与评估建议

- 每日教师在上课后 5 分钟内在 `teacher_notes.md` 写"本日错 3 件事" + 当堂 5 人作品打分
- 每周最后一天(第 7 / 14 / 21 天)带测"自动评测脚本"`pytest -q test_week_N.py`,通过即 1.0 倍,每一道补交加 0.2
- 分数构成:
  - 当堂小作品 30%(取最高 10 次)
  - 每周中型项目 40%
  - 作品 README 与 demo 展示 20%
  - 出勤与错题本 10%

---

## 7. 执行阶段

本次重构要做的事(一次性落地的顺序):

1. 按 `lesson01/ ~ lesson21/` 创建目录骨架
2. 逐个填充 **slides.md + demo + in_class + homework + mini_project + teacher_notes**(优先前 7 天可用,后续由授课教师边讲边补)
3. 同步更新 `day01_day07/ 同步修订指引.md`,指出旧课件的哪些范例仍然可复用、哪些当堂练习缺失需要补
4. 教师轮第一遍试讲后反馈迭代(第 1 周后提交 iteration log)

---

## 8. 关键文件清单(本次就落盘)

- `/Users/bang/Documents/learning/python/课件/重构计划/slides-lesson01~21/`(按需生成)
- `/Users/bang/Documents/learning/python/课件/重构计划/weekly_projects/week01_shopping_cart/`
- `/Users/bang/Documents/learning/python/课件/重构计划/weekly_projects/week02_library_manager/`
- `/Users/bang/Documents/learning/python/课件/重构计划/weekly_projects/week03_book_manager_oop/`
- `/Users/bang/Documents/learning/python/课件/重构计划/summary.md`(本计划的统一入口)

---

## 9. 验证方式

教师按计划授课,验证点:
1. Day07 阶段测平均正确率 ≥ 70% 即算平稳过渡
2. Day14 阶段测 Day09-Day13 的函数综合题正确率 ≥ 65%
3. Day21 中型项目有 ≥ 5 项验收点通过即合格

项目层面:Week1 购物车必须能跑通完整购买流程;Week2 图书系统 v1 必须能 add/list/delete/query 不崩溃;Week3 图书系统 v2 必须在 JSON 持久化 + 异常 + OOP 三测全过。
