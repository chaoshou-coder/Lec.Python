"""
[难度: ⭐⭐⭐]
[所属知识点: 类属性 vs 实例属性]
[预计完成时间: 15 分钟]

题目描述:
    给 Dog 类加类属性 species = "犬科",实例属性 name。
    体会:类属性所有实例共享,实例属性各自独立。

示例:
    >>> d1 = Dog("旺财")
    >>> d2 = Dog("小黑")
    >>> print(d1.species, d2.species)
    犬科 犬科
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Dog:
    # 类属性:所有实例共享
    species = "犬科"

    def __init__(self, name):
        # 实例属性:各自独立
        self.name = name

d1 = Dog("旺财")
d2 = Dog("小黑")
print(f"{d1.name} 属于 {d1.species}")
print(f"{d2.name} 属于 {d2.species}")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    d1 = Dog("旺财")
    d2 = Dog("小黑")

    # 测试 1: 类属性共享
    print(f"测试1: {d1.species} {d2.species}")  # 犬科 犬科

    # 测试 2: 改类属性影响所有实例
    Dog.species = "Canidae"
    print(f"测试2: {d1.species} {d2.species}")  # Canidae Canidae

    # 测试 3: 实例属性独立
    d1.name = "大黄"
    print(f"测试3: {d1.name} {d2.name}")  # 大黄 小黑

    # 测试 4: 恢复类属性
    Dog.species = "犬科"
    print(f"测试4: {Dog.species}")  # 犬科
