"""
[难度: ⭐⭐⭐]
[所属知识点: 添加商品到购物车(按编号)]
[预计完成时间: 25 分钟]

题目描述:
    实现 add_to_cart(products, cart, product_id, qty),
    将指定商品加入购物车。

    规则:
      - 若购物车已有该商品,数量累加
      - 若不存在,新增一条记录
      - 商品编号不存在时,打印提示并返回

示例:
    >>> products = {1: {"name": "苹果", "price": 5.0}}
    >>> cart = []
    >>> add_to_cart(products, cart, 1, 2)
    >>> print(cart)
    [{'id': 1, 'name': '苹果', 'price': 5.0, 'qty': 2}]
    >>> add_to_cart(products, cart, 1, 3)
    >>> print(cart[0]['qty'])
    5
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================

def add_to_cart(products, cart, product_id, qty):
    """将商品加入购物车"""
    # 1. 检查 product_id 是否存在于 products
    # 2. 遍历 cart 看是否已有该商品
    #    - 有: qty 累加
    #    - 无: 新建字典 append 到 cart
    pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    products = {
        1: {"name": "苹果", "price": 5.0},
        2: {"name": "香蕉", "price": 3.5},
    }
    cart = []
    # 测试 1: 新增商品
    add_to_cart(products, cart, 1, 2)
    print(f"加入后: {cart}")
    # 测试 2: 累加数量
    add_to_cart(products, cart, 1, 3)
    print(f"累加后 qty: {cart[0]['qty']}")
    # 测试 3: 无效编号
    add_to_cart(products, cart, 99, 1)
