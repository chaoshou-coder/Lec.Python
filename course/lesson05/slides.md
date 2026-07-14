# Day05 · OOP 封装 (L1)

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day01-04(print/input/变量/字符串/分支/循环/函数/列表字典)
> 关键问题: 函数把"行为"打包成工具,但数据还散着 —— 能不能把
> **数据 + 行为**打包成一个整体(对象)?本节进入**类与对象**的世界。
> 叙事锚点: 电商订单系统 v2 — 从散落的 dict 到 Product 类

---

## 0. 引入(10 分钟)

- **破冰 + 抽问**(3 分钟): 前 4 天用字典表示一个商品
  `{"name": "Python入门", "price": 59.8}` —— 数据有了,但打折的
  函数在外面,怎么做到 `product.discount(0.8)` 这种'自己的
  数据自己算'?
- **赏玩 demo**(2 分钟): 当场定义一个 `Dog` 类,`dog.bark()`
  直接叫,学员第一次看到"自己造的类型也能用点号访问方法"。
- **微项目预告**(5 分钟): 告诉学员今天的最终产出 ——
  一个能保护余额/友好打印的 `BankAccount` 类。

---

## 1. 第一讲(15 分钟) —— 类与构造函数

### 知识点 1.1 `class` 定义类

类是**对象的蓝图/模板**。用 `class` 关键字定义,类名约定
**大驼峰**(`Student`、`Product`)。

### 知识点 1.2 `__init__` 构造函数

`__init__(self, ...)` 在**实例化时自动调用**,用来初始化对象
的属性。`self` 代表"当前这个对象"。

> 口诀:**`__init__` 是构造函数,`self` 是自己,造对象时自动跑**。

### 知识点 1.3 实例方法

第一个参数写 `self`,通过 `self.属性名` 访问对象自己的数据。

### BREAK IT:故意漏写 self

教师演示:漏写 `self` 参数,让学生读 `TypeError`。

---

## 2. 当堂练 1(20 分钟)

- 练习 1: `in_class/practice01.py` —— `Product` 类定义(⭐⭐,8 分钟)
- 练习 2: `in_class/practice02.py` —— `Product.info()` 实例方法(⭐⭐,10 分钟)

> 巡场重点: 学员是否在 `__init__` 内写了 `self.name = name`(而非 `name = name`)。

---

## 3. 第二讲(15 分钟) —— 类属性 vs 实例属性 + @property

### 知识点 3.1 类属性 vs 实例属性

- **类属性**:写在类体内、方法外,被所有实例**共享**。
- **实例属性**:写在 `self.xxx = ...` 里,**每个实例独立**。

### 知识点 3.2 @property:伪属性 + 写保护

`@property` 把一个方法伪装成 '只读属性'；
`@xxx.setter` 给这个 '属性' 加上写保护逻辑。

### BREAK IT: 直接暴露 attribute 的后果

演示:直接暴露 `balance`,用户可以赋负数 → 引出 `@property` 需求。

---

## 4. 当堂练 2(25 分钟)

- 练习 3: `in_class/practice03.py` —— `Student` `@property` 成绩校验(⭐⭐⭐,12 分钟)
- 练习 4: `in_class/practice04.py` —— `Product.__str__`(⭐⭐⭐,12 分钟)

> 巡场重点: 练习 3 学员常忘记 `@xxx.setter` 必须与 `@property` 同名;
  练习 4 学员常 `__str__` 直接 return 数字(应 return str)。

---

## 5. 第三讲(15 分钟) —— `__str__` 与对象打印

### 知识点 5.1 为什么 `print(对象)` 不可读

`print(对象)` 默认打印 `<__main__.BankAccount object at 0x...>`,
调试时完全看不出对象里装了什么数据。

### 知识点 5.2 `__str__` 与 `__repr__` 的区别

- `__str__` 面向 '用户可读',print 时触发。
- `__repr__` 面向 '开发者调试',交互式提示符默认显示。

---

## 6. 当堂练 3(25 分钟)

- 练习 5: `in_class/practice05.py` —— 类属性 `tax_rate` 共享(⭐⭐⭐,13 分钟)
- 练习 6: `in_class/practice06.py` —— `@property` setter 余额保护(⭐⭐⭐⭐,15 分钟)

---

## 7. 小项目:BankAccount 综合类(45 分钟)

- 项目: `mini_project/` 新建 `bankaccount.py`
- 要求:封装 5 项能力,并在主程序里调用验证:
  1. `__init__(owner, balance)` 绑定属性
  2. `@property` 保护 balance(不允许为负)
  3. `deposit(amount)` 存款,返回余额
  4. `withdraw(amount)` 取款,超额拒绝
  5. `__str__` 输出 `BankAccount(owner=xxx, balance=xxx)`

> 巡场重点: 每个函数**只负责一件事**,不要在一个函数里又算又打印。

---

## 8. 总结(5 分钟)

- **本日错 3 件事**(课后教师把真实错例填进 `teacher_notes.md`):
  1. 忘写 `self` 或 `self.`,导致属性未绑定
  2. `@property` 忘了写对应的 `@xxx.setter`
  3. `__str__` 返回了非 str 类型
- **作业说明**: `homework/task01-03.py`,下节课前 10 分钟复盘。

---

## 易错点

1. **实例方法忘写 `self` 参数** —— 口诀"实例方法第一个必 self"。
2. **直接 return 数字而非 str** —— `__str__` 必须返回 `str`。
3. **`@xxx.setter` 名字与 `@property` 不同名** —— 赋值不触发 setter。
4. **通过实例给类属性赋值** —— 会创建实例属性,遮盖类属性。

## 延伸题

- (CS50P Week2,⭐⭐): 输入"7:00" 或 "12:30",判断是早餐/午餐/晚餐时间。
- (PyNative Ex11,⭐⭐⭐): `CoffeeMachine` 多资源跟踪。
