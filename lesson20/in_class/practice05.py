"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 继承 + 方法重写 + 多态]
[预计完成时间: 20 分钟]

题目描述:
定义一个基类 Shape,包含 area() 方法(返回 0);
定义子类 Circle(半径属性),重写 area() 返回圆面积;
定义子类 Rectangle(宽高属性),重写 area() 返回矩形面积。
圆周率使用 3.14。

示例:
    >>> c = Circle(5)
    >>> c.area()
    78.5
    >>> r = Rectangle(4, 6)
    >>> r.area()
    24
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: Circle 面积
    c1 = Circle(5)
    print(f"圆面积: {c1.area()}")

    # 测试 2: Rectangle 面积
    r1 = Rectangle(4, 6)
    print(f"矩形面积: {r1.area()}")

    # 测试 3: 基类 Shape
    s1 = Shape()
    print(f"Shape 面积: {s1.area()}")

    # 测试 4: 半径为 0
    c2 = Circle(0)
    print(f"半径为 0 的圆面积: {c2.area()}")
