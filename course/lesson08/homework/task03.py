"""
[难度: ⭐⭐⭐⭐]
[所属知识点: class / __init__ / @property]
[预计完成时间: 20 分钟]

题目描述:
  请定义一个 Rectangle 类,表示矩形。
    - __init__ 接收 width 和 height 两个参数
    - 使用 @property 定义 area 属性(面积)
    - 使用 @property 定义 perimeter 属性(周长)
    - 实现 __str__ 方法,返回格式:
      "矩形(width=X,height=Y)"
  编写完后创建实例并打印其面积和周长。

示例:
    >>> r = Rectangle(3, 4)
    >>> print(r)
    矩形(width=3,height=4)
    >>> r.area
    12
    >>> r.perimeter
    14
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
    r1 = Rectangle(3, 4)
    print(r1)
    assert str(r1) == "矩形(width=3,height=4)"
    assert r1.area == 12
    assert r1.perimeter == 14

    # 测试 2: 正方形
    r2 = Rectangle(5, 5)
    print(r2)
    assert str(r2) == "矩形(width=5,height=5)"
    assert r2.area == 25
    assert r2.perimeter == 20

    # 测试 3: 宽或高为 1
    r3 = Rectangle(1, 10)
    print(r3)
    assert str(r3) == "矩形(width=1,height=10)"
    assert r3.area == 10
    assert r3.perimeter == 22

    print("所有测试通过!")
