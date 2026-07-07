"""
[难度: ⭐⭐⭐]
[所属知识点: 继承 + 方法重写]
[预计完成时间: 15 分钟]

题目描述:
定义一个基类 Employee,包含 name、salary 属性和 work() 方法;
定义子类 Manager,重写 work() 返回 "我在管理团队";
定义子类 Developer,重写 work() 返回 "我在写代码"。

示例:
    >>> e = Employee("张三", 5000)
    >>> e.work()
    '我在工作'
    >>> m = Manager("李四", 15000)
    >>> m.work()
    '我在管理团队'
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 基类 Employee
    e1 = Employee("张三", 5000)
    print(e1.work())

    # 测试 2: Manager 子类
    m1 = Manager("李四", 15000)
    print(m1.work())

    # 测试 3: Developer 子类
    d1 = Developer("王五", 12000)
    print(d1.work())

    # 测试 4: 多态调用
    staff = [Employee("赵六", 6000), Manager("孙七", 20000)]
    for person in staff:
        print(f"{person.name}: {person.work()}")
