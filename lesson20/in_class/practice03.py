"""
[难度: ⭐⭐⭐]
[所属知识点: 多态]
[预计完成时间: 15 分钟]

题目描述:
定义一个函数 let_speak(animal),调用 animal.speak() 并打印结果。
传入不同类型的 Animal 子类对象,观察同样的调用产生不同的行为。

示例:
    >>> let_speak(Dog("旺财"))
    汪汪
    >>> let_speak(Cat("小花"))
    喵喵
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 传入 Dog 对象
    let_speak(Dog("旺财"))

    # 测试 2: 传入 Cat 对象
    let_speak(Cat("小花"))

    # 测试 3: 传入基类 Animal 对象
    let_speak(Animal("某动物"))

    # 测试 4: 循环遍历不同动物
    animals = [Dog("大黄"), Cat("咪咪"), Animal("未知")]
    for a in animals:
        let_speak(a)
