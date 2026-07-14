"""
[难度: ⭐⭐⭐]
[所属知识点: @property getter/setter(写保护)]
[预计完成时间: 15 分钟]

题目描述:
    给 Dog 类加 age 的 @property 保护:读取返回年龄,
    写入时校验非负,负数抛 ValueError。体会"属性写保护"。

示例:
    >>> dog = Dog("旺财", 3)
    >>> dog.age = -1
    ValueError: 年龄不能为负数
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age  # 走 setter 校验

    @property
    def age(self):
        return self._age  # 真实值存在 _age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("年龄不能为负数")
        self._age = value

dog = Dog("旺财", 3)
print(f"{dog.name} 今年 {dog.age} 岁")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常读取
    d = Dog("旺财", 3)
    print(f"测试1: {d.age}")  # 3

    # 测试 2: 正常修改
    d.age = 5
    print(f"测试2: {d.age}")  # 5

    # 测试 3: 负数抛异常
    try:
        d.age = -1
        print("测试3: 未抛异常(错)")
    except ValueError as e:
        print(f"测试3: {e}")  # 年龄不能为负数

    # 测试 4: 构造时负数也抛异常
    try:
        Dog("小黑", -2)
        print("测试4: 未抛异常(错)")
    except ValueError as e:
        print(f"测试4: {e}")  # 年龄不能为负数
