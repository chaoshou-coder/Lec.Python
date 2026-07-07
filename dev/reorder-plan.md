# 工具先行(Tools-First)模式 · Day03–Day13 重排方案

> 生成日期: 2026-07-07
> 模式: 条件第一 → 循环紧跟 → 字符串 → 列表 → 函数 → 字符串提升 → 列表进阶 → 函数进阶 → 字典 → 迭代/内置/递归 → 阶段复习②
> 参考标杆: CS50P (W0–W9)、MIT 6.0001
> 本文件为**规划文件**,不修改任何现有文件。所有改动需用户确认后由主 agent 执行。

---

## 1. 新 21 天进度表

> 说明: 表格新增"来源/备注"列,标注每个 Day 的内容来自旧计划的哪个 Day。Day01/02 和 Day14–21 不变。

| Day | 主题 | 关键新增 | 当堂 / 课后 / 小项目 | 来源/备注 |
|---|---|---|---|---|
| 01 | Python 与开发环境 | `print` `input` `type` `id` 变量 | 4 / 2 / 🎯 自我介绍 | **不变** |
| 02 | 数据类型与运算 | `int/float/str/bool` 算术/比较/逻辑 | 5 / 2 / 🎯 简易收银台 | **不变** |
| 03 | **条件分支** | `if/elif/else` 嵌套、逻辑运算组合、条件运算符(三元)、`random.randint()` `for...else` | 6 / 3 / 🎯 BMI 计算器 | **← 旧 Day06**(lesson06 整体迁入) |
| 04 | **循环入门** | `while` `for` `range` 转义 `\t` `end=`、嵌套循环、累加/累乘/计数 | 6 / 3 / 🌟 每日记账本 | **← 旧 Day05**(lesson05 整体迁入) |
| 05 | **字符串基础(极低量)** | 索引/切片/`len()`、`isdigit/isalpha/isalnum`、f-string/format、**replace() 仅做 1 个简单演示** | 5 / 2 / 🎯 手机号脱敏 | **← 旧 Day03**(lesson03 迁入,但 find/rfind/replace 主打题需移到 Day08) |
| 06 | **列表基础 CRUD** | 创建/索引、`append/insert/extend`、`pop/remove/del`、`sort/reverse`、`in` 运算符、嵌套列表 | 6 / 2 / 🎯 购物清单 | **← 旧 Day04**(lesson04 迁入,但 homework 含 `def` 需处理) |
| 07 | **函数入门 + 阶段复习① + 购物车** | `def` 四种形式 `return`、Day01-06 综合、购物车中型项目 | 6 / 3 / 🌟 阶段中型项目:购物车 | **← 旧 Day10**(lesson10 函数入门)+ 旧 Day07(购物车项目)合并 |
| 08 | **字符串提升** | `find/index/rfind/endswith/startswith/replace/split/join/title/strip` 完整用法 | 6 / 2 / 🎯 敏感词过滤器 | **← 旧 Day08**(lesson08)+ 旧 Day03 的 find/rfind/replace 主打题 |
| 09 | **列表进阶** | 切片进阶/列表生成式/二维/深浅拷贝 `*args` 引入 | 6 / 3 / 🌟 成绩统计表 | **← 旧 Day09**(lesson9 不变,已在正确位置) |
| 10 | **函数进阶** | 默认参数 `*args` `**kwargs` 混合顺序 组包/解包 `lambda` 入门 | 6 / 3 / 🌟 成语词典(函数版) | **← 旧 Day11**(lesson11 整体迁入) |
| 11 | **字典 + 集合** | 字典 CRUD、`keys/values/items`、嵌套字典、`set` 去重/交并差、`dict` 与 `list` 互转 | 6 / 3 / 🎯 通讯录 v1(字典版) | **← 新增锚点**(从 references.md §2.1 取素材,需新建 slides/习题) |
| 12 | **迭代 / 内置 / 递归** | `lambda` 进阶 `filter/map/sorted/max/min/sum/any/all` `global` `globals()` 递归 | 6 / 3 /  | **← 旧 Day12**(lesson12 不变,已在正确位置) |
| 13 | **阶段复习②** | Day08-12 综合 | 6 / 3 / 🌟 中型项目:控制台计算器(函数+异常) | **← 旧 Day13**(lesson13 不变) |
| 14 | 文件操作(基础) | `open/read/readline/readlines` `with` `'w/a/r/rb'` `print('…',file=)` encoding | 5 / 2 / 🎯 日志写入器 | **不变** |
| 15 | 文件操作(进阶) + `os` | `os.getcwd/listdir/remove/makedirs/rename/path.exists` | 6 / 2 / 🌟 批量重命名工具 | **不变** |
| 16 | 异常处理 | `try/except/else/finally` 常见异常类 `raise` 自定义异常 | 6 / 2 / 🎯 弹性输入助手 | **不变** |
| 17 | JSON 与 CSV | `json.load/loads/dump/dumps` `csv.reader/writer` + `with` | 5 / 2 / 🌟 个人账本(JSON 持久化) | **不变** |
| 18 | **阶段复习③** | Day14-17 综合 | 6 / 3 /  | **不变** |
| 19 | OOP(封装) | `class` `__init__(self,…)` 实例属性/方法 `_/__name` `@property` `__str__/__repr__` | 6 / 2 / 🎯 Student 类建模 | **不变** |
| 20 | OOP(继承 + 多态) | 单继承 `super().__init__()` 重写 多态 vs 实例属性 | 6 / 3 / 🎯 动物叫声 | **不变** |
| 21 | 期末总复习 + 作品展示 | Day01-20 错题串讲 + 学员秀 3 作品 + 查缺 | - / - / 🌟 图书管理系统 v2(中型项目答辩) | **不变** |

