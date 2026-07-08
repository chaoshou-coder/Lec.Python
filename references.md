# Python 入门到 AI 就绪工程师 · 教学参考资料库

> 调研日期:2026-07-07
> 用途:为 60 天课程的 slides / in_class / homework 提供"素材池"
> 信息来源:Coursera、edX、MIT OCW、B 站、GitHub、知乎、菜鸟教程、W3CSchool、廖雪峰、莫烦、Harvard CS50P、Think Python 2E 等
> 原则:自己归纳不照抄原文;每格 ≤ 20 字;未搜到外部素材的章节显式标注

---

## 1. 推荐课程一览(机构 + 特点 + 适合人群)

| # | 课程 | 来源 | 适合人群 | 特点 |
|---|---|---|---|---|
| 1 | **MIT 6.0001**(Introduction to CS using Python) | MIT OCW / MITx 6.0.1x(edX) | 有或无编程基础 | 6 套 PS,项目驱动(猜字/密码/订阅过滤) |
| 2 | **MIT 6.0002**(Introduction to Computational Thinking) | MIT OCW / MITx 6.0.2x(edX) | 已完成 6.0001 学员 | 模拟/拟合/蒙特卡罗,可做 Day14–17 拔高素材 |
| 3 | **Python for Everybody**(Specialization) | Coursera(Dr. Chuck) | 零基础学员、自学者 | 5 门课约 80h,自动评分,Capstone(爬+SQLite+可视化) |
| 4 | **Harvard CS50P** | Harvard/edX | 喜欢"做中学"的高中/大学生 | 10 周每周 4–6 题,check50 自动评测,Final Project 自选 |
| 5 | **Automate the Boring Stuff with Python**(Al Sweigart) | 免费在线阅读 | 办公室/白领、兴趣驱动 | 34 个真实场景项目(PDF/Excel/爬虫/发邮件) |
| 6 | **Python Crash Course 3rd Ed.**(Eric Matthes) | No Starch Press | 零基+喜欢"边读边练" | 两部分(基础 + 项目),500+ 编号练习,3 大项目 |
| 7 | **Think Python 2E**(Allen B. Downey) | Green Tea Press(免费 PDF) | 想理解计算思维的学习者 | 每章 3–10 题,4 个 Case Study(龟/单词/Markov/扑克) |
| 8 | **廖雪峰 Python 教程** | liaoxuefeng.com | 中文纯零基础 | 覆盖面极广,教科书式结构,无系统习题 |
| 9 | **莫烦 Python** | B 站 / GitHub / mofanpy.com | 对 ML/NLP 方向感兴趣 | 视频驱动,强项在 ML/数据,基础部分偏略 |
| 10 | **小甲鱼 零基础入门学 Python** | B 站 / 鱼 C 论坛 | 短视频学习者 | 98 课,OOP 讲得最深(含元类/描述符),3 大项目 |
| 11 | **黑马程序员 28 天 Python** | B 站 / 传智播客 | 就业导向、视频优先 | 28 天紧凑计划,含名片系统 + 飞机大战 |
| 12 | **菜鸟教程 Python 3** | runoob.com | 碎片化查阅 + 刷 100 例 | 每节可在线运行,100 例答案公开 |
| 13 | **W3CSchool Python** | w3cschool.cn / w3schools.com | 浏览器内即学即练 | 每节配 Exercises,含 Quiz、Bootcamp、面试题 |
| 14 | **Python.org 官方 Tutorial** | docs.python.org/3/tutorial/ | 有其他语言经验者 | 权威精炼,无配套习题,适合"语法字典" |

---

## 2. 分主题的"优秀习题 / 小项目"摘录

> ⭐ 难度约定:⭐ 纯语法复制 / ⭐⭐ 单步变形 / ⭐⭐⭐ 组合 2–3 知识点 / ⭐⭐⭐⭐ 抽象建模或递归 / ⭐⭐⭐⭐⭐ 综合项目 / 多文件

---

### 2.1 Python 核心(Day01–Day10)

> 对应 Module 0 前半段。以下习题已在 course/lesson01-10 中参考并实现。

#### 推荐习题(难度:⭐ ~ ⭐⭐⭐⭐)

