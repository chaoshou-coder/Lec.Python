"""
[难度: ⭐⭐⭐⭐⭐]
[所属知识点: 完整 Payment 系统(L3 综合)]
[预计完成时间: 30 分钟,选做]

题目描述:
    **给定的 checkout 函数**(下方,不可修改核心逻辑)。

    要求:
    1. 补全 Alipay / WeChatPay / ApplePay 三个子类
    2. 新增一个 `CreditPay`(信用卡),不需改 checkout
    3. 单元测试验证 4 种支付方式都能工作
    4. **约束**:checkout 内禁止 if/elif/isinstance/type

    这是 L3 的最终检验 —— 消费者函数即门控。

示例:
    >>> for p in [Alipay(), WeChatPay(), ApplePay()]:
    ...     checkout(99.0, p)
    支付宝支付 99.0 元
    微信支付 99.0 元
    Apple Pay 99.0 元
    True
"""

# ======================
# 学员代码区(下方 checkout 不可修改)
# ======================
import abc

class Payment(abc.ABC):
    @abc.abstractmethod
    def execute(self, amount: float) -> bool:
        ...

def checkout(cart_total, payment):
    """核心函数,不可修改核心逻辑"""
    if cart_total <= 0:
        print("购物车为空")
        return False
    return payment.execute(cart_total)

# 请补全三个子类 + 新增 CreditPay:
class Alipay(Payment):
    pass

# class WeChatPay(Payment): ...
# class ApplePay(Payment): ...
# class CreditPay(Payment): ...

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    payments = [Alipay(), WeChatPay(), ApplePay(), CreditPay()]
    for p in payments:
        result = checkout(99.0, p)
        assert result is True, f"{type(p).__name__} 应返回 True"

    # 漏写 execute 报错
    try:
        class BadPay(Payment): pass
        BadPay()
        assert False
    except TypeError:
        pass

    # 0 元购物车
    assert checkout(0, Alipay()) is False
    print("✅ 所有测试通过")
