# Day08 · OOP 基础

## 关键知识点
- `class` 定义类（大驼峰命名）
- `__init__` 构造函数：`self` 代表当前对象，实例化时自动调用
- 实例方法：第一个参数写 `self`
- 实例属性 vs 类属性（`self.name` vs `类名.school`）
- `@property`：把方法变成"属性"（getter / setter 校验）
- `__str__` 与 `__repr__` 魔术方法
- 继承：`class 子类(父类)`，复用 + 扩展 + 覆盖
- `super()` 调用父类方法
- 类属性统计实例数

## 当堂练习

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `in_class/practice01.py` | ⭐⭐ | 8 分钟 | 定义 `Book` 类，实例化并打印属性 |
| 2 | `in_class/practice02.py` | ⭐⭐⭐ | 12 分钟 | 给 `Book` 加 `info()` 方法，返回格式化字符串 |
| 3 | `in_class/practice03.py` | ⭐⭐⭐ | 12 分钟 | `Student` 类 `@property` 校验成绩 0-100 |
| 4 | `in_class/practice04.py` | ⭐⭐⭐ | 13 分钟 | `Book` 类加 `__str__`，`print(book)` 输出格式化 |
| 5 | `in_class/practice05.py` | ⭐⭐⭐ | 12 分钟 | `Vehicle` 父类 + `Car`/`Bike` 子类，覆盖 `move()` |
| 6 | `in_class/practice06.py` | ⭐⭐⭐⭐ | 13 分钟 | 类属性实现"统计共创建了多少个实例" |

## 课后作业

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `homework/task01.py` | ⭐⭐⭐⭐ | 20 分钟 | BankAccount 类 + 余额校验 |
| 2 | `homework/task02.py` | ⭐⭐⭐⭐ | 20 分钟 | Animal 继承体系 |
| 3 | `homework/task03.py` | ⭐⭐⭐⭐ | 25 分钟 | 类属性统计实例数 + 文件持久化 |

## 小 / 中型项目

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `mini_project/student.py` | ⭐⭐⭐⭐ | 45 分钟 | `Student` 类综合（`@property average` + `__str__` + 成绩校验 + 异常处理） |

## 阶段复习要点

后续 Day14 阶段复习
