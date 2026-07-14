# Day06 · OOP 继承 (L2)

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day01-05(print/input/变量/字符串/分支/循环/函数/列表字典/
> OOP 封装)
> 关键问题: 当几个类的代码几乎一样,复制粘贴越多改 bug 越痛 ——
> 能不能**抽共性到上层**,差异留在下层?
> 叙事锚点: 电商订单系统 v2 — Product 基类 + Physical/Digital 子类

---

## 0. 引入(10 分钟)

- **痛点演示**(5 分钟): 给出两份 90% 重复的代码
  (`PhysicalProduct` + `DigitalProduct`),要求改运费计算 →
  学员发现要改两处 → 引出"代码坏味道:重复"。
- **赏玩 demo**(2 分钟): 给出重构后的基类 + 子类版本,
  改一处即生效。
- **微项目预告**(3 分钟): 今天的最终产出 —— 员工薪资系统
  `show_pay` 函数一行调用,多态执行。

---

## 1. 第一讲(15 分钟) —— 为什么需要继承(is-a 关系)

### 知识点 1.1 继承 = 代码复用 + is-a 语义

- 子类**自动拥有**父类的属性和方法
- 子类可以**扩展**或**修改**父类行为
- `class Dog(Animal):` 代表 "Dog is-a Animal"

### 知识点 1.2 Python 单继承语法

`class 子类(父类):` 括号里写父类名,Python 支持多继承
(本节只讲单继承)。

### BREAK IT: 忘记继承括号

教师演示:`class Dog Animal:`(漏冒号) 和 `class Dog:`(漏括号) 的报错。

---

## 2. 当堂练 1(20 分钟)

- 练习 1: `in_class/practice01.py` —— Product→Book 继承(⭐⭐,10 分钟)
- 练习 2: `in_class/practice02.py` —— `super().__init__()` 扩展(⭐⭐⭐,12 分钟)

---

## 3. 第二讲(15 分钟) —— `super().__init__()` 深度

### 知识点 3.1 子类构造函数必须调 `super()`

- `super().__init__(父类参数)` 安全调用父类构造函数
- 等价于 `Animal.__init__(self, ...)`,但**更规范**

### 知识点 3.2 方法重写(override)

- 子类**同名定义**即覆盖父类方法
- 如果想保留父类版本并扩展:子类里用 `super().方法()`

### BREAK IT: 重写 `__init__` 忘调 super → 父类属性丢失

```python
class Dog(Animal):
    def __init__(self, name, breed):
        # 忘记 super().__init__(name) ← BREAK IT!
        self.breed = breed

dog = Dog("旺财", "柯基")
print(dog.name)  # AttributeError! Dog 没有 name 属性
```

---

## 4. 当堂练 2(25 分钟)

- 练习 3: `in_class/practice03.py` —— 继承+重写+`super().方法()`(⭐⭐⭐,12 分钟)
- 练习 4: `in_class/practice04.py` —— 动物园体系(Animal→Dog/Cat + 多态)(⭐⭐⭐,13 分钟)

---

## 5. 第三讲(15 分钟) —— MRO + isinstance 反模式

### 知识点 5.1 MRO(Method Resolution Order)

查找顺序:**子类 → 父类 → 父类的父类 → object**。
可看 `ClassName.__mro__`。

### 知识点 5.2 isinstance / issubclass

- `isinstance(obj, cls)` 判断对象是否是某类实例
- **反模式**:用 isinstance 做类型分发 → 应该用多态

### BREAK IT: 用 isinstance 做分发的"扩展噩梦"

```python
# 反模式代码(给学员 5 分钟找错):
def show_pay(emp):
    if isinstance(emp, Manager):
        return emp.base + emp.bonus
    elif isinstance(emp, Sales):
        return emp.base + emp.commission
    # 每加一个新员工类型都要改这个函数! ← BUG!
```

---

## 6. 当堂练 3(25 分钟)

- 练习 5: `in_class/practice05.py` —— Employee+Manager+Sales(⭐⭐⭐⭐,15 分钟)
- 练习 6: `in_class/practice06.py` —— MRO + isinstance 反模式(⭐⭐⭐⭐,13 分钟)

---

## 7. 小项目:员工薪资系统(45 分钟)

- 项目: `mini_project/` 新建 `employee_pay.py`
- 要求:
  1. `Employee` 基类:`name` + `base_salary` + `pay()` 返回 base_salary
  2. `Manager(Employee)`:新增 `bonus`,**重写** `pay()` = base + bonus
  3. `Sales(Employee)`:新增 `commission`,**重写** `pay()` = base + commission
  4. 用 `super().__init__()` 调用父类构造
  5. 写 `show_pay(emp)` 打印 `emp.name + emp.pay()`(**多态**)
  6. 用 `isinstance 检查:禁止！`

---

## 8. 总结(5 分钟)

- **本日错 3 件事**:
  1. 子类重写 `__init__` 忘调 `super().__init__()` → 父类属性丢失
  2. 用 `isinstance` 做类型分发 → 每加新类都改分发函数
  3. 继承层级 > 3 层 → 应该用组合替代
- **作业说明**: `homework/task01-03.py`。

---

## 延伸题

- PyNative Ex13-15(⭐⭐⭐):Bus/Vehicle 继承体系。
- PyNative Ex16(⭐⭐⭐):Dog/Cat 多态。