| 题号 | 题目描述 | 难度 | 来源 | 可嵌入我们的 Day |
|---|---|---|---|---|
| 1 | 温度换算器(°C↔°F),支持双向 | ⭐ | PCC Ch2 | 01 |
| 2 | 奇偶判断 + 4 整除提示 | ⭐ | CS50P Week0 Einstein | 02 |
| 3 | 小写化输入字符串(Indoor Voice) | ⭐ | CS50P Week0 | 02 |
| 4 | 字符串替换表情符号(Making Faces) | ⭐⭐ | CS50P Week0 | 02 |
| 5 | Tip Calculator(餐费分账,四舍五入) | ⭐⭐ | CS50P Week0 | 03 |
| 6 | 九九乘法表,右对齐输出 | ⭐⭐ | 小甲鱼 P36 | 04 |
| 7 | 打印小星星斜三角/倒三角 | ⭐⭐ | 黑马 | 04 |
| 8 | 石头剪刀布人机对战 | ⭐⭐ | 小甲鱼 P58 | 03 |
| 9 | 猜数字(1–100,提示大小) | ⭐⭐⭐ | 黑马 | 04 |
| 10 | FizzBuzz(1–100 输出) | ⭐ | py4e Ch2 | 04 |
| 11 | 回文数/字符串判别 | ⭐⭐ | w3resource Basic | 02 |
| 12 | 计算两点距离 | ⭐⭐ | PCC Ch02 | 06 |
| 13 | 计算复利 n 年后总额 | ⭐⭐ | py4e Ch3 | 03 |
| 14 | BMI 计算器 + 健康提示 | ⭐ | Think Python 2E | 03 |
| 15 | 闰年判断(含逻辑运算) | ⭐⭐ | CS50P | 03 |
| 14 | BMI 计算器 + 健康提示 | ⭐ | Think Python 2E Ex1-2 | 06 |
| 15 | ASCII 字符 ↔ 十进制互转 | ⭐ | py4e Ch4 | 06 |
| 16 | 列表筛选偶数 / 被 5 整除 | ⭐ | py4e Ch8 | 07 |
| 17 | 字典统计单词词频 | ⭐⭐ | py4e Ch9 | 07 |
| 18 | 过滤 1–20 中的质数(filter) | ⭐⭐ | w3resource Lambda | 07 |
| 19 | 所有数平方 / 摄华氏双向转换(map) | ⭐⭐ | w3resource Map | 07 |
| 20 | 求列表累乘(reduce) | ⭐⭐ | py4e Ch5 | 07 |
| 21 | 汉诺塔移动步数(最少步公式) | ⭐⭐⭐⭐ | Think Python 2E Ch5 | 07 |
| 22 | 斐波那契第 n 项,三种实现 | ⭐⭐⭐ | Think Python 2E Ch6 | 07 |

#### 推荐小项目

| 项目名 | 描述 | 来源 | 可嵌入我们的 Day |
|---|---|---|---|
| **小九九乘法器** | 输入 n,输出 n×n 三角形 | 黑马 Day04 | 04 |
| **猜数字(双向)** | 人猜 + 电脑猜(二分) | CS50P Week0 + Week2 | 05 |
| **简易计算器** | 支持 + - * / 和括号 | 小甲鱼 P45 | 06 |
| **通讯录 v1** | 列表 + 字典,增删改查 | 黑马 Day06 | 07 |
| **单词本 v1** | 中英对照,随机抽背 | py4e Ch9 | 07 |

---

### 2.2 函数与进阶(Day05–Day09)

> 对应 Module 0 中函数/OOP/高级特性部分。

#### 推荐习题(难度:⭐ ~ ⭐⭐⭐⭐)

