"""
[难度: ⭐⭐]
[所属知识点: class 定义类 / __init__ 构造函数]
[预计完成时间: 8 分钟]

题目描述:
    定义一个 `Product` 类,表示电商商品。
    - 构造函数接收 `name`(商品名)和 `price`(价格)
    - 创建两个商品实例,分别打印它们的名字和价格。

示例:
    >>> p1 = Product("Python 入门", 59.8)
    >>> p2 = Product("算法图解", 45.0)
    >>> print(p1.name, p1.price)
    Python 入门 59.8
    >>> print(p2.name, p2.price)
    算法图解 45.0
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    p1 = Product("Python 入门", 59.8)
    p2 = Product("算法图解", 45.0)
    assert p1.name == "Python 入门"
    assert p1.price == 59.8
    assert p2.name == "算法图解"
    p1.name = "改名"
    assert p2.name == "算法图解"
    print("✅ 所有测试通过")
