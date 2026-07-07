# Day19 · OOP(封装)

## 关键知识点
- `class` 与 `__init__(self, ...)` 初始化实例
- 实例属性 / 实例方法
- 私有属性约定:`_name` / `__name` 名称改写
- `@property` 装饰器(只读封装)
- `__str__` / `__repr__` 自定义对象字符串表示
- 在方法中使用 `raise` 管理非法状态

## 当堂练习

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `in_class/practice01.py` | ⭐⭐ | 10 分钟 | class + __init__ + 实例方法 introduce |
| 2 | `in_class/practice02.py` | ⭐⭐⭐ | 15 分钟 | 实例方法 is_adult 返回布尔 |
| 3 | `in_class/practice03.py` | ⭐⭐⭐ | 15 分钟 | __str__ 自定义打印格式 |
| 4 | `in_class/practice04.py` | ⭐⭐⭐⭐ | 20 分钟 | 私有属性 _score + @property 只读 |
| 5 | `in_class/practice05.py` | ⭐⭐⭐⭐ | 20 分钟 | BankAccount 存款取款 + 余额不足 raise |
| 6 | `in_class/practice06.py` | ⭐⭐⭐⭐⭐ | 25 分钟 | Book 借还书 + 异常管理状态机 |

## 课后作业

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `homework/task01.py` | ⭐⭐⭐ | 15 分钟 | Rectangle 面积与周长方法 |
| 2 | `homework/task02.py` | ⭐⭐⭐⭐ | 20 分钟 | ShoppingCart 商品增删总价计算 |
| 3 | `homework/task03.py` | ⭐⭐⭐⭐⭐ | 25 分钟 | Library 借还图书 + 字典记录借阅关系 |

## 小 / 中型项目

本节以多个小练习逐步构建 OOP 思维,下节 Day20 进入继承和多态。

## 阶段复习要点

后续 Day21 期末总复习将综合考察封装、属性管理、异常处理等 OOP 基础场景
