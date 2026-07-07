"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 私有属性 + 方法 + raise]
[预计完成时间: 20 分钟]

题目描述:
定义一个类 BankAccount,包含私有属性 _balance,
定义 deposit(amount) 方法用于存款(余额增加),
定义 withdraw(amount) 方法用于取款(余额减少),
取款时如果余额不足,抛出 ValueError("余额不足")。

示例:
    >>> acc = BankAccount(100)
    >>> acc.deposit(50)
    >>> acc._balance
    150
    >>> acc.withdraw(200)
    ValueError: 余额不足
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常存取款
    acc1 = BankAccount(100)
    acc1.deposit(50)
    acc1.withdraw(30)
    print(f"余额: {acc1._balance}")

    # 测试 2: 余额不足抛出异常
    acc2 = BankAccount(50)
    try:
        acc2.withdraw(100)
    except ValueError as e:
        print(f"异常: {e}")

    # 测试 3: 刚好取完全部余额
    acc3 = BankAccount(80)
    acc3.withdraw(80)
    print(f"余额: {acc3._balance}")
