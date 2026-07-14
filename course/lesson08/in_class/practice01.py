"""
[难度: ⭐]
[所属知识点: class 定义类 + 实例化]
[预计完成时间: 5 分钟]

题目描述:
    定义一个空类 Dog(类名大驼峰),然后实例化一只狗打印类型。
    体会"类是蓝图,实例是具体的对象"。

示例:
    >>> dog = Dog()
    >>> print(type(dog))
    <class '__main__.Dog'>
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
# 定义空类 Dog(类名大驼峰)
class Dog:
    pass

# 实例化一只狗
dog = Dog()
print(type(dog))

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 实例类型是 Dog
    d = Dog()
    print(f"测试1: {type(d)}")  # <class '__main__.Dog'>

    # 测试 2: 两个实例是不同的对象
    d1 = Dog()
    d2 = Dog()
    print(f"测试2: {d1 is d2}")  # False

    # 测试 3: isinstance 判断
    print(f"测试3: {isinstance(d1, Dog)}")  # True