### 重排前后对照(仅 Day03–Day13)

| 新 Day | 新主题 | 旧 Day | 旧主题 |
|---|---|---|---|
| 03 | 条件分支 | 06 | 分支与嵌套 |
| 04 | 循环入门 | 05 | 循环入门 |
| 05 | 字符串基础(极低量) | 03 | 字符串(基础) |
| 06 | 列表基础 CRUD | 04 | 列表(基础) |
| 07 | 函数入门 + 阶段复习① + 购物车 | 07 | 阶段复习①(+购物车) |
| 08 | 字符串提升 | 08 | 字符串(提升) |
| 09 | 列表进阶 | 09 | 列表(进阶) |
| 10 | 函数进阶 | 11 | 函数进阶 |
| 11 | 字典 + 集合 | — | 新增锚点 |
| 12 | 迭代 / 内置 / 递归 | 12 | 迭代 / 内置 / 递归 |
| 13 | 阶段复习② | 13 | 阶段复习② |

---

## 2. 习题冲突清单(逐 Day 扫描)

### 2.1 新 Day03(条件分支) ← 旧 Day06 内容

**来源**: `lesson06/in_class/practice01-06.py` + `lesson06/homework/task01-03.py`

| 文件 | 当前 `[所属知识点]` | 冲突? | 建议 |
|---|---|---|---|
| `practice01.py` | `if/elif/else` | ✅ 无冲突 | 保留 |
| `practice02.py` | `if/elif/else + 闰年判断` | ✅ 无冲突 | 保留 |
| `practice03.py` | `if 嵌套` | ✅ 无冲突 | 保留 |
| `practice04.py` | `if/elif/else` | ✅ 无冲突 | 保留 |
| `practice05.py` | `if/elif/else + 算术` | ✅ 无冲突 | 保留 |
| `practice06.py` | `嵌套循环 + if` | ⚠️ 含"嵌套循环"字样 | 保留(循环在新 Day04 已学),但知识点声明建议改为 `if 嵌套 + 穷举法` |
| `task01.py` | `if/elif/else + 算术` | ✅ 无冲突 | 保留 |
| `task02.py` | `// + % + 算术 + if` | ✅ 无冲突 | 保留 |
| `task03.py` | `random.randint() + for/else + if/elif/else` | ⚠️ 含 `for/else` | 保留(循环已学),知识点声明建议简化为 `random + if/elif/else` |

**结论**: 旧 Day06 习题整体适配新 Day03,无需移动。

---

### 2.2 新 Day04(循环入门) ← 旧 Day05 内容

**来源**: `lesson05/in_class/practice01-06.py` + `lesson05/homework/task01-03.py`

| 文件 | 当前 `[所属知识点]` | 冲突? | 建议 |
|---|---|---|---|
| `practice01.py` | `while 循环` | ✅ 无冲突 | 保留 |
| `practice02.py` | `for + range(开始, 结束, 步长)` | ✅ 无冲突 | 保留 |
| `practice03.py` | `嵌套循环 + end=''` | ✅ 无冲突 | 保留 |
| `practice04.py` | `while + // + 计数` | ✅ 无冲突 | 保留 |
| `practice05.py` | `while + if/else + 累加 + 累乘` | ⚠️ 含 `if/else` | 保留(分支在新 Day03 已学),OK |
| `practice06.py` | `嵌套循环 + end=''` | ✅ 无冲突 | 保留 |
| `task01.py` | `嵌套循环 + 空格 + 星号` | ✅ 无冲突 | 保留 |
| `task02.py` | `time.sleep() + 循环` | ✅ 无冲突 | 保留 |
| `task03.py` | `逆推 + 循环` | ✅ 无冲突 | 保留 |

**结论**: 旧 Day05 习题整体适配新 Day04,无需移动。

---

### 2.3 新 Day05(字符串基础·极低量) ← 旧 Day03 内容(筛选后)

**来源**: `lesson03/in_class/practice01-05.py` + `lesson03/homework/task01-02.py` + `lesson03/mini_project/phone_masking.py`

⚠️ **核心约束**: Day05 仅做极低量引入,`find/rfind/replace` 不得作为主打知识点(应移到 Day08)。