| 题号 | 题目描述 | 难度 | 来源 | 可嵌入我们的 Day |
|---|---|---|---|---|
| 1 | 函数封装 BMI 计算 | ⭐ | PCC Ch8 | 08 |
| 2 | 默认参数实现"欢迎语" | ⭐ | 廖雪峰 函数 | 08 |
| 3 | 可变参数 *args 求和 | ⭐ | 廖雪峰 函数 | 08 |
| 4 | 关键字参数 **kwargs 打印 | ⭐ | 廖雪峰 函数 | 08 |
| 5 | 递归求阶乘 / 斐波那契 | ⭐⭐ | Think Python 2E Ch5 | 09 |
| 6 | 递归实现字符串反转 | ⭐⭐ | w3resource Recursion | 09 |
| 7 | 递归实现二分查找 | ⭐⭐⭐ | w3resource Recursion | 09 |
| 8 | lambda 排序学生列表(按成绩) | ⭐⭐ | py4e Ch10 | 10 |
| 9 | map 批量字符串转大写 | ⭐ | w3resource Map | 10 |
| 10 | filter 筛选质数列表 | ⭐⭐ | w3resource Lambda | 10 |
| 11 | reduce 求列表累乘/累加 | ⭐⭐ | py4e Ch5 | 10 |
| 12 | sorted 多关键字排序(先年龄后姓名) | ⭐⭐ | 廖雪峰 高阶函数 | 10 |
| 13 | 装饰器:计时器(测函数耗时) | ⭐⭐⭐ | 廖雪峰 装饰器 | 11 |
| 14 | 装饰器:日志记录(打印入参出参) | ⭐⭐⭐ | 廖雪峰 装饰器 | 11 |
| 15 | 闭包实现累加器 | ⭐⭐⭐ | Think Python 2E Ch13 | 11 |
| 16 | 偏函数固定 base=2 的 int() | ⭐⭐ | 廖雪峰 偏函数 | 11 |
| 17 | 列表推导式实现矩阵转置 | ⭐⭐⭐ | PCC Ch7 | 12 |
| 18 | 生成器实现无限斐波那契 | ⭐⭐⭐ | 廖雪峰 生成器 | 12 |
| 19 | 迭代器实现 Range 类 | ⭐⭐⭐⭐ | Think Python 2E Ch18 | 12 |
| 20 | 高阶函数实现 map/filter 自实现 | ⭐⭐⭐⭐ | Think Python 2E Ch11 | 12 |

#### 推荐小项目

| 项目名 | 描述 | 来源 | 可嵌入我们的 Day |
|---|---|---|---|
| **密码生成器** | 随机长度 + 大小写 + 数字 + 符号 | PracticePython Ex16 | 09 |
| **猜单词(Hangman)** | 6 次机会猜字母 | MIT 6.0001 PS2 | 10 |
| **Scrabble 计分器** | 字母分值 + 单词得分 | MIT 6.0001 PS3 | 11 |
| **凯撒密码** | 加密 + 解密 + 暴力破解 | MIT 6.0001 PS4 | 12 |
| **通讯录 v2** | 函数封装 + 文件持久化 | 黑马 | 07 |

---

### 2.3 数据处理(Day11–Day17)

> 对应 Module 0 后半段(NumPy/Pandas/Matplotlib/数据摄取)。

#### 推荐习题(难度:⭐ ~ ⭐⭐⭐⭐)

| 题号 | 题目描述 | 难度 | 来源 | 可嵌入我们的 Day |
|---|---|---|---|---|
| 1 | 读取文本文件,统计行数/字数/字符数 | ⭐ | PCC Ch10 | 13 |
| 2 | 读取文件,统计单词词频 Top10 | ⭐⭐ | py4e Ch7 | 13 |
| 3 | 复制文本文件(逐行读写) | ⭐ | Automate Ch9 | 13 |
| 4 | 复制二进制文件(图片/音频) | ⭐⭐ | Automate Ch9 | 13 |
| 5 | 批量重命名文件(加前缀/日期) | ⭐⭐ | Automate Ch9 | 13 |
| 6 | 读取 CSV,计算某列平均值 | ⭐⭐ | Automate Ch16 | 14 |
| 7 | 读取 CSV,筛选满足条件的行 | ⭐⭐ | Automate Ch16 | 14 |
| 8 | 写入 CSV(字典列表 → 文件) | ⭐⭐ | Automate Ch16 | 14 |
| 9 | 读取 JSON,解析嵌套结构 | ⭐⭐ | Automate Ch16 | 15 |
| 10 | 写入 JSON(对象 → 文件) | ⭐⭐ | Automate Ch16 | 15 |
| 11 | 异常处理:除零 / 类型错误 | ⭐ | PCC Ch10 | 16 |
| 12 | 异常处理:文件不存在 | ⭐ | PCC Ch10 | 16 |
| 13 | 自定义异常:年龄非法 / 余额不足 | ⭐⭐⭐ | py4e Ch11 | 16 |
| 14 | try/except/else/finally 综合 | ⭐⭐⭐ | Python.org Tutorial Ch8 | 16 |
| 15 | 日志记录(logging 模块) | ⭐⭐⭐ | Automate Ch11 | 17 |
| 16 | 正则提取邮箱/手机号 | ⭐⭐⭐ | Automate Ch7 | 17 |
| 17 | 正则替换文本中的日期格式 | ⭐⭐⭐ | Automate Ch7 | 17 |
| 18 | 综合:CSV → JSON 格式转换 | ⭐⭐⭐⭐ | Automate Ch16 | 17 |
| 19 | 综合:日志分析(统计错误次数) | ⭐⭐⭐⭐ | CS50P Week7 | 17 |

