"""
[难度: ⭐⭐⭐]
[所属知识点: __add__ 购物车合并]
[预计完成时间: 12 分钟]

题目描述:
    定义 `ShoppingCart` 类,表示购物车。
    - 构造函数接收 `items`(商品列表,
      每个元素是商品名 字符串)
    - 实现 `__add__(self, other)`:
      合并两辆购物车,**返回新对象**
    - 验证原购物车不被修改

示例:
    >>> cart1 = ShoppingCart(["Python 入门", "算法"])
    >>> cart2 = ShoppingCart(["英语"])
    >>> cart3 = cart1 + cart2
    >>> print(len(cart3.items))
    3
    >>> print(len(cart1.items))
    2  (cart1 没变!)
    >>> print(len(cart2.items))
    1  (cart2 没变!)
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class ShoppingCart:
    def __init__(self, items=None):
        self.items = items or []

    def __add__(self, other):
        pass

# cart1 = ShoppingCart(["A", "B"])
# cart2 = ShoppingCart(["C"])
# cart3 = cart1 + cart2
# print(len(cart3.items))

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    cart1 = ShoppingCart(["Python 入门", "算法"])
    cart2 = ShoppingCart(["英语"])
    cart3 = cart1 + cart2
    assert len(cart3.items) == 3
    assert len(cart1.items) == 2  # 未修改
    assert len(cart2.items) == 1  # 未修改

    # 边界:其中一辆车为空
    cart_empty = ShoppingCart([])
    cart4 = cart1 + cart_empty
    assert len(cart4.items) == 2
    print("✅ 所有测试通过")
