# Day10 · 函数进阶

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day07 已掌握函数入门(`def`、`return`、形参/实参、无返回值函数)、Day08 字符串提升、Day09 列表进阶
> 关键问题: Day07 学的函数"参数个数是固定的",但现实场景常常"不知道会传几个参数进来"——如何让函数**既能接收 1 个也能接收 100 个参数**?如何让函数**调用时省略某些参数**?本节把函数从"固定模具"升级为"万能接口"

---

## 0. 引入(5 分钟)

- **抽问上节**(2 分钟): 让学员口答 —— `def add(a, b): return a + b`,调用 `add(1, 2, 3)` 会怎样?(答:报错 `TypeError`,参数个数不对)。目的: 唤醒"参数必须一一对应"的记忆,为今天"打破这个限制"埋伏笔。
- **赏玩 demo**(3 分钟): 在终端现场写 `print(1)`, `print(1, 2)`, `print(1, 2, 3)`,都能正常输出 —— "为什么 `print()` 能传任意多个参数,我们自己写的函数就不行?"一句话吊足胃口。

---

## 1. 第一讲(15 分钟) —— 默认参数

### 知识点 1.1 默认参数:让调用更省事

给参数设一个"默认值",调用时**可以不传**这个参数,函数自动用默认值。

```python
def greet(name, greeting="你好"):
    print(f"{greeting},{name}!")

greet("小明")              # 你好,小明!     ← 省略 greeting,用默认值
greet("小明", "早上好")    # 早上好,小明!   ← 传了就用传的
greet("Tom", "Hello")      # Hello,Tom!
```

> 口诀:**有默认值的参数放后面,调用时可省**。

### 知识点 1.2 多个默认参数:命名参数调用

多个参数都有默认值时,可以用 `参数名=值` 的方式**跳过中间参数**。

```python
def create_user(name, age=18, city="北京"):
    print(f"{name},{age}岁,来自{city}")

create_user("张三")                          # 张三,18岁,来自北京
create_user("李四", city="上海")             # 李四,18岁,来自上海
create_user("王五", age=25, city="深圳")     # 王五,25岁,来自深圳
```

> 命名参数(`city="上海"`)让调用意图一目了然,不用死记参数顺序。

### 知识点 1.3 🔴 可变默认参数陷阱(本节重点)

用**列表、字典**等可变对象作默认值,会导致**跨调用共享状态** —— 这是 Python 最著名的坑之一。

```python
# ❌ 错误写法
def add_item(item, basket=[]):
    basket.append(item)
    return basket

print(add_item("苹果"))   # ['苹果']
print(add_item("香蕉"))   # ['苹果', '香蕉']  ← 竟然还有"苹果"!
```

🔴 教学红线(可变默认参数): 默认值在**函数定义时**只创建一次,之后每次调用都**共享同一个列表**。正确做法是用 `None` 作默认值,函数内部再创建新列表:

```python
# ✅ 正确写法
def add_item(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket

print(add_item("苹果"))   # ['苹果']
print(add_item("香蕉"))   # ['香蕉']  ← 互不影响
```

> 记忆口诀:**默认值用不可变(int/str/tuple/None),不用可变(list/dict/set)**。

## 2. 当堂练 1(20 分钟)

- 练习 1: `in_class/practice01.py` —— 定义 `greet(name)` 打印欢迎语(⭐⭐,10 分钟),复习 Day07 函数定义,为默认参数做铺垫
- 练习 2: `in_class/practice02.py` —— 定义 `add(a, b)` 返回两数之和(⭐⭐,10 分钟),巩固 `return` 用法

> 巡场重点: 检查学员是否还在函数末尾写 `print()` 而不是 `return` —— Day07 遗留问题。提示:"`return` 把结果**交出去**,`print()` 只是**显示一下**,别人拿不到"。

---

## 3. 第二讲(15 分钟) —— `*args` 与 `**kwargs` 可变参数

