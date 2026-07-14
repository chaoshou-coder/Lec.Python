"""
[难度: ⭐⭐⭐]
[所属知识点: 方法重写 override + super().方法()]
[预计完成时间: 12 分钟]

题目描述:
    定义基类 `Product`,方法 `shipping_cost()` 返回 0。
    定义子类 `PhysicalProduct(Product)`,新增属性 `weight`,
    **重写** `shipping_cost()` 返回 `weight * 8`。
    定义子类 `DigitalProduct(Product)`,**不重写**,
    基类的 0 直接继承。

示例:
    >>> p = PhysicalProduct("纸质书", 50, 10)
    >>> d = DigitalProduct("电子书", 30)
    >>> print(p.shipping_cost())
    80
    >>> print(d.shipping_cost())
    0
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Product:
    def shipping_cost(self):
        return 0

class PhysicalProduct(Product):
    pass

# p = PhysicalProduct("纸质书", 50, 10)
# print(p.shipping_cost())

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    p = PhysicalProduct("纸质书", 50, 10)
    d = DigitalProduct("电子书", 30)
    assert p.shipping_cost() == 80
    assert d.shipping_cost() == 0
    # 边界:重量为 0
    p0 = PhysicalProduct("小册子", 20, 0)
    assert p0.shipping_cost() == 0
    print("✅ 所有测试通过")
