"""
[难度: ⭐⭐⭐]
[所属知识点: super().__init__() 扩展父类属性]
[预计完成时间: 12 分钟]

题目描述:
    定义基类 `Product`,属性 `name` 和 `price`。
    定义子类 `Book(Product)`,新增属性 `author`(作者)。
    子类用 `super().__init__()` 继承基类属性,
    再用 `self.author` 扩展自己的属性。

示例:
    >>> b = Book("Python 入门", 59.8, "张三")
    >>> print(b.name, b.price, b.author)
    Python 入门 59.8 张三
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Book(Product):
    pass

# b = Book("...", ...)
# print(b.name, b.price, b.author)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    b = Book("Python 入门", 59.8, "张三")
    assert b.name == "Python 入门"
    assert b.price == 59.8
    assert b.author == "张三"
    # 验证各实例独立
    b2 = Book("算法", 45, "李四")
    assert b.author == "张三"  # b 未受影响
    print("✅ 所有测试通过")
