"""
[难度: ⭐⭐⭐⭐]
[所属知识点: BankAccount 综合(@property + 存取款 + __str__)]
[预计完成时间: 20 分钟,选做]

题目描述:
    扩展 `BankAccount` 类,实现以下完整功能:
    1. `@property` 保护 balance(不允许为负)
    2. 实例方法 `deposit(amount)`:存款,返回新余额
       - 如果 amount 为负,拒绝并打印 "存款金额不能为负"
    3. 实例方法 `withdraw(amount)`:取款,返回是否成功(bool)
       - 超额拒绝,打印 "余额不足,取款失败"
    4. `__str__` 返回 "BankAccount(owner=XXX, balance=XXX)"

示例:
    >>> acc = BankAccount("张三", 1000)
    >>> acc.deposit(500)
    1500
    >>> print(acc)
    BankAccount(owner=张三, balance=1500)
    >>> acc.withdraw(2000)
    余额不足,取款失败
    False
    >>> acc.withdraw(300)
    True
    >>> print(acc.balance)
    1200
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance  # 走 setter 校验

    # 请补全 @property / setter / deposit / withdraw / __str__
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    acc = BankAccount("张三", 1000)
    # 测试 1: 存款
    assert acc.deposit(500) == 1500
    assert acc.balance == 1500

    # 测试 2: 非法存款
    result = acc.deposit(-100)
    assert acc.balance == 1500, "负数存款应被拒绝"

    # 测试 3: 取款
    assert acc.withdraw(300) is True
    assert acc.balance == 1200

    # 测试 4: 超额取款
    assert acc.withdraw(2000) is False
    assert acc.balance == 1200, "超额取款不应扣款"

    # 测试 5: __str__ 友好
    s = str(acc)
    assert "张三" in s
    assert "1200" in s
    assert "0x" not in s  # 不含内存地址
    print("✅ 所有测试通过")
    print(f"账户信息: {acc}")
