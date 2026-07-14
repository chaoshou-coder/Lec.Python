# Week03 中型项目 · 控制台电商订单系统 v2(OOP L1-L4 + JSON + 异常)

> 状态:v2(2026-07-14) — 从图书管理升级为电商订单系统,
> 新增 L4 组合/运算符重载/对象协议验收点。

## 涉及知识点

Day01-Day08 全部,重点是 Day05-08 的 OOP L1-L4。

## 设计叙事

你接手了一个"散落在 dict 里"的订单系统 v1。
v1 用字典存商品/订单/支付,逻辑全在 if-elif 里,加一种支付方式要改核心函数。
你的任务:用 OOP L1-L4 把 v1 重构成 v2,让系统**可扩展、可合并、像内建类型一样自然**。

## 验收点

### 基础(必修,来自 v1 验收)

- [ ] **三个核心类**:`Product` / `Order` / `Payment`(及其子类)
- [ ] 启动时加载 `./data/products.json` + `./data/orders.json`,失败则创建空库
- [ ] 每项操作都有 `try/except`,终端提示友好
- [ ] 能导出 `./data/report.csv`(订单排行/销售额统计)
- [ ] 单元测试用例(教师事先写好 test 脚本,学员跑通即给分)
- [ ] 作品 README(含类关系图) + 3 分钟 Demo 录像

### L1 封装(必修)

- [ ] `Product` 类用 `@property` 保护价格(非负)和库存(非负)
- [ ] `Product.__str__` 打印友好信息(不再是内存地址)
- [ ] 类属性 `Product.tax_rate` 所有实例共享

### L2 继承(必修)

- [ ] `Product` 基类 + `PhysicalProduct`(实体,有运费) + `DigitalProduct`(数字,无运费)子类
- [ ] 子类用 `super().__init__()` 继承父类属性
- [ ] 子类**重写** `shipping_cost()`,但复用基类属性

### L3 多态+契约(必修)

- [ ] `Payment(abc.ABC)` 抽象基类,定义 `execute(amount)` 抽象方法
- [ ] 三个子类:`Alipay` / `WeChatPay` / `ApplePay`,各自不同实现
- [ ] **核心函数 `checkout(cart_total, payment)` 体内不出现 if/elif/isinstance/type**
- [ ] 新增支付方式只需**添加一个文件**,不需改 `checkout` 函数

### L4 组合 + Pythonic(必修,L4 新增)

- [ ] `Order` 类**组合**(而非继承)了 `Cart` + `Payment` + `Address`
- [ ] `ShoppingCart.__add__(other)` 合并两辆购物车
- [ ] `ShoppingCart.__len__()` 返回总件数(可用 `len(cart)`)
- [ ] `ShoppingCart.__iter__()` 可用 `for item in cart`
- [ ] `Product.__eq__()` 同款判定(购物车去重用)

## 建议时长

某一天全天(建议日程末期 Day08 之后安排)

## 评分标准

| 项 | 分值 | 覆盖 L |
|---|---|---|
| 基础功能(菜单循环+CRUD+JSON 加载) | 20 | L1 |
| OOP 类拆分合理(封装+继承层级) | 20 | L1+L2 |
| 多态+abc 契约(结账函数无 if-elif) | 15 | L3 |
| 组合+运算符重载(购物车合并+len+iter) | 15 | L4 |
| JSON 持久化 + CSV 导出 | 10 | L1 |
| 异常处理 | 10 | L1 |
| 单元测试通过 | 5 | 全 L |
| README + Demo | 5 | 总计 |

## 给学员的脚手架(教师可以提供)

```python
# === 文件: models/payment.py ===
import abc

class Payment(abc.ABC):
    """支付抽象基类。子类必须实现 execute 方法。"""
    @abc.abstractmethod
    def execute(self, amount: float) -> bool:
        ...

# === 文件: utils/checkout.py ===
# 下面的函数由教师提供给学员,学员不可修改其核心逻辑。
# 学员通过实现正确的 Payment 子类让它跑通。

def checkout(cart_total: float, payment: Payment) -> bool:
    """
    处理一笔支付。
    约束:本函数不使用 if/elif/isinstance/type,
    函数体不超过 5 行。
    """
    if cart_total <= 0:
        print("购物车为空")
        return False
    return payment.execute(cart_total)
```

## 验收测试脚本(教师提供)

```python
# === test_week03.py ===
from models.product import Product, PhysicalProduct, DigitalProduct
from models.payment import Alipay, WeChatPay, ApplePay, Payment
from models.cart import ShoppingCart
from utils.checkout import checkout

def test_l1_encapsulation():
    p = Product("Python 入门", 59.8, stock=100)
    assert p.price == 59.8
    p.price = -10  # 应该被拒绝
    assert p.price == 59.8, "@property 应该阻止负数价格"
    assert "Python 入门" in str(p), "__str__ 应该友好"

def test_l2_inheritance():
    pp = PhysicalProduct("纸质书", 50, weight=0.5)
    dp = DigitalProduct("电子书", 30, file_size="5MB")
    assert pp.shipping_cost() > 0
    assert dp.shipping_cost() == 0

def test_l3_polymorphism():
    payments = [Alipay(), WeChatPay(), ApplePay()]
    for p in payments:
        result = checkout(99.0, p)
        assert result is True or result is False

def test_l4_dunder():
    from models.product import Product
    p1 = Product("同款", 10)
    p2 = Product("同款", 10)
    p3 = Product("不同款", 20)
    cart = ShoppingCart()
    cart.add(p1)
    cart.add(p2)
    cart.add(p3)
    assert len(cart) == 3
    # 同款去重后迭代
    unique = list(cart.unique_products())
    assert len(unique) == 2

if __name__ == '__main__':
    test_l1_encapsulation(); print("✅ L1 封装")
    test_l2_inheritance(); print("✅ L2 继承")
    test_l3_polymorphism(); print("✅ L3 多态")
    test_l4_dunder(); print("✅ L4 组合+运算符")
    print("🎉 全部验收通过")
```

## 旧版参考(图书管理 v1)

旧的图书管理验收标准已归档到 `.versions/week03-v1-backup/`。
