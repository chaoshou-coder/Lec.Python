"""
[难度: ⭐⭐⭐]
[所属知识点: 类 + 方法]
[预计完成时间: 15 分钟]

题目描述:
定义一个类 Rectangle,包含 width 和 height 属性,
定义 area() 方法计算面积,定义 perimeter() 方法计算周长。

示例:
    >>> r = Rectangle(5, 3)
    >>> r.area()
    15
    >>> r.perimeter()
    16
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 普通矩形
    r1 = Rectangle(5, 3)
    print(f"面积: {r1.area()}")
    print(f"周长: {r1.perimeter()}")

    # 测试 2: 正方形
    r2 = Rectangle(4, 4)
    print(f"面积: {r2.area()}")
    print(f"周长: {r2.perimeter()}")

    # 测试 3: 宽或高为 0
    r3 = Rectangle(0, 10)
    print(f"面积: {r3.area()}")
    print(f"周长: {r3.perimeter()}")