#### 推荐小项目

| 项目名 | 描述 | 来源 | 可嵌入我们的 Day |
|---|---|---|---|
| **文件批量重命名工具** | 正则匹配 + 批量改名 | Automate Ch9 | 13 |
| **CSV 成绩分析器** | 读成绩 CSV,输出平均分/最高最低 | py4e Ch7 | 14 |
| **JSON 通讯录** | 增删改查 + JSON 持久化 | Automate Ch16 | 15 |
| **简易日志分析器** | 解析 Nginx 日志,统计 IP 访问次数 | CS50P Week7 | 17 |
| **CSV ↔ JSON 互转工具** | 命令行参数 + 格式转换 | Automate Ch16 | 17 |

---

### 2.4 AI/ML/DL/NLP/爬虫/AI 应用(Day18–Day60)

> 对应 Module 1-6。以下为进阶模块素材池,教师可用于拓展习题或项目。

#### 推荐习题(难度:⭐ ~ ⭐⭐⭐⭐⭐)

| 题号 | 题目描述 | 难度 | 来源 | 可嵌入我们的 Day |
|---|---|---|---|---|
| 1 | 定义空类 `Vehicle` | ⭐ | PyNative OOP Ex1 | 18 |
| 2 | `Vehicle` 类含 `max_speed` 和 `mileage` | ⭐ | PyNative OOP Ex2 | 18 |
| 3 | `Student` 类,计算平均成绩 | ⭐⭐ | PyNative OOP Ex4 | 18 |
| 4 | `BankAccount` 类,存款 + 余额保护 | ⭐⭐ | PyNative OOP Ex6 | 18 |
| 5 | `Temperature` 类,单位转换方法 | ⭐⭐ | PyNative OOP Ex9 | 18 |
| 6 | `CoffeeMachine` 多资源跟踪 | ⭐⭐⭐ | PyNative OOP Ex11 | 18 |
| 7 | 类变量 vs 实例变量(共享属性) | ⭐⭐⭐ | PyNative OOP Ex12 | 19 |
| 8 | `Bus` 继承 `Vehicle` | ⭐⭐ | PyNative OOP Ex13 | 19 |
| 9 | 方法重写 + `super()` 调用 | ⭐⭐⭐ | PyNative OOP Ex14 | 19 |
| 10 | 多态:`Dog` / `Cat` 的 `speak()` | ⭐⭐⭐ | PyNative OOP Ex16 | 19 |
| 11 | `Shape` 抽象类 + 子类 `area()` | ⭐⭐⭐⭐ | PyNative OOP Ex18 | 19 |
| 12 | 运算符重载:`__add__` 向量加法 | ⭐⭐⭐ | PyNative OOP Ex24 | 20 |
| 13 | `__len__` 实现购物车长度 | ⭐⭐⭐ | PyNative OOP Ex25 | 20 |
| 14 | `@property` 私有余额 getter/setter | ⭐⭐⭐ | PyNative OOP Ex26 | 20 |
| 15 | `__call__` 可调用对象 | ⭐⭐⭐⭐ | PyNative OOP Ex27 | 20 |
| 16 | 组合:`Zoo` 喂养所有动物 | ⭐⭐⭐⭐ | PyNative OOP Ex29 | 20 |
| 17 | `Playlist` 增删改查 + 洗牌 | ⭐⭐⭐⭐ | PyNative OOP Ex31 | 20 |
| 18 | 抽象基类 `abc.ABC` 实现 | ⭐⭐⭐⭐ | GeeksforGeeks OOP | 21 |
| 19 | 多重继承 + MRO 顺序 | ⭐⭐⭐⭐ | Think Python 2E Ch18 | 21 |
| 20 | 设计模式:Singleton / Factory | ⭐⭐⭐⭐⭐ | GeeksforGeeks OOP | 21 |