| 文件 | 当前 `[所属知识点]` | 冲突? | 建议 |
|---|---|---|---|
| `practice01.py` | `字符串查找与切片` | ⚠️ **主打 `find()`** | **移到 Day08**(字符串提升) |
| `practice02.py` | `字符串长度与数字判断` | ✅ 用 `len()` + `isdigit()`,OK | **保留** |
| `practice03.py` | `字符串正反查找` | ⚠️ **主打 `find()` 与 `rfind()`** | **移到 Day08** |
| `practice04.py` | `rfind() 与切片` | ⚠️ **主打 `rfind()`** | **移到 Day08** |
| `practice05.py` | `切片与类型转换` | ✅ 切片 + f-string + `int()` 去前导零 | **保留** |
| `task01.py` | `字符串替换` | ⚠️ **主打 `replace()`** | **移到 Day08** |
| `task02.py` | `find() 与切片` | ⚠️ **主打 `find()`** | **移到 Day08** |
| `mini_project/phone_masking.py` | `字符串切片、长度与数字判断、格式化输出` | ✅ 仅用 `len()` + `isdigit()` + 切片 + f-string | **保留**(完美适配极低量定位) |

**结论**: 旧 Day03 的 8 个习题中,**保留 3 个**(practice02/practice05/phone_masking),**移动 5 个**(practice01/practice03/practice04/task01/task02)到 Day08。

---

### 2.4 新 Day06(列表基础 CRUD) ← 旧 Day04 内容

**来源**: `lesson04/in_class/practice01-06.py` + `lesson04/homework/task01-02.py`

| 文件 | 当前 `[所属知识点]` | 冲突? | 建议 |
|---|---|---|---|
| `practice01.py` | `列表创建与索引` | ✅ 无冲突 | 保留 |
| `practice02.py` | `append() 与 while 循环` | ⚠️ 含 `while` | 保留(循环在新 Day04 已学),OK |
| `practice03.py` | `循环累加与比较` | ⚠️ 含循环 | 保留(循环已学),OK |
| `practice04.py` | `in 运算符` | ✅ 无冲突 | 保留 |
| `practice05.py` | `列表增删与循环菜单` | ⚠️ 含循环 + 菜单 | 保留(循环已学),OK |
| `practice06.py` | `列表索引与 f-string` | ✅ 无冲突 | 保留 |
| `task01.py` | `切片与循环` | ⚠️ **含 `def list_to_2d()`** | **[待用户确认]** — 见下文 |
| `task02.py` | `循环、in 运算符、append()` | ⚠️ **含 `def remove_dup()`** | **[待用户确认]** — 见下文 |

#### ⚠️ 关键冲突: lesson04/homework 含 `def` 函数定义

- `task01.py` 第 20 行: `def list_to_2d(lst):`
- `task02.py` 第 19 行: `def remove_dup(lst):`

**问题**: 按"工具先行"约束,Day01–Day06 不应出现 `def`。但新 Day06 是列表基础课,学员尚未学函数(Day07 才学)。

**建议方案(待用户确认)**:
- **方案 A**: 将这两道题从 homework 移到 Day07(函数入门)的 in_class,作为"函数 + 列表"综合题。
- **方案 B**: 将这两道题改为"不定义函数,直接写脚本"版本(去掉 `def`,改为顺序执行)。
- **方案 C**: 保留在 Day06 homework 但标注为"预习题",提示学员"先感受函数形态,下节详细讲"。

---

### 2.5 新 Day07(函数入门 + 阶段复习① + 购物车) ← 旧 Day10 + 旧 Day07

**来源**: `lesson10/in_class/practice01-06.py` + `lesson10/homework/task01-03.py` + `lesson07/in_class/practice01-06.py` + `lesson07/homework/task01-03.py`

#### 2.5.1 函数入门部分(旧 lesson10)

| 文件 | 当前 `[所属知识点]` | 冲突? | 建议 |
|---|---|---|---|
| `practice01.py` | `def + 无返回值` | ✅ 无冲突 | 保留 |
| `practice02.py` | `def + return` | ✅ 无冲突 | 保留 |
| `practice03.py` | `def + return + 布尔` | ✅ 无冲突 | 保留 |
| `practice04.py` | `def + if/else + return` | ✅ 无冲突 | 保留 |
| `practice05.py` | `def + 循环 + in + return` | ✅ 无冲突 | 保留 |
| `practice06.py` | `def + 循环 + return` | ✅ 无冲突 | 保留 |
| `task01.py` | `def + 算术` | ✅ 无冲突 | 保留 |
| `task02.py` | `def + 循环 + if + return` | ✅ 无冲突 | 保留 |
| `task03.py` | `def + 循环 + 字符串拼接` | ✅ 无冲突 | 保留 |

#### 2.5.2 阶段复习 + 购物车部分(旧 lesson07)

| 文件 | 当前 `[所属知识点]` | 冲突? | 建议 |
|---|---|---|---|
| `practice01.py` | `Day01-Day02 综合 + f-string 对齐` | ✅ 无冲突 | 保留 |
| `practice02.py` | `Day03 字符串 + Day04 列表 + Day05 字典` | ⚠️ **含 `def parse_csv()` + 字典** | **[待用户确认]** — 见下文 |
| `practice03.py` | `Day04 列表 + Day05 循环 + Day06 分支` | ⚠️ 引用旧 Day 编号 | 保留,但需更新知识点声明为"列表 + 循环 + 分支" |
| `practice04.py` | `Day04 嵌套列表 + Day05 循环 + Day06 分支` | ⚠️ 引用旧 Day 编号 | 保留,更新声明 |
| `practice05.py` | `Day06 分支 + Day02 算术` | ⚠️ 引用旧 Day 编号 | 保留,更新声明 |
| `practice06.py` | `Day01-Day06 大综合` | ✅ 无冲突 | 保留 |
| `task01.py` | `Day05-Day06 综合 + 状态追踪` | ⚠️ 引用旧 Day 编号 | 保留,更新声明 |
| `task02.py` | `Day06 分支 + Day05 循环 + 函数封装` | ✅ 含函数封装,正好适配新 Day07 | 保留 |
| `task03.py` | `Day04 列表 + Day05 循环 + 文件写入` | ⚠️ 含文件写入(`with open`) | **[待用户确认]** — 文件操作是 Day14 内容 |

