"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 类 + 列表 + 方法]
[预计完成时间: 20 分钟]

题目描述:
定义一个类 ShoppingCart,包含 items 列表(元素为 (name, price) 元组),
定义 add_item(name, price) 添加商品,
定义 remove_item(name) 移除第一个同名商品,
定义 total() 计算购物车总价。

示例:
    >>> cart = ShoppingCart()
    >>> cart.add_item("苹果", 5.5)
    >>> cart.add_item("香蕉", 3.0)
    >>> cart.total()
    8.5
    >>> cart.remove_item("苹果")
    >>> cart.total()
    3.0
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常添加商品并计算总价
    cart1 = ShoppingCart()
    cart1.add_item("苹果", 5.5)
    cart1.add_item("香蕉", 3.0)
    print(f"总价: {cart1.total()}")

    # 测试 2: 移除商品
    cart1.remove_item("苹果")
    print(f"移除后总价: {cart1.total()}")

    # 测试 3: 移除不存在的商品
    cart1.remove_item("不存在的商品")

    # 测试 4: 空购物车
    cart2 = ShoppingCart()
    print(f"空购物车总价: {cart2.total()}")
