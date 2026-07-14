"""
[难度: ⭐⭐⭐⭐⭐]
[所属知识点: __repr__ vs __str__ + Order 聚合]
[预计完成时间: 15 分钟]

题目描述:
    1. 实现 `Product` 类:
       - `__repr__` 返回 `Product('name', price)`(能 eval)
       - `__str__` 返回 `"[name]: price 元"`(友好)
    2. 实现 `Order` 类(组合):
       - 持有 `Product` 实例
       - 持有 `Address` 实例
       - 方法 `summary()` 返回订单摘要
    3. 验证 `print(order)` 走 `__str__`,
       而 `repr(order)` 走 `__repr__`。

示例:
    >>> p = Product("Python", 59.8)
    >>> print(repr(p))
    Product('Python', 59.8)
    >>> print(p)
    [Python]: 59.8 元
    >>> addr = Address("北京")
    >>> order = Order(p, addr)
    >>> print(order.summary())
    [Python]: 59.8 元  -> 送到 北京
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # 请补全 __repr__ 和 __str__
    pass

class Address:
    def __init__(self, city):
        self.city = city

class Order:
    """组合 Product + Address"""
    def __init__(self, product, address):
        pass

    def summary(self):
        pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    p = Product("Python", 59.8)
    # __repr__
    assert "Product" in repr(p)
    assert "Python" in repr(p)
    # __str__
    assert "Python" in str(p)
    assert "59.8" in str(p)
    assert "元" in str(p)

    # Order 组合
    addr = Address("北京")
    order = Order(p, addr)
    text = order.summary()
    assert "Python" in text
    assert "北京" in text
    print("✅ 所有测试通过")
    print(f"repr: {repr(p)}")
    print(f"str:  {str(p)}")