#### ⚠️ 关键冲突 1: lesson07/practice02.py 含 `def` + 字典

- 第 26 行: `def parse_csv(csv_string: str) -> dict:`
- 涉及字典推导/循环创建字典

**问题**: 新 Day07 是函数入门 + 购物车项目日,学员刚学函数,做这道题 OK。但**字典**在新 Day11 才系统学。

**建议**: 保留此题,但将"字典"改为"嵌套列表"实现(用 `[['col1', '苹果'], ['col2', '5.5'], ...]` 代替字典),或标注为"预习题"。[待用户确认]

#### ⚠️ 关键冲突 2: lesson07/task03.py 含文件写入

- 题目要求"把购物车数据导出到一个文本文件"(`with open`)
- 文件操作是 Day14 内容

**建议**: 保留此题,但标注为"拓展选做",提示学员"先用 `print()` 模拟输出,下学期学文件后再回来实现"。或移到 Day14 作为文件操作课的引入题。[待用户确认]

---

### 2.6 新 Day08(字符串提升) ← 旧 Day08 + 旧 Day03 的 find/rfind/replace 主打题

**来源**: `lesson08/in_class/practice01-06.py` + `lesson08/homework/task01-02.py` + 从 lesson03 迁入的 5 个题

| 文件 | 当前 `[所属知识点]` | 冲突? | 建议 |
|---|---|---|---|
| `practice01.py` | `字符串find()` | ✅ 无冲突 | 保留 |
| `practice02.py` | `字符串replace()` | ✅ 无冲突 | 保留 |
| `practice03.py` | `字符串split()` | ✅ 无冲突 | 保留 |
| `practice04.py` | `字符串join()` | ✅ 无冲突 | 保留 |
| `practice05.py` | `字符串title()` | ✅ 无冲突 | 保留 |
| `practice06.py` | `strip() / lstrip() / rstrip()` | ✅ 无冲突 | 保留 |
| `task01.py` | `find() + 切片` | ✅ 无冲突 | 保留 |
| `task02.py` | `循环 + replace()` | ✅ 无冲突 | 保留 |

**从 lesson03 迁入的题**:
- `practice01.py`(原 lesson03)→ 重命名为 `practice07.py` 或合并
- `practice03.py`(原 lesson03)→ 重命名为 `practice08.py`
- `practice04.py`(原 lesson03)→ 重命名为 `practice09.py`
- `task01.py`(原 lesson03)→ 重命名为 `task03.py`
- `task02.py`(原 lesson03)→ 重命名为 `task04.py`

**结论**: Day08 内容充实,可容纳 9 道 in_class + 4 道 homework。需确认题号重命名方案。[待用户确认]

---

### 2.7 新 Day09(列表进阶) ← 旧 Day09 内容

**来源**: `lesson09/in_class/practice01-06.py` + `lesson09/homework/task01-03.py`

| 文件 | 当前 `[所属知识点]` | 冲突? | 建议 |
|---|---|---|---|
| `practice01.py` | `切片` | ✅ 无冲突 | 保留 |
| `practice02.py` | `列表生成式` | ✅ 无冲突 | 保留 |
| `practice03.py` | `嵌套循环 + 二维列表` | ✅ 无冲突 | 保留 |
| `practice04.py` | `循环 + in + append` | ✅ 无冲突 | 保留 |
| `practice05.py` | `copy.copy() / copy.deepcopy()` | ✅ 无冲突 | 保留 |
| `practice06.py` | `函数 + 二维列表 + CRUD` | ⚠️ 含 `def` | 保留(函数在新 Day07 已学),OK |
| `task01.py` | `列表生成式 + 二维列表` | ✅ 无冲突 | 保留 |
| `task02.py` | `sort(key=lambda x: ...)` | ⚠️ 含 `lambda` | **[待用户确认]** — lambda 在新 Day10 才学 |
| `task03.py` | `递归 + 列表` | ⚠️ 含递归 | **[待用户确认]** — 递归在新 Day12 才学 |

#### ⚠️ 冲突: task02 含 lambda、task03 含递归

**建议**:
- `task02.py`: 保留,但提示学员"先用普通函数写 `key=`,下节学 lambda 后再改写"。或移到 Day10。
- `task03.py`: 移到 Day12(递归专题),或保留但标注为"挑战选做"。

---

### 2.8 新 Day10(函数进阶) ← 旧 Day11 内容

**来源**: `lesson11/in_class/practice01-06.py` + `lesson11/homework/task01-03.py`

