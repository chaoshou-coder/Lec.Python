# Day08 · OOP 基础

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day01-07(print/input/变量/字符串/分支/循环/函数/列表字典/
> 文件 I/O/异常)
> 关键问题: 函数把"行为"打包成工具,但数据还散着 —— 能不能把
> **数据 + 行为**打包成一个整体(对象)?本节引入面向对象编程(OOP)
> 的三大基石:封装、属性、魔术方法

---

## 0. 引入(5 分钟)

- **破冰 + 抽问**(2 分钟): "前 7 天我们用字典表示一个学生
  `{"name": "小明", "scores": [90, 85]}` —— 数据有了,但计算
  平均分的函数在外面,怎么做到 `student.average()` 这种'自己的
  数据自己算'?"引出**类**(class):**数据 + 方法**打包。
- **赏玩 demo**(3 分钟): 当场定义一个 `Dog` 类,`dog.bark()`
  直接叫,学员第一次看到"自己造的类型也能用点号访问方法"。

---

## 1. 第一讲(15 分钟) —— 类与构造函数

### 知识点 1.1 `class` 定义类

类是**对象的蓝图/模板**。用 `class` 关键字定义,类名约定
**大驼峰**(`Student`、`ShoppingCart`)。

```python
class Dog:
    pass

dog = Dog()   # 实例化:用类制造一个具体的对象
print(type(dog))  # <class '__main__.Dog'>
```

### 知识点 1.2 `__init__` 构造函数

`__init__(self, ...)` 在**实例化时自动调用**,用来初始化对象
的属性。`self` 代表"当前这个对象"。

```python
class Dog:
    def __init__(self, name, age):
        self.name = name    # 实例属性:每个对象各有一份
        self.age = age

dog1 = Dog("旺财", 3)
dog2 = Dog("小白", 5)
print(dog1.name)    # 旺财
print(dog2.name)    # 小白(互不影响)
```

> 口诀:**`__init__` 是构造函数,`self` 是自己,造对象时自动跑**。

### 知识点 1.3 实例方法

第一个参数写 `self`,通过 `self.属性名` 访问对象自己的数据。

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name}:汪汪!")

dog = Dog("旺财", 3)
dog.bark()      # 旺财:汪汪!
```

> 🔴 教学红线(`self` 不用传): `dog.bark()` 等价于
> `Dog.bark(dog)`,Python 自动把 `dog` 传成 `self`,调用时**别
> 再传一遍**。

## 2. 当堂练 1(20 分钟)

- 练习 1: `in_class/practice01.py` —— 定义 `Book` 类(书名/
  作者/价格),实例化并打印属性(⭐⭐,8 分钟)
- 练习 2: `in_class/practice02.py` —— 给 `Book` 加 `info()`
  方法,返回格式化字符串(⭐⭐⭐,12 分钟)

> 巡场重点: 学员常漏写 `self`,写成 `def bark():`,调用时报
> `TypeError: bark() takes 0 positional arguments but 1 was given`。

---

## 3. 第二讲(15 分钟) —— 类属性 vs 实例属性 + `@property`

### 知识点 3.1 类属性 vs 实例属性

```python
class Student:
    school = "清华大学"      # 类属性:所有实例共享

    def __init__(self, name):
        self.name = name    # 实例属性:每个对象各有一份

s1 = Student("小明")
s2 = Student("小红")
print(s1.school)    # 清华大学(共享)
print(s2.school)    # 清华大学
```

### 知识点 3.2 `@property` 把方法变成"属性"

想**校验/计算**某个值时,用 `@property`。访问时像属性一样
`obj.name`,背后其实调了方法。

```python
class Student:
    def __init__(self, name):
        self._name = name       # 习惯:单下划线表示"内部值"

    @property
    def name(self):
        return self._name       # getter:读取时触发

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("姓名不能为空")
        self._name = value      # setter:赋值时触发校验

stu = Student("小明")
print(stu.name)        # 小明      ← 像读属性,实际调 getter
stu.name = "小红"      ← 像写属性,实际调 setter 校验
```

> 口诀:**`@property` 让方法伪装成属性,读/写都能加校验逻辑**。

### 知识点 3.3 `__str__` 与 `__repr__` 魔术方法

- `__str__`:`print(obj)` 时触发,给人看的,友好字符串。
- `__repr__`:`repr(obj)` / 交互式输入时触发,给开发者看的,最好能`eval()` 还原。

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age}岁)"

dog = Dog("旺财", 3)
print(dog)      # 旺财(3岁)    ← 调 __str__
```

## 4. 当堂练 2(25 分钟)

- 练习 3: `in_class/practice03.py` —— 给 `Student` 加
  `@property` 校验成绩 0-100,越界抛 `ValueError`(⭐⭐⭐,12 分钟)