### 知识点 3.1 `*args`:接收任意多个位置参数

在参数前加 `*`,函数就能接收**任意多个**位置参数,内部以 **tuple** 形式访问。

```python
def total(*args):
    result = 0
    for num in args:
        result += num
    return result

print(total())             # 0
print(total(1, 2, 3))      # 6
print(total(10, 20, 30, 40, 50))  # 150
```

> `args` 只是约定命名,可以改,但**强烈建议统一用 `args`**。
>
> 为什么是 tuple? 因为 tuple 不可变,防止函数内部意外修改外部传入的数据。

### 知识点 3.2 `**kwargs`:接收任意多个关键字参数

在参数前加 `**`,函数就能接收**任意多个**关键字参数,内部以 **dict** 形式访问。

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="小明", age=18, city="北京")
# name: 小明
# age: 18
# city: 北京
```

> `kwargs` = "keyword arguments",同样是约定命名。
>
> 🔴 教学红线(kwargs 产出的是字典): `**kwargs` 把传入的 `name="小明", age=18` 自动"组包"成 `{"name": "小明", "age": 18}`。遍历方式和 Day09 学过的字典 `.items()` 完全一致。

### 知识点 3.3 混合参数顺序:必默星关

一个函数同时有四种参数时,**必须按这个顺序**:

```python
def func(必选参数, 默认参数, *args, **kwargs):
    pass

# 实际例子
def register(name, age=18, *hobbies, **scores):
    print(f"姓名: {name}")
    print(f"年龄: {age}")
    print(f"爱好: {hobbies}")
    print(f"成绩: {scores}")

register("小明", 20, "篮球", "编程", math=95, english=88)
# 姓名: 小明
# 年龄: 20
# 爱好: ('篮球', '编程')
# 成绩: {'math': 95, 'english': 88}
```

> 口诀:**必默星关**(必选 → 默认 → `*args` → `**kwargs`)。考试常考顺序,写错直接 `SyntaxError`。

## 4. 当堂练 2(25 分钟)

- 练习 3: `in_class/practice03.py` —— 定义 `is_even(num)` 判断偶数(⭐⭐⭐,15 分钟),巩固 `return` + 布尔表达式
- 练习 4: `in_class/practice04.py` —— 定义 `find_max(a, b, c)` 返回三数最大值(⭐⭐⭐,15 分钟),巩固 `if/elif/else` + `return`

> 巡场重点: 练习 4 学员常写 `if a > b or a > c` 而不是 `if a >= b and a >= c`,导致三个数相等时走到 `else` 分支。提示:"最大值**大于等于**其他所有数,用 `and` 连接"。

---

## 5. 第三讲(15 分钟) —— 解包调用与 lambda 入门

### 知识点 5.1 解包调用:`*` 和 `**` 的另一面

定义函数时 `*` 是"组包",**调用函数**时 `*` 是"解包" —— 把列表/字典"拆"成参数。

```python
def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
print(add(*nums))       # 6  ← 等价于 add(1, 2, 3)

data = {"a": 10, "b": 20, "c": 30}
print(add(**data))      # 60 ← 等价于 add(a=10, b=20, c=30)
```

> 类比: 定义时 `*args` 是把散件**打包**成箱子,调用时 `*list` 是把箱子**拆开**成散件。

### 知识点 5.2 lambda 入门:一行写一个函数

`lambda` 用来写**简单的匿名函数**(没有名字的函数),适合"用完即走"的场景。

```python
# 普通函数
def add(x, y):
    return x + y

# 等价的 lambda
add = lambda x, y: x + y

print(add(3, 5))  # 8
```

> 语法:`lambda 参数1, 参数2: 表达式`(表达式结果自动返回,不用写 `return`)。

### 知识点 5.3 lambda + `sort(key=...)`:按指定规则排序

`sort()` 默认按**第一个元素**排序,`key=` 可以指定"按什么排"。

```python
students = [
    ("小明", 85),
    ("小红", 92),
    ("小刚", 78)
]

