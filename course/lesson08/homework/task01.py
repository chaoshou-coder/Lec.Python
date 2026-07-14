"""
[难度: ⭐⭐⭐⭐]
[所属知识点: Order 聚合 Cart + Payment + Address]
[预计完成时间: 25 分钟,选做]

题目描述:
    电商订单系统 v2 的 L4 部分。

    - `Product` 类(name + price + __eq__ + __str__)
    - `ShoppingCart` 类(items + __len__ + __iter__)
    - `Address` 类(city + detail)
    - `Order` 类**组合** Cart + Address
      - 方法 `total()`:返回购物车总价
      - 方法 `summary()`:返回订单摘要

    验证:
    1. Order 不继承 Cart(组合而非继承)
    2. len(cart) 可用
    3. for item in cart 可用
    4. 两个同名 Product == 为 True

示例:
    >>> p1 = Product("Python", 50)
    >>> p2 = Product("算法", 30)
    >>> cart = ShoppingCart([p1, p2])
    >>> addr = Address("北京", "朝阳")
    >>> order = Order(cart, addr)
    >>> print(order.summary())
    订单含 2 件,总价: 80,送到: 北京
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        pass

    def __hash__(self):
        pass

    def __str__(self):
        pass

class ShoppingCart:
    def __init__(self, items=None):
        self.items = items or []

    def __len__(self):
        pass

    def __iter__(self):
        pass

class Address:
    def __init__(self, city, detail):
        self.city = city
        self.detail = detail

class Order:
    """组合 Cart + Address"""
    def __init__(self, cart, address):
        pass

    def total(self):
        pass

    def summary(self):
        pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    p1 = Product("Python", 50)
    p2 = Product("算法", 30)
    cart = ShoppingCart([p1, p2])
    addr = Address("北京", "朝阳")
    order = Order(cart, addr)

    # 组合验证
    assert not isinstance(order, ShoppingCart)
    assert order.cart is cart

    # __len__ / __iter__
    assert len(cart) == 2
    assert [p.name for p in cart] == ["Python", "算法"]

    # __eq__
    assert Product("Python", 50) == Product("Python", 999)

    # total / summary
    assert order.total() == 80
    text = order.summary()
    assert "2" in text and "80" in text and "北京" in text
    print("✅ 所有测试通过")