#### 推荐小项目

| 项目名 | 描述 | 来源 | 可嵌入我们的 Day |
|---|---|---|---|
| **银行账户系统** | `Account` + `SavingsAccount` + `CheckingAccount` | PyNative OOP Ex6/13 | 19 |
| **学生成绩管理** | `Student` + `Course` + 平均分 | PyNative OOP Ex4 | 19 |
| **形状面积计算器** | `Shape`(ABC) + `Circle`/`Rectangle`/`Triangle` | PyNative OOP Ex18 | 19 |
| **员工工资系统** | `Employee` + `FullTime`/`PartTime` | PyNative OOP Ex17 | 20 |
| **购物车系统** | `Product` + `CartItem` + `Cart` + `Order` | PyNative OOP Ex20 | 20 |
| **动物园喂食系统** | `Animal` + `Lion`/`Elephant`/`Parrot` + `Zoo` | PyNative OOP Ex29 | 20 |
| **音乐播放列表** | `Song` + `Playlist` + 洗牌 | PyNative OOP Ex31 | 20 |
| **RAG 问答系统** | `Document` + `VectorDB` + `Retriever` + `Agent` | RAG + 向量检索 + Agent | 54 |

---

### 2.5 期末综合项目思路(四选一:AI 应用/LLM 微调/数据爬虫/ML 工程)

| 项目 | 核心类 | 涉及知识点 | 来源参考 |
|---|---|---|---|
| **AI 应用(RAG+Agent)** | `Document`/`VectorDB`/`Retriever` | RAG + 向量检索 + LangChain | 54 |
| **学生管理系统** | `Student`/`Course`/`Teacher`/`School` | OOP + 继承 + 持久化 | GeeksforGeeks OOP |
| **超市收银系统** | `Product`/`Cart`/`Order`/`Payment` | OOP + 组合 + 文件 | PyNative OOP Ex20 |
| **记账本** | `Transaction`/`Account`/`Category` | OOP + CSV + 统计 | Automate Ch16 |
| **酒店预订系统** | `Hotel`/`Room`/`Guest`/`Reservation` | OOP + 日期 + 异常 | GeeksforGeeks OOP |
| **航班预订系统** | `Flight`/`Passenger`/`Seat`/`Booking` | OOP + 容量管理 | PyNative OOP Ex28 |
| **RPG 角色系统** | `Player`/`Enemy`/`Room`/`Inventory` | OOP + 状态机 | PyNative OOP Ex30 |
| **扑克牌模拟** | `Card`/`Deck`/`Hand`/`Player` | OOP + 继承 + 洗牌 | Think Python 2E Ch18 |
| **井字棋 AI** | `Board`/`Player`/`AI` | OOP + 极小化极大 | PracticePython Ex26–29 |
| **CS50P Final Project** | 学生自选 | 综合 | Harvard CS50P Week9 |

---

## 3. 常见"教学红线"与"易错点"清单

> 按主题分组,附"教案建议"。共 25 项。

### 3.1 基础语法(Day01–Day07)