| 文件 | 当前 `[所属知识点]` | 冲突? | 建议 |
|---|---|---|---|
| `practice01.py` | `默认参数` | ✅ 无冲突 | 保留 |
| `practice02.py` | `*args` | ✅ 无冲突 | 保留 |
| `practice03.py` | `**kwargs` | ✅ 无冲突 | 保留 |
| `practice04.py` | `默认参数 + if/elif/else` | ✅ 无冲突 | 保留 |
| `practice05.py` | `lambda + sort(key=...)` | ⚠️ 含 `lambda` | 保留(lambda 在新 Day10 函数进阶课引入),OK |
| `practice06.py` | `混合参数顺序` | ✅ 无冲突 | 保留 |
| `task01.py` | `默认参数 + 算术` | ✅ 无冲突 | 保留 |
| `task02.py` | `默认参数 + 循环 + 列表` | ✅ 无冲突 | 保留 |
| `task03.py` | `**kwargs + 字典` | ⚠️ 含字典 | **[待用户确认]** — 字典在新 Day11 才学 |

#### ⚠️ 冲突: task03 含字典

- `create_user("张三", age=20, city="成都")` → `{'name': '张三', 'age': 20, 'city': '成都'}`

**建议**: 保留此题,因为 `**kwargs` 本身就是"收集为字典",学员在 Day10 自然接触字典结构。可在 Day11 系统学时回顾此题。

---

### 2.9 新 Day11(字典 + 集合) ← 新增锚点

**来源**: 需新建(当前 lesson11 是函数进阶内容,已迁到新 Day10)

**缺失内容**: 见第 3 节"缺失内容清单"。

---

### 2.10 新 Day12(迭代 / 内置 / 递归) ← 旧 Day12 内容

**来源**: `lesson12/in_class/practice01-06.py` + `lesson12/homework/task01-03.py`

| 文件 | 当前 `[所属知识点]` | 冲突? | 建议 |
|---|---|---|---|
| `practice01.py` | `lambda 匿名函数` | ✅ 无冲突 | 保留 |
| `practice02.py` | `filter() + lambda` | ✅ 无冲突 | 保留 |
| `practice03.py` | `map() + lambda` | ✅ 无冲突 | 保留 |
| `practice04.py` | `all() 和 any()` | ✅ 无冲突 | 保留 |
| `practice05.py` | `递归` | ✅ 无冲突 | 保留 |
| `practice06.py` | `递归` | ✅ 无冲突 | 保留 |
| `task01.py` | `sorted() + reverse` | ✅ 无冲突 | 保留 |
| `task02.py` | `sorted(key=lambda x: ...)` | ⚠️ 含字典列表 | 保留(字典在新 Day11 已学),OK |
| `task03.py` | `递归` | ✅ 无冲突 | 保留 |

**结论**: 旧 Day12 习题整体适配新 Day12,无需移动。

---

### 2.11 新 Day13(阶段复习②) ← 旧 Day13 内容

**来源**: `lesson13/in_class/practice01-06.py` + `lesson13/homework/task01-03.py`

| 文件 | 当前 `[所属知识点]` | 冲突? | 建议 |
|---|---|---|---|
| `practice01.py` | `函数 + 字符串` | ✅ 无冲突 | 保留 |
| `practice02.py` | `*args` | ✅ 无冲突 | 保留 |
| `practice03.py` | `sorted(key=lambda x: ...)` | ✅ 无冲突 | 保留 |
| `practice04.py` | `filter() + lambda` | ✅ 无冲突 | 保留 |
| `practice05.py` | `递归 + 列表` | ✅ 无冲突 | 保留 |
| `practice06.py` | `Day08-12 综合` | ⚠️ 引用旧 Day 编号 | 保留,更新声明为"函数 + lambda + filter + 列表综合" |
| `task01.py` | `函数 + 字符串解析` | ✅ 无冲突 | 保留 |
| `task02.py` | `函数 + 循环 + 分支` | ✅ 无冲突 | 保留 |
| `task03.py` | `函数 + 列表 + 循环` | ✅ 无冲突 | 保留 |

**结论**: 旧 Day13 习题整体适配新 Day13,无需移动。

---

## 3. 缺失内容清单

### 3.1 Day11 字典 + 集合(需完全新建)

当前 `lesson11/` 是函数进阶内容(已迁到新 Day10),需**完全重写**为字典 + 集合主题。

| 需新建项 | 状态 | 素材来源 |
|---|---|---|
| `lesson11/slides.md` | ❌ 需新建 | references.md §2.1 第 17 题(字典统计词频)、第 73 行(通讯录 v1); py4e Ch9; PCC Ch6 |
| `lesson11/in_class/practice01-06.py` | ❌ 需新建 | 参考 py4e Ch9 练习、PCC Ch6 练习 |
| `lesson11/homework/task01-03.py` | ❌ 需新建 | 参考 py4e Ch9 练习、PCC Ch6 练习 |
| `lesson11/mini_project/` | ❌ 需新建 | 通讯录 v1(字典版)、单词本 v1 |
| `lesson11/demo/` | ❌ 需新建 | 字典 CRUD 演示脚本 |
| `lesson11/README.md` | ❌ 需新建 | — |
| `lesson11/teacher_notes.md` | ❌ 需新建 | — |

