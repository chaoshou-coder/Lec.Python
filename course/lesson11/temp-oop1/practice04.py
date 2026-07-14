"""
[难度: ⭐⭐⭐]
[所属知识点: __str__ 魔术方法]
[预计完成时间: 12 分钟]

题目描述:
    在前一题 `Product` 类基础上,新增 `__str__` 方法,
    使得 `print(product)` 直接输出商品信息,
    格式为 "商品[XXX] 价格:XX.XX 元"。

    对比不加 `__str__` 时的输出:
    >>> print(product)
    <__main__.Product object at 0x7f...>  ← 内存地址,无意义

    加了之后:
    >>> print(product)
    商品[Python 入门] 价格:59.80 元
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # 请补全 __str__ 方法
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    p = Product("Python 入门", 59.8)
    result = str(p)
    # 测试 1: 包含商品名和价格
    assert "Python 入门" in result
    assert "59.80" in result

    # 测试 2: 返回字符串
    assert isinstance(result, str)

    # 测试 3: 不含内存地址(关键)
    assert "0x" not in result
    assert "__main__" not in result
    print("✅ 所有测试通过")
    print(f"实际输出: {result}")