- 练习 4: `in_class/practice04.py` —— 给 `Book` 加 `__str__`,
  `print(book)` 输出 `"《Python入门》- 李明 著"`(⭐⭐⭐,13 分钟)

> 巡场重点: 练习 3 学员常把 `@name.setter` 写成 `@name_setter`,
> 强调**setter 装饰器名必须和 property 同名**。

---

## 5. 第三讲(15 分钟) —— 继承入门

### 知识点 5.1 继承:子类复用父类的代码

`class 子类(父类):` —— 子类**继承**父类所有方法和属性,还能
**扩展**或**覆盖**。

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}:???")

class Dog(Animal):          # Dog 继承 Animal
    def speak(self):        # 覆盖父类方法
        print(f"{self.name}:汪汪!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name}:喵!")

Dog("旺财").bark()       # 旺财:汪汪!
Cat("小白").speak()      # 小白:喵!
```

### 知识点 5.2 `super()` 调用父类方法

子类想**复用**父类的 `__init__` 而不是全部重写,用 `super()`。

```python
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # 调 Animal.__init__
        self.breed = breed      # 子类扩展的属性

    def speak(self):
        print(f"{self.name}({self.breed}):汪汪!")
```

> 口诀:**继承用 `class 子(父)`,复写用 `super()`,覆盖就重写同名**。

## 6. 当堂练 3(25 分钟)

- 练习 5: `in_class/practice05.py` —— `Vehicle` 父类 + `Car`
  / `Bike` 子类,各自覆盖 `move()` 方法(⭐⭐⭐,12 分钟)
- 练习 6: `in_class/practice06.py` —— 类属性实现"统计共创建
  了多少个实例"(⭐⭐⭐⭐,13 分钟)

> 巡场重点: 练习 6 学员常在 `__init__` 里写 `self.count += 1`,
> 这会变成实例属性,强调**类属性用 `类名.count` 改**。

---

## 7. 小项目:Student 类综合(45 分钟)

- 项目: `mini_project/` 新建 `student.py`
- 需求:
  1. `Student(name, scores)` —— `scores` 是成绩列表。
  2. `@property average` 计算平均分。
  3. `__str__` 返回 `"小明: 平均分 88.5 (3 科)"`。
  4. 用 `@property` + setter 校验成绩范围 0-100。
  5. 用异常处理让非法成绩不崩溃,提示后要求重新输入。

```python
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    @property
    def average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

    def __str__(self):
        return (f"{self.name}: 平均分 "
                f"{self.average:.1f} ({len(self.scores)}科)")

stu = Student("小明", [90, 85, 92])
print(stu)      # 小明: 平均分 89.0 (3科)
```

> 巡场重点: 学员常把 `average` 当方法写 `stu.average()`,加
> `@property` 后变成 `stu.average`,不再加括号。

---

## 8. 总结(5 分钟)

- **本日错 3 件事**(课后教师把真实错例填进 `teacher_notes.md`):
  1. 漏写 `self` 参数,调用时报 `TypeError` 多传了一个参数
  2. 给已有 `@property` 的 setter 写错装饰器名,setter 不生效
  3. 改类属性用了 `self.count`,实际改了实例属性,类属性没变动
- **作业说明**: `homework/task01.py`(BankAccount 类+余额校验)、
  `homework/task02.py`(Animal 继承体系)、`homework/task03.py`
  (类属性统计实例数+文件持久化),下节课前 10 分钟复盘。

---

## 易错点

1. **`self` 必须作为实例方法的第一个参数**,调用时由 Python
   自动传入,不要再传一遍。
2. **`@property` 装饰的方法是属性**,访问时不再加 `()`;setter
   装饰器名必须和 property **同名**。
3. **类属性用 `类名.属性` 访问/修改**,`self.属性` 是实例属性,
   两者互不干扰。
4. **`__init__` 构造函数不需要 `return`**,它永远返回 `None`,
   不能在 `__init__` 里 `return 值`。
5. **`super().__init__()` 必须在子类 `__init__` 最前面调用**,
   否则父类属性还没建好。

## 延伸题

- **(CS50P Week8 OOP, ⭐⭐)**: 定义一个 `Student` 类,用
  `@property` 计算 GPA —— 巩固类 + property。
- **(Real Python OOP, ⭐⭐⭐)**: 实现 `BankAccount` 类,余额
  低于 0 时抛 `ValueError`,取款超出余额同样异常 —— 巩固
  `@property` + 异常。
- **(MIT 6.100L, ⭐⭐⭐⭐)**: 实现 `Person` → `MITPerson` →
  `Student` 三层继承链,体现 `super()` 复用 —— 巩固继承。
