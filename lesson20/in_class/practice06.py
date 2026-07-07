"""
[难度: ⭐⭐⭐⭐⭐]
[所属知识点: 多态 + 循环]
[预计完成时间: 25 分钟]

题目描述:
定义一个函数 total_area(shapes),接收一个 Shape 及其子类对象的列表,
计算所有图形的面积之和,体验多态的魅力。

示例:
    >>> shapes = [Circle(5), Rectangle(4, 6), Circle(3)]
    >>> total_area(shapes)
    106.76
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 混合图形
    shapes1 = [Circle(5), Rectangle(4, 6), Circle(3)]
    print(f"总面积: {total_area(shapes1)}")

    # 测试 2: 只有圆
    shapes2 = [Circle(1), Circle(2), Circle(3)]
    print(f"圆的总面积: {total_area(shapes2)}")

    # 测试 3: 空列表
    shapes3 = []
    print(f"空列表总面积: {total_area(shapes3)}")

    # 测试 4: 单个图形
    shapes4 = [Rectangle(10, 10)]
    print(f"单个矩形面积: {total_area(shapes4)}")
