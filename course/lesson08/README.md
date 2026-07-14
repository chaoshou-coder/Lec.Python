# Day08 · OOP 组合+Pythonic (L4)

## 关键知识点

- **组合优于继承**(Composition over Inheritance):has-a 关系用组合
- 运算符重载:`__add__` / `__eq__` / `__lt__` 等
- `__len__` 与 `len()` 内建函数对接
- `__iter__` / `__next__` 迭代协议 —— 支持 `for x in obj`
- `__repr__` 与 `__str__` 完整对比

## 设计叙事

> 电商订单系统 v2:最后一块拼图。
> 老板:两个客户的购物车能不能合并?能不能 `len(cart)` 直接数?
> for 循环能不能直接遍历?
> 今天让自定义对象"像内置类型一样自然" —— 这就是 Pythonic。

## 当堂练习

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `in_class/practice01.py` | ⭐⭐ | 10 分钟 | 组合 vs 继承:何时用哪个 |
| 2 | `in_class/practice02.py` | ⭐⭐⭐ | 12 分钟 | `__add__` 实现购物车合并 |
| 3 | `in_class/practice03.py` | ⭐⭐⭐ | 12 分钟 | `__len__` + `__iter__` 让 `len()` / `for` 直接能用 |
| 4 | `in_class/practice04.py` | ⭐⭐⭐⭐ | 15 分钟 | `__eq__` 同款判定(购物车去重) |
| 5 | `in_class/practice05.py` | ⭐⭐⭐⭐ | 15 分钟 | 综合:`Playlist` 类完整实现 add/len/iter/eq |
| 6 | `in_class/practice06.py` | ⭐⭐⭐⭐⭐ | 15 分钟 | `__repr__` vs `__str__` + `Order 聚合`设计 |

## 课后作业

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `homework/task01.py` | ⭐⭐⭐⭐ | 25 分钟 | Order 聚合 Cart + Payment + Address(组合实践) |
| 2 | `homework/task02.py` | ⭐⭐⭐⭐⭐ | 30 分钟 | 电商订单系统 v2 雏形(全 L1-L4 知识整合) |
| 3 | `homework/task03.py` | ⭐⭐⭐⭐⭐ | 35 分钟 | 对比题:同样需求分别用继承和组合实现,分析优劣 |

## 小项目(当堂完成)

| # | 文件 | 难度 | 预计时间 | 验收 |
|---|---|---|---|---|
| 1 | `mini_project/ecommerce_v2.py` | ⭐⭐⭐⭐⭐ | 45 分钟 | 电商订单系统 v2 —— Product/Cart.__add__/__len__/__iter__ + Order(组合) + Payment(abc) |

## 门控验收

学员需提交订单系统 v2,满足:
- `ShoppingCart.__add__(other)` 合并两车
- `len(cart)` 直接返回件数
- `for item in cart` 遍历
- `product1 == product2` 同款判定
- `Order` 类**组合**了 `Cart` + `Payment` + `Address`
- **不使用继承来模拟 has-a 关系**(教师检查 Order 不应继承 Cart)

## BREAK IT 环节

**Break It 1**(10 分钟):直接用 `+` 会 TypeError
```python
cart1 = ShoppingCart([...])
cart2 = ShoppingCart([...])
cart3 = cart1 + cart2  # TypeError: unsupported operand type(s) for +: 'ShoppingCart' and 'ShoppingCart'
```
→ 引出 `__add__`:"我们想让对象怎么做,就定义对应的运算符方法"

**Break It 2**(15 分钟):只有 `__len__` 没有 `__iter__`,for 循环会报错
```python
class BadCart:
    def __len__(self): return 3
    # 没有 __iter__!

for item in BadCart():  # TypeError: 'BadCart' object is not iterable
    print(item)
```
→ 引出"协议":`len()` 用 `__len__`,`for` 用 `__iter__`,想支持什么操作就实现什么协议

**Break It 3**(10 分钟):继承模拟组合 → 设计坏味道
```python
# 错误示范:
class Order(ShoppingCart):  # Order is-a Cart?! 设计错误!
    ...
```
→ "继承是 is-a,组合是 has-a" 的判断练习

## 易错点

1. **`__add__` 修改了原对象而非返回新对象** —— 运算符通常应返回新对象
2. **只写 `__len__` 没写 `__iter__`** —— `for` 循环仍不可用
3. **`__eq__` 漏写导致对象比较变成身份比较(`is` 而非 `==`)**
4. **用继承模拟 has-a 关系** —— is-a(继承) vs has-a(组合) 混淆

## 阶段复习要点

Day09 复习日综合(购物车从 dict 到完整 OOP 系统)