| # | 易错点 | 教案建议 |
|---|---|---|
| 1 | **缩进混用 Tab / Space** | 强制 IDE 设置"Tab 转 4 空格";首次课演示报错截图 |
| 2 | **if/for/while/def/class 漏冒号** | 口诀"控制结构冒号跟";每节课前 5 分钟找茬练习 |
| 3 | **`=` 与 `==` 混淆** | 强调"赋值 vs 比较";演示 `if x = 5:` 报错 |
| 4 | **零索引困惑(IndexError)** | 用"门牌号 vs 距离"类比;画内存图 |
| 5 | **字符串不可变性** | 演示 `s[0] = 'a'` 报错;引出 `.replace()` |
| 6 | **列表可变性(别名陷阱)** | 演示 `a = b = []` 修改同步;引出 `copy()` |
| 7 | **整数除法 vs 真除法** | 对比 `//` 与 `/`;Python 2 vs 3 历史 |
| 8 | **字符串拼接性能** | 引出 `join()` vs `+`;大字符串用 f-string |
| 9 | **不读 Traceback** | 教"从下往上读错误";每节课演示调试过程 |
| 10 | **变量作用域 LEGB** | 演示 `UnboundLocalError`;引出 `global` / `nonlocal` |

### 3.2 函数与高阶函数(Module 0 Day05-09 + Module 1-2)

| # | 易错点 | 教案建议 |
|---|---|---|
| 11 | **可变默认参数** `def f(x=[])` | 演示跨调用共享状态;改为 `def f(x=None)` |
| 12 | **lambda 延迟绑定** | 演示循环中 lambda 捕获最终值;引出默认参数绑定 |
| 13 | **递归缺少基准情形** | 演示 `RecursionError`;强调"先写终止条件" |
| 14 | **返回函数 vs 返回值** | 对比 `return f` 与 `return f()`;演示闭包 |
| 15 | **装饰器丢失元信息** | 引出 `@functools.wraps`;演示 `__name__` 变化 |

### 3.3 文件 / 异常 / JSON / CSV(Module 0 Day07 + Module 4-5)

| # | 易错点 | 教案建议 |
|---|---|---|
| 16 | **忘记关闭文件** | 强制 `with open(...) as f:` 写法 |
| 17 | **编码问题(GBK vs UTF-8)** | 演示 `UnicodeDecodeError`;统一 UTF-8 |
| 18 | **CSV 含逗号/换行** | 引出 `csv` 模块;不手写 split(',') |
| 19 | **JSON 不支持 datetime** | 演示 `TypeError`;引出 `default=` 参数 |
| 20 | **异常捕获过于宽泛** | 避免 `except:`;指定异常类型 |

### 3.4 面向对象(Module 0 Day08)

| # | 易错点 | 教案建议 |
|---|---|---|
| 21 | **忘记 self 参数** | 口诀"实例方法第一个必 self";演示报错 |
| 22 | **类变量被实例修改** | 演示 `self.class_var = ...` 创建实例变量;引出类变量正确用法 |
| 23 | **继承 vs 组合选择** | 教"has-a 用组合,is-a 用继承";演示过度继承的反例 |
| 24 | **重写 `__init__` 不调用 super()** | 演示父类属性丢失;强调 `super().__init__()` |
| 25 | **滥用多重继承** | 演示 MRO 混乱;引出 `abc.ABC` 与接口 |

---

## 4. 本课程(60 天)与市面对比

| 维度 | 黑马 28 天 | 达内 30 天 | 廖雪峰 14 天速成 | 莫烦 Python | 小甲鱼 98 课 | **我们的 60 天** |
|---|---|---|---|---|---|---|
| **总时长** | ~168h | ~180h | ~84h | ~60h | ~100h | ~126h |
| **每日强度** | 6h | 6h | 6h | 弹性 | 弹性 | 6h |
| **基础语法** | Day01–10 | Day01–07 | 1–2 周 | 简略 | 30 课 | Day01–10(10 天) |
| **函数+进阶** | Day05–09 | Day08–10 | 1 周 | 简略 | 10 课 | Day05–09(5 天) |
| **数据处理** | Day11–17 | Day10–14 | 1 周 | 无 | 5 课 | Day11–17(7 天) |
| **ML+DL** | Day18–31 | Day13–16 | 2 周 | 无 | 10 课 | Day18–31(14 天) |
| **NLP+LLM** | Day32–43 | — | — | 无 | — | Day32–43(12 天) |
| **AI 专项总课时** | 0 | 0 | 0 | 0 | 0 | **31 天(ML+DL+NLP+LLM+爬虫+AI 应用)** |
| **练习密度** | 中(穿插) | 中 | 低(无系统习题) | 低 | 中(每课作业) | **高(每节 in_class + 每日 homework)** |
| **阶段项目** | 名片 + 飞机大战 | 名片 + 爬虫 | 无 | ML 项目 | 3 大项目 | **5 个 mini + 1 个 capstone** |
| **OOP 系统性** | ⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐ | ⭐⭐⭐ | **⭐⭐⭐⭐(4 天递进 + 综合项目)** |
| **持久化** | 无 | 无 | 无 | 无 | 无 | **JSON + CSV 双格式** |
| **异常处理** | 1 天 | 1 天 | 半天 | 无 | 1 课 | **1 天(含自定义异常)** |
| **期末作品** | 飞机大战(Pygame) | 爬虫 + 数据分析 | 无 | ML Demo | 3 选 1 | **四选一(AI 应用/LLM/爬虫/ML)** |
| **适合人群** | 就业导向 | 就业导向 | 快速了解 | ML 兴趣 | 视频偏好 | **零基 + 考证 / 跨考 / 兴趣** |

