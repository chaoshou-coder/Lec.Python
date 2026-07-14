"""
[难度: ⭐⭐⭐⭐⭐]
[所属知识点: 对比题 — 继承 vs 组合同需求实现]
[预计完成时间: 35 分钟,选做]

题目描述:
    同一需求(动物园喂食系统)分别用两种方式实现。

    需求:
    - 多种动物(Lion/Elephant/Parrot),每种有 `eat()` 方法
    - Zoo 类能 `feed_all()`,调用每只动物的 eat()

    方式 A(继承):
    - Animal 基类 + 子类重写 eat()
    - Zoo 持有 Animal 列表

    方式 B(组合):
    - 每种动物独立类,不继承
    - Zoo 持有动物列表(鸭子类型)

    分别实现后,回答:
    1. 哪种方式新增动物更容易?
    2. 哪种方式能强制所有动物都实现 eat()?
    3. 如果要加"必须实现 eat()"的约束,方式 B 怎么改?

示例:
    # 方式 A
    zoo_a = Zoo([Lion(), Elephant(), Parrot()])
    zoo_a.feed_all()
    狮子吃肉
    大象吃草
    鹦鹉吃瓜子

    # 方式 B(结果相同)
    zoo_b = Zoo([Lion(), Elephant(), Parrot()])
    zoo_b.feed_all()
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

# ===== 方式 A:继承 =====
class Animal:
    def eat(self):
        pass

class Lion(Animal):
    pass

# class Elephant(Animal): ...
# class Parrot(Animal): ...

class Zoo:
    def __init__(self, animals):
        self.animals = animals

    def feed_all(self):
        for a in self.animals:
            print(a.eat())

# ===== 方式 B:组合 =====
class Lion2:
    pass

# class Elephant2: ...
# class Parrot2: ...

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 方式 A
    zoo_a = Zoo([Lion(), Elephant(), Parrot()])
    sounds_a = []
    for a in zoo_a.animals:
        sounds_a.append(a.eat())

    # 方式 B
    zoo_b = Zoo([Lion2(), Elephant2(), Parrot2()])
    sounds_b = []
    for a in zoo_b.animals:
        sounds_b.append(a.eat())

    # 结果相同
    assert sounds_a == sounds_b

    # 方式 A 有继承链
    assert isinstance(Lion(), Animal)
    # 方式 B 没有
    assert not isinstance(Lion2(), Animal)
    print("✅ 所有测试通过")
    print(f"方式 A: {sounds_a}")
    print(f"方式 B: {sounds_b}")
