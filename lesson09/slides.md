# Day09 · 模块与高级特性

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day01-08(全部已学,重点是函数/OOP/文件 I/O)
> 关键问题: 代码量破千行后,单文件不堪重负 —— 如何把代码
> **拆分到多个文件**、让重复的"计时/日志/资源管理"逻辑自动
> 复用?本节把"高级特性"作为工具箱补完课:包、生成器、上下文
> 管理器、装饰器

---

## 0. 引入(5 分钟)

- **破冰 + 抽问**(2 分钟): "一个 Python 文件已经 2000 行,滚动
  条细如发丝 —— 怎么管理?"引出**模块化 + 包**。
- **赏玩 demo**(3 分钟): 写一个 `@timer` 装饰器,随便套到哪个
  函数上都能自动打印耗时,"黑魔法"效果拉满,吊足胃口。

---

## 1. 第一讲(15 分钟) —— import 与包

### 知识点 1.1 三种 import 方式

```python
import math
math.sqrt(16)           # 通过模块名访问成员

from math import sqrt
sqrt(16)                # 直接用成员名,不再写模块名前缀

from math import factorial as fac
fac(5)                  # 用别名 fac 替代原函数名
```

> 口诀:**`import 模块` 带前缀,`from` 直接用,`as` 改别名**。

### 知识点 1.2 自定义模块

把函数/类复制进 `utils.py`,同目录下 `import utils` 即可使用。

```python
# utils.py
def add(a, b):
    return a + b

# main.py
import utils
print(utils.add(1, 2))  # 3
```

### 知识点 1.3 包(Package) = 模块的文件夹

```
my_pkg/
├── __init__.py       ← 包标识(可以为空)
├── math_tools.py
└── string_tools.py
```

```python
from my_pkg.math_tools import add
from my_pkg.string_tools import capitalize
```

> 🔴 教学红线(`__init__.py`): Python 3.3+ 中不是必须,但**强烈
> 建议保留**,否则部分工具(IDE、旧版 pip)不认识这是包。

## 2. 当堂练 1(20 分钟)

- 练习 1: `in_class/practice01.py` —— 把 Day08 的 `Student`
  类移到独立模块,主程序里 import 使用(⭐⭐,10 分钟)
- 练习 2: `in_class/practice02.py` —— 搭 3 个文件的包结构,
  包含 `__init__.py`(⭐⭐⭐,10 分钟)

> 巡场重点: 学员常漏写 `__init__.py`,或把包目录建在错误路径
> 下导致 `ModuleNotFoundError`。

---

## 3. 第二讲(15 分钟) —— 生成器 yield

### 知识点 3.1 为何需要生成器

普通函数 `return` 一次就结束,想**逐个产出**数据且**不占内存**,
用 `yield`。生成器是**惰性计算**的迭代器。

```python
def 平方(limit):
    for i in range(limit):
        yield i * i         # 每次产一个值,暂停,下次从这里恢复

gen = 平方(4)
print(next(gen))    # 0
print(next(gen))    # 1
print(next(gen))    # 4
```

> 口诀:**`yield` 是 `return` 的"Hold"版本 —— 产出值但不退场**。

### 知识点 3.2 `yield from` 委托子生成器

```python
def 正向(n):
    yield from range(n)         # 等价于 for i in range(n): yield i
```

### 知识点 3.3 生成器 vs 列表

| 对比 | 列表 | 生成器 |
|---|---|---|
| 内存 | 全量存 | 产一个放一个 |
| 遍历 | 多次 | 一次性 |
| 求长度 | `len()` | 不支持 |

## 4. 当堂练 2(25 分钟)

- 练习 3: `in_class/practice03.py` —— 生成器实现斐波那契
  数列,前 n 项(⭐⭐⭐,12 分钟)
- 练习 4: `in_class/practice04.py` —— 用生成器读大文件,
  每次只读一行到内存(⭐⭐⭐,13 分钟)

> 巡场重点: 斐波那契初学者容易用递归,提示**用 `yield` 才是
> 生成器的正确打开方式**。

---

## 5. 第三讲(15 分钟) —— 上下文管理器与装饰器

### 知识点 5.1 自定义上下文管理器

`with` 语句需要对象实现 `__enter__` 和 `__exit__` —— 进/出
时自动执行。

