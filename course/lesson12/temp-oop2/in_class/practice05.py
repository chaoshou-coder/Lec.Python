"""
[难度: ⭐⭐⭐⭐]
[所属知识点: Employee + Manager + Sales 多级继承]
[预计完成时间: 15 分钟]

题目描述:
    设计员工薪资系统:
    - 基类 `Employee(name, base)`,方法 `pay()` 返回 base
    - 子类 `Manager(name, base, bonus)`,
      重写 `pay()` = base + bonus
    - 子类 `Sales(name, base, commission)`,
      重写 `pay()` = base + commission
    - 子类必须用 `super().__init__()` 继承基类属性

    创建各一个实例,验证薪资计算正确。

示例:
    >>> Employee("张三", 5000).pay()
    5000
    >>> Manager("李四", 8000, 3000).pay()
    11000
    >>> Sales("王五", 5000, 2000).pay()
    7000
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class Employee:
    def __init__(self, name, base):
        self.name = name
        self.base = base

    def pay(self):
        return self.base

class Manager(Employee):
    pass

# m = Manager("李四", 8000, 3000)
# print(m.pay())

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    e = Employee("张三", 5000)
    assert e.pay() == 5000
    m = Manager("李四", 8000, 3000)
    assert m.pay() == 11000
    assert m.name == "李四"  # 继承自基类
    s = Sales("王五", 5000, 2000)
    assert s.pay() == 7000
    # 独立验证
    assert e.pay() == 5000  # Employee 不影响 Manager
    print("✅ 所有测试通过")
