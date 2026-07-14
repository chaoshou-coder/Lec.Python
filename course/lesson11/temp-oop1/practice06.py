"""
[难度: ⭐⭐⭐⭐]
[所属知识点: @property setter 拒绝非法值]
[预计完成时间: 15 分钟]

题目描述:
    定义一个 `BankAccount` 类,表示银行账户。
    - 构造函数接收 `owner`(户名)和 `balance`(初始余额)
    - `balance` 用 `@property` 保护,**不允许为负数**
    - setter 收到负数时拒绝修改,并打印 "余额不能为负,已忽略"
    - 定义一个方法 `can_withdraw(amount)`,返回该金额能否取出

示例:
    >>> acc = BankAccount("张三", 1000)
    >>> print(acc.balance)
    1000
    >>> acc.balance = -500
    余额不能为负,已忽略
    >>> print(acc.balance)
    1000  (没变)
    >>> print(acc.can_withdraw(800))
    True
    >>> print(acc.can_withdraw(1200))
    False
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance  # 走 setter 校验

    # 请补全 @property / @balance.setter / can_withdraw
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 正常创建
    acc = BankAccount("张三", 1000)
    assert acc.balance == 1000
    assert acc.owner == "张三"

    # 测试 2: setter 拒绝负数
    acc.balance = -500
    assert acc.balance == 1000, "setter 应拒绝负数"

    # 测试 3: 合法值可以通过
    acc.balance = 2000
    assert acc.balance == 2000

    # 测试 4: can_withdraw 超额判断
    assert acc.can_withdraw(500) is True
    assert acc.can_withdraw(2000) is True  # 恰好等于也能
    assert acc.can_withdraw(2001) is False

    # 测试 5: 0 也是合法余额
    acc.balance = 0
    assert acc.balance == 0
    print("✅ 所有测试通过")
