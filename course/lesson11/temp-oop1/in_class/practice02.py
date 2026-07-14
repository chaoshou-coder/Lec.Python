"""
[难度: ⭐⭐]
[所属知识点: 实例方法]
[预计完成时间: 10 分钟]

题目描述:
    定义 `Product` 类(属性 name/price),
    新增实例方法 `info()`,
    返回格式为 "商品名:XXX,价格:XX.XX 元" 的字符串。
    创建商品,调用 info() 并打印。

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

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    p = Product("Python 入门", 59.8)
    assert "Python 入门" in p.info()
    assert "59.80" in p.info()
    assert isinstance(p.info(), str)
    p2 = Product("测试", 100)
    assert "100.00" in p2.info()
    print("✅ 所有测试通过")