**建议知识点分布**:
- 字典 CRUD:`d[key]`、`d.get(key, default)`、`d.keys()`、`d.values()`、`d.items()`
- 字典嵌套:列表套字典(学生信息)、字典套字典(通讯录)
- 集合:`set()` 去重、`&` `|` `-` `^` 交并差
- `dict` 与 `list` 互转:`list(d.items())`、`dict(lst)`
- 综合项目:通讯录 v1(增删改查 + 字典存储)

### 3.2 Day05 字符串基础(极低量)的习题缺口

从 lesson03 迁入后,Day05 仅保留 3 个题(practice02/practice05/phone_masking),**不足 5/2/🎯 的标准配置**。

| 需补充项 | 数量 | 说明 |
|---|---|---|
| `in_class/practiceXX.py` | 2~3 道 | 补充索引/切片/isdigit/f-string 基础题(不含 find/rfind/replace) |
| `homework/taskXX.py` | 1~2 道 | 补充字符串基础练习题 |

**建议方向**:
- 字符串索引与切片基础(取首字符、末字符、子串)
- `len()` + 字符串拼接
- `isdigit()` / `isalpha()` / `isalnum()` 输入校验
- f-string 格式化输出(对齐、保留小数)

### 3.3 mini_project 缺口

| Day | 当前状态 | summary.md 标注 | 缺口 |
|---|---|---|---|
| 03 | `lesson03/mini_project/` 有 phone_masking.py(但这是旧 Day03 的) | 🎯 BMI 计算器 | 需新建 BMI 计算器(条件分支主题) |
| 04 | `lesson04/mini_project/` 空 | 🌟 每日记账本 | 需新建每日记账本(循环主题) |
| 05 | `lesson05/mini_project/` 空(迁入 phone_masking.py) | 🎯 手机号脱敏 | phone_masking.py 已迁入,OK |
| 06 | `lesson06/mini_project/` 空 | 🎯 购物清单 | 需新建购物清单(列表 CRUD 主题) |
| 07 | `lesson07/mini_project/` 空 | 🌟 购物车 | 购物车项目在 weekly_projects/week01,OK |
| 08 | `lesson08/mini_project/` 空 | 🎯 敏感词过滤器 | 需新建敏感词过滤器(字符串提升主题) |
| 09 | `lesson09/mini_project/` 空 | 🌟 成绩统计表 | 需新建成绩统计表(列表进阶主题) |
| 10 | `lesson10/mini_project/` 空 | 🌟 成语词典(函数版) | 需新建成语词典(函数进阶主题) |
| 11 | `lesson11/mini_project/` 空 | 🎯 通讯录 v1(字典版) | 需新建通讯录 v1(字典主题) |
| 12 | `lesson12/mini_project/` 空 | — | 无小项目,OK |
| 13 | `lesson13/mini_project/` 空 | 🌟 控制台计算器 | 控制台计算器在 homework/task02,OK |

---

## 4. 迁移执行清单

> 以下清单按执行顺序排列。每项完成后打勾 `[x]`。

### 阶段 0: 前置准备

- [ ] **确认本方案**: 用户审阅 `dev/reorder-plan.md`,确认所有 `[待用户确认]` 项的裁定
- [ ] **备份当前状态**: 执行 `TIMESTAMP=$(date +%Y%m%d-%H%M%S) && cp -r lesson*/ .versions/lessons-v1-before-reorder-${TIMESTAMP}/`

### 阶段 1: 处理 Day11 字典(完全新建,无冲突)

- [ ] **Day11**: 新建 `lesson11/slides.md` —— 字典 + 集合主题(参考 py4e Ch9、PCC Ch6)
- [ ] **Day11**: 新建 `lesson11/in_class/practice01-06.py` —— 6 道当堂练(字典 CRUD、keys/values/items、嵌套字典、集合去重/交并差)
- [ ] **Day11**: 新建 `lesson11/homework/task01-03.py` —— 3 道课后作业
- [ ] **Day11**: 新建 `lesson11/mini_project/` —— 通讯录 v1(字典版)
- [ ] **Day11**: 新建 `lesson11/demo/` —— 字典 CRUD 演示脚本
- [ ] **Day11**: 新建 `lesson11/README.md` 和 `lesson11/teacher_notes.md`
- [ ] **Day11**: 清空旧 `lesson11/` 的函数进阶内容(已迁到新 Day10)

### 阶段 2: Day03–Day06 重排(条件/循环/字符串/列表)

