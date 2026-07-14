"""
[难度: ⭐⭐⭐]
[所属知识点: 类属性 vs 实例属性]
[预计完成时间: 13 分钟]

题目描述:
    定义一个 `Product` 类,所有商品共享同一个增值税率 `tax_rate`。
    - 类属性 `tax_rate = 0.13`(13%)
    - 每个商品有独立的 `name` 和 `price`(实例属性)
    - 定义一个实例方法 `price_with_tax()`,返回含税价格

示例:
    >>> p1 = Product("Python 入门", 100)
    >>> p2 = Product("算法图解", 200)
    >>> print(p1.price_with_tax())
    113.0
    >>> Product.tax_rate = 0.09  # 税率改为 9%
    >>> print(p1.price_with_tax())
    109.0  (所有商品一起变)
    >>> print(p2.price_with_tax())
    218.0
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 初始税率 13%
    Product.tax_rate = 0.13
    p1 = Product("Python 入门", 100)
    p2 = Product("算法图解", 200)
    assert p1.price_with_tax() == 113.0
    assert p2.price_with_tax() == 226.0

    # 测试 2: 改类属性影响所有实例
    original_p1 = p1.price_with_tax()
    Product.tax_rate = 0.09
    assert p1.price_with_tax() == 109.0
    assert p2.price_with_tax() == 218.0

    # 测试 3: 通过实例赋值会创建实例属性(遮盖类属性)
    p1.tax_rate = 0.5  # 给 p1 加了实例属性
    assert p1.tax_rate == 0.5  # p1 被遮盖
    assert Product.tax_rate == 0.09  # 类属性没变
    assert p2.price_with_tax() == 218.0  # p2 仍走类属性
    print("✅ 所有测试通过")
