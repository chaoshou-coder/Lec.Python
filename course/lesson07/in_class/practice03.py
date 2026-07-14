"""
[难度: ⭐⭐⭐]
[所属知识点: abc.ABC + abstractmethod 基础]
[预计完成时间: 13 分钟]

题目描述:
    定义抽象类 `Payment`,包含抽象方法 `execute(amount)`:
    1. 尝试直接实例化 `Payment` → 观察 TypeError
    2. 尝试创建空子类 `MyPay` 不实现任何方法,
       同样尝试实例化 → 观察 TypeError
    3. 完整实现 `Alipay(Payment)`,实现 execute 方法

    体会:abc 把错误提前到**实例化阶段**,
    而不是等到运行中调用方法时。

示例:
    >>> p = Payment()
    TypeError: Can't instantiate abstract class Payment
    >>> a = Alipay()
    >>> a.execute(100)
    支付宝支付 100 元
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import abc

class Payment(abc.ABC):
    # 请定义 execute 抽象方法
    pass

# 尝试实例化抽象类
# try:
#     Payment()
# except TypeError as e:
#     print(f"报错: {e}")

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    import io, sys

    # 测试 1: Payment 不能实例化
    try:
        Payment()
        assert False, "Payment 应该不能实例化"
    except TypeError:
        pass  # 预期

    # 测试 2: 空子类也不能实例化
    class BadPay(Payment):
        pass

    try:
        BadPay()
        assert False, "空子类应该不能实例化"
    except TypeError:
        pass  # 预期

    # 测试 3: 完整实现的子类可以
    a = Alipay()
    assert a.execute(100)  # 返回 True 表示成功
    print("✅ 所有测试通过")
