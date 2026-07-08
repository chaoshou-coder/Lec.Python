# Day20 · OOP(继承 + 多态)

## 关键知识点
- 单继承:`class Dog(Animal)`
- 通过 `super().__init__()` 调用父类构造
- 方法重写(Override)
- 多态体验:同接口异实现、遍历不同子类对象
- 类属性 vs 实例属性(`Animal.count` 类级共享计数)
- 抽象方法 / 基类 `area()` 默认返回 0

## 当堂练习

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `in_class/practice01.py` | ⭐⭐ | 10 分钟 | 定义基类 Animal + speak() |
| 2 | `in_class/practice02.py` | ⭐⭐⭐ | 15 分钟 | Dog/Cat 重写 speak() 汪汪/喵喵 |
| 3 | `in_class/practice03.py` | ⭐⭐⭐ | 15 分钟 | let_speak 函数,体验多态调度 |
| 4 | `in_class/practice04.py` | ⭐⭐⭐⭐ | 20 分钟 | Animal.count 类属性统计实例数 |
| 5 | `in_class/practice05.py` | ⭐⭐⭐⭐ | 20 分钟 | Shape/Circle/Rectangle 重写 area |
| 6 | `in_class/practice06.py` | ⭐⭐⭐⭐⭐ | 25 分钟 | total_area 多态累加不同图形面积 |

## 课后作业

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `homework/task01.py` | ⭐⭐⭐ | 15 分钟 | Employee/Manager/Developer 方法重写 |
| 2 | `homework/task02.py` | ⭐⭐⭐⭐ | 20 分钟 | FileHandler 多态读写 txt/json |
| 3 | `homework/task03.py` | ⭐⭐⭐⭐⭐ | 30 分钟 | SavingsAccount/CheckingAccount 取款扩展 |

## 小 / 中型项目

本节以 `Circle`/`Rectangle` 与 `Animal`/`Dog`/`Cat`/`Shape` 系列练习强化多态体验,为下节 Day21 期末综合做准备。

## 阶段复习要点

后续 Day21 期末总复习将大综合考察封装、继承、多态三大 OOP 支柱
