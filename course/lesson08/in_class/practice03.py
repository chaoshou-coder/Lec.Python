"""
[难度: ⭐⭐]
[所属知识点: 实例方法(def 方法,第一个参数写 self)]
[预计完成时间: 10 分钟]

题目描述:
    给 Dog 类加实例方法 bark(self),返回叫声字符串。
    实例化后调用方法,体会"自己的数据自己处理"。

示例:
    >>> dog = Dog("旺财", 3)
    >>> print(dog.bark())
    旺财说: 汪汪汪!
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法:第一个参数写 self
    def bark(self):
        return f"{self.name}说: 汪汪汪!"

dog = Dog("旺财", 3)
print(dog.bark())

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常调用
    d1 = Dog("旺财", 3)
    print(f"测试1: {d1.bark()}")  # 旺财说: 汪汪汪!

    # 测试 2: 不同实例返回不同
    d2 = Dog("小黑", 5)
    print(f"测试2: {d2.bark()}")  # 小黑说: 汪汪汪!

    # 测试 3: 返回值是字符串
    result = d1.bark()
    print(f"测试3: {type(result)}")  # <class 'str'>
