# Day08 · OOP 组合+Pythonic (L4)

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day01-07(print/input/变量/字符串/分支/循环/函数/列表字典/
> OOP 封装/继承/多态)
> 关键问题: 我们写的类能不能像内置类型(int/list/str)一样**自然运算**?
> 能不能 `cart1 + cart2`、`len(cart)`、`for item in cart`?
> 本节让自定义对象"融入 Python 生态" —— 这就是 Pythonic。
> 叙事锚点: 电商订单系统 v2 —— 最后一公里

---

## 0. 引入(10 分钟)

- **破冰**(2 分钟): 用 `+` 把两个列表加起来 → 引出"运算符是对象的方法"。
- **痛点演示**(3 分钟):
  - `cart1 + cart2` → `TypeError`
  - `len(cart1)` → `TypeError`
  - `for item in cart1` → `TypeError`
  - 看起来很简单的事,自定义类都得从头造轮子?
- **微项目预告**(5 分钟): 今天产出 —— 订单系统 v2,
  `cart1 + cart2` 合并,`len(cart)` 直接数,`for item in cart` 遍历。

---

## 1. 第一讲(15 分钟) —— 组合优于继承

### 知识点 1.1 is-a vs has-a

- **is-a**(继承):`Dog is-a Dog` → `class Dog(Animal)`
- **has-a**(组合):`Order has-a Cart + Payment + Address`

### 知识点 1.2 继承的三个坏味道(该用组合时)

1. 子类使用了父类的**少数几个方法** → 说明不是真正的 is-a
2. 子类**屏蔽/跳过**父类的一些方法 → 说明分类不对
3. 继承层级 **> 3 层** → 说明抽取方式有问题

### BREAK IT: 用继承模拟组合

```python
class Order(ShoppingCart):  # 订单 is-a 购物车? 错!
    def __init__(self):
        super().__init__()
        self.payment = None
        self.address = None
```

学员讨论:这样写的坏处?(修改 Cart 会影响 Order,...)。

---

## 2. 当堂练 1(20 分钟)

- 练习 1: `in_class/practice01.py` —— 组合 vs 继承判断题(⭐⭐,10 分钟)
- 练习 2: `in_class/practice02.py` —— `ShoppingCart.__add__`(⭐⭐⭐,12 分钟)

---

## 3. 第二讲(15 分钟) —— 运算符重载:`__add__` / `__eq__` / `__lt__`

### 知识点 3.1 常用运算符对应魔术方法

| 运算符 | 魔术方法 |
|---|---|
| `a + b` | `a.__add__(b)` |
| `a == b` | `a.__eq__(b)` |
| `a < b` | `a.__lt__(b)` |
| `a != b` | `a.__ne__(b)` |
| `a > b` | `a.__gt__(b)` |

### 知识点 3.2 运算符重载的契约

- `__add__` 应**返回新对象**,不修改原对象
- `__eq__` 应满足:自反性、对称性、传递性
- 如果不确定如何实现,先想想内置 `list` / `int` 的做法

---

## 4. BREAK IT 核心环节(30 分钟)

### Break It 1(15 分钟):只有 `__len__`,没有 `__iter__`

```python
class BadCart:
    def __init__(self, items): self.items = items
    def __len__(self): return len(self.items)
    # 没有 __iter__!

len(BadCart([1,2,3]))  # 3 → 看起来 OK?
for item in BadCart([1,2,3]):  # TypeError: 'BadCart' object is not iterable
    print(item)
```

学员体会:**协议**:`len()` 用 `__len__`,`for` 用 `__iter__`,想支持什么操作就实现什么协议。

### Break It 2(15 分钟):继承 vs 组合的选择题

给出 5 个候选设计(3 个错用继承),学员举手投票"该用继承还是组合"。

---

## 5. 当堂练 2(25 分钟)

- 练习 3: `in_class/practice03.py` —— `__len__` + `__iter__`(⭐⭐⭐,12 分钟)
- 练习 4: `in_class/practice04.py` —— `__eq__` 同款判定(⭐⭐⭐⭐,15 分钟)

---

## 6. 第三讲(15 分钟) —— `__iter__` 迭代协议

### 知识点 6.1 `for obj` 是怎么工作的

本质:Python 调 `iter(obj)`,循环调 `next()` 直到 `StopIteration`。

### 知识点 6.2 两种实现方式

- **方式 1(简单)**:类内同时写 `__iter__`(返回 self)和 `__next__`
- **方式 2(推荐)**:用 `yield` 生成器 —— `__iter__` 里 `yield` 每个元素

---

## 7. 当堂练 3(25 分钟)

- 练习 5: `in_class/practice05.py` —— Playlist 类完整(⭐⭐⭐⭐,15 分钟)
- 练习 6: `in_class/practice06.py` —— `__repr__` vs `__str__` + Order 聚合(⭐⭐⭐⭐⭐,15 分钟)

---

## 8. 小项目:电商订单系统 v2(45 分钟)

- 项目: `mini_project/` 新建 `ecommerce_v2.py`
- 要求(整合 L1-L4):
  1. `Product` 类(`__init__`+`@property`+`__str__`+`__eq__`) → L1
  2. `PhysicalProduct(DigitalProduct)` 子类 → L2
  3. `Payment(abc.ABC)` + Alipay/WeChatPay/ApplePay → L3
  4. `ShoppingCart.__add__` / `__len__` / `__iter__` → L4
  5. `Order` 组合了 Cart + Payment + Address → L4
  6. `checkout(cart_total, payment)` 多态调用,无 if-elif → L3

---

## 9. 总结(5 分钟)

- **本日错 3 件事**:
  1. `__add__` 修改了原对象(应返回新对象)
  2. 只写 `__len__` 没写 `__iter__`(for 循环仍不可用)
  3. 用继承模拟 has-a(该用组合)
- **作业说明**: `homework/task01-03.py`,下节课(复习日)前 10 分钟复盘。

---

## 延伸题

- (PyNative Ex29,⭐⭐⭐⭐):组合 — Zoo 喂养所有动物。
- (PyNative Ex31,⭐⭐⭐⭐):Playlist 增删改查 + 洗牌。
- (Think Python 2E Ch18,⭐⭐⭐⭐⭐):扑克牌模拟(Card/Deck/Hand/Player)。
