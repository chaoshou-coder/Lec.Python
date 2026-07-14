"""
[难度: ⭐⭐⭐⭐]
[所属知识点: Order 类原型(L1 综合)]
[预计完成时间: 25 分钟,选做]

题目描述:
    电商订单系统 v2 起步阶段:定义 `Order` 类表示订单。
    - 构造函数接收 `order_id`(订单号)和 `customer`(客户名)
    - 内部用列表 `items` 存储多个商品名(每个商品是一个字符串)
    - 提供方法 `add_item(product_name)`:添加商品
    - 提供方法 `remove_item(product_name)`:移除商品(不存在则忽略)
    - 提供方法 `item_count()`:返回商品数量
    - `__str__` 返回 "订单[XXX] 共 N 件,客户:XXX"

    这是后续 L2-L4 的基础原型,先在 L1 用简单字符串表示商品。

示例:
    >>> order = Order("ORD-001", "张三")
    >>> order.add_item("Python 入门")
    >>> order.add_item("算法图解")
    >>> order.add_item("Python 入门")  # 同款可以重复
    >>> print(order.item_count())
    3
    >>> print(order)
    订单[ORD-001] 共 3 件,客户:张三
    >>> order.remove_item("算法图解")
    >>> print(order.item_count())
    2
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.items = []

    # 请补全 add_item / remove_item / item_count / __str__
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    order = Order("ORD-001", "张三")
    # 测试 1: 添加商品
    order.add_item("Python 入门")
    order.add_item("算法图解")
    assert order.item_count() == 2

    # 测试 2: 同款可以重复
    order.add_item("Python 入门")
    assert order.item_count() == 3

    # 测试 3: 移除商品
    order.remove_item("算法图解")
    assert order.item_count() == 2

    # 测试 4: 移除不存在的商品不报错
    order.remove_item("不存在的商品")
    assert order.item_count() == 2

    # 测试 5: __str__ 友好
    s = str(order)
    assert "ORD-001" in s
    assert "2 件" in s or "2件" in s
    assert "张三" in s
    print("✅ 所有测试通过")
    print(f"订单信息: {order}")
