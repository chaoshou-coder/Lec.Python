# Day05 · OOP 封装 (L1)

## 关键知识点

- `class` 定义类（大驼峰命名）
- `__init__` 构造函数：`self` 代表当前对象，实例化时自动调用
- 实例方法：第一个参数写 `self`，通过 `self.属性名` 访问对象自己的数据
- 实例属性 vs 类属性（`self.name` vs `类名.school`）
- `@property`：把方法变成"伪属性"（getter / setter 校验）
- `__str__` 魔术方法 — `print(对象)` 时输出可读信息

## 设计叙事

> 电商订单系统 v2 起点:订单数据散落在 dict 里,100 行 if-elif 处理。
> 今天用"类和对象"把数据 + 行为打包成一个整体。

## 当堂练习

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `in_class/practice01.py` | ⭐⭐ | 8 分钟 | 定义 `Product` 类,`__init__` 绑定 name/price |
| 2 | `in_class/practice02.py` | ⭐⭐ | 10 分钟 | 给 `Product` 加 `info()` 实例方法 |
| 3 | `in_class/practice03.py` | ⭐⭐⭐ | 12 分钟 | `Student` 类 `@property` 校验成绩 0-100 |
| 4 | `in_class/practice04.py` | ⭐⭐⭐ | 12 分钟 | `Product` 加 `__str__`,`print(p)` 输出友好 |
| 5 | `in_class/practice05.py` | ⭐⭐⭐ | 13 分钟 | 类属性 `tax_rate` 所有实例共享 |
| 6 | `in_class/practice06.py` | ⭐⭐⭐⭐ | 15 分钟 | `@property` setter 拒绝非法赋值(余额不能负) |

## 课后作业

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `homework/task01.py` | ⭐⭐⭐⭐ | 20 分钟 | `BankAccount` 类综合(`@property` 校验+存取款+`__str__`) |
| 2 | `homework/task02.py` | ⭐⭐⭐⭐ | 20 分钟 | `Temperature` 类(`@property` 绝对零度校验+单位转换) |
| 3 | `homework/task03.py` | ⭐⭐⭐⭐ | 25 分钟 | 订单系统 v2 起步:支持多商品的 `Order` 类原型 |

## 小项目(当堂完成)

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `mini_project/bankaccount.py` | ⭐⭐⭐⭐ | 45 分钟 | `BankAccount` 类综合(`@property`+类属性+`__str__`+存取款+异常处理) |

## 门控验收

学员需提交 `BankAccount` 类,满足:
- 用 `@property` 保护 balance(非负)
- 支持 `deposit` / `withdraw` 操作
- `__str__` 友好打印
- **不可使用任何外部库**
- **必须使用 `self` 绑定实例属性(不可漏写)**

## BREAK IT 环节(教师用)

- 漏写 `self` 参数 → `TypeError: __init__() takes 2 positional arguments but 3 were given`
- 漏写 `self.name = name`(直接写 `name = name`) → 属性未绑定,`AttributeError`
- setter 忘写 `return` 在被拒后,学员会困惑"为什么不报错也不改"
- `print(对象)` 默认打印 `<__main__.BankAccount object at 0x...>` 引出 `__str__`

## 易错点

1. **函数定义后不调用,代码不会执行** — 写了 `def` 不等于"跑一次"
2. **`return` 语句后面的代码不会执行** — 像放学铃,听到就走
3. **默认参数必须放在非默认参数后面** — `SyntaxError`
4. **函数内部不能直接修改全局变量** — 要用 `global` 显式声明

## 阶段复习要点

后续 Day06 L2 复习