# 按成绩排序(key 取每个元组的第 2 个元素)
students.sort(key=lambda s: s[1])
print(students)
# [('小刚', 78), ('小明', 85), ('小红', 92)]
```

> 🔴 教学红线(lambda 延迟绑定): 在**循环**中创建 lambda,lambda 会捕获变量的**最终值**,不是创建时的值。例如:
>
> ```python
> funcs = [lambda: i for i in range(3)]
> print(funcs[0]())  # 2,不是 0!
> print(funcs[1]())  # 2,不是 1!
> ```
>
> 修复: 用默认参数绑定当前值 —— `lambda i=i: i`。本节只需**演示现象 + 给出修复**,不必深究原理(闭包细节留到 Day11)。

## 6. 当堂练 3(25 分钟)

- 练习 5: `in_class/practice05.py` —— 定义 `count_vowels(s)` 统计元音个数(⭐⭐⭐⭐,20 分钟),巩固循环 + `in` 判断 + `return`
- 练习 6: `in_class/practice06.py` —— 定义 `factorial(n)` 求阶乘(⭐⭐⭐⭐,20 分钟),巩固循环累乘 + 边界(0! = 1)

> 巡场重点: 练习 6 学员常把 `result` 初始化为 `0`,导致乘积永远是 0。提示:"累乘初始值是 1,累加初始值是 0"。

## 7. 小项目(若本日有,45 分钟)

本节无小项目。

## 8. 总结(5 分钟)

- **本日错 3 件事**(教师课后把真实错例填进 `teacher_notes.md`):
  1. 用列表作默认参数 `def f(x=[])` 导致跨调用共享状态
  2. 混合参数顺序写错,把 `*args` 放在默认参数前面导致 `SyntaxError`
  3. lambda 在循环中捕获最终值,而不是创建时的值
- **作业说明**: 课后 `homework/task01.py`(摄氏转华氏)、`homework/task02.py`(质数判断)、`homework/task03.py`(字符串逆序),下节课前 10 分钟复盘。
- **下节预告**: 今天用 `**kwargs` 产出的就是**字典**,明天我们系统学字典 —— 届时你会恍然大悟"原来 kwargs 一直在用字典"。

---

## 易错点

1. **可变默认参数**: `def f(x=[])` 的默认值只创建一次,跨调用共享。改用 `def f(x=None)`,函数内部再 `x = []`。
2. **混合参数顺序**: 必选 → 默认 → `*args` → `**kwargs`(口诀"必默星关"),写错直接 `SyntaxError`。
3. **`*args` 是 tuple,`**kwargs` 是 dict**: 定义时组包,调用时解包,方向相反。
4. **lambda 只能写一行表达式**: 不能写 `if/else` 语句(但可以写三元表达式 `x if x > 0 else -x`)。
5. **lambda 延迟绑定**: 循环中创建 lambda 会捕获变量最终值,用 `lambda i=i: ...` 绑定当前值。

## 延伸题

> 以下素材来自外部课程(references.md §2.2),教师可按需选用或替换当堂练。

- **(lambda 排序学生列表, py4e Ch10, ⭐⭐)**: 给定学生列表 `[("小明", 85), ("小红", 92)]`,用 `sort(key=lambda s: s[1])` 按成绩排序 —— 巩固本节 lambda + `key=` 搭配。
- **(map 批量字符串转大写, w3resource Map, ⭐)**: 用 `map(str.upper, words)` 把列表中所有字符串转为大写 —— 引出 Day11 高阶函数 `map/filter/reduce`。
- **(猜单词 Hangman, MIT 6.0001 PS2, ⭐⭐⭐)**: 6 次机会猜字母,显示当前进度 —— 综合巩固循环 + 列表 + 函数封装,可作为阶段复习项目。
