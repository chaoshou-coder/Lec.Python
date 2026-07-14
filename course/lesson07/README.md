# Day07 · OOP 多态+契约 (L3)

## 关键知识点

- 鸭子类型(Duck Typing):不关注类型,只关注"有没有这个方法"
- 多态(Polymorphism):同一接口不同实现,调用方不感知具体类型
- `abc.ABC` 抽象基类 —— 把"必须实现的接口"写进代码
- `@abstractmethod` 装饰器 —— 漏实现会在实例化时报错(而非运行中)
- 接口概念(Interface)—— 多人协作时的强制契约

## 设计叙事

> 电商订单系统 v2:要接支付宝/微信/Apple Pay。
> 第一次用 if-elif 写 → 改一处动全身。
> 第二次用继承多态 → 很好,但新手漏写方法要跑起来才发现。
> 第三次用 abc 契约 → 漏实现立刻在设计期报错,不用等运行。

## 当堂练习

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `in_class/practice01.py` | ⭐⭐ | 10 分钟 | 鸭子类型:不写继承也能多态 |
| 2 | `in_class/practice02.py` | ⭐⭐⭐ | 12 分钟 | 重写 Day06 employee 为多态版(去掉 if-elif) |
| 3 | `in_class/practice03.py` | ⭐⭐⭐ | 13 分钟 | `abc.ABC` + `@abstractmethod` 基础 |
| 4 | `in_class/practice04.py` | ⭐⭐⭐⭐ | 15 分钟 | `Plugin(abc.ABC)` 插件系统基础 |
| 5 | `in_class/practice05.py` | ⭐⭐⭐⭐ | 15 分钟 | 给定的 `checkout()` 骨架 + 学员补全 Payment 子类 |
| 6 | `in_class/practice06.py` | ⭐⭐⭐⭐⭐ | 15 分钟 | 接口:多人协作的契约设计 |

## 课后作业

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `homework/task01.py` | ⭐⭐⭐⭐ | 20 分钟 | `Payment(abc.ABC)` + Alipay/WeChatPay 两个子类 |
| 2 | `homework/task02.py` | ⭐⭐⭐⭐ | 25 分钟 | NCDL 复盘:给定一段"错代码",找出哪些违反了契约 |
| 3 | `homework/task03.py` | ⭐⭐⭐⭐⭐ | 30 分钟 | 给定的 `checkout()` 骨架 + 支付系统 4 子类 + 新增一个无需改核心 |

## 小项目(当堂完成)

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `mini_project/payment_system.py` | ⭐⭐⭐⭐⭐ | 45 分钟 | `Payment(abc.ABC)` + Alipay/WeChatPay/ApplePay + `checkout()` 无 if-elif + 单元测试 |

## 门控验收

学员需提交电商支付系统,满足:
- `Payment(abc.ABC)` + 至少 3 个子类
- `checkout(cart_total, payment)` **不使用 if/elif/isinstance/type**
- 子类漏实现 `execute()` 方法时,**在实例化阶段就报 `TypeError`**
- **约束(机器可检)**:`checkout` 函数内禁止出现 `if ` / `elif ` / `isinstance` / `type(`
- **新增支付方式只需添加一个文件**(不需改任何现有代码)

## BREAK IT 环节(核心!约 45 分钟)

这是 Day07 的核心 —— NCDL 负案例教学法完整落地:

**Break It 1**(10 分钟):漏写抽象方法
  - 给学员"不完整"的 `Alipay` 子类(漏写 `execute()` 方法)
  - 学员运行立刻报 `TypeError: Can't instantiate abstract class Alipay with abstract method execute`
  - 对比 Day06:漏写时**运行中才报错**,可能找不到 bug 在哪

**Break It 2**(15 分钟):用 if-elif 绕过契约
  - 给学员一份"能跑"的 `checkout`(内含 if-elif),要求找出 3 个坏味道
  - 引导:每新增一种支付方式都要改核心函数 → 违反"开闭原则"
  - 学员亲手用多态替换 if-elif,感受差异

**Break It 3**(20 分钟):故意把 Payment 当"纯数据类"用
  - 给学员一段"忘记继承 abc.ABC"的代码
  - 学员跑起来"能跑",但漏写 execute 不会报错
  - 讨论:为什么 Python 不强制 abc? --> 引出鸭子类型哲学
  - 引出结论:abc 是"工程规范",不是"语言强制"

## 易错点

1. **混淆"继承 abc.ABC"与"继承普通类"** —— abc.ABC 的"抽象方法"是契约不是实现
2. **所有子类都实现了抽象方法,但仍报错** —— 检查父类是否使用了 `abc.ABC` 作为 metaclass
3. **用 isinstance 做"补救检查"** —— 说明多态设计还有问题,应检查接口
4. **漏写 `@abstractmethod` 装饰器** —— 方法变成普通方法,没契约效果

## 阶段复习要点

后续 Day08 L4 复习