```python
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        print(f"耗时 {time.time() - self.start:.4f}s")

with Timer():
    sum(range(1000000))     # 自动计时
```

### 知识点 5.2 装饰器:包装函数

装饰器本质是**接收函数 → 返回新函数**的高阶函数,语法糖
`@decorator`。

```python
import functools, time

def timer(fn):
    @functools.wraps(fn)        # 保留原函数名/文档
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        print(f"{fn.__name__} 耗时 {time.time() - start:.4f}s")
        return result
    return wrapper

@timer                          # ← 等价于 slow = timer(slow)
def slow():
    time.sleep(0.1)

slow()      # slow 耗时 0.1xxx s
```

> 口诀:**装饰器 = 把函数装进壳,@ 语法糖,`functools.wraps` 留名**。

### 知识点 5.3 带参数的装饰器

需要参数时再加一层:

```python
def log(level="INFO"):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            print(f"[{level}] 调用 {fn.__name__}")
            return fn(*args, **kwargs)
        return wrapper
    return decorator

@log("DEBUG")
def add(a, b):
    return a + b

add(1, 2)       # [DEBUG] 调用 add
```

> 🔴 教学红线(`functools.wraps`): 不加它,被装饰函数的 `__name__`
> 会变成 `wrapper`,调试/文档都会出错。**永远写 `@functools.wraps(fn)`**。

## 6. 当堂练 3(25 分钟)

- 练习 5: `in_class/practice05.py` —— 实现一个 `@log` 装饰器,
  打印函数名和参数(⭐⭐⭐,12 分钟)
- 练习 6: `in_class/practice06.py` —— 实现一个
  `ResourceManager` 类作为上下文管理器,`with` 块退出时
  自动 `close()`(⭐⭐⭐⭐,13 分钟)

> 巡场重点: 练习 5 学员常漏写 `@functools.wraps`,巡场直接问:
> "你的被装饰函数 `.__name__` 还是原来那个吗?"

---

## 7. 小项目(若本日有,45 分钟)

本日无综合小项目,但可把前面练习文件整合成一个**工具包**:

```
mini_project/
├── __init__.py
├── decorators.py     ← timer / log
├── generators.py     ← 斐波那契 / 读大文件
└── main.py           ← import 演示
```

---

## 8. 总结(5 分钟)

- **本日错 3 件事**(课后教师把真实错例填进 `teacher_notes.md`):
  1. 自定义装饰器漏写 `@functools.wraps`,原函数名丢失
  2. 把生成器当列表用 —— 取 `len()` 报错,或遍历两次第 2 轮空
  3. 上下文管理器 `__exit__` 不加三个 exc_ 参数,签名报错
- **作业说明**: `homework/task01.py`(生成器实现无限序列)、
  `homework/task02.py`(装饰器带参数 + 类方法装饰)、
  `homework/task03.py`(项目结构搭建多模块工具包),下节课前
  10 分钟复盘。

---

## 易错点

1. **生成器只能遍历一次**,第二次 `for x in gen` 直接空 —— 想
   复用请再调用一次生成器函数产生新对象。
2. **装饰器必须 `@functools.wraps(fn)`**,否则被装饰函数名变
   成 `wrapper`,调试/文档全部出错。
3. **`yield from` 不是 `yield` 的语法糖 + range**,它把子生成器
   的值**逐个委托**给外层。
4. **包目录必须有 `__init__.py`**(Python 3.3+ 虽非强制,但最
   好保留),否则 IDE 不认识。
5. **上下文管理器 `__exit__` 必须接受三个 exc_ 参数**,否则
   `with` 调用时签名不匹配报 `TypeError`。

## 延伸题

- **(CS50P Week9, ⭐⭐)**: 用 `@property` 实现只读属性,结合本
  节装饰器做日志记录 —— 巩固装饰器。
- **(Real Python Generators, ⭐⭐⭐)**: 用生成器实现 `tail -f`
  风格日志跟踪器,边写边读 —— 巩固生成器惰性求值。
- **(MIT 6.100L, ⭐⭐⭐⭐)**: 实现带参数的 `@memoize` 装饰器,
  缓存函数调用结果 —— 巩固装饰器 + 字典。