- [ ] **Day03**: 将 `lesson06/` 的 slides/习题/小项目 迁移到 `lesson03/`(条件分支主题)
- [ ] **Day03**: 更新 `lesson03/in_class/practice06.py` 知识点声明(去掉"嵌套循环"字样,改为"if 嵌套 + 穷举法")
- [ ] **Day03**: 新建 `lesson03/mini_project/` —— BMI 计算器(条件分支主题)
- [ ] **Day03**: 清空旧 `lesson03/` 的字符串基础内容(部分迁入新 Day05,部分移到 Day08)
- [ ] **Day04**: 将 `lesson05/` 的 slides/习题/小项目 迁移到 `lesson04/`(循环入门主题)
- [ ] **Day04**: 新建 `lesson04/mini_project/` —— 每日记账本(循环主题)
- [ ] **Day04**: 清空旧 `lesson04/` 的列表基础内容(迁入新 Day06)
- [ ] **Day05**: 将 `lesson03/` 的 slides(筛选后)迁移到 `lesson05/` —— 仅保留索引/切片/len/isdigit/f-string 内容
- [ ] **Day05**: 从 `lesson03/in_class/` 筛选保留 `practice02.py`(len+isdigit)、`practice05.py`(切片+身份证),移到 `lesson05/in_class/`
- [ ] **Day05**: 从 `lesson03/homework/` 筛选 —— **全部迁走**(task01=replace 主打,task02=find 主打,均移到 Day08)
- [ ] **Day05**: 保留 `lesson03/mini_project/phone_masking.py` 在 `lesson05/mini_project/`
- [ ] **Day05**: 新建 2~3 道 in_class 题 + 1~2 道 homework 题(补充字符串基础练习,不含 find/rfind/replace)
- [ ] **Day06**: 将 `lesson04/` 的 slides/习题 迁移到 `lesson06/`(列表基础 CRUD 主题)
- [ ] **Day06**: 处理 `lesson04/homework/task01-02.py` 含 `def` 的问题(见 2.4 节方案 A/B/C)
- [ ] **Day06**: 新建 `lesson06/mini_project/` —— 购物清单(列表 CRUD 主题)

### 阶段 3: Day07 函数入门 + 阶段复习① + 购物车(合并日)

- [ ] **Day07**: 将 `lesson10/` 的 slides/习题/小项目 迁移到 `lesson07/`(函数入门部分)
- [ ] **Day07**: 将 `lesson07/` 的阶段复习+购物车习题 合并到 `lesson07/`(注意去重)
- [ ] **Day07**: 处理 `lesson07/in_class/practice02.py` 含字典的问题(见 2.5.2 节)
- [ ] **Day07**: 处理 `lesson07/homework/task03.py` 含文件写入的问题(见 2.5.2 节)
- [ ] **Day07**: 更新所有习题的知识点声明(去掉旧 Day 编号引用)
- [ ] **Day07**: 确认 `weekly_projects/week01_shopping_cart/README.md` 验收标准与 Day07 对齐

### 阶段 4: Day08–Day10 字符串提升/列表进阶/函数进阶

- [ ] **Day08**: 将 `lesson08/` 保持原位(字符串提升主题)
- [ ] **Day08**: 将 `lesson03/in_class/practice01.py`、`practice03.py`、`practice04.py` 迁入 `lesson08/in_class/`,重命名为 `practice07-09.py`
- [ ] **Day08**: 将 `lesson03/homework/task01.py`、`task02.py` 迁入 `lesson08/homework/`,重命名为 `task03-04.py`
- [ ] **Day08**: 新建 `lesson08/mini_project/` —— 敏感词过滤器
- [ ] **Day09**: 保持 `lesson09/` 不变(列表进阶主题)
- [ ] **Day09**: 处理 `lesson09/homework/task02.py`(lambda)和 `task03.py`(递归)的冲突(见 2.7 节)
- [ ] **Day09**: 新建 `lesson09/mini_project/` —— 成绩统计表
- [ ] **Day10**: 将 `lesson11/` 的 slides/习题/小项目 迁移到 `lesson10/`(函数进阶主题)
- [ ] **Day10**: 处理 `lesson11/homework/task03.py` 含字典的问题(见 2.8 节)
- [ ] **Day10**: 新建 `lesson10/mini_project/` —— 成语词典(函数版)

### 阶段 5: Day12–Day13 保持不变

- [ ] **Day12**: 保持 `lesson12/` 不变(迭代/内置/递归主题)
- [ ] **Day13**: 保持 `lesson13/` 不变(阶段复习② + 控制台计算器)

### 阶段 6: 收尾

- [ ] **更新 summary.md**: 替换 Day03–Day13 行,添加"来源/备注"列
- [ ] **更新 CLAUDE.md**: 更新"当前进度"和"待做"清单
- [ ] **更新 CHANGELOG.md**: 记录本次重排的版本变更
- [ ] **全量扫描**: 运行所有 `practiceNN.py` 和 `taskNN.py`,确认无语法错误
- [ ] **更新 teacher_notes.md**: 标注每个 Day 的主题变更

---

## 5. 给主 agent 的交接说明

### 5.1 需要用户确认的裁定(共 6 项)

在执行迁移前,请用户确认以下裁定:

1. **[裁定 1] lesson04/homework/task01-02.py 含 `def` 的处理方案**
   - 方案 A: 移到 Day07 函数入门课
   - 方案 B: 改为无函数版本
   - 方案 C: 保留为预习题

2. **[裁定 2] lesson07/in_class/practice02.py 含字典的处理方案**
   - 方案 A: 保留,改为嵌套列表实现
   - 方案 B: 保留为"预习题"
   - 方案 C: 移到 Day11 字典课

3. **[裁定 3] lesson07/homework/task03.py 含文件写入的处理方案**
   - 方案 A: 保留为"拓展选做"
   - 方案 B: 移到 Day14 文件操作课

