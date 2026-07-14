# Day07 · OOP 多态+契约 (L3)

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day01-06(print/input/变量/字符串/分支/循环/函数/列表字典/
> OOP 封装/继承)
> 关键问题: 同一种操作要处理多种类型,if-elif 越改越痛 ——
> 能不能让"新增类型"**无需修改核心函数**即可接入?
> 叙事锚点: 电商订单系统 v2 — Payment(abc) 支付系统
> 教学法: 本节是 NCDL(负案例驱动学习)的完整落地

---

## 0. 引入(10 分钟)(NCDL 三步之"先展示痛点")

- **痛点演示**(5 分钟): 给出 120 行 `pay(payment_type, amount)` if-else 代码。
  要求:新增 Apple Pay。
  学员发现:要在核心函数里加新分支 → **改一处动全身**。
- **重构预告**(3 分钟): 今天要让 "新增支付方式 = 添加一个文件"。
- **微项目预告**(2 分钟): 今天终极产出 —— `checkout()` 只有 4 行,3 种支付即插即用。

---

## 1. 第一讲(15 分钟) —— 鸭子类型:Python 的多态哲学

### 知识点 1.1 "像鸭子就是鸭子"

> "If it walks like a duck and quacks like a duck, it's a duck."

- 不需要继承同一个父类
- 只需要对象有同名方法
- Python 是动态类型,天然支持

### 知识点 1.2 为什么 Python 不需要"声明接口"

对比:
- Java/C#:必须先 `implements IPayment` → 编译器强制
- Python:跑起来再说 → 运行时才报错

### BREAK IT: Python 鸭子类型的代价

```python
class BrokenAlipay:
    # 漏写 execute 方法!
    pass

def checkout(total, payment):
    return payment.execute(total)  # AttributeError! 运行到这里才报错

checkout(99, BrokenAlipay())  # 可能过了好几天才跑到这一行!
```

学员体会:**鸭子类型的弱点 —— bug 难追溯**。

---

## 2. 当堂练 1(15 分钟)

- 练习 1: `in_class/practice01.py` —— 不写继承也能多态(⭐⭐,10 分钟)
- 练习 2: `in_class/practice02.py` —— Day06 employee 多态重写(⭐⭐⭐,12 分钟)

---

## 3. 第二讲(15 分钟) —— abc.ABC:把契约写进代码

### 知识点 3.1 用 `abc.ABC` + `@abstractmethod` 锁定接口

```python
import abc

class Payment(abc.ABC):
    @abc.abstractmethod
    def execute(self, amount): ...
```

- 继承 `abc.ABC` → 类成为抽象基类
- `@abstractmethod` 装饰 → 子类必须实现,否则**实例化时报错**
- 错误提前:从"运行中"提前到"实例化时"

### 知识点 3.2 抽象类 vs 鸭子类型的取舍

| | 鸭子类型 | abc.ABC |
|---|---|---|
| 哲学 | "跑起来再说" | "先签合同" |
| 报错时机 | 运行中 | 实例化时 |
| 适用 | 个人脚本 | 团队协作 |
| 学习曲线 | 低 | 中 |

**推荐**: 团队项目用 abc,除非你有充分理由不用。

---

## 4. BREAK IT 核心环节(45 分钟)

### Break It 1(15 分钟):漏写抽象方法

给学员"不完整"的 Alipay 子类:
```python
class Alipay(Payment):
    # 漏写 execute 方法!
    pass

alipay = Alipay()  # TypeError! 立刻报错
```

学员对比 Day06:漏写时**运行中才报错**,可能找不到 bug 在哪。

### Break It 2(15 分钟):用 if-elif 绕过契约

给学员一份"能跑"的 checkout(内含 if-elif),要求找出 3 个坏味道:
1. 每新增一种支付方式都要改核心函数
2. 违反"开闭原则"
3. 函数体越来越长

学员亲手用多态替换 if-elif,感受差异。

### Break It 3(15 分钟):忘记继承 abc.ABC

给学员一段"忘记继承 abc.ABC"的代码:
```python
class Payment:  # 没有 abc.ABC!
    @abc.abstractmethod
    def execute(self, amount): ...
```

学员跑起来"能跑",但漏写 execute 不会报错。
讨论:为什么 Python 不强制 abc? → 引出鸭子类型哲学。

---

## 5. 当堂练 2(25 分钟)

- 练习 3: `in_class/practice03.py` —— abc.ABC + @abstractmethod 基础(⭐⭐⭐,13 分钟)
- 练习 4: `in_class/practice04.py` —— Plugin(abc.ABC) 插件系统(⭐⭐⭐⭐,15 分钟)

---

## 6. 第三讲(10 分钟) —— 接口概念(团队协作契约)

### 知识点 6.1 接口 = 只包含抽象方法的抽象类

- Python 没有 `interface` 关键字
- 用"全抽象方法的 ABC"模拟接口
- 多人协作时:架构师定义接口,开发者各自实现

### 知识点 6.2 接口 vs 抽象类的区别

| | 接口 | 抽象类 |
|---|---|---|
| 方法 | 全部抽象 | 可以有普通方法 |
| 属性 | 通常没有 | 可以有 |
| 用途 | "能做什么"契约 | "是什么"共性 |

---

## 7. 当堂练 3(20 分钟)

- 练习 5: `in_class/practice05.py` —— 给定的 checkout() 骨架 + 学员补全(⭐⭐⭐⭐,15 分钟)
- 练习 6: `in_class/practice06.py` —— 接口:多人协作契约(⭐⭐⭐⭐⭐,15 分钟)

---

## 8. 小项目:Payment 支付系统(45 分钟)

- 项目: `mini_project/` 新建 `payment_system.py`
- 要求:
  1. `Payment(abc.ABC)` + `execute(amount)` 抽象方法
  2. 三个子类:`Alipay` / `WeChatPay` / `ApplePay`
  3. `checkout(cart_total, payment)` 函数 ≤4 行,无 if-elif
  4. 单元测试:每种支付都能正常 checkout
  5. 新增 ApplePay 只需添加一个文件

---

## 9. 总结(5 分钟)

- **本日错 3 件事**:
  1. 漏写 `@abstractmethod` 装饰器 → 方法变成普通方法,没契约效果
  2. 用 isinstance 做"补救检查" → 说明多态设计还有问题
  3. 混淆"继承 abc.ABC"与"继承普通类" → 抽象方法不是实现
- **作业说明**: `homework/task01-03.py`。

---

## 延伸题

- PyNative Ex18(⭐⭐⭐⭐):Shape(ABC) + Circle/Rectangle。
- GeeksforGeeks OOP(⭐⭐⭐⭐):abc.ABC 实现。
