"""
[难度: ⭐⭐⭐⭐]
[所属知识点: __eq__ 同款判定(购物车去重)]
[预计完成时间: 15 分钟]

题目描述:
    定义 `Product` 类,包含 `name`。
    实现 `__eq__`:两个 Product 的 `name` 相同则同款。
    实现 `__hash__`:使商品能放入 `set`(用于去重)。

    定义函数 `unique_count(products)`:
    用 set 去重后返回商品数。

示例:
    >>> p1 = Product("Python")
    >>> p2 = Product("Python")  # 同款
    >>> p3 = Product("算法")
    >>> print(p1 == p2)      # True
    >>> print(p1 == p3)      # False
    >>> unique_count([p1, p2, p3])
    2
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Product:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        pass

    def __hash__(self):
        pass

# def unique_count(products): ...

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    p1 = Product("Python")
    p2 = Product("Python")  # 同款
    p3 = Product("算法")

    # __eq__
    assert p1 == p2
    assert not (p1 == p3)

    # set 去重
    s = {p1, p2, p3}
    assert len(s) == 2

    # unique_count
    assert unique_count([p1, p2, p3, Product("算法")]) == 2

    # hash
    assert hash(p1) == hash(p2)
    print("✅ 所有测试通过")