4. **[裁定 4] lesson09/homework/task02.py(lambda)和 task03.py(递归)的处理方案**
   - 方案 A: 保留,标注为"挑战选做"
   - 方案 B: 移到对应专题 Day

5. **[裁定 5] Day08 题号重命名方案**
   - 方案 A: 迁入题重命名为 practice07-09 / task03-04
   - 方案 B: 重新编号 practice01-09 / task01-04

6. **[裁定 6] Day11 字典课的练习数量**
   - 方案 A: 6 道 in_class + 3 道 homework(标准配置)
   - 方案 B: 4 道 in_class + 2 道 homework(精简配置,留时间做通讯录项目)

### 5.2 执行注意事项

1. **不要修改现有文件**: 本方案只写 `dev/reorder-plan.md`,所有改动需用户确认后由主 agent 执行。
2. **题号连续性**: 迁入新 Day 后,确保 `practiceNN.py` 和 `taskNN.py` 的 NN 连续无跳号。
3. **知识点声明同步**: 迁入后需更新每道题的 `[所属知识点: xxx]` 声明,去掉旧 Day 编号引用。
4. **README 同步**: 每个 Day 的 `README.md` 需更新主题/习题/项目表。
5. **slides.md 同步**: 每个 Day 的 `slides.md` 需重写为对应主题(或从迁入来源复制后调整)。
6. **teacher_notes.md 清空**: 迁入后需清空旧的教师备忘,由新教师填写。

### 5.3 风险提示

1. **Day07 内容膨胀风险**: 新 Day07 合并了函数入门(6+3 题)+ 阶段复习(6+3 题)= 18 道题,可能超出 6 小时课时容量。建议:
   - 函数入门部分精选 4 道核心题(practice01-04)
   - 阶段复习部分精选 4 道核心题(practice01/03/04/06)
   - 其余题为"选做"或移到 homework

2. **Day08 习题过多风险**: 迁入后 Day08 可能有 9 道 in_class + 4 道 homework。建议:
   - 精选 6 道 in_class + 2 道 homework
   - 其余题为"拓展选做"

3. **Day11 字典课新建工作量**: 需从零创建 slides/习题/小项目,约 4~6 小时工作量。建议优先从 references.md §2.1 第 17 题(字典统计词频)和第 73 行(通讯录 v1)取素材。

4. **购物车项目函数依赖**: `weekly_projects/week01_shopping_cart/README.md` 验收标准要求"用函数封装每个功能"(30 分),新 Day07 学员刚学函数,可能不够熟练。建议:
   - Day07 下午专门安排"函数封装实战"环节
   - 提供函数模板脚手架(降低入门门槛)

---

## 6. 附录: 迁移映射表(文件级)

| 原文件 | 新位置 | 操作 |
|---|---|---|
| `lesson06/in_class/practice01-06.py` | `lesson03/in_class/practice01-06.py` | 复制 |
| `lesson06/homework/task01-03.py` | `lesson03/homework/task01-03.py` | 复制 |
| `lesson05/in_class/practice01-06.py` | `lesson04/in_class/practice01-06.py` | 复制 |
| `lesson05/homework/task01-03.py` | `lesson04/homework/task01-03.py` | 复制 |
| `lesson03/in_class/practice02.py` | `lesson05/in_class/practice01.py` | 复制+重命名 |
| `lesson03/in_class/practice05.py` | `lesson05/in_class/practice02.py` | 复制+重命名 |
| `lesson03/mini_project/phone_masking.py` | `lesson05/mini_project/phone_masking.py` | 复制 |
| `lesson03/in_class/practice01.py` | `lesson08/in_class/practice07.py` | 复制+重命名 |
| `lesson03/in_class/practice03.py` | `lesson08/in_class/practice08.py` | 复制+重命名 |
| `lesson03/in_class/practice04.py` | `lesson08/in_class/practice09.py` | 复制+重命名 |
| `lesson03/homework/task01.py` | `lesson08/homework/task03.py` | 复制+重命名 |
| `lesson03/homework/task02.py` | `lesson08/homework/task04.py` | 复制+重命名 |
| `lesson04/in_class/practice01-06.py` | `lesson06/in_class/practice01-06.py` | 复制 |
| `lesson04/homework/task01.py` | `lesson06/homework/task01.py` 或移走 | [待用户确认] |
| `lesson04/homework/task02.py` | `lesson06/homework/task02.py` 或移走 | [待用户确认] |
| `lesson10/in_class/practice01-06.py` | `lesson07/in_class/practice01-06.py` | 复制 |
| `lesson10/homework/task01-03.py` | `lesson07/homework/task01-03.py` | 复制 |
| `lesson11/in_class/practice01-06.py` | `lesson10/in_class/practice01-06.py` | 复制 |
| `lesson11/homework/task01-03.py` | `lesson10/homework/task01-03.py` | 复制 |
| `lesson11/slides.md` | `lesson10/slides.md` | 复制+调整 |
| `lesson11/`(全部字典内容) | `lesson11/` | 完全新建 |

---

> **本文件结束**
> 下一步: 请用户确认 6 项裁定后,由主 agent 按"迁移执行清单"执行。
