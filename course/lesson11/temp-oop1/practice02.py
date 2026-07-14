"""
[难度: ⭐⭐]
[所属知识点: 实例方法]
[预计完成时间: 10 分钟]

题目描述:
    在前一题 `Product` 类基础上,新增实例方法 `info()`,
    返回格式为 "商品名:商品名,价格:XX.XX 元" 的字符串。
    创建两个商品,分别调用 info() 并打印。

示例:
    >>> p = Product("Python 入门", 59.8)
    >>> print(p.info())
    商品名:Python 入门,价格:59.80 元
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # 请在下方新增 info() 方法
    pass

# p1 = Product("Python 入门", 59.8)
# print(p1.info())
# p2 = Product("算法图解", 45.0)
# print(p2.info())

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    p1 = Product("Python 入门", 59.8)
    # 测试 1: info 包含商品名与价格
    assert "Python 入门" in p1.info()
    assert "59.80" in p1.info()

    # 测试 2: info 返回字符串
    assert isinstance(p1.info(), str)

    # 测试 3: 边界:整数价格也能正确格式化
    p2 = Product("测试商品", 100)
    assert "100.00" in p2.info()
    print("✅ 所有测试通过")