### 我们的核心优势

1. **练习密度最高**:513 道习题(342 当堂练 + 171 作业)+ 每天 6 小时高强度实战,远超廖雪峰/莫烦的"读懂为主"模式
2. **AI 专项最强**:31 天递进(ML → DL → NLP → LLM 微调 → 爬虫 → AI 应用) + 期末四选一作品,覆盖完整 AI 工程能力链
3. **持久化 + 异常完整覆盖**:JSON + CSV 双格式 + 自定义异常,这是多数入门课忽略的"工程化"能力
4. **难度梯度精细**:每节习题按 ⭐~⭐⭐⭐⭐⭐ 分级,学员可按需选做,避免"一刀切"
5. **素材池丰富**:本参考资料库提供 100+ 外部习题 + 20+ 项目思路,教师可灵活替换

---

## 5. 参考链接汇总

| 资源 | URL |
|---|---|
| MIT 6.0001 OCW | https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/ |
| MIT 6.0002 OCW | https://ocw.mit.edu/courses/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/ |
| MITx 6.00.1x(edX) | https://www.edx.org/course/introduction-to-computer-science-and-programming-7 |
| Python for Everybody | https://www.py4e.com/ |
| Harvard CS50P | https://cs50.harvard.edu/python/ |
| Automate the Boring Stuff | https://automatetheboringstuff.com/ |
| Python Crash Course | https://nostarch.com/python-crash-course-3rd-edition |
| Think Python 2E | https://greenteapress.com/wp/think-python-2e/ |
| 廖雪峰 Python 教程 | https://www.liaoxuefeng.com/wiki/1016959663602400 |
| 莫烦 Python | https://mofanpy.com/ |
| 小甲鱼零基础入门 | https://www.bilibili.com/video/BV1xs411Q799 |
| 黑马程序员 Python | https://www.bilibili.com/video/BV1ex411x7Em |
| 菜鸟教程 Python 3 | https://www.runoob.com/python3/python3-tutorial.html |
| W3CSchool Python | https://www.w3cschool.cn/python3/ |
| Python.org 官方 Tutorial | https://docs.python.org/3/tutorial/ |
| PyNative OOP 练习 | https://pynative.com/python-object-oriented-programming-oop-exercise/ |
| PyNative 基础练习 | https://pynative.com/python-basic-exercise-for-beginners/ |
| PracticePython | https://www.practicepython.org/ |
| w3resource Python | https://www.w3resource.com/python-exercises/ |
| Py.CheckiO | https://py.checkio.org/ |
| PythonPrinciples | https://pythonprinciples.com/challenges/ |
| GeeksforGeeks OOP | https://www.geeksforgeeks.org/python-oops/ |
| Exercism Python | https://exercism.org/tracks/python |
| HackerRank Python | https://www.hackerrank.com/domains/python |
| GitHub Awesome Python | https://github.com/vinta/awesome-python |
| GitHub project-based-learning | https://github.com/practical-tutorials/project-based-learning |

---

> 本文件为"素材池",不替代主线教学计划。教师可按需从各章节抽取习题 / 项目,嵌入对应 Day 的 slides / in_class / homework 中。
