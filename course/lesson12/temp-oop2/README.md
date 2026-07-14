# Day06 · OOP 继承 (L2)

## 关键知识点

- `class Child(Parent)` 单继承语法
- `super().__init__()` 调用父类构造函数
- 方法重写(override):子类同名方法替换父类
- MRO(方法解析顺序)查找链:子类 → 父类 → 父类的父类
- `isinstance()` / `issubclass()` —— 反模式演示(为什么不用)

## 设计叙事

> 电商订单系统 v2:老板说要上实体书/电子书/会员卡,
> 它们的属性几乎是重复的,改一个 bug 要改三处。
> 今天用"继承"抽出共性,让"改一处生效"成为现实。

## 当堂练习

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `in_class/practice01.py` | ⭐⭐ | 10 分钟 | `Product` 基类 + `Book` 子类继承 |
| 2 | `in_class/practice02.py` | ⭐⭐⭐ | 12 分钟 | `super().__init__()` 扩展子类属性 |
| 3 | `in_class/practice03.py` | ⭐⭐⭐ | 12 分钟 | 方法重写 + `super().方法()` 复用父类 |
| 4 | `in_class/practice04.py` | ⭐⭐⭐ | 13 分钟 | 动物园体系:Animal→Dog/Cat + 多态引入 |
| 5 | `in_class/practice05.py` | ⭐⭐⭐⭐ | 15 分钟 | `Employee→Manager→Sales` 多级继承 |
| 6 | `in_class/practice06.py` | ⭐⭐⭐⭐ | 13 分钟 | MRO 查找链 + isinstance 反模式识别 |

## 课后作业

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `homework/task01.py` | ⭐⭐⭐⭐ | 25 分钟 | 电商 Product 继承体系:PhysicalProduct/DigitalProduct |
| 2 | `homework/task02.py` | ⭐⭐⭐⭐ | 25 分钟 | Employee+Manager+Sales 薪资系统(多态引入) |
| 3 | `homework/task03.py` | ⭐⭐⭐⭐ | 30 分钟 | 对比题:动物园系统"继承+重写" vs "纯 duck typing" |

## 小项目(当堂完成)

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `mini_project/employee_pay.py` | ⭐⭐⭐⭐ | 45 分钟 | `Employee` 基类 + Manager/Sales 子类 + show_pay(emp) 多态调用 |

## 门控验收

学员需提交员工薪资系统,满足:
- 至少 2 级继承(Employee → Manager / Sales)
- 子类用 `super().__init__()` 调用父类构造
- 至少一个方法被**重写**(pay() 不同实现)
- `show_pay(emp)` 函数不使用 `isinstance` / `type()`
- **约束:不调用 `isinstance`/`type()`**(教师可用 grep 检查)

## BREAK IT 环节(教师用)

- 子类重写 `__init__` **不调用 `super().__init__()`** → 父类属性丢失 → `AttributeError`
- 学员给出 `show_pay` 用 `isinstance(emp, Manager)` 的教师回答:"可以跑,但加新员工类型时此函数要改" → 引出"开闭原则"
- 多级继承(`A→B→C`)时 MRO 查找顺序 → `C.__mro__` 查看

## 易错点

1. **重写 `__init__` 忘调 `super().__init__()`** —— 父类属性直接丢失
2. **继承与组合混淆** —— "has-a 用组合,is-a 用继承"
3. **过度继承** —— 继承层级 > 3 层就是设计坏味道
4. **MRO 混乱** —— 多重继承时属性查找顺序不清

## 阶段复习要点

后续 Day07 L3 复习
