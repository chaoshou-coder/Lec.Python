"""
[难度: ⭐⭐⭐⭐]
[所属知识点: Product 继承体系(Physical/Digital)]
[预计完成时间: 25 分钟,选做]

题目描述:
    电商系统的产品继承体系。

    - 基类 `Product(name, price)`
      - `@property` 保护 price(不能为负)
      - 方法 `shipping_cost()` 返回 0
      - `__str__` 返回 "商品[XXX] :XX 元"
    - 子类 `PhysicalProduct(Product)`,新增 `weight`
      - 重写 `shipping_cost()` = weight * 8
    - 子类 `DigitalProduct(Product)`,新增 `file_size`
      - 不重写 `shipping_cost()`,继承基类的 0
      - 免费送货

    验证:两个子类的运费差异,
    以及基类的 @property 保护仍然生效。

示例:
    >>> PhysicalProduct("纸质书", 50, 10).shipping_cost()
    80
    >>> DigitalProduct("电子书", 30, "5MB").shipping_cost()
    0
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Product:
    pass

# p = PhysicalProduct("纸质书", 50, 10)
# d = DigitalProduct("电子书", 30, "5MB")
# print(p.shipping_cost())
# print(d.shipping_cost())

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    p = PhysicalProduct("纸质书", 50, 10)
    assert p.shipping_cost() == 80
    assert p.name == "纸质书"

    d = DigitalProduct("电子书", 30, "5MB")
    assert d.shipping_cost() == 0
    assert d.file_size == "5MB"

    # __str__ 友好
    assert "纸质书" in str(p)
    assert "电子书" in str(d)

    # 基类 @property 仍生效
    try:
        bad = Product("错误", -10)
        assert False, "应该拒绝负数"
    except ValueError:
        pass

    print("✅ 所有测试通过")
